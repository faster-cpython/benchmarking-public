# Results vs. 3.13.0

- fork: python
- ref: 880c9526f91960b9cba5
- machine: windows-amd64
- commit hash: 880c952
- commit date: 2025-10-04
- overall geometric mean: 1.275x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.16x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20251004-pythonperf1_win32-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 250 ms                                                          | 217 ms: 1.15x faster                                                             |
| docutils       | 1.78 sec                                                        | 1.60 sec: 1.11x faster                                                           |
| html5lib       | 47.5 ms                                                         | 37.6 ms: 1.26x faster                                                            |
| sphinx         | 719 ms                                                          | 627 ms: 1.15x faster                                                             |
| Geometric mean | (ref)                                                           | 1.17x faster                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20251004-pythonperf1_win32-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952 |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| asyncio_websockets         | 363 ms                                                          | 161 ms: 2.25x faster                                                             |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 327 ms: 1.48x faster                                                             |
| async_tree_memoization     | 297 ms                                                          | 204 ms: 1.45x faster                                                             |
| async_tree_none            | 245 ms                                                          | 175 ms: 1.40x faster                                                             |
| async_tree_io              | 526 ms                                                          | 386 ms: 1.36x faster                                                             |
| async_tree_memoization_tg  | 282 ms                                                          | 209 ms: 1.35x faster                                                             |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 341 ms: 1.34x faster                                                             |
| async_tree_io_tg           | 494 ms                                                          | 388 ms: 1.27x faster                                                             |
| async_tree_none_tg         | 214 ms                                                          | 169 ms: 1.27x faster                                                             |
| async_generators           | 270 ms                                                          | 230 ms: 1.17x faster                                                             |
| coroutines                 | 16.2 ms                                                         | 14.8 ms: 1.09x faster                                                            |
| Geometric mean             | (ref)                                                           | 1.38x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20251004-pythonperf1_win32-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pidigits       | 201 ms                                                          | 146 ms: 1.38x faster                                                             |
| nbody          | 80.0 ms                                                         | 63.5 ms: 1.26x faster                                                            |
| float          | 54.6 ms                                                         | 43.4 ms: 1.26x faster                                                            |
| Geometric mean | (ref)                                                           | 1.30x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20251004-pythonperf1_win32-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 101 ms                                                          | 80.1 ms: 1.26x faster                                                            |
| regex_v8       | 16.8 ms                                                         | 14.0 ms: 1.20x faster                                                            |
| regex_effbot   | 1.80 ms                                                         | 1.56 ms: 1.16x faster                                                            |
| regex_dna      | 114 ms                                                          | 120 ms: 1.05x slower                                                             |
| Geometric mean | (ref)                                                           | 1.14x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20251004-pythonperf1_win32-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952 |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| json_loads           | 21.6 us                                                         | 14.0 us: 1.55x faster                                                            |
| json_dumps           | 7.30 ms                                                         | 5.50 ms: 1.33x faster                                                            |
| tomli_loads          | 1.71 sec                                                        | 1.37 sec: 1.25x faster                                                           |
| xml_etree_parse      | 107 ms                                                          | 86.5 ms: 1.24x faster                                                            |
| unpickle_pure_python | 160 us                                                          | 135 us: 1.18x faster                                                             |
| xml_etree_process    | 44.2 ms                                                         | 38.6 ms: 1.14x faster                                                            |
| xml_etree_generate   | 61.4 ms                                                         | 55.2 ms: 1.11x faster                                                            |
| pickle_pure_python   | 231 us                                                          | 210 us: 1.10x faster                                                             |
| Geometric mean       | (ref)                                                           | 1.20x faster                                                                     |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20251004-pythonperf1_win32-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952 |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup         | 28.3 ms                                                         | 25.3 ms: 1.12x faster                                                            |
| python_startup_no_site | 19.7 ms                                                         | 19.1 ms: 1.03x faster                                                            |
| Geometric mean         | (ref)                                                           | 1.07x faster                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20251004-pythonperf1_win32-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952 |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| genshi_xml      | 50.1 ms                                                         | 34.5 ms: 1.46x faster                                                            |
| genshi_text     | 21.5 ms                                                         | 15.4 ms: 1.40x faster                                                            |
| django_template | 29.8 ms                                                         | 24.4 ms: 1.22x faster                                                            |
| mako            | 7.09 ms                                                         | 6.80 ms: 1.04x faster                                                            |
| Geometric mean  | (ref)                                                           | 1.27x faster                                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20251004-pythonperf1_win32-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952 |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| thrift                     | 9.98 ms                                                         | 501 us: 19.92x faster                                                            |
| coverage                   | 324 ms                                                          | 49.0 ms: 6.60x faster                                                            |
| pathlib                    | 82.9 ms                                                         | 29.1 ms: 2.85x faster                                                            |
| asyncio_websockets         | 363 ms                                                          | 161 ms: 2.25x faster                                                             |
| mdp                        | 1.62 sec                                                        | 798 ms: 2.03x faster                                                             |
| deepcopy                   | 314 us                                                          | 167 us: 1.88x faster                                                             |
| telco                      | 6.96 ms                                                         | 4.18 ms: 1.66x faster                                                            |
| deepcopy_reduce            | 2.92 us                                                         | 1.81 us: 1.61x faster                                                            |
| json_loads                 | 21.6 us                                                         | 14.0 us: 1.55x faster                                                            |
| deepcopy_memo              | 25.4 us                                                         | 16.7 us: 1.52x faster                                                            |
| json                       | 4.27 ms                                                         | 2.88 ms: 1.48x faster                                                            |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 327 ms: 1.48x faster                                                             |
| genshi_xml                 | 50.1 ms                                                         | 34.5 ms: 1.46x faster                                                            |
| async_tree_memoization     | 297 ms                                                          | 204 ms: 1.45x faster                                                             |
| go                         | 109 ms                                                          | 77.6 ms: 1.40x faster                                                            |
| genshi_text                | 21.5 ms                                                         | 15.4 ms: 1.40x faster                                                            |
| async_tree_none            | 245 ms                                                          | 175 ms: 1.40x faster                                                             |
| pidigits                   | 201 ms                                                          | 146 ms: 1.38x faster                                                             |
| async_tree_io              | 526 ms                                                          | 386 ms: 1.36x faster                                                             |
| logging_format             | 8.72 us                                                         | 6.43 us: 1.36x faster                                                            |
| async_tree_memoization_tg  | 282 ms                                                          | 209 ms: 1.35x faster                                                             |
| logging_simple             | 7.99 us                                                         | 5.92 us: 1.35x faster                                                            |
| pprint_pformat             | 1.33 sec                                                        | 986 ms: 1.35x faster                                                             |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 341 ms: 1.34x faster                                                             |
| pprint_safe_repr           | 648 ms                                                          | 488 ms: 1.33x faster                                                             |
| json_dumps                 | 7.30 ms                                                         | 5.50 ms: 1.33x faster                                                            |
| sympy_expand               | 373 ms                                                          | 282 ms: 1.32x faster                                                             |
| typing_runtime_protocols   | 138 us                                                          | 105 us: 1.31x faster                                                             |
| sympy_str                  | 212 ms                                                          | 165 ms: 1.28x faster                                                             |
| async_tree_io_tg           | 494 ms                                                          | 388 ms: 1.27x faster                                                             |
| async_tree_none_tg         | 214 ms                                                          | 169 ms: 1.27x faster                                                             |
| html5lib                   | 47.5 ms                                                         | 37.6 ms: 1.26x faster                                                            |
| regex_compile              | 101 ms                                                          | 80.1 ms: 1.26x faster                                                            |
| nbody                      | 80.0 ms                                                         | 63.5 ms: 1.26x faster                                                            |
| float                      | 54.6 ms                                                         | 43.4 ms: 1.26x faster                                                            |
| tomli_loads                | 1.71 sec                                                        | 1.37 sec: 1.25x faster                                                           |
| dulwich_log                | 48.8 ms                                                         | 39.1 ms: 1.25x faster                                                            |
| sqlite_synth               | 1.95 us                                                         | 1.57 us: 1.25x faster                                                            |
| sympy_sum                  | 106 ms                                                          | 84.9 ms: 1.24x faster                                                            |
| xml_etree_parse            | 107 ms                                                          | 86.5 ms: 1.24x faster                                                            |
| chaos                      | 50.2 ms                                                         | 40.5 ms: 1.24x faster                                                            |
| sympy_integrate            | 15.0 ms                                                         | 12.2 ms: 1.23x faster                                                            |
| pycparser                  | 872 ms                                                          | 712 ms: 1.22x faster                                                             |
| django_template            | 29.8 ms                                                         | 24.4 ms: 1.22x faster                                                            |
| scimark_fft                | 205 ms                                                          | 168 ms: 1.22x faster                                                             |
| regex_v8                   | 16.8 ms                                                         | 14.0 ms: 1.20x faster                                                            |
| richards                   | 32.7 ms                                                         | 27.2 ms: 1.20x faster                                                            |
| richards_super             | 36.7 ms                                                         | 30.6 ms: 1.20x faster                                                            |
| crypto_pyaes               | 56.9 ms                                                         | 47.7 ms: 1.19x faster                                                            |
| bench_thread_pool          | 1.00 ms                                                         | 846 us: 1.18x faster                                                             |
| unpickle_pure_python       | 160 us                                                          | 135 us: 1.18x faster                                                             |
| pylint                     | 227 ms                                                          | 192 ms: 1.18x faster                                                             |
| scimark_monte_carlo        | 47.7 ms                                                         | 40.6 ms: 1.17x faster                                                            |
| async_generators           | 270 ms                                                          | 230 ms: 1.17x faster                                                             |
| scimark_sparse_mat_mult    | 2.84 ms                                                         | 2.43 ms: 1.17x faster                                                            |
| bpe_tokeniser              | 3.46 sec                                                        | 2.99 sec: 1.16x faster                                                           |
| nqueens                    | 72.1 ms                                                         | 62.3 ms: 1.16x faster                                                            |
| regex_effbot               | 1.80 ms                                                         | 1.56 ms: 1.16x faster                                                            |
| 2to3                       | 250 ms                                                          | 217 ms: 1.15x faster                                                             |
| sphinx                     | 719 ms                                                          | 627 ms: 1.15x faster                                                             |
| xml_etree_process          | 44.2 ms                                                         | 38.6 ms: 1.14x faster                                                            |
| comprehensions             | 12.5 us                                                         | 11.0 us: 1.14x faster                                                            |
| raytrace                   | 201 ms                                                          | 179 ms: 1.12x faster                                                             |
| python_startup             | 28.3 ms                                                         | 25.3 ms: 1.12x faster                                                            |
| fannkuch                   | 299 ms                                                          | 267 ms: 1.12x faster                                                             |
| generators                 | 21.8 ms                                                         | 19.5 ms: 1.12x faster                                                            |
| pyflate                    | 320 ms                                                          | 287 ms: 1.12x faster                                                             |
| xml_etree_generate         | 61.4 ms                                                         | 55.2 ms: 1.11x faster                                                            |
| docutils                   | 1.78 sec                                                        | 1.60 sec: 1.11x faster                                                           |
| pickle_pure_python         | 231 us                                                          | 210 us: 1.10x faster                                                             |
| scimark_sor                | 85.9 ms                                                         | 78.3 ms: 1.10x faster                                                            |
| coroutines                 | 16.2 ms                                                         | 14.8 ms: 1.09x faster                                                            |
| hexiom                     | 4.44 ms                                                         | 4.10 ms: 1.08x faster                                                            |
| logging_silent             | 60.3 ns                                                         | 55.8 ns: 1.08x faster                                                            |
| deltablue                  | 2.33 ms                                                         | 2.19 ms: 1.07x faster                                                            |
| mako                       | 7.09 ms                                                         | 6.80 ms: 1.04x faster                                                            |
| spectral_norm              | 69.4 ms                                                         | 66.9 ms: 1.04x faster                                                            |
| meteor_contest             | 74.6 ms                                                         | 72.1 ms: 1.03x faster                                                            |
| python_startup_no_site     | 19.7 ms                                                         | 19.1 ms: 1.03x faster                                                            |
| scimark_lu                 | 60.2 ms                                                         | 58.9 ms: 1.02x faster                                                            |
| bench_mp_pool              | 90.6 ms                                                         | 89.5 ms: 1.01x faster                                                            |
| regex_dna                  | 114 ms                                                          | 120 ms: 1.05x slower                                                             |
| gc_traversal               | 1.75 ms                                                         | 2.08 ms: 1.19x slower                                                            |
| create_gc_cycles           | 1.06 ms                                                         | 1.26 ms: 1.19x slower                                                            |
| connected_components       | 267 ms                                                          | 320 ms: 1.20x slower                                                             |
| shortest_path              | 290 ms                                                          | 351 ms: 1.21x slower                                                             |
| k_core                     | 1.38 sec                                                        | 1.67 sec: 1.21x slower                                                           |
| many_optionals             | 436 us                                                          | 573 us: 1.31x slower                                                             |
| subparsers                 | 14.8 ms                                                         | 30.9 ms: 2.09x slower                                                            |
| Geometric mean             | (ref)                                                           | 1.27x faster                                                                     |

Benchmark hidden because not significant (1): xml_etree_iterparse
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20251004-3.15.0a0-880c952/bm-20251004-pythonperf1_win32-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.275x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.18x
- 95% likely to have a speedup of 1.17x
- 99% likely to have a speedup of 1.16x

# Memory
- memory change: unknown