# Results vs. 3.13.0

- fork: brandtbucher
- ref: justin_no_externs
- machine: windows-x86
- commit hash: 5791853
- commit date: 2024-10-25
- overall geometric mean: 1.045x faster
- HPT reliability: 84.76%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241025-pythonperf1_win32-x86-brandtbucher-justin_no_externs-3.14.0a1+-5791853 |
|----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| 2to3           | 255 ms                                                          | 267 ms: 1.05x slower                                                               |
| docutils       | 1.80 sec                                                        | 2.05 sec: 1.14x slower                                                             |
| html5lib       | 47.1 ms                                                         | 46.9 ms: 1.00x faster                                                              |
| sphinx         | 729 ms                                                          | 851 ms: 1.17x slower                                                               |
| tornado_http   | 105 ms                                                          | 110 ms: 1.05x slower                                                               |
| Geometric mean | (ref)                                                           | 1.08x slower                                                                       |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241025-pythonperf1_win32-x86-brandtbucher-justin_no_externs-3.14.0a1+-5791853 |
|----------------------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 287 ms                                                          | 252 ms: 1.14x faster                                                               |
| async_tree_none            | 245 ms                                                          | 218 ms: 1.12x faster                                                               |
| async_tree_memoization     | 302 ms                                                          | 276 ms: 1.09x faster                                                               |
| async_tree_none_tg         | 216 ms                                                          | 203 ms: 1.06x faster                                                               |
| async_tree_cpu_io_mixed    | 490 ms                                                          | 465 ms: 1.05x faster                                                               |
| async_tree_io              | 530 ms                                                          | 521 ms: 1.02x faster                                                               |
| async_tree_cpu_io_mixed_tg | 469 ms                                                          | 462 ms: 1.01x faster                                                               |
| coroutines                 | 16.1 ms                                                         | 17.5 ms: 1.08x slower                                                              |
| async_tree_io_tg           | 499 ms                                                          | 552 ms: 1.10x slower                                                               |
| async_generators           | 267 ms                                                          | 320 ms: 1.20x slower                                                               |
| Geometric mean             | (ref)                                                           | 1.01x faster                                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241025-pythonperf1_win32-x86-brandtbucher-justin_no_externs-3.14.0a1+-5791853 |
|----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| nbody          | 81.4 ms                                                         | 67.2 ms: 1.21x faster                                                              |
| float          | 56.4 ms                                                         | 49.7 ms: 1.14x faster                                                              |
| pidigits       | 204 ms                                                          | 207 ms: 1.02x slower                                                               |
| Geometric mean | (ref)                                                           | 1.11x faster                                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241025-pythonperf1_win32-x86-brandtbucher-justin_no_externs-3.14.0a1+-5791853 |
|----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| regex_effbot   | 1.82 ms                                                         | 1.80 ms: 1.01x faster                                                              |
| regex_v8       | 15.5 ms                                                         | 15.9 ms: 1.03x slower                                                              |
| regex_dna      | 112 ms                                                          | 120 ms: 1.07x slower                                                               |
| regex_compile  | 101 ms                                                          | 108 ms: 1.07x slower                                                               |
| Geometric mean | (ref)                                                           | 1.04x slower                                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241025-pythonperf1_win32-x86-brandtbucher-justin_no_externs-3.14.0a1+-5791853 |
|----------------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| tomli_loads          | 1.74 sec                                                        | 1.56 sec: 1.12x faster                                                             |
| json_loads           | 21.7 us                                                         | 20.9 us: 1.03x faster                                                              |
| xml_etree_generate   | 61.9 ms                                                         | 60.5 ms: 1.02x faster                                                              |
| pickle_pure_python   | 239 us                                                          | 244 us: 1.02x slower                                                               |
| unpickle_pure_python | 162 us                                                          | 166 us: 1.03x slower                                                               |
| xml_etree_process    | 44.6 ms                                                         | 47.2 ms: 1.06x slower                                                              |
| json_dumps           | 7.53 ms                                                         | 8.11 ms: 1.08x slower                                                              |
| xml_etree_iterparse  | 61.3 ms                                                         | 66.6 ms: 1.09x slower                                                              |
| xml_etree_parse      | 102 ms                                                          | 112 ms: 1.10x slower                                                               |
| Geometric mean       | (ref)                                                           | 1.02x slower                                                                       |

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241025-pythonperf1_win32-x86-brandtbucher-justin_no_externs-3.14.0a1+-5791853 |
|----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| python_startup | 28.3 ms                                                         | 26.9 ms: 1.05x faster                                                              |
| Geometric mean | (ref)                                                           | 1.03x faster                                                                       |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241025-pythonperf1_win32-x86-brandtbucher-justin_no_externs-3.14.0a1+-5791853 |
|-----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| mako            | 7.02 ms                                                         | 6.29 ms: 1.12x faster                                                              |
| django_template | 32.0 ms                                                         | 32.4 ms: 1.01x slower                                                              |
| genshi_text     | 21.7 ms                                                         | 23.2 ms: 1.07x slower                                                              |
| genshi_xml      | 49.0 ms                                                         | 56.3 ms: 1.15x slower                                                              |
| Geometric mean  | (ref)                                                           | 1.03x slower                                                                       |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241025-pythonperf1_win32-x86-brandtbucher-justin_no_externs-3.14.0a1+-5791853 |
|----------------------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| thrift                     | 10.3 ms                                                         | 767 us: 13.38x faster                                                              |
| coverage                   | 326 ms                                                          | 52.0 ms: 6.28x faster                                                              |
| sqlglot_normalize          | 223 ms                                                          | 102 ms: 2.18x faster                                                               |
| deepcopy_memo              | 26.2 us                                                         | 18.0 us: 1.46x faster                                                              |
| deepcopy                   | 311 us                                                          | 244 us: 1.27x faster                                                               |
| nbody                      | 81.4 ms                                                         | 67.2 ms: 1.21x faster                                                              |
| deepcopy_reduce            | 2.94 us                                                         | 2.50 us: 1.18x faster                                                              |
| async_tree_memoization_tg  | 287 ms                                                          | 252 ms: 1.14x faster                                                               |
| float                      | 56.4 ms                                                         | 49.7 ms: 1.14x faster                                                              |
| async_tree_none            | 245 ms                                                          | 218 ms: 1.12x faster                                                               |
| mako                       | 7.02 ms                                                         | 6.29 ms: 1.12x faster                                                              |
| tomli_loads                | 1.74 sec                                                        | 1.56 sec: 1.12x faster                                                             |
| go                         | 111 ms                                                          | 99.8 ms: 1.11x faster                                                              |
| scimark_sor                | 85.8 ms                                                         | 78.0 ms: 1.10x faster                                                              |
| pprint_safe_repr           | 658 ms                                                          | 602 ms: 1.09x faster                                                               |
| async_tree_memoization     | 302 ms                                                          | 276 ms: 1.09x faster                                                               |
| scimark_monte_carlo        | 48.7 ms                                                         | 45.2 ms: 1.08x faster                                                              |
| pprint_pformat             | 1.32 sec                                                        | 1.23 sec: 1.07x faster                                                             |
| async_tree_none_tg         | 216 ms                                                          | 203 ms: 1.06x faster                                                               |
| pycparser                  | 869 ms                                                          | 823 ms: 1.06x faster                                                               |
| scimark_sparse_mat_mult    | 2.88 ms                                                         | 2.73 ms: 1.05x faster                                                              |
| async_tree_cpu_io_mixed    | 490 ms                                                          | 465 ms: 1.05x faster                                                               |
| python_startup             | 28.3 ms                                                         | 26.9 ms: 1.05x faster                                                              |
| crypto_pyaes               | 56.6 ms                                                         | 54.6 ms: 1.04x faster                                                              |
| meteor_contest             | 78.1 ms                                                         | 75.3 ms: 1.04x faster                                                              |
| json_loads                 | 21.7 us                                                         | 20.9 us: 1.03x faster                                                              |
| bench_thread_pool          | 1.04 ms                                                         | 1.01 ms: 1.03x faster                                                              |
| logging_simple             | 7.89 us                                                         | 7.70 us: 1.02x faster                                                              |
| xml_etree_generate         | 61.9 ms                                                         | 60.5 ms: 1.02x faster                                                              |
| logging_format             | 8.59 us                                                         | 8.40 us: 1.02x faster                                                              |
| spectral_norm              | 70.0 ms                                                         | 68.5 ms: 1.02x faster                                                              |
| telco                      | 6.27 ms                                                         | 6.14 ms: 1.02x faster                                                              |
| async_tree_io              | 530 ms                                                          | 521 ms: 1.02x faster                                                               |
| async_tree_cpu_io_mixed_tg | 469 ms                                                          | 462 ms: 1.01x faster                                                               |
| pathlib                    | 89.1 ms                                                         | 87.9 ms: 1.01x faster                                                              |
| fannkuch                   | 288 ms                                                          | 286 ms: 1.01x faster                                                               |
| regex_effbot               | 1.82 ms                                                         | 1.80 ms: 1.01x faster                                                              |
| html5lib                   | 47.1 ms                                                         | 46.9 ms: 1.00x faster                                                              |
| bench_mp_pool              | 93.6 ms                                                         | 94.4 ms: 1.01x slower                                                              |
| scimark_fft                | 204 ms                                                          | 206 ms: 1.01x slower                                                               |
| django_template            | 32.0 ms                                                         | 32.4 ms: 1.01x slower                                                              |
| pidigits                   | 204 ms                                                          | 207 ms: 1.02x slower                                                               |
| logging_silent             | 62.4 ns                                                         | 63.6 ns: 1.02x slower                                                              |
| pickle_pure_python         | 239 us                                                          | 244 us: 1.02x slower                                                               |
| regex_v8                   | 15.5 ms                                                         | 15.9 ms: 1.03x slower                                                              |
| unpickle_pure_python       | 162 us                                                          | 166 us: 1.03x slower                                                               |
| gc_traversal               | 1.76 ms                                                         | 1.82 ms: 1.03x slower                                                              |
| mdp                        | 1.70 sec                                                        | 1.75 sec: 1.03x slower                                                             |
| sqlglot_parse              | 1.02 ms                                                         | 1.06 ms: 1.03x slower                                                              |
| pyflate                    | 322 ms                                                          | 335 ms: 1.04x slower                                                               |
| 2to3                       | 255 ms                                                          | 267 ms: 1.05x slower                                                               |
| tornado_http               | 105 ms                                                          | 110 ms: 1.05x slower                                                               |
| xml_etree_process          | 44.6 ms                                                         | 47.2 ms: 1.06x slower                                                              |
| sympy_expand               | 377 ms                                                          | 400 ms: 1.06x slower                                                               |
| richards                   | 33.4 ms                                                         | 35.4 ms: 1.06x slower                                                              |
| regex_dna                  | 112 ms                                                          | 120 ms: 1.07x slower                                                               |
| genshi_text                | 21.7 ms                                                         | 23.2 ms: 1.07x slower                                                              |
| comprehensions             | 13.1 us                                                         | 14.0 us: 1.07x slower                                                              |
| nqueens                    | 75.1 ms                                                         | 80.3 ms: 1.07x slower                                                              |
| regex_compile              | 101 ms                                                          | 108 ms: 1.07x slower                                                               |
| json_dumps                 | 7.53 ms                                                         | 8.11 ms: 1.08x slower                                                              |
| richards_super             | 37.0 ms                                                         | 40.0 ms: 1.08x slower                                                              |
| sympy_str                  | 214 ms                                                          | 232 ms: 1.08x slower                                                               |
| coroutines                 | 16.1 ms                                                         | 17.5 ms: 1.08x slower                                                              |
| json                       | 4.40 ms                                                         | 4.77 ms: 1.09x slower                                                              |
| xml_etree_iterparse        | 61.3 ms                                                         | 66.6 ms: 1.09x slower                                                              |
| sqlglot_transpile          | 1.26 ms                                                         | 1.37 ms: 1.09x slower                                                              |
| sympy_sum                  | 108 ms                                                          | 118 ms: 1.09x slower                                                               |
| xml_etree_parse            | 102 ms                                                          | 112 ms: 1.10x slower                                                               |
| create_gc_cycles           | 1.08 ms                                                         | 1.19 ms: 1.10x slower                                                              |
| async_tree_io_tg           | 499 ms                                                          | 552 ms: 1.10x slower                                                               |
| scimark_lu                 | 60.7 ms                                                         | 68.9 ms: 1.13x slower                                                              |
| docutils                   | 1.80 sec                                                        | 2.05 sec: 1.14x slower                                                             |
| genshi_xml                 | 49.0 ms                                                         | 56.3 ms: 1.15x slower                                                              |
| deltablue                  | 2.35 ms                                                         | 2.71 ms: 1.15x slower                                                              |
| sphinx                     | 729 ms                                                          | 851 ms: 1.17x slower                                                               |
| sympy_integrate            | 15.2 ms                                                         | 18.1 ms: 1.19x slower                                                              |
| sqlglot_optimize           | 42.4 ms                                                         | 50.3 ms: 1.19x slower                                                              |
| chaos                      | 49.4 ms                                                         | 59.1 ms: 1.20x slower                                                              |
| async_generators           | 267 ms                                                          | 320 ms: 1.20x slower                                                               |
| raytrace                   | 203 ms                                                          | 250 ms: 1.23x slower                                                               |
| generators                 | 21.5 ms                                                         | 26.6 ms: 1.24x slower                                                              |
| pylint                     | 225 ms                                                          | 285 ms: 1.27x slower                                                               |
| hexiom                     | 4.60 ms                                                         | 5.90 ms: 1.28x slower                                                              |
| Geometric mean             | (ref)                                                           | 1.04x faster                                                                       |

Benchmark hidden because not significant (3): python_startup_no_site, dulwich_log, typing_runtime_protocols
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: asyncio_websockets, bpe_tokeniser, chameleon, connected_components, gevent_hub, k_core, shortest_path, sqlalchemy_declarative, sqlalchemy_imperative

- Geometric mean (including insignificant results): 1.045x faster
# HPT report

- Reliability score: 84.76% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown