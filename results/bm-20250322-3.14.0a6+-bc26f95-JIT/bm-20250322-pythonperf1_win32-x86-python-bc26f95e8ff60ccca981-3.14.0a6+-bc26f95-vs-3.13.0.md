# Results vs. 3.13.0

- fork: python
- ref: bc26f95e8ff60ccca981
- machine: windows-x86
- commit hash: bc26f95
- commit date: 2025-03-22
- overall geometric mean: 1.076x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.10x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250322-pythonperf1_win32-x86-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 250 ms                                                          | 287 ms: 1.15x slower                                                            |
| docutils       | 1.78 sec                                                        | 2.03 sec: 1.14x slower                                                          |
| html5lib       | 47.5 ms                                                         | 51.8 ms: 1.09x slower                                                           |
| sphinx         | 719 ms                                                          | 805 ms: 1.12x slower                                                            |
| Geometric mean | (ref)                                                           | 1.12x slower                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250322-pythonperf1_win32-x86-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| asyncio_websockets         | 363 ms                                                          | 201 ms: 1.81x faster                                                            |
| async_tree_memoization_tg  | 282 ms                                                          | 262 ms: 1.08x faster                                                            |
| async_tree_memoization     | 297 ms                                                          | 281 ms: 1.06x faster                                                            |
| async_tree_io              | 526 ms                                                          | 513 ms: 1.02x faster                                                            |
| async_tree_none            | 245 ms                                                          | 241 ms: 1.01x faster                                                            |
| async_tree_io_tg           | 494 ms                                                          | 501 ms: 1.01x slower                                                            |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 506 ms: 1.04x slower                                                            |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 485 ms: 1.06x slower                                                            |
| coroutines                 | 16.2 ms                                                         | 17.8 ms: 1.10x slower                                                           |
| async_generators           | 270 ms                                                          | 340 ms: 1.26x slower                                                            |
| Geometric mean             | (ref)                                                           | 1.03x faster                                                                    |

Benchmark hidden because not significant (1): async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250322-pythonperf1_win32-x86-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pidigits       | 201 ms                                                          | 201 ms: 1.00x slower                                                            |
| float          | 54.6 ms                                                         | 59.0 ms: 1.08x slower                                                           |
| nbody          | 80.0 ms                                                         | 130 ms: 1.63x slower                                                            |
| Geometric mean | (ref)                                                           | 1.21x slower                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250322-pythonperf1_win32-x86-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_effbot   | 1.80 ms                                                         | 1.59 ms: 1.14x faster                                                           |
| regex_v8       | 16.8 ms                                                         | 15.0 ms: 1.12x faster                                                           |
| regex_dna      | 114 ms                                                          | 115 ms: 1.01x slower                                                            |
| regex_compile  | 101 ms                                                          | 120 ms: 1.18x slower                                                            |
| Geometric mean | (ref)                                                           | 1.02x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250322-pythonperf1_win32-x86-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| json_loads           | 21.6 us                                                         | 22.0 us: 1.01x slower                                                           |
| xml_etree_parse      | 107 ms                                                          | 112 ms: 1.04x slower                                                            |
| xml_etree_iterparse  | 62.6 ms                                                         | 71.2 ms: 1.14x slower                                                           |
| tomli_loads          | 1.71 sec                                                        | 1.96 sec: 1.14x slower                                                          |
| json_dumps           | 7.30 ms                                                         | 8.55 ms: 1.17x slower                                                           |
| xml_etree_generate   | 61.4 ms                                                         | 78.0 ms: 1.27x slower                                                           |
| xml_etree_process    | 44.2 ms                                                         | 58.9 ms: 1.33x slower                                                           |
| pickle_pure_python   | 231 us                                                          | 350 us: 1.51x slower                                                            |
| unpickle_pure_python | 160 us                                                          | 254 us: 1.58x slower                                                            |
| Geometric mean       | (ref)                                                           | 1.23x slower                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250322-pythonperf1_win32-x86-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 28.3 ms                                                         | 28.7 ms: 1.01x slower                                                           |
| python_startup_no_site | 19.7 ms                                                         | 22.8 ms: 1.16x slower                                                           |
| Geometric mean         | (ref)                                                           | 1.08x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250322-pythonperf1_win32-x86-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_xml      | 50.1 ms                                                         | 55.4 ms: 1.10x slower                                                           |
| mako            | 7.09 ms                                                         | 8.05 ms: 1.14x slower                                                           |
| genshi_text     | 21.5 ms                                                         | 25.1 ms: 1.17x slower                                                           |
| django_template | 29.8 ms                                                         | 37.2 ms: 1.25x slower                                                           |
| Geometric mean  | (ref)                                                           | 1.16x slower                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250322-pythonperf1_win32-x86-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| thrift                     | 9.98 ms                                                         | 794 us: 12.56x faster                                                           |
| coverage                   | 324 ms                                                          | 55.9 ms: 5.80x faster                                                           |
| pathlib                    | 82.9 ms                                                         | 38.1 ms: 2.18x faster                                                           |
| asyncio_websockets         | 363 ms                                                          | 201 ms: 1.81x faster                                                            |
| deepcopy                   | 314 us                                                          | 275 us: 1.14x faster                                                            |
| regex_effbot               | 1.80 ms                                                         | 1.59 ms: 1.14x faster                                                           |
| regex_v8                   | 16.8 ms                                                         | 15.0 ms: 1.12x faster                                                           |
| async_tree_memoization_tg  | 282 ms                                                          | 262 ms: 1.08x faster                                                            |
| deepcopy_memo              | 25.4 us                                                         | 23.8 us: 1.07x faster                                                           |
| async_tree_memoization     | 297 ms                                                          | 281 ms: 1.06x faster                                                            |
| deepcopy_reduce            | 2.92 us                                                         | 2.80 us: 1.04x faster                                                           |
| sqlite_synth               | 1.95 us                                                         | 1.90 us: 1.03x faster                                                           |
| async_tree_io              | 526 ms                                                          | 513 ms: 1.02x faster                                                            |
| async_tree_none            | 245 ms                                                          | 241 ms: 1.01x faster                                                            |
| pidigits                   | 201 ms                                                          | 201 ms: 1.00x slower                                                            |
| regex_dna                  | 114 ms                                                          | 115 ms: 1.01x slower                                                            |
| async_tree_io_tg           | 494 ms                                                          | 501 ms: 1.01x slower                                                            |
| python_startup             | 28.3 ms                                                         | 28.7 ms: 1.01x slower                                                           |
| json_loads                 | 21.6 us                                                         | 22.0 us: 1.01x slower                                                           |
| xml_etree_parse            | 107 ms                                                          | 112 ms: 1.04x slower                                                            |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 506 ms: 1.04x slower                                                            |
| pylint                     | 227 ms                                                          | 239 ms: 1.05x slower                                                            |
| gc_traversal               | 1.75 ms                                                         | 1.85 ms: 1.06x slower                                                           |
| bench_mp_pool              | 90.6 ms                                                         | 96.2 ms: 1.06x slower                                                           |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 485 ms: 1.06x slower                                                            |
| json                       | 4.27 ms                                                         | 4.61 ms: 1.08x slower                                                           |
| k_core                     | 1.38 sec                                                        | 1.49 sec: 1.08x slower                                                          |
| float                      | 54.6 ms                                                         | 59.0 ms: 1.08x slower                                                           |
| telco                      | 6.96 ms                                                         | 7.56 ms: 1.09x slower                                                           |
| html5lib                   | 47.5 ms                                                         | 51.8 ms: 1.09x slower                                                           |
| coroutines                 | 16.2 ms                                                         | 17.8 ms: 1.10x slower                                                           |
| genshi_xml                 | 50.1 ms                                                         | 55.4 ms: 1.10x slower                                                           |
| dulwich_log                | 48.8 ms                                                         | 53.9 ms: 1.11x slower                                                           |
| sympy_sum                  | 106 ms                                                          | 117 ms: 1.11x slower                                                            |
| sphinx                     | 719 ms                                                          | 805 ms: 1.12x slower                                                            |
| mdp                        | 1.62 sec                                                        | 1.83 sec: 1.12x slower                                                          |
| scimark_sparse_mat_mult    | 2.84 ms                                                         | 3.19 ms: 1.12x slower                                                           |
| sympy_str                  | 212 ms                                                          | 239 ms: 1.13x slower                                                            |
| sympy_expand               | 373 ms                                                          | 421 ms: 1.13x slower                                                            |
| go                         | 109 ms                                                          | 123 ms: 1.13x slower                                                            |
| mako                       | 7.09 ms                                                         | 8.05 ms: 1.14x slower                                                           |
| xml_etree_iterparse        | 62.6 ms                                                         | 71.2 ms: 1.14x slower                                                           |
| logging_format             | 8.72 us                                                         | 9.92 us: 1.14x slower                                                           |
| sympy_integrate            | 15.0 ms                                                         | 17.1 ms: 1.14x slower                                                           |
| docutils                   | 1.78 sec                                                        | 2.03 sec: 1.14x slower                                                          |
| tomli_loads                | 1.71 sec                                                        | 1.96 sec: 1.14x slower                                                          |
| 2to3                       | 250 ms                                                          | 287 ms: 1.15x slower                                                            |
| shortest_path              | 290 ms                                                          | 334 ms: 1.15x slower                                                            |
| logging_simple             | 7.99 us                                                         | 9.20 us: 1.15x slower                                                           |
| python_startup_no_site     | 19.7 ms                                                         | 22.8 ms: 1.16x slower                                                           |
| connected_components       | 267 ms                                                          | 309 ms: 1.16x slower                                                            |
| genshi_text                | 21.5 ms                                                         | 25.1 ms: 1.17x slower                                                           |
| json_dumps                 | 7.30 ms                                                         | 8.55 ms: 1.17x slower                                                           |
| pycparser                  | 872 ms                                                          | 1.03 sec: 1.18x slower                                                          |
| regex_compile              | 101 ms                                                          | 120 ms: 1.18x slower                                                            |
| spectral_norm              | 69.4 ms                                                         | 82.8 ms: 1.19x slower                                                           |
| bpe_tokeniser              | 3.46 sec                                                        | 4.18 sec: 1.21x slower                                                          |
| pprint_pformat             | 1.33 sec                                                        | 1.61 sec: 1.21x slower                                                          |
| pprint_safe_repr           | 648 ms                                                          | 793 ms: 1.22x slower                                                            |
| scimark_monte_carlo        | 47.7 ms                                                         | 58.8 ms: 1.23x slower                                                           |
| pyflate                    | 320 ms                                                          | 399 ms: 1.25x slower                                                            |
| django_template            | 29.8 ms                                                         | 37.2 ms: 1.25x slower                                                           |
| chaos                      | 50.2 ms                                                         | 63.2 ms: 1.26x slower                                                           |
| async_generators           | 270 ms                                                          | 340 ms: 1.26x slower                                                            |
| scimark_sor                | 85.9 ms                                                         | 108 ms: 1.26x slower                                                            |
| xml_etree_generate         | 61.4 ms                                                         | 78.0 ms: 1.27x slower                                                           |
| richards                   | 32.7 ms                                                         | 41.6 ms: 1.27x slower                                                           |
| richards_super             | 36.7 ms                                                         | 47.1 ms: 1.28x slower                                                           |
| meteor_contest             | 74.6 ms                                                         | 96.1 ms: 1.29x slower                                                           |
| scimark_lu                 | 60.2 ms                                                         | 78.1 ms: 1.30x slower                                                           |
| scimark_fft                | 205 ms                                                          | 268 ms: 1.31x slower                                                            |
| fannkuch                   | 299 ms                                                          | 391 ms: 1.31x slower                                                            |
| raytrace                   | 201 ms                                                          | 266 ms: 1.32x slower                                                            |
| many_optionals             | 436 us                                                          | 576 us: 1.32x slower                                                            |
| xml_etree_process          | 44.2 ms                                                         | 58.9 ms: 1.33x slower                                                           |
| bench_thread_pool          | 1.00 ms                                                         | 1.35 ms: 1.34x slower                                                           |
| typing_runtime_protocols   | 138 us                                                          | 186 us: 1.35x slower                                                            |
| logging_silent             | 60.3 ns                                                         | 82.6 ns: 1.37x slower                                                           |
| generators                 | 21.8 ms                                                         | 30.0 ms: 1.38x slower                                                           |
| deltablue                  | 2.33 ms                                                         | 3.23 ms: 1.39x slower                                                           |
| nqueens                    | 72.1 ms                                                         | 102 ms: 1.42x slower                                                            |
| pickle_pure_python         | 231 us                                                          | 350 us: 1.51x slower                                                            |
| comprehensions             | 12.5 us                                                         | 19.3 us: 1.54x slower                                                           |
| subparsers                 | 14.8 ms                                                         | 22.8 ms: 1.54x slower                                                           |
| crypto_pyaes               | 56.9 ms                                                         | 88.6 ms: 1.56x slower                                                           |
| hexiom                     | 4.44 ms                                                         | 6.92 ms: 1.56x slower                                                           |
| unpickle_pure_python       | 160 us                                                          | 254 us: 1.58x slower                                                            |
| nbody                      | 80.0 ms                                                         | 130 ms: 1.63x slower                                                            |
| Geometric mean             | (ref)                                                           | 1.09x slower                                                                    |

Benchmark hidden because not significant (2): create_gc_cycles, async_tree_none_tg
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250322-3.14.0a6+-bc26f95-JIT/bm-20250322-pythonperf1_win32-x86-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.076x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.12x
- 95% likely to have a slowdown of 1.12x
- 99% likely to have a slowdown of 1.10x

# Memory
- memory change: unknown