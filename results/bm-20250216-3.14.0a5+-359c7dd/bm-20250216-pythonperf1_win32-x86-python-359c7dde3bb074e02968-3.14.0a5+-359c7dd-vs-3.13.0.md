# Results vs. 3.13.0

- fork: python
- ref: 359c7dde3bb074e02968
- machine: windows-x86
- commit hash: 359c7dd
- commit date: 2025-02-16
- overall geometric mean: 1.019x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250216-pythonperf1_win32-x86-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 250 ms                                                          | 263 ms: 1.05x slower                                                            |
| docutils       | 1.78 sec                                                        | 1.89 sec: 1.06x slower                                                          |
| html5lib       | 47.5 ms                                                         | 48.4 ms: 1.02x slower                                                           |
| sphinx         | 719 ms                                                          | 768 ms: 1.07x slower                                                            |
| Geometric mean | (ref)                                                           | 1.05x slower                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250216-pythonperf1_win32-x86-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 282 ms                                                          | 269 ms: 1.05x faster                                                            |
| async_tree_io              | 526 ms                                                          | 502 ms: 1.05x faster                                                            |
| async_tree_none            | 245 ms                                                          | 235 ms: 1.04x faster                                                            |
| async_tree_memoization     | 297 ms                                                          | 284 ms: 1.04x faster                                                            |
| asyncio_websockets         | 363 ms                                                          | 354 ms: 1.03x faster                                                            |
| async_tree_io_tg           | 494 ms                                                          | 500 ms: 1.01x slower                                                            |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 503 ms: 1.04x slower                                                            |
| coroutines                 | 16.2 ms                                                         | 17.1 ms: 1.06x slower                                                           |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 484 ms: 1.06x slower                                                            |
| async_generators           | 270 ms                                                          | 325 ms: 1.20x slower                                                            |
| Geometric mean             | (ref)                                                           | 1.01x slower                                                                    |

Benchmark hidden because not significant (1): async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250216-pythonperf1_win32-x86-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pidigits       | 201 ms                                                          | 200 ms: 1.00x faster                                                            |
| float          | 54.6 ms                                                         | 58.2 ms: 1.07x slower                                                           |
| nbody          | 80.0 ms                                                         | 88.2 ms: 1.10x slower                                                           |
| Geometric mean | (ref)                                                           | 1.05x slower                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250216-pythonperf1_win32-x86-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_effbot   | 1.80 ms                                                         | 1.60 ms: 1.13x faster                                                           |
| regex_dna      | 114 ms                                                          | 119 ms: 1.05x slower                                                            |
| regex_compile  | 101 ms                                                          | 113 ms: 1.12x slower                                                            |
| Geometric mean | (ref)                                                           | 1.00x faster                                                                    |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250216-pythonperf1_win32-x86-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| xml_etree_parse      | 107 ms                                                          | 107 ms: 1.01x faster                                                            |
| tomli_loads          | 1.71 sec                                                        | 1.77 sec: 1.03x slower                                                          |
| json_loads           | 21.6 us                                                         | 22.8 us: 1.05x slower                                                           |
| xml_etree_iterparse  | 62.6 ms                                                         | 67.1 ms: 1.07x slower                                                           |
| xml_etree_generate   | 61.4 ms                                                         | 69.3 ms: 1.13x slower                                                           |
| xml_etree_process    | 44.2 ms                                                         | 51.9 ms: 1.17x slower                                                           |
| unpickle_pure_python | 160 us                                                          | 193 us: 1.21x slower                                                            |
| json_dumps           | 7.30 ms                                                         | 9.33 ms: 1.28x slower                                                           |
| pickle_pure_python   | 231 us                                                          | 305 us: 1.32x slower                                                            |
| Geometric mean       | (ref)                                                           | 1.14x slower                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250216-pythonperf1_win32-x86-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 28.3 ms                                                         | 27.7 ms: 1.02x faster                                                           |
| python_startup_no_site | 19.7 ms                                                         | 21.4 ms: 1.09x slower                                                           |
| Geometric mean         | (ref)                                                           | 1.03x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250216-pythonperf1_win32-x86-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_xml      | 50.1 ms                                                         | 52.3 ms: 1.04x slower                                                           |
| genshi_text     | 21.5 ms                                                         | 23.1 ms: 1.07x slower                                                           |
| mako            | 7.09 ms                                                         | 8.48 ms: 1.20x slower                                                           |
| django_template | 29.8 ms                                                         | 37.1 ms: 1.25x slower                                                           |
| Geometric mean  | (ref)                                                           | 1.14x slower                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250216-pythonperf1_win32-x86-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| thrift                     | 9.98 ms                                                         | 806 us: 12.37x faster                                                           |
| coverage                   | 324 ms                                                          | 53.6 ms: 6.04x faster                                                           |
| pathlib                    | 82.9 ms                                                         | 34.6 ms: 2.40x faster                                                           |
| sqlglot_normalize          | 216 ms                                                          | 103 ms: 2.10x faster                                                            |
| deepcopy                   | 314 us                                                          | 262 us: 1.20x faster                                                            |
| regex_effbot               | 1.80 ms                                                         | 1.60 ms: 1.13x faster                                                           |
| deepcopy_memo              | 25.4 us                                                         | 22.8 us: 1.11x faster                                                           |
| deepcopy_reduce            | 2.92 us                                                         | 2.74 us: 1.06x faster                                                           |
| async_tree_memoization_tg  | 282 ms                                                          | 269 ms: 1.05x faster                                                            |
| async_tree_io              | 526 ms                                                          | 502 ms: 1.05x faster                                                            |
| async_tree_none            | 245 ms                                                          | 235 ms: 1.04x faster                                                            |
| async_tree_memoization     | 297 ms                                                          | 284 ms: 1.04x faster                                                            |
| asyncio_websockets         | 363 ms                                                          | 354 ms: 1.03x faster                                                            |
| sqlite_synth               | 1.95 us                                                         | 1.91 us: 1.02x faster                                                           |
| python_startup             | 28.3 ms                                                         | 27.7 ms: 1.02x faster                                                           |
| bench_mp_pool              | 90.6 ms                                                         | 89.7 ms: 1.01x faster                                                           |
| telco                      | 6.96 ms                                                         | 6.90 ms: 1.01x faster                                                           |
| xml_etree_parse            | 107 ms                                                          | 107 ms: 1.01x faster                                                            |
| pidigits                   | 201 ms                                                          | 200 ms: 1.00x faster                                                            |
| async_tree_io_tg           | 494 ms                                                          | 500 ms: 1.01x slower                                                            |
| bpe_tokeniser              | 3.46 sec                                                        | 3.52 sec: 1.02x slower                                                          |
| html5lib                   | 47.5 ms                                                         | 48.4 ms: 1.02x slower                                                           |
| scimark_sparse_mat_mult    | 2.84 ms                                                         | 2.92 ms: 1.03x slower                                                           |
| go                         | 109 ms                                                          | 112 ms: 1.03x slower                                                            |
| fannkuch                   | 299 ms                                                          | 308 ms: 1.03x slower                                                            |
| gc_traversal               | 1.75 ms                                                         | 1.80 ms: 1.03x slower                                                           |
| shortest_path              | 290 ms                                                          | 299 ms: 1.03x slower                                                            |
| tomli_loads                | 1.71 sec                                                        | 1.77 sec: 1.03x slower                                                          |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 503 ms: 1.04x slower                                                            |
| genshi_xml                 | 50.1 ms                                                         | 52.3 ms: 1.04x slower                                                           |
| regex_dna                  | 114 ms                                                          | 119 ms: 1.05x slower                                                            |
| bench_thread_pool          | 1.00 ms                                                         | 1.05 ms: 1.05x slower                                                           |
| 2to3                       | 250 ms                                                          | 263 ms: 1.05x slower                                                            |
| json_loads                 | 21.6 us                                                         | 22.8 us: 1.05x slower                                                           |
| coroutines                 | 16.2 ms                                                         | 17.1 ms: 1.06x slower                                                           |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 484 ms: 1.06x slower                                                            |
| docutils                   | 1.78 sec                                                        | 1.89 sec: 1.06x slower                                                          |
| float                      | 54.6 ms                                                         | 58.2 ms: 1.07x slower                                                           |
| sphinx                     | 719 ms                                                          | 768 ms: 1.07x slower                                                            |
| xml_etree_iterparse        | 62.6 ms                                                         | 67.1 ms: 1.07x slower                                                           |
| mdp                        | 1.62 sec                                                        | 1.74 sec: 1.07x slower                                                          |
| genshi_text                | 21.5 ms                                                         | 23.1 ms: 1.07x slower                                                           |
| sympy_sum                  | 106 ms                                                          | 114 ms: 1.08x slower                                                            |
| json                       | 4.27 ms                                                         | 4.61 ms: 1.08x slower                                                           |
| meteor_contest             | 74.6 ms                                                         | 80.5 ms: 1.08x slower                                                           |
| pycparser                  | 872 ms                                                          | 940 ms: 1.08x slower                                                            |
| crypto_pyaes               | 56.9 ms                                                         | 61.7 ms: 1.08x slower                                                           |
| python_startup_no_site     | 19.7 ms                                                         | 21.4 ms: 1.09x slower                                                           |
| sympy_str                  | 212 ms                                                          | 232 ms: 1.10x slower                                                            |
| sympy_integrate            | 15.0 ms                                                         | 16.4 ms: 1.10x slower                                                           |
| sympy_expand               | 373 ms                                                          | 412 ms: 1.10x slower                                                            |
| nbody                      | 80.0 ms                                                         | 88.2 ms: 1.10x slower                                                           |
| dulwich_log                | 48.8 ms                                                         | 54.1 ms: 1.11x slower                                                           |
| pprint_safe_repr           | 648 ms                                                          | 722 ms: 1.11x slower                                                            |
| logging_format             | 8.72 us                                                         | 9.73 us: 1.12x slower                                                           |
| regex_compile              | 101 ms                                                          | 113 ms: 1.12x slower                                                            |
| scimark_fft                | 205 ms                                                          | 230 ms: 1.12x slower                                                            |
| logging_simple             | 7.99 us                                                         | 8.98 us: 1.12x slower                                                           |
| xml_etree_generate         | 61.4 ms                                                         | 69.3 ms: 1.13x slower                                                           |
| spectral_norm              | 69.4 ms                                                         | 78.6 ms: 1.13x slower                                                           |
| pprint_pformat             | 1.33 sec                                                        | 1.51 sec: 1.13x slower                                                          |
| nqueens                    | 72.1 ms                                                         | 81.9 ms: 1.14x slower                                                           |
| sqlglot_optimize           | 41.4 ms                                                         | 47.1 ms: 1.14x slower                                                           |
| pyflate                    | 320 ms                                                          | 366 ms: 1.14x slower                                                            |
| comprehensions             | 12.5 us                                                         | 14.3 us: 1.15x slower                                                           |
| sqlglot_transpile          | 1.24 ms                                                         | 1.43 ms: 1.16x slower                                                           |
| scimark_monte_carlo        | 47.7 ms                                                         | 55.4 ms: 1.16x slower                                                           |
| typing_runtime_protocols   | 138 us                                                          | 160 us: 1.16x slower                                                            |
| xml_etree_process          | 44.2 ms                                                         | 51.9 ms: 1.17x slower                                                           |
| sqlglot_parse              | 1.00 ms                                                         | 1.19 ms: 1.19x slower                                                           |
| mako                       | 7.09 ms                                                         | 8.48 ms: 1.20x slower                                                           |
| chaos                      | 50.2 ms                                                         | 60.4 ms: 1.20x slower                                                           |
| async_generators           | 270 ms                                                          | 325 ms: 1.20x slower                                                            |
| scimark_lu                 | 60.2 ms                                                         | 72.5 ms: 1.20x slower                                                           |
| scimark_sor                | 85.9 ms                                                         | 104 ms: 1.21x slower                                                            |
| unpickle_pure_python       | 160 us                                                          | 193 us: 1.21x slower                                                            |
| django_template            | 29.8 ms                                                         | 37.1 ms: 1.25x slower                                                           |
| hexiom                     | 4.44 ms                                                         | 5.58 ms: 1.26x slower                                                           |
| richards_super             | 36.7 ms                                                         | 46.4 ms: 1.26x slower                                                           |
| json_dumps                 | 7.30 ms                                                         | 9.33 ms: 1.28x slower                                                           |
| richards                   | 32.7 ms                                                         | 42.1 ms: 1.29x slower                                                           |
| many_optionals             | 436 us                                                          | 563 us: 1.29x slower                                                            |
| generators                 | 21.8 ms                                                         | 28.4 ms: 1.30x slower                                                           |
| deltablue                  | 2.33 ms                                                         | 3.05 ms: 1.31x slower                                                           |
| pickle_pure_python         | 231 us                                                          | 305 us: 1.32x slower                                                            |
| logging_silent             | 60.3 ns                                                         | 80.3 ns: 1.33x slower                                                           |
| raytrace                   | 201 ms                                                          | 288 ms: 1.43x slower                                                            |
| subparsers                 | 14.8 ms                                                         | 22.6 ms: 1.53x slower                                                           |
| Geometric mean             | (ref)                                                           | 1.02x slower                                                                    |

Benchmark hidden because not significant (6): regex_v8, async_tree_none_tg, create_gc_cycles, k_core, pylint, connected_components
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (8) of results/bm-20250216-3.14.0a5+-359c7dd/bm-20250216-pythonperf1_win32-x86-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.019x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.05x
- 95% likely to have a slowdown of 1.04x
- 99% likely to have a slowdown of 1.03x

# Memory
- memory change: unknown