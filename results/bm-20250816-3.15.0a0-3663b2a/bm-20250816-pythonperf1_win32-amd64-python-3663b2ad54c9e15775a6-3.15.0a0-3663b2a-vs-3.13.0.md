# Results vs. 3.13.0

- fork: python
- ref: 3663b2ad54c9e15775a6
- machine: windows-amd64
- commit hash: 3663b2a
- commit date: 2025-08-16
- overall geometric mean: 1.281x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.17x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250816-pythonperf1_win32-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 250 ms                                                          | 218 ms: 1.15x faster                                                             |
| docutils       | 1.78 sec                                                        | 1.59 sec: 1.12x faster                                                           |
| html5lib       | 47.5 ms                                                         | 37.3 ms: 1.27x faster                                                            |
| sphinx         | 719 ms                                                          | 615 ms: 1.17x faster                                                             |
| Geometric mean | (ref)                                                           | 1.18x faster                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250816-pythonperf1_win32-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| asyncio_websockets         | 363 ms                                                          | 156 ms: 2.33x faster                                                             |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 328 ms: 1.47x faster                                                             |
| async_tree_memoization     | 297 ms                                                          | 204 ms: 1.46x faster                                                             |
| async_tree_none            | 245 ms                                                          | 172 ms: 1.42x faster                                                             |
| async_tree_io              | 526 ms                                                          | 383 ms: 1.37x faster                                                             |
| async_tree_memoization_tg  | 282 ms                                                          | 208 ms: 1.35x faster                                                             |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 338 ms: 1.35x faster                                                             |
| async_tree_none_tg         | 214 ms                                                          | 166 ms: 1.29x faster                                                             |
| async_tree_io_tg           | 494 ms                                                          | 386 ms: 1.28x faster                                                             |
| async_generators           | 270 ms                                                          | 227 ms: 1.19x faster                                                             |
| coroutines                 | 16.2 ms                                                         | 14.6 ms: 1.11x faster                                                            |
| Geometric mean             | (ref)                                                           | 1.39x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250816-pythonperf1_win32-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pidigits       | 201 ms                                                          | 144 ms: 1.39x faster                                                             |
| float          | 54.6 ms                                                         | 42.6 ms: 1.28x faster                                                            |
| nbody          | 80.0 ms                                                         | 63.5 ms: 1.26x faster                                                            |
| Geometric mean | (ref)                                                           | 1.31x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250816-pythonperf1_win32-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 101 ms                                                          | 79.0 ms: 1.28x faster                                                            |
| regex_v8       | 16.8 ms                                                         | 13.9 ms: 1.21x faster                                                            |
| regex_effbot   | 1.80 ms                                                         | 1.52 ms: 1.19x faster                                                            |
| regex_dna      | 114 ms                                                          | 118 ms: 1.04x slower                                                             |
| Geometric mean | (ref)                                                           | 1.15x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250816-pythonperf1_win32-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| json_loads           | 21.6 us                                                         | 13.9 us: 1.56x faster                                                            |
| json_dumps           | 7.30 ms                                                         | 5.43 ms: 1.34x faster                                                            |
| xml_etree_parse      | 107 ms                                                          | 87.6 ms: 1.23x faster                                                            |
| tomli_loads          | 1.71 sec                                                        | 1.42 sec: 1.21x faster                                                           |
| unpickle_pure_python | 160 us                                                          | 133 us: 1.21x faster                                                             |
| xml_etree_process    | 44.2 ms                                                         | 38.8 ms: 1.14x faster                                                            |
| pickle_pure_python   | 231 us                                                          | 212 us: 1.09x faster                                                             |
| xml_etree_generate   | 61.4 ms                                                         | 56.6 ms: 1.09x faster                                                            |
| xml_etree_iterparse  | 62.6 ms                                                         | 64.3 ms: 1.03x slower                                                            |
| Geometric mean       | (ref)                                                           | 1.19x faster                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250816-pythonperf1_win32-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup         | 28.3 ms                                                         | 25.3 ms: 1.12x faster                                                            |
| python_startup_no_site | 19.7 ms                                                         | 19.2 ms: 1.02x faster                                                            |
| Geometric mean         | (ref)                                                           | 1.07x faster                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250816-pythonperf1_win32-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| genshi_xml      | 50.1 ms                                                         | 34.5 ms: 1.45x faster                                                            |
| genshi_text     | 21.5 ms                                                         | 15.3 ms: 1.40x faster                                                            |
| django_template | 29.8 ms                                                         | 24.5 ms: 1.22x faster                                                            |
| mako            | 7.09 ms                                                         | 6.58 ms: 1.08x faster                                                            |
| Geometric mean  | (ref)                                                           | 1.28x faster                                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250816-pythonperf1_win32-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| thrift                     | 9.98 ms                                                         | 499 us: 19.98x faster                                                            |
| coverage                   | 324 ms                                                          | 49.7 ms: 6.52x faster                                                            |
| pathlib                    | 82.9 ms                                                         | 28.5 ms: 2.91x faster                                                            |
| asyncio_websockets         | 363 ms                                                          | 156 ms: 2.33x faster                                                             |
| mdp                        | 1.62 sec                                                        | 794 ms: 2.05x faster                                                             |
| deepcopy                   | 314 us                                                          | 169 us: 1.86x faster                                                             |
| deepcopy_reduce            | 2.92 us                                                         | 1.83 us: 1.60x faster                                                            |
| telco                      | 6.96 ms                                                         | 4.40 ms: 1.58x faster                                                            |
| json_loads                 | 21.6 us                                                         | 13.9 us: 1.56x faster                                                            |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 328 ms: 1.47x faster                                                             |
| json                       | 4.27 ms                                                         | 2.93 ms: 1.46x faster                                                            |
| async_tree_memoization     | 297 ms                                                          | 204 ms: 1.46x faster                                                             |
| genshi_xml                 | 50.1 ms                                                         | 34.5 ms: 1.45x faster                                                            |
| async_tree_none            | 245 ms                                                          | 172 ms: 1.42x faster                                                             |
| go                         | 109 ms                                                          | 76.6 ms: 1.42x faster                                                            |
| genshi_text                | 21.5 ms                                                         | 15.3 ms: 1.40x faster                                                            |
| pidigits                   | 201 ms                                                          | 144 ms: 1.39x faster                                                             |
| logging_format             | 8.72 us                                                         | 6.26 us: 1.39x faster                                                            |
| deepcopy_memo              | 25.4 us                                                         | 18.3 us: 1.39x faster                                                            |
| logging_simple             | 7.99 us                                                         | 5.83 us: 1.37x faster                                                            |
| async_tree_io              | 526 ms                                                          | 383 ms: 1.37x faster                                                             |
| async_tree_memoization_tg  | 282 ms                                                          | 208 ms: 1.35x faster                                                             |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 338 ms: 1.35x faster                                                             |
| json_dumps                 | 7.30 ms                                                         | 5.43 ms: 1.34x faster                                                            |
| pprint_pformat             | 1.33 sec                                                        | 998 ms: 1.33x faster                                                             |
| pprint_safe_repr           | 648 ms                                                          | 489 ms: 1.33x faster                                                             |
| sympy_expand               | 373 ms                                                          | 282 ms: 1.32x faster                                                             |
| typing_runtime_protocols   | 138 us                                                          | 105 us: 1.31x faster                                                             |
| async_tree_none_tg         | 214 ms                                                          | 166 ms: 1.29x faster                                                             |
| float                      | 54.6 ms                                                         | 42.6 ms: 1.28x faster                                                            |
| async_tree_io_tg           | 494 ms                                                          | 386 ms: 1.28x faster                                                             |
| regex_compile              | 101 ms                                                          | 79.0 ms: 1.28x faster                                                            |
| html5lib                   | 47.5 ms                                                         | 37.3 ms: 1.27x faster                                                            |
| sympy_str                  | 212 ms                                                          | 167 ms: 1.27x faster                                                             |
| dulwich_log                | 48.8 ms                                                         | 38.5 ms: 1.27x faster                                                            |
| nbody                      | 80.0 ms                                                         | 63.5 ms: 1.26x faster                                                            |
| pycparser                  | 872 ms                                                          | 694 ms: 1.26x faster                                                             |
| chaos                      | 50.2 ms                                                         | 40.3 ms: 1.25x faster                                                            |
| sqlite_synth               | 1.95 us                                                         | 1.57 us: 1.25x faster                                                            |
| crypto_pyaes               | 56.9 ms                                                         | 46.0 ms: 1.24x faster                                                            |
| sympy_sum                  | 106 ms                                                          | 85.6 ms: 1.23x faster                                                            |
| sympy_integrate            | 15.0 ms                                                         | 12.2 ms: 1.23x faster                                                            |
| xml_etree_parse            | 107 ms                                                          | 87.6 ms: 1.23x faster                                                            |
| richards                   | 32.7 ms                                                         | 26.7 ms: 1.22x faster                                                            |
| django_template            | 29.8 ms                                                         | 24.5 ms: 1.22x faster                                                            |
| regex_v8                   | 16.8 ms                                                         | 13.9 ms: 1.21x faster                                                            |
| tomli_loads                | 1.71 sec                                                        | 1.42 sec: 1.21x faster                                                           |
| unpickle_pure_python       | 160 us                                                          | 133 us: 1.21x faster                                                             |
| richards_super             | 36.7 ms                                                         | 30.5 ms: 1.20x faster                                                            |
| scimark_monte_carlo        | 47.7 ms                                                         | 39.8 ms: 1.20x faster                                                            |
| bench_thread_pool          | 1.00 ms                                                         | 839 us: 1.19x faster                                                             |
| bpe_tokeniser              | 3.46 sec                                                        | 2.91 sec: 1.19x faster                                                           |
| nqueens                    | 72.1 ms                                                         | 60.6 ms: 1.19x faster                                                            |
| async_generators           | 270 ms                                                          | 227 ms: 1.19x faster                                                             |
| regex_effbot               | 1.80 ms                                                         | 1.52 ms: 1.19x faster                                                            |
| pylint                     | 227 ms                                                          | 193 ms: 1.18x faster                                                             |
| sphinx                     | 719 ms                                                          | 615 ms: 1.17x faster                                                             |
| raytrace                   | 201 ms                                                          | 174 ms: 1.16x faster                                                             |
| scimark_sparse_mat_mult    | 2.84 ms                                                         | 2.47 ms: 1.15x faster                                                            |
| 2to3                       | 250 ms                                                          | 218 ms: 1.15x faster                                                             |
| scimark_fft                | 205 ms                                                          | 179 ms: 1.15x faster                                                             |
| fannkuch                   | 299 ms                                                          | 262 ms: 1.14x faster                                                             |
| xml_etree_process          | 44.2 ms                                                         | 38.8 ms: 1.14x faster                                                            |
| scimark_sor                | 85.9 ms                                                         | 76.0 ms: 1.13x faster                                                            |
| generators                 | 21.8 ms                                                         | 19.3 ms: 1.13x faster                                                            |
| comprehensions             | 12.5 us                                                         | 11.1 us: 1.12x faster                                                            |
| docutils                   | 1.78 sec                                                        | 1.59 sec: 1.12x faster                                                           |
| python_startup             | 28.3 ms                                                         | 25.3 ms: 1.12x faster                                                            |
| coroutines                 | 16.2 ms                                                         | 14.6 ms: 1.11x faster                                                            |
| pyflate                    | 320 ms                                                          | 289 ms: 1.11x faster                                                             |
| hexiom                     | 4.44 ms                                                         | 4.02 ms: 1.10x faster                                                            |
| logging_silent             | 60.3 ns                                                         | 55.0 ns: 1.10x faster                                                            |
| pickle_pure_python         | 231 us                                                          | 212 us: 1.09x faster                                                             |
| xml_etree_generate         | 61.4 ms                                                         | 56.6 ms: 1.09x faster                                                            |
| mako                       | 7.09 ms                                                         | 6.58 ms: 1.08x faster                                                            |
| spectral_norm              | 69.4 ms                                                         | 64.6 ms: 1.07x faster                                                            |
| deltablue                  | 2.33 ms                                                         | 2.18 ms: 1.07x faster                                                            |
| meteor_contest             | 74.6 ms                                                         | 70.9 ms: 1.05x faster                                                            |
| scimark_lu                 | 60.2 ms                                                         | 57.6 ms: 1.05x faster                                                            |
| python_startup_no_site     | 19.7 ms                                                         | 19.2 ms: 1.02x faster                                                            |
| bench_mp_pool              | 90.6 ms                                                         | 91.7 ms: 1.01x slower                                                            |
| xml_etree_iterparse        | 62.6 ms                                                         | 64.3 ms: 1.03x slower                                                            |
| regex_dna                  | 114 ms                                                          | 118 ms: 1.04x slower                                                             |
| gc_traversal               | 1.75 ms                                                         | 2.06 ms: 1.18x slower                                                            |
| create_gc_cycles           | 1.06 ms                                                         | 1.26 ms: 1.19x slower                                                            |
| k_core                     | 1.38 sec                                                        | 1.65 sec: 1.20x slower                                                           |
| connected_components       | 267 ms                                                          | 322 ms: 1.21x slower                                                             |
| shortest_path              | 290 ms                                                          | 353 ms: 1.22x slower                                                             |
| many_optionals             | 436 us                                                          | 555 us: 1.27x slower                                                             |
| subparsers                 | 14.8 ms                                                         | 29.7 ms: 2.01x slower                                                            |
| Geometric mean             | (ref)                                                           | 1.28x faster                                                                     |
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250816-3.15.0a0-3663b2a/bm-20250816-pythonperf1_win32-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.281x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.19x
- 95% likely to have a speedup of 1.18x
- 99% likely to have a speedup of 1.17x

# Memory
- memory change: unknown