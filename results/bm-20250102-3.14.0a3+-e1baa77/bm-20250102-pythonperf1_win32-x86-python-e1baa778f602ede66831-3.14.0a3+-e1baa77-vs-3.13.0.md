# Results vs. 3.13.0

- fork: python
- ref: e1baa778f602ede66831
- machine: windows-x86
- commit hash: e1baa77
- commit date: 2025-01-02
- overall geometric mean: 1.041x faster
- HPT reliability: 59.93%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250102-pythonperf1_win32-x86-python-e1baa778f602ede66831-3.14.0a3+-e1baa77 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 250 ms                                                          | 243 ms: 1.03x faster                                                            |
| docutils       | 1.78 sec                                                        | 1.80 sec: 1.01x slower                                                          |
| html5lib       | 47.5 ms                                                         | 43.5 ms: 1.09x faster                                                           |
| sphinx         | 719 ms                                                          | 727 ms: 1.01x slower                                                            |
| Geometric mean | (ref)                                                           | 1.02x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250102-pythonperf1_win32-x86-python-e1baa778f602ede66831-3.14.0a3+-e1baa77 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 282 ms                                                          | 222 ms: 1.27x faster                                                            |
| async_tree_none            | 245 ms                                                          | 194 ms: 1.26x faster                                                            |
| async_tree_memoization     | 297 ms                                                          | 240 ms: 1.23x faster                                                            |
| async_tree_io              | 526 ms                                                          | 426 ms: 1.23x faster                                                            |
| async_tree_io_tg           | 494 ms                                                          | 408 ms: 1.21x faster                                                            |
| async_tree_none_tg         | 214 ms                                                          | 177 ms: 1.21x faster                                                            |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 434 ms: 1.12x faster                                                            |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 423 ms: 1.08x faster                                                            |
| asyncio_websockets         | 363 ms                                                          | 352 ms: 1.03x faster                                                            |
| coroutines                 | 16.2 ms                                                         | 16.6 ms: 1.02x slower                                                           |
| async_generators           | 270 ms                                                          | 302 ms: 1.12x slower                                                            |
| Geometric mean             | (ref)                                                           | 1.13x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250102-pythonperf1_win32-x86-python-e1baa778f602ede66831-3.14.0a3+-e1baa77 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pidigits       | 201 ms                                                          | 197 ms: 1.02x faster                                                            |
| float          | 54.6 ms                                                         | 55.8 ms: 1.02x slower                                                           |
| nbody          | 80.0 ms                                                         | 85.8 ms: 1.07x slower                                                           |
| Geometric mean | (ref)                                                           | 1.02x slower                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250102-pythonperf1_win32-x86-python-e1baa778f602ede66831-3.14.0a3+-e1baa77 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_effbot   | 1.80 ms                                                         | 1.65 ms: 1.09x faster                                                           |
| regex_dna      | 114 ms                                                          | 126 ms: 1.11x slower                                                            |
| Geometric mean | (ref)                                                           | 1.01x faster                                                                    |

Benchmark hidden because not significant (2): regex_v8, regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250102-pythonperf1_win32-x86-python-e1baa778f602ede66831-3.14.0a3+-e1baa77 |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 1.71 sec                                                        | 1.64 sec: 1.04x faster                                                          |
| json_loads           | 21.6 us                                                         | 20.7 us: 1.04x faster                                                           |
| xml_etree_parse      | 107 ms                                                          | 111 ms: 1.03x slower                                                            |
| unpickle_pure_python | 160 us                                                          | 171 us: 1.07x slower                                                            |
| xml_etree_iterparse  | 62.6 ms                                                         | 67.2 ms: 1.07x slower                                                           |
| xml_etree_generate   | 61.4 ms                                                         | 67.8 ms: 1.10x slower                                                           |
| pickle_pure_python   | 231 us                                                          | 259 us: 1.12x slower                                                            |
| xml_etree_process    | 44.2 ms                                                         | 50.0 ms: 1.13x slower                                                           |
| json_dumps           | 7.30 ms                                                         | 8.81 ms: 1.21x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.07x slower                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250102-pythonperf1_win32-x86-python-e1baa778f602ede66831-3.14.0a3+-e1baa77 |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 28.3 ms                                                         | 26.9 ms: 1.05x faster                                                           |
| python_startup_no_site | 19.7 ms                                                         | 20.3 ms: 1.03x slower                                                           |
| Geometric mean         | (ref)                                                           | 1.01x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250102-pythonperf1_win32-x86-python-e1baa778f602ede66831-3.14.0a3+-e1baa77 |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_xml      | 50.1 ms                                                         | 45.0 ms: 1.12x faster                                                           |
| genshi_text     | 21.5 ms                                                         | 20.5 ms: 1.05x faster                                                           |
| django_template | 29.8 ms                                                         | 31.8 ms: 1.07x slower                                                           |
| mako            | 7.09 ms                                                         | 7.79 ms: 1.10x slower                                                           |
| Geometric mean  | (ref)                                                           | 1.00x slower                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250102-pythonperf1_win32-x86-python-e1baa778f602ede66831-3.14.0a3+-e1baa77 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| thrift                     | 9.98 ms                                                         | 721 us: 13.83x faster                                                           |
| coverage                   | 324 ms                                                          | 51.6 ms: 6.27x faster                                                           |
| deepcopy                   | 314 us                                                          | 227 us: 1.38x faster                                                            |
| async_tree_memoization_tg  | 282 ms                                                          | 222 ms: 1.27x faster                                                            |
| async_tree_none            | 245 ms                                                          | 194 ms: 1.26x faster                                                            |
| async_tree_memoization     | 297 ms                                                          | 240 ms: 1.23x faster                                                            |
| async_tree_io              | 526 ms                                                          | 426 ms: 1.23x faster                                                            |
| async_tree_io_tg           | 494 ms                                                          | 408 ms: 1.21x faster                                                            |
| async_tree_none_tg         | 214 ms                                                          | 177 ms: 1.21x faster                                                            |
| deepcopy_reduce            | 2.92 us                                                         | 2.42 us: 1.21x faster                                                           |
| deepcopy_memo              | 25.4 us                                                         | 22.2 us: 1.15x faster                                                           |
| go                         | 109 ms                                                          | 96.4 ms: 1.13x faster                                                           |
| genshi_xml                 | 50.1 ms                                                         | 45.0 ms: 1.12x faster                                                           |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 434 ms: 1.12x faster                                                            |
| html5lib                   | 47.5 ms                                                         | 43.5 ms: 1.09x faster                                                           |
| regex_effbot               | 1.80 ms                                                         | 1.65 ms: 1.09x faster                                                           |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 423 ms: 1.08x faster                                                            |
| pycparser                  | 872 ms                                                          | 812 ms: 1.07x faster                                                            |
| python_startup             | 28.3 ms                                                         | 26.9 ms: 1.05x faster                                                           |
| pylint                     | 227 ms                                                          | 216 ms: 1.05x faster                                                            |
| genshi_text                | 21.5 ms                                                         | 20.5 ms: 1.05x faster                                                           |
| connected_components       | 267 ms                                                          | 255 ms: 1.05x faster                                                            |
| tomli_loads                | 1.71 sec                                                        | 1.64 sec: 1.04x faster                                                          |
| json_loads                 | 21.6 us                                                         | 20.7 us: 1.04x faster                                                           |
| bench_mp_pool              | 90.6 ms                                                         | 87.2 ms: 1.04x faster                                                           |
| telco                      | 6.96 ms                                                         | 6.73 ms: 1.03x faster                                                           |
| logging_format             | 8.72 us                                                         | 8.44 us: 1.03x faster                                                           |
| 2to3                       | 250 ms                                                          | 243 ms: 1.03x faster                                                            |
| asyncio_websockets         | 363 ms                                                          | 352 ms: 1.03x faster                                                            |
| json                       | 4.27 ms                                                         | 4.17 ms: 1.03x faster                                                           |
| logging_simple             | 7.99 us                                                         | 7.80 us: 1.02x faster                                                           |
| k_core                     | 1.38 sec                                                        | 1.35 sec: 1.02x faster                                                          |
| pidigits                   | 201 ms                                                          | 197 ms: 1.02x faster                                                            |
| shortest_path              | 290 ms                                                          | 285 ms: 1.02x faster                                                            |
| sqlite_synth               | 1.95 us                                                         | 1.93 us: 1.01x faster                                                           |
| pprint_pformat             | 1.33 sec                                                        | 1.32 sec: 1.01x faster                                                          |
| fannkuch                   | 299 ms                                                          | 298 ms: 1.00x faster                                                            |
| sqlglot_normalize          | 216 ms                                                          | 217 ms: 1.00x slower                                                            |
| sympy_expand               | 373 ms                                                          | 375 ms: 1.01x slower                                                            |
| sqlglot_optimize           | 41.4 ms                                                         | 41.7 ms: 1.01x slower                                                           |
| sympy_str                  | 212 ms                                                          | 213 ms: 1.01x slower                                                            |
| sphinx                     | 719 ms                                                          | 727 ms: 1.01x slower                                                            |
| docutils                   | 1.78 sec                                                        | 1.80 sec: 1.01x slower                                                          |
| dulwich_log                | 48.8 ms                                                         | 49.4 ms: 1.01x slower                                                           |
| sqlglot_parse              | 1.00 ms                                                         | 1.02 ms: 1.02x slower                                                           |
| coroutines                 | 16.2 ms                                                         | 16.6 ms: 1.02x slower                                                           |
| sympy_integrate            | 15.0 ms                                                         | 15.3 ms: 1.02x slower                                                           |
| float                      | 54.6 ms                                                         | 55.8 ms: 1.02x slower                                                           |
| typing_runtime_protocols   | 138 us                                                          | 141 us: 1.02x slower                                                            |
| sqlglot_transpile          | 1.24 ms                                                         | 1.27 ms: 1.03x slower                                                           |
| spectral_norm              | 69.4 ms                                                         | 71.3 ms: 1.03x slower                                                           |
| gc_traversal               | 1.75 ms                                                         | 1.81 ms: 1.03x slower                                                           |
| xml_etree_parse            | 107 ms                                                          | 111 ms: 1.03x slower                                                            |
| python_startup_no_site     | 19.7 ms                                                         | 20.3 ms: 1.03x slower                                                           |
| scimark_sparse_mat_mult    | 2.84 ms                                                         | 2.97 ms: 1.04x slower                                                           |
| nqueens                    | 72.1 ms                                                         | 75.6 ms: 1.05x slower                                                           |
| pyflate                    | 320 ms                                                          | 336 ms: 1.05x slower                                                            |
| scimark_fft                | 205 ms                                                          | 216 ms: 1.05x slower                                                            |
| mdp                        | 1.62 sec                                                        | 1.73 sec: 1.07x slower                                                          |
| django_template            | 29.8 ms                                                         | 31.8 ms: 1.07x slower                                                           |
| crypto_pyaes               | 56.9 ms                                                         | 60.9 ms: 1.07x slower                                                           |
| unpickle_pure_python       | 160 us                                                          | 171 us: 1.07x slower                                                            |
| nbody                      | 80.0 ms                                                         | 85.8 ms: 1.07x slower                                                           |
| xml_etree_iterparse        | 62.6 ms                                                         | 67.2 ms: 1.07x slower                                                           |
| chaos                      | 50.2 ms                                                         | 54.0 ms: 1.08x slower                                                           |
| mako                       | 7.09 ms                                                         | 7.79 ms: 1.10x slower                                                           |
| comprehensions             | 12.5 us                                                         | 13.8 us: 1.10x slower                                                           |
| meteor_contest             | 74.6 ms                                                         | 82.2 ms: 1.10x slower                                                           |
| xml_etree_generate         | 61.4 ms                                                         | 67.8 ms: 1.10x slower                                                           |
| regex_dna                  | 114 ms                                                          | 126 ms: 1.11x slower                                                            |
| deltablue                  | 2.33 ms                                                         | 2.59 ms: 1.11x slower                                                           |
| async_generators           | 270 ms                                                          | 302 ms: 1.12x slower                                                            |
| pickle_pure_python         | 231 us                                                          | 259 us: 1.12x slower                                                            |
| richards                   | 32.7 ms                                                         | 36.8 ms: 1.13x slower                                                           |
| hexiom                     | 4.44 ms                                                         | 5.00 ms: 1.13x slower                                                           |
| scimark_monte_carlo        | 47.7 ms                                                         | 53.8 ms: 1.13x slower                                                           |
| generators                 | 21.8 ms                                                         | 24.6 ms: 1.13x slower                                                           |
| xml_etree_process          | 44.2 ms                                                         | 50.0 ms: 1.13x slower                                                           |
| scimark_lu                 | 60.2 ms                                                         | 68.6 ms: 1.14x slower                                                           |
| richards_super             | 36.7 ms                                                         | 42.3 ms: 1.15x slower                                                           |
| scimark_sor                | 85.9 ms                                                         | 101 ms: 1.17x slower                                                            |
| logging_silent             | 60.3 ns                                                         | 70.7 ns: 1.17x slower                                                           |
| many_optionals             | 436 us                                                          | 520 us: 1.19x slower                                                            |
| raytrace                   | 201 ms                                                          | 242 ms: 1.20x slower                                                            |
| json_dumps                 | 7.30 ms                                                         | 8.81 ms: 1.21x slower                                                           |
| subparsers                 | 14.8 ms                                                         | 20.5 ms: 1.39x slower                                                           |
| Geometric mean             | (ref)                                                           | 1.04x faster                                                                    |

Benchmark hidden because not significant (8): regex_v8, create_gc_cycles, pprint_safe_repr, regex_compile, bpe_tokeniser, pathlib, sympy_sum, bench_thread_pool
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (1) of results/bm-20250102-3.14.0a3+-e1baa77/bm-20250102-pythonperf1_win32-x86-python-e1baa778f602ede66831-3.14.0a3+-e1baa77.json: mypy2

- Geometric mean (including insignificant results): 1.041x faster

# HPT report

- Reliability score: 59.93% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown