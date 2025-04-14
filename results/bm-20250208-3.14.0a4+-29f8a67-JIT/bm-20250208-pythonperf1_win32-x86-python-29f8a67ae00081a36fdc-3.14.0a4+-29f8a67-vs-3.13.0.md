# Results vs. 3.13.0

- fork: python
- ref: 29f8a67ae00081a36fdc
- machine: windows-x86
- commit hash: 29f8a67
- commit date: 2025-02-08
- overall geometric mean: 1.037x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250208-pythonperf1_win32-x86-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 250 ms                                                          | 272 ms: 1.09x slower                                                            |
| docutils       | 1.78 sec                                                        | 1.97 sec: 1.11x slower                                                          |
| sphinx         | 719 ms                                                          | 761 ms: 1.06x slower                                                            |
| Geometric mean | (ref)                                                           | 1.06x slower                                                                    |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250208-pythonperf1_win32-x86-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_io              | 526 ms                                                          | 481 ms: 1.09x faster                                                            |
| async_tree_memoization_tg  | 282 ms                                                          | 264 ms: 1.07x faster                                                            |
| async_tree_memoization     | 297 ms                                                          | 280 ms: 1.06x faster                                                            |
| async_tree_none            | 245 ms                                                          | 231 ms: 1.06x faster                                                            |
| async_tree_io_tg           | 494 ms                                                          | 477 ms: 1.04x faster                                                            |
| coroutines                 | 16.2 ms                                                         | 15.8 ms: 1.02x faster                                                           |
| async_tree_none_tg         | 214 ms                                                          | 209 ms: 1.02x faster                                                            |
| asyncio_websockets         | 363 ms                                                          | 355 ms: 1.02x faster                                                            |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 486 ms: 1.00x slower                                                            |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 470 ms: 1.03x slower                                                            |
| async_generators           | 270 ms                                                          | 335 ms: 1.24x slower                                                            |
| Geometric mean             | (ref)                                                           | 1.01x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250208-pythonperf1_win32-x86-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pidigits       | 201 ms                                                          | 203 ms: 1.01x slower                                                            |
| nbody          | 80.0 ms                                                         | 114 ms: 1.42x slower                                                            |
| Geometric mean | (ref)                                                           | 1.12x slower                                                                    |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250208-pythonperf1_win32-x86-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_effbot   | 1.80 ms                                                         | 1.55 ms: 1.16x faster                                                           |
| regex_v8       | 16.8 ms                                                         | 15.7 ms: 1.07x faster                                                           |
| regex_dna      | 114 ms                                                          | 126 ms: 1.11x slower                                                            |
| regex_compile  | 101 ms                                                          | 117 ms: 1.16x slower                                                            |
| Geometric mean | (ref)                                                           | 1.01x slower                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250208-pythonperf1_win32-x86-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| xml_etree_parse      | 107 ms                                                          | 110 ms: 1.02x slower                                                            |
| json_loads           | 21.6 us                                                         | 22.4 us: 1.04x slower                                                           |
| tomli_loads          | 1.71 sec                                                        | 1.83 sec: 1.07x slower                                                          |
| xml_etree_iterparse  | 62.6 ms                                                         | 67.4 ms: 1.08x slower                                                           |
| xml_etree_generate   | 61.4 ms                                                         | 73.7 ms: 1.20x slower                                                           |
| xml_etree_process    | 44.2 ms                                                         | 55.9 ms: 1.27x slower                                                           |
| json_dumps           | 7.30 ms                                                         | 9.26 ms: 1.27x slower                                                           |
| pickle_pure_python   | 231 us                                                          | 326 us: 1.41x slower                                                            |
| unpickle_pure_python | 160 us                                                          | 226 us: 1.41x slower                                                            |
| Geometric mean       | (ref)                                                           | 1.19x slower                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250208-pythonperf1_win32-x86-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 28.3 ms                                                         | 29.0 ms: 1.03x slower                                                           |
| python_startup_no_site | 19.7 ms                                                         | 21.9 ms: 1.12x slower                                                           |
| Geometric mean         | (ref)                                                           | 1.07x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250208-pythonperf1_win32-x86-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_xml      | 50.1 ms                                                         | 52.1 ms: 1.04x slower                                                           |
| mako            | 7.09 ms                                                         | 7.63 ms: 1.08x slower                                                           |
| genshi_text     | 21.5 ms                                                         | 24.2 ms: 1.13x slower                                                           |
| django_template | 29.8 ms                                                         | 35.8 ms: 1.20x slower                                                           |
| Geometric mean  | (ref)                                                           | 1.11x slower                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250208-pythonperf1_win32-x86-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| thrift                     | 9.98 ms                                                         | 741 us: 13.47x faster                                                           |
| coverage                   | 324 ms                                                          | 55.1 ms: 5.87x faster                                                           |
| sqlglot_normalize          | 216 ms                                                          | 102 ms: 2.12x faster                                                            |
| deepcopy                   | 314 us                                                          | 252 us: 1.25x faster                                                            |
| pathlib                    | 82.9 ms                                                         | 67.7 ms: 1.23x faster                                                           |
| deepcopy_memo              | 25.4 us                                                         | 21.4 us: 1.19x faster                                                           |
| regex_effbot               | 1.80 ms                                                         | 1.55 ms: 1.16x faster                                                           |
| deepcopy_reduce            | 2.92 us                                                         | 2.63 us: 1.11x faster                                                           |
| async_tree_io              | 526 ms                                                          | 481 ms: 1.09x faster                                                            |
| regex_v8                   | 16.8 ms                                                         | 15.7 ms: 1.07x faster                                                           |
| async_tree_memoization_tg  | 282 ms                                                          | 264 ms: 1.07x faster                                                            |
| async_tree_memoization     | 297 ms                                                          | 280 ms: 1.06x faster                                                            |
| async_tree_none            | 245 ms                                                          | 231 ms: 1.06x faster                                                            |
| spectral_norm              | 69.4 ms                                                         | 65.9 ms: 1.05x faster                                                           |
| sqlite_synth               | 1.95 us                                                         | 1.87 us: 1.04x faster                                                           |
| async_tree_io_tg           | 494 ms                                                          | 477 ms: 1.04x faster                                                            |
| coroutines                 | 16.2 ms                                                         | 15.8 ms: 1.02x faster                                                           |
| async_tree_none_tg         | 214 ms                                                          | 209 ms: 1.02x faster                                                            |
| asyncio_websockets         | 363 ms                                                          | 355 ms: 1.02x faster                                                            |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 486 ms: 1.00x slower                                                            |
| pidigits                   | 201 ms                                                          | 203 ms: 1.01x slower                                                            |
| go                         | 109 ms                                                          | 111 ms: 1.02x slower                                                            |
| xml_etree_parse            | 107 ms                                                          | 110 ms: 1.02x slower                                                            |
| logging_format             | 8.72 us                                                         | 8.90 us: 1.02x slower                                                           |
| python_startup             | 28.3 ms                                                         | 29.0 ms: 1.03x slower                                                           |
| logging_simple             | 7.99 us                                                         | 8.21 us: 1.03x slower                                                           |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 470 ms: 1.03x slower                                                            |
| json_loads                 | 21.6 us                                                         | 22.4 us: 1.04x slower                                                           |
| genshi_xml                 | 50.1 ms                                                         | 52.1 ms: 1.04x slower                                                           |
| k_core                     | 1.38 sec                                                        | 1.44 sec: 1.05x slower                                                          |
| bench_mp_pool              | 90.6 ms                                                         | 95.4 ms: 1.05x slower                                                           |
| json                       | 4.27 ms                                                         | 4.52 ms: 1.06x slower                                                           |
| sphinx                     | 719 ms                                                          | 761 ms: 1.06x slower                                                            |
| gc_traversal               | 1.75 ms                                                         | 1.85 ms: 1.06x slower                                                           |
| pyflate                    | 320 ms                                                          | 340 ms: 1.06x slower                                                            |
| tomli_loads                | 1.71 sec                                                        | 1.83 sec: 1.07x slower                                                          |
| scimark_monte_carlo        | 47.7 ms                                                         | 51.0 ms: 1.07x slower                                                           |
| bench_thread_pool          | 1.00 ms                                                         | 1.07 ms: 1.07x slower                                                           |
| generators                 | 21.8 ms                                                         | 23.4 ms: 1.07x slower                                                           |
| mako                       | 7.09 ms                                                         | 7.63 ms: 1.08x slower                                                           |
| xml_etree_iterparse        | 62.6 ms                                                         | 67.4 ms: 1.08x slower                                                           |
| sympy_sum                  | 106 ms                                                          | 114 ms: 1.08x slower                                                            |
| 2to3                       | 250 ms                                                          | 272 ms: 1.09x slower                                                            |
| sympy_expand               | 373 ms                                                          | 409 ms: 1.09x slower                                                            |
| dulwich_log                | 48.8 ms                                                         | 53.4 ms: 1.09x slower                                                           |
| scimark_lu                 | 60.2 ms                                                         | 66.2 ms: 1.10x slower                                                           |
| docutils                   | 1.78 sec                                                        | 1.97 sec: 1.11x slower                                                          |
| regex_dna                  | 114 ms                                                          | 126 ms: 1.11x slower                                                            |
| sympy_str                  | 212 ms                                                          | 234 ms: 1.11x slower                                                            |
| pycparser                  | 872 ms                                                          | 968 ms: 1.11x slower                                                            |
| mdp                        | 1.62 sec                                                        | 1.81 sec: 1.11x slower                                                          |
| python_startup_no_site     | 19.7 ms                                                         | 21.9 ms: 1.12x slower                                                           |
| connected_components       | 267 ms                                                          | 300 ms: 1.12x slower                                                            |
| genshi_text                | 21.5 ms                                                         | 24.2 ms: 1.13x slower                                                           |
| bpe_tokeniser              | 3.46 sec                                                        | 3.90 sec: 1.13x slower                                                          |
| chaos                      | 50.2 ms                                                         | 56.7 ms: 1.13x slower                                                           |
| telco                      | 6.96 ms                                                         | 7.89 ms: 1.13x slower                                                           |
| sympy_integrate            | 15.0 ms                                                         | 17.1 ms: 1.14x slower                                                           |
| shortest_path              | 290 ms                                                          | 332 ms: 1.14x slower                                                            |
| scimark_sor                | 85.9 ms                                                         | 98.7 ms: 1.15x slower                                                           |
| scimark_sparse_mat_mult    | 2.84 ms                                                         | 3.28 ms: 1.16x slower                                                           |
| logging_silent             | 60.3 ns                                                         | 69.9 ns: 1.16x slower                                                           |
| regex_compile              | 101 ms                                                          | 117 ms: 1.16x slower                                                            |
| richards                   | 32.7 ms                                                         | 38.1 ms: 1.17x slower                                                           |
| sqlglot_transpile          | 1.24 ms                                                         | 1.46 ms: 1.18x slower                                                           |
| sqlglot_parse              | 1.00 ms                                                         | 1.19 ms: 1.19x slower                                                           |
| pprint_safe_repr           | 648 ms                                                          | 773 ms: 1.19x slower                                                            |
| richards_super             | 36.7 ms                                                         | 43.8 ms: 1.19x slower                                                           |
| pprint_pformat             | 1.33 sec                                                        | 1.59 sec: 1.19x slower                                                          |
| django_template            | 29.8 ms                                                         | 35.8 ms: 1.20x slower                                                           |
| xml_etree_generate         | 61.4 ms                                                         | 73.7 ms: 1.20x slower                                                           |
| sqlglot_optimize           | 41.4 ms                                                         | 50.2 ms: 1.21x slower                                                           |
| meteor_contest             | 74.6 ms                                                         | 92.3 ms: 1.24x slower                                                           |
| async_generators           | 270 ms                                                          | 335 ms: 1.24x slower                                                            |
| typing_runtime_protocols   | 138 us                                                          | 173 us: 1.26x slower                                                            |
| raytrace                   | 201 ms                                                          | 253 ms: 1.26x slower                                                            |
| scimark_fft                | 205 ms                                                          | 258 ms: 1.26x slower                                                            |
| xml_etree_process          | 44.2 ms                                                         | 55.9 ms: 1.27x slower                                                           |
| json_dumps                 | 7.30 ms                                                         | 9.26 ms: 1.27x slower                                                           |
| fannkuch                   | 299 ms                                                          | 380 ms: 1.27x slower                                                            |
| deltablue                  | 2.33 ms                                                         | 2.97 ms: 1.28x slower                                                           |
| many_optionals             | 436 us                                                          | 568 us: 1.30x slower                                                            |
| crypto_pyaes               | 56.9 ms                                                         | 74.6 ms: 1.31x slower                                                           |
| comprehensions             | 12.5 us                                                         | 16.4 us: 1.31x slower                                                           |
| hexiom                     | 4.44 ms                                                         | 5.93 ms: 1.34x slower                                                           |
| pickle_pure_python         | 231 us                                                          | 326 us: 1.41x slower                                                            |
| unpickle_pure_python       | 160 us                                                          | 226 us: 1.41x slower                                                            |
| nbody                      | 80.0 ms                                                         | 114 ms: 1.42x slower                                                            |
| nqueens                    | 72.1 ms                                                         | 106 ms: 1.47x slower                                                            |
| subparsers                 | 14.8 ms                                                         | 22.3 ms: 1.51x slower                                                           |
| Geometric mean             | (ref)                                                           | 1.04x slower                                                                    |

Benchmark hidden because not significant (4): float, create_gc_cycles, html5lib, pylint
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (8) of results/bm-20250208-3.14.0a4+-29f8a67-JIT/bm-20250208-pythonperf1_win32-x86-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.037x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.06x
- 95% likely to have a slowdown of 1.06x
- 99% likely to have a slowdown of 1.05x

# Memory
- memory change: unknown