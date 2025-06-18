# Results vs. 3.13.0

- fork: python
- ref: fba5dded6df3c2b19435
- machine: windows-amd64
- commit hash: fba5dde
- commit date: 2025-06-17
- overall geometric mean: 1.112x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.11x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250617-pythonperf1_win32-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 250 ms                                                          | 291 ms: 1.16x slower                                                             |
| docutils       | 1.78 sec                                                        | 2.08 sec: 1.17x slower                                                           |
| html5lib       | 47.5 ms                                                         | 51.9 ms: 1.09x slower                                                            |
| sphinx         | 719 ms                                                          | 844 ms: 1.17x slower                                                             |
| Geometric mean | (ref)                                                           | 1.15x slower                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250617-pythonperf1_win32-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| asyncio_websockets         | 363 ms                                                          | 161 ms: 2.26x faster                                                             |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 442 ms: 1.10x faster                                                             |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 439 ms: 1.04x faster                                                             |
| async_tree_none            | 245 ms                                                          | 243 ms: 1.01x faster                                                             |
| async_tree_memoization_tg  | 282 ms                                                          | 291 ms: 1.03x slower                                                             |
| async_tree_io              | 526 ms                                                          | 548 ms: 1.04x slower                                                             |
| async_tree_none_tg         | 214 ms                                                          | 233 ms: 1.09x slower                                                             |
| async_tree_io_tg           | 494 ms                                                          | 564 ms: 1.14x slower                                                             |
| async_generators           | 270 ms                                                          | 332 ms: 1.23x slower                                                             |
| coroutines                 | 16.2 ms                                                         | 24.7 ms: 1.52x slower                                                            |
| Geometric mean             | (ref)                                                           | 1.00x faster                                                                     |

Benchmark hidden because not significant (1): async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250617-pythonperf1_win32-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pidigits       | 201 ms                                                          | 147 ms: 1.37x faster                                                             |
| nbody          | 80.0 ms                                                         | 99.3 ms: 1.24x slower                                                            |
| float          | 54.6 ms                                                         | 75.5 ms: 1.38x slower                                                            |
| Geometric mean | (ref)                                                           | 1.08x slower                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250617-pythonperf1_win32-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_effbot   | 1.80 ms                                                         | 1.72 ms: 1.04x faster                                                            |
| regex_dna      | 114 ms                                                          | 117 ms: 1.03x slower                                                             |
| regex_compile  | 101 ms                                                          | 122 ms: 1.20x slower                                                             |
| Geometric mean | (ref)                                                           | 1.05x slower                                                                     |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250617-pythonperf1_win32-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| json_loads           | 21.6 us                                                         | 20.8 us: 1.04x faster                                                            |
| xml_etree_parse      | 107 ms                                                          | 109 ms: 1.01x slower                                                             |
| json_dumps           | 7.30 ms                                                         | 8.53 ms: 1.17x slower                                                            |
| tomli_loads          | 1.71 sec                                                        | 2.02 sec: 1.18x slower                                                           |
| xml_etree_process    | 44.2 ms                                                         | 64.0 ms: 1.45x slower                                                            |
| xml_etree_generate   | 61.4 ms                                                         | 89.1 ms: 1.45x slower                                                            |
| xml_etree_iterparse  | 62.6 ms                                                         | 92.2 ms: 1.47x slower                                                            |
| pickle_pure_python   | 231 us                                                          | 358 us: 1.55x slower                                                             |
| unpickle_pure_python | 160 us                                                          | 275 us: 1.72x slower                                                             |
| Geometric mean       | (ref)                                                           | 1.31x slower                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250617-pythonperf1_win32-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup         | 28.3 ms                                                         | 27.4 ms: 1.03x faster                                                            |
| python_startup_no_site | 19.7 ms                                                         | 20.2 ms: 1.03x slower                                                            |
| Geometric mean         | (ref)                                                           | 1.00x faster                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250617-pythonperf1_win32-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| genshi_xml      | 50.1 ms                                                         | 48.3 ms: 1.04x faster                                                            |
| genshi_text     | 21.5 ms                                                         | 23.3 ms: 1.09x slower                                                            |
| django_template | 29.8 ms                                                         | 36.3 ms: 1.22x slower                                                            |
| mako            | 7.09 ms                                                         | 12.4 ms: 1.74x slower                                                            |
| Geometric mean  | (ref)                                                           | 1.22x slower                                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250617-pythonperf1_win32-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| thrift                     | 9.98 ms                                                         | 688 us: 14.50x faster                                                            |
| coverage                   | 324 ms                                                          | 62.2 ms: 5.20x faster                                                            |
| pathlib                    | 82.9 ms                                                         | 34.2 ms: 2.43x faster                                                            |
| asyncio_websockets         | 363 ms                                                          | 161 ms: 2.26x faster                                                             |
| mdp                        | 1.62 sec                                                        | 1.15 sec: 1.42x faster                                                           |
| pidigits                   | 201 ms                                                          | 147 ms: 1.37x faster                                                             |
| deepcopy                   | 314 us                                                          | 262 us: 1.20x faster                                                             |
| telco                      | 6.96 ms                                                         | 6.25 ms: 1.11x faster                                                            |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 442 ms: 1.10x faster                                                             |
| deepcopy_reduce            | 2.92 us                                                         | 2.69 us: 1.08x faster                                                            |
| json                       | 4.27 ms                                                         | 4.05 ms: 1.06x faster                                                            |
| sqlite_synth               | 1.95 us                                                         | 1.86 us: 1.05x faster                                                            |
| regex_effbot               | 1.80 ms                                                         | 1.72 ms: 1.04x faster                                                            |
| json_loads                 | 21.6 us                                                         | 20.8 us: 1.04x faster                                                            |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 439 ms: 1.04x faster                                                             |
| genshi_xml                 | 50.1 ms                                                         | 48.3 ms: 1.04x faster                                                            |
| python_startup             | 28.3 ms                                                         | 27.4 ms: 1.03x faster                                                            |
| async_tree_none            | 245 ms                                                          | 243 ms: 1.01x faster                                                             |
| xml_etree_parse            | 107 ms                                                          | 109 ms: 1.01x slower                                                             |
| regex_dna                  | 114 ms                                                          | 117 ms: 1.03x slower                                                             |
| python_startup_no_site     | 19.7 ms                                                         | 20.2 ms: 1.03x slower                                                            |
| async_tree_memoization_tg  | 282 ms                                                          | 291 ms: 1.03x slower                                                             |
| async_tree_io              | 526 ms                                                          | 548 ms: 1.04x slower                                                             |
| dulwich_log                | 48.8 ms                                                         | 50.9 ms: 1.04x slower                                                            |
| sympy_expand               | 373 ms                                                          | 395 ms: 1.06x slower                                                             |
| pylint                     | 227 ms                                                          | 246 ms: 1.09x slower                                                             |
| genshi_text                | 21.5 ms                                                         | 23.3 ms: 1.09x slower                                                            |
| sympy_sum                  | 106 ms                                                          | 115 ms: 1.09x slower                                                             |
| async_tree_none_tg         | 214 ms                                                          | 233 ms: 1.09x slower                                                             |
| sympy_str                  | 212 ms                                                          | 232 ms: 1.09x slower                                                             |
| html5lib                   | 47.5 ms                                                         | 51.9 ms: 1.09x slower                                                            |
| sympy_integrate            | 15.0 ms                                                         | 16.4 ms: 1.10x slower                                                            |
| logging_format             | 8.72 us                                                         | 9.72 us: 1.12x slower                                                            |
| typing_runtime_protocols   | 138 us                                                          | 154 us: 1.12x slower                                                             |
| pycparser                  | 872 ms                                                          | 975 ms: 1.12x slower                                                             |
| async_tree_io_tg           | 494 ms                                                          | 564 ms: 1.14x slower                                                             |
| logging_simple             | 7.99 us                                                         | 9.21 us: 1.15x slower                                                            |
| bench_mp_pool              | 90.6 ms                                                         | 105 ms: 1.15x slower                                                             |
| 2to3                       | 250 ms                                                          | 291 ms: 1.16x slower                                                             |
| json_dumps                 | 7.30 ms                                                         | 8.53 ms: 1.17x slower                                                            |
| docutils                   | 1.78 sec                                                        | 2.08 sec: 1.17x slower                                                           |
| sphinx                     | 719 ms                                                          | 844 ms: 1.17x slower                                                             |
| tomli_loads                | 1.71 sec                                                        | 2.02 sec: 1.18x slower                                                           |
| regex_compile              | 101 ms                                                          | 122 ms: 1.20x slower                                                             |
| go                         | 109 ms                                                          | 132 ms: 1.21x slower                                                             |
| django_template            | 29.8 ms                                                         | 36.3 ms: 1.22x slower                                                            |
| async_generators           | 270 ms                                                          | 332 ms: 1.23x slower                                                             |
| meteor_contest             | 74.6 ms                                                         | 92.2 ms: 1.24x slower                                                            |
| bpe_tokeniser              | 3.46 sec                                                        | 4.28 sec: 1.24x slower                                                           |
| nbody                      | 80.0 ms                                                         | 99.3 ms: 1.24x slower                                                            |
| many_optionals             | 436 us                                                          | 546 us: 1.25x slower                                                             |
| nqueens                    | 72.1 ms                                                         | 91.5 ms: 1.27x slower                                                            |
| chaos                      | 50.2 ms                                                         | 63.9 ms: 1.27x slower                                                            |
| scimark_fft                | 205 ms                                                          | 266 ms: 1.30x slower                                                             |
| deepcopy_memo              | 25.4 us                                                         | 33.1 us: 1.30x slower                                                            |
| connected_components       | 267 ms                                                          | 348 ms: 1.31x slower                                                             |
| shortest_path              | 290 ms                                                          | 381 ms: 1.31x slower                                                             |
| pprint_pformat             | 1.33 sec                                                        | 1.74 sec: 1.31x slower                                                           |
| k_core                     | 1.38 sec                                                        | 1.81 sec: 1.32x slower                                                           |
| pprint_safe_repr           | 648 ms                                                          | 856 ms: 1.32x slower                                                             |
| fannkuch                   | 299 ms                                                          | 406 ms: 1.36x slower                                                             |
| float                      | 54.6 ms                                                         | 75.5 ms: 1.38x slower                                                            |
| create_gc_cycles           | 1.06 ms                                                         | 1.47 ms: 1.39x slower                                                            |
| crypto_pyaes               | 56.9 ms                                                         | 79.5 ms: 1.40x slower                                                            |
| pyflate                    | 320 ms                                                          | 451 ms: 1.41x slower                                                             |
| xml_etree_process          | 44.2 ms                                                         | 64.0 ms: 1.45x slower                                                            |
| xml_etree_generate         | 61.4 ms                                                         | 89.1 ms: 1.45x slower                                                            |
| scimark_sparse_mat_mult    | 2.84 ms                                                         | 4.15 ms: 1.46x slower                                                            |
| xml_etree_iterparse        | 62.6 ms                                                         | 92.2 ms: 1.47x slower                                                            |
| raytrace                   | 201 ms                                                          | 301 ms: 1.49x slower                                                             |
| scimark_sor                | 85.9 ms                                                         | 129 ms: 1.50x slower                                                             |
| scimark_monte_carlo        | 47.7 ms                                                         | 71.7 ms: 1.50x slower                                                            |
| subparsers                 | 14.8 ms                                                         | 22.4 ms: 1.52x slower                                                            |
| coroutines                 | 16.2 ms                                                         | 24.7 ms: 1.52x slower                                                            |
| comprehensions             | 12.5 us                                                         | 19.3 us: 1.54x slower                                                            |
| richards                   | 32.7 ms                                                         | 50.6 ms: 1.55x slower                                                            |
| pickle_pure_python         | 231 us                                                          | 358 us: 1.55x slower                                                             |
| richards_super             | 36.7 ms                                                         | 57.3 ms: 1.56x slower                                                            |
| spectral_norm              | 69.4 ms                                                         | 111 ms: 1.60x slower                                                             |
| hexiom                     | 4.44 ms                                                         | 7.40 ms: 1.67x slower                                                            |
| generators                 | 21.8 ms                                                         | 36.5 ms: 1.68x slower                                                            |
| gc_traversal               | 1.75 ms                                                         | 2.99 ms: 1.71x slower                                                            |
| unpickle_pure_python       | 160 us                                                          | 275 us: 1.72x slower                                                             |
| mako                       | 7.09 ms                                                         | 12.4 ms: 1.74x slower                                                            |
| deltablue                  | 2.33 ms                                                         | 4.29 ms: 1.84x slower                                                            |
| scimark_lu                 | 60.2 ms                                                         | 119 ms: 1.98x slower                                                             |
| logging_silent             | 60.3 ns                                                         | 495 ns: 8.20x slower                                                             |
| Geometric mean             | (ref)                                                           | 1.15x slower                                                                     |

Benchmark hidden because not significant (3): bench_thread_pool, async_tree_memoization, regex_v8
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250617-3.15.0a0-fba5dde/bm-20250617-pythonperf1_win32-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.112x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.14x
- 95% likely to have a slowdown of 1.13x
- 99% likely to have a slowdown of 1.11x

# Memory
- memory change: unknown