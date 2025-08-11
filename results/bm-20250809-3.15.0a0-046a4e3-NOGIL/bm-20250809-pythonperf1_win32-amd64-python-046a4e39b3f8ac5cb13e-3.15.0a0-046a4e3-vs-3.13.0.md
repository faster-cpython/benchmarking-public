# Results vs. 3.13.0

- fork: python
- ref: 046a4e39b3f8ac5cb13e
- machine: windows-amd64
- commit hash: 046a4e3
- commit date: 2025-08-09
- overall geometric mean: 1.105x faster
- HPT reliability: 97.45%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250809-pythonperf1_win32-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 250 ms                                                          | 229 ms: 1.09x faster                                                             |
| docutils       | 1.78 sec                                                        | 2.92 sec: 1.64x slower                                                           |
| html5lib       | 47.5 ms                                                         | 41.0 ms: 1.16x faster                                                            |
| Geometric mean | (ref)                                                           | 1.07x slower                                                                     |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250809-pythonperf1_win32-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| asyncio_websockets         | 363 ms                                                          | 142 ms: 2.56x faster                                                             |
| async_tree_io_tg           | 494 ms                                                          | 331 ms: 1.49x faster                                                             |
| async_tree_memoization_tg  | 282 ms                                                          | 190 ms: 1.49x faster                                                             |
| async_tree_io              | 526 ms                                                          | 354 ms: 1.48x faster                                                             |
| async_tree_none_tg         | 214 ms                                                          | 147 ms: 1.46x faster                                                             |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 313 ms: 1.46x faster                                                             |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 336 ms: 1.44x faster                                                             |
| async_tree_none            | 245 ms                                                          | 173 ms: 1.41x faster                                                             |
| async_tree_memoization     | 297 ms                                                          | 210 ms: 1.41x faster                                                             |
| coroutines                 | 16.2 ms                                                         | 15.4 ms: 1.06x faster                                                            |
| async_generators           | 270 ms                                                          | 266 ms: 1.02x faster                                                             |
| Geometric mean             | (ref)                                                           | 1.44x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250809-pythonperf1_win32-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pidigits       | 201 ms                                                          | 137 ms: 1.46x faster                                                             |
| float          | 54.6 ms                                                         | 47.1 ms: 1.16x faster                                                            |
| nbody          | 80.0 ms                                                         | 86.2 ms: 1.08x slower                                                            |
| Geometric mean | (ref)                                                           | 1.16x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250809-pythonperf1_win32-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_v8       | 16.8 ms                                                         | 12.8 ms: 1.31x faster                                                            |
| regex_effbot   | 1.80 ms                                                         | 1.53 ms: 1.18x faster                                                            |
| regex_compile  | 101 ms                                                          | 95.1 ms: 1.06x faster                                                            |
| regex_dna      | 114 ms                                                          | 112 ms: 1.01x faster                                                             |
| Geometric mean | (ref)                                                           | 1.14x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250809-pythonperf1_win32-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|---------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| json_loads          | 21.6 us                                                         | 15.7 us: 1.38x faster                                                            |
| json_dumps          | 7.30 ms                                                         | 5.96 ms: 1.22x faster                                                            |
| xml_etree_parse     | 107 ms                                                          | 90.5 ms: 1.19x faster                                                            |
| xml_etree_iterparse | 62.6 ms                                                         | 58.3 ms: 1.07x faster                                                            |
| xml_etree_process   | 44.2 ms                                                         | 44.7 ms: 1.01x slower                                                            |
| pickle_pure_python  | 231 us                                                          | 235 us: 1.01x slower                                                             |
| xml_etree_generate  | 61.4 ms                                                         | 63.0 ms: 1.03x slower                                                            |
| tomli_loads         | 1.71 sec                                                        | 2.75 sec: 1.61x slower                                                           |
| Geometric mean      | (ref)                                                           | 1.03x faster                                                                     |

Benchmark hidden because not significant (1): unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250809-pythonperf1_win32-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup         | 28.3 ms                                                         | 27.1 ms: 1.04x faster                                                            |
| python_startup_no_site | 19.7 ms                                                         | 20.0 ms: 1.02x slower                                                            |
| Geometric mean         | (ref)                                                           | 1.01x faster                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250809-pythonperf1_win32-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| genshi_xml      | 50.1 ms                                                         | 41.6 ms: 1.21x faster                                                            |
| django_template | 29.8 ms                                                         | 27.3 ms: 1.09x faster                                                            |
| genshi_text     | 21.5 ms                                                         | 20.5 ms: 1.05x faster                                                            |
| mako            | 7.09 ms                                                         | 10.1 ms: 1.42x slower                                                            |
| Geometric mean  | (ref)                                                           | 1.01x slower                                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250809-pythonperf1_win32-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| thrift                     | 9.98 ms                                                         | 577 us: 17.29x faster                                                            |
| coverage                   | 324 ms                                                          | 69.4 ms: 4.67x faster                                                            |
| asyncio_websockets         | 363 ms                                                          | 142 ms: 2.56x faster                                                             |
| pathlib                    | 82.9 ms                                                         | 32.7 ms: 2.54x faster                                                            |
| deepcopy                   | 314 us                                                          | 207 us: 1.52x faster                                                             |
| async_tree_io_tg           | 494 ms                                                          | 331 ms: 1.49x faster                                                             |
| async_tree_memoization_tg  | 282 ms                                                          | 190 ms: 1.49x faster                                                             |
| async_tree_io              | 526 ms                                                          | 354 ms: 1.48x faster                                                             |
| async_tree_none_tg         | 214 ms                                                          | 147 ms: 1.46x faster                                                             |
| pidigits                   | 201 ms                                                          | 137 ms: 1.46x faster                                                             |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 313 ms: 1.46x faster                                                             |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 336 ms: 1.44x faster                                                             |
| async_tree_none            | 245 ms                                                          | 173 ms: 1.41x faster                                                             |
| async_tree_memoization     | 297 ms                                                          | 210 ms: 1.41x faster                                                             |
| json                       | 4.27 ms                                                         | 3.04 ms: 1.41x faster                                                            |
| sqlite_synth               | 1.95 us                                                         | 1.40 us: 1.40x faster                                                            |
| gc_traversal               | 1.75 ms                                                         | 1.26 ms: 1.38x faster                                                            |
| json_loads                 | 21.6 us                                                         | 15.7 us: 1.38x faster                                                            |
| mdp                        | 1.62 sec                                                        | 1.18 sec: 1.38x faster                                                           |
| deepcopy_reduce            | 2.92 us                                                         | 2.18 us: 1.34x faster                                                            |
| telco                      | 6.96 ms                                                         | 5.29 ms: 1.32x faster                                                            |
| regex_v8                   | 16.8 ms                                                         | 12.8 ms: 1.31x faster                                                            |
| json_dumps                 | 7.30 ms                                                         | 5.96 ms: 1.22x faster                                                            |
| genshi_xml                 | 50.1 ms                                                         | 41.6 ms: 1.21x faster                                                            |
| logging_format             | 8.72 us                                                         | 7.32 us: 1.19x faster                                                            |
| xml_etree_parse            | 107 ms                                                          | 90.5 ms: 1.19x faster                                                            |
| regex_effbot               | 1.80 ms                                                         | 1.53 ms: 1.18x faster                                                            |
| deepcopy_memo              | 25.4 us                                                         | 21.8 us: 1.16x faster                                                            |
| pycparser                  | 872 ms                                                          | 752 ms: 1.16x faster                                                             |
| float                      | 54.6 ms                                                         | 47.1 ms: 1.16x faster                                                            |
| html5lib                   | 47.5 ms                                                         | 41.0 ms: 1.16x faster                                                            |
| logging_simple             | 7.99 us                                                         | 6.92 us: 1.15x faster                                                            |
| go                         | 109 ms                                                          | 94.6 ms: 1.15x faster                                                            |
| pprint_safe_repr           | 648 ms                                                          | 565 ms: 1.15x faster                                                             |
| sympy_expand               | 373 ms                                                          | 326 ms: 1.14x faster                                                             |
| dulwich_log                | 48.8 ms                                                         | 42.8 ms: 1.14x faster                                                            |
| bench_mp_pool              | 90.6 ms                                                         | 80.9 ms: 1.12x faster                                                            |
| sympy_str                  | 212 ms                                                          | 191 ms: 1.11x faster                                                             |
| pylint                     | 227 ms                                                          | 207 ms: 1.10x faster                                                             |
| 2to3                       | 250 ms                                                          | 229 ms: 1.09x faster                                                             |
| django_template            | 29.8 ms                                                         | 27.3 ms: 1.09x faster                                                            |
| xml_etree_iterparse        | 62.6 ms                                                         | 58.3 ms: 1.07x faster                                                            |
| sympy_sum                  | 106 ms                                                          | 99.1 ms: 1.07x faster                                                            |
| regex_compile              | 101 ms                                                          | 95.1 ms: 1.06x faster                                                            |
| chaos                      | 50.2 ms                                                         | 47.5 ms: 1.06x faster                                                            |
| coroutines                 | 16.2 ms                                                         | 15.4 ms: 1.06x faster                                                            |
| genshi_text                | 21.5 ms                                                         | 20.5 ms: 1.05x faster                                                            |
| sympy_integrate            | 15.0 ms                                                         | 14.3 ms: 1.05x faster                                                            |
| python_startup             | 28.3 ms                                                         | 27.1 ms: 1.04x faster                                                            |
| typing_runtime_protocols   | 138 us                                                          | 132 us: 1.04x faster                                                             |
| comprehensions             | 12.5 us                                                         | 12.3 us: 1.02x faster                                                            |
| async_generators           | 270 ms                                                          | 266 ms: 1.02x faster                                                             |
| regex_dna                  | 114 ms                                                          | 112 ms: 1.01x faster                                                             |
| xml_etree_process          | 44.2 ms                                                         | 44.7 ms: 1.01x slower                                                            |
| pickle_pure_python         | 231 us                                                          | 235 us: 1.01x slower                                                             |
| python_startup_no_site     | 19.7 ms                                                         | 20.0 ms: 1.02x slower                                                            |
| crypto_pyaes               | 56.9 ms                                                         | 58.0 ms: 1.02x slower                                                            |
| scimark_sor                | 85.9 ms                                                         | 87.7 ms: 1.02x slower                                                            |
| xml_etree_generate         | 61.4 ms                                                         | 63.0 ms: 1.03x slower                                                            |
| scimark_monte_carlo        | 47.7 ms                                                         | 49.0 ms: 1.03x slower                                                            |
| fannkuch                   | 299 ms                                                          | 310 ms: 1.04x slower                                                             |
| logging_silent             | 60.3 ns                                                         | 62.9 ns: 1.04x slower                                                            |
| raytrace                   | 201 ms                                                          | 211 ms: 1.05x slower                                                             |
| richards                   | 32.7 ms                                                         | 34.3 ms: 1.05x slower                                                            |
| nqueens                    | 72.1 ms                                                         | 76.0 ms: 1.05x slower                                                            |
| scimark_fft                | 205 ms                                                          | 217 ms: 1.06x slower                                                             |
| hexiom                     | 4.44 ms                                                         | 4.74 ms: 1.07x slower                                                            |
| generators                 | 21.8 ms                                                         | 23.3 ms: 1.07x slower                                                            |
| deltablue                  | 2.33 ms                                                         | 2.50 ms: 1.07x slower                                                            |
| nbody                      | 80.0 ms                                                         | 86.2 ms: 1.08x slower                                                            |
| richards_super             | 36.7 ms                                                         | 39.8 ms: 1.09x slower                                                            |
| spectral_norm              | 69.4 ms                                                         | 75.8 ms: 1.09x slower                                                            |
| bench_thread_pool          | 1.00 ms                                                         | 1.10 ms: 1.10x slower                                                            |
| scimark_sparse_mat_mult    | 2.84 ms                                                         | 3.17 ms: 1.12x slower                                                            |
| scimark_lu                 | 60.2 ms                                                         | 67.4 ms: 1.12x slower                                                            |
| meteor_contest             | 74.6 ms                                                         | 88.2 ms: 1.18x slower                                                            |
| pprint_pformat             | 1.33 sec                                                        | 1.76 sec: 1.33x slower                                                           |
| many_optionals             | 436 us                                                          | 619 us: 1.42x slower                                                             |
| mako                       | 7.09 ms                                                         | 10.1 ms: 1.42x slower                                                            |
| bpe_tokeniser              | 3.46 sec                                                        | 5.56 sec: 1.61x slower                                                           |
| tomli_loads                | 1.71 sec                                                        | 2.75 sec: 1.61x slower                                                           |
| docutils                   | 1.78 sec                                                        | 2.92 sec: 1.64x slower                                                           |
| k_core                     | 1.38 sec                                                        | 2.70 sec: 1.97x slower                                                           |
| shortest_path              | 290 ms                                                          | 662 ms: 2.28x slower                                                             |
| connected_components       | 267 ms                                                          | 629 ms: 2.36x slower                                                             |
| subparsers                 | 14.8 ms                                                         | 34.9 ms: 2.36x slower                                                            |
| Geometric mean             | (ref)                                                           | 1.10x faster                                                                     |

Benchmark hidden because not significant (4): sphinx, create_gc_cycles, unpickle_pure_python, pyflate
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250809-3.15.0a0-046a4e3-NOGIL/bm-20250809-pythonperf1_win32-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.105x faster

# HPT report

- Reliability score: 97.45% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown