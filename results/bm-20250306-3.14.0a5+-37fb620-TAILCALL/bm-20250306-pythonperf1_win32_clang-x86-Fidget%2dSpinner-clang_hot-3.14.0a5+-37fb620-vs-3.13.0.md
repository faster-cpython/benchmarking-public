# Results vs. 3.13.0

- fork: Fidget-Spinner
- ref: clang_hot
- machine: windows-x86
- commit hash: 37fb620
- commit date: 2025-03-06
- overall geometric mean: 1.077x faster
- HPT reliability: 93.04%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250306-pythonperf1_win32-x86-Fidget%2dSpinner-clang_hot-3.14.0a5+-37fb620 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| docutils       | 1.78 sec                                                        | 1.82 sec: 1.02x slower                                                         |
| html5lib       | 47.5 ms                                                         | 44.8 ms: 1.06x faster                                                          |
| sphinx         | 719 ms                                                          | 740 ms: 1.03x slower                                                           |
| Geometric mean | (ref)                                                           | 1.00x faster                                                                   |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250306-pythonperf1_win32-x86-Fidget%2dSpinner-clang_hot-3.14.0a5+-37fb620 |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_none            | 245 ms                                                          | 186 ms: 1.31x faster                                                           |
| async_tree_memoization     | 297 ms                                                          | 229 ms: 1.29x faster                                                           |
| async_tree_io              | 526 ms                                                          | 410 ms: 1.28x faster                                                           |
| async_tree_memoization_tg  | 282 ms                                                          | 220 ms: 1.28x faster                                                           |
| async_tree_io_tg           | 494 ms                                                          | 399 ms: 1.24x faster                                                           |
| async_tree_none_tg         | 214 ms                                                          | 174 ms: 1.23x faster                                                           |
| coroutines                 | 16.2 ms                                                         | 14.0 ms: 1.16x faster                                                          |
| asyncio_websockets         | 363 ms                                                          | 333 ms: 1.09x faster                                                           |
| async_generators           | 270 ms                                                          | 248 ms: 1.09x faster                                                           |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 446 ms: 1.08x faster                                                           |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 442 ms: 1.03x faster                                                           |
| Geometric mean             | (ref)                                                           | 1.19x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250306-pythonperf1_win32-x86-Fidget%2dSpinner-clang_hot-3.14.0a5+-37fb620 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| float          | 54.6 ms                                                         | 48.6 ms: 1.12x faster                                                          |
| nbody          | 80.0 ms                                                         | 75.7 ms: 1.06x faster                                                          |
| pidigits       | 201 ms                                                          | 219 ms: 1.09x slower                                                           |
| Geometric mean | (ref)                                                           | 1.03x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250306-pythonperf1_win32-x86-Fidget%2dSpinner-clang_hot-3.14.0a5+-37fb620 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_compile  | 101 ms                                                          | 97.1 ms: 1.04x faster                                                          |
| regex_effbot   | 1.80 ms                                                         | 1.96 ms: 1.09x slower                                                          |
| regex_dna      | 114 ms                                                          | 128 ms: 1.13x slower                                                           |
| Geometric mean | (ref)                                                           | 1.05x slower                                                                   |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250306-pythonperf1_win32-x86-Fidget%2dSpinner-clang_hot-3.14.0a5+-37fb620 |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| tomli_loads          | 1.71 sec                                                        | 1.53 sec: 1.12x faster                                                         |
| unpickle_pure_python | 160 us                                                          | 166 us: 1.04x slower                                                           |
| xml_etree_parse      | 107 ms                                                          | 115 ms: 1.07x slower                                                           |
| json_dumps           | 7.30 ms                                                         | 7.86 ms: 1.08x slower                                                          |
| pickle_pure_python   | 231 us                                                          | 252 us: 1.09x slower                                                           |
| xml_etree_process    | 44.2 ms                                                         | 50.0 ms: 1.13x slower                                                          |
| xml_etree_generate   | 61.4 ms                                                         | 70.3 ms: 1.15x slower                                                          |
| xml_etree_iterparse  | 62.6 ms                                                         | 72.8 ms: 1.16x slower                                                          |
| Geometric mean       | (ref)                                                           | 1.06x slower                                                                   |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250306-pythonperf1_win32-x86-Fidget%2dSpinner-clang_hot-3.14.0a5+-37fb620 |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 28.3 ms                                                         | 29.7 ms: 1.05x slower                                                          |
| python_startup_no_site | 19.7 ms                                                         | 22.6 ms: 1.15x slower                                                          |
| Geometric mean         | (ref)                                                           | 1.10x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250306-pythonperf1_win32-x86-Fidget%2dSpinner-clang_hot-3.14.0a5+-37fb620 |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| genshi_xml      | 50.1 ms                                                         | 39.6 ms: 1.27x faster                                                          |
| genshi_text     | 21.5 ms                                                         | 18.3 ms: 1.18x faster                                                          |
| django_template | 29.8 ms                                                         | 31.0 ms: 1.04x slower                                                          |
| mako            | 7.09 ms                                                         | 8.56 ms: 1.21x slower                                                          |
| Geometric mean  | (ref)                                                           | 1.04x faster                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250306-pythonperf1_win32-x86-Fidget%2dSpinner-clang_hot-3.14.0a5+-37fb620 |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| thrift                     | 9.98 ms                                                         | 679 us: 14.70x faster                                                          |
| coverage                   | 324 ms                                                          | 57.1 ms: 5.68x faster                                                          |
| pathlib                    | 82.9 ms                                                         | 35.4 ms: 2.34x faster                                                          |
| deepcopy                   | 314 us                                                          | 212 us: 1.48x faster                                                           |
| deepcopy_reduce            | 2.92 us                                                         | 2.16 us: 1.35x faster                                                          |
| async_tree_none            | 245 ms                                                          | 186 ms: 1.31x faster                                                           |
| async_tree_memoization     | 297 ms                                                          | 229 ms: 1.29x faster                                                           |
| async_tree_io              | 526 ms                                                          | 410 ms: 1.28x faster                                                           |
| async_tree_memoization_tg  | 282 ms                                                          | 220 ms: 1.28x faster                                                           |
| deepcopy_memo              | 25.4 us                                                         | 19.9 us: 1.28x faster                                                          |
| genshi_xml                 | 50.1 ms                                                         | 39.6 ms: 1.27x faster                                                          |
| async_tree_io_tg           | 494 ms                                                          | 399 ms: 1.24x faster                                                           |
| async_tree_none_tg         | 214 ms                                                          | 174 ms: 1.23x faster                                                           |
| go                         | 109 ms                                                          | 90.3 ms: 1.20x faster                                                          |
| genshi_text                | 21.5 ms                                                         | 18.3 ms: 1.18x faster                                                          |
| pprint_safe_repr           | 648 ms                                                          | 558 ms: 1.16x faster                                                           |
| telco                      | 6.96 ms                                                         | 6.00 ms: 1.16x faster                                                          |
| coroutines                 | 16.2 ms                                                         | 14.0 ms: 1.16x faster                                                          |
| pprint_pformat             | 1.33 sec                                                        | 1.15 sec: 1.15x faster                                                         |
| float                      | 54.6 ms                                                         | 48.6 ms: 1.12x faster                                                          |
| tomli_loads                | 1.71 sec                                                        | 1.53 sec: 1.12x faster                                                         |
| spectral_norm              | 69.4 ms                                                         | 62.5 ms: 1.11x faster                                                          |
| generators                 | 21.8 ms                                                         | 19.9 ms: 1.10x faster                                                          |
| asyncio_websockets         | 363 ms                                                          | 333 ms: 1.09x faster                                                           |
| async_generators           | 270 ms                                                          | 248 ms: 1.09x faster                                                           |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 446 ms: 1.08x faster                                                           |
| sympy_expand               | 373 ms                                                          | 348 ms: 1.07x faster                                                           |
| sympy_str                  | 212 ms                                                          | 200 ms: 1.06x faster                                                           |
| html5lib                   | 47.5 ms                                                         | 44.8 ms: 1.06x faster                                                          |
| nbody                      | 80.0 ms                                                         | 75.7 ms: 1.06x faster                                                          |
| pycparser                  | 872 ms                                                          | 827 ms: 1.05x faster                                                           |
| scimark_sor                | 85.9 ms                                                         | 82.0 ms: 1.05x faster                                                          |
| pylint                     | 227 ms                                                          | 216 ms: 1.05x faster                                                           |
| scimark_sparse_mat_mult    | 2.84 ms                                                         | 2.73 ms: 1.04x faster                                                          |
| regex_compile              | 101 ms                                                          | 97.1 ms: 1.04x faster                                                          |
| deltablue                  | 2.33 ms                                                         | 2.25 ms: 1.04x faster                                                          |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 442 ms: 1.03x faster                                                           |
| logging_format             | 8.72 us                                                         | 8.46 us: 1.03x faster                                                          |
| sqlite_synth               | 1.95 us                                                         | 1.90 us: 1.03x faster                                                          |
| sympy_sum                  | 106 ms                                                          | 103 ms: 1.03x faster                                                           |
| sqlglot_parse              | 1.00 ms                                                         | 982 us: 1.02x faster                                                           |
| chaos                      | 50.2 ms                                                         | 49.5 ms: 1.01x faster                                                          |
| typing_runtime_protocols   | 138 us                                                          | 136 us: 1.01x faster                                                           |
| bpe_tokeniser              | 3.46 sec                                                        | 3.42 sec: 1.01x faster                                                         |
| sqlglot_transpile          | 1.24 ms                                                         | 1.22 ms: 1.01x faster                                                          |
| logging_simple             | 7.99 us                                                         | 8.06 us: 1.01x slower                                                          |
| shortest_path              | 290 ms                                                          | 293 ms: 1.01x slower                                                           |
| pyflate                    | 320 ms                                                          | 324 ms: 1.01x slower                                                           |
| nqueens                    | 72.1 ms                                                         | 73.2 ms: 1.02x slower                                                          |
| sympy_integrate            | 15.0 ms                                                         | 15.2 ms: 1.02x slower                                                          |
| json                       | 4.27 ms                                                         | 4.35 ms: 1.02x slower                                                          |
| sqlglot_optimize           | 41.4 ms                                                         | 42.2 ms: 1.02x slower                                                          |
| docutils                   | 1.78 sec                                                        | 1.82 sec: 1.02x slower                                                         |
| sphinx                     | 719 ms                                                          | 740 ms: 1.03x slower                                                           |
| unpickle_pure_python       | 160 us                                                          | 166 us: 1.04x slower                                                           |
| django_template            | 29.8 ms                                                         | 31.0 ms: 1.04x slower                                                          |
| raytrace                   | 201 ms                                                          | 211 ms: 1.05x slower                                                           |
| python_startup             | 28.3 ms                                                         | 29.7 ms: 1.05x slower                                                          |
| bench_mp_pool              | 90.6 ms                                                         | 95.5 ms: 1.05x slower                                                          |
| scimark_fft                | 205 ms                                                          | 216 ms: 1.06x slower                                                           |
| comprehensions             | 12.5 us                                                         | 13.2 us: 1.06x slower                                                          |
| xml_etree_parse            | 107 ms                                                          | 115 ms: 1.07x slower                                                           |
| json_dumps                 | 7.30 ms                                                         | 7.86 ms: 1.08x slower                                                          |
| pickle_pure_python         | 231 us                                                          | 252 us: 1.09x slower                                                           |
| regex_effbot               | 1.80 ms                                                         | 1.96 ms: 1.09x slower                                                          |
| pidigits                   | 201 ms                                                          | 219 ms: 1.09x slower                                                           |
| hexiom                     | 4.44 ms                                                         | 4.87 ms: 1.10x slower                                                          |
| meteor_contest             | 74.6 ms                                                         | 81.9 ms: 1.10x slower                                                          |
| logging_silent             | 60.3 ns                                                         | 66.7 ns: 1.11x slower                                                          |
| richards                   | 32.7 ms                                                         | 36.2 ms: 1.11x slower                                                          |
| richards_super             | 36.7 ms                                                         | 40.9 ms: 1.11x slower                                                          |
| mdp                        | 1.62 sec                                                        | 1.82 sec: 1.12x slower                                                         |
| crypto_pyaes               | 56.9 ms                                                         | 64.1 ms: 1.13x slower                                                          |
| regex_dna                  | 114 ms                                                          | 128 ms: 1.13x slower                                                           |
| xml_etree_process          | 44.2 ms                                                         | 50.0 ms: 1.13x slower                                                          |
| create_gc_cycles           | 1.06 ms                                                         | 1.20 ms: 1.13x slower                                                          |
| xml_etree_generate         | 61.4 ms                                                         | 70.3 ms: 1.15x slower                                                          |
| python_startup_no_site     | 19.7 ms                                                         | 22.6 ms: 1.15x slower                                                          |
| xml_etree_iterparse        | 62.6 ms                                                         | 72.8 ms: 1.16x slower                                                          |
| many_optionals             | 436 us                                                          | 511 us: 1.17x slower                                                           |
| scimark_lu                 | 60.2 ms                                                         | 71.8 ms: 1.19x slower                                                          |
| mako                       | 7.09 ms                                                         | 8.56 ms: 1.21x slower                                                          |
| gc_traversal               | 1.75 ms                                                         | 2.36 ms: 1.35x slower                                                          |
| subparsers                 | 14.8 ms                                                         | 20.1 ms: 1.36x slower                                                          |
| bench_thread_pool          | 1.00 ms                                                         | 1.36 ms: 1.36x slower                                                          |
| Geometric mean             | (ref)                                                           | 1.07x faster                                                                   |

Benchmark hidden because not significant (9): 2to3, sqlglot_normalize, connected_components, scimark_monte_carlo, json_loads, fannkuch, dulwich_log, k_core, regex_v8
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http

- Geometric mean (including insignificant results): 1.077x faster

# HPT report

- Reliability score: 93.04% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown