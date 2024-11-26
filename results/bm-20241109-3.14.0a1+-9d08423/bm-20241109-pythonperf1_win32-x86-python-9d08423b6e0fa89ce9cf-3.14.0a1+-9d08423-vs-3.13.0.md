# Results vs. 3.13.0

- fork: python
- ref: 9d08423b6e0fa89ce9cf
- machine: windows-x86
- commit hash: 9d08423
- commit date: 2024-11-09
- overall geometric mean: 1.012x faster
- HPT reliability: 99.73%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241109-pythonperf1_win32-x86-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 255 ms                                                          | 251 ms: 1.02x faster                                                            |
| docutils       | 1.80 sec                                                        | 1.84 sec: 1.02x slower                                                          |
| html5lib       | 47.1 ms                                                         | 46.0 ms: 1.02x faster                                                           |
| sphinx         | 729 ms                                                          | 757 ms: 1.04x slower                                                            |
| Geometric mean | (ref)                                                           | 1.00x slower                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241109-pythonperf1_win32-x86-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|---------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_memoization_tg | 287 ms                                                          | 252 ms: 1.14x faster                                                            |
| async_tree_none           | 245 ms                                                          | 219 ms: 1.12x faster                                                            |
| async_tree_memoization    | 302 ms                                                          | 275 ms: 1.10x faster                                                            |
| async_tree_none_tg        | 216 ms                                                          | 201 ms: 1.07x faster                                                            |
| async_tree_cpu_io_mixed   | 490 ms                                                          | 469 ms: 1.04x faster                                                            |
| async_tree_io             | 530 ms                                                          | 519 ms: 1.02x faster                                                            |
| coroutines                | 16.1 ms                                                         | 16.3 ms: 1.01x slower                                                           |
| asyncio_websockets        | 352 ms                                                          | 380 ms: 1.08x slower                                                            |
| async_tree_io_tg          | 499 ms                                                          | 547 ms: 1.10x slower                                                            |
| async_generators          | 267 ms                                                          | 300 ms: 1.12x slower                                                            |
| Geometric mean            | (ref)                                                           | 1.02x faster                                                                    |

Benchmark hidden because not significant (1): async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241109-pythonperf1_win32-x86-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pidigits       | 204 ms                                                          | 201 ms: 1.02x faster                                                            |
| float          | 56.4 ms                                                         | 61.7 ms: 1.09x slower                                                           |
| nbody          | 81.4 ms                                                         | 95.8 ms: 1.18x slower                                                           |
| Geometric mean | (ref)                                                           | 1.08x slower                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241109-pythonperf1_win32-x86-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_v8       | 15.5 ms                                                         | 15.6 ms: 1.01x slower                                                           |
| regex_effbot   | 1.82 ms                                                         | 1.88 ms: 1.03x slower                                                           |
| regex_compile  | 101 ms                                                          | 105 ms: 1.04x slower                                                            |
| regex_dna      | 112 ms                                                          | 122 ms: 1.08x slower                                                            |
| Geometric mean | (ref)                                                           | 1.04x slower                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241109-pythonperf1_win32-x86-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| json_loads           | 21.7 us                                                         | 21.2 us: 1.02x faster                                                           |
| tomli_loads          | 1.74 sec                                                        | 1.81 sec: 1.04x slower                                                          |
| unpickle_pure_python | 162 us                                                          | 178 us: 1.10x slower                                                            |
| xml_etree_parse      | 102 ms                                                          | 113 ms: 1.10x slower                                                            |
| xml_etree_generate   | 61.9 ms                                                         | 68.8 ms: 1.11x slower                                                           |
| pickle_pure_python   | 239 us                                                          | 267 us: 1.12x slower                                                            |
| xml_etree_iterparse  | 61.3 ms                                                         | 68.5 ms: 1.12x slower                                                           |
| xml_etree_process    | 44.6 ms                                                         | 50.5 ms: 1.13x slower                                                           |
| json_dumps           | 7.53 ms                                                         | 8.75 ms: 1.16x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.09x slower                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241109-pythonperf1_win32-x86-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 28.3 ms                                                         | 26.1 ms: 1.08x faster                                                           |
| python_startup_no_site | 20.2 ms                                                         | 19.5 ms: 1.03x faster                                                           |
| Geometric mean         | (ref)                                                           | 1.06x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241109-pythonperf1_win32-x86-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_xml      | 49.0 ms                                                         | 46.1 ms: 1.06x faster                                                           |
| genshi_text     | 21.7 ms                                                         | 20.7 ms: 1.05x faster                                                           |
| django_template | 32.0 ms                                                         | 32.7 ms: 1.02x slower                                                           |
| mako            | 7.02 ms                                                         | 7.62 ms: 1.09x slower                                                           |
| Geometric mean  | (ref)                                                           | 1.00x faster                                                                    |

All benchmarks:
===============

| Benchmark                 | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241109-pythonperf1_win32-x86-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|---------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| thrift                    | 10.3 ms                                                         | 757 us: 13.55x faster                                                           |
| coverage                  | 326 ms                                                          | 51.7 ms: 6.31x faster                                                           |
| deepcopy                  | 311 us                                                          | 235 us: 1.32x faster                                                            |
| deepcopy_reduce           | 2.94 us                                                         | 2.50 us: 1.18x faster                                                           |
| deepcopy_memo             | 26.2 us                                                         | 22.5 us: 1.16x faster                                                           |
| async_tree_memoization_tg | 287 ms                                                          | 252 ms: 1.14x faster                                                            |
| async_tree_none           | 245 ms                                                          | 219 ms: 1.12x faster                                                            |
| go                        | 111 ms                                                          | 101 ms: 1.10x faster                                                            |
| async_tree_memoization    | 302 ms                                                          | 275 ms: 1.10x faster                                                            |
| python_startup            | 28.3 ms                                                         | 26.1 ms: 1.08x faster                                                           |
| async_tree_none_tg        | 216 ms                                                          | 201 ms: 1.07x faster                                                            |
| genshi_xml                | 49.0 ms                                                         | 46.1 ms: 1.06x faster                                                           |
| bench_mp_pool             | 93.6 ms                                                         | 88.7 ms: 1.06x faster                                                           |
| pycparser                 | 869 ms                                                          | 823 ms: 1.06x faster                                                            |
| genshi_text               | 21.7 ms                                                         | 20.7 ms: 1.05x faster                                                           |
| async_tree_cpu_io_mixed   | 490 ms                                                          | 469 ms: 1.04x faster                                                            |
| python_startup_no_site    | 20.2 ms                                                         | 19.5 ms: 1.03x faster                                                           |
| shortest_path             | 298 ms                                                          | 289 ms: 1.03x faster                                                            |
| connected_components      | 266 ms                                                          | 259 ms: 1.03x faster                                                            |
| pathlib                   | 89.1 ms                                                         | 86.7 ms: 1.03x faster                                                           |
| sympy_sum                 | 108 ms                                                          | 105 ms: 1.03x faster                                                            |
| html5lib                  | 47.1 ms                                                         | 46.0 ms: 1.02x faster                                                           |
| json_loads                | 21.7 us                                                         | 21.2 us: 1.02x faster                                                           |
| async_tree_io             | 530 ms                                                          | 519 ms: 1.02x faster                                                            |
| 2to3                      | 255 ms                                                          | 251 ms: 1.02x faster                                                            |
| pidigits                  | 204 ms                                                          | 201 ms: 1.02x faster                                                            |
| nqueens                   | 75.1 ms                                                         | 74.0 ms: 1.01x faster                                                           |
| logging_simple            | 7.89 us                                                         | 7.81 us: 1.01x faster                                                           |
| mdp                       | 1.70 sec                                                        | 1.68 sec: 1.01x faster                                                          |
| logging_format            | 8.59 us                                                         | 8.54 us: 1.01x faster                                                           |
| sympy_expand              | 377 ms                                                          | 376 ms: 1.00x faster                                                            |
| bpe_tokeniser             | 3.49 sec                                                        | 3.50 sec: 1.00x slower                                                          |
| regex_v8                  | 15.5 ms                                                         | 15.6 ms: 1.01x slower                                                           |
| coroutines                | 16.1 ms                                                         | 16.3 ms: 1.01x slower                                                           |
| sympy_integrate           | 15.2 ms                                                         | 15.4 ms: 1.01x slower                                                           |
| django_template           | 32.0 ms                                                         | 32.7 ms: 1.02x slower                                                           |
| json                      | 4.40 ms                                                         | 4.49 ms: 1.02x slower                                                           |
| docutils                  | 1.80 sec                                                        | 1.84 sec: 1.02x slower                                                          |
| pprint_safe_repr          | 658 ms                                                          | 677 ms: 1.03x slower                                                            |
| dulwich_log               | 50.2 ms                                                         | 51.8 ms: 1.03x slower                                                           |
| regex_effbot              | 1.82 ms                                                         | 1.88 ms: 1.03x slower                                                           |
| sphinx                    | 729 ms                                                          | 757 ms: 1.04x slower                                                            |
| tomli_loads               | 1.74 sec                                                        | 1.81 sec: 1.04x slower                                                          |
| meteor_contest            | 78.1 ms                                                         | 81.4 ms: 1.04x slower                                                           |
| regex_compile             | 101 ms                                                          | 105 ms: 1.04x slower                                                            |
| typing_runtime_protocols  | 141 us                                                          | 147 us: 1.05x slower                                                            |
| sqlglot_transpile         | 1.26 ms                                                         | 1.32 ms: 1.05x slower                                                           |
| sqlglot_normalize         | 223 ms                                                          | 234 ms: 1.05x slower                                                            |
| telco                     | 6.27 ms                                                         | 6.59 ms: 1.05x slower                                                           |
| sqlglot_optimize          | 42.4 ms                                                         | 44.6 ms: 1.05x slower                                                           |
| crypto_pyaes              | 56.6 ms                                                         | 59.8 ms: 1.06x slower                                                           |
| sqlglot_parse             | 1.02 ms                                                         | 1.08 ms: 1.06x slower                                                           |
| pprint_pformat            | 1.32 sec                                                        | 1.40 sec: 1.06x slower                                                          |
| create_gc_cycles          | 1.08 ms                                                         | 1.16 ms: 1.07x slower                                                           |
| asyncio_websockets        | 352 ms                                                          | 380 ms: 1.08x slower                                                            |
| regex_dna                 | 112 ms                                                          | 122 ms: 1.08x slower                                                            |
| mako                      | 7.02 ms                                                         | 7.62 ms: 1.09x slower                                                           |
| comprehensions            | 13.1 us                                                         | 14.3 us: 1.09x slower                                                           |
| fannkuch                  | 288 ms                                                          | 314 ms: 1.09x slower                                                            |
| float                     | 56.4 ms                                                         | 61.7 ms: 1.09x slower                                                           |
| async_tree_io_tg          | 499 ms                                                          | 547 ms: 1.10x slower                                                            |
| unpickle_pure_python      | 162 us                                                          | 178 us: 1.10x slower                                                            |
| xml_etree_parse           | 102 ms                                                          | 113 ms: 1.10x slower                                                            |
| spectral_norm             | 70.0 ms                                                         | 77.7 ms: 1.11x slower                                                           |
| xml_etree_generate        | 61.9 ms                                                         | 68.8 ms: 1.11x slower                                                           |
| hexiom                    | 4.60 ms                                                         | 5.11 ms: 1.11x slower                                                           |
| pickle_pure_python        | 239 us                                                          | 267 us: 1.12x slower                                                            |
| xml_etree_iterparse       | 61.3 ms                                                         | 68.5 ms: 1.12x slower                                                           |
| scimark_sparse_mat_mult   | 2.88 ms                                                         | 3.23 ms: 1.12x slower                                                           |
| async_generators          | 267 ms                                                          | 300 ms: 1.12x slower                                                            |
| logging_silent            | 62.4 ns                                                         | 70.5 ns: 1.13x slower                                                           |
| xml_etree_process         | 44.6 ms                                                         | 50.5 ms: 1.13x slower                                                           |
| generators                | 21.5 ms                                                         | 24.4 ms: 1.13x slower                                                           |
| deltablue                 | 2.35 ms                                                         | 2.67 ms: 1.14x slower                                                           |
| scimark_fft               | 204 ms                                                          | 233 ms: 1.14x slower                                                            |
| scimark_lu                | 60.7 ms                                                         | 69.5 ms: 1.14x slower                                                           |
| richards                  | 33.4 ms                                                         | 38.4 ms: 1.15x slower                                                           |
| scimark_monte_carlo       | 48.7 ms                                                         | 56.2 ms: 1.15x slower                                                           |
| pyflate                   | 322 ms                                                          | 373 ms: 1.16x slower                                                            |
| json_dumps                | 7.53 ms                                                         | 8.75 ms: 1.16x slower                                                           |
| nbody                     | 81.4 ms                                                         | 95.8 ms: 1.18x slower                                                           |
| chaos                     | 49.4 ms                                                         | 58.8 ms: 1.19x slower                                                           |
| richards_super            | 37.0 ms                                                         | 44.3 ms: 1.20x slower                                                           |
| raytrace                  | 203 ms                                                          | 249 ms: 1.23x slower                                                            |
| scimark_sor               | 85.8 ms                                                         | 109 ms: 1.27x slower                                                            |
| k_core                    | 1.43 sec                                                        | 2.01 sec: 1.40x slower                                                          |
| Geometric mean            | (ref)                                                           | 1.01x faster                                                                    |

Benchmark hidden because not significant (5): bench_thread_pool, async_tree_cpu_io_mixed_tg, sympy_str, gc_traversal, pylint
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (1) of results/bm-20241109-3.14.0a1+-9d08423/bm-20241109-pythonperf1_win32-x86-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423.json: sqlite_synth

- Geometric mean (including insignificant results): 1.012x faster
# HPT report

- Reliability score: 99.73% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown