# Results vs. 3.13.0

- fork: nascheme
- ref: pgo_benchmark_task
- machine: windows-x86
- commit hash: 8dd8862
- commit date: 2025-02-28
- overall geometric mean: 1.014x faster
- HPT reliability: 99.88%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250228-pythonperf1_win32-x86-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 250 ms                                                          | 257 ms: 1.03x slower                                                            |
| docutils       | 1.78 sec                                                        | 1.84 sec: 1.04x slower                                                          |
| html5lib       | 47.5 ms                                                         | 48.8 ms: 1.03x slower                                                           |
| sphinx         | 719 ms                                                          | 743 ms: 1.03x slower                                                            |
| Geometric mean | (ref)                                                           | 1.03x slower                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250228-pythonperf1_win32-x86-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 282 ms                                                          | 246 ms: 1.15x faster                                                            |
| async_tree_io              | 526 ms                                                          | 460 ms: 1.14x faster                                                            |
| async_tree_memoization     | 297 ms                                                          | 262 ms: 1.13x faster                                                            |
| async_tree_none            | 245 ms                                                          | 220 ms: 1.11x faster                                                            |
| async_tree_io_tg           | 494 ms                                                          | 454 ms: 1.09x faster                                                            |
| async_tree_none_tg         | 214 ms                                                          | 198 ms: 1.08x faster                                                            |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 438 ms: 1.04x faster                                                            |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 469 ms: 1.03x faster                                                            |
| asyncio_websockets         | 363 ms                                                          | 352 ms: 1.03x faster                                                            |
| coroutines                 | 16.2 ms                                                         | 16.7 ms: 1.03x slower                                                           |
| async_generators           | 270 ms                                                          | 290 ms: 1.08x slower                                                            |
| Geometric mean             | (ref)                                                           | 1.06x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250228-pythonperf1_win32-x86-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pidigits       | 201 ms                                                          | 200 ms: 1.01x faster                                                            |
| nbody          | 80.0 ms                                                         | 87.3 ms: 1.09x slower                                                           |
| Geometric mean | (ref)                                                           | 1.03x slower                                                                    |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250228-pythonperf1_win32-x86-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_effbot   | 1.80 ms                                                         | 1.54 ms: 1.17x faster                                                           |
| regex_dna      | 114 ms                                                          | 115 ms: 1.01x slower                                                            |
| regex_compile  | 101 ms                                                          | 108 ms: 1.07x slower                                                            |
| Geometric mean | (ref)                                                           | 1.04x faster                                                                    |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250228-pythonperf1_win32-x86-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862 |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 1.71 sec                                                        | 1.73 sec: 1.01x slower                                                          |
| xml_etree_iterparse  | 62.6 ms                                                         | 65.9 ms: 1.05x slower                                                           |
| json_dumps           | 7.30 ms                                                         | 7.90 ms: 1.08x slower                                                           |
| xml_etree_generate   | 61.4 ms                                                         | 67.7 ms: 1.10x slower                                                           |
| xml_etree_process    | 44.2 ms                                                         | 49.3 ms: 1.12x slower                                                           |
| unpickle_pure_python | 160 us                                                          | 182 us: 1.14x slower                                                            |
| pickle_pure_python   | 231 us                                                          | 287 us: 1.24x slower                                                            |
| Geometric mean       | (ref)                                                           | 1.08x slower                                                                    |

Benchmark hidden because not significant (2): xml_etree_parse, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250228-pythonperf1_win32-x86-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862 |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 28.3 ms                                                         | 28.5 ms: 1.01x slower                                                           |
| python_startup_no_site | 19.7 ms                                                         | 22.0 ms: 1.12x slower                                                           |
| Geometric mean         | (ref)                                                           | 1.06x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250228-pythonperf1_win32-x86-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862 |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_xml      | 50.1 ms                                                         | 47.8 ms: 1.05x faster                                                           |
| genshi_text     | 21.5 ms                                                         | 22.2 ms: 1.03x slower                                                           |
| mako            | 7.09 ms                                                         | 7.82 ms: 1.10x slower                                                           |
| django_template | 29.8 ms                                                         | 34.1 ms: 1.14x slower                                                           |
| Geometric mean  | (ref)                                                           | 1.06x slower                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250228-pythonperf1_win32-x86-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| thrift                     | 9.98 ms                                                         | 757 us: 13.18x faster                                                           |
| coverage                   | 324 ms                                                          | 51.6 ms: 6.27x faster                                                           |
| pathlib                    | 82.9 ms                                                         | 36.8 ms: 2.25x faster                                                           |
| deepcopy                   | 314 us                                                          | 242 us: 1.30x faster                                                            |
| regex_effbot               | 1.80 ms                                                         | 1.54 ms: 1.17x faster                                                           |
| async_tree_memoization_tg  | 282 ms                                                          | 246 ms: 1.15x faster                                                            |
| async_tree_io              | 526 ms                                                          | 460 ms: 1.14x faster                                                            |
| deepcopy_reduce            | 2.92 us                                                         | 2.56 us: 1.14x faster                                                           |
| telco                      | 6.96 ms                                                         | 6.15 ms: 1.13x faster                                                           |
| async_tree_memoization     | 297 ms                                                          | 262 ms: 1.13x faster                                                            |
| deepcopy_memo              | 25.4 us                                                         | 22.5 us: 1.13x faster                                                           |
| async_tree_none            | 245 ms                                                          | 220 ms: 1.11x faster                                                            |
| async_tree_io_tg           | 494 ms                                                          | 454 ms: 1.09x faster                                                            |
| async_tree_none_tg         | 214 ms                                                          | 198 ms: 1.08x faster                                                            |
| genshi_xml                 | 50.1 ms                                                         | 47.8 ms: 1.05x faster                                                           |
| pprint_safe_repr           | 648 ms                                                          | 619 ms: 1.05x faster                                                            |
| sqlite_synth               | 1.95 us                                                         | 1.87 us: 1.04x faster                                                           |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 438 ms: 1.04x faster                                                            |
| pprint_pformat             | 1.33 sec                                                        | 1.28 sec: 1.04x faster                                                          |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 469 ms: 1.03x faster                                                            |
| asyncio_websockets         | 363 ms                                                          | 352 ms: 1.03x faster                                                            |
| create_gc_cycles           | 1.06 ms                                                         | 1.04 ms: 1.02x faster                                                           |
| go                         | 109 ms                                                          | 107 ms: 1.02x faster                                                            |
| pidigits                   | 201 ms                                                          | 200 ms: 1.01x faster                                                            |
| bpe_tokeniser              | 3.46 sec                                                        | 3.48 sec: 1.01x slower                                                          |
| python_startup             | 28.3 ms                                                         | 28.5 ms: 1.01x slower                                                           |
| regex_dna                  | 114 ms                                                          | 115 ms: 1.01x slower                                                            |
| tomli_loads                | 1.71 sec                                                        | 1.73 sec: 1.01x slower                                                          |
| bench_mp_pool              | 90.6 ms                                                         | 91.6 ms: 1.01x slower                                                           |
| gc_traversal               | 1.75 ms                                                         | 1.78 ms: 1.02x slower                                                           |
| pycparser                  | 872 ms                                                          | 894 ms: 1.03x slower                                                            |
| 2to3                       | 250 ms                                                          | 257 ms: 1.03x slower                                                            |
| sqlglot_normalize          | 216 ms                                                          | 222 ms: 1.03x slower                                                            |
| fannkuch                   | 299 ms                                                          | 307 ms: 1.03x slower                                                            |
| html5lib                   | 47.5 ms                                                         | 48.8 ms: 1.03x slower                                                           |
| sympy_expand               | 373 ms                                                          | 384 ms: 1.03x slower                                                            |
| coroutines                 | 16.2 ms                                                         | 16.7 ms: 1.03x slower                                                           |
| sphinx                     | 719 ms                                                          | 743 ms: 1.03x slower                                                            |
| sympy_sum                  | 106 ms                                                          | 109 ms: 1.03x slower                                                            |
| genshi_text                | 21.5 ms                                                         | 22.2 ms: 1.03x slower                                                           |
| docutils                   | 1.78 sec                                                        | 1.84 sec: 1.04x slower                                                          |
| spectral_norm              | 69.4 ms                                                         | 72.3 ms: 1.04x slower                                                           |
| sqlglot_optimize           | 41.4 ms                                                         | 43.2 ms: 1.04x slower                                                           |
| shortest_path              | 290 ms                                                          | 302 ms: 1.04x slower                                                            |
| json                       | 4.27 ms                                                         | 4.47 ms: 1.05x slower                                                           |
| sympy_str                  | 212 ms                                                          | 222 ms: 1.05x slower                                                            |
| xml_etree_iterparse        | 62.6 ms                                                         | 65.9 ms: 1.05x slower                                                           |
| regex_compile              | 101 ms                                                          | 108 ms: 1.07x slower                                                            |
| sympy_integrate            | 15.0 ms                                                         | 16.0 ms: 1.07x slower                                                           |
| logging_format             | 8.72 us                                                         | 9.37 us: 1.07x slower                                                           |
| typing_runtime_protocols   | 138 us                                                          | 148 us: 1.08x slower                                                            |
| async_generators           | 270 ms                                                          | 290 ms: 1.08x slower                                                            |
| comprehensions             | 12.5 us                                                         | 13.5 us: 1.08x slower                                                           |
| json_dumps                 | 7.30 ms                                                         | 7.90 ms: 1.08x slower                                                           |
| logging_simple             | 7.99 us                                                         | 8.67 us: 1.09x slower                                                           |
| dulwich_log                | 48.8 ms                                                         | 53.1 ms: 1.09x slower                                                           |
| nbody                      | 80.0 ms                                                         | 87.3 ms: 1.09x slower                                                           |
| meteor_contest             | 74.6 ms                                                         | 81.5 ms: 1.09x slower                                                           |
| pyflate                    | 320 ms                                                          | 351 ms: 1.10x slower                                                            |
| sqlglot_transpile          | 1.24 ms                                                         | 1.36 ms: 1.10x slower                                                           |
| xml_etree_generate         | 61.4 ms                                                         | 67.7 ms: 1.10x slower                                                           |
| mdp                        | 1.62 sec                                                        | 1.79 sec: 1.10x slower                                                          |
| mako                       | 7.09 ms                                                         | 7.82 ms: 1.10x slower                                                           |
| scimark_sparse_mat_mult    | 2.84 ms                                                         | 3.14 ms: 1.10x slower                                                           |
| xml_etree_process          | 44.2 ms                                                         | 49.3 ms: 1.12x slower                                                           |
| sqlglot_parse              | 1.00 ms                                                         | 1.12 ms: 1.12x slower                                                           |
| python_startup_no_site     | 19.7 ms                                                         | 22.0 ms: 1.12x slower                                                           |
| nqueens                    | 72.1 ms                                                         | 80.7 ms: 1.12x slower                                                           |
| crypto_pyaes               | 56.9 ms                                                         | 64.7 ms: 1.14x slower                                                           |
| unpickle_pure_python       | 160 us                                                          | 182 us: 1.14x slower                                                            |
| django_template            | 29.8 ms                                                         | 34.1 ms: 1.14x slower                                                           |
| scimark_fft                | 205 ms                                                          | 236 ms: 1.15x slower                                                            |
| scimark_sor                | 85.9 ms                                                         | 99.0 ms: 1.15x slower                                                           |
| chaos                      | 50.2 ms                                                         | 58.6 ms: 1.17x slower                                                           |
| hexiom                     | 4.44 ms                                                         | 5.18 ms: 1.17x slower                                                           |
| scimark_monte_carlo        | 47.7 ms                                                         | 55.9 ms: 1.17x slower                                                           |
| scimark_lu                 | 60.2 ms                                                         | 70.8 ms: 1.18x slower                                                           |
| logging_silent             | 60.3 ns                                                         | 71.7 ns: 1.19x slower                                                           |
| deltablue                  | 2.33 ms                                                         | 2.78 ms: 1.19x slower                                                           |
| richards                   | 32.7 ms                                                         | 39.1 ms: 1.20x slower                                                           |
| generators                 | 21.8 ms                                                         | 26.9 ms: 1.24x slower                                                           |
| many_optionals             | 436 us                                                          | 540 us: 1.24x slower                                                            |
| richards_super             | 36.7 ms                                                         | 45.5 ms: 1.24x slower                                                           |
| pickle_pure_python         | 231 us                                                          | 287 us: 1.24x slower                                                            |
| raytrace                   | 201 ms                                                          | 265 ms: 1.31x slower                                                            |
| bench_thread_pool          | 1.00 ms                                                         | 1.35 ms: 1.35x slower                                                           |
| subparsers                 | 14.8 ms                                                         | 21.6 ms: 1.46x slower                                                           |
| Geometric mean             | (ref)                                                           | 1.01x faster                                                                    |

Benchmark hidden because not significant (7): regex_v8, pylint, xml_etree_parse, json_loads, float, k_core, connected_components
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http

- Geometric mean (including insignificant results): 1.014x faster

# HPT report

- Reliability score: 99.88% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown