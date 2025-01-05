# Results vs. 3.13.0

- fork: python
- ref: 0cafa97932c6574734bb
- machine: windows-x86
- commit hash: 0cafa97
- commit date: 2025-01-04
- overall geometric mean: 1.042x faster
- HPT reliability: 56.79%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250104-pythonperf1_win32-x86-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 250 ms                                                          | 246 ms: 1.02x faster                                                            |
| docutils       | 1.78 sec                                                        | 1.80 sec: 1.01x slower                                                          |
| html5lib       | 47.5 ms                                                         | 43.8 ms: 1.08x faster                                                           |
| sphinx         | 719 ms                                                          | 730 ms: 1.02x slower                                                            |
| Geometric mean | (ref)                                                           | 1.02x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250104-pythonperf1_win32-x86-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 282 ms                                                          | 221 ms: 1.27x faster                                                            |
| async_tree_none            | 245 ms                                                          | 194 ms: 1.26x faster                                                            |
| async_tree_io              | 526 ms                                                          | 428 ms: 1.23x faster                                                            |
| async_tree_none_tg         | 214 ms                                                          | 176 ms: 1.22x faster                                                            |
| async_tree_memoization     | 297 ms                                                          | 244 ms: 1.21x faster                                                            |
| async_tree_io_tg           | 494 ms                                                          | 408 ms: 1.21x faster                                                            |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 432 ms: 1.12x faster                                                            |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 423 ms: 1.08x faster                                                            |
| asyncio_websockets         | 363 ms                                                          | 366 ms: 1.01x slower                                                            |
| async_generators           | 270 ms                                                          | 304 ms: 1.13x slower                                                            |
| Geometric mean             | (ref)                                                           | 1.13x faster                                                                    |

Benchmark hidden because not significant (1): coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250104-pythonperf1_win32-x86-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pidigits       | 201 ms                                                          | 200 ms: 1.00x faster                                                            |
| float          | 54.6 ms                                                         | 56.5 ms: 1.03x slower                                                           |
| nbody          | 80.0 ms                                                         | 85.5 ms: 1.07x slower                                                           |
| Geometric mean | (ref)                                                           | 1.03x slower                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250104-pythonperf1_win32-x86-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_v8       | 16.8 ms                                                         | 15.5 ms: 1.08x faster                                                           |
| regex_effbot   | 1.80 ms                                                         | 1.66 ms: 1.08x faster                                                           |
| regex_compile  | 101 ms                                                          | 102 ms: 1.01x slower                                                            |
| regex_dna      | 114 ms                                                          | 123 ms: 1.08x slower                                                            |
| Geometric mean | (ref)                                                           | 1.02x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250104-pythonperf1_win32-x86-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 1.71 sec                                                        | 1.61 sec: 1.06x faster                                                          |
| json_loads           | 21.6 us                                                         | 20.9 us: 1.03x faster                                                           |
| xml_etree_parse      | 107 ms                                                          | 107 ms: 1.01x faster                                                            |
| xml_etree_iterparse  | 62.6 ms                                                         | 66.2 ms: 1.06x slower                                                           |
| unpickle_pure_python | 160 us                                                          | 171 us: 1.07x slower                                                            |
| xml_etree_generate   | 61.4 ms                                                         | 66.7 ms: 1.09x slower                                                           |
| xml_etree_process    | 44.2 ms                                                         | 48.7 ms: 1.10x slower                                                           |
| pickle_pure_python   | 231 us                                                          | 259 us: 1.12x slower                                                            |
| json_dumps           | 7.30 ms                                                         | 8.78 ms: 1.20x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.06x slower                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250104-pythonperf1_win32-x86-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 28.3 ms                                                         | 26.3 ms: 1.08x faster                                                           |
| python_startup_no_site | 19.7 ms                                                         | 20.0 ms: 1.02x slower                                                           |
| Geometric mean         | (ref)                                                           | 1.03x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250104-pythonperf1_win32-x86-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_xml      | 50.1 ms                                                         | 44.6 ms: 1.12x faster                                                           |
| genshi_text     | 21.5 ms                                                         | 20.6 ms: 1.04x faster                                                           |
| django_template | 29.8 ms                                                         | 31.9 ms: 1.07x slower                                                           |
| mako            | 7.09 ms                                                         | 7.69 ms: 1.09x slower                                                           |
| Geometric mean  | (ref)                                                           | 1.00x faster                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250104-pythonperf1_win32-x86-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| thrift                     | 9.98 ms                                                         | 737 us: 13.53x faster                                                           |
| coverage                   | 324 ms                                                          | 52.0 ms: 6.23x faster                                                           |
| deepcopy                   | 314 us                                                          | 240 us: 1.31x faster                                                            |
| async_tree_memoization_tg  | 282 ms                                                          | 221 ms: 1.27x faster                                                            |
| async_tree_none            | 245 ms                                                          | 194 ms: 1.26x faster                                                            |
| async_tree_io              | 526 ms                                                          | 428 ms: 1.23x faster                                                            |
| async_tree_none_tg         | 214 ms                                                          | 176 ms: 1.22x faster                                                            |
| async_tree_memoization     | 297 ms                                                          | 244 ms: 1.21x faster                                                            |
| async_tree_io_tg           | 494 ms                                                          | 408 ms: 1.21x faster                                                            |
| deepcopy_reduce            | 2.92 us                                                         | 2.54 us: 1.15x faster                                                           |
| genshi_xml                 | 50.1 ms                                                         | 44.6 ms: 1.12x faster                                                           |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 432 ms: 1.12x faster                                                            |
| go                         | 109 ms                                                          | 97.2 ms: 1.12x faster                                                           |
| deepcopy_memo              | 25.4 us                                                         | 23.1 us: 1.10x faster                                                           |
| html5lib                   | 47.5 ms                                                         | 43.8 ms: 1.08x faster                                                           |
| regex_v8                   | 16.8 ms                                                         | 15.5 ms: 1.08x faster                                                           |
| regex_effbot               | 1.80 ms                                                         | 1.66 ms: 1.08x faster                                                           |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 423 ms: 1.08x faster                                                            |
| python_startup             | 28.3 ms                                                         | 26.3 ms: 1.08x faster                                                           |
| pylint                     | 227 ms                                                          | 212 ms: 1.07x faster                                                            |
| tomli_loads                | 1.71 sec                                                        | 1.61 sec: 1.06x faster                                                          |
| pycparser                  | 872 ms                                                          | 825 ms: 1.06x faster                                                            |
| genshi_text                | 21.5 ms                                                         | 20.6 ms: 1.04x faster                                                           |
| connected_components       | 267 ms                                                          | 257 ms: 1.04x faster                                                            |
| pprint_pformat             | 1.33 sec                                                        | 1.28 sec: 1.04x faster                                                          |
| logging_format             | 8.72 us                                                         | 8.43 us: 1.03x faster                                                           |
| pprint_safe_repr           | 648 ms                                                          | 627 ms: 1.03x faster                                                            |
| json_loads                 | 21.6 us                                                         | 20.9 us: 1.03x faster                                                           |
| k_core                     | 1.38 sec                                                        | 1.33 sec: 1.03x faster                                                          |
| logging_simple             | 7.99 us                                                         | 7.75 us: 1.03x faster                                                           |
| sqlite_synth               | 1.95 us                                                         | 1.91 us: 1.02x faster                                                           |
| telco                      | 6.96 ms                                                         | 6.81 ms: 1.02x faster                                                           |
| 2to3                       | 250 ms                                                          | 246 ms: 1.02x faster                                                            |
| shortest_path              | 290 ms                                                          | 286 ms: 1.01x faster                                                            |
| bpe_tokeniser              | 3.46 sec                                                        | 3.43 sec: 1.01x faster                                                          |
| fannkuch                   | 299 ms                                                          | 296 ms: 1.01x faster                                                            |
| xml_etree_parse            | 107 ms                                                          | 107 ms: 1.01x faster                                                            |
| sympy_sum                  | 106 ms                                                          | 105 ms: 1.00x faster                                                            |
| pidigits                   | 201 ms                                                          | 200 ms: 1.00x faster                                                            |
| asyncio_websockets         | 363 ms                                                          | 366 ms: 1.01x slower                                                            |
| regex_compile              | 101 ms                                                          | 102 ms: 1.01x slower                                                            |
| sympy_expand               | 373 ms                                                          | 377 ms: 1.01x slower                                                            |
| pathlib                    | 82.9 ms                                                         | 83.6 ms: 1.01x slower                                                           |
| sympy_str                  | 212 ms                                                          | 214 ms: 1.01x slower                                                            |
| docutils                   | 1.78 sec                                                        | 1.80 sec: 1.01x slower                                                          |
| json                       | 4.27 ms                                                         | 4.33 ms: 1.01x slower                                                           |
| sphinx                     | 719 ms                                                          | 730 ms: 1.02x slower                                                            |
| python_startup_no_site     | 19.7 ms                                                         | 20.0 ms: 1.02x slower                                                           |
| gc_traversal               | 1.75 ms                                                         | 1.78 ms: 1.02x slower                                                           |
| dulwich_log                | 48.8 ms                                                         | 49.7 ms: 1.02x slower                                                           |
| sqlglot_parse              | 1.00 ms                                                         | 1.02 ms: 1.02x slower                                                           |
| sqlglot_transpile          | 1.24 ms                                                         | 1.26 ms: 1.02x slower                                                           |
| bench_mp_pool              | 90.6 ms                                                         | 93.0 ms: 1.03x slower                                                           |
| typing_runtime_protocols   | 138 us                                                          | 141 us: 1.03x slower                                                            |
| sympy_integrate            | 15.0 ms                                                         | 15.4 ms: 1.03x slower                                                           |
| scimark_sparse_mat_mult    | 2.84 ms                                                         | 2.92 ms: 1.03x slower                                                           |
| spectral_norm              | 69.4 ms                                                         | 71.6 ms: 1.03x slower                                                           |
| float                      | 54.6 ms                                                         | 56.5 ms: 1.03x slower                                                           |
| pyflate                    | 320 ms                                                          | 336 ms: 1.05x slower                                                            |
| mdp                        | 1.62 sec                                                        | 1.71 sec: 1.05x slower                                                          |
| nqueens                    | 72.1 ms                                                         | 76.1 ms: 1.06x slower                                                           |
| xml_etree_iterparse        | 62.6 ms                                                         | 66.2 ms: 1.06x slower                                                           |
| nbody                      | 80.0 ms                                                         | 85.5 ms: 1.07x slower                                                           |
| unpickle_pure_python       | 160 us                                                          | 171 us: 1.07x slower                                                            |
| django_template            | 29.8 ms                                                         | 31.9 ms: 1.07x slower                                                           |
| chaos                      | 50.2 ms                                                         | 54.4 ms: 1.08x slower                                                           |
| regex_dna                  | 114 ms                                                          | 123 ms: 1.08x slower                                                            |
| mako                       | 7.09 ms                                                         | 7.69 ms: 1.09x slower                                                           |
| xml_etree_generate         | 61.4 ms                                                         | 66.7 ms: 1.09x slower                                                           |
| meteor_contest             | 74.6 ms                                                         | 81.1 ms: 1.09x slower                                                           |
| crypto_pyaes               | 56.9 ms                                                         | 62.1 ms: 1.09x slower                                                           |
| comprehensions             | 12.5 us                                                         | 13.7 us: 1.09x slower                                                           |
| xml_etree_process          | 44.2 ms                                                         | 48.7 ms: 1.10x slower                                                           |
| scimark_fft                | 205 ms                                                          | 225 ms: 1.10x slower                                                            |
| scimark_monte_carlo        | 47.7 ms                                                         | 52.7 ms: 1.11x slower                                                           |
| deltablue                  | 2.33 ms                                                         | 2.59 ms: 1.11x slower                                                           |
| pickle_pure_python         | 231 us                                                          | 259 us: 1.12x slower                                                            |
| async_generators           | 270 ms                                                          | 304 ms: 1.13x slower                                                            |
| richards                   | 32.7 ms                                                         | 36.9 ms: 1.13x slower                                                           |
| scimark_lu                 | 60.2 ms                                                         | 68.2 ms: 1.13x slower                                                           |
| generators                 | 21.8 ms                                                         | 24.7 ms: 1.14x slower                                                           |
| hexiom                     | 4.44 ms                                                         | 5.07 ms: 1.14x slower                                                           |
| richards_super             | 36.7 ms                                                         | 41.9 ms: 1.14x slower                                                           |
| scimark_sor                | 85.9 ms                                                         | 98.2 ms: 1.14x slower                                                           |
| many_optionals             | 436 us                                                          | 505 us: 1.16x slower                                                            |
| logging_silent             | 60.3 ns                                                         | 70.9 ns: 1.17x slower                                                           |
| json_dumps                 | 7.30 ms                                                         | 8.78 ms: 1.20x slower                                                           |
| raytrace                   | 201 ms                                                          | 243 ms: 1.20x slower                                                            |
| subparsers                 | 14.8 ms                                                         | 20.3 ms: 1.37x slower                                                           |
| Geometric mean             | (ref)                                                           | 1.04x faster                                                                    |

Benchmark hidden because not significant (5): coroutines, create_gc_cycles, sqlglot_normalize, sqlglot_optimize, bench_thread_pool
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (1) of results/bm-20250104-3.14.0a3+-0cafa97/bm-20250104-pythonperf1_win32-x86-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97.json: mypy2

- Geometric mean (including insignificant results): 1.042x faster

# HPT report

- Reliability score: 56.79% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown