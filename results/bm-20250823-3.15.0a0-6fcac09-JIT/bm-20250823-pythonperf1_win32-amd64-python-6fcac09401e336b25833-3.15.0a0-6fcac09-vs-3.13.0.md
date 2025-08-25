# Results vs. 3.13.0

- fork: python
- ref: 6fcac09401e336b25833
- machine: windows-amd64
- commit hash: 6fcac09
- commit date: 2025-08-23
- overall geometric mean: 1.317x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.21x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250823-pythonperf1_win32-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 250 ms                                                          | 214 ms: 1.17x faster                                                             |
| docutils       | 1.78 sec                                                        | 1.61 sec: 1.11x faster                                                           |
| html5lib       | 47.5 ms                                                         | 37.8 ms: 1.26x faster                                                            |
| sphinx         | 719 ms                                                          | 620 ms: 1.16x faster                                                             |
| Geometric mean | (ref)                                                           | 1.17x faster                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250823-pythonperf1_win32-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09 |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| asyncio_websockets         | 363 ms                                                          | 161 ms: 2.26x faster                                                             |
| async_tree_memoization     | 297 ms                                                          | 201 ms: 1.48x faster                                                             |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 329 ms: 1.47x faster                                                             |
| async_tree_none            | 245 ms                                                          | 170 ms: 1.44x faster                                                             |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 333 ms: 1.37x faster                                                             |
| async_tree_memoization_tg  | 282 ms                                                          | 208 ms: 1.35x faster                                                             |
| async_tree_io              | 526 ms                                                          | 389 ms: 1.35x faster                                                             |
| async_tree_io_tg           | 494 ms                                                          | 381 ms: 1.30x faster                                                             |
| async_tree_none_tg         | 214 ms                                                          | 166 ms: 1.29x faster                                                             |
| coroutines                 | 16.2 ms                                                         | 14.0 ms: 1.16x faster                                                            |
| async_generators           | 270 ms                                                          | 245 ms: 1.10x faster                                                             |
| Geometric mean             | (ref)                                                           | 1.39x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250823-pythonperf1_win32-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| nbody          | 80.0 ms                                                         | 53.0 ms: 1.51x faster                                                            |
| pidigits       | 201 ms                                                          | 145 ms: 1.39x faster                                                             |
| float          | 54.6 ms                                                         | 43.6 ms: 1.25x faster                                                            |
| Geometric mean | (ref)                                                           | 1.38x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250823-pythonperf1_win32-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 101 ms                                                          | 78.1 ms: 1.29x faster                                                            |
| regex_v8       | 16.8 ms                                                         | 13.1 ms: 1.28x faster                                                            |
| regex_effbot   | 1.80 ms                                                         | 1.57 ms: 1.15x faster                                                            |
| regex_dna      | 114 ms                                                          | 116 ms: 1.02x slower                                                             |
| Geometric mean | (ref)                                                           | 1.17x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250823-pythonperf1_win32-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09 |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| tomli_loads          | 1.71 sec                                                        | 1.09 sec: 1.57x faster                                                           |
| json_loads           | 21.6 us                                                         | 13.9 us: 1.55x faster                                                            |
| unpickle_pure_python | 160 us                                                          | 104 us: 1.54x faster                                                             |
| json_dumps           | 7.30 ms                                                         | 5.38 ms: 1.36x faster                                                            |
| xml_etree_parse      | 107 ms                                                          | 85.5 ms: 1.26x faster                                                            |
| xml_etree_process    | 44.2 ms                                                         | 35.4 ms: 1.25x faster                                                            |
| xml_etree_generate   | 61.4 ms                                                         | 51.1 ms: 1.20x faster                                                            |
| pickle_pure_python   | 231 us                                                          | 201 us: 1.15x faster                                                             |
| xml_etree_iterparse  | 62.6 ms                                                         | 61.6 ms: 1.02x faster                                                            |
| Geometric mean       | (ref)                                                           | 1.31x faster                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250823-pythonperf1_win32-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09 |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup         | 28.3 ms                                                         | 25.2 ms: 1.12x faster                                                            |
| python_startup_no_site | 19.7 ms                                                         | 18.9 ms: 1.04x faster                                                            |
| Geometric mean         | (ref)                                                           | 1.08x faster                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250823-pythonperf1_win32-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09 |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| genshi_xml      | 50.1 ms                                                         | 34.5 ms: 1.45x faster                                                            |
| genshi_text     | 21.5 ms                                                         | 15.6 ms: 1.38x faster                                                            |
| mako            | 7.09 ms                                                         | 5.20 ms: 1.36x faster                                                            |
| django_template | 29.8 ms                                                         | 24.1 ms: 1.23x faster                                                            |
| Geometric mean  | (ref)                                                           | 1.35x faster                                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250823-pythonperf1_win32-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09 |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| thrift                     | 9.98 ms                                                         | 506 us: 19.71x faster                                                            |
| coverage                   | 324 ms                                                          | 50.1 ms: 6.46x faster                                                            |
| pathlib                    | 82.9 ms                                                         | 30.1 ms: 2.75x faster                                                            |
| asyncio_websockets         | 363 ms                                                          | 161 ms: 2.26x faster                                                             |
| mdp                        | 1.62 sec                                                        | 788 ms: 2.06x faster                                                             |
| deepcopy                   | 314 us                                                          | 170 us: 1.85x faster                                                             |
| telco                      | 6.96 ms                                                         | 3.82 ms: 1.82x faster                                                            |
| deepcopy_reduce            | 2.92 us                                                         | 1.85 us: 1.58x faster                                                            |
| tomli_loads                | 1.71 sec                                                        | 1.09 sec: 1.57x faster                                                           |
| pprint_pformat             | 1.33 sec                                                        | 851 ms: 1.56x faster                                                             |
| pprint_safe_repr           | 648 ms                                                          | 417 ms: 1.55x faster                                                             |
| json_loads                 | 21.6 us                                                         | 13.9 us: 1.55x faster                                                            |
| unpickle_pure_python       | 160 us                                                          | 104 us: 1.54x faster                                                             |
| nbody                      | 80.0 ms                                                         | 53.0 ms: 1.51x faster                                                            |
| async_tree_memoization     | 297 ms                                                          | 201 ms: 1.48x faster                                                             |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 329 ms: 1.47x faster                                                             |
| genshi_xml                 | 50.1 ms                                                         | 34.5 ms: 1.45x faster                                                            |
| async_tree_none            | 245 ms                                                          | 170 ms: 1.44x faster                                                             |
| json                       | 4.27 ms                                                         | 2.98 ms: 1.43x faster                                                            |
| go                         | 109 ms                                                          | 76.8 ms: 1.42x faster                                                            |
| fannkuch                   | 299 ms                                                          | 212 ms: 1.41x faster                                                             |
| pidigits                   | 201 ms                                                          | 145 ms: 1.39x faster                                                             |
| genshi_text                | 21.5 ms                                                         | 15.6 ms: 1.38x faster                                                            |
| scimark_fft                | 205 ms                                                          | 149 ms: 1.37x faster                                                             |
| bpe_tokeniser              | 3.46 sec                                                        | 2.53 sec: 1.37x faster                                                           |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 333 ms: 1.37x faster                                                             |
| mako                       | 7.09 ms                                                         | 5.20 ms: 1.36x faster                                                            |
| typing_runtime_protocols   | 138 us                                                          | 101 us: 1.36x faster                                                             |
| json_dumps                 | 7.30 ms                                                         | 5.38 ms: 1.36x faster                                                            |
| async_tree_memoization_tg  | 282 ms                                                          | 208 ms: 1.35x faster                                                             |
| logging_format             | 8.72 us                                                         | 6.44 us: 1.35x faster                                                            |
| async_tree_io              | 526 ms                                                          | 389 ms: 1.35x faster                                                             |
| logging_simple             | 7.99 us                                                         | 6.05 us: 1.32x faster                                                            |
| async_tree_io_tg           | 494 ms                                                          | 381 ms: 1.30x faster                                                             |
| sympy_expand               | 373 ms                                                          | 288 ms: 1.30x faster                                                             |
| regex_compile              | 101 ms                                                          | 78.1 ms: 1.29x faster                                                            |
| async_tree_none_tg         | 214 ms                                                          | 166 ms: 1.29x faster                                                             |
| sqlite_synth               | 1.95 us                                                         | 1.52 us: 1.29x faster                                                            |
| pycparser                  | 872 ms                                                          | 678 ms: 1.29x faster                                                             |
| regex_v8                   | 16.8 ms                                                         | 13.1 ms: 1.28x faster                                                            |
| deepcopy_memo              | 25.4 us                                                         | 19.8 us: 1.28x faster                                                            |
| crypto_pyaes               | 56.9 ms                                                         | 44.6 ms: 1.28x faster                                                            |
| sympy_str                  | 212 ms                                                          | 167 ms: 1.27x faster                                                             |
| html5lib                   | 47.5 ms                                                         | 37.8 ms: 1.26x faster                                                            |
| xml_etree_parse            | 107 ms                                                          | 85.5 ms: 1.26x faster                                                            |
| float                      | 54.6 ms                                                         | 43.6 ms: 1.25x faster                                                            |
| scimark_sparse_mat_mult    | 2.84 ms                                                         | 2.27 ms: 1.25x faster                                                            |
| xml_etree_process          | 44.2 ms                                                         | 35.4 ms: 1.25x faster                                                            |
| dulwich_log                | 48.8 ms                                                         | 39.1 ms: 1.25x faster                                                            |
| sympy_sum                  | 106 ms                                                          | 85.5 ms: 1.23x faster                                                            |
| django_template            | 29.8 ms                                                         | 24.1 ms: 1.23x faster                                                            |
| chaos                      | 50.2 ms                                                         | 41.1 ms: 1.22x faster                                                            |
| richards                   | 32.7 ms                                                         | 26.7 ms: 1.22x faster                                                            |
| richards_super             | 36.7 ms                                                         | 30.1 ms: 1.22x faster                                                            |
| sympy_integrate            | 15.0 ms                                                         | 12.3 ms: 1.22x faster                                                            |
| comprehensions             | 12.5 us                                                         | 10.3 us: 1.22x faster                                                            |
| nqueens                    | 72.1 ms                                                         | 59.7 ms: 1.21x faster                                                            |
| xml_etree_generate         | 61.4 ms                                                         | 51.1 ms: 1.20x faster                                                            |
| bench_thread_pool          | 1.00 ms                                                         | 835 us: 1.20x faster                                                             |
| pyflate                    | 320 ms                                                          | 268 ms: 1.19x faster                                                             |
| scimark_monte_carlo        | 47.7 ms                                                         | 40.3 ms: 1.18x faster                                                            |
| pylint                     | 227 ms                                                          | 192 ms: 1.18x faster                                                             |
| raytrace                   | 201 ms                                                          | 172 ms: 1.17x faster                                                             |
| 2to3                       | 250 ms                                                          | 214 ms: 1.17x faster                                                             |
| coroutines                 | 16.2 ms                                                         | 14.0 ms: 1.16x faster                                                            |
| sphinx                     | 719 ms                                                          | 620 ms: 1.16x faster                                                             |
| pickle_pure_python         | 231 us                                                          | 201 us: 1.15x faster                                                             |
| regex_effbot               | 1.80 ms                                                         | 1.57 ms: 1.15x faster                                                            |
| generators                 | 21.8 ms                                                         | 19.2 ms: 1.13x faster                                                            |
| spectral_norm              | 69.4 ms                                                         | 61.5 ms: 1.13x faster                                                            |
| python_startup             | 28.3 ms                                                         | 25.2 ms: 1.12x faster                                                            |
| hexiom                     | 4.44 ms                                                         | 3.95 ms: 1.12x faster                                                            |
| scimark_sor                | 85.9 ms                                                         | 77.1 ms: 1.11x faster                                                            |
| logging_silent             | 60.3 ns                                                         | 54.4 ns: 1.11x faster                                                            |
| docutils                   | 1.78 sec                                                        | 1.61 sec: 1.11x faster                                                           |
| async_generators           | 270 ms                                                          | 245 ms: 1.10x faster                                                             |
| meteor_contest             | 74.6 ms                                                         | 70.4 ms: 1.06x faster                                                            |
| deltablue                  | 2.33 ms                                                         | 2.22 ms: 1.05x faster                                                            |
| python_startup_no_site     | 19.7 ms                                                         | 18.9 ms: 1.04x faster                                                            |
| xml_etree_iterparse        | 62.6 ms                                                         | 61.6 ms: 1.02x faster                                                            |
| scimark_lu                 | 60.2 ms                                                         | 59.7 ms: 1.01x faster                                                            |
| regex_dna                  | 114 ms                                                          | 116 ms: 1.02x slower                                                             |
| bench_mp_pool              | 90.6 ms                                                         | 92.0 ms: 1.02x slower                                                            |
| k_core                     | 1.38 sec                                                        | 1.58 sec: 1.15x slower                                                           |
| connected_components       | 267 ms                                                          | 312 ms: 1.17x slower                                                             |
| create_gc_cycles           | 1.06 ms                                                         | 1.26 ms: 1.19x slower                                                            |
| shortest_path              | 290 ms                                                          | 345 ms: 1.19x slower                                                             |
| gc_traversal               | 1.75 ms                                                         | 2.12 ms: 1.21x slower                                                            |
| many_optionals             | 436 us                                                          | 554 us: 1.27x slower                                                             |
| subparsers                 | 14.8 ms                                                         | 29.2 ms: 1.98x slower                                                            |
| Geometric mean             | (ref)                                                           | 1.31x faster                                                                     |
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250823-3.15.0a0-6fcac09-JIT/bm-20250823-pythonperf1_win32-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.317x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.23x
- 95% likely to have a speedup of 1.22x
- 99% likely to have a speedup of 1.21x

# Memory
- memory change: unknown