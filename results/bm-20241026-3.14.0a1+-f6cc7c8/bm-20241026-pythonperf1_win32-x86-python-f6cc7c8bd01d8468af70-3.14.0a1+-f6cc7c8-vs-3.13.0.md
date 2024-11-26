# Results vs. 3.13.0

- fork: python
- ref: f6cc7c8bd01d8468af70
- machine: windows-x86
- commit hash: f6cc7c8
- commit date: 2024-10-26
- overall geometric mean: 1.008x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.01x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241026-pythonperf1_win32-x86-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 255 ms                                                          | 248 ms: 1.03x faster                                                            |
| docutils       | 1.80 sec                                                        | 1.87 sec: 1.04x slower                                                          |
| html5lib       | 47.1 ms                                                         | 45.9 ms: 1.03x faster                                                           |
| sphinx         | 729 ms                                                          | 758 ms: 1.04x slower                                                            |
| Geometric mean | (ref)                                                           | 1.00x slower                                                                    |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241026-pythonperf1_win32-x86-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|---------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_memoization_tg | 287 ms                                                          | 262 ms: 1.10x faster                                                            |
| async_tree_none           | 245 ms                                                          | 226 ms: 1.08x faster                                                            |
| async_tree_memoization    | 302 ms                                                          | 281 ms: 1.08x faster                                                            |
| async_tree_none_tg        | 216 ms                                                          | 208 ms: 1.04x faster                                                            |
| async_tree_cpu_io_mixed   | 490 ms                                                          | 477 ms: 1.03x faster                                                            |
| coroutines                | 16.1 ms                                                         | 17.6 ms: 1.09x slower                                                           |
| async_generators          | 267 ms                                                          | 295 ms: 1.10x slower                                                            |
| async_tree_io_tg          | 499 ms                                                          | 562 ms: 1.12x slower                                                            |
| Geometric mean            | (ref)                                                           | 1.00x slower                                                                    |

Benchmark hidden because not significant (2): async_tree_cpu_io_mixed_tg, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241026-pythonperf1_win32-x86-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 81.4 ms                                                         | 88.2 ms: 1.08x slower                                                           |
| float          | 56.4 ms                                                         | 61.5 ms: 1.09x slower                                                           |
| Geometric mean | (ref)                                                           | 1.06x slower                                                                    |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241026-pythonperf1_win32-x86-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_dna      | 112 ms                                                          | 113 ms: 1.01x slower                                                            |
| regex_v8       | 15.5 ms                                                         | 15.8 ms: 1.02x slower                                                           |
| regex_compile  | 101 ms                                                          | 108 ms: 1.07x slower                                                            |
| Geometric mean | (ref)                                                           | 1.02x slower                                                                    |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241026-pythonperf1_win32-x86-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| json_loads           | 21.7 us                                                         | 21.0 us: 1.03x faster                                                           |
| tomli_loads          | 1.74 sec                                                        | 1.82 sec: 1.05x slower                                                          |
| xml_etree_generate   | 61.9 ms                                                         | 65.8 ms: 1.06x slower                                                           |
| xml_etree_process    | 44.6 ms                                                         | 47.6 ms: 1.07x slower                                                           |
| xml_etree_parse      | 102 ms                                                          | 112 ms: 1.09x slower                                                            |
| unpickle_pure_python | 162 us                                                          | 179 us: 1.11x slower                                                            |
| pickle_pure_python   | 239 us                                                          | 266 us: 1.11x slower                                                            |
| xml_etree_iterparse  | 61.3 ms                                                         | 68.7 ms: 1.12x slower                                                           |
| json_dumps           | 7.53 ms                                                         | 9.04 ms: 1.20x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.08x slower                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241026-pythonperf1_win32-x86-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup | 28.3 ms                                                         | 26.8 ms: 1.06x faster                                                           |
| Geometric mean | (ref)                                                           | 1.03x faster                                                                    |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241026-pythonperf1_win32-x86-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_xml      | 49.0 ms                                                         | 46.2 ms: 1.06x faster                                                           |
| genshi_text     | 21.7 ms                                                         | 21.1 ms: 1.03x faster                                                           |
| django_template | 32.0 ms                                                         | 34.0 ms: 1.06x slower                                                           |
| mako            | 7.02 ms                                                         | 7.78 ms: 1.11x slower                                                           |
| Geometric mean  | (ref)                                                           | 1.02x slower                                                                    |

All benchmarks:
===============

| Benchmark                 | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241026-pythonperf1_win32-x86-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|---------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| thrift                    | 10.3 ms                                                         | 740 us: 13.86x faster                                                           |
| coverage                  | 326 ms                                                          | 56.4 ms: 5.78x faster                                                           |
| deepcopy                  | 311 us                                                          | 238 us: 1.31x faster                                                            |
| deepcopy_reduce           | 2.94 us                                                         | 2.46 us: 1.20x faster                                                           |
| deepcopy_memo             | 26.2 us                                                         | 21.9 us: 1.19x faster                                                           |
| go                        | 111 ms                                                          | 100 ms: 1.11x faster                                                            |
| async_tree_memoization_tg | 287 ms                                                          | 262 ms: 1.10x faster                                                            |
| async_tree_none           | 245 ms                                                          | 226 ms: 1.08x faster                                                            |
| async_tree_memoization    | 302 ms                                                          | 281 ms: 1.08x faster                                                            |
| genshi_xml                | 49.0 ms                                                         | 46.2 ms: 1.06x faster                                                           |
| python_startup            | 28.3 ms                                                         | 26.8 ms: 1.06x faster                                                           |
| bench_mp_pool             | 93.6 ms                                                         | 88.8 ms: 1.05x faster                                                           |
| bench_thread_pool         | 1.04 ms                                                         | 1.00 ms: 1.04x faster                                                           |
| async_tree_none_tg        | 216 ms                                                          | 208 ms: 1.04x faster                                                            |
| json_loads                | 21.7 us                                                         | 21.0 us: 1.03x faster                                                           |
| 2to3                      | 255 ms                                                          | 248 ms: 1.03x faster                                                            |
| genshi_text               | 21.7 ms                                                         | 21.1 ms: 1.03x faster                                                           |
| async_tree_cpu_io_mixed   | 490 ms                                                          | 477 ms: 1.03x faster                                                            |
| html5lib                  | 47.1 ms                                                         | 45.9 ms: 1.03x faster                                                           |
| pycparser                 | 869 ms                                                          | 850 ms: 1.02x faster                                                            |
| pprint_safe_repr          | 658 ms                                                          | 651 ms: 1.01x faster                                                            |
| sympy_sum                 | 108 ms                                                          | 107 ms: 1.01x faster                                                            |
| regex_dna                 | 112 ms                                                          | 113 ms: 1.01x slower                                                            |
| logging_simple            | 7.89 us                                                         | 7.98 us: 1.01x slower                                                           |
| typing_runtime_protocols  | 141 us                                                          | 143 us: 1.01x slower                                                            |
| sympy_expand              | 377 ms                                                          | 383 ms: 1.01x slower                                                            |
| sympy_str                 | 214 ms                                                          | 218 ms: 1.02x slower                                                            |
| gc_traversal              | 1.76 ms                                                         | 1.80 ms: 1.02x slower                                                           |
| regex_v8                  | 15.5 ms                                                         | 15.8 ms: 1.02x slower                                                           |
| meteor_contest            | 78.1 ms                                                         | 80.4 ms: 1.03x slower                                                           |
| pprint_pformat            | 1.32 sec                                                        | 1.36 sec: 1.03x slower                                                          |
| sympy_integrate           | 15.2 ms                                                         | 15.7 ms: 1.03x slower                                                           |
| dulwich_log               | 50.2 ms                                                         | 52.1 ms: 1.04x slower                                                           |
| sqlglot_optimize          | 42.4 ms                                                         | 44.1 ms: 1.04x slower                                                           |
| sphinx                    | 729 ms                                                          | 758 ms: 1.04x slower                                                            |
| docutils                  | 1.80 sec                                                        | 1.87 sec: 1.04x slower                                                          |
| tomli_loads               | 1.74 sec                                                        | 1.82 sec: 1.05x slower                                                          |
| pylint                    | 225 ms                                                          | 236 ms: 1.05x slower                                                            |
| sqlglot_normalize         | 223 ms                                                          | 234 ms: 1.05x slower                                                            |
| crypto_pyaes              | 56.6 ms                                                         | 59.8 ms: 1.06x slower                                                           |
| nqueens                   | 75.1 ms                                                         | 79.6 ms: 1.06x slower                                                           |
| django_template           | 32.0 ms                                                         | 34.0 ms: 1.06x slower                                                           |
| xml_etree_generate        | 61.9 ms                                                         | 65.8 ms: 1.06x slower                                                           |
| xml_etree_process         | 44.6 ms                                                         | 47.6 ms: 1.07x slower                                                           |
| comprehensions            | 13.1 us                                                         | 14.0 us: 1.07x slower                                                           |
| mdp                       | 1.70 sec                                                        | 1.81 sec: 1.07x slower                                                          |
| sqlglot_transpile         | 1.26 ms                                                         | 1.35 ms: 1.07x slower                                                           |
| regex_compile             | 101 ms                                                          | 108 ms: 1.07x slower                                                            |
| sqlglot_parse             | 1.02 ms                                                         | 1.10 ms: 1.07x slower                                                           |
| nbody                     | 81.4 ms                                                         | 88.2 ms: 1.08x slower                                                           |
| coroutines                | 16.1 ms                                                         | 17.6 ms: 1.09x slower                                                           |
| fannkuch                  | 288 ms                                                          | 314 ms: 1.09x slower                                                            |
| float                     | 56.4 ms                                                         | 61.5 ms: 1.09x slower                                                           |
| create_gc_cycles          | 1.08 ms                                                         | 1.18 ms: 1.09x slower                                                           |
| xml_etree_parse           | 102 ms                                                          | 112 ms: 1.09x slower                                                            |
| async_generators          | 267 ms                                                          | 295 ms: 1.10x slower                                                            |
| unpickle_pure_python      | 162 us                                                          | 179 us: 1.11x slower                                                            |
| spectral_norm             | 70.0 ms                                                         | 77.4 ms: 1.11x slower                                                           |
| mako                      | 7.02 ms                                                         | 7.78 ms: 1.11x slower                                                           |
| pickle_pure_python        | 239 us                                                          | 266 us: 1.11x slower                                                            |
| scimark_sparse_mat_mult   | 2.88 ms                                                         | 3.21 ms: 1.11x slower                                                           |
| telco                     | 6.27 ms                                                         | 7.00 ms: 1.12x slower                                                           |
| logging_silent            | 62.4 ns                                                         | 69.7 ns: 1.12x slower                                                           |
| generators                | 21.5 ms                                                         | 24.1 ms: 1.12x slower                                                           |
| xml_etree_iterparse       | 61.3 ms                                                         | 68.7 ms: 1.12x slower                                                           |
| hexiom                    | 4.60 ms                                                         | 5.16 ms: 1.12x slower                                                           |
| async_tree_io_tg          | 499 ms                                                          | 562 ms: 1.12x slower                                                            |
| deltablue                 | 2.35 ms                                                         | 2.65 ms: 1.13x slower                                                           |
| scimark_lu                | 60.7 ms                                                         | 69.2 ms: 1.14x slower                                                           |
| pyflate                   | 322 ms                                                          | 368 ms: 1.14x slower                                                            |
| chaos                     | 49.4 ms                                                         | 57.7 ms: 1.17x slower                                                           |
| scimark_monte_carlo       | 48.7 ms                                                         | 57.0 ms: 1.17x slower                                                           |
| richards                  | 33.4 ms                                                         | 39.2 ms: 1.17x slower                                                           |
| richards_super            | 37.0 ms                                                         | 44.1 ms: 1.19x slower                                                           |
| json_dumps                | 7.53 ms                                                         | 9.04 ms: 1.20x slower                                                           |
| scimark_fft               | 204 ms                                                          | 246 ms: 1.21x slower                                                            |
| raytrace                  | 203 ms                                                          | 250 ms: 1.23x slower                                                            |
| scimark_sor               | 85.8 ms                                                         | 106 ms: 1.24x slower                                                            |
| json                      | 4.40 ms                                                         | 5.89 ms: 1.34x slower                                                           |
| Geometric mean            | (ref)                                                           | 1.01x faster                                                                    |

Benchmark hidden because not significant (8): tornado_http, regex_effbot, python_startup_no_site, logging_format, pidigits, async_tree_cpu_io_mixed_tg, pathlib, async_tree_io
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: asyncio_websockets, bpe_tokeniser, chameleon, connected_components, gevent_hub, k_core, shortest_path, sqlalchemy_declarative, sqlalchemy_imperative

- Geometric mean (including insignificant results): 1.008x faster
# HPT report

- Reliability score: 99.99% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: unknown