# Results vs. 3.13.0

- fork: brandtbucher
- ref: justin_no_externs
- machine: linux-x86_64
- commit hash: 9698931
- commit date: 2024-10-24
- overall geometric mean: 1.074x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x slower
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241024-pythonperf2-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 335 ms: 1.14x slower                                                            |
| docutils       | 2.81 sec                                                     | 3.25 sec: 1.16x slower                                                          |
| html5lib       | 72.9 ms                                                      | 73.9 ms: 1.01x slower                                                           |
| sphinx         | 1.11 sec                                                     | 1.30 sec: 1.17x slower                                                          |
| tornado_http   | 119 ms                                                       | 123 ms: 1.04x slower                                                            |
| Geometric mean | (ref)                                                        | 1.10x slower                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241024-pythonperf2-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|---------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_memoization_tg | 458 ms                                                       | 389 ms: 1.18x faster                                                            |
| async_tree_memoization    | 447 ms                                                       | 430 ms: 1.04x faster                                                            |
| async_tree_none           | 370 ms                                                       | 358 ms: 1.03x faster                                                            |
| asyncio_websockets        | 395 ms                                                       | 384 ms: 1.03x faster                                                            |
| async_tree_none_tg        | 342 ms                                                       | 333 ms: 1.03x faster                                                            |
| coroutines                | 21.6 ms                                                      | 21.3 ms: 1.01x faster                                                           |
| async_tree_io             | 832 ms                                                       | 868 ms: 1.04x slower                                                            |
| async_tree_io_tg          | 823 ms                                                       | 878 ms: 1.07x slower                                                            |
| async_generators          | 364 ms                                                       | 390 ms: 1.07x slower                                                            |
| Geometric mean            | (ref)                                                        | 1.01x faster                                                                    |

Benchmark hidden because not significant (2): async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241024-pythonperf2-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 81.6 ms                                                      | 80.3 ms: 1.02x faster                                                           |
| nbody          | 92.1 ms                                                      | 101 ms: 1.10x slower                                                            |
| Geometric mean | (ref)                                                        | 1.03x slower                                                                    |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241024-pythonperf2-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_dna      | 238 ms                                                       | 246 ms: 1.03x slower                                                            |
| regex_effbot   | 3.51 ms                                                      | 3.65 ms: 1.04x slower                                                           |
| regex_v8       | 24.9 ms                                                      | 26.3 ms: 1.06x slower                                                           |
| regex_compile  | 143 ms                                                       | 157 ms: 1.10x slower                                                            |
| Geometric mean | (ref)                                                        | 1.06x slower                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241024-pythonperf2-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|----------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 2.43 sec                                                     | 2.29 sec: 1.06x faster                                                          |
| xml_etree_iterparse  | 99.8 ms                                                      | 100 ms: 1.00x slower                                                            |
| xml_etree_parse      | 144 ms                                                       | 146 ms: 1.02x slower                                                            |
| xml_etree_generate   | 85.2 ms                                                      | 87.7 ms: 1.03x slower                                                           |
| json_loads           | 24.7 us                                                      | 25.4 us: 1.03x slower                                                           |
| xml_etree_process    | 60.7 ms                                                      | 64.8 ms: 1.07x slower                                                           |
| unpickle_pure_python | 216 us                                                       | 236 us: 1.09x slower                                                            |
| json_dumps           | 10.8 ms                                                      | 11.8 ms: 1.09x slower                                                           |
| pickle_pure_python   | 322 us                                                       | 375 us: 1.16x slower                                                            |
| Geometric mean       | (ref)                                                        | 1.05x slower                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241024-pythonperf2-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 15.6 ms                                                      | 14.9 ms: 1.05x faster                                                           |
| python_startup_no_site | 8.93 ms                                                      | 9.01 ms: 1.01x slower                                                           |
| Geometric mean         | (ref)                                                        | 1.02x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241024-pythonperf2-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|-----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| django_template | 38.9 ms                                                      | 44.4 ms: 1.14x slower                                                           |
| genshi_xml      | 58.0 ms                                                      | 68.3 ms: 1.18x slower                                                           |
| genshi_text     | 27.2 ms                                                      | 32.6 ms: 1.20x slower                                                           |
| Geometric mean  | (ref)                                                        | 1.13x slower                                                                    |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                 | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241024-pythonperf2-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|---------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| deepcopy_memo             | 38.9 us                                                      | 32.3 us: 1.20x faster                                                           |
| async_tree_memoization_tg | 458 ms                                                       | 389 ms: 1.18x faster                                                            |
| deepcopy                  | 388 us                                                       | 350 us: 1.11x faster                                                            |
| pathlib                   | 17.4 ms                                                      | 16.3 ms: 1.07x faster                                                           |
| tomli_loads               | 2.43 sec                                                     | 2.29 sec: 1.06x faster                                                          |
| json                      | 5.62 ms                                                      | 5.34 ms: 1.05x faster                                                           |
| python_startup            | 15.6 ms                                                      | 14.9 ms: 1.05x faster                                                           |
| telco                     | 8.77 ms                                                      | 8.37 ms: 1.05x faster                                                           |
| coverage                  | 84.5 ms                                                      | 80.8 ms: 1.05x faster                                                           |
| async_tree_memoization    | 447 ms                                                       | 430 ms: 1.04x faster                                                            |
| async_tree_none           | 370 ms                                                       | 358 ms: 1.03x faster                                                            |
| asyncio_websockets        | 395 ms                                                       | 384 ms: 1.03x faster                                                            |
| async_tree_none_tg        | 342 ms                                                       | 333 ms: 1.03x faster                                                            |
| dulwich_log               | 65.5 ms                                                      | 64.4 ms: 1.02x faster                                                           |
| float                     | 81.6 ms                                                      | 80.3 ms: 1.02x faster                                                           |
| coroutines                | 21.6 ms                                                      | 21.3 ms: 1.01x faster                                                           |
| deepcopy_reduce           | 3.49 us                                                      | 3.47 us: 1.01x faster                                                           |
| xml_etree_iterparse       | 99.8 ms                                                      | 100 ms: 1.00x slower                                                            |
| thrift                    | 918 us                                                       | 925 us: 1.01x slower                                                            |
| python_startup_no_site    | 8.93 ms                                                      | 9.01 ms: 1.01x slower                                                           |
| scimark_lu                | 97.4 ms                                                      | 98.3 ms: 1.01x slower                                                           |
| html5lib                  | 72.9 ms                                                      | 73.9 ms: 1.01x slower                                                           |
| bpe_tokeniser             | 5.09 sec                                                     | 5.17 sec: 1.01x slower                                                          |
| xml_etree_parse           | 144 ms                                                       | 146 ms: 1.02x slower                                                            |
| spectral_norm             | 97.4 ms                                                      | 100 ms: 1.03x slower                                                            |
| xml_etree_generate        | 85.2 ms                                                      | 87.7 ms: 1.03x slower                                                           |
| sqlalchemy_imperative     | 18.1 ms                                                      | 18.7 ms: 1.03x slower                                                           |
| json_loads                | 24.7 us                                                      | 25.4 us: 1.03x slower                                                           |
| regex_dna                 | 238 ms                                                       | 246 ms: 1.03x slower                                                            |
| tornado_http              | 119 ms                                                       | 123 ms: 1.04x slower                                                            |
| regex_effbot              | 3.51 ms                                                      | 3.65 ms: 1.04x slower                                                           |
| async_tree_io             | 832 ms                                                       | 868 ms: 1.04x slower                                                            |
| logging_format            | 6.95 us                                                      | 7.31 us: 1.05x slower                                                           |
| regex_v8                  | 24.9 ms                                                      | 26.3 ms: 1.06x slower                                                           |
| mdp                       | 2.53 sec                                                     | 2.67 sec: 1.06x slower                                                          |
| deltablue                 | 3.38 ms                                                      | 3.58 ms: 1.06x slower                                                           |
| bench_thread_pool         | 929 us                                                       | 984 us: 1.06x slower                                                            |
| pycparser                 | 1.28 sec                                                     | 1.36 sec: 1.06x slower                                                          |
| async_tree_io_tg          | 823 ms                                                       | 878 ms: 1.07x slower                                                            |
| xml_etree_process         | 60.7 ms                                                      | 64.8 ms: 1.07x slower                                                           |
| richards_super            | 60.2 ms                                                      | 64.3 ms: 1.07x slower                                                           |
| logging_silent            | 97.5 ns                                                      | 104 ns: 1.07x slower                                                            |
| logging_simple            | 6.28 us                                                      | 6.72 us: 1.07x slower                                                           |
| async_generators          | 364 ms                                                       | 390 ms: 1.07x slower                                                            |
| sympy_expand              | 506 ms                                                       | 549 ms: 1.08x slower                                                            |
| go                        | 167 ms                                                       | 181 ms: 1.09x slower                                                            |
| scimark_fft               | 298 ms                                                       | 324 ms: 1.09x slower                                                            |
| create_gc_cycles          | 2.65 ms                                                      | 2.88 ms: 1.09x slower                                                           |
| unpickle_pure_python      | 216 us                                                       | 236 us: 1.09x slower                                                            |
| json_dumps                | 10.8 ms                                                      | 11.8 ms: 1.09x slower                                                           |
| nbody                     | 92.1 ms                                                      | 101 ms: 1.10x slower                                                            |
| regex_compile             | 143 ms                                                       | 157 ms: 1.10x slower                                                            |
| pyflate                   | 493 ms                                                       | 548 ms: 1.11x slower                                                            |
| sympy_str                 | 297 ms                                                       | 334 ms: 1.13x slower                                                            |
| meteor_contest            | 130 ms                                                       | 148 ms: 1.13x slower                                                            |
| typing_runtime_protocols  | 176 us                                                       | 200 us: 1.14x slower                                                            |
| sqlglot_parse             | 1.37 ms                                                      | 1.56 ms: 1.14x slower                                                           |
| django_template           | 38.9 ms                                                      | 44.4 ms: 1.14x slower                                                           |
| scimark_sparse_mat_mult   | 4.21 ms                                                      | 4.81 ms: 1.14x slower                                                           |
| 2to3                      | 293 ms                                                       | 335 ms: 1.14x slower                                                            |
| richards                  | 52.5 ms                                                      | 60.1 ms: 1.14x slower                                                           |
| sqlalchemy_declarative    | 148 ms                                                       | 170 ms: 1.15x slower                                                            |
| docutils                  | 2.81 sec                                                     | 3.25 sec: 1.16x slower                                                          |
| pprint_safe_repr          | 835 ms                                                       | 967 ms: 1.16x slower                                                            |
| pickle_pure_python        | 322 us                                                       | 375 us: 1.16x slower                                                            |
| sympy_sum                 | 154 ms                                                       | 179 ms: 1.17x slower                                                            |
| sqlglot_transpile         | 1.76 ms                                                      | 2.05 ms: 1.17x slower                                                           |
| pprint_pformat            | 1.70 sec                                                     | 1.99 sec: 1.17x slower                                                          |
| sphinx                    | 1.11 sec                                                     | 1.30 sec: 1.17x slower                                                          |
| genshi_xml                | 58.0 ms                                                      | 68.3 ms: 1.18x slower                                                           |
| crypto_pyaes              | 73.5 ms                                                      | 86.7 ms: 1.18x slower                                                           |
| gc_traversal              | 4.48 ms                                                      | 5.36 ms: 1.20x slower                                                           |
| genshi_text               | 27.2 ms                                                      | 32.6 ms: 1.20x slower                                                           |
| fannkuch                  | 384 ms                                                       | 461 ms: 1.20x slower                                                            |
| sqlglot_normalize         | 119 ms                                                       | 143 ms: 1.20x slower                                                            |
| sympy_integrate           | 23.4 ms                                                      | 28.4 ms: 1.21x slower                                                           |
| pylint                    | 345 ms                                                       | 431 ms: 1.25x slower                                                            |
| raytrace                  | 267 ms                                                       | 335 ms: 1.25x slower                                                            |
| sqlglot_optimize          | 58.7 ms                                                      | 73.9 ms: 1.26x slower                                                           |
| generators                | 33.9 ms                                                      | 44.3 ms: 1.31x slower                                                           |
| comprehensions            | 17.3 us                                                      | 22.7 us: 1.31x slower                                                           |
| nqueens                   | 92.3 ms                                                      | 121 ms: 1.32x slower                                                            |
| chaos                     | 60.6 ms                                                      | 80.3 ms: 1.33x slower                                                           |
| scimark_monte_carlo       | 65.2 ms                                                      | 87.4 ms: 1.34x slower                                                           |
| hexiom                    | 6.47 ms                                                      | 8.92 ms: 1.38x slower                                                           |
| bench_mp_pool             | 4.82 ms                                                      | 2.20 sec: 456.42x slower                                                        |
| Geometric mean            | (ref)                                                        | 1.15x slower                                                                    |

Benchmark hidden because not significant (5): scimark_sor, mako, pidigits, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path

- Geometric mean (including insignificant results): 1.074x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.06x
- 95% likely to have a slowdown of 1.05x
- 99% likely to have a slowdown of 1.04x

# Memory
- memory change: 1.07x