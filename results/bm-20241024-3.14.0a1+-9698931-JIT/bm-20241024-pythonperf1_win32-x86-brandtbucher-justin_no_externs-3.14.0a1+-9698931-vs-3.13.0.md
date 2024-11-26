# Results vs. 3.13.0

- fork: brandtbucher
- ref: justin_no_externs
- machine: windows-x86
- commit hash: 9698931
- commit date: 2024-10-24
- overall geometric mean: 1.007x faster
- HPT reliability: 99.95%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241024-pythonperf1_win32-x86-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| 2to3           | 255 ms                                                          | 274 ms: 1.08x slower                                                               |
| docutils       | 1.80 sec                                                        | 2.10 sec: 1.17x slower                                                             |
| html5lib       | 47.1 ms                                                         | 48.7 ms: 1.03x slower                                                              |
| sphinx         | 729 ms                                                          | 870 ms: 1.19x slower                                                               |
| tornado_http   | 105 ms                                                          | 110 ms: 1.05x slower                                                               |
| Geometric mean | (ref)                                                           | 1.10x slower                                                                       |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241024-pythonperf1_win32-x86-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|---------------------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| async_tree_memoization_tg | 287 ms                                                          | 264 ms: 1.09x faster                                                               |
| async_tree_none           | 245 ms                                                          | 228 ms: 1.07x faster                                                               |
| async_tree_memoization    | 302 ms                                                          | 287 ms: 1.05x faster                                                               |
| async_tree_cpu_io_mixed   | 490 ms                                                          | 474 ms: 1.03x faster                                                               |
| async_tree_none_tg        | 216 ms                                                          | 212 ms: 1.02x faster                                                               |
| async_tree_io             | 530 ms                                                          | 540 ms: 1.02x slower                                                               |
| coroutines                | 16.1 ms                                                         | 17.9 ms: 1.11x slower                                                              |
| async_tree_io_tg          | 499 ms                                                          | 559 ms: 1.12x slower                                                               |
| async_generators          | 267 ms                                                          | 326 ms: 1.22x slower                                                               |
| Geometric mean            | (ref)                                                           | 1.02x slower                                                                       |

Benchmark hidden because not significant (1): async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241024-pythonperf1_win32-x86-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| nbody          | 81.4 ms                                                         | 70.3 ms: 1.16x faster                                                              |
| float          | 56.4 ms                                                         | 52.2 ms: 1.08x faster                                                              |
| pidigits       | 204 ms                                                          | 207 ms: 1.02x slower                                                               |
| Geometric mean | (ref)                                                           | 1.07x faster                                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241024-pythonperf1_win32-x86-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| regex_effbot   | 1.82 ms                                                         | 1.79 ms: 1.02x faster                                                              |
| regex_v8       | 15.5 ms                                                         | 15.7 ms: 1.02x slower                                                              |
| regex_dna      | 112 ms                                                          | 119 ms: 1.06x slower                                                               |
| regex_compile  | 101 ms                                                          | 113 ms: 1.12x slower                                                               |
| Geometric mean | (ref)                                                           | 1.04x slower                                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241024-pythonperf1_win32-x86-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|----------------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| tomli_loads          | 1.74 sec                                                        | 1.64 sec: 1.06x faster                                                             |
| xml_etree_generate   | 61.9 ms                                                         | 63.8 ms: 1.03x slower                                                              |
| xml_etree_process    | 44.6 ms                                                         | 47.7 ms: 1.07x slower                                                              |
| unpickle_pure_python | 162 us                                                          | 173 us: 1.07x slower                                                               |
| pickle_pure_python   | 239 us                                                          | 258 us: 1.08x slower                                                               |
| xml_etree_parse      | 102 ms                                                          | 113 ms: 1.10x slower                                                               |
| xml_etree_iterparse  | 61.3 ms                                                         | 68.2 ms: 1.11x slower                                                              |
| json_dumps           | 7.53 ms                                                         | 8.50 ms: 1.13x slower                                                              |
| Geometric mean       | (ref)                                                           | 1.06x slower                                                                       |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241024-pythonperf1_win32-x86-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| python_startup | 28.3 ms                                                         | 26.4 ms: 1.07x faster                                                              |
| Geometric mean | (ref)                                                           | 1.04x faster                                                                       |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241024-pythonperf1_win32-x86-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|-----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| mako            | 7.02 ms                                                         | 6.83 ms: 1.03x faster                                                              |
| django_template | 32.0 ms                                                         | 34.7 ms: 1.08x slower                                                              |
| genshi_text     | 21.7 ms                                                         | 24.9 ms: 1.15x slower                                                              |
| genshi_xml      | 49.0 ms                                                         | 58.0 ms: 1.18x slower                                                              |
| Geometric mean  | (ref)                                                           | 1.09x slower                                                                       |

All benchmarks:
===============

| Benchmark                 | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241024-pythonperf1_win32-x86-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|---------------------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| thrift                    | 10.3 ms                                                         | 788 us: 13.03x faster                                                              |
| coverage                  | 326 ms                                                          | 54.3 ms: 6.01x faster                                                              |
| sqlglot_normalize         | 223 ms                                                          | 102 ms: 2.19x faster                                                               |
| deepcopy_memo             | 26.2 us                                                         | 19.6 us: 1.34x faster                                                              |
| deepcopy                  | 311 us                                                          | 244 us: 1.28x faster                                                               |
| deepcopy_reduce           | 2.94 us                                                         | 2.52 us: 1.17x faster                                                              |
| nbody                     | 81.4 ms                                                         | 70.3 ms: 1.16x faster                                                              |
| async_tree_memoization_tg | 287 ms                                                          | 264 ms: 1.09x faster                                                               |
| float                     | 56.4 ms                                                         | 52.2 ms: 1.08x faster                                                              |
| python_startup            | 28.3 ms                                                         | 26.4 ms: 1.07x faster                                                              |
| async_tree_none           | 245 ms                                                          | 228 ms: 1.07x faster                                                               |
| tomli_loads               | 1.74 sec                                                        | 1.64 sec: 1.06x faster                                                             |
| async_tree_memoization    | 302 ms                                                          | 287 ms: 1.05x faster                                                               |
| async_tree_cpu_io_mixed   | 490 ms                                                          | 474 ms: 1.03x faster                                                               |
| scimark_sor               | 85.8 ms                                                         | 83.3 ms: 1.03x faster                                                              |
| mako                      | 7.02 ms                                                         | 6.83 ms: 1.03x faster                                                              |
| pprint_safe_repr          | 658 ms                                                          | 642 ms: 1.03x faster                                                               |
| regex_effbot              | 1.82 ms                                                         | 1.79 ms: 1.02x faster                                                              |
| async_tree_none_tg        | 216 ms                                                          | 212 ms: 1.02x faster                                                               |
| go                        | 111 ms                                                          | 109 ms: 1.02x faster                                                               |
| pathlib                   | 89.1 ms                                                         | 88.3 ms: 1.01x faster                                                              |
| pycparser                 | 869 ms                                                          | 862 ms: 1.01x faster                                                               |
| telco                     | 6.27 ms                                                         | 6.32 ms: 1.01x slower                                                              |
| logging_simple            | 7.89 us                                                         | 7.96 us: 1.01x slower                                                              |
| bench_mp_pool             | 93.6 ms                                                         | 94.6 ms: 1.01x slower                                                              |
| fannkuch                  | 288 ms                                                          | 291 ms: 1.01x slower                                                               |
| regex_v8                  | 15.5 ms                                                         | 15.7 ms: 1.02x slower                                                              |
| pidigits                  | 204 ms                                                          | 207 ms: 1.02x slower                                                               |
| async_tree_io             | 530 ms                                                          | 540 ms: 1.02x slower                                                               |
| gc_traversal              | 1.76 ms                                                         | 1.81 ms: 1.02x slower                                                              |
| scimark_fft               | 204 ms                                                          | 210 ms: 1.03x slower                                                               |
| xml_etree_generate        | 61.9 ms                                                         | 63.8 ms: 1.03x slower                                                              |
| html5lib                  | 47.1 ms                                                         | 48.7 ms: 1.03x slower                                                              |
| spectral_norm             | 70.0 ms                                                         | 72.5 ms: 1.04x slower                                                              |
| meteor_contest            | 78.1 ms                                                         | 81.3 ms: 1.04x slower                                                              |
| scimark_monte_carlo       | 48.7 ms                                                         | 51.0 ms: 1.05x slower                                                              |
| tornado_http              | 105 ms                                                          | 110 ms: 1.05x slower                                                               |
| mdp                       | 1.70 sec                                                        | 1.79 sec: 1.05x slower                                                             |
| crypto_pyaes              | 56.6 ms                                                         | 59.7 ms: 1.05x slower                                                              |
| regex_dna                 | 112 ms                                                          | 119 ms: 1.06x slower                                                               |
| xml_etree_process         | 44.6 ms                                                         | 47.7 ms: 1.07x slower                                                              |
| unpickle_pure_python      | 162 us                                                          | 173 us: 1.07x slower                                                               |
| sqlglot_parse             | 1.02 ms                                                         | 1.10 ms: 1.07x slower                                                              |
| 2to3                      | 255 ms                                                          | 274 ms: 1.08x slower                                                               |
| pickle_pure_python        | 239 us                                                          | 258 us: 1.08x slower                                                               |
| typing_runtime_protocols  | 141 us                                                          | 152 us: 1.08x slower                                                               |
| scimark_lu                | 60.7 ms                                                         | 65.7 ms: 1.08x slower                                                              |
| django_template           | 32.0 ms                                                         | 34.7 ms: 1.08x slower                                                              |
| sympy_expand              | 377 ms                                                          | 410 ms: 1.09x slower                                                               |
| nqueens                   | 75.1 ms                                                         | 82.6 ms: 1.10x slower                                                              |
| create_gc_cycles          | 1.08 ms                                                         | 1.19 ms: 1.10x slower                                                              |
| xml_etree_parse           | 102 ms                                                          | 113 ms: 1.10x slower                                                               |
| coroutines                | 16.1 ms                                                         | 17.9 ms: 1.11x slower                                                              |
| pyflate                   | 322 ms                                                          | 358 ms: 1.11x slower                                                               |
| xml_etree_iterparse       | 61.3 ms                                                         | 68.2 ms: 1.11x slower                                                              |
| sympy_str                 | 214 ms                                                          | 239 ms: 1.12x slower                                                               |
| async_tree_io_tg          | 499 ms                                                          | 559 ms: 1.12x slower                                                               |
| regex_compile             | 101 ms                                                          | 113 ms: 1.12x slower                                                               |
| sqlglot_transpile         | 1.26 ms                                                         | 1.42 ms: 1.12x slower                                                              |
| sympy_sum                 | 108 ms                                                          | 122 ms: 1.13x slower                                                               |
| json_dumps                | 7.53 ms                                                         | 8.50 ms: 1.13x slower                                                              |
| genshi_text               | 21.7 ms                                                         | 24.9 ms: 1.15x slower                                                              |
| comprehensions            | 13.1 us                                                         | 15.3 us: 1.16x slower                                                              |
| docutils                  | 1.80 sec                                                        | 2.10 sec: 1.17x slower                                                             |
| json                      | 4.40 ms                                                         | 5.19 ms: 1.18x slower                                                              |
| genshi_xml                | 49.0 ms                                                         | 58.0 ms: 1.18x slower                                                              |
| richards                  | 33.4 ms                                                         | 39.5 ms: 1.18x slower                                                              |
| chaos                     | 49.4 ms                                                         | 58.7 ms: 1.19x slower                                                              |
| sphinx                    | 729 ms                                                          | 870 ms: 1.19x slower                                                               |
| sqlglot_optimize          | 42.4 ms                                                         | 50.6 ms: 1.19x slower                                                              |
| sympy_integrate           | 15.2 ms                                                         | 18.3 ms: 1.20x slower                                                              |
| richards_super            | 37.0 ms                                                         | 44.6 ms: 1.20x slower                                                              |
| async_generators          | 267 ms                                                          | 326 ms: 1.22x slower                                                               |
| logging_silent            | 62.4 ns                                                         | 76.8 ns: 1.23x slower                                                              |
| deltablue                 | 2.35 ms                                                         | 2.91 ms: 1.24x slower                                                              |
| pylint                    | 225 ms                                                          | 291 ms: 1.30x slower                                                               |
| generators                | 21.5 ms                                                         | 28.1 ms: 1.31x slower                                                              |
| raytrace                  | 203 ms                                                          | 277 ms: 1.37x slower                                                               |
| hexiom                    | 4.60 ms                                                         | 6.40 ms: 1.39x slower                                                              |
| Geometric mean            | (ref)                                                           | 1.01x faster                                                                       |

Benchmark hidden because not significant (8): bench_thread_pool, logging_format, python_startup_no_site, dulwich_log, json_loads, scimark_sparse_mat_mult, async_tree_cpu_io_mixed_tg, pprint_pformat
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: asyncio_websockets, bpe_tokeniser, chameleon, connected_components, gevent_hub, k_core, shortest_path, sqlalchemy_declarative, sqlalchemy_imperative

- Geometric mean (including insignificant results): 1.007x faster
# HPT report

- Reliability score: 99.95% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown