# Results vs. 3.13.0

- fork: brandtbucher
- ref: justin_no_externs
- machine: windows-x86
- commit hash: 64b198a
- commit date: 2024-10-25
- overall geometric mean: 1.046x faster
- HPT reliability: 69.76%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241025-pythonperf1_win32-x86-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| 2to3           | 255 ms                                                          | 270 ms: 1.06x slower                                                               |
| docutils       | 1.80 sec                                                        | 2.08 sec: 1.15x slower                                                             |
| html5lib       | 47.1 ms                                                         | 45.9 ms: 1.03x faster                                                              |
| sphinx         | 729 ms                                                          | 860 ms: 1.18x slower                                                               |
| tornado_http   | 105 ms                                                          | 109 ms: 1.04x slower                                                               |
| Geometric mean | (ref)                                                           | 1.08x slower                                                                       |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241025-pythonperf1_win32-x86-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|----------------------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 287 ms                                                          | 252 ms: 1.14x faster                                                               |
| async_tree_none            | 245 ms                                                          | 223 ms: 1.10x faster                                                               |
| async_tree_memoization     | 302 ms                                                          | 281 ms: 1.07x faster                                                               |
| async_tree_none_tg         | 216 ms                                                          | 203 ms: 1.06x faster                                                               |
| async_tree_cpu_io_mixed    | 490 ms                                                          | 470 ms: 1.04x faster                                                               |
| async_tree_cpu_io_mixed_tg | 469 ms                                                          | 465 ms: 1.01x faster                                                               |
| coroutines                 | 16.1 ms                                                         | 17.3 ms: 1.07x slower                                                              |
| async_tree_io_tg           | 499 ms                                                          | 551 ms: 1.10x slower                                                               |
| async_generators           | 267 ms                                                          | 332 ms: 1.24x slower                                                               |
| Geometric mean             | (ref)                                                           | 1.00x faster                                                                       |

Benchmark hidden because not significant (1): async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241025-pythonperf1_win32-x86-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| nbody          | 81.4 ms                                                         | 63.0 ms: 1.29x faster                                                              |
| float          | 56.4 ms                                                         | 49.6 ms: 1.14x faster                                                              |
| pidigits       | 204 ms                                                          | 203 ms: 1.00x faster                                                               |
| Geometric mean | (ref)                                                           | 1.14x faster                                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241025-pythonperf1_win32-x86-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| regex_effbot   | 1.82 ms                                                         | 1.77 ms: 1.03x faster                                                              |
| regex_v8       | 15.5 ms                                                         | 15.9 ms: 1.03x slower                                                              |
| regex_dna      | 112 ms                                                          | 120 ms: 1.07x slower                                                               |
| regex_compile  | 101 ms                                                          | 110 ms: 1.09x slower                                                               |
| Geometric mean | (ref)                                                           | 1.04x slower                                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241025-pythonperf1_win32-x86-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|----------------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| tomli_loads          | 1.74 sec                                                        | 1.59 sec: 1.09x faster                                                             |
| xml_etree_generate   | 61.9 ms                                                         | 58.2 ms: 1.06x faster                                                              |
| json_loads           | 21.7 us                                                         | 21.2 us: 1.02x faster                                                              |
| xml_etree_process    | 44.6 ms                                                         | 45.4 ms: 1.02x slower                                                              |
| pickle_pure_python   | 239 us                                                          | 245 us: 1.02x slower                                                               |
| unpickle_pure_python | 162 us                                                          | 169 us: 1.04x slower                                                               |
| json_dumps           | 7.53 ms                                                         | 7.99 ms: 1.06x slower                                                              |
| xml_etree_parse      | 102 ms                                                          | 111 ms: 1.08x slower                                                               |
| xml_etree_iterparse  | 61.3 ms                                                         | 67.7 ms: 1.10x slower                                                              |
| Geometric mean       | (ref)                                                           | 1.02x slower                                                                       |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241025-pythonperf1_win32-x86-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|------------------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| python_startup         | 28.3 ms                                                         | 26.6 ms: 1.06x faster                                                              |
| python_startup_no_site | 20.2 ms                                                         | 20.3 ms: 1.01x slower                                                              |
| Geometric mean         | (ref)                                                           | 1.03x faster                                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241025-pythonperf1_win32-x86-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|-----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| mako            | 7.02 ms                                                         | 6.44 ms: 1.09x faster                                                              |
| django_template | 32.0 ms                                                         | 33.0 ms: 1.03x slower                                                              |
| genshi_text     | 21.7 ms                                                         | 23.2 ms: 1.07x slower                                                              |
| genshi_xml      | 49.0 ms                                                         | 55.0 ms: 1.12x slower                                                              |
| Geometric mean  | (ref)                                                           | 1.03x slower                                                                       |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241025-pythonperf1_win32-x86-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|----------------------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| thrift                     | 10.3 ms                                                         | 766 us: 13.39x faster                                                              |
| coverage                   | 326 ms                                                          | 53.8 ms: 6.06x faster                                                              |
| sqlglot_normalize          | 223 ms                                                          | 105 ms: 2.12x faster                                                               |
| deepcopy_memo              | 26.2 us                                                         | 18.0 us: 1.45x faster                                                              |
| nbody                      | 81.4 ms                                                         | 63.0 ms: 1.29x faster                                                              |
| deepcopy                   | 311 us                                                          | 245 us: 1.27x faster                                                               |
| deepcopy_reduce            | 2.94 us                                                         | 2.53 us: 1.16x faster                                                              |
| async_tree_memoization_tg  | 287 ms                                                          | 252 ms: 1.14x faster                                                               |
| float                      | 56.4 ms                                                         | 49.6 ms: 1.14x faster                                                              |
| fannkuch                   | 288 ms                                                          | 256 ms: 1.13x faster                                                               |
| scimark_sor                | 85.8 ms                                                         | 76.9 ms: 1.12x faster                                                              |
| go                         | 111 ms                                                          | 101 ms: 1.10x faster                                                               |
| async_tree_none            | 245 ms                                                          | 223 ms: 1.10x faster                                                               |
| tomli_loads                | 1.74 sec                                                        | 1.59 sec: 1.09x faster                                                             |
| pprint_safe_repr           | 658 ms                                                          | 603 ms: 1.09x faster                                                               |
| mako                       | 7.02 ms                                                         | 6.44 ms: 1.09x faster                                                              |
| scimark_sparse_mat_mult    | 2.88 ms                                                         | 2.65 ms: 1.09x faster                                                              |
| pprint_pformat             | 1.32 sec                                                        | 1.23 sec: 1.08x faster                                                             |
| async_tree_memoization     | 302 ms                                                          | 281 ms: 1.07x faster                                                               |
| python_startup             | 28.3 ms                                                         | 26.6 ms: 1.06x faster                                                              |
| async_tree_none_tg         | 216 ms                                                          | 203 ms: 1.06x faster                                                               |
| xml_etree_generate         | 61.9 ms                                                         | 58.2 ms: 1.06x faster                                                              |
| meteor_contest             | 78.1 ms                                                         | 73.6 ms: 1.06x faster                                                              |
| crypto_pyaes               | 56.6 ms                                                         | 54.0 ms: 1.05x faster                                                              |
| scimark_fft                | 204 ms                                                          | 195 ms: 1.05x faster                                                               |
| telco                      | 6.27 ms                                                         | 6.01 ms: 1.04x faster                                                              |
| async_tree_cpu_io_mixed    | 490 ms                                                          | 470 ms: 1.04x faster                                                               |
| spectral_norm              | 70.0 ms                                                         | 67.5 ms: 1.04x faster                                                              |
| pycparser                  | 869 ms                                                          | 845 ms: 1.03x faster                                                               |
| regex_effbot               | 1.82 ms                                                         | 1.77 ms: 1.03x faster                                                              |
| html5lib                   | 47.1 ms                                                         | 45.9 ms: 1.03x faster                                                              |
| json_loads                 | 21.7 us                                                         | 21.2 us: 1.02x faster                                                              |
| logging_format             | 8.59 us                                                         | 8.45 us: 1.02x faster                                                              |
| logging_simple             | 7.89 us                                                         | 7.78 us: 1.01x faster                                                              |
| pathlib                    | 89.1 ms                                                         | 87.8 ms: 1.01x faster                                                              |
| async_tree_cpu_io_mixed_tg | 469 ms                                                          | 465 ms: 1.01x faster                                                               |
| pidigits                   | 204 ms                                                          | 203 ms: 1.00x faster                                                               |
| bench_mp_pool              | 93.6 ms                                                         | 94.4 ms: 1.01x slower                                                              |
| python_startup_no_site     | 20.2 ms                                                         | 20.3 ms: 1.01x slower                                                              |
| typing_runtime_protocols   | 141 us                                                          | 143 us: 1.02x slower                                                               |
| xml_etree_process          | 44.6 ms                                                         | 45.4 ms: 1.02x slower                                                              |
| sqlglot_parse              | 1.02 ms                                                         | 1.04 ms: 1.02x slower                                                              |
| pickle_pure_python         | 239 us                                                          | 245 us: 1.02x slower                                                               |
| gc_traversal               | 1.76 ms                                                         | 1.81 ms: 1.03x slower                                                              |
| pyflate                    | 322 ms                                                          | 330 ms: 1.03x slower                                                               |
| django_template            | 32.0 ms                                                         | 33.0 ms: 1.03x slower                                                              |
| regex_v8                   | 15.5 ms                                                         | 15.9 ms: 1.03x slower                                                              |
| mdp                        | 1.70 sec                                                        | 1.76 sec: 1.04x slower                                                             |
| tornado_http               | 105 ms                                                          | 109 ms: 1.04x slower                                                               |
| logging_silent             | 62.4 ns                                                         | 64.9 ns: 1.04x slower                                                              |
| unpickle_pure_python       | 162 us                                                          | 169 us: 1.04x slower                                                               |
| 2to3                       | 255 ms                                                          | 270 ms: 1.06x slower                                                               |
| json_dumps                 | 7.53 ms                                                         | 7.99 ms: 1.06x slower                                                              |
| genshi_text                | 21.7 ms                                                         | 23.2 ms: 1.07x slower                                                              |
| regex_dna                  | 112 ms                                                          | 120 ms: 1.07x slower                                                               |
| scimark_lu                 | 60.7 ms                                                         | 65.2 ms: 1.07x slower                                                              |
| coroutines                 | 16.1 ms                                                         | 17.3 ms: 1.07x slower                                                              |
| richards                   | 33.4 ms                                                         | 35.9 ms: 1.08x slower                                                              |
| sympy_expand               | 377 ms                                                          | 406 ms: 1.08x slower                                                               |
| comprehensions             | 13.1 us                                                         | 14.2 us: 1.08x slower                                                              |
| sqlglot_transpile          | 1.26 ms                                                         | 1.36 ms: 1.08x slower                                                              |
| xml_etree_parse            | 102 ms                                                          | 111 ms: 1.08x slower                                                               |
| regex_compile              | 101 ms                                                          | 110 ms: 1.09x slower                                                               |
| create_gc_cycles           | 1.08 ms                                                         | 1.18 ms: 1.09x slower                                                              |
| sympy_str                  | 214 ms                                                          | 236 ms: 1.10x slower                                                               |
| sympy_sum                  | 108 ms                                                          | 119 ms: 1.10x slower                                                               |
| async_tree_io_tg           | 499 ms                                                          | 551 ms: 1.10x slower                                                               |
| xml_etree_iterparse        | 61.3 ms                                                         | 67.7 ms: 1.10x slower                                                              |
| richards_super             | 37.0 ms                                                         | 41.0 ms: 1.11x slower                                                              |
| nqueens                    | 75.1 ms                                                         | 83.7 ms: 1.11x slower                                                              |
| json                       | 4.40 ms                                                         | 4.93 ms: 1.12x slower                                                              |
| genshi_xml                 | 49.0 ms                                                         | 55.0 ms: 1.12x slower                                                              |
| chaos                      | 49.4 ms                                                         | 55.8 ms: 1.13x slower                                                              |
| docutils                   | 1.80 sec                                                        | 2.08 sec: 1.15x slower                                                             |
| deltablue                  | 2.35 ms                                                         | 2.73 ms: 1.16x slower                                                              |
| sphinx                     | 729 ms                                                          | 860 ms: 1.18x slower                                                               |
| sympy_integrate            | 15.2 ms                                                         | 18.0 ms: 1.18x slower                                                              |
| generators                 | 21.5 ms                                                         | 25.5 ms: 1.19x slower                                                              |
| sqlglot_optimize           | 42.4 ms                                                         | 50.8 ms: 1.20x slower                                                              |
| async_generators           | 267 ms                                                          | 332 ms: 1.24x slower                                                               |
| raytrace                   | 203 ms                                                          | 256 ms: 1.26x slower                                                               |
| pylint                     | 225 ms                                                          | 288 ms: 1.28x slower                                                               |
| hexiom                     | 4.60 ms                                                         | 5.94 ms: 1.29x slower                                                              |
| Geometric mean             | (ref)                                                           | 1.04x faster                                                                       |

Benchmark hidden because not significant (4): bench_thread_pool, scimark_monte_carlo, async_tree_io, dulwich_log
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: asyncio_websockets, bpe_tokeniser, chameleon, connected_components, gevent_hub, k_core, shortest_path, sqlalchemy_declarative, sqlalchemy_imperative

- Geometric mean (including insignificant results): 1.046x faster
# HPT report

- Reliability score: 69.76% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown