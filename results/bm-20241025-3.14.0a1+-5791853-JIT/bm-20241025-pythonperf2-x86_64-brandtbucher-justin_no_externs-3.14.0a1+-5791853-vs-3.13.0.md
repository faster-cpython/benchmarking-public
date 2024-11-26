# Results vs. 3.13.0

- fork: brandtbucher
- ref: justin_no_externs
- machine: linux-x86_64
- commit hash: 5791853
- commit date: 2024-10-25
- overall geometric mean: 1.021x slower
- HPT reliability: 84.81%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241025-pythonperf2-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-5791853 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 318 ms: 1.09x slower                                                            |
| docutils       | 2.81 sec                                                     | 3.20 sec: 1.14x slower                                                          |
| html5lib       | 72.9 ms                                                      | 71.2 ms: 1.02x faster                                                           |
| sphinx         | 1.11 sec                                                     | 1.27 sec: 1.14x slower                                                          |
| tornado_http   | 119 ms                                                       | 123 ms: 1.03x slower                                                            |
| Geometric mean | (ref)                                                        | 1.07x slower                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241025-pythonperf2-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-5791853 |
|----------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 458 ms                                                       | 380 ms: 1.21x faster                                                            |
| async_tree_memoization     | 447 ms                                                       | 415 ms: 1.08x faster                                                            |
| async_tree_none            | 370 ms                                                       | 344 ms: 1.08x faster                                                            |
| async_tree_none_tg         | 342 ms                                                       | 324 ms: 1.06x faster                                                            |
| async_tree_cpu_io_mixed    | 596 ms                                                       | 579 ms: 1.03x faster                                                            |
| asyncio_websockets         | 395 ms                                                       | 385 ms: 1.03x faster                                                            |
| coroutines                 | 21.6 ms                                                      | 21.2 ms: 1.02x faster                                                           |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 566 ms: 1.01x faster                                                            |
| async_tree_io              | 832 ms                                                       | 845 ms: 1.02x slower                                                            |
| async_generators           | 364 ms                                                       | 384 ms: 1.06x slower                                                            |
| async_tree_io_tg           | 823 ms                                                       | 874 ms: 1.06x slower                                                            |
| Geometric mean             | (ref)                                                        | 1.03x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241025-pythonperf2-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-5791853 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 92.1 ms                                                      | 83.3 ms: 1.11x faster                                                           |
| float          | 81.6 ms                                                      | 79.4 ms: 1.03x faster                                                           |
| pidigits       | 252 ms                                                       | 252 ms: 1.00x faster                                                            |
| Geometric mean | (ref)                                                        | 1.04x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241025-pythonperf2-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-5791853 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 143 ms                                                       | 146 ms: 1.03x slower                                                            |
| regex_v8       | 24.9 ms                                                      | 25.9 ms: 1.04x slower                                                           |
| regex_effbot   | 3.51 ms                                                      | 3.70 ms: 1.05x slower                                                           |
| regex_dna      | 238 ms                                                       | 253 ms: 1.06x slower                                                            |
| Geometric mean | (ref)                                                        | 1.04x slower                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241025-pythonperf2-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-5791853 |
|----------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 2.43 sec                                                     | 2.14 sec: 1.14x faster                                                          |
| xml_etree_generate   | 85.2 ms                                                      | 81.2 ms: 1.05x faster                                                           |
| xml_etree_process    | 60.7 ms                                                      | 58.7 ms: 1.03x faster                                                           |
| json_loads           | 24.7 us                                                      | 24.6 us: 1.01x faster                                                           |
| unpickle_pure_python | 216 us                                                       | 225 us: 1.04x slower                                                            |
| json_dumps           | 10.8 ms                                                      | 11.3 ms: 1.04x slower                                                           |
| pickle_pure_python   | 322 us                                                       | 338 us: 1.05x slower                                                            |
| Geometric mean       | (ref)                                                        | 1.01x faster                                                                    |

Benchmark hidden because not significant (2): xml_etree_iterparse, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241025-pythonperf2-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-5791853 |
|------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 15.6 ms                                                      | 14.8 ms: 1.05x faster                                                           |
| python_startup_no_site | 8.93 ms                                                      | 9.01 ms: 1.01x slower                                                           |
| Geometric mean         | (ref)                                                        | 1.02x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241025-pythonperf2-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-5791853 |
|-----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 10.3 ms                                                      | 9.65 ms: 1.07x faster                                                           |
| django_template | 38.9 ms                                                      | 44.0 ms: 1.13x slower                                                           |
| genshi_text     | 27.2 ms                                                      | 30.8 ms: 1.13x slower                                                           |
| genshi_xml      | 58.0 ms                                                      | 65.8 ms: 1.13x slower                                                           |
| Geometric mean  | (ref)                                                        | 1.08x slower                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241025-pythonperf2-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-5791853 |
|----------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| deepcopy_memo              | 38.9 us                                                      | 30.8 us: 1.26x faster                                                           |
| deepcopy                   | 388 us                                                       | 320 us: 1.21x faster                                                            |
| async_tree_memoization_tg  | 458 ms                                                       | 380 ms: 1.21x faster                                                            |
| tomli_loads                | 2.43 sec                                                     | 2.14 sec: 1.14x faster                                                          |
| richards                   | 52.5 ms                                                      | 46.5 ms: 1.13x faster                                                           |
| deepcopy_reduce            | 3.49 us                                                      | 3.13 us: 1.12x faster                                                           |
| richards_super             | 60.2 ms                                                      | 54.3 ms: 1.11x faster                                                           |
| nbody                      | 92.1 ms                                                      | 83.3 ms: 1.11x faster                                                           |
| telco                      | 8.77 ms                                                      | 8.02 ms: 1.09x faster                                                           |
| coverage                   | 84.5 ms                                                      | 78.1 ms: 1.08x faster                                                           |
| pathlib                    | 17.4 ms                                                      | 16.1 ms: 1.08x faster                                                           |
| json                       | 5.62 ms                                                      | 5.21 ms: 1.08x faster                                                           |
| async_tree_memoization     | 447 ms                                                       | 415 ms: 1.08x faster                                                            |
| async_tree_none            | 370 ms                                                       | 344 ms: 1.08x faster                                                            |
| mako                       | 10.3 ms                                                      | 9.65 ms: 1.07x faster                                                           |
| scimark_sor                | 125 ms                                                       | 117 ms: 1.07x faster                                                            |
| async_tree_none_tg         | 342 ms                                                       | 324 ms: 1.06x faster                                                            |
| python_startup             | 15.6 ms                                                      | 14.8 ms: 1.05x faster                                                           |
| xml_etree_generate         | 85.2 ms                                                      | 81.2 ms: 1.05x faster                                                           |
| go                         | 167 ms                                                       | 159 ms: 1.05x faster                                                            |
| bpe_tokeniser              | 5.09 sec                                                     | 4.87 sec: 1.04x faster                                                          |
| dulwich_log                | 65.5 ms                                                      | 62.9 ms: 1.04x faster                                                           |
| pprint_pformat             | 1.70 sec                                                     | 1.63 sec: 1.04x faster                                                          |
| pprint_safe_repr           | 835 ms                                                       | 802 ms: 1.04x faster                                                            |
| xml_etree_process          | 60.7 ms                                                      | 58.7 ms: 1.03x faster                                                           |
| async_tree_cpu_io_mixed    | 596 ms                                                       | 579 ms: 1.03x faster                                                            |
| float                      | 81.6 ms                                                      | 79.4 ms: 1.03x faster                                                           |
| spectral_norm              | 97.4 ms                                                      | 94.9 ms: 1.03x faster                                                           |
| asyncio_websockets         | 395 ms                                                       | 385 ms: 1.03x faster                                                            |
| html5lib                   | 72.9 ms                                                      | 71.2 ms: 1.02x faster                                                           |
| scimark_fft                | 298 ms                                                       | 292 ms: 1.02x faster                                                            |
| coroutines                 | 21.6 ms                                                      | 21.2 ms: 1.02x faster                                                           |
| pycparser                  | 1.28 sec                                                     | 1.26 sec: 1.02x faster                                                          |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 566 ms: 1.01x faster                                                            |
| deltablue                  | 3.38 ms                                                      | 3.36 ms: 1.01x faster                                                           |
| json_loads                 | 24.7 us                                                      | 24.6 us: 1.01x faster                                                           |
| scimark_lu                 | 97.4 ms                                                      | 97.0 ms: 1.00x faster                                                           |
| pyflate                    | 493 ms                                                       | 491 ms: 1.00x faster                                                            |
| pidigits                   | 252 ms                                                       | 252 ms: 1.00x faster                                                            |
| python_startup_no_site     | 8.93 ms                                                      | 9.01 ms: 1.01x slower                                                           |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.25 ms: 1.01x slower                                                           |
| thrift                     | 918 us                                                       | 930 us: 1.01x slower                                                            |
| async_tree_io              | 832 ms                                                       | 845 ms: 1.02x slower                                                            |
| sqlalchemy_imperative      | 18.1 ms                                                      | 18.4 ms: 1.02x slower                                                           |
| regex_compile              | 143 ms                                                       | 146 ms: 1.03x slower                                                            |
| bench_thread_pool          | 929 us                                                       | 956 us: 1.03x slower                                                            |
| tornado_http               | 119 ms                                                       | 123 ms: 1.03x slower                                                            |
| unpickle_pure_python       | 216 us                                                       | 225 us: 1.04x slower                                                            |
| regex_v8                   | 24.9 ms                                                      | 25.9 ms: 1.04x slower                                                           |
| json_dumps                 | 10.8 ms                                                      | 11.3 ms: 1.04x slower                                                           |
| mdp                        | 2.53 sec                                                     | 2.65 sec: 1.05x slower                                                          |
| pickle_pure_python         | 322 us                                                       | 338 us: 1.05x slower                                                            |
| sympy_expand               | 506 ms                                                       | 532 ms: 1.05x slower                                                            |
| crypto_pyaes               | 73.5 ms                                                      | 77.3 ms: 1.05x slower                                                           |
| regex_effbot               | 3.51 ms                                                      | 3.70 ms: 1.05x slower                                                           |
| meteor_contest             | 130 ms                                                       | 137 ms: 1.05x slower                                                            |
| logging_silent             | 97.5 ns                                                      | 103 ns: 1.05x slower                                                            |
| async_generators           | 364 ms                                                       | 384 ms: 1.06x slower                                                            |
| regex_dna                  | 238 ms                                                       | 253 ms: 1.06x slower                                                            |
| async_tree_io_tg           | 823 ms                                                       | 874 ms: 1.06x slower                                                            |
| logging_format             | 6.95 us                                                      | 7.44 us: 1.07x slower                                                           |
| sympy_str                  | 297 ms                                                       | 321 ms: 1.08x slower                                                            |
| typing_runtime_protocols   | 176 us                                                       | 190 us: 1.08x slower                                                            |
| logging_simple             | 6.28 us                                                      | 6.80 us: 1.08x slower                                                           |
| 2to3                       | 293 ms                                                       | 318 ms: 1.09x slower                                                            |
| create_gc_cycles           | 2.65 ms                                                      | 2.89 ms: 1.09x slower                                                           |
| sqlglot_parse              | 1.37 ms                                                      | 1.50 ms: 1.09x slower                                                           |
| scimark_monte_carlo        | 65.2 ms                                                      | 72.2 ms: 1.11x slower                                                           |
| sqlglot_transpile          | 1.76 ms                                                      | 1.97 ms: 1.12x slower                                                           |
| sqlglot_normalize          | 119 ms                                                       | 134 ms: 1.13x slower                                                            |
| comprehensions             | 17.3 us                                                      | 19.5 us: 1.13x slower                                                           |
| django_template            | 38.9 ms                                                      | 44.0 ms: 1.13x slower                                                           |
| genshi_text                | 27.2 ms                                                      | 30.8 ms: 1.13x slower                                                           |
| genshi_xml                 | 58.0 ms                                                      | 65.8 ms: 1.13x slower                                                           |
| sympy_sum                  | 154 ms                                                       | 174 ms: 1.13x slower                                                            |
| sqlalchemy_declarative     | 148 ms                                                       | 169 ms: 1.14x slower                                                            |
| docutils                   | 2.81 sec                                                     | 3.20 sec: 1.14x slower                                                          |
| sphinx                     | 1.11 sec                                                     | 1.27 sec: 1.14x slower                                                          |
| chaos                      | 60.6 ms                                                      | 69.4 ms: 1.14x slower                                                           |
| nqueens                    | 92.3 ms                                                      | 106 ms: 1.15x slower                                                            |
| hexiom                     | 6.47 ms                                                      | 7.46 ms: 1.15x slower                                                           |
| generators                 | 33.9 ms                                                      | 39.2 ms: 1.16x slower                                                           |
| sympy_integrate            | 23.4 ms                                                      | 27.4 ms: 1.17x slower                                                           |
| sqlglot_optimize           | 58.7 ms                                                      | 69.6 ms: 1.19x slower                                                           |
| raytrace                   | 267 ms                                                       | 324 ms: 1.21x slower                                                            |
| gc_traversal               | 4.48 ms                                                      | 5.53 ms: 1.23x slower                                                           |
| pylint                     | 345 ms                                                       | 426 ms: 1.23x slower                                                            |
| bench_mp_pool              | 4.82 ms                                                      | 1.90 sec: 394.88x slower                                                        |
| Geometric mean             | (ref)                                                        | 1.09x slower                                                                    |

Benchmark hidden because not significant (3): xml_etree_iterparse, xml_etree_parse, fannkuch
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path

- Geometric mean (including insignificant results): 1.021x slower
# HPT report

- Reliability score: 84.81% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.07x