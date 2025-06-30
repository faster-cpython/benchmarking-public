# Results vs. 3.13.0

- fork: python
- ref: 75f40595e555e7d016cf
- machine: windows-amd64
- commit hash: 75f4059
- commit date: 2025-06-30
- overall geometric mean: 1.115x faster
- HPT reliability: 98.49%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250630-pythonperf1_win32-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 250 ms                                                          | 229 ms: 1.09x faster                                                             |
| docutils       | 1.78 sec                                                        | 2.94 sec: 1.65x slower                                                           |
| html5lib       | 47.5 ms                                                         | 41.6 ms: 1.14x faster                                                            |
| sphinx         | 719 ms                                                          | 687 ms: 1.05x faster                                                             |
| Geometric mean | (ref)                                                           | 1.06x slower                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250630-pythonperf1_win32-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059 |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| asyncio_websockets         | 363 ms                                                          | 143 ms: 2.54x faster                                                             |
| async_tree_io              | 526 ms                                                          | 354 ms: 1.48x faster                                                             |
| async_tree_io_tg           | 494 ms                                                          | 334 ms: 1.48x faster                                                             |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 316 ms: 1.44x faster                                                             |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 337 ms: 1.44x faster                                                             |
| async_tree_memoization_tg  | 282 ms                                                          | 197 ms: 1.44x faster                                                             |
| async_tree_none            | 245 ms                                                          | 175 ms: 1.40x faster                                                             |
| async_tree_none_tg         | 214 ms                                                          | 153 ms: 1.40x faster                                                             |
| async_tree_memoization     | 297 ms                                                          | 215 ms: 1.38x faster                                                             |
| coroutines                 | 16.2 ms                                                         | 14.8 ms: 1.10x faster                                                            |
| async_generators           | 270 ms                                                          | 261 ms: 1.03x faster                                                             |
| Geometric mean             | (ref)                                                           | 1.43x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250630-pythonperf1_win32-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pidigits       | 201 ms                                                          | 137 ms: 1.47x faster                                                             |
| float          | 54.6 ms                                                         | 46.2 ms: 1.18x faster                                                            |
| nbody          | 80.0 ms                                                         | 85.9 ms: 1.07x slower                                                            |
| Geometric mean | (ref)                                                           | 1.17x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250630-pythonperf1_win32-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_v8       | 16.8 ms                                                         | 13.5 ms: 1.25x faster                                                            |
| regex_effbot   | 1.80 ms                                                         | 1.62 ms: 1.12x faster                                                            |
| regex_compile  | 101 ms                                                          | 95.9 ms: 1.05x faster                                                            |
| Geometric mean | (ref)                                                           | 1.10x faster                                                                     |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250630-pythonperf1_win32-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059 |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| json_loads           | 21.6 us                                                         | 16.1 us: 1.34x faster                                                            |
| xml_etree_parse      | 107 ms                                                          | 90.4 ms: 1.19x faster                                                            |
| json_dumps           | 7.30 ms                                                         | 6.67 ms: 1.09x faster                                                            |
| xml_etree_iterparse  | 62.6 ms                                                         | 58.8 ms: 1.06x faster                                                            |
| unpickle_pure_python | 160 us                                                          | 156 us: 1.02x faster                                                             |
| pickle_pure_python   | 231 us                                                          | 237 us: 1.03x slower                                                             |
| xml_etree_generate   | 61.4 ms                                                         | 63.3 ms: 1.03x slower                                                            |
| xml_etree_process    | 44.2 ms                                                         | 45.9 ms: 1.04x slower                                                            |
| tomli_loads          | 1.71 sec                                                        | 2.72 sec: 1.59x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.01x faster                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250630-pythonperf1_win32-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059 |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup         | 28.3 ms                                                         | 25.6 ms: 1.10x faster                                                            |
| python_startup_no_site | 19.7 ms                                                         | 19.4 ms: 1.01x faster                                                            |
| Geometric mean         | (ref)                                                           | 1.06x faster                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250630-pythonperf1_win32-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059 |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| genshi_xml      | 50.1 ms                                                         | 41.8 ms: 1.20x faster                                                            |
| genshi_text     | 21.5 ms                                                         | 20.0 ms: 1.07x faster                                                            |
| django_template | 29.8 ms                                                         | 28.2 ms: 1.06x faster                                                            |
| mako            | 7.09 ms                                                         | 9.89 ms: 1.40x slower                                                            |
| Geometric mean  | (ref)                                                           | 1.01x slower                                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250630-pythonperf1_win32-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059 |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| thrift                     | 9.98 ms                                                         | 575 us: 17.35x faster                                                            |
| coverage                   | 324 ms                                                          | 66.9 ms: 4.84x faster                                                            |
| pathlib                    | 82.9 ms                                                         | 32.3 ms: 2.56x faster                                                            |
| asyncio_websockets         | 363 ms                                                          | 143 ms: 2.54x faster                                                             |
| deepcopy                   | 314 us                                                          | 204 us: 1.54x faster                                                             |
| async_tree_io              | 526 ms                                                          | 354 ms: 1.48x faster                                                             |
| async_tree_io_tg           | 494 ms                                                          | 334 ms: 1.48x faster                                                             |
| pidigits                   | 201 ms                                                          | 137 ms: 1.47x faster                                                             |
| sqlite_synth               | 1.95 us                                                         | 1.34 us: 1.45x faster                                                            |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 316 ms: 1.44x faster                                                             |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 337 ms: 1.44x faster                                                             |
| async_tree_memoization_tg  | 282 ms                                                          | 197 ms: 1.44x faster                                                             |
| gc_traversal               | 1.75 ms                                                         | 1.23 ms: 1.42x faster                                                            |
| async_tree_none            | 245 ms                                                          | 175 ms: 1.40x faster                                                             |
| async_tree_none_tg         | 214 ms                                                          | 153 ms: 1.40x faster                                                             |
| json                       | 4.27 ms                                                         | 3.09 ms: 1.38x faster                                                            |
| async_tree_memoization     | 297 ms                                                          | 215 ms: 1.38x faster                                                             |
| mdp                        | 1.62 sec                                                        | 1.18 sec: 1.38x faster                                                           |
| json_loads                 | 21.6 us                                                         | 16.1 us: 1.34x faster                                                            |
| deepcopy_reduce            | 2.92 us                                                         | 2.19 us: 1.33x faster                                                            |
| telco                      | 6.96 ms                                                         | 5.47 ms: 1.27x faster                                                            |
| regex_v8                   | 16.8 ms                                                         | 13.5 ms: 1.25x faster                                                            |
| deepcopy_memo              | 25.4 us                                                         | 21.1 us: 1.21x faster                                                            |
| genshi_xml                 | 50.1 ms                                                         | 41.8 ms: 1.20x faster                                                            |
| logging_format             | 8.72 us                                                         | 7.31 us: 1.19x faster                                                            |
| xml_etree_parse            | 107 ms                                                          | 90.4 ms: 1.19x faster                                                            |
| float                      | 54.6 ms                                                         | 46.2 ms: 1.18x faster                                                            |
| logging_simple             | 7.99 us                                                         | 6.77 us: 1.18x faster                                                            |
| pycparser                  | 872 ms                                                          | 739 ms: 1.18x faster                                                             |
| go                         | 109 ms                                                          | 92.7 ms: 1.17x faster                                                            |
| html5lib                   | 47.5 ms                                                         | 41.6 ms: 1.14x faster                                                            |
| sympy_expand               | 373 ms                                                          | 328 ms: 1.14x faster                                                             |
| bench_mp_pool              | 90.6 ms                                                         | 79.8 ms: 1.13x faster                                                            |
| dulwich_log                | 48.8 ms                                                         | 43.1 ms: 1.13x faster                                                            |
| pprint_safe_repr           | 648 ms                                                          | 573 ms: 1.13x faster                                                             |
| regex_effbot               | 1.80 ms                                                         | 1.62 ms: 1.12x faster                                                            |
| sympy_str                  | 212 ms                                                          | 191 ms: 1.11x faster                                                             |
| python_startup             | 28.3 ms                                                         | 25.6 ms: 1.10x faster                                                            |
| coroutines                 | 16.2 ms                                                         | 14.8 ms: 1.10x faster                                                            |
| json_dumps                 | 7.30 ms                                                         | 6.67 ms: 1.09x faster                                                            |
| 2to3                       | 250 ms                                                          | 229 ms: 1.09x faster                                                             |
| genshi_text                | 21.5 ms                                                         | 20.0 ms: 1.07x faster                                                            |
| sympy_sum                  | 106 ms                                                          | 98.7 ms: 1.07x faster                                                            |
| xml_etree_iterparse        | 62.6 ms                                                         | 58.8 ms: 1.06x faster                                                            |
| typing_runtime_protocols   | 138 us                                                          | 130 us: 1.06x faster                                                             |
| chaos                      | 50.2 ms                                                         | 47.5 ms: 1.06x faster                                                            |
| django_template            | 29.8 ms                                                         | 28.2 ms: 1.06x faster                                                            |
| regex_compile              | 101 ms                                                          | 95.9 ms: 1.05x faster                                                            |
| pylint                     | 227 ms                                                          | 215 ms: 1.05x faster                                                             |
| sympy_integrate            | 15.0 ms                                                         | 14.3 ms: 1.05x faster                                                            |
| sphinx                     | 719 ms                                                          | 687 ms: 1.05x faster                                                             |
| comprehensions             | 12.5 us                                                         | 12.1 us: 1.04x faster                                                            |
| async_generators           | 270 ms                                                          | 261 ms: 1.03x faster                                                             |
| unpickle_pure_python       | 160 us                                                          | 156 us: 1.02x faster                                                             |
| python_startup_no_site     | 19.7 ms                                                         | 19.4 ms: 1.01x faster                                                            |
| pyflate                    | 320 ms                                                          | 318 ms: 1.01x faster                                                             |
| crypto_pyaes               | 56.9 ms                                                         | 57.5 ms: 1.01x slower                                                            |
| scimark_sor                | 85.9 ms                                                         | 87.4 ms: 1.02x slower                                                            |
| nqueens                    | 72.1 ms                                                         | 73.9 ms: 1.03x slower                                                            |
| pickle_pure_python         | 231 us                                                          | 237 us: 1.03x slower                                                             |
| logging_silent             | 60.3 ns                                                         | 62.1 ns: 1.03x slower                                                            |
| xml_etree_generate         | 61.4 ms                                                         | 63.3 ms: 1.03x slower                                                            |
| scimark_fft                | 205 ms                                                          | 212 ms: 1.04x slower                                                             |
| fannkuch                   | 299 ms                                                          | 310 ms: 1.04x slower                                                             |
| xml_etree_process          | 44.2 ms                                                         | 45.9 ms: 1.04x slower                                                            |
| richards                   | 32.7 ms                                                         | 34.1 ms: 1.04x slower                                                            |
| hexiom                     | 4.44 ms                                                         | 4.64 ms: 1.05x slower                                                            |
| deltablue                  | 2.33 ms                                                         | 2.46 ms: 1.06x slower                                                            |
| generators                 | 21.8 ms                                                         | 23.0 ms: 1.06x slower                                                            |
| scimark_monte_carlo        | 47.7 ms                                                         | 50.5 ms: 1.06x slower                                                            |
| spectral_norm              | 69.4 ms                                                         | 74.4 ms: 1.07x slower                                                            |
| nbody                      | 80.0 ms                                                         | 85.9 ms: 1.07x slower                                                            |
| raytrace                   | 201 ms                                                          | 216 ms: 1.08x slower                                                             |
| richards_super             | 36.7 ms                                                         | 39.6 ms: 1.08x slower                                                            |
| bench_thread_pool          | 1.00 ms                                                         | 1.09 ms: 1.09x slower                                                            |
| scimark_sparse_mat_mult    | 2.84 ms                                                         | 3.14 ms: 1.11x slower                                                            |
| many_optionals             | 436 us                                                          | 486 us: 1.11x slower                                                             |
| scimark_lu                 | 60.2 ms                                                         | 67.4 ms: 1.12x slower                                                            |
| meteor_contest             | 74.6 ms                                                         | 86.0 ms: 1.15x slower                                                            |
| pprint_pformat             | 1.33 sec                                                        | 1.74 sec: 1.31x slower                                                           |
| subparsers                 | 14.8 ms                                                         | 19.6 ms: 1.33x slower                                                            |
| mako                       | 7.09 ms                                                         | 9.89 ms: 1.40x slower                                                            |
| tomli_loads                | 1.71 sec                                                        | 2.72 sec: 1.59x slower                                                           |
| bpe_tokeniser              | 3.46 sec                                                        | 5.56 sec: 1.61x slower                                                           |
| docutils                   | 1.78 sec                                                        | 2.94 sec: 1.65x slower                                                           |
| k_core                     | 1.38 sec                                                        | 2.72 sec: 1.98x slower                                                           |
| shortest_path              | 290 ms                                                          | 655 ms: 2.26x slower                                                             |
| connected_components       | 267 ms                                                          | 625 ms: 2.34x slower                                                             |
| Geometric mean             | (ref)                                                           | 1.11x faster                                                                     |

Benchmark hidden because not significant (2): regex_dna, create_gc_cycles
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250630-3.15.0a0-75f4059-NOGIL/bm-20250630-pythonperf1_win32-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.115x faster

# HPT report

- Reliability score: 98.49% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown