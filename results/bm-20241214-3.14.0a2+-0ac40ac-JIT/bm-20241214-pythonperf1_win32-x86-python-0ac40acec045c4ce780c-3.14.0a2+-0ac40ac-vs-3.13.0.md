# Results vs. 3.13.0

- fork: python
- ref: 0ac40acec045c4ce780c
- machine: windows-x86
- commit hash: 0ac40ac
- commit date: 2024-12-14
- overall geometric mean: 1.043x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241214-pythonperf1_win32-x86-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 250 ms                                                          | 260 ms: 1.04x slower                                                            |
| docutils       | 1.78 sec                                                        | 1.92 sec: 1.08x slower                                                          |
| html5lib       | 47.5 ms                                                         | 49.7 ms: 1.05x slower                                                           |
| sphinx         | 719 ms                                                          | 785 ms: 1.09x slower                                                            |
| Geometric mean | (ref)                                                           | 1.06x slower                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241214-pythonperf1_win32-x86-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 282 ms                                                          | 247 ms: 1.14x faster                                                            |
| async_tree_io              | 526 ms                                                          | 483 ms: 1.09x faster                                                            |
| async_tree_none_tg         | 214 ms                                                          | 198 ms: 1.08x faster                                                            |
| async_tree_none            | 245 ms                                                          | 227 ms: 1.08x faster                                                            |
| async_tree_io_tg           | 494 ms                                                          | 460 ms: 1.08x faster                                                            |
| async_tree_memoization     | 297 ms                                                          | 279 ms: 1.06x faster                                                            |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 441 ms: 1.03x faster                                                            |
| asyncio_websockets         | 363 ms                                                          | 352 ms: 1.03x faster                                                            |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 473 ms: 1.02x faster                                                            |
| coroutines                 | 16.2 ms                                                         | 17.2 ms: 1.06x slower                                                           |
| async_generators           | 270 ms                                                          | 307 ms: 1.14x slower                                                            |
| Geometric mean             | (ref)                                                           | 1.04x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241214-pythonperf1_win32-x86-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pidigits       | 201 ms                                                          | 200 ms: 1.00x faster                                                            |
| float          | 54.6 ms                                                         | 56.2 ms: 1.03x slower                                                           |
| nbody          | 80.0 ms                                                         | 104 ms: 1.31x slower                                                            |
| Geometric mean | (ref)                                                           | 1.10x slower                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241214-pythonperf1_win32-x86-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_effbot   | 1.80 ms                                                         | 1.57 ms: 1.15x faster                                                           |
| regex_v8       | 16.8 ms                                                         | 15.4 ms: 1.09x faster                                                           |
| regex_dna      | 114 ms                                                          | 111 ms: 1.02x faster                                                            |
| regex_compile  | 101 ms                                                          | 114 ms: 1.13x slower                                                            |
| Geometric mean | (ref)                                                           | 1.03x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241214-pythonperf1_win32-x86-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| json_loads           | 21.6 us                                                         | 20.6 us: 1.05x faster                                                           |
| tomli_loads          | 1.71 sec                                                        | 1.75 sec: 1.02x slower                                                          |
| xml_etree_iterparse  | 62.6 ms                                                         | 66.4 ms: 1.06x slower                                                           |
| xml_etree_generate   | 61.4 ms                                                         | 71.0 ms: 1.16x slower                                                           |
| xml_etree_process    | 44.2 ms                                                         | 53.0 ms: 1.20x slower                                                           |
| json_dumps           | 7.30 ms                                                         | 9.05 ms: 1.24x slower                                                           |
| pickle_pure_python   | 231 us                                                          | 296 us: 1.28x slower                                                            |
| unpickle_pure_python | 160 us                                                          | 207 us: 1.29x slower                                                            |
| Geometric mean       | (ref)                                                           | 1.13x slower                                                                    |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241214-pythonperf1_win32-x86-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 28.3 ms                                                         | 25.9 ms: 1.09x faster                                                           |
| python_startup_no_site | 19.7 ms                                                         | 19.5 ms: 1.01x faster                                                           |
| Geometric mean         | (ref)                                                           | 1.05x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241214-pythonperf1_win32-x86-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                         | 7.36 ms: 1.04x slower                                                           |
| genshi_xml      | 50.1 ms                                                         | 56.4 ms: 1.12x slower                                                           |
| genshi_text     | 21.5 ms                                                         | 26.4 ms: 1.23x slower                                                           |
| django_template | 29.8 ms                                                         | 37.3 ms: 1.25x slower                                                           |
| Geometric mean  | (ref)                                                           | 1.16x slower                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241214-pythonperf1_win32-x86-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| thrift                     | 9.98 ms                                                         | 777 us: 12.85x faster                                                           |
| coverage                   | 324 ms                                                          | 53.8 ms: 6.02x faster                                                           |
| sqlglot_normalize          | 216 ms                                                          | 106 ms: 2.04x faster                                                            |
| deepcopy                   | 314 us                                                          | 271 us: 1.16x faster                                                            |
| regex_effbot               | 1.80 ms                                                         | 1.57 ms: 1.15x faster                                                           |
| async_tree_memoization_tg  | 282 ms                                                          | 247 ms: 1.14x faster                                                            |
| regex_v8                   | 16.8 ms                                                         | 15.4 ms: 1.09x faster                                                           |
| python_startup             | 28.3 ms                                                         | 25.9 ms: 1.09x faster                                                           |
| async_tree_io              | 526 ms                                                          | 483 ms: 1.09x faster                                                            |
| deepcopy_memo              | 25.4 us                                                         | 23.4 us: 1.09x faster                                                           |
| async_tree_none_tg         | 214 ms                                                          | 198 ms: 1.08x faster                                                            |
| async_tree_none            | 245 ms                                                          | 227 ms: 1.08x faster                                                            |
| async_tree_io_tg           | 494 ms                                                          | 460 ms: 1.08x faster                                                            |
| async_tree_memoization     | 297 ms                                                          | 279 ms: 1.06x faster                                                            |
| json_loads                 | 21.6 us                                                         | 20.6 us: 1.05x faster                                                           |
| deepcopy_reduce            | 2.92 us                                                         | 2.79 us: 1.04x faster                                                           |
| bench_mp_pool              | 90.6 ms                                                         | 87.3 ms: 1.04x faster                                                           |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 441 ms: 1.03x faster                                                            |
| asyncio_websockets         | 363 ms                                                          | 352 ms: 1.03x faster                                                            |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 473 ms: 1.02x faster                                                            |
| regex_dna                  | 114 ms                                                          | 111 ms: 1.02x faster                                                            |
| sqlite_synth               | 1.95 us                                                         | 1.93 us: 1.01x faster                                                           |
| create_gc_cycles           | 1.06 ms                                                         | 1.05 ms: 1.01x faster                                                           |
| python_startup_no_site     | 19.7 ms                                                         | 19.5 ms: 1.01x faster                                                           |
| pidigits                   | 201 ms                                                          | 200 ms: 1.00x faster                                                            |
| tomli_loads                | 1.71 sec                                                        | 1.75 sec: 1.02x slower                                                          |
| k_core                     | 1.38 sec                                                        | 1.41 sec: 1.02x slower                                                          |
| float                      | 54.6 ms                                                         | 56.2 ms: 1.03x slower                                                           |
| gc_traversal               | 1.75 ms                                                         | 1.81 ms: 1.03x slower                                                           |
| bench_thread_pool          | 1.00 ms                                                         | 1.04 ms: 1.03x slower                                                           |
| json                       | 4.27 ms                                                         | 4.44 ms: 1.04x slower                                                           |
| 2to3                       | 250 ms                                                          | 260 ms: 1.04x slower                                                            |
| mako                       | 7.09 ms                                                         | 7.36 ms: 1.04x slower                                                           |
| telco                      | 6.96 ms                                                         | 7.24 ms: 1.04x slower                                                           |
| logging_format             | 8.72 us                                                         | 9.07 us: 1.04x slower                                                           |
| dulwich_log                | 48.8 ms                                                         | 50.8 ms: 1.04x slower                                                           |
| html5lib                   | 47.5 ms                                                         | 49.7 ms: 1.05x slower                                                           |
| pycparser                  | 872 ms                                                          | 912 ms: 1.05x slower                                                            |
| logging_simple             | 7.99 us                                                         | 8.40 us: 1.05x slower                                                           |
| coroutines                 | 16.2 ms                                                         | 17.2 ms: 1.06x slower                                                           |
| xml_etree_iterparse        | 62.6 ms                                                         | 66.4 ms: 1.06x slower                                                           |
| docutils                   | 1.78 sec                                                        | 1.92 sec: 1.08x slower                                                          |
| sympy_expand               | 373 ms                                                          | 404 ms: 1.08x slower                                                            |
| sympy_sum                  | 106 ms                                                          | 114 ms: 1.08x slower                                                            |
| connected_components       | 267 ms                                                          | 289 ms: 1.08x slower                                                            |
| spectral_norm              | 69.4 ms                                                         | 75.4 ms: 1.09x slower                                                           |
| sphinx                     | 719 ms                                                          | 785 ms: 1.09x slower                                                            |
| sympy_str                  | 212 ms                                                          | 233 ms: 1.10x slower                                                            |
| shortest_path              | 290 ms                                                          | 320 ms: 1.10x slower                                                            |
| go                         | 109 ms                                                          | 121 ms: 1.11x slower                                                            |
| bpe_tokeniser              | 3.46 sec                                                        | 3.87 sec: 1.12x slower                                                          |
| genshi_xml                 | 50.1 ms                                                         | 56.4 ms: 1.12x slower                                                           |
| scimark_sor                | 85.9 ms                                                         | 96.6 ms: 1.12x slower                                                           |
| regex_compile              | 101 ms                                                          | 114 ms: 1.13x slower                                                            |
| fannkuch                   | 299 ms                                                          | 338 ms: 1.13x slower                                                            |
| mdp                        | 1.62 sec                                                        | 1.84 sec: 1.13x slower                                                          |
| scimark_sparse_mat_mult    | 2.84 ms                                                         | 3.22 ms: 1.13x slower                                                           |
| async_generators           | 270 ms                                                          | 307 ms: 1.14x slower                                                            |
| pprint_pformat             | 1.33 sec                                                        | 1.51 sec: 1.14x slower                                                          |
| pprint_safe_repr           | 648 ms                                                          | 740 ms: 1.14x slower                                                            |
| sqlglot_parse              | 1.00 ms                                                         | 1.15 ms: 1.15x slower                                                           |
| sqlglot_transpile          | 1.24 ms                                                         | 1.43 ms: 1.15x slower                                                           |
| xml_etree_generate         | 61.4 ms                                                         | 71.0 ms: 1.16x slower                                                           |
| sympy_integrate            | 15.0 ms                                                         | 17.4 ms: 1.16x slower                                                           |
| typing_runtime_protocols   | 138 us                                                          | 160 us: 1.16x slower                                                            |
| crypto_pyaes               | 56.9 ms                                                         | 67.6 ms: 1.19x slower                                                           |
| scimark_fft                | 205 ms                                                          | 244 ms: 1.19x slower                                                            |
| meteor_contest             | 74.6 ms                                                         | 89.3 ms: 1.20x slower                                                           |
| xml_etree_process          | 44.2 ms                                                         | 53.0 ms: 1.20x slower                                                           |
| pyflate                    | 320 ms                                                          | 384 ms: 1.20x slower                                                            |
| genshi_text                | 21.5 ms                                                         | 26.4 ms: 1.23x slower                                                           |
| sqlglot_optimize           | 41.4 ms                                                         | 51.0 ms: 1.23x slower                                                           |
| json_dumps                 | 7.30 ms                                                         | 9.05 ms: 1.24x slower                                                           |
| django_template            | 29.8 ms                                                         | 37.3 ms: 1.25x slower                                                           |
| chaos                      | 50.2 ms                                                         | 63.6 ms: 1.27x slower                                                           |
| pickle_pure_python         | 231 us                                                          | 296 us: 1.28x slower                                                            |
| many_optionals             | 436 us                                                          | 558 us: 1.28x slower                                                            |
| richards                   | 32.7 ms                                                         | 42.0 ms: 1.29x slower                                                           |
| unpickle_pure_python       | 160 us                                                          | 207 us: 1.29x slower                                                            |
| richards_super             | 36.7 ms                                                         | 47.6 ms: 1.30x slower                                                           |
| logging_silent             | 60.3 ns                                                         | 78.4 ns: 1.30x slower                                                           |
| nbody                      | 80.0 ms                                                         | 104 ms: 1.31x slower                                                            |
| scimark_lu                 | 60.2 ms                                                         | 78.8 ms: 1.31x slower                                                           |
| scimark_monte_carlo        | 47.7 ms                                                         | 64.1 ms: 1.34x slower                                                           |
| nqueens                    | 72.1 ms                                                         | 97.4 ms: 1.35x slower                                                           |
| deltablue                  | 2.33 ms                                                         | 3.16 ms: 1.36x slower                                                           |
| subparsers                 | 14.8 ms                                                         | 21.3 ms: 1.45x slower                                                           |
| comprehensions             | 12.5 us                                                         | 18.3 us: 1.47x slower                                                           |
| raytrace                   | 201 ms                                                          | 297 ms: 1.48x slower                                                            |
| hexiom                     | 4.44 ms                                                         | 7.14 ms: 1.61x slower                                                           |
| generators                 | 21.8 ms                                                         | 36.1 ms: 1.66x slower                                                           |
| Geometric mean             | (ref)                                                           | 1.04x slower                                                                    |

Benchmark hidden because not significant (3): pathlib, xml_etree_parse, pylint
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (1) of results/bm-20241214-3.14.0a2+-0ac40ac-JIT/bm-20241214-pythonperf1_win32-x86-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac.json: mypy2

- Geometric mean (including insignificant results): 1.043x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.06x
- 95% likely to have a slowdown of 1.05x
- 99% likely to have a slowdown of 1.04x

# Memory
- memory change: unknown