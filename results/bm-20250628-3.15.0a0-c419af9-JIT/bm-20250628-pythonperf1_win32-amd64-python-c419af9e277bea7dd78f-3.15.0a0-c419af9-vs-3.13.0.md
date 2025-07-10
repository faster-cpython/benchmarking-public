# Results vs. 3.13.0

- fork: python
- ref: c419af9e277bea7dd78f
- machine: windows-amd64
- commit hash: c419af9
- commit date: 2025-06-28
- overall geometric mean: 1.307x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.19x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250628-pythonperf1_win32-amd64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 250 ms                                                          | 219 ms: 1.14x faster                                                             |
| docutils       | 1.78 sec                                                        | 1.65 sec: 1.08x faster                                                           |
| html5lib       | 47.5 ms                                                         | 38.1 ms: 1.25x faster                                                            |
| sphinx         | 719 ms                                                          | 639 ms: 1.12x faster                                                             |
| Geometric mean | (ref)                                                           | 1.15x faster                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250628-pythonperf1_win32-amd64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| asyncio_websockets         | 363 ms                                                          | 161 ms: 2.26x faster                                                             |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 331 ms: 1.46x faster                                                             |
| async_tree_memoization     | 297 ms                                                          | 204 ms: 1.45x faster                                                             |
| async_tree_none            | 245 ms                                                          | 170 ms: 1.44x faster                                                             |
| async_tree_io              | 526 ms                                                          | 390 ms: 1.35x faster                                                             |
| async_tree_memoization_tg  | 282 ms                                                          | 210 ms: 1.34x faster                                                             |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 341 ms: 1.34x faster                                                             |
| async_tree_io_tg           | 494 ms                                                          | 383 ms: 1.29x faster                                                             |
| async_tree_none_tg         | 214 ms                                                          | 166 ms: 1.29x faster                                                             |
| coroutines                 | 16.2 ms                                                         | 14.2 ms: 1.14x faster                                                            |
| async_generators           | 270 ms                                                          | 250 ms: 1.08x faster                                                             |
| Geometric mean             | (ref)                                                           | 1.38x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250628-pythonperf1_win32-amd64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| nbody          | 80.0 ms                                                         | 53.3 ms: 1.50x faster                                                            |
| pidigits       | 201 ms                                                          | 146 ms: 1.37x faster                                                             |
| float          | 54.6 ms                                                         | 44.5 ms: 1.23x faster                                                            |
| Geometric mean | (ref)                                                           | 1.36x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250628-pythonperf1_win32-amd64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 101 ms                                                          | 78.9 ms: 1.28x faster                                                            |
| regex_v8       | 16.8 ms                                                         | 14.4 ms: 1.16x faster                                                            |
| regex_effbot   | 1.80 ms                                                         | 1.57 ms: 1.14x faster                                                            |
| regex_dna      | 114 ms                                                          | 120 ms: 1.05x slower                                                             |
| Geometric mean | (ref)                                                           | 1.13x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250628-pythonperf1_win32-amd64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| tomli_loads          | 1.71 sec                                                        | 1.12 sec: 1.53x faster                                                           |
| json_loads           | 21.6 us                                                         | 14.6 us: 1.49x faster                                                            |
| unpickle_pure_python | 160 us                                                          | 109 us: 1.47x faster                                                             |
| xml_etree_process    | 44.2 ms                                                         | 35.7 ms: 1.24x faster                                                            |
| xml_etree_parse      | 107 ms                                                          | 87.1 ms: 1.23x faster                                                            |
| xml_etree_generate   | 61.4 ms                                                         | 50.9 ms: 1.21x faster                                                            |
| json_dumps           | 7.30 ms                                                         | 6.15 ms: 1.19x faster                                                            |
| pickle_pure_python   | 231 us                                                          | 203 us: 1.14x faster                                                             |
| Geometric mean       | (ref)                                                           | 1.27x faster                                                                     |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250628-pythonperf1_win32-amd64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup         | 28.3 ms                                                         | 25.4 ms: 1.11x faster                                                            |
| python_startup_no_site | 19.7 ms                                                         | 19.2 ms: 1.02x faster                                                            |
| Geometric mean         | (ref)                                                           | 1.07x faster                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250628-pythonperf1_win32-amd64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| genshi_xml      | 50.1 ms                                                         | 34.2 ms: 1.47x faster                                                            |
| genshi_text     | 21.5 ms                                                         | 15.3 ms: 1.41x faster                                                            |
| mako            | 7.09 ms                                                         | 5.45 ms: 1.30x faster                                                            |
| django_template | 29.8 ms                                                         | 24.2 ms: 1.23x faster                                                            |
| Geometric mean  | (ref)                                                           | 1.35x faster                                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250628-pythonperf1_win32-amd64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| thrift                     | 9.98 ms                                                         | 495 us: 20.17x faster                                                            |
| coverage                   | 324 ms                                                          | 49.6 ms: 6.53x faster                                                            |
| pathlib                    | 82.9 ms                                                         | 28.7 ms: 2.88x faster                                                            |
| asyncio_websockets         | 363 ms                                                          | 161 ms: 2.26x faster                                                             |
| mdp                        | 1.62 sec                                                        | 810 ms: 2.01x faster                                                             |
| deepcopy                   | 314 us                                                          | 169 us: 1.86x faster                                                             |
| telco                      | 6.96 ms                                                         | 4.32 ms: 1.61x faster                                                            |
| deepcopy_reduce            | 2.92 us                                                         | 1.85 us: 1.58x faster                                                            |
| tomli_loads                | 1.71 sec                                                        | 1.12 sec: 1.53x faster                                                           |
| nbody                      | 80.0 ms                                                         | 53.3 ms: 1.50x faster                                                            |
| json_loads                 | 21.6 us                                                         | 14.6 us: 1.49x faster                                                            |
| genshi_xml                 | 50.1 ms                                                         | 34.2 ms: 1.47x faster                                                            |
| unpickle_pure_python       | 160 us                                                          | 109 us: 1.47x faster                                                             |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 331 ms: 1.46x faster                                                             |
| deepcopy_memo              | 25.4 us                                                         | 17.5 us: 1.46x faster                                                            |
| async_tree_memoization     | 297 ms                                                          | 204 ms: 1.45x faster                                                             |
| async_tree_none            | 245 ms                                                          | 170 ms: 1.44x faster                                                             |
| pprint_pformat             | 1.33 sec                                                        | 922 ms: 1.44x faster                                                             |
| pprint_safe_repr           | 648 ms                                                          | 450 ms: 1.44x faster                                                             |
| go                         | 109 ms                                                          | 75.9 ms: 1.43x faster                                                            |
| json                       | 4.27 ms                                                         | 3.02 ms: 1.41x faster                                                            |
| genshi_text                | 21.5 ms                                                         | 15.3 ms: 1.41x faster                                                            |
| pidigits                   | 201 ms                                                          | 146 ms: 1.37x faster                                                             |
| scimark_fft                | 205 ms                                                          | 150 ms: 1.36x faster                                                             |
| bpe_tokeniser              | 3.46 sec                                                        | 2.56 sec: 1.35x faster                                                           |
| async_tree_io              | 526 ms                                                          | 390 ms: 1.35x faster                                                             |
| async_tree_memoization_tg  | 282 ms                                                          | 210 ms: 1.34x faster                                                             |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 341 ms: 1.34x faster                                                             |
| fannkuch                   | 299 ms                                                          | 224 ms: 1.33x faster                                                             |
| typing_runtime_protocols   | 138 us                                                          | 104 us: 1.32x faster                                                             |
| logging_format             | 8.72 us                                                         | 6.64 us: 1.31x faster                                                            |
| mako                       | 7.09 ms                                                         | 5.45 ms: 1.30x faster                                                            |
| logging_simple             | 7.99 us                                                         | 6.18 us: 1.29x faster                                                            |
| async_tree_io_tg           | 494 ms                                                          | 383 ms: 1.29x faster                                                             |
| async_tree_none_tg         | 214 ms                                                          | 166 ms: 1.29x faster                                                             |
| regex_compile              | 101 ms                                                          | 78.9 ms: 1.28x faster                                                            |
| sympy_expand               | 373 ms                                                          | 293 ms: 1.28x faster                                                             |
| pyflate                    | 320 ms                                                          | 253 ms: 1.26x faster                                                             |
| scimark_sparse_mat_mult    | 2.84 ms                                                         | 2.26 ms: 1.26x faster                                                            |
| pycparser                  | 872 ms                                                          | 697 ms: 1.25x faster                                                             |
| sympy_str                  | 212 ms                                                          | 170 ms: 1.25x faster                                                             |
| sqlite_synth               | 1.95 us                                                         | 1.56 us: 1.25x faster                                                            |
| html5lib                   | 47.5 ms                                                         | 38.1 ms: 1.25x faster                                                            |
| crypto_pyaes               | 56.9 ms                                                         | 45.7 ms: 1.25x faster                                                            |
| xml_etree_process          | 44.2 ms                                                         | 35.7 ms: 1.24x faster                                                            |
| xml_etree_parse            | 107 ms                                                          | 87.1 ms: 1.23x faster                                                            |
| django_template            | 29.8 ms                                                         | 24.2 ms: 1.23x faster                                                            |
| chaos                      | 50.2 ms                                                         | 40.9 ms: 1.23x faster                                                            |
| float                      | 54.6 ms                                                         | 44.5 ms: 1.23x faster                                                            |
| richards                   | 32.7 ms                                                         | 26.7 ms: 1.22x faster                                                            |
| xml_etree_generate         | 61.4 ms                                                         | 50.9 ms: 1.21x faster                                                            |
| sympy_sum                  | 106 ms                                                          | 87.7 ms: 1.20x faster                                                            |
| nqueens                    | 72.1 ms                                                         | 59.9 ms: 1.20x faster                                                            |
| dulwich_log                | 48.8 ms                                                         | 40.7 ms: 1.20x faster                                                            |
| richards_super             | 36.7 ms                                                         | 30.6 ms: 1.20x faster                                                            |
| json_dumps                 | 7.30 ms                                                         | 6.15 ms: 1.19x faster                                                            |
| sympy_integrate            | 15.0 ms                                                         | 12.8 ms: 1.17x faster                                                            |
| comprehensions             | 12.5 us                                                         | 10.7 us: 1.17x faster                                                            |
| regex_v8                   | 16.8 ms                                                         | 14.4 ms: 1.16x faster                                                            |
| scimark_monte_carlo        | 47.7 ms                                                         | 41.5 ms: 1.15x faster                                                            |
| coroutines                 | 16.2 ms                                                         | 14.2 ms: 1.14x faster                                                            |
| regex_effbot               | 1.80 ms                                                         | 1.57 ms: 1.14x faster                                                            |
| pylint                     | 227 ms                                                          | 198 ms: 1.14x faster                                                             |
| pickle_pure_python         | 231 us                                                          | 203 us: 1.14x faster                                                             |
| 2to3                       | 250 ms                                                          | 219 ms: 1.14x faster                                                             |
| sphinx                     | 719 ms                                                          | 639 ms: 1.12x faster                                                             |
| scimark_sor                | 85.9 ms                                                         | 76.6 ms: 1.12x faster                                                            |
| generators                 | 21.8 ms                                                         | 19.4 ms: 1.12x faster                                                            |
| raytrace                   | 201 ms                                                          | 181 ms: 1.11x faster                                                             |
| python_startup             | 28.3 ms                                                         | 25.4 ms: 1.11x faster                                                            |
| logging_silent             | 60.3 ns                                                         | 54.3 ns: 1.11x faster                                                            |
| hexiom                     | 4.44 ms                                                         | 4.11 ms: 1.08x faster                                                            |
| docutils                   | 1.78 sec                                                        | 1.65 sec: 1.08x faster                                                           |
| async_generators           | 270 ms                                                          | 250 ms: 1.08x faster                                                             |
| spectral_norm              | 69.4 ms                                                         | 64.9 ms: 1.07x faster                                                            |
| meteor_contest             | 74.6 ms                                                         | 70.3 ms: 1.06x faster                                                            |
| deltablue                  | 2.33 ms                                                         | 2.21 ms: 1.06x faster                                                            |
| python_startup_no_site     | 19.7 ms                                                         | 19.2 ms: 1.02x faster                                                            |
| scimark_lu                 | 60.2 ms                                                         | 59.5 ms: 1.01x faster                                                            |
| many_optionals             | 436 us                                                          | 445 us: 1.02x slower                                                             |
| regex_dna                  | 114 ms                                                          | 120 ms: 1.05x slower                                                             |
| subparsers                 | 14.8 ms                                                         | 16.8 ms: 1.14x slower                                                            |
| k_core                     | 1.38 sec                                                        | 1.60 sec: 1.16x slower                                                           |
| gc_traversal               | 1.75 ms                                                         | 2.11 ms: 1.20x slower                                                            |
| connected_components       | 267 ms                                                          | 322 ms: 1.21x slower                                                             |
| shortest_path              | 290 ms                                                          | 352 ms: 1.21x slower                                                             |
| create_gc_cycles           | 1.06 ms                                                         | 1.32 ms: 1.25x slower                                                            |
| Geometric mean             | (ref)                                                           | 1.31x faster                                                                     |

Benchmark hidden because not significant (1): xml_etree_iterparse
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250628-3.15.0a0-c419af9-JIT/bm-20250628-pythonperf1_win32-amd64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.307x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.22x
- 95% likely to have a speedup of 1.21x
- 99% likely to have a speedup of 1.19x

# Memory
- memory change: unknown