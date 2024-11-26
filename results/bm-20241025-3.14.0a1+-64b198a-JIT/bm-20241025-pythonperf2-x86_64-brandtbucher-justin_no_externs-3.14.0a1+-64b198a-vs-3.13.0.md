# Results vs. 3.13.0

- fork: brandtbucher
- ref: justin_no_externs
- machine: linux-x86_64
- commit hash: 64b198a
- commit date: 2024-10-25
- overall geometric mean: 1.022x slower
- HPT reliability: 93.35%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241025-pythonperf2-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 318 ms: 1.09x slower                                                            |
| docutils       | 2.81 sec                                                     | 3.21 sec: 1.14x slower                                                          |
| html5lib       | 72.9 ms                                                      | 71.6 ms: 1.02x faster                                                           |
| sphinx         | 1.11 sec                                                     | 1.28 sec: 1.15x slower                                                          |
| tornado_http   | 119 ms                                                       | 121 ms: 1.02x slower                                                            |
| Geometric mean | (ref)                                                        | 1.07x slower                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241025-pythonperf2-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|----------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 458 ms                                                       | 379 ms: 1.21x faster                                                            |
| async_tree_memoization     | 447 ms                                                       | 416 ms: 1.07x faster                                                            |
| async_tree_none            | 370 ms                                                       | 345 ms: 1.07x faster                                                            |
| async_tree_none_tg         | 342 ms                                                       | 326 ms: 1.05x faster                                                            |
| asyncio_websockets         | 395 ms                                                       | 381 ms: 1.04x faster                                                            |
| async_tree_cpu_io_mixed    | 596 ms                                                       | 582 ms: 1.02x faster                                                            |
| coroutines                 | 21.6 ms                                                      | 21.2 ms: 1.01x faster                                                           |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 568 ms: 1.01x faster                                                            |
| async_tree_io              | 832 ms                                                       | 855 ms: 1.03x slower                                                            |
| async_generators           | 364 ms                                                       | 380 ms: 1.05x slower                                                            |
| async_tree_io_tg           | 823 ms                                                       | 869 ms: 1.06x slower                                                            |
| Geometric mean             | (ref)                                                        | 1.03x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241025-pythonperf2-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 92.1 ms                                                      | 86.1 ms: 1.07x faster                                                           |
| float          | 81.6 ms                                                      | 78.6 ms: 1.04x faster                                                           |
| pidigits       | 252 ms                                                       | 251 ms: 1.00x faster                                                            |
| Geometric mean | (ref)                                                        | 1.04x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241025-pythonperf2-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 143 ms                                                       | 147 ms: 1.03x slower                                                            |
| regex_effbot   | 3.51 ms                                                      | 3.66 ms: 1.04x slower                                                           |
| regex_v8       | 24.9 ms                                                      | 26.1 ms: 1.05x slower                                                           |
| regex_dna      | 238 ms                                                       | 256 ms: 1.08x slower                                                            |
| Geometric mean | (ref)                                                        | 1.05x slower                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241025-pythonperf2-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|----------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 2.43 sec                                                     | 2.18 sec: 1.12x faster                                                          |
| xml_etree_generate   | 85.2 ms                                                      | 81.9 ms: 1.04x faster                                                           |
| xml_etree_parse      | 144 ms                                                       | 146 ms: 1.02x slower                                                            |
| json_dumps           | 10.8 ms                                                      | 11.3 ms: 1.05x slower                                                           |
| unpickle_pure_python | 216 us                                                       | 227 us: 1.05x slower                                                            |
| pickle_pure_python   | 322 us                                                       | 349 us: 1.08x slower                                                            |
| Geometric mean       | (ref)                                                        | 1.00x slower                                                                    |

Benchmark hidden because not significant (3): json_loads, xml_etree_iterparse, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241025-pythonperf2-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 15.6 ms                                                      | 14.9 ms: 1.05x faster                                                           |
| python_startup_no_site | 8.93 ms                                                      | 9.05 ms: 1.01x slower                                                           |
| Geometric mean         | (ref)                                                        | 1.02x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241025-pythonperf2-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|-----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 10.3 ms                                                      | 9.98 ms: 1.03x faster                                                           |
| django_template | 38.9 ms                                                      | 42.2 ms: 1.09x slower                                                           |
| genshi_xml      | 58.0 ms                                                      | 64.4 ms: 1.11x slower                                                           |
| genshi_text     | 27.2 ms                                                      | 30.2 ms: 1.11x slower                                                           |
| Geometric mean  | (ref)                                                        | 1.07x slower                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241025-pythonperf2-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|----------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| deepcopy_memo              | 38.9 us                                                      | 30.3 us: 1.28x faster                                                           |
| deepcopy                   | 388 us                                                       | 317 us: 1.22x faster                                                            |
| async_tree_memoization_tg  | 458 ms                                                       | 379 ms: 1.21x faster                                                            |
| richards_super             | 60.2 ms                                                      | 52.1 ms: 1.16x faster                                                           |
| tomli_loads                | 2.43 sec                                                     | 2.18 sec: 1.12x faster                                                          |
| deepcopy_reduce            | 3.49 us                                                      | 3.17 us: 1.10x faster                                                           |
| telco                      | 8.77 ms                                                      | 7.99 ms: 1.10x faster                                                           |
| json                       | 5.62 ms                                                      | 5.17 ms: 1.09x faster                                                           |
| pathlib                    | 17.4 ms                                                      | 16.1 ms: 1.08x faster                                                           |
| async_tree_memoization     | 447 ms                                                       | 416 ms: 1.07x faster                                                            |
| async_tree_none            | 370 ms                                                       | 345 ms: 1.07x faster                                                            |
| nbody                      | 92.1 ms                                                      | 86.1 ms: 1.07x faster                                                           |
| richards                   | 52.5 ms                                                      | 49.2 ms: 1.07x faster                                                           |
| go                         | 167 ms                                                       | 157 ms: 1.07x faster                                                            |
| python_startup             | 15.6 ms                                                      | 14.9 ms: 1.05x faster                                                           |
| async_tree_none_tg         | 342 ms                                                       | 326 ms: 1.05x faster                                                            |
| dulwich_log                | 65.5 ms                                                      | 62.8 ms: 1.04x faster                                                           |
| scimark_sor                | 125 ms                                                       | 120 ms: 1.04x faster                                                            |
| xml_etree_generate         | 85.2 ms                                                      | 81.9 ms: 1.04x faster                                                           |
| float                      | 81.6 ms                                                      | 78.6 ms: 1.04x faster                                                           |
| asyncio_websockets         | 395 ms                                                       | 381 ms: 1.04x faster                                                            |
| bpe_tokeniser              | 5.09 sec                                                     | 4.92 sec: 1.04x faster                                                          |
| mako                       | 10.3 ms                                                      | 9.98 ms: 1.03x faster                                                           |
| pprint_safe_repr           | 835 ms                                                       | 812 ms: 1.03x faster                                                            |
| pprint_pformat             | 1.70 sec                                                     | 1.66 sec: 1.02x faster                                                          |
| async_tree_cpu_io_mixed    | 596 ms                                                       | 582 ms: 1.02x faster                                                            |
| pycparser                  | 1.28 sec                                                     | 1.26 sec: 1.02x faster                                                          |
| html5lib                   | 72.9 ms                                                      | 71.6 ms: 1.02x faster                                                           |
| coroutines                 | 21.6 ms                                                      | 21.2 ms: 1.01x faster                                                           |
| spectral_norm              | 97.4 ms                                                      | 96.2 ms: 1.01x faster                                                           |
| coverage                   | 84.5 ms                                                      | 83.5 ms: 1.01x faster                                                           |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 568 ms: 1.01x faster                                                            |
| pidigits                   | 252 ms                                                       | 251 ms: 1.00x faster                                                            |
| deltablue                  | 3.38 ms                                                      | 3.41 ms: 1.01x slower                                                           |
| scimark_lu                 | 97.4 ms                                                      | 98.7 ms: 1.01x slower                                                           |
| python_startup_no_site     | 8.93 ms                                                      | 9.05 ms: 1.01x slower                                                           |
| xml_etree_parse            | 144 ms                                                       | 146 ms: 1.02x slower                                                            |
| tornado_http               | 119 ms                                                       | 121 ms: 1.02x slower                                                            |
| sqlalchemy_imperative      | 18.1 ms                                                      | 18.5 ms: 1.02x slower                                                           |
| crypto_pyaes               | 73.5 ms                                                      | 75.1 ms: 1.02x slower                                                           |
| async_tree_io              | 832 ms                                                       | 855 ms: 1.03x slower                                                            |
| logging_silent             | 97.5 ns                                                      | 100 ns: 1.03x slower                                                            |
| regex_compile              | 143 ms                                                       | 147 ms: 1.03x slower                                                            |
| bench_thread_pool          | 929 us                                                       | 961 us: 1.03x slower                                                            |
| meteor_contest             | 130 ms                                                       | 135 ms: 1.04x slower                                                            |
| mdp                        | 2.53 sec                                                     | 2.63 sec: 1.04x slower                                                          |
| regex_effbot               | 3.51 ms                                                      | 3.66 ms: 1.04x slower                                                           |
| json_dumps                 | 10.8 ms                                                      | 11.3 ms: 1.05x slower                                                           |
| async_generators           | 364 ms                                                       | 380 ms: 1.05x slower                                                            |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.41 ms: 1.05x slower                                                           |
| regex_v8                   | 24.9 ms                                                      | 26.1 ms: 1.05x slower                                                           |
| logging_format             | 6.95 us                                                      | 7.30 us: 1.05x slower                                                           |
| unpickle_pure_python       | 216 us                                                       | 227 us: 1.05x slower                                                            |
| sympy_expand               | 506 ms                                                       | 535 ms: 1.06x slower                                                            |
| async_tree_io_tg           | 823 ms                                                       | 869 ms: 1.06x slower                                                            |
| logging_simple             | 6.28 us                                                      | 6.63 us: 1.06x slower                                                           |
| typing_runtime_protocols   | 176 us                                                       | 186 us: 1.06x slower                                                            |
| regex_dna                  | 238 ms                                                       | 256 ms: 1.08x slower                                                            |
| sqlglot_parse              | 1.37 ms                                                      | 1.47 ms: 1.08x slower                                                           |
| pickle_pure_python         | 322 us                                                       | 349 us: 1.08x slower                                                            |
| django_template            | 38.9 ms                                                      | 42.2 ms: 1.09x slower                                                           |
| 2to3                       | 293 ms                                                       | 318 ms: 1.09x slower                                                            |
| sympy_str                  | 297 ms                                                       | 322 ms: 1.09x slower                                                            |
| create_gc_cycles           | 2.65 ms                                                      | 2.88 ms: 1.09x slower                                                           |
| sqlglot_transpile          | 1.76 ms                                                      | 1.95 ms: 1.11x slower                                                           |
| genshi_xml                 | 58.0 ms                                                      | 64.4 ms: 1.11x slower                                                           |
| genshi_text                | 27.2 ms                                                      | 30.2 ms: 1.11x slower                                                           |
| scimark_monte_carlo        | 65.2 ms                                                      | 73.6 ms: 1.13x slower                                                           |
| sqlalchemy_declarative     | 148 ms                                                       | 168 ms: 1.13x slower                                                            |
| chaos                      | 60.6 ms                                                      | 68.6 ms: 1.13x slower                                                           |
| sqlglot_normalize          | 119 ms                                                       | 136 ms: 1.14x slower                                                            |
| docutils                   | 2.81 sec                                                     | 3.21 sec: 1.14x slower                                                          |
| sympy_sum                  | 154 ms                                                       | 176 ms: 1.14x slower                                                            |
| nqueens                    | 92.3 ms                                                      | 106 ms: 1.15x slower                                                            |
| sphinx                     | 1.11 sec                                                     | 1.28 sec: 1.15x slower                                                          |
| comprehensions             | 17.3 us                                                      | 19.9 us: 1.15x slower                                                           |
| hexiom                     | 6.47 ms                                                      | 7.51 ms: 1.16x slower                                                           |
| raytrace                   | 267 ms                                                       | 312 ms: 1.17x slower                                                            |
| sympy_integrate            | 23.4 ms                                                      | 27.6 ms: 1.18x slower                                                           |
| sqlglot_optimize           | 58.7 ms                                                      | 69.9 ms: 1.19x slower                                                           |
| generators                 | 33.9 ms                                                      | 40.6 ms: 1.20x slower                                                           |
| gc_traversal               | 4.48 ms                                                      | 5.51 ms: 1.23x slower                                                           |
| pylint                     | 345 ms                                                       | 424 ms: 1.23x slower                                                            |
| bench_mp_pool              | 4.82 ms                                                      | 1.70 sec: 352.23x slower                                                        |
| Geometric mean             | (ref)                                                        | 1.09x slower                                                                    |

Benchmark hidden because not significant (7): fannkuch, thrift, json_loads, xml_etree_iterparse, scimark_fft, pyflate, xml_etree_process
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path

- Geometric mean (including insignificant results): 1.022x slower
# HPT report

- Reliability score: 93.35% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.07x