# Results vs. 3.13.0

- fork: python
- ref: v3.13.0a1
- machine: linux-x86_64
- commit hash: ad056f0
- commit date: 2023-10-13
- overall geometric mean: 1.031x slower
- HPT reliability: 99.98%
- HPT 99th percentile: 1.01x slower
- Memory change: 0.85x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20231013-pythonperf2-x86_64-python-v3.13.0a1-3.13.0a1-ad056f0 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 297 ms: 1.02x slower                                             |
| chameleon      | 7.49 ms                                                      | 7.78 ms: 1.04x slower                                            |
| docutils       | 2.81 sec                                                     | 2.88 sec: 1.03x slower                                           |
| tornado_http   | 119 ms                                                       | 121 ms: 1.02x slower                                             |
| Geometric mean | (ref)                                                        | 1.02x slower                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20231013-pythonperf2-x86_64-python-v3.13.0a1-3.13.0a1-ad056f0 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| asyncio_websockets         | 395 ms                                                       | 389 ms: 1.02x faster                                             |
| coroutines                 | 21.6 ms                                                      | 22.6 ms: 1.05x slower                                            |
| async_generators           | 364 ms                                                       | 399 ms: 1.10x slower                                             |
| async_tree_none            | 370 ms                                                       | 439 ms: 1.19x slower                                             |
| async_tree_cpu_io_mixed    | 596 ms                                                       | 713 ms: 1.20x slower                                             |
| async_tree_memoization     | 447 ms                                                       | 557 ms: 1.25x slower                                             |
| async_tree_memoization_tg  | 458 ms                                                       | 571 ms: 1.25x slower                                             |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 727 ms: 1.27x slower                                             |
| async_tree_none_tg         | 342 ms                                                       | 447 ms: 1.31x slower                                             |
| async_tree_io              | 832 ms                                                       | 1.09 sec: 1.31x slower                                           |
| async_tree_io_tg           | 823 ms                                                       | 1.11 sec: 1.35x slower                                           |
| Geometric mean             | (ref)                                                        | 1.20x slower                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20231013-pythonperf2-x86_64-python-v3.13.0a1-3.13.0a1-ad056f0 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| nbody          | 92.1 ms                                                      | 87.7 ms: 1.05x faster                                            |
| pidigits       | 252 ms                                                       | 264 ms: 1.05x slower                                             |
| Geometric mean | (ref)                                                        | 1.00x faster                                                     |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20231013-pythonperf2-x86_64-python-v3.13.0a1-3.13.0a1-ad056f0 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_dna      | 238 ms                                                       | 241 ms: 1.01x slower                                             |
| regex_effbot   | 3.51 ms                                                      | 3.55 ms: 1.01x slower                                            |
| regex_v8       | 24.9 ms                                                      | 26.2 ms: 1.05x slower                                            |
| regex_compile  | 143 ms                                                       | 150 ms: 1.05x slower                                             |
| Geometric mean | (ref)                                                        | 1.03x slower                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20231013-pythonperf2-x86_64-python-v3.13.0a1-3.13.0a1-ad056f0 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| tomli_loads          | 2.43 sec                                                     | 2.24 sec: 1.09x faster                                           |
| pickle_pure_python   | 322 us                                                       | 314 us: 1.02x faster                                             |
| json_dumps           | 10.8 ms                                                      | 10.6 ms: 1.02x faster                                            |
| json_loads           | 24.7 us                                                      | 24.3 us: 1.02x faster                                            |
| xml_etree_process    | 60.7 ms                                                      | 59.9 ms: 1.01x faster                                            |
| unpickle_pure_python | 216 us                                                       | 220 us: 1.02x slower                                             |
| xml_etree_generate   | 85.2 ms                                                      | 87.3 ms: 1.02x slower                                            |
| xml_etree_parse      | 144 ms                                                       | 152 ms: 1.06x slower                                             |
| xml_etree_iterparse  | 99.8 ms                                                      | 110 ms: 1.11x slower                                             |
| Geometric mean       | (ref)                                                        | 1.00x slower                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20231013-pythonperf2-x86_64-python-v3.13.0a1-3.13.0a1-ad056f0 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup         | 15.6 ms                                                      | 12.6 ms: 1.24x faster                                            |
| python_startup_no_site | 8.93 ms                                                      | 8.70 ms: 1.03x faster                                            |
| Geometric mean         | (ref)                                                        | 1.13x faster                                                     |

Benchmarks with tag 'template':
===============================

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20231013-pythonperf2-x86_64-python-v3.13.0a1-3.13.0a1-ad056f0 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| create_gc_cycles           | 2.65 ms                                                      | 1.58 ms: 1.68x faster                                            |
| python_startup             | 15.6 ms                                                      | 12.6 ms: 1.24x faster                                            |
| typing_runtime_protocols   | 176 us                                                       | 155 us: 1.14x faster                                             |
| gc_traversal               | 4.48 ms                                                      | 3.95 ms: 1.13x faster                                            |
| json                       | 5.62 ms                                                      | 5.12 ms: 1.10x faster                                            |
| tomli_loads                | 2.43 sec                                                     | 2.24 sec: 1.09x faster                                           |
| telco                      | 8.77 ms                                                      | 8.25 ms: 1.06x faster                                            |
| spectral_norm              | 97.4 ms                                                      | 92.3 ms: 1.06x faster                                            |
| nbody                      | 92.1 ms                                                      | 87.7 ms: 1.05x faster                                            |
| nqueens                    | 92.3 ms                                                      | 89.2 ms: 1.03x faster                                            |
| deepcopy_reduce            | 3.49 us                                                      | 3.39 us: 1.03x faster                                            |
| python_startup_no_site     | 8.93 ms                                                      | 8.70 ms: 1.03x faster                                            |
| deepcopy                   | 388 us                                                       | 379 us: 1.03x faster                                             |
| sympy_expand               | 506 ms                                                       | 494 ms: 1.02x faster                                             |
| pickle_pure_python         | 322 us                                                       | 314 us: 1.02x faster                                             |
| json_dumps                 | 10.8 ms                                                      | 10.6 ms: 1.02x faster                                            |
| sqlglot_normalize          | 119 ms                                                       | 117 ms: 1.02x faster                                             |
| json_loads                 | 24.7 us                                                      | 24.3 us: 1.02x faster                                            |
| asyncio_websockets         | 395 ms                                                       | 389 ms: 1.02x faster                                             |
| xml_etree_process          | 60.7 ms                                                      | 59.9 ms: 1.01x faster                                            |
| coverage                   | 84.5 ms                                                      | 83.6 ms: 1.01x faster                                            |
| pprint_pformat             | 1.70 sec                                                     | 1.68 sec: 1.01x faster                                           |
| deepcopy_memo              | 38.9 us                                                      | 38.6 us: 1.01x faster                                            |
| pprint_safe_repr           | 835 ms                                                       | 829 ms: 1.01x faster                                             |
| mdp                        | 2.53 sec                                                     | 2.52 sec: 1.00x faster                                           |
| sqlglot_optimize           | 58.7 ms                                                      | 58.8 ms: 1.00x slower                                            |
| meteor_contest             | 130 ms                                                       | 131 ms: 1.00x slower                                             |
| logging_silent             | 97.5 ns                                                      | 98.3 ns: 1.01x slower                                            |
| regex_dna                  | 238 ms                                                       | 241 ms: 1.01x slower                                             |
| regex_effbot               | 3.51 ms                                                      | 3.55 ms: 1.01x slower                                            |
| hexiom                     | 6.47 ms                                                      | 6.54 ms: 1.01x slower                                            |
| 2to3                       | 293 ms                                                       | 297 ms: 1.02x slower                                             |
| unpickle_pure_python       | 216 us                                                       | 220 us: 1.02x slower                                             |
| tornado_http               | 119 ms                                                       | 121 ms: 1.02x slower                                             |
| xml_etree_generate         | 85.2 ms                                                      | 87.3 ms: 1.02x slower                                            |
| richards_super             | 60.2 ms                                                      | 61.7 ms: 1.02x slower                                            |
| docutils                   | 2.81 sec                                                     | 2.88 sec: 1.03x slower                                           |
| fannkuch                   | 384 ms                                                       | 396 ms: 1.03x slower                                             |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.34 ms: 1.03x slower                                            |
| go                         | 167 ms                                                       | 172 ms: 1.03x slower                                             |
| raytrace                   | 267 ms                                                       | 276 ms: 1.03x slower                                             |
| bench_thread_pool          | 929 us                                                       | 961 us: 1.03x slower                                             |
| sympy_str                  | 297 ms                                                       | 307 ms: 1.03x slower                                             |
| sympy_integrate            | 23.4 ms                                                      | 24.2 ms: 1.03x slower                                            |
| chaos                      | 60.6 ms                                                      | 62.7 ms: 1.04x slower                                            |
| chameleon                  | 7.49 ms                                                      | 7.78 ms: 1.04x slower                                            |
| sqlglot_transpile          | 1.76 ms                                                      | 1.83 ms: 1.04x slower                                            |
| pycparser                  | 1.28 sec                                                     | 1.33 sec: 1.04x slower                                           |
| pyflate                    | 493 ms                                                       | 513 ms: 1.04x slower                                             |
| sqlglot_parse              | 1.37 ms                                                      | 1.42 ms: 1.04x slower                                            |
| generators                 | 33.9 ms                                                      | 35.4 ms: 1.04x slower                                            |
| pidigits                   | 252 ms                                                       | 264 ms: 1.05x slower                                             |
| coroutines                 | 21.6 ms                                                      | 22.6 ms: 1.05x slower                                            |
| sympy_sum                  | 154 ms                                                       | 161 ms: 1.05x slower                                             |
| regex_v8                   | 24.9 ms                                                      | 26.2 ms: 1.05x slower                                            |
| regex_compile              | 143 ms                                                       | 150 ms: 1.05x slower                                             |
| scimark_lu                 | 97.4 ms                                                      | 103 ms: 1.05x slower                                             |
| richards                   | 52.5 ms                                                      | 55.4 ms: 1.06x slower                                            |
| dulwich_log                | 65.5 ms                                                      | 69.2 ms: 1.06x slower                                            |
| scimark_fft                | 298 ms                                                       | 315 ms: 1.06x slower                                             |
| xml_etree_parse            | 144 ms                                                       | 152 ms: 1.06x slower                                             |
| logging_format             | 6.95 us                                                      | 7.44 us: 1.07x slower                                            |
| deltablue                  | 3.38 ms                                                      | 3.66 ms: 1.08x slower                                            |
| logging_simple             | 6.28 us                                                      | 6.79 us: 1.08x slower                                            |
| scimark_monte_carlo        | 65.2 ms                                                      | 71.0 ms: 1.09x slower                                            |
| async_generators           | 364 ms                                                       | 399 ms: 1.10x slower                                             |
| xml_etree_iterparse        | 99.8 ms                                                      | 110 ms: 1.11x slower                                             |
| pathlib                    | 17.4 ms                                                      | 19.3 ms: 1.11x slower                                            |
| async_tree_none            | 370 ms                                                       | 439 ms: 1.19x slower                                             |
| scimark_sor                | 125 ms                                                       | 149 ms: 1.19x slower                                             |
| async_tree_cpu_io_mixed    | 596 ms                                                       | 713 ms: 1.20x slower                                             |
| async_tree_memoization     | 447 ms                                                       | 557 ms: 1.25x slower                                             |
| comprehensions             | 17.3 us                                                      | 21.5 us: 1.25x slower                                            |
| async_tree_memoization_tg  | 458 ms                                                       | 571 ms: 1.25x slower                                             |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 727 ms: 1.27x slower                                             |
| async_tree_none_tg         | 342 ms                                                       | 447 ms: 1.31x slower                                             |
| async_tree_io              | 832 ms                                                       | 1.09 sec: 1.31x slower                                           |
| async_tree_io_tg           | 823 ms                                                       | 1.11 sec: 1.35x slower                                           |
| Geometric mean             | (ref)                                                        | 1.03x slower                                                     |

Benchmark hidden because not significant (4): bench_mp_pool, crypto_pyaes, float, mako
Ignored benchmarks (15) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: bpe_tokeniser, connected_components, django_template, genshi_text, genshi_xml, gevent_hub, html5lib, k_core, mypy2, pylint, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, thrift
Ignored benchmarks (9) of results/bm-20231013-3.13.0a1-ad056f0/bm-20231013-pythonperf2-x86_64-python-v3.13.0a1-3.13.0a1-ad056f0.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.031x slower
# HPT report

- Reliability score: 99.98% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: 0.85x