# Results vs. 3.12.0

- fork: brandtbucher
- ref: justin_no_externs
- machine: linux-x86_64
- commit hash: 5791853
- commit date: 2024-10-25
- overall geometric mean: 1.023x slower
- HPT reliability: 90.40%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241025-pythonperf2-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-5791853 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 318 ms: 1.12x slower                                                            |
| docutils       | 2.87 sec                                                     | 3.20 sec: 1.12x slower                                                          |
| tornado_http   | 121 ms                                                       | 123 ms: 1.01x slower                                                            |
| Geometric mean | (ref)                                                        | 1.08x slower                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241025-pythonperf2-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-5791853 |
|----------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 540 ms                                                       | 380 ms: 1.42x faster                                                            |
| async_tree_none_tg         | 431 ms                                                       | 324 ms: 1.33x faster                                                            |
| async_tree_none            | 452 ms                                                       | 344 ms: 1.31x faster                                                            |
| async_tree_memoization     | 544 ms                                                       | 415 ms: 1.31x faster                                                            |
| async_tree_io              | 1.04 sec                                                     | 845 ms: 1.23x faster                                                            |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 566 ms: 1.23x faster                                                            |
| async_tree_io_tg           | 1.05 sec                                                     | 874 ms: 1.21x faster                                                            |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 579 ms: 1.20x faster                                                            |
| Geometric mean             | (ref)                                                        | 1.28x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241025-pythonperf2-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-5791853 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 88.0 ms                                                      | 83.3 ms: 1.06x faster                                                           |
| pidigits       | 265 ms                                                       | 252 ms: 1.05x faster                                                            |
| float          | 76.6 ms                                                      | 79.4 ms: 1.04x slower                                                           |
| Geometric mean | (ref)                                                        | 1.02x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241025-pythonperf2-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-5791853 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 144 ms                                                       | 146 ms: 1.02x slower                                                            |
| regex_effbot   | 3.57 ms                                                      | 3.70 ms: 1.03x slower                                                           |
| regex_dna      | 239 ms                                                       | 253 ms: 1.06x slower                                                            |
| regex_v8       | 23.6 ms                                                      | 25.9 ms: 1.10x slower                                                           |
| Geometric mean | (ref)                                                        | 1.05x slower                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241025-pythonperf2-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-5791853 |
|----------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| xml_etree_generate   | 86.1 ms                                                      | 81.2 ms: 1.06x faster                                                           |
| xml_etree_iterparse  | 103 ms                                                       | 99.8 ms: 1.03x faster                                                           |
| tomli_loads          | 2.16 sec                                                     | 2.14 sec: 1.01x faster                                                          |
| json_loads           | 24.4 us                                                      | 24.6 us: 1.01x slower                                                           |
| pickle_pure_python   | 318 us                                                       | 338 us: 1.06x slower                                                            |
| unpickle_pure_python | 210 us                                                       | 225 us: 1.07x slower                                                            |
| json_dumps           | 10.2 ms                                                      | 11.3 ms: 1.10x slower                                                           |
| Geometric mean       | (ref)                                                        | 1.02x slower                                                                    |

Benchmark hidden because not significant (2): xml_etree_parse, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241025-pythonperf2-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-5791853 |
|------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 9.01 ms: 1.04x slower                                                           |
| python_startup         | 11.6 ms                                                      | 14.8 ms: 1.28x slower                                                           |
| Geometric mean         | (ref)                                                        | 1.15x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241025-pythonperf2-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-5791853 |
|-----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 10.0 ms                                                      | 9.65 ms: 1.04x faster                                                           |
| django_template | 38.2 ms                                                      | 44.0 ms: 1.15x slower                                                           |
| Geometric mean  | (ref)                                                        | 1.05x slower                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241025-pythonperf2-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-5791853 |
|----------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 540 ms                                                       | 380 ms: 1.42x faster                                                            |
| async_tree_none_tg         | 431 ms                                                       | 324 ms: 1.33x faster                                                            |
| async_tree_none            | 452 ms                                                       | 344 ms: 1.31x faster                                                            |
| async_tree_memoization     | 544 ms                                                       | 415 ms: 1.31x faster                                                            |
| async_tree_io              | 1.04 sec                                                     | 845 ms: 1.23x faster                                                            |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 566 ms: 1.23x faster                                                            |
| async_tree_io_tg           | 1.05 sec                                                     | 874 ms: 1.21x faster                                                            |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 579 ms: 1.20x faster                                                            |
| deepcopy_memo              | 36.8 us                                                      | 30.8 us: 1.19x faster                                                           |
| pathlib                    | 18.9 ms                                                      | 16.1 ms: 1.17x faster                                                           |
| deepcopy                   | 368 us                                                       | 320 us: 1.15x faster                                                            |
| comprehensions             | 21.9 us                                                      | 19.5 us: 1.12x faster                                                           |
| coroutines                 | 23.0 ms                                                      | 21.2 ms: 1.08x faster                                                           |
| deepcopy_reduce            | 3.37 us                                                      | 3.13 us: 1.08x faster                                                           |
| xml_etree_generate         | 86.1 ms                                                      | 81.2 ms: 1.06x faster                                                           |
| nbody                      | 88.0 ms                                                      | 83.3 ms: 1.06x faster                                                           |
| pidigits                   | 265 ms                                                       | 252 ms: 1.05x faster                                                            |
| dulwich_log                | 65.4 ms                                                      | 62.9 ms: 1.04x faster                                                           |
| crypto_pyaes               | 80.3 ms                                                      | 77.3 ms: 1.04x faster                                                           |
| mako                       | 10.0 ms                                                      | 9.65 ms: 1.04x faster                                                           |
| scimark_fft                | 301 ms                                                       | 292 ms: 1.03x faster                                                            |
| xml_etree_iterparse        | 103 ms                                                       | 99.8 ms: 1.03x faster                                                           |
| scimark_lu                 | 98.8 ms                                                      | 97.0 ms: 1.02x faster                                                           |
| sqlalchemy_imperative      | 18.7 ms                                                      | 18.4 ms: 1.02x faster                                                           |
| async_generators           | 390 ms                                                       | 384 ms: 1.02x faster                                                            |
| pprint_pformat             | 1.65 sec                                                     | 1.63 sec: 1.01x faster                                                          |
| tomli_loads                | 2.16 sec                                                     | 2.14 sec: 1.01x faster                                                          |
| logging_format             | 7.48 us                                                      | 7.44 us: 1.01x faster                                                           |
| pprint_safe_repr           | 807 ms                                                       | 802 ms: 1.01x faster                                                            |
| json_loads                 | 24.4 us                                                      | 24.6 us: 1.01x slower                                                           |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.25 ms: 1.01x slower                                                           |
| logging_simple             | 6.71 us                                                      | 6.80 us: 1.01x slower                                                           |
| tornado_http               | 121 ms                                                       | 123 ms: 1.01x slower                                                            |
| richards                   | 45.7 ms                                                      | 46.5 ms: 1.02x slower                                                           |
| regex_compile              | 144 ms                                                       | 146 ms: 1.02x slower                                                            |
| json                       | 5.12 ms                                                      | 5.21 ms: 1.02x slower                                                           |
| pycparser                  | 1.23 sec                                                     | 1.26 sec: 1.02x slower                                                          |
| mdp                        | 2.57 sec                                                     | 2.65 sec: 1.03x slower                                                          |
| regex_effbot               | 3.57 ms                                                      | 3.70 ms: 1.03x slower                                                           |
| float                      | 76.6 ms                                                      | 79.4 ms: 1.04x slower                                                           |
| spectral_norm              | 91.6 ms                                                      | 94.9 ms: 1.04x slower                                                           |
| deltablue                  | 3.24 ms                                                      | 3.36 ms: 1.04x slower                                                           |
| python_startup_no_site     | 8.64 ms                                                      | 9.01 ms: 1.04x slower                                                           |
| scimark_monte_carlo        | 69.0 ms                                                      | 72.2 ms: 1.05x slower                                                           |
| generators                 | 37.4 ms                                                      | 39.2 ms: 1.05x slower                                                           |
| richards_super             | 51.3 ms                                                      | 54.3 ms: 1.06x slower                                                           |
| sqlalchemy_declarative     | 159 ms                                                       | 169 ms: 1.06x slower                                                            |
| regex_dna                  | 239 ms                                                       | 253 ms: 1.06x slower                                                            |
| sympy_str                  | 302 ms                                                       | 321 ms: 1.06x slower                                                            |
| pickle_pure_python         | 318 us                                                       | 338 us: 1.06x slower                                                            |
| go                         | 150 ms                                                       | 159 ms: 1.07x slower                                                            |
| meteor_contest             | 128 ms                                                       | 137 ms: 1.07x slower                                                            |
| unpickle_pure_python       | 210 us                                                       | 225 us: 1.07x slower                                                            |
| scimark_sor                | 109 ms                                                       | 117 ms: 1.08x slower                                                            |
| sympy_sum                  | 162 ms                                                       | 174 ms: 1.08x slower                                                            |
| chaos                      | 64.0 ms                                                      | 69.4 ms: 1.08x slower                                                           |
| sqlglot_parse              | 1.38 ms                                                      | 1.50 ms: 1.09x slower                                                           |
| raytrace                   | 298 ms                                                       | 324 ms: 1.09x slower                                                            |
| logging_silent             | 94.4 ns                                                      | 103 ns: 1.09x slower                                                            |
| regex_v8                   | 23.6 ms                                                      | 25.9 ms: 1.10x slower                                                           |
| sympy_expand               | 484 ms                                                       | 532 ms: 1.10x slower                                                            |
| json_dumps                 | 10.2 ms                                                      | 11.3 ms: 1.10x slower                                                           |
| sqlglot_transpile          | 1.78 ms                                                      | 1.97 ms: 1.11x slower                                                           |
| fannkuch                   | 350 ms                                                       | 389 ms: 1.11x slower                                                            |
| 2to3                       | 285 ms                                                       | 318 ms: 1.12x slower                                                            |
| docutils                   | 2.87 sec                                                     | 3.20 sec: 1.12x slower                                                          |
| pyflate                    | 439 ms                                                       | 491 ms: 1.12x slower                                                            |
| sympy_integrate            | 23.9 ms                                                      | 27.4 ms: 1.15x slower                                                           |
| django_template            | 38.2 ms                                                      | 44.0 ms: 1.15x slower                                                           |
| telco                      | 6.96 ms                                                      | 8.02 ms: 1.15x slower                                                           |
| sqlglot_normalize          | 116 ms                                                       | 134 ms: 1.16x slower                                                            |
| coverage                   | 66.7 ms                                                      | 78.1 ms: 1.17x slower                                                           |
| nqueens                    | 89.9 ms                                                      | 106 ms: 1.18x slower                                                            |
| sqlglot_optimize           | 57.5 ms                                                      | 69.6 ms: 1.21x slower                                                           |
| hexiom                     | 5.96 ms                                                      | 7.46 ms: 1.25x slower                                                           |
| typing_runtime_protocols   | 152 us                                                       | 190 us: 1.25x slower                                                            |
| python_startup             | 11.6 ms                                                      | 14.8 ms: 1.28x slower                                                           |
| gc_traversal               | 3.48 ms                                                      | 5.53 ms: 1.59x slower                                                           |
| create_gc_cycles           | 1.59 ms                                                      | 2.89 ms: 1.82x slower                                                           |
| bench_mp_pool              | 4.76 ms                                                      | 1.90 sec: 399.34x slower                                                        |
| Geometric mean             | (ref)                                                        | 1.10x slower                                                                    |

Benchmark hidden because not significant (4): asyncio_websockets, xml_etree_parse, xml_etree_process, bench_thread_pool
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (7) of results/bm-20241025-3.14.0a1+-5791853-JIT/bm-20241025-pythonperf2-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-5791853.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift

- Geometric mean (including insignificant results): 1.023x slower
# HPT report

- Reliability score: 90.40% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.10x