# Results vs. 3.13.0

- fork: python
- ref: 5ec4bf86b7f4455432ae
- machine: windows-x86
- commit hash: 5ec4bf8
- commit date: 2025-02-22
- overall geometric mean: 1.146x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250222-pythonperf1_win32-x86-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 250 ms                                                          | 235 ms: 1.07x faster                                                            |
| docutils       | 1.78 sec                                                        | 1.72 sec: 1.03x faster                                                          |
| html5lib       | 47.5 ms                                                         | 40.9 ms: 1.16x faster                                                           |
| sphinx         | 719 ms                                                          | 710 ms: 1.01x faster                                                            |
| Geometric mean | (ref)                                                           | 1.07x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250222-pythonperf1_win32-x86-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_none            | 245 ms                                                          | 174 ms: 1.41x faster                                                            |
| async_tree_io              | 526 ms                                                          | 376 ms: 1.40x faster                                                            |
| async_tree_memoization     | 297 ms                                                          | 213 ms: 1.39x faster                                                            |
| async_tree_io_tg           | 494 ms                                                          | 366 ms: 1.35x faster                                                            |
| async_tree_none_tg         | 214 ms                                                          | 159 ms: 1.35x faster                                                            |
| async_tree_memoization_tg  | 282 ms                                                          | 210 ms: 1.35x faster                                                            |
| coroutines                 | 16.2 ms                                                         | 13.5 ms: 1.21x faster                                                           |
| async_generators           | 270 ms                                                          | 233 ms: 1.16x faster                                                            |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 441 ms: 1.10x faster                                                            |
| asyncio_websockets         | 363 ms                                                          | 334 ms: 1.09x faster                                                            |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 429 ms: 1.06x faster                                                            |
| Geometric mean             | (ref)                                                           | 1.25x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250222-pythonperf1_win32-x86-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 54.6 ms                                                         | 46.3 ms: 1.18x faster                                                           |
| nbody          | 80.0 ms                                                         | 69.2 ms: 1.15x faster                                                           |
| pidigits       | 201 ms                                                          | 217 ms: 1.08x slower                                                            |
| Geometric mean | (ref)                                                           | 1.08x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250222-pythonperf1_win32-x86-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 101 ms                                                          | 88.8 ms: 1.14x faster                                                           |
| regex_effbot   | 1.80 ms                                                         | 1.93 ms: 1.07x slower                                                           |
| regex_dna      | 114 ms                                                          | 132 ms: 1.16x slower                                                            |
| Geometric mean | (ref)                                                           | 1.03x slower                                                                    |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250222-pythonperf1_win32-x86-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 1.71 sec                                                        | 1.39 sec: 1.23x faster                                                          |
| unpickle_pure_python | 160 us                                                          | 154 us: 1.04x faster                                                            |
| pickle_pure_python   | 231 us                                                          | 224 us: 1.03x faster                                                            |
| json_loads           | 21.6 us                                                         | 21.4 us: 1.01x faster                                                           |
| json_dumps           | 7.30 ms                                                         | 7.49 ms: 1.03x slower                                                           |
| xml_etree_parse      | 107 ms                                                          | 113 ms: 1.06x slower                                                            |
| xml_etree_process    | 44.2 ms                                                         | 46.8 ms: 1.06x slower                                                           |
| xml_etree_generate   | 61.4 ms                                                         | 67.3 ms: 1.10x slower                                                           |
| xml_etree_iterparse  | 62.6 ms                                                         | 72.6 ms: 1.16x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.01x slower                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250222-pythonperf1_win32-x86-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 28.3 ms                                                         | 28.7 ms: 1.01x slower                                                           |
| python_startup_no_site | 19.7 ms                                                         | 22.1 ms: 1.12x slower                                                           |
| Geometric mean         | (ref)                                                           | 1.07x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250222-pythonperf1_win32-x86-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_xml      | 50.1 ms                                                         | 36.3 ms: 1.38x faster                                                           |
| genshi_text     | 21.5 ms                                                         | 16.1 ms: 1.34x faster                                                           |
| django_template | 29.8 ms                                                         | 27.0 ms: 1.10x faster                                                           |
| mako            | 7.09 ms                                                         | 7.79 ms: 1.10x slower                                                           |
| Geometric mean  | (ref)                                                           | 1.17x faster                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250222-pythonperf1_win32-x86-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| thrift                     | 9.98 ms                                                         | 628 us: 15.89x faster                                                           |
| coverage                   | 324 ms                                                          | 55.0 ms: 5.89x faster                                                           |
| pathlib                    | 82.9 ms                                                         | 32.7 ms: 2.54x faster                                                           |
| deepcopy                   | 314 us                                                          | 187 us: 1.68x faster                                                            |
| deepcopy_reduce            | 2.92 us                                                         | 1.94 us: 1.51x faster                                                           |
| async_tree_none            | 245 ms                                                          | 174 ms: 1.41x faster                                                            |
| deepcopy_memo              | 25.4 us                                                         | 18.2 us: 1.40x faster                                                           |
| async_tree_io              | 526 ms                                                          | 376 ms: 1.40x faster                                                            |
| async_tree_memoization     | 297 ms                                                          | 213 ms: 1.39x faster                                                            |
| genshi_xml                 | 50.1 ms                                                         | 36.3 ms: 1.38x faster                                                           |
| go                         | 109 ms                                                          | 79.1 ms: 1.38x faster                                                           |
| async_tree_io_tg           | 494 ms                                                          | 366 ms: 1.35x faster                                                            |
| async_tree_none_tg         | 214 ms                                                          | 159 ms: 1.35x faster                                                            |
| async_tree_memoization_tg  | 282 ms                                                          | 210 ms: 1.35x faster                                                            |
| genshi_text                | 21.5 ms                                                         | 16.1 ms: 1.34x faster                                                           |
| generators                 | 21.8 ms                                                         | 17.0 ms: 1.28x faster                                                           |
| pprint_pformat             | 1.33 sec                                                        | 1.08 sec: 1.23x faster                                                          |
| tomli_loads                | 1.71 sec                                                        | 1.39 sec: 1.23x faster                                                          |
| pprint_safe_repr           | 648 ms                                                          | 532 ms: 1.22x faster                                                            |
| coroutines                 | 16.2 ms                                                         | 13.5 ms: 1.21x faster                                                           |
| float                      | 54.6 ms                                                         | 46.3 ms: 1.18x faster                                                           |
| telco                      | 6.96 ms                                                         | 5.98 ms: 1.17x faster                                                           |
| deltablue                  | 2.33 ms                                                         | 2.01 ms: 1.16x faster                                                           |
| html5lib                   | 47.5 ms                                                         | 40.9 ms: 1.16x faster                                                           |
| async_generators           | 270 ms                                                          | 233 ms: 1.16x faster                                                            |
| nbody                      | 80.0 ms                                                         | 69.2 ms: 1.15x faster                                                           |
| pycparser                  | 872 ms                                                          | 757 ms: 1.15x faster                                                            |
| sqlglot_parse              | 1.00 ms                                                         | 873 us: 1.15x faster                                                            |
| spectral_norm              | 69.4 ms                                                         | 60.6 ms: 1.15x faster                                                           |
| sympy_expand               | 373 ms                                                          | 328 ms: 1.14x faster                                                            |
| logging_format             | 8.72 us                                                         | 7.65 us: 1.14x faster                                                           |
| scimark_sor                | 85.9 ms                                                         | 75.5 ms: 1.14x faster                                                           |
| regex_compile              | 101 ms                                                          | 88.8 ms: 1.14x faster                                                           |
| logging_simple             | 7.99 us                                                         | 7.10 us: 1.12x faster                                                           |
| sqlglot_transpile          | 1.24 ms                                                         | 1.10 ms: 1.12x faster                                                           |
| chaos                      | 50.2 ms                                                         | 44.9 ms: 1.12x faster                                                           |
| typing_runtime_protocols   | 138 us                                                          | 124 us: 1.11x faster                                                            |
| sympy_str                  | 212 ms                                                          | 190 ms: 1.11x faster                                                            |
| sqlglot_normalize          | 216 ms                                                          | 195 ms: 1.11x faster                                                            |
| pylint                     | 227 ms                                                          | 205 ms: 1.11x faster                                                            |
| scimark_sparse_mat_mult    | 2.84 ms                                                         | 2.57 ms: 1.10x faster                                                           |
| django_template            | 29.8 ms                                                         | 27.0 ms: 1.10x faster                                                           |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 441 ms: 1.10x faster                                                            |
| asyncio_websockets         | 363 ms                                                          | 334 ms: 1.09x faster                                                            |
| scimark_monte_carlo        | 47.7 ms                                                         | 43.8 ms: 1.09x faster                                                           |
| sqlglot_optimize           | 41.4 ms                                                         | 38.4 ms: 1.08x faster                                                           |
| sympy_sum                  | 106 ms                                                          | 98.1 ms: 1.08x faster                                                           |
| fannkuch                   | 299 ms                                                          | 280 ms: 1.07x faster                                                            |
| pyflate                    | 320 ms                                                          | 300 ms: 1.07x faster                                                            |
| 2to3                       | 250 ms                                                          | 235 ms: 1.07x faster                                                            |
| dulwich_log                | 48.8 ms                                                         | 45.8 ms: 1.06x faster                                                           |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 429 ms: 1.06x faster                                                            |
| sqlite_synth               | 1.95 us                                                         | 1.85 us: 1.06x faster                                                           |
| sympy_integrate            | 15.0 ms                                                         | 14.2 ms: 1.06x faster                                                           |
| bpe_tokeniser              | 3.46 sec                                                        | 3.29 sec: 1.05x faster                                                          |
| raytrace                   | 201 ms                                                          | 192 ms: 1.05x faster                                                            |
| unpickle_pure_python       | 160 us                                                          | 154 us: 1.04x faster                                                            |
| shortest_path              | 290 ms                                                          | 279 ms: 1.04x faster                                                            |
| k_core                     | 1.38 sec                                                        | 1.32 sec: 1.04x faster                                                          |
| scimark_fft                | 205 ms                                                          | 197 ms: 1.04x faster                                                            |
| nqueens                    | 72.1 ms                                                         | 69.5 ms: 1.04x faster                                                           |
| connected_components       | 267 ms                                                          | 257 ms: 1.04x faster                                                            |
| docutils                   | 1.78 sec                                                        | 1.72 sec: 1.03x faster                                                          |
| pickle_pure_python         | 231 us                                                          | 224 us: 1.03x faster                                                            |
| richards                   | 32.7 ms                                                         | 32.0 ms: 1.02x faster                                                           |
| richards_super             | 36.7 ms                                                         | 36.0 ms: 1.02x faster                                                           |
| comprehensions             | 12.5 us                                                         | 12.3 us: 1.02x faster                                                           |
| hexiom                     | 4.44 ms                                                         | 4.38 ms: 1.01x faster                                                           |
| sphinx                     | 719 ms                                                          | 710 ms: 1.01x faster                                                            |
| json_loads                 | 21.6 us                                                         | 21.4 us: 1.01x faster                                                           |
| python_startup             | 28.3 ms                                                         | 28.7 ms: 1.01x slower                                                           |
| bench_mp_pool              | 90.6 ms                                                         | 92.4 ms: 1.02x slower                                                           |
| crypto_pyaes               | 56.9 ms                                                         | 58.4 ms: 1.03x slower                                                           |
| json_dumps                 | 7.30 ms                                                         | 7.49 ms: 1.03x slower                                                           |
| meteor_contest             | 74.6 ms                                                         | 76.8 ms: 1.03x slower                                                           |
| logging_silent             | 60.3 ns                                                         | 63.4 ns: 1.05x slower                                                           |
| xml_etree_parse            | 107 ms                                                          | 113 ms: 1.06x slower                                                            |
| xml_etree_process          | 44.2 ms                                                         | 46.8 ms: 1.06x slower                                                           |
| regex_effbot               | 1.80 ms                                                         | 1.93 ms: 1.07x slower                                                           |
| pidigits                   | 201 ms                                                          | 217 ms: 1.08x slower                                                            |
| xml_etree_generate         | 61.4 ms                                                         | 67.3 ms: 1.10x slower                                                           |
| mdp                        | 1.62 sec                                                        | 1.79 sec: 1.10x slower                                                          |
| mako                       | 7.09 ms                                                         | 7.79 ms: 1.10x slower                                                           |
| create_gc_cycles           | 1.06 ms                                                         | 1.17 ms: 1.10x slower                                                           |
| many_optionals             | 436 us                                                          | 489 us: 1.12x slower                                                            |
| python_startup_no_site     | 19.7 ms                                                         | 22.1 ms: 1.12x slower                                                           |
| regex_dna                  | 114 ms                                                          | 132 ms: 1.16x slower                                                            |
| xml_etree_iterparse        | 62.6 ms                                                         | 72.6 ms: 1.16x slower                                                           |
| scimark_lu                 | 60.2 ms                                                         | 74.1 ms: 1.23x slower                                                           |
| subparsers                 | 14.8 ms                                                         | 18.8 ms: 1.27x slower                                                           |
| bench_thread_pool          | 1.00 ms                                                         | 1.32 ms: 1.32x slower                                                           |
| gc_traversal               | 1.75 ms                                                         | 2.45 ms: 1.40x slower                                                           |
| Geometric mean             | (ref)                                                           | 1.14x faster                                                                    |

Benchmark hidden because not significant (2): json, regex_v8
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (8) of results/bm-20250222-3.14.0a5+-5ec4bf8-CLANG/bm-20250222-pythonperf1_win32-x86-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.146x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.06x
- 99% likely to have a speedup of 1.05x

# Memory
- memory change: unknown