# Results vs. 3.13.0

- fork: python
- ref: 79b7cab50a3292a1c014
- machine: windows-x86
- commit hash: 79b7cab
- commit date: 2024-12-07
- overall geometric mean: 1.049x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241207-pythonperf1_win32-x86-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 250 ms                                                          | 259 ms: 1.04x slower                                                            |
| docutils       | 1.78 sec                                                        | 1.95 sec: 1.10x slower                                                          |
| html5lib       | 47.5 ms                                                         | 49.1 ms: 1.03x slower                                                           |
| sphinx         | 719 ms                                                          | 793 ms: 1.10x slower                                                            |
| Geometric mean | (ref)                                                           | 1.07x slower                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241207-pythonperf1_win32-x86-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab |
|---------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_memoization_tg | 282 ms                                                          | 252 ms: 1.12x faster                                                            |
| async_tree_io             | 526 ms                                                          | 480 ms: 1.10x faster                                                            |
| async_tree_io_tg          | 494 ms                                                          | 451 ms: 1.10x faster                                                            |
| async_tree_none           | 245 ms                                                          | 228 ms: 1.07x faster                                                            |
| async_tree_none_tg        | 214 ms                                                          | 200 ms: 1.07x faster                                                            |
| async_tree_memoization    | 297 ms                                                          | 282 ms: 1.05x faster                                                            |
| asyncio_websockets        | 363 ms                                                          | 357 ms: 1.02x faster                                                            |
| async_tree_cpu_io_mixed   | 484 ms                                                          | 480 ms: 1.01x faster                                                            |
| coroutines                | 16.2 ms                                                         | 16.6 ms: 1.02x slower                                                           |
| async_generators          | 270 ms                                                          | 326 ms: 1.21x slower                                                            |
| Geometric mean            | (ref)                                                           | 1.03x faster                                                                    |

Benchmark hidden because not significant (1): async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241207-pythonperf1_win32-x86-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pidigits       | 201 ms                                                          | 200 ms: 1.00x faster                                                            |
| float          | 54.6 ms                                                         | 57.5 ms: 1.05x slower                                                           |
| nbody          | 80.0 ms                                                         | 99.4 ms: 1.24x slower                                                           |
| Geometric mean | (ref)                                                           | 1.09x slower                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241207-pythonperf1_win32-x86-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_effbot   | 1.80 ms                                                         | 1.59 ms: 1.13x faster                                                           |
| regex_dna      | 114 ms                                                          | 115 ms: 1.02x slower                                                            |
| regex_compile  | 101 ms                                                          | 115 ms: 1.14x slower                                                            |
| Geometric mean | (ref)                                                           | 1.01x faster                                                                    |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241207-pythonperf1_win32-x86-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| json_loads           | 21.6 us                                                         | 20.5 us: 1.05x faster                                                           |
| xml_etree_parse      | 107 ms                                                          | 104 ms: 1.03x faster                                                            |
| xml_etree_iterparse  | 62.6 ms                                                         | 63.4 ms: 1.01x slower                                                           |
| tomli_loads          | 1.71 sec                                                        | 1.85 sec: 1.08x slower                                                          |
| xml_etree_generate   | 61.4 ms                                                         | 71.5 ms: 1.16x slower                                                           |
| xml_etree_process    | 44.2 ms                                                         | 53.3 ms: 1.21x slower                                                           |
| json_dumps           | 7.30 ms                                                         | 9.01 ms: 1.23x slower                                                           |
| unpickle_pure_python | 160 us                                                          | 203 us: 1.27x slower                                                            |
| pickle_pure_python   | 231 us                                                          | 304 us: 1.31x slower                                                            |
| Geometric mean       | (ref)                                                           | 1.13x slower                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241207-pythonperf1_win32-x86-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup | 28.3 ms                                                         | 26.3 ms: 1.08x faster                                                           |
| Geometric mean | (ref)                                                           | 1.04x faster                                                                    |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241207-pythonperf1_win32-x86-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                         | 7.31 ms: 1.03x slower                                                           |
| genshi_xml      | 50.1 ms                                                         | 57.1 ms: 1.14x slower                                                           |
| genshi_text     | 21.5 ms                                                         | 26.0 ms: 1.21x slower                                                           |
| django_template | 29.8 ms                                                         | 36.8 ms: 1.24x slower                                                           |
| Geometric mean  | (ref)                                                           | 1.15x slower                                                                    |

All benchmarks:
===============

| Benchmark                 | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241207-pythonperf1_win32-x86-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab |
|---------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| thrift                    | 9.98 ms                                                         | 776 us: 12.86x faster                                                           |
| coverage                  | 324 ms                                                          | 54.7 ms: 5.92x faster                                                           |
| sqlglot_normalize         | 216 ms                                                          | 110 ms: 1.98x faster                                                            |
| regex_effbot              | 1.80 ms                                                         | 1.59 ms: 1.13x faster                                                           |
| async_tree_memoization_tg | 282 ms                                                          | 252 ms: 1.12x faster                                                            |
| deepcopy                  | 314 us                                                          | 281 us: 1.12x faster                                                            |
| async_tree_io             | 526 ms                                                          | 480 ms: 1.10x faster                                                            |
| async_tree_io_tg          | 494 ms                                                          | 451 ms: 1.10x faster                                                            |
| create_gc_cycles          | 1.06 ms                                                         | 981 us: 1.08x faster                                                            |
| python_startup            | 28.3 ms                                                         | 26.3 ms: 1.08x faster                                                           |
| async_tree_none           | 245 ms                                                          | 228 ms: 1.07x faster                                                            |
| async_tree_none_tg        | 214 ms                                                          | 200 ms: 1.07x faster                                                            |
| json_loads                | 21.6 us                                                         | 20.5 us: 1.05x faster                                                           |
| async_tree_memoization    | 297 ms                                                          | 282 ms: 1.05x faster                                                            |
| deepcopy_memo             | 25.4 us                                                         | 24.3 us: 1.04x faster                                                           |
| bench_mp_pool             | 90.6 ms                                                         | 87.0 ms: 1.04x faster                                                           |
| xml_etree_parse           | 107 ms                                                          | 104 ms: 1.03x faster                                                            |
| deepcopy_reduce           | 2.92 us                                                         | 2.85 us: 1.02x faster                                                           |
| pathlib                   | 82.9 ms                                                         | 81.4 ms: 1.02x faster                                                           |
| asyncio_websockets        | 363 ms                                                          | 357 ms: 1.02x faster                                                            |
| async_tree_cpu_io_mixed   | 484 ms                                                          | 480 ms: 1.01x faster                                                            |
| pidigits                  | 201 ms                                                          | 200 ms: 1.00x faster                                                            |
| xml_etree_iterparse       | 62.6 ms                                                         | 63.4 ms: 1.01x slower                                                           |
| regex_dna                 | 114 ms                                                          | 115 ms: 1.02x slower                                                            |
| sqlite_synth              | 1.95 us                                                         | 1.99 us: 1.02x slower                                                           |
| coroutines                | 16.2 ms                                                         | 16.6 ms: 1.02x slower                                                           |
| bench_thread_pool         | 1.00 ms                                                         | 1.03 ms: 1.03x slower                                                           |
| mako                      | 7.09 ms                                                         | 7.31 ms: 1.03x slower                                                           |
| telco                     | 6.96 ms                                                         | 7.19 ms: 1.03x slower                                                           |
| html5lib                  | 47.5 ms                                                         | 49.1 ms: 1.03x slower                                                           |
| json                      | 4.27 ms                                                         | 4.43 ms: 1.04x slower                                                           |
| 2to3                      | 250 ms                                                          | 259 ms: 1.04x slower                                                            |
| logging_format            | 8.72 us                                                         | 9.07 us: 1.04x slower                                                           |
| pycparser                 | 872 ms                                                          | 913 ms: 1.05x slower                                                            |
| float                     | 54.6 ms                                                         | 57.5 ms: 1.05x slower                                                           |
| logging_simple            | 7.99 us                                                         | 8.42 us: 1.05x slower                                                           |
| dulwich_log               | 48.8 ms                                                         | 52.0 ms: 1.07x slower                                                           |
| connected_components      | 267 ms                                                          | 288 ms: 1.08x slower                                                            |
| tomli_loads               | 1.71 sec                                                        | 1.85 sec: 1.08x slower                                                          |
| shortest_path             | 290 ms                                                          | 316 ms: 1.09x slower                                                            |
| sympy_sum                 | 106 ms                                                          | 115 ms: 1.09x slower                                                            |
| sympy_expand              | 373 ms                                                          | 408 ms: 1.09x slower                                                            |
| docutils                  | 1.78 sec                                                        | 1.95 sec: 1.10x slower                                                          |
| sphinx                    | 719 ms                                                          | 793 ms: 1.10x slower                                                            |
| bpe_tokeniser             | 3.46 sec                                                        | 3.84 sec: 1.11x slower                                                          |
| sympy_str                 | 212 ms                                                          | 235 ms: 1.11x slower                                                            |
| go                        | 109 ms                                                          | 121 ms: 1.11x slower                                                            |
| fannkuch                  | 299 ms                                                          | 335 ms: 1.12x slower                                                            |
| pprint_safe_repr          | 648 ms                                                          | 732 ms: 1.13x slower                                                            |
| scimark_sparse_mat_mult   | 2.84 ms                                                         | 3.21 ms: 1.13x slower                                                           |
| pprint_pformat            | 1.33 sec                                                        | 1.51 sec: 1.13x slower                                                          |
| regex_compile             | 101 ms                                                          | 115 ms: 1.14x slower                                                            |
| genshi_xml                | 50.1 ms                                                         | 57.1 ms: 1.14x slower                                                           |
| mdp                       | 1.62 sec                                                        | 1.85 sec: 1.14x slower                                                          |
| spectral_norm             | 69.4 ms                                                         | 79.9 ms: 1.15x slower                                                           |
| xml_etree_generate        | 61.4 ms                                                         | 71.5 ms: 1.16x slower                                                           |
| crypto_pyaes              | 56.9 ms                                                         | 66.6 ms: 1.17x slower                                                           |
| scimark_sor               | 85.9 ms                                                         | 102 ms: 1.18x slower                                                            |
| sqlglot_parse             | 1.00 ms                                                         | 1.19 ms: 1.19x slower                                                           |
| sqlglot_transpile         | 1.24 ms                                                         | 1.47 ms: 1.19x slower                                                           |
| scimark_lu                | 60.2 ms                                                         | 72.2 ms: 1.20x slower                                                           |
| scimark_fft               | 205 ms                                                          | 246 ms: 1.20x slower                                                            |
| meteor_contest            | 74.6 ms                                                         | 89.8 ms: 1.20x slower                                                           |
| xml_etree_process         | 44.2 ms                                                         | 53.3 ms: 1.21x slower                                                           |
| async_generators          | 270 ms                                                          | 326 ms: 1.21x slower                                                            |
| genshi_text               | 21.5 ms                                                         | 26.0 ms: 1.21x slower                                                           |
| typing_runtime_protocols  | 138 us                                                          | 166 us: 1.21x slower                                                            |
| sympy_integrate           | 15.0 ms                                                         | 18.1 ms: 1.21x slower                                                           |
| pyflate                   | 320 ms                                                          | 391 ms: 1.22x slower                                                            |
| json_dumps                | 7.30 ms                                                         | 9.01 ms: 1.23x slower                                                           |
| django_template           | 29.8 ms                                                         | 36.8 ms: 1.24x slower                                                           |
| nbody                     | 80.0 ms                                                         | 99.4 ms: 1.24x slower                                                           |
| sqlglot_optimize          | 41.4 ms                                                         | 51.7 ms: 1.25x slower                                                           |
| unpickle_pure_python      | 160 us                                                          | 203 us: 1.27x slower                                                            |
| many_optionals            | 436 us                                                          | 565 us: 1.29x slower                                                            |
| chaos                     | 50.2 ms                                                         | 65.1 ms: 1.30x slower                                                           |
| scimark_monte_carlo       | 47.7 ms                                                         | 61.9 ms: 1.30x slower                                                           |
| pickle_pure_python        | 231 us                                                          | 304 us: 1.31x slower                                                            |
| richards_super            | 36.7 ms                                                         | 49.3 ms: 1.34x slower                                                           |
| richards                  | 32.7 ms                                                         | 44.4 ms: 1.36x slower                                                           |
| deltablue                 | 2.33 ms                                                         | 3.19 ms: 1.37x slower                                                           |
| logging_silent            | 60.3 ns                                                         | 83.1 ns: 1.38x slower                                                           |
| nqueens                   | 72.1 ms                                                         | 99.5 ms: 1.38x slower                                                           |
| subparsers                | 14.8 ms                                                         | 21.5 ms: 1.46x slower                                                           |
| comprehensions            | 12.5 us                                                         | 18.7 us: 1.49x slower                                                           |
| raytrace                  | 201 ms                                                          | 301 ms: 1.50x slower                                                            |
| hexiom                    | 4.44 ms                                                         | 7.02 ms: 1.58x slower                                                           |
| generators                | 21.8 ms                                                         | 37.8 ms: 1.74x slower                                                           |
| Geometric mean            | (ref)                                                           | 1.05x slower                                                                    |

Benchmark hidden because not significant (6): regex_v8, python_startup_no_site, async_tree_cpu_io_mixed_tg, gc_traversal, k_core, pylint
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http

- Geometric mean (including insignificant results): 1.049x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.07x
- 95% likely to have a slowdown of 1.06x
- 99% likely to have a slowdown of 1.04x

# Memory
- memory change: unknown