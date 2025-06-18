# Results vs. 3.13.0

- fork: python
- ref: fba5dded6df3c2b19435
- machine: windows-amd64
- commit hash: fba5dde
- commit date: 2025-06-17
- overall geometric mean: 1.304x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.35x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250617-pythonperf1_win32-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 250 ms                                                          | 338 ms: 1.35x slower                                                             |
| docutils       | 1.78 sec                                                        | 4.22 sec: 2.37x slower                                                           |
| html5lib       | 47.5 ms                                                         | 63.4 ms: 1.34x slower                                                            |
| sphinx         | 719 ms                                                          | 1.31 sec: 1.82x slower                                                           |
| Geometric mean | (ref)                                                           | 1.67x slower                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250617-pythonperf1_win32-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| asyncio_websockets         | 363 ms                                                          | 142 ms: 2.55x faster                                                             |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 460 ms: 1.01x slower                                                             |
| async_tree_io              | 526 ms                                                          | 580 ms: 1.10x slower                                                             |
| async_tree_memoization_tg  | 282 ms                                                          | 313 ms: 1.11x slower                                                             |
| async_tree_none            | 245 ms                                                          | 275 ms: 1.12x slower                                                             |
| async_tree_io_tg           | 494 ms                                                          | 555 ms: 1.12x slower                                                             |
| async_tree_memoization     | 297 ms                                                          | 336 ms: 1.13x slower                                                             |
| async_tree_none_tg         | 214 ms                                                          | 248 ms: 1.16x slower                                                             |
| async_generators           | 270 ms                                                          | 418 ms: 1.55x slower                                                             |
| coroutines                 | 16.2 ms                                                         | 34.0 ms: 2.09x slower                                                            |
| Geometric mean             | (ref)                                                           | 1.09x slower                                                                     |

Benchmark hidden because not significant (1): async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250617-pythonperf1_win32-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pidigits       | 201 ms                                                          | 140 ms: 1.43x faster                                                             |
| float          | 54.6 ms                                                         | 97.7 ms: 1.79x slower                                                            |
| nbody          | 80.0 ms                                                         | 184 ms: 2.30x slower                                                             |
| Geometric mean | (ref)                                                           | 1.42x slower                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250617-pythonperf1_win32-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_effbot   | 1.80 ms                                                         | 1.83 ms: 1.01x slower                                                            |
| regex_compile  | 101 ms                                                          | 161 ms: 1.59x slower                                                             |
| Geometric mean | (ref)                                                           | 1.13x slower                                                                     |

Benchmark hidden because not significant (2): regex_dna, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250617-pythonperf1_win32-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| xml_etree_parse      | 107 ms                                                          | 112 ms: 1.05x slower                                                             |
| json_loads           | 21.6 us                                                         | 23.1 us: 1.07x slower                                                            |
| json_dumps           | 7.30 ms                                                         | 9.52 ms: 1.30x slower                                                            |
| xml_etree_iterparse  | 62.6 ms                                                         | 92.3 ms: 1.48x slower                                                            |
| xml_etree_generate   | 61.4 ms                                                         | 107 ms: 1.75x slower                                                             |
| xml_etree_process    | 44.2 ms                                                         | 79.9 ms: 1.81x slower                                                            |
| pickle_pure_python   | 231 us                                                          | 451 us: 1.95x slower                                                             |
| unpickle_pure_python | 160 us                                                          | 356 us: 2.22x slower                                                             |
| tomli_loads          | 1.71 sec                                                        | 5.05 sec: 2.94x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.64x slower                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250617-pythonperf1_win32-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup         | 28.3 ms                                                         | 27.7 ms: 1.02x faster                                                            |
| python_startup_no_site | 19.7 ms                                                         | 20.4 ms: 1.04x slower                                                            |
| Geometric mean         | (ref)                                                           | 1.01x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250617-pythonperf1_win32-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| genshi_xml      | 50.1 ms                                                         | 66.2 ms: 1.32x slower                                                            |
| django_template | 29.8 ms                                                         | 45.9 ms: 1.54x slower                                                            |
| genshi_text     | 21.5 ms                                                         | 34.3 ms: 1.60x slower                                                            |
| mako            | 7.09 ms                                                         | 16.4 ms: 2.32x slower                                                            |
| Geometric mean  | (ref)                                                           | 1.66x slower                                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250617-pythonperf1_win32-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| thrift                     | 9.98 ms                                                         | 852 us: 11.71x faster                                                            |
| coverage                   | 324 ms                                                          | 84.1 ms: 3.85x faster                                                            |
| asyncio_websockets         | 363 ms                                                          | 142 ms: 2.55x faster                                                             |
| pathlib                    | 82.9 ms                                                         | 35.5 ms: 2.33x faster                                                            |
| pidigits                   | 201 ms                                                          | 140 ms: 1.43x faster                                                             |
| sqlite_synth               | 1.95 us                                                         | 1.71 us: 1.14x faster                                                            |
| python_startup             | 28.3 ms                                                         | 27.7 ms: 1.02x faster                                                            |
| gc_traversal               | 1.75 ms                                                         | 1.72 ms: 1.02x faster                                                            |
| bench_mp_pool              | 90.6 ms                                                         | 89.4 ms: 1.01x faster                                                            |
| json                       | 4.27 ms                                                         | 4.23 ms: 1.01x faster                                                            |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 460 ms: 1.01x slower                                                             |
| regex_effbot               | 1.80 ms                                                         | 1.83 ms: 1.01x slower                                                            |
| create_gc_cycles           | 1.06 ms                                                         | 1.10 ms: 1.04x slower                                                            |
| python_startup_no_site     | 19.7 ms                                                         | 20.4 ms: 1.04x slower                                                            |
| xml_etree_parse            | 107 ms                                                          | 112 ms: 1.05x slower                                                             |
| json_loads                 | 21.6 us                                                         | 23.1 us: 1.07x slower                                                            |
| deepcopy                   | 314 us                                                          | 336 us: 1.07x slower                                                             |
| async_tree_io              | 526 ms                                                          | 580 ms: 1.10x slower                                                             |
| async_tree_memoization_tg  | 282 ms                                                          | 313 ms: 1.11x slower                                                             |
| async_tree_none            | 245 ms                                                          | 275 ms: 1.12x slower                                                             |
| async_tree_io_tg           | 494 ms                                                          | 555 ms: 1.12x slower                                                             |
| async_tree_memoization     | 297 ms                                                          | 336 ms: 1.13x slower                                                             |
| dulwich_log                | 48.8 ms                                                         | 56.3 ms: 1.15x slower                                                            |
| async_tree_none_tg         | 214 ms                                                          | 248 ms: 1.16x slower                                                             |
| telco                      | 6.96 ms                                                         | 8.06 ms: 1.16x slower                                                            |
| deepcopy_reduce            | 2.92 us                                                         | 3.48 us: 1.19x slower                                                            |
| bench_thread_pool          | 1.00 ms                                                         | 1.23 ms: 1.23x slower                                                            |
| pylint                     | 227 ms                                                          | 282 ms: 1.24x slower                                                             |
| json_dumps                 | 7.30 ms                                                         | 9.52 ms: 1.30x slower                                                            |
| genshi_xml                 | 50.1 ms                                                         | 66.2 ms: 1.32x slower                                                            |
| sympy_expand               | 373 ms                                                          | 496 ms: 1.33x slower                                                             |
| html5lib                   | 47.5 ms                                                         | 63.4 ms: 1.34x slower                                                            |
| logging_format             | 8.72 us                                                         | 11.7 us: 1.34x slower                                                            |
| 2to3                       | 250 ms                                                          | 338 ms: 1.35x slower                                                             |
| sympy_sum                  | 106 ms                                                          | 144 ms: 1.36x slower                                                             |
| mdp                        | 1.62 sec                                                        | 2.22 sec: 1.37x slower                                                           |
| sympy_str                  | 212 ms                                                          | 292 ms: 1.38x slower                                                             |
| sympy_integrate            | 15.0 ms                                                         | 20.8 ms: 1.39x slower                                                            |
| logging_simple             | 7.99 us                                                         | 11.1 us: 1.39x slower                                                            |
| typing_runtime_protocols   | 138 us                                                          | 198 us: 1.44x slower                                                             |
| xml_etree_iterparse        | 62.6 ms                                                         | 92.3 ms: 1.48x slower                                                            |
| many_optionals             | 436 us                                                          | 650 us: 1.49x slower                                                             |
| django_template            | 29.8 ms                                                         | 45.9 ms: 1.54x slower                                                            |
| async_generators           | 270 ms                                                          | 418 ms: 1.55x slower                                                             |
| meteor_contest             | 74.6 ms                                                         | 117 ms: 1.57x slower                                                             |
| regex_compile              | 101 ms                                                          | 161 ms: 1.59x slower                                                             |
| genshi_text                | 21.5 ms                                                         | 34.3 ms: 1.60x slower                                                            |
| deepcopy_memo              | 25.4 us                                                         | 43.7 us: 1.72x slower                                                            |
| nqueens                    | 72.1 ms                                                         | 125 ms: 1.73x slower                                                             |
| xml_etree_generate         | 61.4 ms                                                         | 107 ms: 1.75x slower                                                             |
| go                         | 109 ms                                                          | 191 ms: 1.76x slower                                                             |
| float                      | 54.6 ms                                                         | 97.7 ms: 1.79x slower                                                            |
| xml_etree_process          | 44.2 ms                                                         | 79.9 ms: 1.81x slower                                                            |
| sphinx                     | 719 ms                                                          | 1.31 sec: 1.82x slower                                                           |
| subparsers                 | 14.8 ms                                                         | 27.4 ms: 1.85x slower                                                            |
| chaos                      | 50.2 ms                                                         | 96.3 ms: 1.92x slower                                                            |
| pyflate                    | 320 ms                                                          | 614 ms: 1.92x slower                                                             |
| fannkuch                   | 299 ms                                                          | 573 ms: 1.92x slower                                                             |
| pickle_pure_python         | 231 us                                                          | 451 us: 1.95x slower                                                             |
| pycparser                  | 872 ms                                                          | 1.74 sec: 1.99x slower                                                           |
| comprehensions             | 12.5 us                                                         | 25.5 us: 2.04x slower                                                            |
| generators                 | 21.8 ms                                                         | 44.8 ms: 2.06x slower                                                            |
| crypto_pyaes               | 56.9 ms                                                         | 117 ms: 2.06x slower                                                             |
| scimark_fft                | 205 ms                                                          | 425 ms: 2.08x slower                                                             |
| raytrace                   | 201 ms                                                          | 419 ms: 2.08x slower                                                             |
| coroutines                 | 16.2 ms                                                         | 34.0 ms: 2.09x slower                                                            |
| richards                   | 32.7 ms                                                         | 70.2 ms: 2.15x slower                                                            |
| richards_super             | 36.7 ms                                                         | 79.3 ms: 2.16x slower                                                            |
| scimark_sor                | 85.9 ms                                                         | 189 ms: 2.20x slower                                                             |
| unpickle_pure_python       | 160 us                                                          | 356 us: 2.22x slower                                                             |
| k_core                     | 1.38 sec                                                        | 3.06 sec: 2.23x slower                                                           |
| scimark_monte_carlo        | 47.7 ms                                                         | 108 ms: 2.27x slower                                                             |
| pprint_safe_repr           | 648 ms                                                          | 1.48 sec: 2.28x slower                                                           |
| nbody                      | 80.0 ms                                                         | 184 ms: 2.30x slower                                                             |
| mako                       | 7.09 ms                                                         | 16.4 ms: 2.32x slower                                                            |
| scimark_sparse_mat_mult    | 2.84 ms                                                         | 6.61 ms: 2.33x slower                                                            |
| hexiom                     | 4.44 ms                                                         | 10.5 ms: 2.36x slower                                                            |
| spectral_norm              | 69.4 ms                                                         | 165 ms: 2.37x slower                                                             |
| docutils                   | 1.78 sec                                                        | 4.22 sec: 2.37x slower                                                           |
| bpe_tokeniser              | 3.46 sec                                                        | 8.38 sec: 2.42x slower                                                           |
| shortest_path              | 290 ms                                                          | 732 ms: 2.52x slower                                                             |
| deltablue                  | 2.33 ms                                                         | 5.91 ms: 2.53x slower                                                            |
| connected_components       | 267 ms                                                          | 690 ms: 2.59x slower                                                             |
| scimark_lu                 | 60.2 ms                                                         | 165 ms: 2.75x slower                                                             |
| tomli_loads                | 1.71 sec                                                        | 5.05 sec: 2.94x slower                                                           |
| pprint_pformat             | 1.33 sec                                                        | 4.25 sec: 3.20x slower                                                           |
| logging_silent             | 60.3 ns                                                         | 586 ns: 9.71x slower                                                             |
| Geometric mean             | (ref)                                                           | 1.47x slower                                                                     |

Benchmark hidden because not significant (3): regex_dna, async_tree_cpu_io_mixed, regex_v8
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250617-3.15.0a0-fba5dde-NOGIL/bm-20250617-pythonperf1_win32-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.304x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.46x
- 95% likely to have a slowdown of 1.41x
- 99% likely to have a slowdown of 1.35x

# Memory
- memory change: unknown