# Results vs. 3.13.0

- fork: python
- ref: 5cdd6e5e758a3fc0a5da
- machine: windows-x86
- commit hash: 5cdd6e5
- commit date: 2025-02-12
- overall geometric mean: 1.028x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250212-pythonperf1_win32-x86-python-5cdd6e5e758a3fc0a5da-3.14.0a4+-5cdd6e5 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 250 ms                                                          | 268 ms: 1.07x slower                                                            |
| docutils       | 1.78 sec                                                        | 2.01 sec: 1.13x slower                                                          |
| sphinx         | 719 ms                                                          | 770 ms: 1.07x slower                                                            |
| Geometric mean | (ref)                                                           | 1.07x slower                                                                    |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250212-pythonperf1_win32-x86-python-5cdd6e5e758a3fc0a5da-3.14.0a4+-5cdd6e5 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_io              | 526 ms                                                          | 483 ms: 1.09x faster                                                            |
| async_tree_memoization_tg  | 282 ms                                                          | 266 ms: 1.06x faster                                                            |
| async_tree_none            | 245 ms                                                          | 231 ms: 1.06x faster                                                            |
| async_tree_memoization     | 297 ms                                                          | 281 ms: 1.06x faster                                                            |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 467 ms: 1.04x faster                                                            |
| async_tree_io_tg           | 494 ms                                                          | 477 ms: 1.04x faster                                                            |
| coroutines                 | 16.2 ms                                                         | 15.7 ms: 1.03x faster                                                           |
| asyncio_websockets         | 363 ms                                                          | 352 ms: 1.03x faster                                                            |
| async_tree_none_tg         | 214 ms                                                          | 209 ms: 1.03x faster                                                            |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 451 ms: 1.01x faster                                                            |
| async_generators           | 270 ms                                                          | 322 ms: 1.19x slower                                                            |
| Geometric mean             | (ref)                                                           | 1.02x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250212-pythonperf1_win32-x86-python-5cdd6e5e758a3fc0a5da-3.14.0a4+-5cdd6e5 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 54.6 ms                                                         | 53.6 ms: 1.02x faster                                                           |
| pidigits       | 201 ms                                                          | 200 ms: 1.01x faster                                                            |
| nbody          | 80.0 ms                                                         | 113 ms: 1.41x slower                                                            |
| Geometric mean | (ref)                                                           | 1.11x slower                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250212-pythonperf1_win32-x86-python-5cdd6e5e758a3fc0a5da-3.14.0a4+-5cdd6e5 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_effbot   | 1.80 ms                                                         | 1.52 ms: 1.18x faster                                                           |
| regex_v8       | 16.8 ms                                                         | 15.6 ms: 1.08x faster                                                           |
| regex_dna      | 114 ms                                                          | 118 ms: 1.04x slower                                                            |
| regex_compile  | 101 ms                                                          | 118 ms: 1.17x slower                                                            |
| Geometric mean | (ref)                                                           | 1.01x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250212-pythonperf1_win32-x86-python-5cdd6e5e758a3fc0a5da-3.14.0a4+-5cdd6e5 |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| xml_etree_parse      | 107 ms                                                          | 109 ms: 1.01x slower                                                            |
| tomli_loads          | 1.71 sec                                                        | 1.81 sec: 1.05x slower                                                          |
| json_loads           | 21.6 us                                                         | 23.1 us: 1.07x slower                                                           |
| xml_etree_iterparse  | 62.6 ms                                                         | 68.1 ms: 1.09x slower                                                           |
| xml_etree_generate   | 61.4 ms                                                         | 74.9 ms: 1.22x slower                                                           |
| json_dumps           | 7.30 ms                                                         | 9.02 ms: 1.24x slower                                                           |
| xml_etree_process    | 44.2 ms                                                         | 55.7 ms: 1.26x slower                                                           |
| pickle_pure_python   | 231 us                                                          | 319 us: 1.38x slower                                                            |
| unpickle_pure_python | 160 us                                                          | 226 us: 1.41x slower                                                            |
| Geometric mean       | (ref)                                                           | 1.18x slower                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250212-pythonperf1_win32-x86-python-5cdd6e5e758a3fc0a5da-3.14.0a4+-5cdd6e5 |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 19.7 ms                                                         | 21.7 ms: 1.10x slower                                                           |
| Geometric mean         | (ref)                                                           | 1.05x slower                                                                    |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250212-pythonperf1_win32-x86-python-5cdd6e5e758a3fc0a5da-3.14.0a4+-5cdd6e5 |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_xml      | 50.1 ms                                                         | 51.3 ms: 1.02x slower                                                           |
| mako            | 7.09 ms                                                         | 7.69 ms: 1.09x slower                                                           |
| genshi_text     | 21.5 ms                                                         | 24.7 ms: 1.15x slower                                                           |
| django_template | 29.8 ms                                                         | 35.6 ms: 1.20x slower                                                           |
| Geometric mean  | (ref)                                                           | 1.11x slower                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250212-pythonperf1_win32-x86-python-5cdd6e5e758a3fc0a5da-3.14.0a4+-5cdd6e5 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| thrift                     | 9.98 ms                                                         | 779 us: 12.81x faster                                                           |
| coverage                   | 324 ms                                                          | 53.4 ms: 6.07x faster                                                           |
| pathlib                    | 82.9 ms                                                         | 34.0 ms: 2.44x faster                                                           |
| sqlglot_normalize          | 216 ms                                                          | 105 ms: 2.05x faster                                                            |
| deepcopy                   | 314 us                                                          | 256 us: 1.23x faster                                                            |
| deepcopy_memo              | 25.4 us                                                         | 21.4 us: 1.19x faster                                                           |
| regex_effbot               | 1.80 ms                                                         | 1.52 ms: 1.18x faster                                                           |
| deepcopy_reduce            | 2.92 us                                                         | 2.61 us: 1.12x faster                                                           |
| async_tree_io              | 526 ms                                                          | 483 ms: 1.09x faster                                                            |
| regex_v8                   | 16.8 ms                                                         | 15.6 ms: 1.08x faster                                                           |
| async_tree_memoization_tg  | 282 ms                                                          | 266 ms: 1.06x faster                                                            |
| async_tree_none            | 245 ms                                                          | 231 ms: 1.06x faster                                                            |
| async_tree_memoization     | 297 ms                                                          | 281 ms: 1.06x faster                                                            |
| spectral_norm              | 69.4 ms                                                         | 66.2 ms: 1.05x faster                                                           |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 467 ms: 1.04x faster                                                            |
| async_tree_io_tg           | 494 ms                                                          | 477 ms: 1.04x faster                                                            |
| sqlite_synth               | 1.95 us                                                         | 1.89 us: 1.04x faster                                                           |
| coroutines                 | 16.2 ms                                                         | 15.7 ms: 1.03x faster                                                           |
| asyncio_websockets         | 363 ms                                                          | 352 ms: 1.03x faster                                                            |
| async_tree_none_tg         | 214 ms                                                          | 209 ms: 1.03x faster                                                            |
| float                      | 54.6 ms                                                         | 53.6 ms: 1.02x faster                                                           |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 451 ms: 1.01x faster                                                            |
| bench_mp_pool              | 90.6 ms                                                         | 89.9 ms: 1.01x faster                                                           |
| pidigits                   | 201 ms                                                          | 200 ms: 1.01x faster                                                            |
| xml_etree_parse            | 107 ms                                                          | 109 ms: 1.01x slower                                                            |
| go                         | 109 ms                                                          | 110 ms: 1.01x slower                                                            |
| genshi_xml                 | 50.1 ms                                                         | 51.3 ms: 1.02x slower                                                           |
| k_core                     | 1.38 sec                                                        | 1.42 sec: 1.03x slower                                                          |
| gc_traversal               | 1.75 ms                                                         | 1.82 ms: 1.04x slower                                                           |
| regex_dna                  | 114 ms                                                          | 118 ms: 1.04x slower                                                            |
| pyflate                    | 320 ms                                                          | 333 ms: 1.04x slower                                                            |
| logging_simple             | 7.99 us                                                         | 8.39 us: 1.05x slower                                                           |
| logging_format             | 8.72 us                                                         | 9.17 us: 1.05x slower                                                           |
| tomli_loads                | 1.71 sec                                                        | 1.81 sec: 1.05x slower                                                          |
| scimark_monte_carlo        | 47.7 ms                                                         | 50.5 ms: 1.06x slower                                                           |
| json_loads                 | 21.6 us                                                         | 23.1 us: 1.07x slower                                                           |
| sphinx                     | 719 ms                                                          | 770 ms: 1.07x slower                                                            |
| 2to3                       | 250 ms                                                          | 268 ms: 1.07x slower                                                            |
| dulwich_log                | 48.8 ms                                                         | 52.4 ms: 1.07x slower                                                           |
| json                       | 4.27 ms                                                         | 4.63 ms: 1.08x slower                                                           |
| mako                       | 7.09 ms                                                         | 7.69 ms: 1.09x slower                                                           |
| generators                 | 21.8 ms                                                         | 23.7 ms: 1.09x slower                                                           |
| xml_etree_iterparse        | 62.6 ms                                                         | 68.1 ms: 1.09x slower                                                           |
| sympy_expand               | 373 ms                                                          | 407 ms: 1.09x slower                                                            |
| connected_components       | 267 ms                                                          | 291 ms: 1.09x slower                                                            |
| sympy_sum                  | 106 ms                                                          | 116 ms: 1.09x slower                                                            |
| sympy_str                  | 212 ms                                                          | 233 ms: 1.10x slower                                                            |
| telco                      | 6.96 ms                                                         | 7.68 ms: 1.10x slower                                                           |
| python_startup_no_site     | 19.7 ms                                                         | 21.7 ms: 1.10x slower                                                           |
| bpe_tokeniser              | 3.46 sec                                                        | 3.83 sec: 1.11x slower                                                          |
| pycparser                  | 872 ms                                                          | 970 ms: 1.11x slower                                                            |
| scimark_sparse_mat_mult    | 2.84 ms                                                         | 3.17 ms: 1.12x slower                                                           |
| docutils                   | 1.78 sec                                                        | 2.01 sec: 1.13x slower                                                          |
| shortest_path              | 290 ms                                                          | 327 ms: 1.13x slower                                                            |
| sympy_integrate            | 15.0 ms                                                         | 16.9 ms: 1.13x slower                                                           |
| scimark_lu                 | 60.2 ms                                                         | 68.5 ms: 1.14x slower                                                           |
| richards                   | 32.7 ms                                                         | 37.2 ms: 1.14x slower                                                           |
| genshi_text                | 21.5 ms                                                         | 24.7 ms: 1.15x slower                                                           |
| mdp                        | 1.62 sec                                                        | 1.89 sec: 1.16x slower                                                          |
| chaos                      | 50.2 ms                                                         | 58.5 ms: 1.16x slower                                                           |
| richards_super             | 36.7 ms                                                         | 42.9 ms: 1.17x slower                                                           |
| regex_compile              | 101 ms                                                          | 118 ms: 1.17x slower                                                            |
| scimark_sor                | 85.9 ms                                                         | 101 ms: 1.17x slower                                                            |
| deltablue                  | 2.33 ms                                                         | 2.75 ms: 1.18x slower                                                           |
| async_generators           | 270 ms                                                          | 322 ms: 1.19x slower                                                            |
| pprint_pformat             | 1.33 sec                                                        | 1.59 sec: 1.19x slower                                                          |
| pprint_safe_repr           | 648 ms                                                          | 775 ms: 1.20x slower                                                            |
| logging_silent             | 60.3 ns                                                         | 72.1 ns: 1.20x slower                                                           |
| django_template            | 29.8 ms                                                         | 35.6 ms: 1.20x slower                                                           |
| sqlglot_parse              | 1.00 ms                                                         | 1.21 ms: 1.21x slower                                                           |
| sqlglot_transpile          | 1.24 ms                                                         | 1.49 ms: 1.21x slower                                                           |
| xml_etree_generate         | 61.4 ms                                                         | 74.9 ms: 1.22x slower                                                           |
| sqlglot_optimize           | 41.4 ms                                                         | 50.8 ms: 1.22x slower                                                           |
| json_dumps                 | 7.30 ms                                                         | 9.02 ms: 1.24x slower                                                           |
| fannkuch                   | 299 ms                                                          | 373 ms: 1.25x slower                                                            |
| xml_etree_process          | 44.2 ms                                                         | 55.7 ms: 1.26x slower                                                           |
| raytrace                   | 201 ms                                                          | 254 ms: 1.26x slower                                                            |
| typing_runtime_protocols   | 138 us                                                          | 174 us: 1.26x slower                                                            |
| meteor_contest             | 74.6 ms                                                         | 95.1 ms: 1.28x slower                                                           |
| scimark_fft                | 205 ms                                                          | 261 ms: 1.28x slower                                                            |
| crypto_pyaes               | 56.9 ms                                                         | 73.5 ms: 1.29x slower                                                           |
| many_optionals             | 436 us                                                          | 568 us: 1.30x slower                                                            |
| comprehensions             | 12.5 us                                                         | 16.6 us: 1.33x slower                                                           |
| bench_thread_pool          | 1.00 ms                                                         | 1.34 ms: 1.34x slower                                                           |
| pickle_pure_python         | 231 us                                                          | 319 us: 1.38x slower                                                            |
| hexiom                     | 4.44 ms                                                         | 6.13 ms: 1.38x slower                                                           |
| unpickle_pure_python       | 160 us                                                          | 226 us: 1.41x slower                                                            |
| nbody                      | 80.0 ms                                                         | 113 ms: 1.41x slower                                                            |
| nqueens                    | 72.1 ms                                                         | 104 ms: 1.45x slower                                                            |
| subparsers                 | 14.8 ms                                                         | 22.6 ms: 1.53x slower                                                           |
| Geometric mean             | (ref)                                                           | 1.03x slower                                                                    |

Benchmark hidden because not significant (4): python_startup, create_gc_cycles, html5lib, pylint
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http

- Geometric mean (including insignificant results): 1.028x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.06x
- 95% likely to have a slowdown of 1.05x
- 99% likely to have a slowdown of 1.04x

# Memory
- memory change: unknown