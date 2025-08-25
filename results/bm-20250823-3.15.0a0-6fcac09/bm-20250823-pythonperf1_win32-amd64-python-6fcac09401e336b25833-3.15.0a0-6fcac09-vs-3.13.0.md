# Results vs. 3.13.0

- fork: python
- ref: 6fcac09401e336b25833
- machine: windows-amd64
- commit hash: 6fcac09
- commit date: 2025-08-23
- overall geometric mean: 1.282x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.17x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250823-pythonperf1_win32-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 250 ms                                                          | 217 ms: 1.15x faster                                                             |
| docutils       | 1.78 sec                                                        | 1.59 sec: 1.12x faster                                                           |
| html5lib       | 47.5 ms                                                         | 37.5 ms: 1.27x faster                                                            |
| sphinx         | 719 ms                                                          | 624 ms: 1.15x faster                                                             |
| Geometric mean | (ref)                                                           | 1.17x faster                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250823-pythonperf1_win32-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09 |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| asyncio_websockets         | 363 ms                                                          | 159 ms: 2.29x faster                                                             |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 327 ms: 1.48x faster                                                             |
| async_tree_memoization     | 297 ms                                                          | 201 ms: 1.48x faster                                                             |
| async_tree_none            | 245 ms                                                          | 173 ms: 1.42x faster                                                             |
| async_tree_memoization_tg  | 282 ms                                                          | 205 ms: 1.38x faster                                                             |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 332 ms: 1.37x faster                                                             |
| async_tree_io              | 526 ms                                                          | 389 ms: 1.35x faster                                                             |
| async_tree_io_tg           | 494 ms                                                          | 384 ms: 1.29x faster                                                             |
| async_tree_none_tg         | 214 ms                                                          | 168 ms: 1.28x faster                                                             |
| async_generators           | 270 ms                                                          | 225 ms: 1.20x faster                                                             |
| coroutines                 | 16.2 ms                                                         | 14.0 ms: 1.16x faster                                                            |
| Geometric mean             | (ref)                                                           | 1.40x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250823-pythonperf1_win32-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pidigits       | 201 ms                                                          | 143 ms: 1.40x faster                                                             |
| float          | 54.6 ms                                                         | 43.5 ms: 1.25x faster                                                            |
| nbody          | 80.0 ms                                                         | 64.0 ms: 1.25x faster                                                            |
| Geometric mean | (ref)                                                           | 1.30x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250823-pythonperf1_win32-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 101 ms                                                          | 78.7 ms: 1.28x faster                                                            |
| regex_v8       | 16.8 ms                                                         | 13.8 ms: 1.22x faster                                                            |
| regex_effbot   | 1.80 ms                                                         | 1.57 ms: 1.14x faster                                                            |
| regex_dna      | 114 ms                                                          | 120 ms: 1.06x slower                                                             |
| Geometric mean | (ref)                                                           | 1.14x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250823-pythonperf1_win32-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09 |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| json_loads           | 21.6 us                                                         | 14.3 us: 1.51x faster                                                            |
| json_dumps           | 7.30 ms                                                         | 5.34 ms: 1.37x faster                                                            |
| xml_etree_parse      | 107 ms                                                          | 85.6 ms: 1.25x faster                                                            |
| tomli_loads          | 1.71 sec                                                        | 1.39 sec: 1.23x faster                                                           |
| unpickle_pure_python | 160 us                                                          | 134 us: 1.20x faster                                                             |
| xml_etree_process    | 44.2 ms                                                         | 38.7 ms: 1.14x faster                                                            |
| pickle_pure_python   | 231 us                                                          | 211 us: 1.10x faster                                                             |
| xml_etree_generate   | 61.4 ms                                                         | 56.4 ms: 1.09x faster                                                            |
| Geometric mean       | (ref)                                                           | 1.20x faster                                                                     |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250823-pythonperf1_win32-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09 |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup         | 28.3 ms                                                         | 25.1 ms: 1.13x faster                                                            |
| python_startup_no_site | 19.7 ms                                                         | 19.3 ms: 1.02x faster                                                            |
| Geometric mean         | (ref)                                                           | 1.07x faster                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250823-pythonperf1_win32-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09 |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| genshi_xml      | 50.1 ms                                                         | 34.0 ms: 1.47x faster                                                            |
| genshi_text     | 21.5 ms                                                         | 15.2 ms: 1.41x faster                                                            |
| django_template | 29.8 ms                                                         | 24.4 ms: 1.22x faster                                                            |
| mako            | 7.09 ms                                                         | 6.56 ms: 1.08x faster                                                            |
| Geometric mean  | (ref)                                                           | 1.29x faster                                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250823-pythonperf1_win32-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09 |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| thrift                     | 9.98 ms                                                         | 488 us: 20.45x faster                                                            |
| coverage                   | 324 ms                                                          | 48.9 ms: 6.62x faster                                                            |
| pathlib                    | 82.9 ms                                                         | 29.9 ms: 2.77x faster                                                            |
| asyncio_websockets         | 363 ms                                                          | 159 ms: 2.29x faster                                                             |
| mdp                        | 1.62 sec                                                        | 794 ms: 2.05x faster                                                             |
| deepcopy                   | 314 us                                                          | 169 us: 1.86x faster                                                             |
| telco                      | 6.96 ms                                                         | 4.13 ms: 1.68x faster                                                            |
| deepcopy_reduce            | 2.92 us                                                         | 1.84 us: 1.59x faster                                                            |
| json_loads                 | 21.6 us                                                         | 14.3 us: 1.51x faster                                                            |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 327 ms: 1.48x faster                                                             |
| async_tree_memoization     | 297 ms                                                          | 201 ms: 1.48x faster                                                             |
| genshi_xml                 | 50.1 ms                                                         | 34.0 ms: 1.47x faster                                                            |
| go                         | 109 ms                                                          | 76.1 ms: 1.43x faster                                                            |
| json                       | 4.27 ms                                                         | 3.00 ms: 1.42x faster                                                            |
| async_tree_none            | 245 ms                                                          | 173 ms: 1.42x faster                                                             |
| genshi_text                | 21.5 ms                                                         | 15.2 ms: 1.41x faster                                                            |
| pidigits                   | 201 ms                                                          | 143 ms: 1.40x faster                                                             |
| async_tree_memoization_tg  | 282 ms                                                          | 205 ms: 1.38x faster                                                             |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 332 ms: 1.37x faster                                                             |
| json_dumps                 | 7.30 ms                                                         | 5.34 ms: 1.37x faster                                                            |
| pprint_safe_repr           | 648 ms                                                          | 478 ms: 1.36x faster                                                             |
| pprint_pformat             | 1.33 sec                                                        | 981 ms: 1.35x faster                                                             |
| async_tree_io              | 526 ms                                                          | 389 ms: 1.35x faster                                                             |
| logging_format             | 8.72 us                                                         | 6.48 us: 1.35x faster                                                            |
| logging_simple             | 7.99 us                                                         | 5.97 us: 1.34x faster                                                            |
| sympy_expand               | 373 ms                                                          | 281 ms: 1.33x faster                                                             |
| typing_runtime_protocols   | 138 us                                                          | 104 us: 1.32x faster                                                             |
| deepcopy_memo              | 25.4 us                                                         | 19.3 us: 1.32x faster                                                            |
| async_tree_io_tg           | 494 ms                                                          | 384 ms: 1.29x faster                                                             |
| sympy_str                  | 212 ms                                                          | 165 ms: 1.28x faster                                                             |
| regex_compile              | 101 ms                                                          | 78.7 ms: 1.28x faster                                                            |
| chaos                      | 50.2 ms                                                         | 39.3 ms: 1.28x faster                                                            |
| async_tree_none_tg         | 214 ms                                                          | 168 ms: 1.28x faster                                                             |
| html5lib                   | 47.5 ms                                                         | 37.5 ms: 1.27x faster                                                            |
| sqlite_synth               | 1.95 us                                                         | 1.55 us: 1.26x faster                                                            |
| float                      | 54.6 ms                                                         | 43.5 ms: 1.25x faster                                                            |
| xml_etree_parse            | 107 ms                                                          | 85.6 ms: 1.25x faster                                                            |
| dulwich_log                | 48.8 ms                                                         | 39.0 ms: 1.25x faster                                                            |
| nbody                      | 80.0 ms                                                         | 64.0 ms: 1.25x faster                                                            |
| pycparser                  | 872 ms                                                          | 701 ms: 1.24x faster                                                             |
| sympy_sum                  | 106 ms                                                          | 85.3 ms: 1.24x faster                                                            |
| tomli_loads                | 1.71 sec                                                        | 1.39 sec: 1.23x faster                                                           |
| richards                   | 32.7 ms                                                         | 26.6 ms: 1.23x faster                                                            |
| scimark_monte_carlo        | 47.7 ms                                                         | 39.0 ms: 1.22x faster                                                            |
| django_template            | 29.8 ms                                                         | 24.4 ms: 1.22x faster                                                            |
| crypto_pyaes               | 56.9 ms                                                         | 46.7 ms: 1.22x faster                                                            |
| regex_v8                   | 16.8 ms                                                         | 13.8 ms: 1.22x faster                                                            |
| sympy_integrate            | 15.0 ms                                                         | 12.3 ms: 1.22x faster                                                            |
| richards_super             | 36.7 ms                                                         | 30.3 ms: 1.21x faster                                                            |
| unpickle_pure_python       | 160 us                                                          | 134 us: 1.20x faster                                                             |
| async_generators           | 270 ms                                                          | 225 ms: 1.20x faster                                                             |
| bench_thread_pool          | 1.00 ms                                                         | 839 us: 1.19x faster                                                             |
| nqueens                    | 72.1 ms                                                         | 60.8 ms: 1.19x faster                                                            |
| bpe_tokeniser              | 3.46 sec                                                        | 2.94 sec: 1.18x faster                                                           |
| pylint                     | 227 ms                                                          | 194 ms: 1.17x faster                                                             |
| raytrace                   | 201 ms                                                          | 174 ms: 1.16x faster                                                             |
| coroutines                 | 16.2 ms                                                         | 14.0 ms: 1.16x faster                                                            |
| generators                 | 21.8 ms                                                         | 18.8 ms: 1.16x faster                                                            |
| comprehensions             | 12.5 us                                                         | 10.8 us: 1.16x faster                                                            |
| sphinx                     | 719 ms                                                          | 624 ms: 1.15x faster                                                             |
| 2to3                       | 250 ms                                                          | 217 ms: 1.15x faster                                                             |
| fannkuch                   | 299 ms                                                          | 260 ms: 1.15x faster                                                             |
| regex_effbot               | 1.80 ms                                                         | 1.57 ms: 1.14x faster                                                            |
| xml_etree_process          | 44.2 ms                                                         | 38.7 ms: 1.14x faster                                                            |
| scimark_fft                | 205 ms                                                          | 180 ms: 1.14x faster                                                             |
| scimark_sparse_mat_mult    | 2.84 ms                                                         | 2.51 ms: 1.13x faster                                                            |
| python_startup             | 28.3 ms                                                         | 25.1 ms: 1.13x faster                                                            |
| scimark_sor                | 85.9 ms                                                         | 76.3 ms: 1.13x faster                                                            |
| docutils                   | 1.78 sec                                                        | 1.59 sec: 1.12x faster                                                           |
| pyflate                    | 320 ms                                                          | 288 ms: 1.11x faster                                                             |
| logging_silent             | 60.3 ns                                                         | 54.6 ns: 1.10x faster                                                            |
| spectral_norm              | 69.4 ms                                                         | 63.1 ms: 1.10x faster                                                            |
| hexiom                     | 4.44 ms                                                         | 4.04 ms: 1.10x faster                                                            |
| pickle_pure_python         | 231 us                                                          | 211 us: 1.10x faster                                                             |
| xml_etree_generate         | 61.4 ms                                                         | 56.4 ms: 1.09x faster                                                            |
| mako                       | 7.09 ms                                                         | 6.56 ms: 1.08x faster                                                            |
| scimark_lu                 | 60.2 ms                                                         | 56.4 ms: 1.07x faster                                                            |
| deltablue                  | 2.33 ms                                                         | 2.23 ms: 1.04x faster                                                            |
| meteor_contest             | 74.6 ms                                                         | 71.5 ms: 1.04x faster                                                            |
| python_startup_no_site     | 19.7 ms                                                         | 19.3 ms: 1.02x faster                                                            |
| bench_mp_pool              | 90.6 ms                                                         | 91.9 ms: 1.02x slower                                                            |
| regex_dna                  | 114 ms                                                          | 120 ms: 1.06x slower                                                             |
| gc_traversal               | 1.75 ms                                                         | 2.05 ms: 1.17x slower                                                            |
| create_gc_cycles           | 1.06 ms                                                         | 1.26 ms: 1.19x slower                                                            |
| k_core                     | 1.38 sec                                                        | 1.66 sec: 1.21x slower                                                           |
| connected_components       | 267 ms                                                          | 326 ms: 1.22x slower                                                             |
| shortest_path              | 290 ms                                                          | 357 ms: 1.23x slower                                                             |
| many_optionals             | 436 us                                                          | 551 us: 1.26x slower                                                             |
| subparsers                 | 14.8 ms                                                         | 30.2 ms: 2.04x slower                                                            |
| Geometric mean             | (ref)                                                           | 1.28x faster                                                                     |

Benchmark hidden because not significant (1): xml_etree_iterparse
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250823-3.15.0a0-6fcac09/bm-20250823-pythonperf1_win32-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.282x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.19x
- 95% likely to have a speedup of 1.18x
- 99% likely to have a speedup of 1.17x

# Memory
- memory change: unknown