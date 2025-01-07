# Results vs. 3.13.0

- fork: kumaraditya303
- ref: future_iter
- machine: windows-x86
- commit hash: 82b905d
- commit date: 2025-01-05
- overall geometric mean: 1.055x faster
- HPT reliability: 71.13%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250105-pythonperf1_win32-x86-kumaraditya303-future_iter-3.14.0a3+-82b905d |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 250 ms                                                          | 245 ms: 1.02x faster                                                           |
| docutils       | 1.78 sec                                                        | 1.79 sec: 1.01x slower                                                         |
| html5lib       | 47.5 ms                                                         | 43.3 ms: 1.10x faster                                                          |
| sphinx         | 719 ms                                                          | 725 ms: 1.01x slower                                                           |
| Geometric mean | (ref)                                                           | 1.02x faster                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250105-pythonperf1_win32-x86-kumaraditya303-future_iter-3.14.0a3+-82b905d |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 282 ms                                                          | 225 ms: 1.25x faster                                                           |
| async_tree_none            | 245 ms                                                          | 197 ms: 1.24x faster                                                           |
| async_tree_memoization     | 297 ms                                                          | 241 ms: 1.23x faster                                                           |
| async_tree_io              | 526 ms                                                          | 434 ms: 1.21x faster                                                           |
| async_tree_none_tg         | 214 ms                                                          | 179 ms: 1.20x faster                                                           |
| async_tree_io_tg           | 494 ms                                                          | 421 ms: 1.17x faster                                                           |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 433 ms: 1.12x faster                                                           |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 423 ms: 1.08x faster                                                           |
| asyncio_websockets         | 363 ms                                                          | 377 ms: 1.04x slower                                                           |
| async_generators           | 270 ms                                                          | 290 ms: 1.07x slower                                                           |
| Geometric mean             | (ref)                                                           | 1.12x faster                                                                   |

Benchmark hidden because not significant (1): coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250105-pythonperf1_win32-x86-kumaraditya303-future_iter-3.14.0a3+-82b905d |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pidigits       | 201 ms                                                          | 196 ms: 1.02x faster                                                           |
| float          | 54.6 ms                                                         | 53.8 ms: 1.01x faster                                                          |
| nbody          | 80.0 ms                                                         | 83.5 ms: 1.04x slower                                                          |
| Geometric mean | (ref)                                                           | 1.00x slower                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250105-pythonperf1_win32-x86-kumaraditya303-future_iter-3.14.0a3+-82b905d |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_effbot   | 1.80 ms                                                         | 1.58 ms: 1.14x faster                                                          |
| regex_dna      | 114 ms                                                          | 117 ms: 1.03x slower                                                           |
| Geometric mean | (ref)                                                           | 1.04x faster                                                                   |

Benchmark hidden because not significant (2): regex_v8, regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250105-pythonperf1_win32-x86-kumaraditya303-future_iter-3.14.0a3+-82b905d |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| xml_etree_parse      | 107 ms                                                          | 95.4 ms: 1.13x faster                                                          |
| tomli_loads          | 1.71 sec                                                        | 1.55 sec: 1.10x faster                                                         |
| json_loads           | 21.6 us                                                         | 20.7 us: 1.04x faster                                                          |
| xml_etree_iterparse  | 62.6 ms                                                         | 63.6 ms: 1.02x slower                                                          |
| unpickle_pure_python | 160 us                                                          | 168 us: 1.05x slower                                                           |
| xml_etree_generate   | 61.4 ms                                                         | 66.3 ms: 1.08x slower                                                          |
| xml_etree_process    | 44.2 ms                                                         | 48.0 ms: 1.09x slower                                                          |
| pickle_pure_python   | 231 us                                                          | 252 us: 1.09x slower                                                           |
| json_dumps           | 7.30 ms                                                         | 9.09 ms: 1.25x slower                                                          |
| Geometric mean       | (ref)                                                           | 1.03x slower                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250105-pythonperf1_win32-x86-kumaraditya303-future_iter-3.14.0a3+-82b905d |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 28.3 ms                                                         | 25.4 ms: 1.11x faster                                                          |
| python_startup_no_site | 19.7 ms                                                         | 19.2 ms: 1.02x faster                                                          |
| Geometric mean         | (ref)                                                           | 1.07x faster                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250105-pythonperf1_win32-x86-kumaraditya303-future_iter-3.14.0a3+-82b905d |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| genshi_xml      | 50.1 ms                                                         | 44.5 ms: 1.13x faster                                                          |
| genshi_text     | 21.5 ms                                                         | 20.4 ms: 1.05x faster                                                          |
| django_template | 29.8 ms                                                         | 31.2 ms: 1.05x slower                                                          |
| mako            | 7.09 ms                                                         | 7.48 ms: 1.06x slower                                                          |
| Geometric mean  | (ref)                                                           | 1.02x faster                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250105-pythonperf1_win32-x86-kumaraditya303-future_iter-3.14.0a3+-82b905d |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| thrift                     | 9.98 ms                                                         | 735 us: 13.57x faster                                                          |
| coverage                   | 324 ms                                                          | 52.3 ms: 6.19x faster                                                          |
| deepcopy                   | 314 us                                                          | 234 us: 1.34x faster                                                           |
| async_tree_memoization_tg  | 282 ms                                                          | 225 ms: 1.25x faster                                                           |
| async_tree_none            | 245 ms                                                          | 197 ms: 1.24x faster                                                           |
| async_tree_memoization     | 297 ms                                                          | 241 ms: 1.23x faster                                                           |
| async_tree_io              | 526 ms                                                          | 434 ms: 1.21x faster                                                           |
| async_tree_none_tg         | 214 ms                                                          | 179 ms: 1.20x faster                                                           |
| deepcopy_reduce            | 2.92 us                                                         | 2.46 us: 1.19x faster                                                          |
| deepcopy_memo              | 25.4 us                                                         | 21.5 us: 1.18x faster                                                          |
| async_tree_io_tg           | 494 ms                                                          | 421 ms: 1.17x faster                                                           |
| go                         | 109 ms                                                          | 94.1 ms: 1.16x faster                                                          |
| regex_effbot               | 1.80 ms                                                         | 1.58 ms: 1.14x faster                                                          |
| genshi_xml                 | 50.1 ms                                                         | 44.5 ms: 1.13x faster                                                          |
| xml_etree_parse            | 107 ms                                                          | 95.4 ms: 1.13x faster                                                          |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 433 ms: 1.12x faster                                                           |
| python_startup             | 28.3 ms                                                         | 25.4 ms: 1.11x faster                                                          |
| tomli_loads                | 1.71 sec                                                        | 1.55 sec: 1.10x faster                                                         |
| html5lib                   | 47.5 ms                                                         | 43.3 ms: 1.10x faster                                                          |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 423 ms: 1.08x faster                                                           |
| pprint_safe_repr           | 648 ms                                                          | 608 ms: 1.07x faster                                                           |
| pprint_pformat             | 1.33 sec                                                        | 1.25 sec: 1.06x faster                                                         |
| pycparser                  | 872 ms                                                          | 819 ms: 1.06x faster                                                           |
| connected_components       | 267 ms                                                          | 253 ms: 1.06x faster                                                           |
| genshi_text                | 21.5 ms                                                         | 20.4 ms: 1.05x faster                                                          |
| pylint                     | 227 ms                                                          | 216 ms: 1.05x faster                                                           |
| json_loads                 | 21.6 us                                                         | 20.7 us: 1.04x faster                                                          |
| telco                      | 6.96 ms                                                         | 6.68 ms: 1.04x faster                                                          |
| bench_mp_pool              | 90.6 ms                                                         | 87.0 ms: 1.04x faster                                                          |
| logging_format             | 8.72 us                                                         | 8.38 us: 1.04x faster                                                          |
| k_core                     | 1.38 sec                                                        | 1.33 sec: 1.03x faster                                                         |
| shortest_path              | 290 ms                                                          | 282 ms: 1.03x faster                                                           |
| sqlite_synth               | 1.95 us                                                         | 1.91 us: 1.03x faster                                                          |
| pidigits                   | 201 ms                                                          | 196 ms: 1.02x faster                                                           |
| fannkuch                   | 299 ms                                                          | 292 ms: 1.02x faster                                                           |
| logging_simple             | 7.99 us                                                         | 7.80 us: 1.02x faster                                                          |
| python_startup_no_site     | 19.7 ms                                                         | 19.2 ms: 1.02x faster                                                          |
| 2to3                       | 250 ms                                                          | 245 ms: 1.02x faster                                                           |
| bpe_tokeniser              | 3.46 sec                                                        | 3.40 sec: 1.02x faster                                                         |
| spectral_norm              | 69.4 ms                                                         | 68.1 ms: 1.02x faster                                                          |
| json                       | 4.27 ms                                                         | 4.21 ms: 1.02x faster                                                          |
| float                      | 54.6 ms                                                         | 53.8 ms: 1.01x faster                                                          |
| docutils                   | 1.78 sec                                                        | 1.79 sec: 1.01x slower                                                         |
| sphinx                     | 719 ms                                                          | 725 ms: 1.01x slower                                                           |
| sympy_str                  | 212 ms                                                          | 214 ms: 1.01x slower                                                           |
| sympy_expand               | 373 ms                                                          | 379 ms: 1.02x slower                                                           |
| xml_etree_iterparse        | 62.6 ms                                                         | 63.6 ms: 1.02x slower                                                          |
| pathlib                    | 82.9 ms                                                         | 84.3 ms: 1.02x slower                                                          |
| sympy_integrate            | 15.0 ms                                                         | 15.3 ms: 1.02x slower                                                          |
| sqlglot_normalize          | 216 ms                                                          | 221 ms: 1.02x slower                                                           |
| sqlglot_optimize           | 41.4 ms                                                         | 42.3 ms: 1.02x slower                                                          |
| gc_traversal               | 1.75 ms                                                         | 1.79 ms: 1.02x slower                                                          |
| sqlglot_parse              | 1.00 ms                                                         | 1.03 ms: 1.03x slower                                                          |
| regex_dna                  | 114 ms                                                          | 117 ms: 1.03x slower                                                           |
| sqlglot_transpile          | 1.24 ms                                                         | 1.27 ms: 1.03x slower                                                          |
| dulwich_log                | 48.8 ms                                                         | 50.3 ms: 1.03x slower                                                          |
| asyncio_websockets         | 363 ms                                                          | 377 ms: 1.04x slower                                                           |
| pyflate                    | 320 ms                                                          | 333 ms: 1.04x slower                                                           |
| nbody                      | 80.0 ms                                                         | 83.5 ms: 1.04x slower                                                          |
| unpickle_pure_python       | 160 us                                                          | 168 us: 1.05x slower                                                           |
| django_template            | 29.8 ms                                                         | 31.2 ms: 1.05x slower                                                          |
| mdp                        | 1.62 sec                                                        | 1.71 sec: 1.05x slower                                                         |
| scimark_sparse_mat_mult    | 2.84 ms                                                         | 2.98 ms: 1.05x slower                                                          |
| crypto_pyaes               | 56.9 ms                                                         | 59.9 ms: 1.05x slower                                                          |
| mako                       | 7.09 ms                                                         | 7.48 ms: 1.06x slower                                                          |
| scimark_monte_carlo        | 47.7 ms                                                         | 50.5 ms: 1.06x slower                                                          |
| nqueens                    | 72.1 ms                                                         | 76.6 ms: 1.06x slower                                                          |
| richards                   | 32.7 ms                                                         | 34.8 ms: 1.07x slower                                                          |
| chaos                      | 50.2 ms                                                         | 53.9 ms: 1.07x slower                                                          |
| async_generators           | 270 ms                                                          | 290 ms: 1.07x slower                                                           |
| xml_etree_generate         | 61.4 ms                                                         | 66.3 ms: 1.08x slower                                                          |
| deltablue                  | 2.33 ms                                                         | 2.52 ms: 1.08x slower                                                          |
| comprehensions             | 12.5 us                                                         | 13.5 us: 1.08x slower                                                          |
| scimark_fft                | 205 ms                                                          | 222 ms: 1.08x slower                                                           |
| meteor_contest             | 74.6 ms                                                         | 80.9 ms: 1.08x slower                                                          |
| scimark_sor                | 85.9 ms                                                         | 93.1 ms: 1.08x slower                                                          |
| xml_etree_process          | 44.2 ms                                                         | 48.0 ms: 1.09x slower                                                          |
| pickle_pure_python         | 231 us                                                          | 252 us: 1.09x slower                                                           |
| scimark_lu                 | 60.2 ms                                                         | 66.0 ms: 1.10x slower                                                          |
| hexiom                     | 4.44 ms                                                         | 4.91 ms: 1.11x slower                                                          |
| richards_super             | 36.7 ms                                                         | 40.7 ms: 1.11x slower                                                          |
| generators                 | 21.8 ms                                                         | 24.5 ms: 1.13x slower                                                          |
| logging_silent             | 60.3 ns                                                         | 69.7 ns: 1.15x slower                                                          |
| raytrace                   | 201 ms                                                          | 235 ms: 1.17x slower                                                           |
| many_optionals             | 436 us                                                          | 523 us: 1.20x slower                                                           |
| json_dumps                 | 7.30 ms                                                         | 9.09 ms: 1.25x slower                                                          |
| subparsers                 | 14.8 ms                                                         | 20.4 ms: 1.38x slower                                                          |
| Geometric mean             | (ref)                                                           | 1.05x faster                                                                   |

Benchmark hidden because not significant (7): regex_v8, create_gc_cycles, regex_compile, sympy_sum, coroutines, typing_runtime_protocols, bench_thread_pool
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (1) of results/bm-20250105-3.14.0a3+-82b905d/bm-20250105-pythonperf1_win32-x86-kumaraditya303-future_iter-3.14.0a3+-82b905d.json: mypy2

- Geometric mean (including insignificant results): 1.055x faster

# HPT report

- Reliability score: 71.13% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown