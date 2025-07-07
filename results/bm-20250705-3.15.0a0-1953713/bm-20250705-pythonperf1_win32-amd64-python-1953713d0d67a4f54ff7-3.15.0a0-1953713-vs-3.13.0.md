# Results vs. 3.13.0

- fork: python
- ref: 1953713d0d67a4f54ff7
- machine: windows-amd64
- commit hash: 1953713
- commit date: 2025-07-05
- overall geometric mean: 1.281x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.16x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250705-pythonperf1_win32-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 250 ms                                                          | 219 ms: 1.14x faster                                                             |
| docutils       | 1.78 sec                                                        | 1.60 sec: 1.11x faster                                                           |
| html5lib       | 47.5 ms                                                         | 37.6 ms: 1.26x faster                                                            |
| sphinx         | 719 ms                                                          | 632 ms: 1.14x faster                                                             |
| Geometric mean | (ref)                                                           | 1.16x faster                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250705-pythonperf1_win32-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713 |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| asyncio_websockets         | 363 ms                                                          | 156 ms: 2.33x faster                                                             |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 331 ms: 1.46x faster                                                             |
| async_tree_none            | 245 ms                                                          | 172 ms: 1.43x faster                                                             |
| async_tree_memoization     | 297 ms                                                          | 209 ms: 1.42x faster                                                             |
| async_tree_memoization_tg  | 282 ms                                                          | 208 ms: 1.36x faster                                                             |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 339 ms: 1.34x faster                                                             |
| async_tree_io              | 526 ms                                                          | 399 ms: 1.32x faster                                                             |
| async_tree_none_tg         | 214 ms                                                          | 167 ms: 1.28x faster                                                             |
| async_tree_io_tg           | 494 ms                                                          | 387 ms: 1.28x faster                                                             |
| async_generators           | 270 ms                                                          | 231 ms: 1.17x faster                                                             |
| coroutines                 | 16.2 ms                                                         | 14.6 ms: 1.11x faster                                                            |
| Geometric mean             | (ref)                                                           | 1.38x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250705-pythonperf1_win32-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pidigits       | 201 ms                                                          | 145 ms: 1.39x faster                                                             |
| nbody          | 80.0 ms                                                         | 62.4 ms: 1.28x faster                                                            |
| float          | 54.6 ms                                                         | 43.1 ms: 1.27x faster                                                            |
| Geometric mean | (ref)                                                           | 1.31x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250705-pythonperf1_win32-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 101 ms                                                          | 78.9 ms: 1.28x faster                                                            |
| regex_v8       | 16.8 ms                                                         | 14.1 ms: 1.20x faster                                                            |
| regex_effbot   | 1.80 ms                                                         | 1.58 ms: 1.14x faster                                                            |
| regex_dna      | 114 ms                                                          | 120 ms: 1.06x slower                                                             |
| Geometric mean | (ref)                                                           | 1.13x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250705-pythonperf1_win32-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713 |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| json_loads           | 21.6 us                                                         | 14.2 us: 1.53x faster                                                            |
| tomli_loads          | 1.71 sec                                                        | 1.36 sec: 1.26x faster                                                           |
| xml_etree_parse      | 107 ms                                                          | 89.0 ms: 1.21x faster                                                            |
| unpickle_pure_python | 160 us                                                          | 133 us: 1.20x faster                                                             |
| xml_etree_process    | 44.2 ms                                                         | 38.0 ms: 1.16x faster                                                            |
| json_dumps           | 7.30 ms                                                         | 6.29 ms: 1.16x faster                                                            |
| pickle_pure_python   | 231 us                                                          | 208 us: 1.11x faster                                                             |
| xml_etree_generate   | 61.4 ms                                                         | 55.3 ms: 1.11x faster                                                            |
| xml_etree_iterparse  | 62.6 ms                                                         | 64.8 ms: 1.04x slower                                                            |
| Geometric mean       | (ref)                                                           | 1.18x faster                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250705-pythonperf1_win32-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713 |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup         | 28.3 ms                                                         | 25.6 ms: 1.10x faster                                                            |
| python_startup_no_site | 19.7 ms                                                         | 19.4 ms: 1.01x faster                                                            |
| Geometric mean         | (ref)                                                           | 1.06x faster                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250705-pythonperf1_win32-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713 |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| genshi_xml      | 50.1 ms                                                         | 34.0 ms: 1.48x faster                                                            |
| genshi_text     | 21.5 ms                                                         | 15.1 ms: 1.42x faster                                                            |
| django_template | 29.8 ms                                                         | 24.4 ms: 1.22x faster                                                            |
| mako            | 7.09 ms                                                         | 6.48 ms: 1.09x faster                                                            |
| Geometric mean  | (ref)                                                           | 1.29x faster                                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250705-pythonperf1_win32-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713 |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| thrift                     | 9.98 ms                                                         | 496 us: 20.11x faster                                                            |
| coverage                   | 324 ms                                                          | 49.9 ms: 6.50x faster                                                            |
| pathlib                    | 82.9 ms                                                         | 32.1 ms: 2.58x faster                                                            |
| asyncio_websockets         | 363 ms                                                          | 156 ms: 2.33x faster                                                             |
| mdp                        | 1.62 sec                                                        | 805 ms: 2.02x faster                                                             |
| deepcopy                   | 314 us                                                          | 169 us: 1.86x faster                                                             |
| deepcopy_reduce            | 2.92 us                                                         | 1.83 us: 1.60x faster                                                            |
| telco                      | 6.96 ms                                                         | 4.54 ms: 1.54x faster                                                            |
| json_loads                 | 21.6 us                                                         | 14.2 us: 1.53x faster                                                            |
| genshi_xml                 | 50.1 ms                                                         | 34.0 ms: 1.48x faster                                                            |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 331 ms: 1.46x faster                                                             |
| deepcopy_memo              | 25.4 us                                                         | 17.4 us: 1.46x faster                                                            |
| json                       | 4.27 ms                                                         | 2.96 ms: 1.44x faster                                                            |
| go                         | 109 ms                                                          | 75.9 ms: 1.43x faster                                                            |
| async_tree_none            | 245 ms                                                          | 172 ms: 1.43x faster                                                             |
| async_tree_memoization     | 297 ms                                                          | 209 ms: 1.42x faster                                                             |
| genshi_text                | 21.5 ms                                                         | 15.1 ms: 1.42x faster                                                            |
| pidigits                   | 201 ms                                                          | 145 ms: 1.39x faster                                                             |
| typing_runtime_protocols   | 138 us                                                          | 101 us: 1.36x faster                                                             |
| async_tree_memoization_tg  | 282 ms                                                          | 208 ms: 1.36x faster                                                             |
| pprint_pformat             | 1.33 sec                                                        | 980 ms: 1.36x faster                                                             |
| pprint_safe_repr           | 648 ms                                                          | 481 ms: 1.35x faster                                                             |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 339 ms: 1.34x faster                                                             |
| async_tree_io              | 526 ms                                                          | 399 ms: 1.32x faster                                                             |
| logging_format             | 8.72 us                                                         | 6.62 us: 1.32x faster                                                            |
| sympy_expand               | 373 ms                                                          | 286 ms: 1.31x faster                                                             |
| logging_simple             | 7.99 us                                                         | 6.15 us: 1.30x faster                                                            |
| async_tree_none_tg         | 214 ms                                                          | 167 ms: 1.28x faster                                                             |
| nbody                      | 80.0 ms                                                         | 62.4 ms: 1.28x faster                                                            |
| regex_compile              | 101 ms                                                          | 78.9 ms: 1.28x faster                                                            |
| async_tree_io_tg           | 494 ms                                                          | 387 ms: 1.28x faster                                                             |
| sympy_str                  | 212 ms                                                          | 167 ms: 1.27x faster                                                             |
| float                      | 54.6 ms                                                         | 43.1 ms: 1.27x faster                                                            |
| html5lib                   | 47.5 ms                                                         | 37.6 ms: 1.26x faster                                                            |
| chaos                      | 50.2 ms                                                         | 39.7 ms: 1.26x faster                                                            |
| tomli_loads                | 1.71 sec                                                        | 1.36 sec: 1.26x faster                                                           |
| pycparser                  | 872 ms                                                          | 700 ms: 1.25x faster                                                             |
| sqlite_synth               | 1.95 us                                                         | 1.59 us: 1.23x faster                                                            |
| django_template            | 29.8 ms                                                         | 24.4 ms: 1.22x faster                                                            |
| sympy_integrate            | 15.0 ms                                                         | 12.3 ms: 1.22x faster                                                            |
| sympy_sum                  | 106 ms                                                          | 86.6 ms: 1.22x faster                                                            |
| richards                   | 32.7 ms                                                         | 26.9 ms: 1.21x faster                                                            |
| scimark_monte_carlo        | 47.7 ms                                                         | 39.3 ms: 1.21x faster                                                            |
| crypto_pyaes               | 56.9 ms                                                         | 47.1 ms: 1.21x faster                                                            |
| xml_etree_parse            | 107 ms                                                          | 89.0 ms: 1.21x faster                                                            |
| unpickle_pure_python       | 160 us                                                          | 133 us: 1.20x faster                                                             |
| richards_super             | 36.7 ms                                                         | 30.5 ms: 1.20x faster                                                            |
| regex_v8                   | 16.8 ms                                                         | 14.1 ms: 1.20x faster                                                            |
| bench_thread_pool          | 1.00 ms                                                         | 837 us: 1.20x faster                                                             |
| dulwich_log                | 48.8 ms                                                         | 40.8 ms: 1.19x faster                                                            |
| nqueens                    | 72.1 ms                                                         | 61.0 ms: 1.18x faster                                                            |
| comprehensions             | 12.5 us                                                         | 10.6 us: 1.18x faster                                                            |
| bpe_tokeniser              | 3.46 sec                                                        | 2.96 sec: 1.17x faster                                                           |
| async_generators           | 270 ms                                                          | 231 ms: 1.17x faster                                                             |
| xml_etree_process          | 44.2 ms                                                         | 38.0 ms: 1.16x faster                                                            |
| json_dumps                 | 7.30 ms                                                         | 6.29 ms: 1.16x faster                                                            |
| pylint                     | 227 ms                                                          | 197 ms: 1.15x faster                                                             |
| fannkuch                   | 299 ms                                                          | 260 ms: 1.15x faster                                                             |
| 2to3                       | 250 ms                                                          | 219 ms: 1.14x faster                                                             |
| scimark_fft                | 205 ms                                                          | 180 ms: 1.14x faster                                                             |
| regex_effbot               | 1.80 ms                                                         | 1.58 ms: 1.14x faster                                                            |
| raytrace                   | 201 ms                                                          | 177 ms: 1.14x faster                                                             |
| sphinx                     | 719 ms                                                          | 632 ms: 1.14x faster                                                             |
| scimark_sor                | 85.9 ms                                                         | 75.7 ms: 1.13x faster                                                            |
| generators                 | 21.8 ms                                                         | 19.5 ms: 1.12x faster                                                            |
| scimark_sparse_mat_mult    | 2.84 ms                                                         | 2.54 ms: 1.12x faster                                                            |
| coroutines                 | 16.2 ms                                                         | 14.6 ms: 1.11x faster                                                            |
| pickle_pure_python         | 231 us                                                          | 208 us: 1.11x faster                                                             |
| xml_etree_generate         | 61.4 ms                                                         | 55.3 ms: 1.11x faster                                                            |
| docutils                   | 1.78 sec                                                        | 1.60 sec: 1.11x faster                                                           |
| hexiom                     | 4.44 ms                                                         | 4.01 ms: 1.11x faster                                                            |
| python_startup             | 28.3 ms                                                         | 25.6 ms: 1.10x faster                                                            |
| spectral_norm              | 69.4 ms                                                         | 62.9 ms: 1.10x faster                                                            |
| deltablue                  | 2.33 ms                                                         | 2.12 ms: 1.10x faster                                                            |
| pyflate                    | 320 ms                                                          | 292 ms: 1.10x faster                                                             |
| logging_silent             | 60.3 ns                                                         | 55.1 ns: 1.10x faster                                                            |
| mako                       | 7.09 ms                                                         | 6.48 ms: 1.09x faster                                                            |
| scimark_lu                 | 60.2 ms                                                         | 57.2 ms: 1.05x faster                                                            |
| meteor_contest             | 74.6 ms                                                         | 71.5 ms: 1.04x faster                                                            |
| python_startup_no_site     | 19.7 ms                                                         | 19.4 ms: 1.01x faster                                                            |
| many_optionals             | 436 us                                                          | 431 us: 1.01x faster                                                             |
| xml_etree_iterparse        | 62.6 ms                                                         | 64.8 ms: 1.04x slower                                                            |
| bench_mp_pool              | 90.6 ms                                                         | 95.1 ms: 1.05x slower                                                            |
| regex_dna                  | 114 ms                                                          | 120 ms: 1.06x slower                                                             |
| subparsers                 | 14.8 ms                                                         | 16.9 ms: 1.15x slower                                                            |
| gc_traversal               | 1.75 ms                                                         | 2.14 ms: 1.22x slower                                                            |
| connected_components       | 267 ms                                                          | 331 ms: 1.24x slower                                                             |
| k_core                     | 1.38 sec                                                        | 1.71 sec: 1.25x slower                                                           |
| create_gc_cycles           | 1.06 ms                                                         | 1.32 ms: 1.25x slower                                                            |
| shortest_path              | 290 ms                                                          | 364 ms: 1.26x slower                                                             |
| Geometric mean             | (ref)                                                           | 1.28x faster                                                                     |
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250705-3.15.0a0-1953713/bm-20250705-pythonperf1_win32-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.281x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.18x
- 95% likely to have a speedup of 1.17x
- 99% likely to have a speedup of 1.16x

# Memory
- memory change: unknown