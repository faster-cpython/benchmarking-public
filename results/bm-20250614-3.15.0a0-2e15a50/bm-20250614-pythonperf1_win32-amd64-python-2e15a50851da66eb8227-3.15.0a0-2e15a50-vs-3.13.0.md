# Results vs. 3.13.0

- fork: python
- ref: 2e15a50851da66eb8227
- machine: windows-amd64
- commit hash: 2e15a50
- commit date: 2025-06-14
- overall geometric mean: 1.190x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.14x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250614-pythonperf1_win32-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 250 ms                                                          | 297 ms: 1.19x slower                                                             |
| docutils       | 1.78 sec                                                        | 2.10 sec: 1.18x slower                                                           |
| html5lib       | 47.5 ms                                                         | 51.4 ms: 1.08x slower                                                            |
| sphinx         | 719 ms                                                          | 847 ms: 1.18x slower                                                             |
| Geometric mean | (ref)                                                           | 1.16x slower                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250614-pythonperf1_win32-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50 |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| asyncio_websockets         | 363 ms                                                          | 160 ms: 2.26x faster                                                             |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 440 ms: 1.10x faster                                                             |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 437 ms: 1.04x faster                                                             |
| async_tree_memoization_tg  | 282 ms                                                          | 294 ms: 1.04x slower                                                             |
| async_tree_io              | 526 ms                                                          | 548 ms: 1.04x slower                                                             |
| async_tree_none_tg         | 214 ms                                                          | 238 ms: 1.11x slower                                                             |
| async_tree_io_tg           | 494 ms                                                          | 566 ms: 1.15x slower                                                             |
| async_generators           | 270 ms                                                          | 341 ms: 1.26x slower                                                             |
| coroutines                 | 16.2 ms                                                         | 26.0 ms: 1.60x slower                                                            |
| Geometric mean             | (ref)                                                           | 1.01x slower                                                                     |

Benchmark hidden because not significant (2): async_tree_none, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250614-pythonperf1_win32-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pidigits       | 201 ms                                                          | 147 ms: 1.37x faster                                                             |
| nbody          | 80.0 ms                                                         | 107 ms: 1.34x slower                                                             |
| float          | 54.6 ms                                                         | 76.7 ms: 1.40x slower                                                            |
| Geometric mean | (ref)                                                           | 1.11x slower                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250614-pythonperf1_win32-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_effbot   | 1.80 ms                                                         | 1.73 ms: 1.04x faster                                                            |
| regex_dna      | 114 ms                                                          | 117 ms: 1.03x slower                                                             |
| regex_compile  | 101 ms                                                          | 124 ms: 1.23x slower                                                             |
| Geometric mean | (ref)                                                           | 1.05x slower                                                                     |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250614-pythonperf1_win32-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50 |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| json_loads           | 21.6 us                                                         | 20.4 us: 1.06x faster                                                            |
| json_dumps           | 7.30 ms                                                         | 8.41 ms: 1.15x slower                                                            |
| tomli_loads          | 1.71 sec                                                        | 2.08 sec: 1.21x slower                                                           |
| xml_etree_iterparse  | 62.6 ms                                                         | 90.6 ms: 1.45x slower                                                            |
| xml_etree_generate   | 61.4 ms                                                         | 90.9 ms: 1.48x slower                                                            |
| xml_etree_process    | 44.2 ms                                                         | 65.7 ms: 1.49x slower                                                            |
| pickle_pure_python   | 231 us                                                          | 364 us: 1.57x slower                                                             |
| unpickle_pure_python | 160 us                                                          | 278 us: 1.74x slower                                                             |
| Geometric mean       | (ref)                                                           | 1.31x slower                                                                     |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250614-pythonperf1_win32-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50 |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup         | 28.3 ms                                                         | 27.5 ms: 1.03x faster                                                            |
| python_startup_no_site | 19.7 ms                                                         | 20.1 ms: 1.02x slower                                                            |
| Geometric mean         | (ref)                                                           | 1.00x faster                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250614-pythonperf1_win32-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50 |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| genshi_text     | 21.5 ms                                                         | 24.3 ms: 1.13x slower                                                            |
| django_template | 29.8 ms                                                         | 37.2 ms: 1.25x slower                                                            |
| mako            | 7.09 ms                                                         | 13.0 ms: 1.83x slower                                                            |
| Geometric mean  | (ref)                                                           | 1.27x slower                                                                     |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250614-pythonperf1_win32-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50 |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pathlib                    | 82.9 ms                                                         | 34.6 ms: 2.40x faster                                                            |
| asyncio_websockets         | 363 ms                                                          | 160 ms: 2.26x faster                                                             |
| mdp                        | 1.62 sec                                                        | 1.17 sec: 1.39x faster                                                           |
| pidigits                   | 201 ms                                                          | 147 ms: 1.37x faster                                                             |
| deepcopy                   | 314 us                                                          | 267 us: 1.18x faster                                                             |
| telco                      | 6.96 ms                                                         | 6.26 ms: 1.11x faster                                                            |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 440 ms: 1.10x faster                                                             |
| json                       | 4.27 ms                                                         | 4.02 ms: 1.06x faster                                                            |
| json_loads                 | 21.6 us                                                         | 20.4 us: 1.06x faster                                                            |
| sqlite_synth               | 1.95 us                                                         | 1.86 us: 1.05x faster                                                            |
| deepcopy_reduce            | 2.92 us                                                         | 2.78 us: 1.05x faster                                                            |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 437 ms: 1.04x faster                                                             |
| regex_effbot               | 1.80 ms                                                         | 1.73 ms: 1.04x faster                                                            |
| python_startup             | 28.3 ms                                                         | 27.5 ms: 1.03x faster                                                            |
| python_startup_no_site     | 19.7 ms                                                         | 20.1 ms: 1.02x slower                                                            |
| regex_dna                  | 114 ms                                                          | 117 ms: 1.03x slower                                                             |
| async_tree_memoization_tg  | 282 ms                                                          | 294 ms: 1.04x slower                                                             |
| async_tree_io              | 526 ms                                                          | 548 ms: 1.04x slower                                                             |
| dulwich_log                | 48.8 ms                                                         | 52.5 ms: 1.08x slower                                                            |
| sympy_expand               | 373 ms                                                          | 403 ms: 1.08x slower                                                             |
| html5lib                   | 47.5 ms                                                         | 51.4 ms: 1.08x slower                                                            |
| pylint                     | 227 ms                                                          | 248 ms: 1.10x slower                                                             |
| sympy_sum                  | 106 ms                                                          | 117 ms: 1.11x slower                                                             |
| sympy_str                  | 212 ms                                                          | 234 ms: 1.11x slower                                                             |
| async_tree_none_tg         | 214 ms                                                          | 238 ms: 1.11x slower                                                             |
| sympy_integrate            | 15.0 ms                                                         | 16.7 ms: 1.11x slower                                                            |
| typing_runtime_protocols   | 138 us                                                          | 155 us: 1.13x slower                                                             |
| genshi_text                | 21.5 ms                                                         | 24.3 ms: 1.13x slower                                                            |
| pycparser                  | 872 ms                                                          | 992 ms: 1.14x slower                                                             |
| logging_format             | 8.72 us                                                         | 9.97 us: 1.14x slower                                                            |
| async_tree_io_tg           | 494 ms                                                          | 566 ms: 1.15x slower                                                             |
| json_dumps                 | 7.30 ms                                                         | 8.41 ms: 1.15x slower                                                            |
| bench_mp_pool              | 90.6 ms                                                         | 104 ms: 1.15x slower                                                             |
| logging_simple             | 7.99 us                                                         | 9.41 us: 1.18x slower                                                            |
| sphinx                     | 719 ms                                                          | 847 ms: 1.18x slower                                                             |
| docutils                   | 1.78 sec                                                        | 2.10 sec: 1.18x slower                                                           |
| 2to3                       | 250 ms                                                          | 297 ms: 1.19x slower                                                             |
| tomli_loads                | 1.71 sec                                                        | 2.08 sec: 1.21x slower                                                           |
| regex_compile              | 101 ms                                                          | 124 ms: 1.23x slower                                                             |
| go                         | 109 ms                                                          | 134 ms: 1.23x slower                                                             |
| meteor_contest             | 74.6 ms                                                         | 92.9 ms: 1.25x slower                                                            |
| django_template            | 29.8 ms                                                         | 37.2 ms: 1.25x slower                                                            |
| bpe_tokeniser              | 3.46 sec                                                        | 4.33 sec: 1.25x slower                                                           |
| async_generators           | 270 ms                                                          | 341 ms: 1.26x slower                                                             |
| many_optionals             | 436 us                                                          | 557 us: 1.28x slower                                                             |
| k_core                     | 1.38 sec                                                        | 1.81 sec: 1.31x slower                                                           |
| connected_components       | 267 ms                                                          | 350 ms: 1.31x slower                                                             |
| chaos                      | 50.2 ms                                                         | 66.1 ms: 1.32x slower                                                            |
| nqueens                    | 72.1 ms                                                         | 94.9 ms: 1.32x slower                                                            |
| pprint_pformat             | 1.33 sec                                                        | 1.75 sec: 1.32x slower                                                           |
| pprint_safe_repr           | 648 ms                                                          | 855 ms: 1.32x slower                                                             |
| deepcopy_memo              | 25.4 us                                                         | 33.6 us: 1.32x slower                                                            |
| shortest_path              | 290 ms                                                          | 384 ms: 1.33x slower                                                             |
| nbody                      | 80.0 ms                                                         | 107 ms: 1.34x slower                                                             |
| scimark_fft                | 205 ms                                                          | 276 ms: 1.35x slower                                                             |
| fannkuch                   | 299 ms                                                          | 413 ms: 1.38x slower                                                             |
| create_gc_cycles           | 1.06 ms                                                         | 1.47 ms: 1.39x slower                                                            |
| crypto_pyaes               | 56.9 ms                                                         | 79.8 ms: 1.40x slower                                                            |
| float                      | 54.6 ms                                                         | 76.7 ms: 1.40x slower                                                            |
| pyflate                    | 320 ms                                                          | 460 ms: 1.44x slower                                                             |
| xml_etree_iterparse        | 62.6 ms                                                         | 90.6 ms: 1.45x slower                                                            |
| coverage                   | 324 ms                                                          | 471 ms: 1.45x slower                                                             |
| xml_etree_generate         | 61.4 ms                                                         | 90.9 ms: 1.48x slower                                                            |
| xml_etree_process          | 44.2 ms                                                         | 65.7 ms: 1.49x slower                                                            |
| raytrace                   | 201 ms                                                          | 304 ms: 1.51x slower                                                             |
| subparsers                 | 14.8 ms                                                         | 22.8 ms: 1.54x slower                                                            |
| scimark_sparse_mat_mult    | 2.84 ms                                                         | 4.39 ms: 1.55x slower                                                            |
| scimark_monte_carlo        | 47.7 ms                                                         | 73.8 ms: 1.55x slower                                                            |
| scimark_sor                | 85.9 ms                                                         | 133 ms: 1.55x slower                                                             |
| pickle_pure_python         | 231 us                                                          | 364 us: 1.57x slower                                                             |
| comprehensions             | 12.5 us                                                         | 19.9 us: 1.59x slower                                                            |
| richards_super             | 36.7 ms                                                         | 58.5 ms: 1.60x slower                                                            |
| richards                   | 32.7 ms                                                         | 52.2 ms: 1.60x slower                                                            |
| spectral_norm              | 69.4 ms                                                         | 111 ms: 1.60x slower                                                             |
| coroutines                 | 16.2 ms                                                         | 26.0 ms: 1.60x slower                                                            |
| generators                 | 21.8 ms                                                         | 36.3 ms: 1.67x slower                                                            |
| hexiom                     | 4.44 ms                                                         | 7.46 ms: 1.68x slower                                                            |
| gc_traversal               | 1.75 ms                                                         | 2.95 ms: 1.68x slower                                                            |
| unpickle_pure_python       | 160 us                                                          | 278 us: 1.74x slower                                                             |
| mako                       | 7.09 ms                                                         | 13.0 ms: 1.83x slower                                                            |
| deltablue                  | 2.33 ms                                                         | 4.37 ms: 1.88x slower                                                            |
| scimark_lu                 | 60.2 ms                                                         | 120 ms: 1.99x slower                                                             |
| logging_silent             | 60.3 ns                                                         | 502 ns: 8.32x slower                                                             |
| thrift                     | 9.98 ms                                                         | 103 ms: 10.34x slower                                                            |
| Geometric mean             | (ref)                                                           | 1.26x slower                                                                     |

Benchmark hidden because not significant (6): bench_thread_pool, genshi_xml, async_tree_none, async_tree_memoization, xml_etree_parse, regex_v8
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250614-3.15.0a0-2e15a50/bm-20250614-pythonperf1_win32-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.190x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.17x
- 95% likely to have a slowdown of 1.16x
- 99% likely to have a slowdown of 1.14x

# Memory
- memory change: unknown