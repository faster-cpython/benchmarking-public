# Results vs. 3.13.0

- fork: Fidget-Spinner
- ref: tail_call
- machine: windows-x86
- commit hash: f1d3190
- commit date: 2025-01-07
- overall geometric mean: 1.043x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250107-pythonperf1_win32-x86-Fidget%2dSpinner-tail_call-3.14.0a3+-f1d3190 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 250 ms                                                          | 277 ms: 1.11x slower                                                           |
| docutils       | 1.78 sec                                                        | 1.95 sec: 1.10x slower                                                         |
| html5lib       | 47.5 ms                                                         | 48.9 ms: 1.03x slower                                                          |
| sphinx         | 719 ms                                                          | 795 ms: 1.11x slower                                                           |
| Geometric mean | (ref)                                                           | 1.09x slower                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250107-pythonperf1_win32-x86-Fidget%2dSpinner-tail_call-3.14.0a3+-f1d3190 |
|---------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_none           | 245 ms                                                          | 213 ms: 1.15x faster                                                           |
| async_tree_memoization_tg | 282 ms                                                          | 246 ms: 1.15x faster                                                           |
| async_tree_io             | 526 ms                                                          | 460 ms: 1.14x faster                                                           |
| async_tree_memoization    | 297 ms                                                          | 266 ms: 1.12x faster                                                           |
| async_tree_none_tg        | 214 ms                                                          | 194 ms: 1.10x faster                                                           |
| async_tree_io_tg          | 494 ms                                                          | 454 ms: 1.09x faster                                                           |
| asyncio_websockets        | 363 ms                                                          | 338 ms: 1.07x faster                                                           |
| async_tree_cpu_io_mixed   | 484 ms                                                          | 474 ms: 1.02x faster                                                           |
| coroutines                | 16.2 ms                                                         | 17.7 ms: 1.09x slower                                                          |
| async_generators          | 270 ms                                                          | 312 ms: 1.16x slower                                                           |
| Geometric mean            | (ref)                                                           | 1.05x faster                                                                   |

Benchmark hidden because not significant (1): async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250107-pythonperf1_win32-x86-Fidget%2dSpinner-tail_call-3.14.0a3+-f1d3190 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pidigits       | 201 ms                                                          | 215 ms: 1.07x slower                                                           |
| float          | 54.6 ms                                                         | 58.8 ms: 1.08x slower                                                          |
| nbody          | 80.0 ms                                                         | 95.9 ms: 1.20x slower                                                          |
| Geometric mean | (ref)                                                           | 1.12x slower                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250107-pythonperf1_win32-x86-Fidget%2dSpinner-tail_call-3.14.0a3+-f1d3190 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_effbot   | 1.80 ms                                                         | 1.94 ms: 1.08x slower                                                          |
| regex_compile  | 101 ms                                                          | 112 ms: 1.11x slower                                                           |
| regex_dna      | 114 ms                                                          | 126 ms: 1.11x slower                                                           |
| Geometric mean | (ref)                                                           | 1.09x slower                                                                   |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250107-pythonperf1_win32-x86-Fidget%2dSpinner-tail_call-3.14.0a3+-f1d3190 |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| json_loads           | 21.6 us                                                         | 20.8 us: 1.04x faster                                                          |
| tomli_loads          | 1.71 sec                                                        | 1.79 sec: 1.04x slower                                                         |
| xml_etree_parse      | 107 ms                                                          | 112 ms: 1.05x slower                                                           |
| xml_etree_iterparse  | 62.6 ms                                                         | 72.9 ms: 1.17x slower                                                          |
| json_dumps           | 7.30 ms                                                         | 8.57 ms: 1.17x slower                                                          |
| unpickle_pure_python | 160 us                                                          | 195 us: 1.22x slower                                                           |
| xml_etree_generate   | 61.4 ms                                                         | 75.7 ms: 1.23x slower                                                          |
| xml_etree_process    | 44.2 ms                                                         | 55.4 ms: 1.25x slower                                                          |
| pickle_pure_python   | 231 us                                                          | 301 us: 1.30x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.15x slower                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250107-pythonperf1_win32-x86-Fidget%2dSpinner-tail_call-3.14.0a3+-f1d3190 |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 28.3 ms                                                         | 28.1 ms: 1.01x faster                                                          |
| python_startup_no_site | 19.7 ms                                                         | 20.8 ms: 1.06x slower                                                          |
| Geometric mean         | (ref)                                                           | 1.02x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250107-pythonperf1_win32-x86-Fidget%2dSpinner-tail_call-3.14.0a3+-f1d3190 |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| genshi_xml      | 50.1 ms                                                         | 48.5 ms: 1.03x faster                                                          |
| genshi_text     | 21.5 ms                                                         | 22.8 ms: 1.06x slower                                                          |
| django_template | 29.8 ms                                                         | 36.1 ms: 1.21x slower                                                          |
| mako            | 7.09 ms                                                         | 8.72 ms: 1.23x slower                                                          |
| Geometric mean  | (ref)                                                           | 1.11x slower                                                                   |

All benchmarks:
===============

| Benchmark                 | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250107-pythonperf1_win32-x86-Fidget%2dSpinner-tail_call-3.14.0a3+-f1d3190 |
|---------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| thrift                    | 9.98 ms                                                         | 728 us: 13.70x faster                                                          |
| coverage                  | 324 ms                                                          | 58.1 ms: 5.58x faster                                                          |
| deepcopy                  | 314 us                                                          | 247 us: 1.27x faster                                                           |
| async_tree_none           | 245 ms                                                          | 213 ms: 1.15x faster                                                           |
| async_tree_memoization_tg | 282 ms                                                          | 246 ms: 1.15x faster                                                           |
| async_tree_io             | 526 ms                                                          | 460 ms: 1.14x faster                                                           |
| deepcopy_reduce           | 2.92 us                                                         | 2.59 us: 1.12x faster                                                          |
| async_tree_memoization    | 297 ms                                                          | 266 ms: 1.12x faster                                                           |
| async_tree_none_tg        | 214 ms                                                          | 194 ms: 1.10x faster                                                           |
| telco                     | 6.96 ms                                                         | 6.39 ms: 1.09x faster                                                          |
| async_tree_io_tg          | 494 ms                                                          | 454 ms: 1.09x faster                                                           |
| asyncio_websockets        | 363 ms                                                          | 338 ms: 1.07x faster                                                           |
| deepcopy_memo             | 25.4 us                                                         | 24.0 us: 1.06x faster                                                          |
| json_loads                | 21.6 us                                                         | 20.8 us: 1.04x faster                                                          |
| genshi_xml                | 50.1 ms                                                         | 48.5 ms: 1.03x faster                                                          |
| async_tree_cpu_io_mixed   | 484 ms                                                          | 474 ms: 1.02x faster                                                           |
| python_startup            | 28.3 ms                                                         | 28.1 ms: 1.01x faster                                                          |
| sqlite_synth              | 1.95 us                                                         | 1.98 us: 1.01x slower                                                          |
| fannkuch                  | 299 ms                                                          | 307 ms: 1.03x slower                                                           |
| sympy_expand              | 373 ms                                                          | 383 ms: 1.03x slower                                                           |
| html5lib                  | 47.5 ms                                                         | 48.9 ms: 1.03x slower                                                          |
| go                        | 109 ms                                                          | 113 ms: 1.04x slower                                                           |
| dulwich_log               | 48.8 ms                                                         | 50.5 ms: 1.04x slower                                                          |
| tomli_loads               | 1.71 sec                                                        | 1.79 sec: 1.04x slower                                                         |
| pathlib                   | 82.9 ms                                                         | 86.4 ms: 1.04x slower                                                          |
| pylint                    | 227 ms                                                          | 237 ms: 1.05x slower                                                           |
| xml_etree_parse           | 107 ms                                                          | 112 ms: 1.05x slower                                                           |
| k_core                    | 1.38 sec                                                        | 1.44 sec: 1.05x slower                                                         |
| sympy_str                 | 212 ms                                                          | 222 ms: 1.05x slower                                                           |
| logging_format            | 8.72 us                                                         | 9.16 us: 1.05x slower                                                          |
| pprint_safe_repr          | 648 ms                                                          | 683 ms: 1.05x slower                                                           |
| bpe_tokeniser             | 3.46 sec                                                        | 3.65 sec: 1.06x slower                                                         |
| sympy_sum                 | 106 ms                                                          | 112 ms: 1.06x slower                                                           |
| python_startup_no_site    | 19.7 ms                                                         | 20.8 ms: 1.06x slower                                                          |
| pprint_pformat            | 1.33 sec                                                        | 1.41 sec: 1.06x slower                                                         |
| pycparser                 | 872 ms                                                          | 925 ms: 1.06x slower                                                           |
| genshi_text               | 21.5 ms                                                         | 22.8 ms: 1.06x slower                                                          |
| logging_simple            | 7.99 us                                                         | 8.54 us: 1.07x slower                                                          |
| scimark_sparse_mat_mult   | 2.84 ms                                                         | 3.04 ms: 1.07x slower                                                          |
| pidigits                  | 201 ms                                                          | 215 ms: 1.07x slower                                                           |
| float                     | 54.6 ms                                                         | 58.8 ms: 1.08x slower                                                          |
| regex_effbot              | 1.80 ms                                                         | 1.94 ms: 1.08x slower                                                          |
| bench_thread_pool         | 1.00 ms                                                         | 1.08 ms: 1.08x slower                                                          |
| connected_components      | 267 ms                                                          | 288 ms: 1.08x slower                                                           |
| shortest_path             | 290 ms                                                          | 314 ms: 1.08x slower                                                           |
| spectral_norm             | 69.4 ms                                                         | 75.6 ms: 1.09x slower                                                          |
| coroutines                | 16.2 ms                                                         | 17.7 ms: 1.09x slower                                                          |
| bench_mp_pool             | 90.6 ms                                                         | 99.3 ms: 1.10x slower                                                          |
| docutils                  | 1.78 sec                                                        | 1.95 sec: 1.10x slower                                                         |
| sphinx                    | 719 ms                                                          | 795 ms: 1.11x slower                                                           |
| 2to3                      | 250 ms                                                          | 277 ms: 1.11x slower                                                           |
| regex_compile             | 101 ms                                                          | 112 ms: 1.11x slower                                                           |
| sympy_integrate           | 15.0 ms                                                         | 16.6 ms: 1.11x slower                                                          |
| regex_dna                 | 114 ms                                                          | 126 ms: 1.11x slower                                                           |
| scimark_monte_carlo       | 47.7 ms                                                         | 53.5 ms: 1.12x slower                                                          |
| create_gc_cycles          | 1.06 ms                                                         | 1.20 ms: 1.14x slower                                                          |
| typing_runtime_protocols  | 138 us                                                          | 157 us: 1.14x slower                                                           |
| sqlglot_parse             | 1.00 ms                                                         | 1.16 ms: 1.15x slower                                                          |
| async_generators          | 270 ms                                                          | 312 ms: 1.16x slower                                                           |
| sqlglot_normalize         | 216 ms                                                          | 250 ms: 1.16x slower                                                           |
| scimark_fft               | 205 ms                                                          | 237 ms: 1.16x slower                                                           |
| sqlglot_optimize          | 41.4 ms                                                         | 48.0 ms: 1.16x slower                                                          |
| pyflate                   | 320 ms                                                          | 371 ms: 1.16x slower                                                           |
| scimark_sor               | 85.9 ms                                                         | 99.7 ms: 1.16x slower                                                          |
| xml_etree_iterparse       | 62.6 ms                                                         | 72.9 ms: 1.17x slower                                                          |
| sqlglot_transpile         | 1.24 ms                                                         | 1.44 ms: 1.17x slower                                                          |
| meteor_contest            | 74.6 ms                                                         | 87.0 ms: 1.17x slower                                                          |
| json_dumps                | 7.30 ms                                                         | 8.57 ms: 1.17x slower                                                          |
| chaos                     | 50.2 ms                                                         | 59.5 ms: 1.19x slower                                                          |
| crypto_pyaes              | 56.9 ms                                                         | 67.6 ms: 1.19x slower                                                          |
| nbody                     | 80.0 ms                                                         | 95.9 ms: 1.20x slower                                                          |
| nqueens                   | 72.1 ms                                                         | 86.8 ms: 1.20x slower                                                          |
| django_template           | 29.8 ms                                                         | 36.1 ms: 1.21x slower                                                          |
| unpickle_pure_python      | 160 us                                                          | 195 us: 1.22x slower                                                           |
| mdp                       | 1.62 sec                                                        | 1.99 sec: 1.23x slower                                                         |
| mako                      | 7.09 ms                                                         | 8.72 ms: 1.23x slower                                                          |
| xml_etree_generate        | 61.4 ms                                                         | 75.7 ms: 1.23x slower                                                          |
| deltablue                 | 2.33 ms                                                         | 2.90 ms: 1.24x slower                                                          |
| xml_etree_process         | 44.2 ms                                                         | 55.4 ms: 1.25x slower                                                          |
| scimark_lu                | 60.2 ms                                                         | 75.9 ms: 1.26x slower                                                          |
| raytrace                  | 201 ms                                                          | 255 ms: 1.27x slower                                                           |
| many_optionals            | 436 us                                                          | 556 us: 1.28x slower                                                           |
| pickle_pure_python        | 231 us                                                          | 301 us: 1.30x slower                                                           |
| hexiom                    | 4.44 ms                                                         | 5.91 ms: 1.33x slower                                                          |
| comprehensions            | 12.5 us                                                         | 16.7 us: 1.33x slower                                                          |
| richards                  | 32.7 ms                                                         | 43.7 ms: 1.34x slower                                                          |
| richards_super            | 36.7 ms                                                         | 49.3 ms: 1.34x slower                                                          |
| gc_traversal              | 1.75 ms                                                         | 2.38 ms: 1.36x slower                                                          |
| logging_silent            | 60.3 ns                                                         | 82.3 ns: 1.37x slower                                                          |
| generators                | 21.8 ms                                                         | 30.3 ms: 1.39x slower                                                          |
| subparsers                | 14.8 ms                                                         | 21.1 ms: 1.43x slower                                                          |
| Geometric mean            | (ref)                                                           | 1.05x slower                                                                   |

Benchmark hidden because not significant (3): json, async_tree_cpu_io_mixed_tg, regex_v8
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http

- Geometric mean (including insignificant results): 1.043x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.06x
- 95% likely to have a slowdown of 1.05x
- 99% likely to have a slowdown of 1.05x

# Memory
- memory change: unknown