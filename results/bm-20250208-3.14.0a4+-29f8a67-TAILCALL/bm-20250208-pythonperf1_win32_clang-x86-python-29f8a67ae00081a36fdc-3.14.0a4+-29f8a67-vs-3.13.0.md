# Results vs. 3.13.0

- fork: python
- ref: 29f8a67ae00081a36fdc
- machine: windows-x86
- commit hash: 29f8a67
- commit date: 2025-02-08
- overall geometric mean: 1.144x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250208-pythonperf1_win32-x86-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 250 ms                                                          | 240 ms: 1.04x faster                                                            |
| docutils       | 1.78 sec                                                        | 1.73 sec: 1.03x faster                                                          |
| html5lib       | 47.5 ms                                                         | 42.4 ms: 1.12x faster                                                           |
| sphinx         | 719 ms                                                          | 707 ms: 1.02x faster                                                            |
| Geometric mean | (ref)                                                           | 1.05x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250208-pythonperf1_win32-x86-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_none            | 245 ms                                                          | 176 ms: 1.39x faster                                                            |
| async_tree_memoization     | 297 ms                                                          | 215 ms: 1.38x faster                                                            |
| async_tree_io              | 526 ms                                                          | 385 ms: 1.36x faster                                                            |
| async_tree_memoization_tg  | 282 ms                                                          | 213 ms: 1.33x faster                                                            |
| async_tree_io_tg           | 494 ms                                                          | 373 ms: 1.33x faster                                                            |
| async_tree_none_tg         | 214 ms                                                          | 162 ms: 1.32x faster                                                            |
| coroutines                 | 16.2 ms                                                         | 13.2 ms: 1.23x faster                                                           |
| async_generators           | 270 ms                                                          | 231 ms: 1.17x faster                                                            |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 438 ms: 1.11x faster                                                            |
| asyncio_websockets         | 363 ms                                                          | 341 ms: 1.06x faster                                                            |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 429 ms: 1.06x faster                                                            |
| Geometric mean             | (ref)                                                           | 1.24x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250208-pythonperf1_win32-x86-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 54.6 ms                                                         | 44.0 ms: 1.24x faster                                                           |
| nbody          | 80.0 ms                                                         | 64.5 ms: 1.24x faster                                                           |
| pidigits       | 201 ms                                                          | 217 ms: 1.08x slower                                                            |
| Geometric mean | (ref)                                                           | 1.12x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250208-pythonperf1_win32-x86-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 101 ms                                                          | 90.0 ms: 1.12x faster                                                           |
| regex_effbot   | 1.80 ms                                                         | 1.97 ms: 1.10x slower                                                           |
| regex_dna      | 114 ms                                                          | 132 ms: 1.16x slower                                                            |
| Geometric mean | (ref)                                                           | 1.04x slower                                                                    |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250208-pythonperf1_win32-x86-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 1.71 sec                                                        | 1.39 sec: 1.23x faster                                                          |
| unpickle_pure_python | 160 us                                                          | 151 us: 1.06x faster                                                            |
| pickle_pure_python   | 231 us                                                          | 220 us: 1.05x faster                                                            |
| json_loads           | 21.6 us                                                         | 21.5 us: 1.00x faster                                                           |
| xml_etree_process    | 44.2 ms                                                         | 46.6 ms: 1.05x slower                                                           |
| json_dumps           | 7.30 ms                                                         | 7.71 ms: 1.06x slower                                                           |
| xml_etree_parse      | 107 ms                                                          | 114 ms: 1.06x slower                                                            |
| xml_etree_generate   | 61.4 ms                                                         | 66.3 ms: 1.08x slower                                                           |
| xml_etree_iterparse  | 62.6 ms                                                         | 71.8 ms: 1.15x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.01x slower                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250208-pythonperf1_win32-x86-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 28.3 ms                                                         | 29.6 ms: 1.05x slower                                                           |
| python_startup_no_site | 19.7 ms                                                         | 22.6 ms: 1.15x slower                                                           |
| Geometric mean         | (ref)                                                           | 1.10x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250208-pythonperf1_win32-x86-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_xml      | 50.1 ms                                                         | 36.0 ms: 1.39x faster                                                           |
| genshi_text     | 21.5 ms                                                         | 15.9 ms: 1.35x faster                                                           |
| django_template | 29.8 ms                                                         | 28.6 ms: 1.04x faster                                                           |
| mako            | 7.09 ms                                                         | 7.59 ms: 1.07x slower                                                           |
| Geometric mean  | (ref)                                                           | 1.16x faster                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250208-pythonperf1_win32-x86-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| thrift                     | 9.98 ms                                                         | 645 us: 15.47x faster                                                           |
| coverage                   | 324 ms                                                          | 55.7 ms: 5.82x faster                                                           |
| deepcopy                   | 314 us                                                          | 189 us: 1.66x faster                                                            |
| deepcopy_reduce            | 2.92 us                                                         | 2.01 us: 1.45x faster                                                           |
| deepcopy_memo              | 25.4 us                                                         | 17.7 us: 1.44x faster                                                           |
| go                         | 109 ms                                                          | 77.5 ms: 1.40x faster                                                           |
| genshi_xml                 | 50.1 ms                                                         | 36.0 ms: 1.39x faster                                                           |
| async_tree_none            | 245 ms                                                          | 176 ms: 1.39x faster                                                            |
| async_tree_memoization     | 297 ms                                                          | 215 ms: 1.38x faster                                                            |
| async_tree_io              | 526 ms                                                          | 385 ms: 1.36x faster                                                            |
| genshi_text                | 21.5 ms                                                         | 15.9 ms: 1.35x faster                                                           |
| async_tree_memoization_tg  | 282 ms                                                          | 213 ms: 1.33x faster                                                            |
| async_tree_io_tg           | 494 ms                                                          | 373 ms: 1.33x faster                                                            |
| async_tree_none_tg         | 214 ms                                                          | 162 ms: 1.32x faster                                                            |
| pathlib                    | 82.9 ms                                                         | 66.0 ms: 1.26x faster                                                           |
| generators                 | 21.8 ms                                                         | 17.5 ms: 1.24x faster                                                           |
| pprint_pformat             | 1.33 sec                                                        | 1.07 sec: 1.24x faster                                                          |
| float                      | 54.6 ms                                                         | 44.0 ms: 1.24x faster                                                           |
| nbody                      | 80.0 ms                                                         | 64.5 ms: 1.24x faster                                                           |
| pprint_safe_repr           | 648 ms                                                          | 524 ms: 1.24x faster                                                            |
| coroutines                 | 16.2 ms                                                         | 13.2 ms: 1.23x faster                                                           |
| tomli_loads                | 1.71 sec                                                        | 1.39 sec: 1.23x faster                                                          |
| deltablue                  | 2.33 ms                                                         | 1.97 ms: 1.19x faster                                                           |
| spectral_norm              | 69.4 ms                                                         | 58.6 ms: 1.18x faster                                                           |
| scimark_sor                | 85.9 ms                                                         | 72.7 ms: 1.18x faster                                                           |
| telco                      | 6.96 ms                                                         | 5.91 ms: 1.18x faster                                                           |
| sqlglot_parse              | 1.00 ms                                                         | 858 us: 1.17x faster                                                            |
| async_generators           | 270 ms                                                          | 231 ms: 1.17x faster                                                            |
| chaos                      | 50.2 ms                                                         | 43.8 ms: 1.15x faster                                                           |
| sqlglot_transpile          | 1.24 ms                                                         | 1.08 ms: 1.15x faster                                                           |
| scimark_monte_carlo        | 47.7 ms                                                         | 41.6 ms: 1.15x faster                                                           |
| pycparser                  | 872 ms                                                          | 765 ms: 1.14x faster                                                            |
| logging_format             | 8.72 us                                                         | 7.65 us: 1.14x faster                                                           |
| sympy_expand               | 373 ms                                                          | 328 ms: 1.14x faster                                                            |
| sqlglot_normalize          | 216 ms                                                          | 192 ms: 1.13x faster                                                            |
| regex_compile              | 101 ms                                                          | 90.0 ms: 1.12x faster                                                           |
| html5lib                   | 47.5 ms                                                         | 42.4 ms: 1.12x faster                                                           |
| logging_simple             | 7.99 us                                                         | 7.17 us: 1.11x faster                                                           |
| sympy_str                  | 212 ms                                                          | 190 ms: 1.11x faster                                                            |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 438 ms: 1.11x faster                                                            |
| scimark_sparse_mat_mult    | 2.84 ms                                                         | 2.58 ms: 1.10x faster                                                           |
| bpe_tokeniser              | 3.46 sec                                                        | 3.15 sec: 1.10x faster                                                          |
| pylint                     | 227 ms                                                          | 207 ms: 1.10x faster                                                            |
| fannkuch                   | 299 ms                                                          | 273 ms: 1.09x faster                                                            |
| pyflate                    | 320 ms                                                          | 293 ms: 1.09x faster                                                            |
| typing_runtime_protocols   | 138 us                                                          | 126 us: 1.09x faster                                                            |
| raytrace                   | 201 ms                                                          | 186 ms: 1.08x faster                                                            |
| sqlglot_optimize           | 41.4 ms                                                         | 38.3 ms: 1.08x faster                                                           |
| sympy_sum                  | 106 ms                                                          | 98.1 ms: 1.08x faster                                                           |
| sympy_integrate            | 15.0 ms                                                         | 14.0 ms: 1.07x faster                                                           |
| richards                   | 32.7 ms                                                         | 30.6 ms: 1.07x faster                                                           |
| asyncio_websockets         | 363 ms                                                          | 341 ms: 1.06x faster                                                            |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 429 ms: 1.06x faster                                                            |
| scimark_fft                | 205 ms                                                          | 193 ms: 1.06x faster                                                            |
| unpickle_pure_python       | 160 us                                                          | 151 us: 1.06x faster                                                            |
| sqlite_synth               | 1.95 us                                                         | 1.85 us: 1.05x faster                                                           |
| nqueens                    | 72.1 ms                                                         | 68.4 ms: 1.05x faster                                                           |
| richards_super             | 36.7 ms                                                         | 34.8 ms: 1.05x faster                                                           |
| hexiom                     | 4.44 ms                                                         | 4.22 ms: 1.05x faster                                                           |
| connected_components       | 267 ms                                                          | 254 ms: 1.05x faster                                                            |
| pickle_pure_python         | 231 us                                                          | 220 us: 1.05x faster                                                            |
| django_template            | 29.8 ms                                                         | 28.6 ms: 1.04x faster                                                           |
| dulwich_log                | 48.8 ms                                                         | 46.8 ms: 1.04x faster                                                           |
| 2to3                       | 250 ms                                                          | 240 ms: 1.04x faster                                                            |
| shortest_path              | 290 ms                                                          | 278 ms: 1.04x faster                                                            |
| k_core                     | 1.38 sec                                                        | 1.33 sec: 1.04x faster                                                          |
| crypto_pyaes               | 56.9 ms                                                         | 54.9 ms: 1.04x faster                                                           |
| comprehensions             | 12.5 us                                                         | 12.1 us: 1.03x faster                                                           |
| docutils                   | 1.78 sec                                                        | 1.73 sec: 1.03x faster                                                          |
| sphinx                     | 719 ms                                                          | 707 ms: 1.02x faster                                                            |
| json                       | 4.27 ms                                                         | 4.21 ms: 1.01x faster                                                           |
| json_loads                 | 21.6 us                                                         | 21.5 us: 1.00x faster                                                           |
| meteor_contest             | 74.6 ms                                                         | 74.9 ms: 1.00x slower                                                           |
| python_startup             | 28.3 ms                                                         | 29.6 ms: 1.05x slower                                                           |
| xml_etree_process          | 44.2 ms                                                         | 46.6 ms: 1.05x slower                                                           |
| json_dumps                 | 7.30 ms                                                         | 7.71 ms: 1.06x slower                                                           |
| xml_etree_parse            | 107 ms                                                          | 114 ms: 1.06x slower                                                            |
| mako                       | 7.09 ms                                                         | 7.59 ms: 1.07x slower                                                           |
| xml_etree_generate         | 61.4 ms                                                         | 66.3 ms: 1.08x slower                                                           |
| pidigits                   | 201 ms                                                          | 217 ms: 1.08x slower                                                            |
| bench_mp_pool              | 90.6 ms                                                         | 98.1 ms: 1.08x slower                                                           |
| mdp                        | 1.62 sec                                                        | 1.77 sec: 1.09x slower                                                          |
| regex_effbot               | 1.80 ms                                                         | 1.97 ms: 1.10x slower                                                           |
| logging_silent             | 60.3 ns                                                         | 66.4 ns: 1.10x slower                                                           |
| many_optionals             | 436 us                                                          | 487 us: 1.12x slower                                                            |
| create_gc_cycles           | 1.06 ms                                                         | 1.19 ms: 1.13x slower                                                           |
| scimark_lu                 | 60.2 ms                                                         | 68.5 ms: 1.14x slower                                                           |
| xml_etree_iterparse        | 62.6 ms                                                         | 71.8 ms: 1.15x slower                                                           |
| python_startup_no_site     | 19.7 ms                                                         | 22.6 ms: 1.15x slower                                                           |
| regex_dna                  | 114 ms                                                          | 132 ms: 1.16x slower                                                            |
| subparsers                 | 14.8 ms                                                         | 19.1 ms: 1.29x slower                                                           |
| bench_thread_pool          | 1.00 ms                                                         | 1.31 ms: 1.31x slower                                                           |
| gc_traversal               | 1.75 ms                                                         | 2.43 ms: 1.39x slower                                                           |
| Geometric mean             | (ref)                                                           | 1.14x faster                                                                    |

Benchmark hidden because not significant (1): regex_v8
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http

- Geometric mean (including insignificant results): 1.144x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.07x
- 95% likely to have a speedup of 1.06x
- 99% likely to have a speedup of 1.06x

# Memory
- memory change: unknown