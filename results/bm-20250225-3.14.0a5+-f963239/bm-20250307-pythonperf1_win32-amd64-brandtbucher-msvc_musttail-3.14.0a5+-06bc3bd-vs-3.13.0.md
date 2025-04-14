# Results vs. 3.13.0

- fork: brandtbucher
- ref: msvc_musttail
- machine: windows-amd64
- commit hash: 06bc3bd
- commit date: 2025-03-07
- overall geometric mean: 1.203x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.13x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250307-pythonperf1_win32-amd64-brandtbucher-msvc_musttail-3.14.0a5+-06bc3bd |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 250 ms                                                          | 231 ms: 1.08x faster                                                             |
| docutils       | 1.78 sec                                                        | 1.77 sec: 1.01x faster                                                           |
| html5lib       | 47.5 ms                                                         | 38.8 ms: 1.23x faster                                                            |
| sphinx         | 719 ms                                                          | 702 ms: 1.02x faster                                                             |
| Geometric mean | (ref)                                                           | 1.08x faster                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250307-pythonperf1_win32-amd64-brandtbucher-msvc_musttail-3.14.0a5+-06bc3bd |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_memoization     | 297 ms                                                          | 210 ms: 1.41x faster                                                             |
| async_tree_none            | 245 ms                                                          | 174 ms: 1.41x faster                                                             |
| async_tree_io              | 526 ms                                                          | 384 ms: 1.37x faster                                                             |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 359 ms: 1.35x faster                                                             |
| async_tree_memoization_tg  | 282 ms                                                          | 210 ms: 1.34x faster                                                             |
| coroutines                 | 16.2 ms                                                         | 12.3 ms: 1.32x faster                                                            |
| async_tree_io_tg           | 494 ms                                                          | 385 ms: 1.28x faster                                                             |
| async_tree_none_tg         | 214 ms                                                          | 167 ms: 1.28x faster                                                             |
| async_generators           | 270 ms                                                          | 213 ms: 1.26x faster                                                             |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 363 ms: 1.26x faster                                                             |
| asyncio_websockets         | 363 ms                                                          | 312 ms: 1.16x faster                                                             |
| Geometric mean             | (ref)                                                           | 1.31x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250307-pythonperf1_win32-amd64-brandtbucher-msvc_musttail-3.14.0a5+-06bc3bd |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| nbody          | 80.0 ms                                                         | 53.1 ms: 1.51x faster                                                            |
| pidigits       | 201 ms                                                          | 146 ms: 1.38x faster                                                             |
| float          | 54.6 ms                                                         | 41.4 ms: 1.32x faster                                                            |
| Geometric mean | (ref)                                                           | 1.40x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250307-pythonperf1_win32-amd64-brandtbucher-msvc_musttail-3.14.0a5+-06bc3bd |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 101 ms                                                          | 81.9 ms: 1.23x faster                                                            |
| regex_effbot   | 1.80 ms                                                         | 1.85 ms: 1.02x slower                                                            |
| regex_dna      | 114 ms                                                          | 121 ms: 1.06x slower                                                             |
| Geometric mean | (ref)                                                           | 1.04x faster                                                                     |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250307-pythonperf1_win32-amd64-brandtbucher-msvc_musttail-3.14.0a5+-06bc3bd |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| tomli_loads          | 1.71 sec                                                        | 1.26 sec: 1.36x faster                                                           |
| unpickle_pure_python | 160 us                                                          | 148 us: 1.08x faster                                                             |
| pickle_pure_python   | 231 us                                                          | 223 us: 1.04x faster                                                             |
| xml_etree_parse      | 107 ms                                                          | 105 ms: 1.03x faster                                                             |
| xml_etree_process    | 44.2 ms                                                         | 44.7 ms: 1.01x slower                                                            |
| json_loads           | 21.6 us                                                         | 21.9 us: 1.01x slower                                                            |
| xml_etree_generate   | 61.4 ms                                                         | 64.7 ms: 1.05x slower                                                            |
| json_dumps           | 7.30 ms                                                         | 7.79 ms: 1.07x slower                                                            |
| xml_etree_iterparse  | 62.6 ms                                                         | 70.4 ms: 1.12x slower                                                            |
| Geometric mean       | (ref)                                                           | 1.02x faster                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250307-pythonperf1_win32-amd64-brandtbucher-msvc_musttail-3.14.0a5+-06bc3bd |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup         | 28.3 ms                                                         | 26.4 ms: 1.07x faster                                                            |
| python_startup_no_site | 19.7 ms                                                         | 19.4 ms: 1.01x faster                                                            |
| Geometric mean         | (ref)                                                           | 1.04x faster                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250307-pythonperf1_win32-amd64-brandtbucher-msvc_musttail-3.14.0a5+-06bc3bd |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| genshi_xml      | 50.1 ms                                                         | 31.3 ms: 1.60x faster                                                            |
| genshi_text     | 21.5 ms                                                         | 14.5 ms: 1.49x faster                                                            |
| django_template | 29.8 ms                                                         | 25.2 ms: 1.18x faster                                                            |
| mako            | 7.09 ms                                                         | 7.84 ms: 1.11x slower                                                            |
| Geometric mean  | (ref)                                                           | 1.26x faster                                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250307-pythonperf1_win32-amd64-brandtbucher-msvc_musttail-3.14.0a5+-06bc3bd |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| thrift                     | 9.98 ms                                                         | 551 us: 18.12x faster                                                            |
| coverage                   | 324 ms                                                          | 55.4 ms: 5.85x faster                                                            |
| pathlib                    | 82.9 ms                                                         | 25.1 ms: 3.30x faster                                                            |
| deepcopy                   | 314 us                                                          | 180 us: 1.74x faster                                                             |
| genshi_xml                 | 50.1 ms                                                         | 31.3 ms: 1.60x faster                                                            |
| go                         | 109 ms                                                          | 70.4 ms: 1.54x faster                                                            |
| deepcopy_reduce            | 2.92 us                                                         | 1.90 us: 1.54x faster                                                            |
| nbody                      | 80.0 ms                                                         | 53.1 ms: 1.51x faster                                                            |
| genshi_text                | 21.5 ms                                                         | 14.5 ms: 1.49x faster                                                            |
| async_tree_memoization     | 297 ms                                                          | 210 ms: 1.41x faster                                                             |
| async_tree_none            | 245 ms                                                          | 174 ms: 1.41x faster                                                             |
| pidigits                   | 201 ms                                                          | 146 ms: 1.38x faster                                                             |
| async_tree_io              | 526 ms                                                          | 384 ms: 1.37x faster                                                             |
| tomli_loads                | 1.71 sec                                                        | 1.26 sec: 1.36x faster                                                           |
| spectral_norm              | 69.4 ms                                                         | 51.1 ms: 1.36x faster                                                            |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 359 ms: 1.35x faster                                                             |
| async_tree_memoization_tg  | 282 ms                                                          | 210 ms: 1.34x faster                                                             |
| generators                 | 21.8 ms                                                         | 16.3 ms: 1.34x faster                                                            |
| chaos                      | 50.2 ms                                                         | 37.7 ms: 1.33x faster                                                            |
| coroutines                 | 16.2 ms                                                         | 12.3 ms: 1.32x faster                                                            |
| telco                      | 6.96 ms                                                         | 5.26 ms: 1.32x faster                                                            |
| deepcopy_memo              | 25.4 us                                                         | 19.3 us: 1.32x faster                                                            |
| float                      | 54.6 ms                                                         | 41.4 ms: 1.32x faster                                                            |
| logging_format             | 8.72 us                                                         | 6.70 us: 1.30x faster                                                            |
| typing_runtime_protocols   | 138 us                                                          | 106 us: 1.30x faster                                                             |
| async_tree_io_tg           | 494 ms                                                          | 385 ms: 1.28x faster                                                             |
| async_tree_none_tg         | 214 ms                                                          | 167 ms: 1.28x faster                                                             |
| pprint_pformat             | 1.33 sec                                                        | 1.04 sec: 1.28x faster                                                           |
| logging_simple             | 7.99 us                                                         | 6.25 us: 1.28x faster                                                            |
| pprint_safe_repr           | 648 ms                                                          | 510 ms: 1.27x faster                                                             |
| async_generators           | 270 ms                                                          | 213 ms: 1.26x faster                                                             |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 363 ms: 1.26x faster                                                             |
| scimark_sor                | 85.9 ms                                                         | 68.6 ms: 1.25x faster                                                            |
| regex_compile              | 101 ms                                                          | 81.9 ms: 1.23x faster                                                            |
| sympy_expand               | 373 ms                                                          | 304 ms: 1.23x faster                                                             |
| html5lib                   | 47.5 ms                                                         | 38.8 ms: 1.23x faster                                                            |
| scimark_monte_carlo        | 47.7 ms                                                         | 38.9 ms: 1.22x faster                                                            |
| pycparser                  | 872 ms                                                          | 713 ms: 1.22x faster                                                             |
| deltablue                  | 2.33 ms                                                         | 1.91 ms: 1.22x faster                                                            |
| scimark_fft                | 205 ms                                                          | 169 ms: 1.21x faster                                                             |
| nqueens                    | 72.1 ms                                                         | 59.6 ms: 1.21x faster                                                            |
| sympy_str                  | 212 ms                                                          | 177 ms: 1.20x faster                                                             |
| fannkuch                   | 299 ms                                                          | 250 ms: 1.19x faster                                                             |
| raytrace                   | 201 ms                                                          | 169 ms: 1.19x faster                                                             |
| crypto_pyaes               | 56.9 ms                                                         | 48.0 ms: 1.19x faster                                                            |
| django_template            | 29.8 ms                                                         | 25.2 ms: 1.18x faster                                                            |
| pyflate                    | 320 ms                                                          | 274 ms: 1.17x faster                                                             |
| sqlite_synth               | 1.95 us                                                         | 1.68 us: 1.17x faster                                                            |
| asyncio_websockets         | 363 ms                                                          | 312 ms: 1.16x faster                                                             |
| sympy_sum                  | 106 ms                                                          | 91.4 ms: 1.15x faster                                                            |
| dulwich_log                | 48.8 ms                                                         | 42.3 ms: 1.15x faster                                                            |
| bpe_tokeniser              | 3.46 sec                                                        | 3.01 sec: 1.15x faster                                                           |
| scimark_sparse_mat_mult    | 2.84 ms                                                         | 2.47 ms: 1.15x faster                                                            |
| bench_thread_pool          | 1.00 ms                                                         | 876 us: 1.14x faster                                                             |
| hexiom                     | 4.44 ms                                                         | 3.92 ms: 1.13x faster                                                            |
| json                       | 4.27 ms                                                         | 3.78 ms: 1.13x faster                                                            |
| mdp                        | 1.62 sec                                                        | 1.44 sec: 1.13x faster                                                           |
| sympy_integrate            | 15.0 ms                                                         | 13.4 ms: 1.12x faster                                                            |
| comprehensions             | 12.5 us                                                         | 11.3 us: 1.11x faster                                                            |
| pylint                     | 227 ms                                                          | 205 ms: 1.11x faster                                                             |
| 2to3                       | 250 ms                                                          | 231 ms: 1.08x faster                                                             |
| unpickle_pure_python       | 160 us                                                          | 148 us: 1.08x faster                                                             |
| python_startup             | 28.3 ms                                                         | 26.4 ms: 1.07x faster                                                            |
| richards                   | 32.7 ms                                                         | 30.9 ms: 1.06x faster                                                            |
| pickle_pure_python         | 231 us                                                          | 223 us: 1.04x faster                                                             |
| xml_etree_parse            | 107 ms                                                          | 105 ms: 1.03x faster                                                             |
| richards_super             | 36.7 ms                                                         | 35.8 ms: 1.02x faster                                                            |
| sphinx                     | 719 ms                                                          | 702 ms: 1.02x faster                                                             |
| python_startup_no_site     | 19.7 ms                                                         | 19.4 ms: 1.01x faster                                                            |
| docutils                   | 1.78 sec                                                        | 1.77 sec: 1.01x faster                                                           |
| meteor_contest             | 74.6 ms                                                         | 74.5 ms: 1.00x faster                                                            |
| xml_etree_process          | 44.2 ms                                                         | 44.7 ms: 1.01x slower                                                            |
| logging_silent             | 60.3 ns                                                         | 61.1 ns: 1.01x slower                                                            |
| json_loads                 | 21.6 us                                                         | 21.9 us: 1.01x slower                                                            |
| regex_effbot               | 1.80 ms                                                         | 1.85 ms: 1.02x slower                                                            |
| bench_mp_pool              | 90.6 ms                                                         | 93.6 ms: 1.03x slower                                                            |
| xml_etree_generate         | 61.4 ms                                                         | 64.7 ms: 1.05x slower                                                            |
| regex_dna                  | 114 ms                                                          | 121 ms: 1.06x slower                                                             |
| scimark_lu                 | 60.2 ms                                                         | 64.2 ms: 1.07x slower                                                            |
| json_dumps                 | 7.30 ms                                                         | 7.79 ms: 1.07x slower                                                            |
| mako                       | 7.09 ms                                                         | 7.84 ms: 1.11x slower                                                            |
| xml_etree_iterparse        | 62.6 ms                                                         | 70.4 ms: 1.12x slower                                                            |
| connected_components       | 267 ms                                                          | 311 ms: 1.17x slower                                                             |
| shortest_path              | 290 ms                                                          | 347 ms: 1.20x slower                                                             |
| k_core                     | 1.38 sec                                                        | 1.71 sec: 1.24x slower                                                           |
| create_gc_cycles           | 1.06 ms                                                         | 1.34 ms: 1.26x slower                                                            |
| gc_traversal               | 1.75 ms                                                         | 2.83 ms: 1.62x slower                                                            |
| many_optionals             | 436 us                                                          | 762 us: 1.75x slower                                                             |
| subparsers                 | 14.8 ms                                                         | 44.5 ms: 3.01x slower                                                            |
| Geometric mean             | (ref)                                                           | 1.20x faster                                                                     |

Benchmark hidden because not significant (1): regex_v8
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250225-3.14.0a5+-f963239/bm-20250307-pythonperf1_win32-amd64-brandtbucher-msvc_musttail-3.14.0a5+-06bc3bd.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.203x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.16x
- 95% likely to have a speedup of 1.15x
- 99% likely to have a speedup of 1.13x

# Memory
- memory change: unknown