# Results vs. 3.13.0

- fork: python
- ref: 9d08423b6e0fa89ce9cf
- machine: windows-x86
- commit hash: 9d08423
- commit date: 2024-11-09
- overall geometric mean: 1.062x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.08x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241109-pythonperf1_win32-x86-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 255 ms                                                          | 293 ms: 1.15x slower                                                            |
| docutils       | 1.80 sec                                                        | 2.14 sec: 1.19x slower                                                          |
| html5lib       | 47.1 ms                                                         | 50.0 ms: 1.06x slower                                                           |
| sphinx         | 729 ms                                                          | 907 ms: 1.24x slower                                                            |
| Geometric mean | (ref)                                                           | 1.16x slower                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241109-pythonperf1_win32-x86-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|---------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_memoization_tg | 287 ms                                                          | 271 ms: 1.06x faster                                                            |
| async_tree_memoization    | 302 ms                                                          | 296 ms: 1.02x faster                                                            |
| async_tree_none           | 245 ms                                                          | 242 ms: 1.01x faster                                                            |
| asyncio_websockets        | 352 ms                                                          | 348 ms: 1.01x faster                                                            |
| async_tree_none_tg        | 216 ms                                                          | 223 ms: 1.03x slower                                                            |
| async_tree_io             | 530 ms                                                          | 567 ms: 1.07x slower                                                            |
| coroutines                | 16.1 ms                                                         | 17.4 ms: 1.08x slower                                                           |
| async_tree_io_tg          | 499 ms                                                          | 575 ms: 1.15x slower                                                            |
| async_generators          | 267 ms                                                          | 323 ms: 1.21x slower                                                            |
| Geometric mean            | (ref)                                                           | 1.04x slower                                                                    |

Benchmark hidden because not significant (2): async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241109-pythonperf1_win32-x86-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pidigits       | 204 ms                                                          | 207 ms: 1.02x slower                                                            |
| nbody          | 81.4 ms                                                         | 93.1 ms: 1.14x slower                                                           |
| Geometric mean | (ref)                                                           | 1.05x slower                                                                    |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241109-pythonperf1_win32-x86-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_v8       | 15.5 ms                                                         | 15.7 ms: 1.01x slower                                                           |
| regex_dna      | 112 ms                                                          | 115 ms: 1.02x slower                                                            |
| regex_compile  | 101 ms                                                          | 122 ms: 1.21x slower                                                            |
| Geometric mean | (ref)                                                           | 1.06x slower                                                                    |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241109-pythonperf1_win32-x86-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| json_loads           | 21.7 us                                                         | 21.3 us: 1.02x faster                                                           |
| tomli_loads          | 1.74 sec                                                        | 1.85 sec: 1.06x slower                                                          |
| xml_etree_parse      | 102 ms                                                          | 111 ms: 1.08x slower                                                            |
| xml_etree_iterparse  | 61.3 ms                                                         | 68.6 ms: 1.12x slower                                                           |
| xml_etree_generate   | 61.9 ms                                                         | 72.0 ms: 1.16x slower                                                           |
| unpickle_pure_python | 162 us                                                          | 189 us: 1.17x slower                                                            |
| json_dumps           | 7.53 ms                                                         | 8.98 ms: 1.19x slower                                                           |
| xml_etree_process    | 44.6 ms                                                         | 54.0 ms: 1.21x slower                                                           |
| pickle_pure_python   | 239 us                                                          | 306 us: 1.28x slower                                                            |
| Geometric mean       | (ref)                                                           | 1.14x slower                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241109-pythonperf1_win32-x86-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 28.3 ms                                                         | 26.2 ms: 1.08x faster                                                           |
| python_startup_no_site | 20.2 ms                                                         | 20.0 ms: 1.01x faster                                                           |
| Geometric mean         | (ref)                                                           | 1.04x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241109-pythonperf1_win32-x86-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 7.02 ms                                                         | 7.39 ms: 1.05x slower                                                           |
| django_template | 32.0 ms                                                         | 35.9 ms: 1.12x slower                                                           |
| genshi_xml      | 49.0 ms                                                         | 58.2 ms: 1.19x slower                                                           |
| genshi_text     | 21.7 ms                                                         | 26.1 ms: 1.20x slower                                                           |
| Geometric mean  | (ref)                                                           | 1.14x slower                                                                    |

All benchmarks:
===============

| Benchmark                 | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241109-pythonperf1_win32-x86-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|---------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| thrift                    | 10.3 ms                                                         | 782 us: 13.12x faster                                                           |
| coverage                  | 326 ms                                                          | 53.1 ms: 6.14x faster                                                           |
| sqlglot_normalize         | 223 ms                                                          | 113 ms: 1.97x faster                                                            |
| deepcopy                  | 311 us                                                          | 272 us: 1.14x faster                                                            |
| deepcopy_memo             | 26.2 us                                                         | 23.2 us: 1.13x faster                                                           |
| deepcopy_reduce           | 2.94 us                                                         | 2.72 us: 1.08x faster                                                           |
| python_startup            | 28.3 ms                                                         | 26.2 ms: 1.08x faster                                                           |
| async_tree_memoization_tg | 287 ms                                                          | 271 ms: 1.06x faster                                                            |
| pathlib                   | 89.1 ms                                                         | 87.1 ms: 1.02x faster                                                           |
| async_tree_memoization    | 302 ms                                                          | 296 ms: 1.02x faster                                                            |
| json_loads                | 21.7 us                                                         | 21.3 us: 1.02x faster                                                           |
| async_tree_none           | 245 ms                                                          | 242 ms: 1.01x faster                                                            |
| asyncio_websockets        | 352 ms                                                          | 348 ms: 1.01x faster                                                            |
| python_startup_no_site    | 20.2 ms                                                         | 20.0 ms: 1.01x faster                                                           |
| gc_traversal              | 1.76 ms                                                         | 1.78 ms: 1.01x slower                                                           |
| bench_mp_pool             | 93.6 ms                                                         | 94.4 ms: 1.01x slower                                                           |
| regex_v8                  | 15.5 ms                                                         | 15.7 ms: 1.01x slower                                                           |
| pidigits                  | 204 ms                                                          | 207 ms: 1.02x slower                                                            |
| dulwich_log               | 50.2 ms                                                         | 51.1 ms: 1.02x slower                                                           |
| json                      | 4.40 ms                                                         | 4.50 ms: 1.02x slower                                                           |
| regex_dna                 | 112 ms                                                          | 115 ms: 1.02x slower                                                            |
| async_tree_none_tg        | 216 ms                                                          | 223 ms: 1.03x slower                                                            |
| logging_format            | 8.59 us                                                         | 8.93 us: 1.04x slower                                                           |
| logging_simple            | 7.89 us                                                         | 8.27 us: 1.05x slower                                                           |
| mako                      | 7.02 ms                                                         | 7.39 ms: 1.05x slower                                                           |
| html5lib                  | 47.1 ms                                                         | 50.0 ms: 1.06x slower                                                           |
| tomli_loads               | 1.74 sec                                                        | 1.85 sec: 1.06x slower                                                          |
| async_tree_io             | 530 ms                                                          | 567 ms: 1.07x slower                                                            |
| coroutines                | 16.1 ms                                                         | 17.4 ms: 1.08x slower                                                           |
| shortest_path             | 298 ms                                                          | 322 ms: 1.08x slower                                                            |
| xml_etree_parse           | 102 ms                                                          | 111 ms: 1.08x slower                                                            |
| pycparser                 | 869 ms                                                          | 944 ms: 1.09x slower                                                            |
| create_gc_cycles          | 1.08 ms                                                         | 1.18 ms: 1.09x slower                                                           |
| connected_components      | 266 ms                                                          | 291 ms: 1.09x slower                                                            |
| mdp                       | 1.70 sec                                                        | 1.86 sec: 1.09x slower                                                          |
| sympy_expand              | 377 ms                                                          | 420 ms: 1.11x slower                                                            |
| xml_etree_iterparse       | 61.3 ms                                                         | 68.6 ms: 1.12x slower                                                           |
| django_template           | 32.0 ms                                                         | 35.9 ms: 1.12x slower                                                           |
| pprint_safe_repr          | 658 ms                                                          | 738 ms: 1.12x slower                                                            |
| spectral_norm             | 70.0 ms                                                         | 78.6 ms: 1.12x slower                                                           |
| go                        | 111 ms                                                          | 125 ms: 1.13x slower                                                            |
| scimark_sparse_mat_mult   | 2.88 ms                                                         | 3.24 ms: 1.13x slower                                                           |
| meteor_contest            | 78.1 ms                                                         | 88.4 ms: 1.13x slower                                                           |
| pprint_pformat            | 1.32 sec                                                        | 1.50 sec: 1.14x slower                                                          |
| telco                     | 6.27 ms                                                         | 7.14 ms: 1.14x slower                                                           |
| nbody                     | 81.4 ms                                                         | 93.1 ms: 1.14x slower                                                           |
| 2to3                      | 255 ms                                                          | 293 ms: 1.15x slower                                                            |
| bpe_tokeniser             | 3.49 sec                                                        | 4.01 sec: 1.15x slower                                                          |
| async_tree_io_tg          | 499 ms                                                          | 575 ms: 1.15x slower                                                            |
| fannkuch                  | 288 ms                                                          | 332 ms: 1.15x slower                                                            |
| scimark_sor               | 85.8 ms                                                         | 99.1 ms: 1.16x slower                                                           |
| sqlglot_parse             | 1.02 ms                                                         | 1.18 ms: 1.16x slower                                                           |
| sympy_str                 | 214 ms                                                          | 249 ms: 1.16x slower                                                            |
| xml_etree_generate        | 61.9 ms                                                         | 72.0 ms: 1.16x slower                                                           |
| sympy_sum                 | 108 ms                                                          | 126 ms: 1.17x slower                                                            |
| unpickle_pure_python      | 162 us                                                          | 189 us: 1.17x slower                                                            |
| genshi_xml                | 49.0 ms                                                         | 58.2 ms: 1.19x slower                                                           |
| crypto_pyaes              | 56.6 ms                                                         | 67.3 ms: 1.19x slower                                                           |
| typing_runtime_protocols  | 141 us                                                          | 168 us: 1.19x slower                                                            |
| docutils                  | 1.80 sec                                                        | 2.14 sec: 1.19x slower                                                          |
| json_dumps                | 7.53 ms                                                         | 8.98 ms: 1.19x slower                                                           |
| genshi_text               | 21.7 ms                                                         | 26.1 ms: 1.20x slower                                                           |
| sqlglot_transpile         | 1.26 ms                                                         | 1.52 ms: 1.20x slower                                                           |
| regex_compile             | 101 ms                                                          | 122 ms: 1.21x slower                                                            |
| xml_etree_process         | 44.6 ms                                                         | 54.0 ms: 1.21x slower                                                           |
| async_generators          | 267 ms                                                          | 323 ms: 1.21x slower                                                            |
| scimark_lu                | 60.7 ms                                                         | 74.1 ms: 1.22x slower                                                           |
| pylint                    | 225 ms                                                          | 278 ms: 1.24x slower                                                            |
| pyflate                   | 322 ms                                                          | 400 ms: 1.24x slower                                                            |
| sphinx                    | 729 ms                                                          | 907 ms: 1.24x slower                                                            |
| scimark_fft               | 204 ms                                                          | 257 ms: 1.26x slower                                                            |
| logging_silent            | 62.4 ns                                                         | 79.0 ns: 1.27x slower                                                           |
| sympy_integrate           | 15.2 ms                                                         | 19.4 ms: 1.28x slower                                                           |
| pickle_pure_python        | 239 us                                                          | 306 us: 1.28x slower                                                            |
| richards                  | 33.4 ms                                                         | 42.8 ms: 1.28x slower                                                           |
| chaos                     | 49.4 ms                                                         | 64.2 ms: 1.30x slower                                                           |
| scimark_monte_carlo       | 48.7 ms                                                         | 63.7 ms: 1.31x slower                                                           |
| nqueens                   | 75.1 ms                                                         | 98.5 ms: 1.31x slower                                                           |
| sqlglot_optimize          | 42.4 ms                                                         | 57.2 ms: 1.35x slower                                                           |
| richards_super            | 37.0 ms                                                         | 50.2 ms: 1.35x slower                                                           |
| deltablue                 | 2.35 ms                                                         | 3.24 ms: 1.38x slower                                                           |
| comprehensions            | 13.1 us                                                         | 18.3 us: 1.39x slower                                                           |
| raytrace                  | 203 ms                                                          | 291 ms: 1.43x slower                                                            |
| k_core                    | 1.43 sec                                                        | 2.06 sec: 1.44x slower                                                          |
| hexiom                    | 4.60 ms                                                         | 7.33 ms: 1.60x slower                                                           |
| generators                | 21.5 ms                                                         | 36.3 ms: 1.69x slower                                                           |
| Geometric mean            | (ref)                                                           | 1.07x slower                                                                    |

Benchmark hidden because not significant (5): float, regex_effbot, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, bench_thread_pool
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (1) of results/bm-20241109-3.14.0a1+-9d08423-JIT/bm-20241109-pythonperf1_win32-x86-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423.json: sqlite_synth

- Geometric mean (including insignificant results): 1.062x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.10x
- 95% likely to have a slowdown of 1.09x
- 99% likely to have a slowdown of 1.08x

# Memory
- memory change: unknown