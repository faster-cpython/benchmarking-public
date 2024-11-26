# Results vs. 3.12.0

- fork: brandtbucher
- ref: justin_no_externs
- machine: linux-x86_64
- commit hash: 9698931
- commit date: 2024-10-24
- overall geometric mean: 1.077x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x slower
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241024-pythonperf2-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 335 ms: 1.17x slower                                                            |
| docutils       | 2.87 sec                                                     | 3.25 sec: 1.13x slower                                                          |
| tornado_http   | 121 ms                                                       | 123 ms: 1.02x slower                                                            |
| Geometric mean | (ref)                                                        | 1.11x slower                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241024-pythonperf2-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|----------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 540 ms                                                       | 389 ms: 1.39x faster                                                            |
| async_tree_none_tg         | 431 ms                                                       | 333 ms: 1.29x faster                                                            |
| async_tree_memoization     | 544 ms                                                       | 430 ms: 1.26x faster                                                            |
| async_tree_none            | 452 ms                                                       | 358 ms: 1.26x faster                                                            |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 575 ms: 1.21x faster                                                            |
| async_tree_io              | 1.04 sec                                                     | 868 ms: 1.20x faster                                                            |
| async_tree_io_tg           | 1.05 sec                                                     | 878 ms: 1.20x faster                                                            |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 598 ms: 1.16x faster                                                            |
| Geometric mean             | (ref)                                                        | 1.25x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241024-pythonperf2-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pidigits       | 265 ms                                                       | 253 ms: 1.05x faster                                                            |
| float          | 76.6 ms                                                      | 80.3 ms: 1.05x slower                                                           |
| nbody          | 88.0 ms                                                      | 101 ms: 1.15x slower                                                            |
| Geometric mean | (ref)                                                        | 1.05x slower                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241024-pythonperf2-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_effbot   | 3.57 ms                                                      | 3.65 ms: 1.02x slower                                                           |
| regex_dna      | 239 ms                                                       | 246 ms: 1.03x slower                                                            |
| regex_compile  | 144 ms                                                       | 157 ms: 1.09x slower                                                            |
| regex_v8       | 23.6 ms                                                      | 26.3 ms: 1.11x slower                                                           |
| Geometric mean | (ref)                                                        | 1.06x slower                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241024-pythonperf2-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|----------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| xml_etree_iterparse  | 103 ms                                                       | 100 ms: 1.03x faster                                                            |
| xml_etree_parse      | 144 ms                                                       | 146 ms: 1.02x slower                                                            |
| xml_etree_generate   | 86.1 ms                                                      | 87.7 ms: 1.02x slower                                                           |
| json_loads           | 24.4 us                                                      | 25.4 us: 1.04x slower                                                           |
| tomli_loads          | 2.16 sec                                                     | 2.29 sec: 1.06x slower                                                          |
| xml_etree_process    | 58.4 ms                                                      | 64.8 ms: 1.11x slower                                                           |
| unpickle_pure_python | 210 us                                                       | 236 us: 1.13x slower                                                            |
| json_dumps           | 10.2 ms                                                      | 11.8 ms: 1.16x slower                                                           |
| pickle_pure_python   | 318 us                                                       | 375 us: 1.18x slower                                                            |
| Geometric mean       | (ref)                                                        | 1.07x slower                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241024-pythonperf2-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 9.01 ms: 1.04x slower                                                           |
| python_startup         | 11.6 ms                                                      | 14.9 ms: 1.28x slower                                                           |
| Geometric mean         | (ref)                                                        | 1.16x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241024-pythonperf2-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|-----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 10.0 ms                                                      | 10.3 ms: 1.03x slower                                                           |
| django_template | 38.2 ms                                                      | 44.4 ms: 1.16x slower                                                           |
| Geometric mean  | (ref)                                                        | 1.09x slower                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241024-pythonperf2-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|----------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 540 ms                                                       | 389 ms: 1.39x faster                                                            |
| async_tree_none_tg         | 431 ms                                                       | 333 ms: 1.29x faster                                                            |
| async_tree_memoization     | 544 ms                                                       | 430 ms: 1.26x faster                                                            |
| async_tree_none            | 452 ms                                                       | 358 ms: 1.26x faster                                                            |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 575 ms: 1.21x faster                                                            |
| async_tree_io              | 1.04 sec                                                     | 868 ms: 1.20x faster                                                            |
| async_tree_io_tg           | 1.05 sec                                                     | 878 ms: 1.20x faster                                                            |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 598 ms: 1.16x faster                                                            |
| pathlib                    | 18.9 ms                                                      | 16.3 ms: 1.16x faster                                                           |
| deepcopy_memo              | 36.8 us                                                      | 32.3 us: 1.14x faster                                                           |
| coroutines                 | 23.0 ms                                                      | 21.3 ms: 1.08x faster                                                           |
| deepcopy                   | 368 us                                                       | 350 us: 1.05x faster                                                            |
| pidigits                   | 265 ms                                                       | 253 ms: 1.05x faster                                                            |
| xml_etree_iterparse        | 103 ms                                                       | 100 ms: 1.03x faster                                                            |
| logging_format             | 7.48 us                                                      | 7.31 us: 1.02x faster                                                           |
| dulwich_log                | 65.4 ms                                                      | 64.4 ms: 1.01x faster                                                           |
| asyncio_websockets         | 387 ms                                                       | 384 ms: 1.01x faster                                                            |
| tornado_http               | 121 ms                                                       | 123 ms: 1.02x slower                                                            |
| xml_etree_parse            | 144 ms                                                       | 146 ms: 1.02x slower                                                            |
| xml_etree_generate         | 86.1 ms                                                      | 87.7 ms: 1.02x slower                                                           |
| regex_effbot               | 3.57 ms                                                      | 3.65 ms: 1.02x slower                                                           |
| mako                       | 10.0 ms                                                      | 10.3 ms: 1.03x slower                                                           |
| deepcopy_reduce            | 3.37 us                                                      | 3.47 us: 1.03x slower                                                           |
| regex_dna                  | 239 ms                                                       | 246 ms: 1.03x slower                                                            |
| comprehensions             | 21.9 us                                                      | 22.7 us: 1.03x slower                                                           |
| bench_thread_pool          | 950 us                                                       | 984 us: 1.04x slower                                                            |
| mdp                        | 2.57 sec                                                     | 2.67 sec: 1.04x slower                                                          |
| python_startup_no_site     | 8.64 ms                                                      | 9.01 ms: 1.04x slower                                                           |
| json                       | 5.12 ms                                                      | 5.34 ms: 1.04x slower                                                           |
| json_loads                 | 24.4 us                                                      | 25.4 us: 1.04x slower                                                           |
| float                      | 76.6 ms                                                      | 80.3 ms: 1.05x slower                                                           |
| tomli_loads                | 2.16 sec                                                     | 2.29 sec: 1.06x slower                                                          |
| sqlalchemy_declarative     | 159 ms                                                       | 170 ms: 1.07x slower                                                            |
| scimark_fft                | 301 ms                                                       | 324 ms: 1.07x slower                                                            |
| crypto_pyaes               | 80.3 ms                                                      | 86.7 ms: 1.08x slower                                                           |
| spectral_norm              | 91.6 ms                                                      | 100 ms: 1.09x slower                                                            |
| regex_compile              | 144 ms                                                       | 157 ms: 1.09x slower                                                            |
| pycparser                  | 1.23 sec                                                     | 1.36 sec: 1.10x slower                                                          |
| logging_silent             | 94.4 ns                                                      | 104 ns: 1.10x slower                                                            |
| sympy_sum                  | 162 ms                                                       | 179 ms: 1.11x slower                                                            |
| sympy_str                  | 302 ms                                                       | 334 ms: 1.11x slower                                                            |
| deltablue                  | 3.24 ms                                                      | 3.58 ms: 1.11x slower                                                           |
| xml_etree_process          | 58.4 ms                                                      | 64.8 ms: 1.11x slower                                                           |
| regex_v8                   | 23.6 ms                                                      | 26.3 ms: 1.11x slower                                                           |
| raytrace                   | 298 ms                                                       | 335 ms: 1.12x slower                                                            |
| unpickle_pure_python       | 210 us                                                       | 236 us: 1.13x slower                                                            |
| sqlglot_parse              | 1.38 ms                                                      | 1.56 ms: 1.13x slower                                                           |
| docutils                   | 2.87 sec                                                     | 3.25 sec: 1.13x slower                                                          |
| sympy_expand               | 484 ms                                                       | 549 ms: 1.13x slower                                                            |
| scimark_sor                | 109 ms                                                       | 124 ms: 1.14x slower                                                            |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.81 ms: 1.14x slower                                                           |
| nbody                      | 88.0 ms                                                      | 101 ms: 1.15x slower                                                            |
| meteor_contest             | 128 ms                                                       | 148 ms: 1.15x slower                                                            |
| sqlglot_transpile          | 1.78 ms                                                      | 2.05 ms: 1.16x slower                                                           |
| json_dumps                 | 10.2 ms                                                      | 11.8 ms: 1.16x slower                                                           |
| django_template            | 38.2 ms                                                      | 44.4 ms: 1.16x slower                                                           |
| 2to3                       | 285 ms                                                       | 335 ms: 1.17x slower                                                            |
| pickle_pure_python         | 318 us                                                       | 375 us: 1.18x slower                                                            |
| generators                 | 37.4 ms                                                      | 44.3 ms: 1.18x slower                                                           |
| sympy_integrate            | 23.9 ms                                                      | 28.4 ms: 1.19x slower                                                           |
| pprint_safe_repr           | 807 ms                                                       | 967 ms: 1.20x slower                                                            |
| telco                      | 6.96 ms                                                      | 8.37 ms: 1.20x slower                                                           |
| pprint_pformat             | 1.65 sec                                                     | 1.99 sec: 1.20x slower                                                          |
| go                         | 150 ms                                                       | 181 ms: 1.21x slower                                                            |
| coverage                   | 66.7 ms                                                      | 80.8 ms: 1.21x slower                                                           |
| sqlglot_normalize          | 116 ms                                                       | 143 ms: 1.24x slower                                                            |
| pyflate                    | 439 ms                                                       | 548 ms: 1.25x slower                                                            |
| richards_super             | 51.3 ms                                                      | 64.3 ms: 1.25x slower                                                           |
| chaos                      | 64.0 ms                                                      | 80.3 ms: 1.25x slower                                                           |
| scimark_monte_carlo        | 69.0 ms                                                      | 87.4 ms: 1.27x slower                                                           |
| python_startup             | 11.6 ms                                                      | 14.9 ms: 1.28x slower                                                           |
| sqlglot_optimize           | 57.5 ms                                                      | 73.9 ms: 1.29x slower                                                           |
| richards                   | 45.7 ms                                                      | 60.1 ms: 1.31x slower                                                           |
| fannkuch                   | 350 ms                                                       | 461 ms: 1.32x slower                                                            |
| typing_runtime_protocols   | 152 us                                                       | 200 us: 1.32x slower                                                            |
| nqueens                    | 89.9 ms                                                      | 121 ms: 1.35x slower                                                            |
| hexiom                     | 5.96 ms                                                      | 8.92 ms: 1.50x slower                                                           |
| gc_traversal               | 3.48 ms                                                      | 5.36 ms: 1.54x slower                                                           |
| create_gc_cycles           | 1.59 ms                                                      | 2.88 ms: 1.81x slower                                                           |
| bench_mp_pool              | 4.76 ms                                                      | 2.20 sec: 461.58x slower                                                        |
| Geometric mean             | (ref)                                                        | 1.16x slower                                                                    |

Benchmark hidden because not significant (4): sqlalchemy_imperative, scimark_lu, async_generators, logging_simple
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (7) of results/bm-20241024-3.14.0a1+-9698931-JIT/bm-20241024-pythonperf2-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-9698931.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift

- Geometric mean (including insignificant results): 1.077x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.05x
- 95% likely to have a slowdown of 1.05x
- 99% likely to have a slowdown of 1.04x

# Memory
- memory change: 1.10x