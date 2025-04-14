# Results vs. 3.13.0

- fork: python
- ref: 61b35f74aa4a6ac60663
- machine: windows-x86
- commit hash: 61b35f7
- commit date: 2025-01-18
- overall geometric mean: 1.079x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.09x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250118-pythonperf1_win32-x86-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 250 ms                                                          | 282 ms: 1.13x slower                                                            |
| docutils       | 1.78 sec                                                        | 2.06 sec: 1.16x slower                                                          |
| html5lib       | 47.5 ms                                                         | 52.8 ms: 1.11x slower                                                           |
| sphinx         | 719 ms                                                          | 831 ms: 1.16x slower                                                            |
| Geometric mean | (ref)                                                           | 1.14x slower                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250118-pythonperf1_win32-x86-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 282 ms                                                          | 256 ms: 1.10x faster                                                            |
| async_tree_none            | 245 ms                                                          | 228 ms: 1.08x faster                                                            |
| async_tree_io              | 526 ms                                                          | 490 ms: 1.07x faster                                                            |
| async_tree_memoization     | 297 ms                                                          | 278 ms: 1.07x faster                                                            |
| async_tree_none_tg         | 214 ms                                                          | 203 ms: 1.05x faster                                                            |
| async_tree_io_tg           | 494 ms                                                          | 473 ms: 1.05x faster                                                            |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 468 ms: 1.03x faster                                                            |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 447 ms: 1.02x faster                                                            |
| asyncio_websockets         | 363 ms                                                          | 361 ms: 1.01x faster                                                            |
| async_generators           | 270 ms                                                          | 323 ms: 1.20x slower                                                            |
| coroutines                 | 16.2 ms                                                         | 21.2 ms: 1.30x slower                                                           |
| Geometric mean             | (ref)                                                           | 1.00x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250118-pythonperf1_win32-x86-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 54.6 ms                                                         | 66.7 ms: 1.22x slower                                                           |
| nbody          | 80.0 ms                                                         | 119 ms: 1.49x slower                                                            |
| Geometric mean | (ref)                                                           | 1.22x slower                                                                    |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250118-pythonperf1_win32-x86-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_effbot   | 1.80 ms                                                         | 1.57 ms: 1.15x faster                                                           |
| regex_dna      | 114 ms                                                          | 123 ms: 1.08x slower                                                            |
| regex_compile  | 101 ms                                                          | 127 ms: 1.26x slower                                                            |
| Geometric mean | (ref)                                                           | 1.04x slower                                                                    |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250118-pythonperf1_win32-x86-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7 |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| xml_etree_parse      | 107 ms                                                          | 109 ms: 1.01x slower                                                            |
| json_loads           | 21.6 us                                                         | 22.0 us: 1.02x slower                                                           |
| xml_etree_iterparse  | 62.6 ms                                                         | 71.4 ms: 1.14x slower                                                           |
| tomli_loads          | 1.71 sec                                                        | 2.02 sec: 1.18x slower                                                          |
| xml_etree_generate   | 61.4 ms                                                         | 73.6 ms: 1.20x slower                                                           |
| xml_etree_process    | 44.2 ms                                                         | 54.8 ms: 1.24x slower                                                           |
| pickle_pure_python   | 231 us                                                          | 305 us: 1.32x slower                                                            |
| json_dumps           | 7.30 ms                                                         | 9.68 ms: 1.33x slower                                                           |
| unpickle_pure_python | 160 us                                                          | 212 us: 1.33x slower                                                            |
| Geometric mean       | (ref)                                                           | 1.19x slower                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250118-pythonperf1_win32-x86-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7 |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 28.3 ms                                                         | 26.9 ms: 1.05x faster                                                           |
| python_startup_no_site | 19.7 ms                                                         | 20.3 ms: 1.03x slower                                                           |
| Geometric mean         | (ref)                                                           | 1.01x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250118-pythonperf1_win32-x86-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7 |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_xml      | 50.1 ms                                                         | 54.0 ms: 1.08x slower                                                           |
| genshi_text     | 21.5 ms                                                         | 25.0 ms: 1.16x slower                                                           |
| django_template | 29.8 ms                                                         | 37.7 ms: 1.26x slower                                                           |
| mako            | 7.09 ms                                                         | 8.96 ms: 1.26x slower                                                           |
| Geometric mean  | (ref)                                                           | 1.19x slower                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250118-pythonperf1_win32-x86-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| thrift                     | 9.98 ms                                                         | 783 us: 12.74x faster                                                           |
| coverage                   | 324 ms                                                          | 53.8 ms: 6.02x faster                                                           |
| sqlglot_normalize          | 216 ms                                                          | 103 ms: 2.10x faster                                                            |
| regex_effbot               | 1.80 ms                                                         | 1.57 ms: 1.15x faster                                                           |
| deepcopy                   | 314 us                                                          | 276 us: 1.14x faster                                                            |
| async_tree_memoization_tg  | 282 ms                                                          | 256 ms: 1.10x faster                                                            |
| async_tree_none            | 245 ms                                                          | 228 ms: 1.08x faster                                                            |
| async_tree_io              | 526 ms                                                          | 490 ms: 1.07x faster                                                            |
| async_tree_memoization     | 297 ms                                                          | 278 ms: 1.07x faster                                                            |
| async_tree_none_tg         | 214 ms                                                          | 203 ms: 1.05x faster                                                            |
| python_startup             | 28.3 ms                                                         | 26.9 ms: 1.05x faster                                                           |
| async_tree_io_tg           | 494 ms                                                          | 473 ms: 1.05x faster                                                            |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 468 ms: 1.03x faster                                                            |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 447 ms: 1.02x faster                                                            |
| deepcopy_reduce            | 2.92 us                                                         | 2.87 us: 1.02x faster                                                           |
| asyncio_websockets         | 363 ms                                                          | 361 ms: 1.01x faster                                                            |
| xml_etree_parse            | 107 ms                                                          | 109 ms: 1.01x slower                                                            |
| json_loads                 | 21.6 us                                                         | 22.0 us: 1.02x slower                                                           |
| gc_traversal               | 1.75 ms                                                         | 1.80 ms: 1.03x slower                                                           |
| python_startup_no_site     | 19.7 ms                                                         | 20.3 ms: 1.03x slower                                                           |
| deepcopy_memo              | 25.4 us                                                         | 26.3 us: 1.04x slower                                                           |
| telco                      | 6.96 ms                                                         | 7.21 ms: 1.04x slower                                                           |
| pathlib                    | 82.9 ms                                                         | 86.2 ms: 1.04x slower                                                           |
| sqlite_synth               | 1.95 us                                                         | 2.04 us: 1.04x slower                                                           |
| k_core                     | 1.38 sec                                                        | 1.46 sec: 1.06x slower                                                          |
| bench_mp_pool              | 90.6 ms                                                         | 96.8 ms: 1.07x slower                                                           |
| genshi_xml                 | 50.1 ms                                                         | 54.0 ms: 1.08x slower                                                           |
| regex_dna                  | 114 ms                                                          | 123 ms: 1.08x slower                                                            |
| bench_thread_pool          | 1.00 ms                                                         | 1.08 ms: 1.08x slower                                                           |
| bpe_tokeniser              | 3.46 sec                                                        | 3.77 sec: 1.09x slower                                                          |
| json                       | 4.27 ms                                                         | 4.67 ms: 1.09x slower                                                           |
| connected_components       | 267 ms                                                          | 293 ms: 1.10x slower                                                            |
| shortest_path              | 290 ms                                                          | 320 ms: 1.10x slower                                                            |
| html5lib                   | 47.5 ms                                                         | 52.8 ms: 1.11x slower                                                           |
| pprint_safe_repr           | 648 ms                                                          | 722 ms: 1.11x slower                                                            |
| meteor_contest             | 74.6 ms                                                         | 83.2 ms: 1.11x slower                                                           |
| pprint_pformat             | 1.33 sec                                                        | 1.49 sec: 1.12x slower                                                          |
| logging_format             | 8.72 us                                                         | 9.77 us: 1.12x slower                                                           |
| go                         | 109 ms                                                          | 122 ms: 1.12x slower                                                            |
| mdp                        | 1.62 sec                                                        | 1.83 sec: 1.12x slower                                                          |
| 2to3                       | 250 ms                                                          | 282 ms: 1.13x slower                                                            |
| pylint                     | 227 ms                                                          | 256 ms: 1.13x slower                                                            |
| logging_simple             | 7.99 us                                                         | 9.09 us: 1.14x slower                                                           |
| xml_etree_iterparse        | 62.6 ms                                                         | 71.4 ms: 1.14x slower                                                           |
| pycparser                  | 872 ms                                                          | 1.00 sec: 1.15x slower                                                          |
| sphinx                     | 719 ms                                                          | 831 ms: 1.16x slower                                                            |
| docutils                   | 1.78 sec                                                        | 2.06 sec: 1.16x slower                                                          |
| sympy_expand               | 373 ms                                                          | 434 ms: 1.16x slower                                                            |
| genshi_text                | 21.5 ms                                                         | 25.0 ms: 1.16x slower                                                           |
| dulwich_log                | 48.8 ms                                                         | 57.0 ms: 1.17x slower                                                           |
| scimark_sparse_mat_mult    | 2.84 ms                                                         | 3.33 ms: 1.17x slower                                                           |
| tomli_loads                | 1.71 sec                                                        | 2.02 sec: 1.18x slower                                                          |
| sympy_str                  | 212 ms                                                          | 249 ms: 1.18x slower                                                            |
| sqlglot_optimize           | 41.4 ms                                                         | 48.9 ms: 1.18x slower                                                           |
| sympy_sum                  | 106 ms                                                          | 125 ms: 1.18x slower                                                            |
| sympy_integrate            | 15.0 ms                                                         | 17.9 ms: 1.19x slower                                                           |
| async_generators           | 270 ms                                                          | 323 ms: 1.20x slower                                                            |
| fannkuch                   | 299 ms                                                          | 358 ms: 1.20x slower                                                            |
| xml_etree_generate         | 61.4 ms                                                         | 73.6 ms: 1.20x slower                                                           |
| typing_runtime_protocols   | 138 us                                                          | 165 us: 1.20x slower                                                            |
| pyflate                    | 320 ms                                                          | 385 ms: 1.20x slower                                                            |
| crypto_pyaes               | 56.9 ms                                                         | 68.7 ms: 1.21x slower                                                           |
| spectral_norm              | 69.4 ms                                                         | 84.5 ms: 1.22x slower                                                           |
| float                      | 54.6 ms                                                         | 66.7 ms: 1.22x slower                                                           |
| xml_etree_process          | 44.2 ms                                                         | 54.8 ms: 1.24x slower                                                           |
| nqueens                    | 72.1 ms                                                         | 89.8 ms: 1.25x slower                                                           |
| regex_compile              | 101 ms                                                          | 127 ms: 1.26x slower                                                            |
| django_template            | 29.8 ms                                                         | 37.7 ms: 1.26x slower                                                           |
| mako                       | 7.09 ms                                                         | 8.96 ms: 1.26x slower                                                           |
| sqlglot_transpile          | 1.24 ms                                                         | 1.56 ms: 1.27x slower                                                           |
| chaos                      | 50.2 ms                                                         | 64.3 ms: 1.28x slower                                                           |
| sqlglot_parse              | 1.00 ms                                                         | 1.28 ms: 1.28x slower                                                           |
| scimark_fft                | 205 ms                                                          | 264 ms: 1.29x slower                                                            |
| coroutines                 | 16.2 ms                                                         | 21.2 ms: 1.30x slower                                                           |
| pickle_pure_python         | 231 us                                                          | 305 us: 1.32x slower                                                            |
| comprehensions             | 12.5 us                                                         | 16.5 us: 1.32x slower                                                           |
| richards_super             | 36.7 ms                                                         | 48.6 ms: 1.32x slower                                                           |
| json_dumps                 | 7.30 ms                                                         | 9.68 ms: 1.33x slower                                                           |
| unpickle_pure_python       | 160 us                                                          | 212 us: 1.33x slower                                                            |
| richards                   | 32.7 ms                                                         | 43.3 ms: 1.33x slower                                                           |
| scimark_monte_carlo        | 47.7 ms                                                         | 63.3 ms: 1.33x slower                                                           |
| scimark_lu                 | 60.2 ms                                                         | 83.9 ms: 1.39x slower                                                           |
| scimark_sor                | 85.9 ms                                                         | 120 ms: 1.39x slower                                                            |
| deltablue                  | 2.33 ms                                                         | 3.25 ms: 1.39x slower                                                           |
| hexiom                     | 4.44 ms                                                         | 6.28 ms: 1.41x slower                                                           |
| raytrace                   | 201 ms                                                          | 289 ms: 1.44x slower                                                            |
| many_optionals             | 436 us                                                          | 638 us: 1.46x slower                                                            |
| nbody                      | 80.0 ms                                                         | 119 ms: 1.49x slower                                                            |
| subparsers                 | 14.8 ms                                                         | 22.6 ms: 1.53x slower                                                           |
| generators                 | 21.8 ms                                                         | 33.6 ms: 1.54x slower                                                           |
| logging_silent             | 60.3 ns                                                         | 95.4 ns: 1.58x slower                                                           |
| Geometric mean             | (ref)                                                           | 1.09x slower                                                                    |

Benchmark hidden because not significant (3): regex_v8, create_gc_cycles, pidigits
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (8) of results/bm-20250118-3.14.0a4+-61b35f7/bm-20250118-pythonperf1_win32-x86-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.079x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.11x
- 95% likely to have a slowdown of 1.11x
- 99% likely to have a slowdown of 1.09x

# Memory
- memory change: unknown