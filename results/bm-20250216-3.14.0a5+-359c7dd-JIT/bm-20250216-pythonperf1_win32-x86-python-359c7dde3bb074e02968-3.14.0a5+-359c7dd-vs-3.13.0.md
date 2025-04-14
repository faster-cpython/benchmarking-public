# Results vs. 3.13.0

- fork: python
- ref: 359c7dde3bb074e02968
- machine: windows-x86
- commit hash: 359c7dd
- commit date: 2025-02-16
- overall geometric mean: 1.052x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250216-pythonperf1_win32-x86-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 250 ms                                                          | 276 ms: 1.10x slower                                                            |
| docutils       | 1.78 sec                                                        | 2.06 sec: 1.16x slower                                                          |
| html5lib       | 47.5 ms                                                         | 49.8 ms: 1.05x slower                                                           |
| sphinx         | 719 ms                                                          | 789 ms: 1.10x slower                                                            |
| Geometric mean | (ref)                                                           | 1.10x slower                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250216-pythonperf1_win32-x86-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_io              | 526 ms                                                          | 506 ms: 1.04x faster                                                            |
| asyncio_websockets         | 363 ms                                                          | 352 ms: 1.03x faster                                                            |
| async_tree_memoization_tg  | 282 ms                                                          | 275 ms: 1.03x faster                                                            |
| async_tree_io_tg           | 494 ms                                                          | 500 ms: 1.01x slower                                                            |
| coroutines                 | 16.2 ms                                                         | 16.5 ms: 1.02x slower                                                           |
| async_tree_none_tg         | 214 ms                                                          | 220 ms: 1.03x slower                                                            |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 500 ms: 1.03x slower                                                            |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 482 ms: 1.06x slower                                                            |
| async_generators           | 270 ms                                                          | 338 ms: 1.25x slower                                                            |
| Geometric mean             | (ref)                                                           | 1.03x slower                                                                    |

Benchmark hidden because not significant (2): async_tree_memoization, async_tree_none

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250216-pythonperf1_win32-x86-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pidigits       | 201 ms                                                          | 203 ms: 1.01x slower                                                            |
| nbody          | 80.0 ms                                                         | 113 ms: 1.41x slower                                                            |
| Geometric mean | (ref)                                                           | 1.13x slower                                                                    |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250216-pythonperf1_win32-x86-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_effbot   | 1.80 ms                                                         | 1.55 ms: 1.16x faster                                                           |
| regex_dna      | 114 ms                                                          | 121 ms: 1.06x slower                                                            |
| regex_compile  | 101 ms                                                          | 122 ms: 1.21x slower                                                            |
| Geometric mean | (ref)                                                           | 1.01x slower                                                                    |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250216-pythonperf1_win32-x86-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| json_loads           | 21.6 us                                                         | 22.7 us: 1.05x slower                                                           |
| xml_etree_iterparse  | 62.6 ms                                                         | 65.6 ms: 1.05x slower                                                           |
| tomli_loads          | 1.71 sec                                                        | 1.89 sec: 1.10x slower                                                          |
| xml_etree_generate   | 61.4 ms                                                         | 73.1 ms: 1.19x slower                                                           |
| json_dumps           | 7.30 ms                                                         | 9.21 ms: 1.26x slower                                                           |
| xml_etree_process    | 44.2 ms                                                         | 56.0 ms: 1.27x slower                                                           |
| pickle_pure_python   | 231 us                                                          | 334 us: 1.45x slower                                                            |
| unpickle_pure_python | 160 us                                                          | 244 us: 1.52x slower                                                            |
| Geometric mean       | (ref)                                                           | 1.20x slower                                                                    |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250216-pythonperf1_win32-x86-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 28.3 ms                                                         | 27.8 ms: 1.02x faster                                                           |
| python_startup_no_site | 19.7 ms                                                         | 21.3 ms: 1.08x slower                                                           |
| Geometric mean         | (ref)                                                           | 1.03x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250216-pythonperf1_win32-x86-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_xml      | 50.1 ms                                                         | 53.5 ms: 1.07x slower                                                           |
| genshi_text     | 21.5 ms                                                         | 23.2 ms: 1.08x slower                                                           |
| mako            | 7.09 ms                                                         | 7.78 ms: 1.10x slower                                                           |
| django_template | 29.8 ms                                                         | 38.8 ms: 1.30x slower                                                           |
| Geometric mean  | (ref)                                                           | 1.13x slower                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250216-pythonperf1_win32-x86-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| thrift                     | 9.98 ms                                                         | 777 us: 12.85x faster                                                           |
| coverage                   | 324 ms                                                          | 54.2 ms: 5.97x faster                                                           |
| pathlib                    | 82.9 ms                                                         | 34.8 ms: 2.38x faster                                                           |
| sqlglot_normalize          | 216 ms                                                          | 108 ms: 2.00x faster                                                            |
| regex_effbot               | 1.80 ms                                                         | 1.55 ms: 1.16x faster                                                           |
| deepcopy                   | 314 us                                                          | 272 us: 1.15x faster                                                            |
| deepcopy_memo              | 25.4 us                                                         | 22.2 us: 1.15x faster                                                           |
| async_tree_io              | 526 ms                                                          | 506 ms: 1.04x faster                                                            |
| asyncio_websockets         | 363 ms                                                          | 352 ms: 1.03x faster                                                            |
| async_tree_memoization_tg  | 282 ms                                                          | 275 ms: 1.03x faster                                                            |
| deepcopy_reduce            | 2.92 us                                                         | 2.84 us: 1.03x faster                                                           |
| create_gc_cycles           | 1.06 ms                                                         | 1.04 ms: 1.02x faster                                                           |
| sqlite_synth               | 1.95 us                                                         | 1.91 us: 1.02x faster                                                           |
| python_startup             | 28.3 ms                                                         | 27.8 ms: 1.02x faster                                                           |
| bench_mp_pool              | 90.6 ms                                                         | 89.6 ms: 1.01x faster                                                           |
| pidigits                   | 201 ms                                                          | 203 ms: 1.01x slower                                                            |
| async_tree_io_tg           | 494 ms                                                          | 500 ms: 1.01x slower                                                            |
| coroutines                 | 16.2 ms                                                         | 16.5 ms: 1.02x slower                                                           |
| async_tree_none_tg         | 214 ms                                                          | 220 ms: 1.03x slower                                                            |
| pylint                     | 227 ms                                                          | 233 ms: 1.03x slower                                                            |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 500 ms: 1.03x slower                                                            |
| gc_traversal               | 1.75 ms                                                         | 1.83 ms: 1.04x slower                                                           |
| spectral_norm              | 69.4 ms                                                         | 72.5 ms: 1.04x slower                                                           |
| k_core                     | 1.38 sec                                                        | 1.44 sec: 1.05x slower                                                          |
| json_loads                 | 21.6 us                                                         | 22.7 us: 1.05x slower                                                           |
| xml_etree_iterparse        | 62.6 ms                                                         | 65.6 ms: 1.05x slower                                                           |
| html5lib                   | 47.5 ms                                                         | 49.8 ms: 1.05x slower                                                           |
| mdp                        | 1.62 sec                                                        | 1.71 sec: 1.05x slower                                                          |
| bench_thread_pool          | 1.00 ms                                                         | 1.05 ms: 1.05x slower                                                           |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 482 ms: 1.06x slower                                                            |
| regex_dna                  | 114 ms                                                          | 121 ms: 1.06x slower                                                            |
| genshi_xml                 | 50.1 ms                                                         | 53.5 ms: 1.07x slower                                                           |
| go                         | 109 ms                                                          | 116 ms: 1.07x slower                                                            |
| json                       | 4.27 ms                                                         | 4.61 ms: 1.08x slower                                                           |
| genshi_text                | 21.5 ms                                                         | 23.2 ms: 1.08x slower                                                           |
| python_startup_no_site     | 19.7 ms                                                         | 21.3 ms: 1.08x slower                                                           |
| dulwich_log                | 48.8 ms                                                         | 53.0 ms: 1.09x slower                                                           |
| sympy_sum                  | 106 ms                                                          | 116 ms: 1.10x slower                                                            |
| sphinx                     | 719 ms                                                          | 789 ms: 1.10x slower                                                            |
| mako                       | 7.09 ms                                                         | 7.78 ms: 1.10x slower                                                           |
| tomli_loads                | 1.71 sec                                                        | 1.89 sec: 1.10x slower                                                          |
| logging_format             | 8.72 us                                                         | 9.60 us: 1.10x slower                                                           |
| 2to3                       | 250 ms                                                          | 276 ms: 1.10x slower                                                            |
| generators                 | 21.8 ms                                                         | 24.1 ms: 1.11x slower                                                           |
| logging_simple             | 7.99 us                                                         | 8.83 us: 1.11x slower                                                           |
| pyflate                    | 320 ms                                                          | 358 ms: 1.12x slower                                                            |
| scimark_lu                 | 60.2 ms                                                         | 67.5 ms: 1.12x slower                                                           |
| telco                      | 6.96 ms                                                         | 7.81 ms: 1.12x slower                                                           |
| scimark_sparse_mat_mult    | 2.84 ms                                                         | 3.19 ms: 1.12x slower                                                           |
| sympy_str                  | 212 ms                                                          | 238 ms: 1.13x slower                                                            |
| shortest_path              | 290 ms                                                          | 327 ms: 1.13x slower                                                            |
| pycparser                  | 872 ms                                                          | 982 ms: 1.13x slower                                                            |
| sympy_expand               | 373 ms                                                          | 423 ms: 1.13x slower                                                            |
| connected_components       | 267 ms                                                          | 302 ms: 1.13x slower                                                            |
| scimark_monte_carlo        | 47.7 ms                                                         | 54.4 ms: 1.14x slower                                                           |
| sympy_integrate            | 15.0 ms                                                         | 17.1 ms: 1.14x slower                                                           |
| scimark_sor                | 85.9 ms                                                         | 98.4 ms: 1.14x slower                                                           |
| docutils                   | 1.78 sec                                                        | 2.06 sec: 1.16x slower                                                          |
| logging_silent             | 60.3 ns                                                         | 71.1 ns: 1.18x slower                                                           |
| xml_etree_generate         | 61.4 ms                                                         | 73.1 ms: 1.19x slower                                                           |
| chaos                      | 50.2 ms                                                         | 60.0 ms: 1.20x slower                                                           |
| regex_compile              | 101 ms                                                          | 122 ms: 1.21x slower                                                            |
| bpe_tokeniser              | 3.46 sec                                                        | 4.21 sec: 1.22x slower                                                          |
| meteor_contest             | 74.6 ms                                                         | 91.5 ms: 1.23x slower                                                           |
| richards                   | 32.7 ms                                                         | 40.1 ms: 1.23x slower                                                           |
| richards_super             | 36.7 ms                                                         | 45.0 ms: 1.23x slower                                                           |
| pprint_safe_repr           | 648 ms                                                          | 801 ms: 1.24x slower                                                            |
| sqlglot_optimize           | 41.4 ms                                                         | 51.2 ms: 1.24x slower                                                           |
| pprint_pformat             | 1.33 sec                                                        | 1.65 sec: 1.24x slower                                                          |
| async_generators           | 270 ms                                                          | 338 ms: 1.25x slower                                                            |
| hexiom                     | 4.44 ms                                                         | 5.59 ms: 1.26x slower                                                           |
| json_dumps                 | 7.30 ms                                                         | 9.21 ms: 1.26x slower                                                           |
| xml_etree_process          | 44.2 ms                                                         | 56.0 ms: 1.27x slower                                                           |
| fannkuch                   | 299 ms                                                          | 379 ms: 1.27x slower                                                            |
| deltablue                  | 2.33 ms                                                         | 2.99 ms: 1.28x slower                                                           |
| sqlglot_transpile          | 1.24 ms                                                         | 1.59 ms: 1.28x slower                                                           |
| nqueens                    | 72.1 ms                                                         | 93.5 ms: 1.30x slower                                                           |
| django_template            | 29.8 ms                                                         | 38.8 ms: 1.30x slower                                                           |
| sqlglot_parse              | 1.00 ms                                                         | 1.31 ms: 1.31x slower                                                           |
| typing_runtime_protocols   | 138 us                                                          | 181 us: 1.31x slower                                                            |
| raytrace                   | 201 ms                                                          | 266 ms: 1.32x slower                                                            |
| many_optionals             | 436 us                                                          | 589 us: 1.35x slower                                                            |
| scimark_fft                | 205 ms                                                          | 279 ms: 1.36x slower                                                            |
| comprehensions             | 12.5 us                                                         | 17.2 us: 1.38x slower                                                           |
| nbody                      | 80.0 ms                                                         | 113 ms: 1.41x slower                                                            |
| crypto_pyaes               | 56.9 ms                                                         | 81.4 ms: 1.43x slower                                                           |
| pickle_pure_python         | 231 us                                                          | 334 us: 1.45x slower                                                            |
| unpickle_pure_python       | 160 us                                                          | 244 us: 1.52x slower                                                            |
| subparsers                 | 14.8 ms                                                         | 23.0 ms: 1.56x slower                                                           |
| Geometric mean             | (ref)                                                           | 1.05x slower                                                                    |

Benchmark hidden because not significant (5): regex_v8, async_tree_memoization, float, async_tree_none, xml_etree_parse
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (8) of results/bm-20250216-3.14.0a5+-359c7dd-JIT/bm-20250216-pythonperf1_win32-x86-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.052x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.08x
- 95% likely to have a slowdown of 1.08x
- 99% likely to have a slowdown of 1.06x

# Memory
- memory change: unknown