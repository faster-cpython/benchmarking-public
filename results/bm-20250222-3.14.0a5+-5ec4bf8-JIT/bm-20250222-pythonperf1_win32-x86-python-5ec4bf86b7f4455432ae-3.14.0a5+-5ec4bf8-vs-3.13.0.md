# Results vs. 3.13.0

- fork: python
- ref: 5ec4bf86b7f4455432ae
- machine: windows-x86
- commit hash: 5ec4bf8
- commit date: 2025-02-22
- overall geometric mean: 1.050x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250222-pythonperf1_win32-x86-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 250 ms                                                          | 278 ms: 1.11x slower                                                            |
| docutils       | 1.78 sec                                                        | 2.00 sec: 1.13x slower                                                          |
| html5lib       | 47.5 ms                                                         | 52.3 ms: 1.10x slower                                                           |
| sphinx         | 719 ms                                                          | 782 ms: 1.09x slower                                                            |
| Geometric mean | (ref)                                                           | 1.11x slower                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250222-pythonperf1_win32-x86-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_io              | 526 ms                                                          | 491 ms: 1.07x faster                                                            |
| async_tree_memoization_tg  | 282 ms                                                          | 269 ms: 1.05x faster                                                            |
| async_tree_io_tg           | 494 ms                                                          | 473 ms: 1.05x faster                                                            |
| async_tree_memoization     | 297 ms                                                          | 284 ms: 1.04x faster                                                            |
| async_tree_none            | 245 ms                                                          | 236 ms: 1.04x faster                                                            |
| asyncio_websockets         | 363 ms                                                          | 352 ms: 1.03x faster                                                            |
| async_tree_none_tg         | 214 ms                                                          | 216 ms: 1.01x slower                                                            |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 503 ms: 1.04x slower                                                            |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 487 ms: 1.07x slower                                                            |
| coroutines                 | 16.2 ms                                                         | 17.5 ms: 1.08x slower                                                           |
| async_generators           | 270 ms                                                          | 314 ms: 1.16x slower                                                            |
| Geometric mean             | (ref)                                                           | 1.01x slower                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250222-pythonperf1_win32-x86-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pidigits       | 201 ms                                                          | 203 ms: 1.01x slower                                                            |
| float          | 54.6 ms                                                         | 57.0 ms: 1.04x slower                                                           |
| nbody          | 80.0 ms                                                         | 115 ms: 1.44x slower                                                            |
| Geometric mean | (ref)                                                           | 1.15x slower                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250222-pythonperf1_win32-x86-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_effbot   | 1.80 ms                                                         | 1.61 ms: 1.12x faster                                                           |
| regex_dna      | 114 ms                                                          | 118 ms: 1.04x slower                                                            |
| regex_compile  | 101 ms                                                          | 123 ms: 1.22x slower                                                            |
| Geometric mean | (ref)                                                           | 1.02x slower                                                                    |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250222-pythonperf1_win32-x86-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| json_loads           | 21.6 us                                                         | 21.8 us: 1.01x slower                                                           |
| xml_etree_iterparse  | 62.6 ms                                                         | 64.9 ms: 1.04x slower                                                           |
| tomli_loads          | 1.71 sec                                                        | 1.87 sec: 1.09x slower                                                          |
| json_dumps           | 7.30 ms                                                         | 8.40 ms: 1.15x slower                                                           |
| xml_etree_generate   | 61.4 ms                                                         | 73.2 ms: 1.19x slower                                                           |
| xml_etree_process    | 44.2 ms                                                         | 56.1 ms: 1.27x slower                                                           |
| pickle_pure_python   | 231 us                                                          | 346 us: 1.50x slower                                                            |
| unpickle_pure_python | 160 us                                                          | 240 us: 1.50x slower                                                            |
| Geometric mean       | (ref)                                                           | 1.18x slower                                                                    |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250222-pythonperf1_win32-x86-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 28.3 ms                                                         | 27.8 ms: 1.02x faster                                                           |
| python_startup_no_site | 19.7 ms                                                         | 21.4 ms: 1.09x slower                                                           |
| Geometric mean         | (ref)                                                           | 1.03x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250222-pythonperf1_win32-x86-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_xml      | 50.1 ms                                                         | 51.8 ms: 1.03x slower                                                           |
| mako            | 7.09 ms                                                         | 7.50 ms: 1.06x slower                                                           |
| genshi_text     | 21.5 ms                                                         | 23.5 ms: 1.09x slower                                                           |
| django_template | 29.8 ms                                                         | 38.9 ms: 1.31x slower                                                           |
| Geometric mean  | (ref)                                                           | 1.12x slower                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250222-pythonperf1_win32-x86-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| thrift                     | 9.98 ms                                                         | 755 us: 13.22x faster                                                           |
| coverage                   | 324 ms                                                          | 53.6 ms: 6.04x faster                                                           |
| pathlib                    | 82.9 ms                                                         | 35.2 ms: 2.35x faster                                                           |
| sqlglot_normalize          | 216 ms                                                          | 105 ms: 2.06x faster                                                            |
| deepcopy                   | 314 us                                                          | 255 us: 1.23x faster                                                            |
| deepcopy_memo              | 25.4 us                                                         | 21.4 us: 1.19x faster                                                           |
| regex_effbot               | 1.80 ms                                                         | 1.61 ms: 1.12x faster                                                           |
| deepcopy_reduce            | 2.92 us                                                         | 2.63 us: 1.11x faster                                                           |
| async_tree_io              | 526 ms                                                          | 491 ms: 1.07x faster                                                            |
| async_tree_memoization_tg  | 282 ms                                                          | 269 ms: 1.05x faster                                                            |
| async_tree_io_tg           | 494 ms                                                          | 473 ms: 1.05x faster                                                            |
| sqlite_synth               | 1.95 us                                                         | 1.87 us: 1.04x faster                                                           |
| async_tree_memoization     | 297 ms                                                          | 284 ms: 1.04x faster                                                            |
| async_tree_none            | 245 ms                                                          | 236 ms: 1.04x faster                                                            |
| asyncio_websockets         | 363 ms                                                          | 352 ms: 1.03x faster                                                            |
| create_gc_cycles           | 1.06 ms                                                         | 1.03 ms: 1.03x faster                                                           |
| python_startup             | 28.3 ms                                                         | 27.8 ms: 1.02x faster                                                           |
| json_loads                 | 21.6 us                                                         | 21.8 us: 1.01x slower                                                           |
| async_tree_none_tg         | 214 ms                                                          | 216 ms: 1.01x slower                                                            |
| pidigits                   | 201 ms                                                          | 203 ms: 1.01x slower                                                            |
| spectral_norm              | 69.4 ms                                                         | 71.4 ms: 1.03x slower                                                           |
| json                       | 4.27 ms                                                         | 4.40 ms: 1.03x slower                                                           |
| genshi_xml                 | 50.1 ms                                                         | 51.8 ms: 1.03x slower                                                           |
| gc_traversal               | 1.75 ms                                                         | 1.81 ms: 1.04x slower                                                           |
| xml_etree_iterparse        | 62.6 ms                                                         | 64.9 ms: 1.04x slower                                                           |
| pylint                     | 227 ms                                                          | 236 ms: 1.04x slower                                                            |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 503 ms: 1.04x slower                                                            |
| regex_dna                  | 114 ms                                                          | 118 ms: 1.04x slower                                                            |
| float                      | 54.6 ms                                                         | 57.0 ms: 1.04x slower                                                           |
| k_core                     | 1.38 sec                                                        | 1.44 sec: 1.04x slower                                                          |
| mako                       | 7.09 ms                                                         | 7.50 ms: 1.06x slower                                                           |
| mdp                        | 1.62 sec                                                        | 1.73 sec: 1.06x slower                                                          |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 487 ms: 1.07x slower                                                            |
| coroutines                 | 16.2 ms                                                         | 17.5 ms: 1.08x slower                                                           |
| telco                      | 6.96 ms                                                         | 7.58 ms: 1.09x slower                                                           |
| sphinx                     | 719 ms                                                          | 782 ms: 1.09x slower                                                            |
| python_startup_no_site     | 19.7 ms                                                         | 21.4 ms: 1.09x slower                                                           |
| scimark_sparse_mat_mult    | 2.84 ms                                                         | 3.09 ms: 1.09x slower                                                           |
| tomli_loads                | 1.71 sec                                                        | 1.87 sec: 1.09x slower                                                          |
| genshi_text                | 21.5 ms                                                         | 23.5 ms: 1.09x slower                                                           |
| sympy_sum                  | 106 ms                                                          | 115 ms: 1.09x slower                                                            |
| dulwich_log                | 48.8 ms                                                         | 53.4 ms: 1.09x slower                                                           |
| html5lib                   | 47.5 ms                                                         | 52.3 ms: 1.10x slower                                                           |
| 2to3                       | 250 ms                                                          | 278 ms: 1.11x slower                                                            |
| sympy_str                  | 212 ms                                                          | 236 ms: 1.11x slower                                                            |
| sympy_expand               | 373 ms                                                          | 416 ms: 1.11x slower                                                            |
| logging_format             | 8.72 us                                                         | 9.78 us: 1.12x slower                                                           |
| shortest_path              | 290 ms                                                          | 326 ms: 1.12x slower                                                            |
| bpe_tokeniser              | 3.46 sec                                                        | 3.90 sec: 1.13x slower                                                          |
| docutils                   | 1.78 sec                                                        | 2.00 sec: 1.13x slower                                                          |
| connected_components       | 267 ms                                                          | 303 ms: 1.14x slower                                                            |
| generators                 | 21.8 ms                                                         | 24.8 ms: 1.14x slower                                                           |
| scimark_lu                 | 60.2 ms                                                         | 68.8 ms: 1.14x slower                                                           |
| sympy_integrate            | 15.0 ms                                                         | 17.1 ms: 1.14x slower                                                           |
| logging_simple             | 7.99 us                                                         | 9.14 us: 1.14x slower                                                           |
| json_dumps                 | 7.30 ms                                                         | 8.40 ms: 1.15x slower                                                           |
| pycparser                  | 872 ms                                                          | 1.01 sec: 1.16x slower                                                          |
| async_generators           | 270 ms                                                          | 314 ms: 1.16x slower                                                            |
| chaos                      | 50.2 ms                                                         | 59.2 ms: 1.18x slower                                                           |
| scimark_sor                | 85.9 ms                                                         | 102 ms: 1.18x slower                                                            |
| scimark_monte_carlo        | 47.7 ms                                                         | 56.6 ms: 1.19x slower                                                           |
| go                         | 109 ms                                                          | 129 ms: 1.19x slower                                                            |
| xml_etree_generate         | 61.4 ms                                                         | 73.2 ms: 1.19x slower                                                           |
| pprint_safe_repr           | 648 ms                                                          | 776 ms: 1.20x slower                                                            |
| pprint_pformat             | 1.33 sec                                                        | 1.59 sec: 1.20x slower                                                          |
| pyflate                    | 320 ms                                                          | 385 ms: 1.20x slower                                                            |
| sqlglot_optimize           | 41.4 ms                                                         | 50.2 ms: 1.21x slower                                                           |
| regex_compile              | 101 ms                                                          | 123 ms: 1.22x slower                                                            |
| nqueens                    | 72.1 ms                                                         | 87.9 ms: 1.22x slower                                                           |
| meteor_contest             | 74.6 ms                                                         | 91.6 ms: 1.23x slower                                                           |
| fannkuch                   | 299 ms                                                          | 370 ms: 1.24x slower                                                            |
| logging_silent             | 60.3 ns                                                         | 75.0 ns: 1.24x slower                                                           |
| typing_runtime_protocols   | 138 us                                                          | 172 us: 1.25x slower                                                            |
| xml_etree_process          | 44.2 ms                                                         | 56.1 ms: 1.27x slower                                                           |
| sqlglot_transpile          | 1.24 ms                                                         | 1.58 ms: 1.28x slower                                                           |
| sqlglot_parse              | 1.00 ms                                                         | 1.30 ms: 1.30x slower                                                           |
| django_template            | 29.8 ms                                                         | 38.9 ms: 1.31x slower                                                           |
| scimark_fft                | 205 ms                                                          | 270 ms: 1.32x slower                                                            |
| richards                   | 32.7 ms                                                         | 43.6 ms: 1.33x slower                                                           |
| bench_thread_pool          | 1.00 ms                                                         | 1.34 ms: 1.33x slower                                                           |
| hexiom                     | 4.44 ms                                                         | 5.92 ms: 1.33x slower                                                           |
| comprehensions             | 12.5 us                                                         | 16.8 us: 1.34x slower                                                           |
| many_optionals             | 436 us                                                          | 596 us: 1.37x slower                                                            |
| deltablue                  | 2.33 ms                                                         | 3.26 ms: 1.40x slower                                                           |
| richards_super             | 36.7 ms                                                         | 51.3 ms: 1.40x slower                                                           |
| crypto_pyaes               | 56.9 ms                                                         | 80.3 ms: 1.41x slower                                                           |
| nbody                      | 80.0 ms                                                         | 115 ms: 1.44x slower                                                            |
| raytrace                   | 201 ms                                                          | 290 ms: 1.44x slower                                                            |
| pickle_pure_python         | 231 us                                                          | 346 us: 1.50x slower                                                            |
| unpickle_pure_python       | 160 us                                                          | 240 us: 1.50x slower                                                            |
| subparsers                 | 14.8 ms                                                         | 22.8 ms: 1.55x slower                                                           |
| Geometric mean             | (ref)                                                           | 1.05x slower                                                                    |

Benchmark hidden because not significant (3): regex_v8, xml_etree_parse, bench_mp_pool
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (8) of results/bm-20250222-3.14.0a5+-5ec4bf8-JIT/bm-20250222-pythonperf1_win32-x86-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.050x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.08x
- 95% likely to have a slowdown of 1.08x
- 99% likely to have a slowdown of 1.06x

# Memory
- memory change: unknown