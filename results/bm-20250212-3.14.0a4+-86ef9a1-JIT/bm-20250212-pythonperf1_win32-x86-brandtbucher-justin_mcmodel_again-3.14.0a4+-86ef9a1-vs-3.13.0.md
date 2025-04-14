# Results vs. 3.13.0

- fork: brandtbucher
- ref: justin_mcmodel_again
- machine: windows-x86
- commit hash: 86ef9a1
- commit date: 2025-02-12
- overall geometric mean: 1.034x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250212-pythonperf1_win32-x86-brandtbucher-justin_mcmodel_again-3.14.0a4+-86ef9a1 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| 2to3           | 250 ms                                                          | 273 ms: 1.09x slower                                                                  |
| docutils       | 1.78 sec                                                        | 1.97 sec: 1.11x slower                                                                |
| sphinx         | 719 ms                                                          | 763 ms: 1.06x slower                                                                  |
| Geometric mean | (ref)                                                           | 1.07x slower                                                                          |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250212-pythonperf1_win32-x86-brandtbucher-justin_mcmodel_again-3.14.0a4+-86ef9a1 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| async_tree_io              | 526 ms                                                          | 479 ms: 1.10x faster                                                                  |
| async_tree_memoization     | 297 ms                                                          | 278 ms: 1.07x faster                                                                  |
| async_tree_none            | 245 ms                                                          | 230 ms: 1.06x faster                                                                  |
| async_tree_memoization_tg  | 282 ms                                                          | 266 ms: 1.06x faster                                                                  |
| async_tree_io_tg           | 494 ms                                                          | 477 ms: 1.04x faster                                                                  |
| asyncio_websockets         | 363 ms                                                          | 353 ms: 1.03x faster                                                                  |
| coroutines                 | 16.2 ms                                                         | 15.9 ms: 1.02x faster                                                                 |
| async_tree_none_tg         | 214 ms                                                          | 212 ms: 1.01x faster                                                                  |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 490 ms: 1.01x slower                                                                  |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 478 ms: 1.05x slower                                                                  |
| async_generators           | 270 ms                                                          | 326 ms: 1.21x slower                                                                  |
| Geometric mean             | (ref)                                                           | 1.01x faster                                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250212-pythonperf1_win32-x86-brandtbucher-justin_mcmodel_again-3.14.0a4+-86ef9a1 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| float          | 54.6 ms                                                         | 52.5 ms: 1.04x faster                                                                 |
| pidigits       | 201 ms                                                          | 203 ms: 1.01x slower                                                                  |
| nbody          | 80.0 ms                                                         | 111 ms: 1.39x slower                                                                  |
| Geometric mean | (ref)                                                           | 1.10x slower                                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250212-pythonperf1_win32-x86-brandtbucher-justin_mcmodel_again-3.14.0a4+-86ef9a1 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| regex_effbot   | 1.80 ms                                                         | 1.53 ms: 1.18x faster                                                                 |
| regex_v8       | 16.8 ms                                                         | 15.7 ms: 1.07x faster                                                                 |
| regex_dna      | 114 ms                                                          | 117 ms: 1.03x slower                                                                  |
| regex_compile  | 101 ms                                                          | 118 ms: 1.17x slower                                                                  |
| Geometric mean | (ref)                                                           | 1.01x faster                                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250212-pythonperf1_win32-x86-brandtbucher-justin_mcmodel_again-3.14.0a4+-86ef9a1 |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| json_loads           | 21.6 us                                                         | 22.2 us: 1.03x slower                                                                 |
| tomli_loads          | 1.71 sec                                                        | 1.80 sec: 1.05x slower                                                                |
| xml_etree_iterparse  | 62.6 ms                                                         | 67.0 ms: 1.07x slower                                                                 |
| xml_etree_generate   | 61.4 ms                                                         | 75.8 ms: 1.23x slower                                                                 |
| xml_etree_process    | 44.2 ms                                                         | 56.2 ms: 1.27x slower                                                                 |
| json_dumps           | 7.30 ms                                                         | 9.38 ms: 1.28x slower                                                                 |
| pickle_pure_python   | 231 us                                                          | 325 us: 1.41x slower                                                                  |
| unpickle_pure_python | 160 us                                                          | 227 us: 1.42x slower                                                                  |
| Geometric mean       | (ref)                                                           | 1.19x slower                                                                          |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250212-pythonperf1_win32-x86-brandtbucher-justin_mcmodel_again-3.14.0a4+-86ef9a1 |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| python_startup_no_site | 19.7 ms                                                         | 21.7 ms: 1.11x slower                                                                 |
| Geometric mean         | (ref)                                                           | 1.05x slower                                                                          |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250212-pythonperf1_win32-x86-brandtbucher-justin_mcmodel_again-3.14.0a4+-86ef9a1 |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                         | 7.47 ms: 1.05x slower                                                                 |
| genshi_text     | 21.5 ms                                                         | 24.5 ms: 1.14x slower                                                                 |
| django_template | 29.8 ms                                                         | 36.4 ms: 1.22x slower                                                                 |
| Geometric mean  | (ref)                                                           | 1.11x slower                                                                          |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250212-pythonperf1_win32-x86-brandtbucher-justin_mcmodel_again-3.14.0a4+-86ef9a1 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| thrift                     | 9.98 ms                                                         | 775 us: 12.87x faster                                                                 |
| coverage                   | 324 ms                                                          | 51.6 ms: 6.27x faster                                                                 |
| sqlglot_normalize          | 216 ms                                                          | 106 ms: 2.04x faster                                                                  |
| pathlib                    | 82.9 ms                                                         | 63.3 ms: 1.31x faster                                                                 |
| deepcopy                   | 314 us                                                          | 259 us: 1.21x faster                                                                  |
| regex_effbot               | 1.80 ms                                                         | 1.53 ms: 1.18x faster                                                                 |
| deepcopy_memo              | 25.4 us                                                         | 22.3 us: 1.14x faster                                                                 |
| async_tree_io              | 526 ms                                                          | 479 ms: 1.10x faster                                                                  |
| regex_v8                   | 16.8 ms                                                         | 15.7 ms: 1.07x faster                                                                 |
| async_tree_memoization     | 297 ms                                                          | 278 ms: 1.07x faster                                                                  |
| async_tree_none            | 245 ms                                                          | 230 ms: 1.06x faster                                                                  |
| async_tree_memoization_tg  | 282 ms                                                          | 266 ms: 1.06x faster                                                                  |
| deepcopy_reduce            | 2.92 us                                                         | 2.75 us: 1.06x faster                                                                 |
| spectral_norm              | 69.4 ms                                                         | 65.7 ms: 1.06x faster                                                                 |
| sqlite_synth               | 1.95 us                                                         | 1.86 us: 1.05x faster                                                                 |
| float                      | 54.6 ms                                                         | 52.5 ms: 1.04x faster                                                                 |
| async_tree_io_tg           | 494 ms                                                          | 477 ms: 1.04x faster                                                                  |
| asyncio_websockets         | 363 ms                                                          | 353 ms: 1.03x faster                                                                  |
| coroutines                 | 16.2 ms                                                         | 15.9 ms: 1.02x faster                                                                 |
| create_gc_cycles           | 1.06 ms                                                         | 1.05 ms: 1.01x faster                                                                 |
| async_tree_none_tg         | 214 ms                                                          | 212 ms: 1.01x faster                                                                  |
| go                         | 109 ms                                                          | 109 ms: 1.01x slower                                                                  |
| pidigits                   | 201 ms                                                          | 203 ms: 1.01x slower                                                                  |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 490 ms: 1.01x slower                                                                  |
| json_loads                 | 21.6 us                                                         | 22.2 us: 1.03x slower                                                                 |
| regex_dna                  | 114 ms                                                          | 117 ms: 1.03x slower                                                                  |
| k_core                     | 1.38 sec                                                        | 1.41 sec: 1.03x slower                                                                |
| bench_mp_pool              | 90.6 ms                                                         | 93.6 ms: 1.03x slower                                                                 |
| logging_format             | 8.72 us                                                         | 9.03 us: 1.04x slower                                                                 |
| gc_traversal               | 1.75 ms                                                         | 1.81 ms: 1.04x slower                                                                 |
| scimark_monte_carlo        | 47.7 ms                                                         | 49.4 ms: 1.04x slower                                                                 |
| logging_simple             | 7.99 us                                                         | 8.30 us: 1.04x slower                                                                 |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 478 ms: 1.05x slower                                                                  |
| tomli_loads                | 1.71 sec                                                        | 1.80 sec: 1.05x slower                                                                |
| mako                       | 7.09 ms                                                         | 7.47 ms: 1.05x slower                                                                 |
| json                       | 4.27 ms                                                         | 4.51 ms: 1.05x slower                                                                 |
| pyflate                    | 320 ms                                                          | 339 ms: 1.06x slower                                                                  |
| sphinx                     | 719 ms                                                          | 763 ms: 1.06x slower                                                                  |
| xml_etree_iterparse        | 62.6 ms                                                         | 67.0 ms: 1.07x slower                                                                 |
| generators                 | 21.8 ms                                                         | 23.3 ms: 1.07x slower                                                                 |
| dulwich_log                | 48.8 ms                                                         | 52.5 ms: 1.08x slower                                                                 |
| sympy_sum                  | 106 ms                                                          | 115 ms: 1.09x slower                                                                  |
| 2to3                       | 250 ms                                                          | 273 ms: 1.09x slower                                                                  |
| sympy_expand               | 373 ms                                                          | 412 ms: 1.10x slower                                                                  |
| python_startup_no_site     | 19.7 ms                                                         | 21.7 ms: 1.11x slower                                                                 |
| sympy_str                  | 212 ms                                                          | 235 ms: 1.11x slower                                                                  |
| docutils                   | 1.78 sec                                                        | 1.97 sec: 1.11x slower                                                                |
| connected_components       | 267 ms                                                          | 296 ms: 1.11x slower                                                                  |
| scimark_lu                 | 60.2 ms                                                         | 67.2 ms: 1.12x slower                                                                 |
| scimark_sparse_mat_mult    | 2.84 ms                                                         | 3.18 ms: 1.12x slower                                                                 |
| telco                      | 6.96 ms                                                         | 7.80 ms: 1.12x slower                                                                 |
| scimark_sor                | 85.9 ms                                                         | 96.4 ms: 1.12x slower                                                                 |
| pycparser                  | 872 ms                                                          | 983 ms: 1.13x slower                                                                  |
| richards                   | 32.7 ms                                                         | 36.9 ms: 1.13x slower                                                                 |
| chaos                      | 50.2 ms                                                         | 57.1 ms: 1.14x slower                                                                 |
| sympy_integrate            | 15.0 ms                                                         | 17.0 ms: 1.14x slower                                                                 |
| genshi_text                | 21.5 ms                                                         | 24.5 ms: 1.14x slower                                                                 |
| mdp                        | 1.62 sec                                                        | 1.86 sec: 1.14x slower                                                                |
| shortest_path              | 290 ms                                                          | 332 ms: 1.15x slower                                                                  |
| pprint_safe_repr           | 648 ms                                                          | 756 ms: 1.17x slower                                                                  |
| regex_compile              | 101 ms                                                          | 118 ms: 1.17x slower                                                                  |
| bpe_tokeniser              | 3.46 sec                                                        | 4.05 sec: 1.17x slower                                                                |
| pprint_pformat             | 1.33 sec                                                        | 1.56 sec: 1.18x slower                                                                |
| logging_silent             | 60.3 ns                                                         | 71.1 ns: 1.18x slower                                                                 |
| richards_super             | 36.7 ms                                                         | 43.5 ms: 1.19x slower                                                                 |
| sqlglot_transpile          | 1.24 ms                                                         | 1.47 ms: 1.19x slower                                                                 |
| sqlglot_parse              | 1.00 ms                                                         | 1.20 ms: 1.20x slower                                                                 |
| async_generators           | 270 ms                                                          | 326 ms: 1.21x slower                                                                  |
| meteor_contest             | 74.6 ms                                                         | 90.3 ms: 1.21x slower                                                                 |
| sqlglot_optimize           | 41.4 ms                                                         | 50.5 ms: 1.22x slower                                                                 |
| typing_runtime_protocols   | 138 us                                                          | 168 us: 1.22x slower                                                                  |
| django_template            | 29.8 ms                                                         | 36.4 ms: 1.22x slower                                                                 |
| xml_etree_generate         | 61.4 ms                                                         | 75.8 ms: 1.23x slower                                                                 |
| scimark_fft                | 205 ms                                                          | 255 ms: 1.25x slower                                                                  |
| fannkuch                   | 299 ms                                                          | 375 ms: 1.26x slower                                                                  |
| raytrace                   | 201 ms                                                          | 254 ms: 1.26x slower                                                                  |
| xml_etree_process          | 44.2 ms                                                         | 56.2 ms: 1.27x slower                                                                 |
| deltablue                  | 2.33 ms                                                         | 2.99 ms: 1.28x slower                                                                 |
| json_dumps                 | 7.30 ms                                                         | 9.38 ms: 1.28x slower                                                                 |
| crypto_pyaes               | 56.9 ms                                                         | 73.2 ms: 1.29x slower                                                                 |
| comprehensions             | 12.5 us                                                         | 16.5 us: 1.32x slower                                                                 |
| many_optionals             | 436 us                                                          | 574 us: 1.32x slower                                                                  |
| bench_thread_pool          | 1.00 ms                                                         | 1.34 ms: 1.34x slower                                                                 |
| hexiom                     | 4.44 ms                                                         | 5.98 ms: 1.35x slower                                                                 |
| nbody                      | 80.0 ms                                                         | 111 ms: 1.39x slower                                                                  |
| pickle_pure_python         | 231 us                                                          | 325 us: 1.41x slower                                                                  |
| unpickle_pure_python       | 160 us                                                          | 227 us: 1.42x slower                                                                  |
| nqueens                    | 72.1 ms                                                         | 106 ms: 1.47x slower                                                                  |
| subparsers                 | 14.8 ms                                                         | 22.6 ms: 1.53x slower                                                                 |
| Geometric mean             | (ref)                                                           | 1.04x slower                                                                          |

Benchmark hidden because not significant (5): xml_etree_parse, html5lib, python_startup, pylint, genshi_xml
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http

- Geometric mean (including insignificant results): 1.034x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.06x
- 95% likely to have a slowdown of 1.05x
- 99% likely to have a slowdown of 1.04x

# Memory
- memory change: unknown