# Results vs. 3.13.0

- fork: python
- ref: 359c7dde3bb074e02968
- machine: windows-x86
- commit hash: 359c7dd
- commit date: 2025-02-16
- overall geometric mean: 1.144x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250216-pythonperf1_win32-x86-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 250 ms                                                          | 234 ms: 1.07x faster                                                            |
| docutils       | 1.78 sec                                                        | 1.72 sec: 1.04x faster                                                          |
| html5lib       | 47.5 ms                                                         | 40.2 ms: 1.18x faster                                                           |
| sphinx         | 719 ms                                                          | 703 ms: 1.02x faster                                                            |
| Geometric mean | (ref)                                                           | 1.08x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250216-pythonperf1_win32-x86-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_none            | 245 ms                                                          | 176 ms: 1.39x faster                                                            |
| async_tree_memoization     | 297 ms                                                          | 217 ms: 1.37x faster                                                            |
| async_tree_io              | 526 ms                                                          | 385 ms: 1.36x faster                                                            |
| async_tree_none_tg         | 214 ms                                                          | 162 ms: 1.33x faster                                                            |
| async_tree_io_tg           | 494 ms                                                          | 376 ms: 1.31x faster                                                            |
| async_tree_memoization_tg  | 282 ms                                                          | 216 ms: 1.31x faster                                                            |
| coroutines                 | 16.2 ms                                                         | 14.0 ms: 1.16x faster                                                           |
| async_generators           | 270 ms                                                          | 235 ms: 1.15x faster                                                            |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 432 ms: 1.12x faster                                                            |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 428 ms: 1.07x faster                                                            |
| asyncio_websockets         | 363 ms                                                          | 342 ms: 1.06x faster                                                            |
| Geometric mean             | (ref)                                                           | 1.23x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250216-pythonperf1_win32-x86-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 54.6 ms                                                         | 45.8 ms: 1.19x faster                                                           |
| nbody          | 80.0 ms                                                         | 71.3 ms: 1.12x faster                                                           |
| pidigits       | 201 ms                                                          | 216 ms: 1.07x slower                                                            |
| Geometric mean | (ref)                                                           | 1.08x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250216-pythonperf1_win32-x86-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 101 ms                                                          | 90.1 ms: 1.12x faster                                                           |
| regex_effbot   | 1.80 ms                                                         | 1.95 ms: 1.08x slower                                                           |
| regex_dna      | 114 ms                                                          | 132 ms: 1.16x slower                                                            |
| Geometric mean | (ref)                                                           | 1.04x slower                                                                    |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250216-pythonperf1_win32-x86-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 1.71 sec                                                        | 1.42 sec: 1.21x faster                                                          |
| pickle_pure_python   | 231 us                                                          | 224 us: 1.03x faster                                                            |
| unpickle_pure_python | 160 us                                                          | 155 us: 1.03x faster                                                            |
| json_loads           | 21.6 us                                                         | 21.5 us: 1.01x faster                                                           |
| xml_etree_parse      | 107 ms                                                          | 110 ms: 1.03x slower                                                            |
| json_dumps           | 7.30 ms                                                         | 7.66 ms: 1.05x slower                                                           |
| xml_etree_process    | 44.2 ms                                                         | 47.0 ms: 1.06x slower                                                           |
| xml_etree_generate   | 61.4 ms                                                         | 67.2 ms: 1.09x slower                                                           |
| xml_etree_iterparse  | 62.6 ms                                                         | 72.3 ms: 1.16x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.01x slower                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250216-pythonperf1_win32-x86-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 28.3 ms                                                         | 28.6 ms: 1.01x slower                                                           |
| python_startup_no_site | 19.7 ms                                                         | 22.1 ms: 1.12x slower                                                           |
| Geometric mean         | (ref)                                                           | 1.07x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250216-pythonperf1_win32-x86-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_xml      | 50.1 ms                                                         | 35.0 ms: 1.43x faster                                                           |
| genshi_text     | 21.5 ms                                                         | 16.1 ms: 1.34x faster                                                           |
| django_template | 29.8 ms                                                         | 27.5 ms: 1.08x faster                                                           |
| mako            | 7.09 ms                                                         | 7.91 ms: 1.12x slower                                                           |
| Geometric mean  | (ref)                                                           | 1.17x faster                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250216-pythonperf1_win32-x86-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| thrift                     | 9.98 ms                                                         | 640 us: 15.58x faster                                                           |
| coverage                   | 324 ms                                                          | 56.3 ms: 5.76x faster                                                           |
| pathlib                    | 82.9 ms                                                         | 31.8 ms: 2.61x faster                                                           |
| deepcopy                   | 314 us                                                          | 187 us: 1.68x faster                                                            |
| deepcopy_reduce            | 2.92 us                                                         | 1.90 us: 1.54x faster                                                           |
| genshi_xml                 | 50.1 ms                                                         | 35.0 ms: 1.43x faster                                                           |
| deepcopy_memo              | 25.4 us                                                         | 18.0 us: 1.41x faster                                                           |
| async_tree_none            | 245 ms                                                          | 176 ms: 1.39x faster                                                            |
| async_tree_memoization     | 297 ms                                                          | 217 ms: 1.37x faster                                                            |
| go                         | 109 ms                                                          | 79.6 ms: 1.37x faster                                                           |
| async_tree_io              | 526 ms                                                          | 385 ms: 1.36x faster                                                            |
| genshi_text                | 21.5 ms                                                         | 16.1 ms: 1.34x faster                                                           |
| async_tree_none_tg         | 214 ms                                                          | 162 ms: 1.33x faster                                                            |
| async_tree_io_tg           | 494 ms                                                          | 376 ms: 1.31x faster                                                            |
| async_tree_memoization_tg  | 282 ms                                                          | 216 ms: 1.31x faster                                                            |
| pprint_safe_repr           | 648 ms                                                          | 518 ms: 1.25x faster                                                            |
| pprint_pformat             | 1.33 sec                                                        | 1.07 sec: 1.24x faster                                                          |
| tomli_loads                | 1.71 sec                                                        | 1.42 sec: 1.21x faster                                                          |
| telco                      | 6.96 ms                                                         | 5.81 ms: 1.20x faster                                                           |
| generators                 | 21.8 ms                                                         | 18.2 ms: 1.19x faster                                                           |
| float                      | 54.6 ms                                                         | 45.8 ms: 1.19x faster                                                           |
| html5lib                   | 47.5 ms                                                         | 40.2 ms: 1.18x faster                                                           |
| coroutines                 | 16.2 ms                                                         | 14.0 ms: 1.16x faster                                                           |
| sympy_expand               | 373 ms                                                          | 324 ms: 1.15x faster                                                            |
| sqlglot_parse              | 1.00 ms                                                         | 870 us: 1.15x faster                                                            |
| async_generators           | 270 ms                                                          | 235 ms: 1.15x faster                                                            |
| deltablue                  | 2.33 ms                                                         | 2.03 ms: 1.15x faster                                                           |
| pycparser                  | 872 ms                                                          | 767 ms: 1.14x faster                                                            |
| sqlglot_transpile          | 1.24 ms                                                         | 1.09 ms: 1.13x faster                                                           |
| scimark_sor                | 85.9 ms                                                         | 76.4 ms: 1.12x faster                                                           |
| nbody                      | 80.0 ms                                                         | 71.3 ms: 1.12x faster                                                           |
| regex_compile              | 101 ms                                                          | 90.1 ms: 1.12x faster                                                           |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 432 ms: 1.12x faster                                                            |
| sympy_str                  | 212 ms                                                          | 189 ms: 1.12x faster                                                            |
| pylint                     | 227 ms                                                          | 204 ms: 1.11x faster                                                            |
| logging_format             | 8.72 us                                                         | 7.86 us: 1.11x faster                                                           |
| typing_runtime_protocols   | 138 us                                                          | 124 us: 1.11x faster                                                            |
| sqlglot_normalize          | 216 ms                                                          | 196 ms: 1.10x faster                                                            |
| chaos                      | 50.2 ms                                                         | 45.8 ms: 1.10x faster                                                           |
| logging_simple             | 7.99 us                                                         | 7.31 us: 1.09x faster                                                           |
| bpe_tokeniser              | 3.46 sec                                                        | 3.18 sec: 1.09x faster                                                          |
| django_template            | 29.8 ms                                                         | 27.5 ms: 1.08x faster                                                           |
| sqlglot_optimize           | 41.4 ms                                                         | 38.3 ms: 1.08x faster                                                           |
| sympy_sum                  | 106 ms                                                          | 97.5 ms: 1.08x faster                                                           |
| scimark_monte_carlo        | 47.7 ms                                                         | 44.2 ms: 1.08x faster                                                           |
| spectral_norm              | 69.4 ms                                                         | 64.8 ms: 1.07x faster                                                           |
| 2to3                       | 250 ms                                                          | 234 ms: 1.07x faster                                                            |
| nqueens                    | 72.1 ms                                                         | 67.6 ms: 1.07x faster                                                           |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 428 ms: 1.07x faster                                                            |
| sympy_integrate            | 15.0 ms                                                         | 14.1 ms: 1.06x faster                                                           |
| asyncio_websockets         | 363 ms                                                          | 342 ms: 1.06x faster                                                            |
| pyflate                    | 320 ms                                                          | 303 ms: 1.06x faster                                                            |
| richards                   | 32.7 ms                                                         | 31.0 ms: 1.06x faster                                                           |
| fannkuch                   | 299 ms                                                          | 284 ms: 1.05x faster                                                            |
| connected_components       | 267 ms                                                          | 253 ms: 1.05x faster                                                            |
| sqlite_synth               | 1.95 us                                                         | 1.86 us: 1.05x faster                                                           |
| dulwich_log                | 48.8 ms                                                         | 46.4 ms: 1.05x faster                                                           |
| raytrace                   | 201 ms                                                          | 193 ms: 1.05x faster                                                            |
| k_core                     | 1.38 sec                                                        | 1.32 sec: 1.05x faster                                                          |
| docutils                   | 1.78 sec                                                        | 1.72 sec: 1.04x faster                                                          |
| scimark_sparse_mat_mult    | 2.84 ms                                                         | 2.74 ms: 1.03x faster                                                           |
| pickle_pure_python         | 231 us                                                          | 224 us: 1.03x faster                                                            |
| richards_super             | 36.7 ms                                                         | 35.5 ms: 1.03x faster                                                           |
| unpickle_pure_python       | 160 us                                                          | 155 us: 1.03x faster                                                            |
| json                       | 4.27 ms                                                         | 4.14 ms: 1.03x faster                                                           |
| shortest_path              | 290 ms                                                          | 281 ms: 1.03x faster                                                            |
| scimark_fft                | 205 ms                                                          | 200 ms: 1.02x faster                                                            |
| sphinx                     | 719 ms                                                          | 703 ms: 1.02x faster                                                            |
| crypto_pyaes               | 56.9 ms                                                         | 56.1 ms: 1.02x faster                                                           |
| hexiom                     | 4.44 ms                                                         | 4.40 ms: 1.01x faster                                                           |
| json_loads                 | 21.6 us                                                         | 21.5 us: 1.01x faster                                                           |
| bench_mp_pool              | 90.6 ms                                                         | 91.5 ms: 1.01x slower                                                           |
| python_startup             | 28.3 ms                                                         | 28.6 ms: 1.01x slower                                                           |
| meteor_contest             | 74.6 ms                                                         | 75.7 ms: 1.01x slower                                                           |
| xml_etree_parse            | 107 ms                                                          | 110 ms: 1.03x slower                                                            |
| bench_thread_pool          | 1.00 ms                                                         | 1.04 ms: 1.04x slower                                                           |
| json_dumps                 | 7.30 ms                                                         | 7.66 ms: 1.05x slower                                                           |
| xml_etree_process          | 44.2 ms                                                         | 47.0 ms: 1.06x slower                                                           |
| pidigits                   | 201 ms                                                          | 216 ms: 1.07x slower                                                            |
| regex_effbot               | 1.80 ms                                                         | 1.95 ms: 1.08x slower                                                           |
| mdp                        | 1.62 sec                                                        | 1.77 sec: 1.09x slower                                                          |
| xml_etree_generate         | 61.4 ms                                                         | 67.2 ms: 1.09x slower                                                           |
| many_optionals             | 436 us                                                          | 480 us: 1.10x slower                                                            |
| create_gc_cycles           | 1.06 ms                                                         | 1.18 ms: 1.11x slower                                                           |
| mako                       | 7.09 ms                                                         | 7.91 ms: 1.12x slower                                                           |
| python_startup_no_site     | 19.7 ms                                                         | 22.1 ms: 1.12x slower                                                           |
| logging_silent             | 60.3 ns                                                         | 68.0 ns: 1.13x slower                                                           |
| xml_etree_iterparse        | 62.6 ms                                                         | 72.3 ms: 1.16x slower                                                           |
| regex_dna                  | 114 ms                                                          | 132 ms: 1.16x slower                                                            |
| scimark_lu                 | 60.2 ms                                                         | 73.0 ms: 1.21x slower                                                           |
| subparsers                 | 14.8 ms                                                         | 18.7 ms: 1.26x slower                                                           |
| gc_traversal               | 1.75 ms                                                         | 2.36 ms: 1.35x slower                                                           |
| Geometric mean             | (ref)                                                           | 1.14x faster                                                                    |

Benchmark hidden because not significant (2): comprehensions, regex_v8
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (8) of results/bm-20250216-3.14.0a5+-359c7dd-CLANG/bm-20250216-pythonperf1_win32-x86-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.144x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.06x
- 99% likely to have a speedup of 1.05x

# Memory
- memory change: unknown