# Results vs. 3.13.0

- fork: python
- ref: cebae977a63f32c3c03d
- machine: windows-amd64
- commit hash: cebae97
- commit date: 2025-06-01
- overall geometric mean: 1.186x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.14x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250601-pythonperf1_win32-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 250 ms                                                          | 294 ms: 1.18x slower                                                             |
| docutils       | 1.78 sec                                                        | 2.07 sec: 1.16x slower                                                           |
| html5lib       | 47.5 ms                                                         | 50.8 ms: 1.07x slower                                                            |
| sphinx         | 719 ms                                                          | 839 ms: 1.17x slower                                                             |
| Geometric mean | (ref)                                                           | 1.14x slower                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250601-pythonperf1_win32-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| asyncio_websockets         | 363 ms                                                          | 162 ms: 2.24x faster                                                             |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 447 ms: 1.08x faster                                                             |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 441 ms: 1.03x faster                                                             |
| async_tree_memoization_tg  | 282 ms                                                          | 292 ms: 1.03x slower                                                             |
| async_tree_io              | 526 ms                                                          | 550 ms: 1.05x slower                                                             |
| async_tree_none_tg         | 214 ms                                                          | 239 ms: 1.12x slower                                                             |
| async_tree_io_tg           | 494 ms                                                          | 560 ms: 1.13x slower                                                             |
| async_generators           | 270 ms                                                          | 343 ms: 1.27x slower                                                             |
| coroutines                 | 16.2 ms                                                         | 25.6 ms: 1.58x slower                                                            |
| Geometric mean             | (ref)                                                           | 1.01x slower                                                                     |

Benchmark hidden because not significant (2): async_tree_none, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250601-pythonperf1_win32-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pidigits       | 201 ms                                                          | 145 ms: 1.38x faster                                                             |
| nbody          | 80.0 ms                                                         | 106 ms: 1.32x slower                                                             |
| float          | 54.6 ms                                                         | 77.3 ms: 1.42x slower                                                            |
| Geometric mean | (ref)                                                           | 1.11x slower                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250601-pythonperf1_win32-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_effbot   | 1.80 ms                                                         | 1.79 ms: 1.01x faster                                                            |
| regex_dna      | 114 ms                                                          | 117 ms: 1.03x slower                                                             |
| regex_compile  | 101 ms                                                          | 123 ms: 1.22x slower                                                             |
| Geometric mean | (ref)                                                           | 1.05x slower                                                                     |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250601-pythonperf1_win32-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| json_loads           | 21.6 us                                                         | 20.5 us: 1.06x faster                                                            |
| tomli_loads          | 1.71 sec                                                        | 2.09 sec: 1.22x slower                                                           |
| json_dumps           | 7.30 ms                                                         | 9.00 ms: 1.23x slower                                                            |
| xml_etree_iterparse  | 62.6 ms                                                         | 89.3 ms: 1.43x slower                                                            |
| xml_etree_generate   | 61.4 ms                                                         | 89.7 ms: 1.46x slower                                                            |
| xml_etree_process    | 44.2 ms                                                         | 64.9 ms: 1.47x slower                                                            |
| pickle_pure_python   | 231 us                                                          | 358 us: 1.55x slower                                                             |
| unpickle_pure_python | 160 us                                                          | 275 us: 1.71x slower                                                             |
| Geometric mean       | (ref)                                                           | 1.31x slower                                                                     |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250601-pythonperf1_win32-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup         | 28.3 ms                                                         | 27.4 ms: 1.03x faster                                                            |
| python_startup_no_site | 19.7 ms                                                         | 20.1 ms: 1.02x slower                                                            |
| Geometric mean         | (ref)                                                           | 1.01x faster                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250601-pythonperf1_win32-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| genshi_text     | 21.5 ms                                                         | 23.9 ms: 1.11x slower                                                            |
| django_template | 29.8 ms                                                         | 37.2 ms: 1.25x slower                                                            |
| mako            | 7.09 ms                                                         | 12.6 ms: 1.77x slower                                                            |
| Geometric mean  | (ref)                                                           | 1.25x slower                                                                     |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250601-pythonperf1_win32-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pathlib                    | 82.9 ms                                                         | 34.1 ms: 2.43x faster                                                            |
| asyncio_websockets         | 363 ms                                                          | 162 ms: 2.24x faster                                                             |
| pidigits                   | 201 ms                                                          | 145 ms: 1.38x faster                                                             |
| mdp                        | 1.62 sec                                                        | 1.18 sec: 1.37x faster                                                           |
| deepcopy                   | 314 us                                                          | 265 us: 1.18x faster                                                             |
| telco                      | 6.96 ms                                                         | 6.26 ms: 1.11x faster                                                            |
| json                       | 4.27 ms                                                         | 3.94 ms: 1.08x faster                                                            |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 447 ms: 1.08x faster                                                             |
| deepcopy_reduce            | 2.92 us                                                         | 2.74 us: 1.06x faster                                                            |
| json_loads                 | 21.6 us                                                         | 20.5 us: 1.06x faster                                                            |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 441 ms: 1.03x faster                                                             |
| python_startup             | 28.3 ms                                                         | 27.4 ms: 1.03x faster                                                            |
| regex_effbot               | 1.80 ms                                                         | 1.79 ms: 1.01x faster                                                            |
| python_startup_no_site     | 19.7 ms                                                         | 20.1 ms: 1.02x slower                                                            |
| regex_dna                  | 114 ms                                                          | 117 ms: 1.03x slower                                                             |
| async_tree_memoization_tg  | 282 ms                                                          | 292 ms: 1.03x slower                                                             |
| async_tree_io              | 526 ms                                                          | 550 ms: 1.05x slower                                                             |
| dulwich_log                | 48.8 ms                                                         | 51.4 ms: 1.05x slower                                                            |
| html5lib                   | 47.5 ms                                                         | 50.8 ms: 1.07x slower                                                            |
| sympy_expand               | 373 ms                                                          | 400 ms: 1.07x slower                                                             |
| pylint                     | 227 ms                                                          | 246 ms: 1.08x slower                                                             |
| sympy_sum                  | 106 ms                                                          | 116 ms: 1.10x slower                                                             |
| sympy_str                  | 212 ms                                                          | 233 ms: 1.10x slower                                                             |
| sympy_integrate            | 15.0 ms                                                         | 16.6 ms: 1.11x slower                                                            |
| genshi_text                | 21.5 ms                                                         | 23.9 ms: 1.11x slower                                                            |
| async_tree_none_tg         | 214 ms                                                          | 239 ms: 1.12x slower                                                             |
| pycparser                  | 872 ms                                                          | 977 ms: 1.12x slower                                                             |
| typing_runtime_protocols   | 138 us                                                          | 155 us: 1.12x slower                                                             |
| logging_format             | 8.72 us                                                         | 9.83 us: 1.13x slower                                                            |
| async_tree_io_tg           | 494 ms                                                          | 560 ms: 1.13x slower                                                             |
| bench_mp_pool              | 90.6 ms                                                         | 103 ms: 1.14x slower                                                             |
| docutils                   | 1.78 sec                                                        | 2.07 sec: 1.16x slower                                                           |
| sphinx                     | 719 ms                                                          | 839 ms: 1.17x slower                                                             |
| logging_simple             | 7.99 us                                                         | 9.32 us: 1.17x slower                                                            |
| 2to3                       | 250 ms                                                          | 294 ms: 1.18x slower                                                             |
| regex_compile              | 101 ms                                                          | 123 ms: 1.22x slower                                                             |
| tomli_loads                | 1.71 sec                                                        | 2.09 sec: 1.22x slower                                                           |
| go                         | 109 ms                                                          | 134 ms: 1.23x slower                                                             |
| json_dumps                 | 7.30 ms                                                         | 9.00 ms: 1.23x slower                                                            |
| django_template            | 29.8 ms                                                         | 37.2 ms: 1.25x slower                                                            |
| many_optionals             | 436 us                                                          | 546 us: 1.25x slower                                                             |
| meteor_contest             | 74.6 ms                                                         | 94.3 ms: 1.26x slower                                                            |
| bpe_tokeniser              | 3.46 sec                                                        | 4.38 sec: 1.27x slower                                                           |
| async_generators           | 270 ms                                                          | 343 ms: 1.27x slower                                                             |
| nqueens                    | 72.1 ms                                                         | 93.9 ms: 1.30x slower                                                            |
| chaos                      | 50.2 ms                                                         | 65.5 ms: 1.30x slower                                                            |
| pprint_pformat             | 1.33 sec                                                        | 1.74 sec: 1.31x slower                                                           |
| connected_components       | 267 ms                                                          | 349 ms: 1.31x slower                                                             |
| pprint_safe_repr           | 648 ms                                                          | 849 ms: 1.31x slower                                                             |
| deepcopy_memo              | 25.4 us                                                         | 33.3 us: 1.31x slower                                                            |
| shortest_path              | 290 ms                                                          | 381 ms: 1.32x slower                                                             |
| nbody                      | 80.0 ms                                                         | 106 ms: 1.32x slower                                                             |
| k_core                     | 1.38 sec                                                        | 1.84 sec: 1.34x slower                                                           |
| scimark_fft                | 205 ms                                                          | 275 ms: 1.34x slower                                                             |
| create_gc_cycles           | 1.06 ms                                                         | 1.47 ms: 1.39x slower                                                            |
| crypto_pyaes               | 56.9 ms                                                         | 79.3 ms: 1.39x slower                                                            |
| fannkuch                   | 299 ms                                                          | 420 ms: 1.41x slower                                                             |
| pyflate                    | 320 ms                                                          | 451 ms: 1.41x slower                                                             |
| float                      | 54.6 ms                                                         | 77.3 ms: 1.42x slower                                                            |
| xml_etree_iterparse        | 62.6 ms                                                         | 89.3 ms: 1.43x slower                                                            |
| xml_etree_generate         | 61.4 ms                                                         | 89.7 ms: 1.46x slower                                                            |
| scimark_sparse_mat_mult    | 2.84 ms                                                         | 4.15 ms: 1.46x slower                                                            |
| coverage                   | 324 ms                                                          | 475 ms: 1.47x slower                                                             |
| xml_etree_process          | 44.2 ms                                                         | 64.9 ms: 1.47x slower                                                            |
| raytrace                   | 201 ms                                                          | 301 ms: 1.50x slower                                                             |
| scimark_monte_carlo        | 47.7 ms                                                         | 72.7 ms: 1.53x slower                                                            |
| subparsers                 | 14.8 ms                                                         | 22.7 ms: 1.54x slower                                                            |
| scimark_sor                | 85.9 ms                                                         | 133 ms: 1.54x slower                                                             |
| pickle_pure_python         | 231 us                                                          | 358 us: 1.55x slower                                                             |
| richards                   | 32.7 ms                                                         | 50.8 ms: 1.56x slower                                                            |
| richards_super             | 36.7 ms                                                         | 57.3 ms: 1.56x slower                                                            |
| comprehensions             | 12.5 us                                                         | 19.6 us: 1.56x slower                                                            |
| coroutines                 | 16.2 ms                                                         | 25.6 ms: 1.58x slower                                                            |
| generators                 | 21.8 ms                                                         | 34.5 ms: 1.58x slower                                                            |
| gc_traversal               | 1.75 ms                                                         | 2.88 ms: 1.65x slower                                                            |
| hexiom                     | 4.44 ms                                                         | 7.37 ms: 1.66x slower                                                            |
| spectral_norm              | 69.4 ms                                                         | 117 ms: 1.69x slower                                                             |
| unpickle_pure_python       | 160 us                                                          | 275 us: 1.71x slower                                                             |
| mako                       | 7.09 ms                                                         | 12.6 ms: 1.77x slower                                                            |
| deltablue                  | 2.33 ms                                                         | 4.32 ms: 1.85x slower                                                            |
| scimark_lu                 | 60.2 ms                                                         | 118 ms: 1.95x slower                                                             |
| logging_silent             | 60.3 ns                                                         | 487 ns: 8.07x slower                                                             |
| thrift                     | 9.98 ms                                                         | 98.7 ms: 9.89x slower                                                            |
| Geometric mean             | (ref)                                                           | 1.25x slower                                                                     |

Benchmark hidden because not significant (7): genshi_xml, regex_v8, sqlite_synth, async_tree_none, xml_etree_parse, bench_thread_pool, async_tree_memoization
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250601-3.15.0a0-cebae97/bm-20250601-pythonperf1_win32-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.186x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.16x
- 95% likely to have a slowdown of 1.15x
- 99% likely to have a slowdown of 1.14x

# Memory
- memory change: unknown