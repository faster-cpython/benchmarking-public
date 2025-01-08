# Results vs. 3.13.0

- fork: brandtbucher
- ref: nojit
- machine: windows-x86
- commit hash: f098037
- commit date: 2025-01-07
- overall geometric mean: 1.041x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250107-pythonperf1_win32-x86-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 250 ms                                                          | 263 ms: 1.05x slower                                                   |
| docutils       | 1.78 sec                                                        | 1.95 sec: 1.10x slower                                                 |
| sphinx         | 719 ms                                                          | 790 ms: 1.10x slower                                                   |
| Geometric mean | (ref)                                                           | 1.06x slower                                                           |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250107-pythonperf1_win32-x86-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 282 ms                                                          | 241 ms: 1.17x faster                                                   |
| async_tree_none_tg         | 214 ms                                                          | 189 ms: 1.13x faster                                                   |
| async_tree_io              | 526 ms                                                          | 470 ms: 1.12x faster                                                   |
| async_tree_io_tg           | 494 ms                                                          | 444 ms: 1.11x faster                                                   |
| async_tree_none            | 245 ms                                                          | 223 ms: 1.10x faster                                                   |
| async_tree_memoization     | 297 ms                                                          | 273 ms: 1.09x faster                                                   |
| asyncio_websockets         | 363 ms                                                          | 349 ms: 1.04x faster                                                   |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 473 ms: 1.02x faster                                                   |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 453 ms: 1.01x faster                                                   |
| coroutines                 | 16.2 ms                                                         | 16.8 ms: 1.03x slower                                                  |
| async_generators           | 270 ms                                                          | 326 ms: 1.21x slower                                                   |
| Geometric mean             | (ref)                                                           | 1.05x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250107-pythonperf1_win32-x86-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 54.6 ms                                                         | 52.2 ms: 1.05x faster                                                  |
| pidigits       | 201 ms                                                          | 201 ms: 1.00x slower                                                   |
| nbody          | 80.0 ms                                                         | 102 ms: 1.27x slower                                                   |
| Geometric mean | (ref)                                                           | 1.07x slower                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250107-pythonperf1_win32-x86-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_effbot   | 1.80 ms                                                         | 1.65 ms: 1.09x faster                                                  |
| regex_v8       | 16.8 ms                                                         | 15.7 ms: 1.07x faster                                                  |
| regex_dna      | 114 ms                                                          | 124 ms: 1.09x slower                                                   |
| regex_compile  | 101 ms                                                          | 112 ms: 1.11x slower                                                   |
| Geometric mean | (ref)                                                           | 1.01x slower                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250107-pythonperf1_win32-x86-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------:|
| json_loads           | 21.6 us                                                         | 20.6 us: 1.05x faster                                                  |
| tomli_loads          | 1.71 sec                                                        | 1.76 sec: 1.02x slower                                                 |
| xml_etree_iterparse  | 62.6 ms                                                         | 66.6 ms: 1.06x slower                                                  |
| xml_etree_generate   | 61.4 ms                                                         | 72.8 ms: 1.19x slower                                                  |
| xml_etree_process    | 44.2 ms                                                         | 53.3 ms: 1.21x slower                                                  |
| json_dumps           | 7.30 ms                                                         | 9.18 ms: 1.26x slower                                                  |
| unpickle_pure_python | 160 us                                                          | 203 us: 1.27x slower                                                   |
| pickle_pure_python   | 231 us                                                          | 294 us: 1.27x slower                                                   |
| Geometric mean       | (ref)                                                           | 1.13x slower                                                           |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250107-pythonperf1_win32-x86-brandtbucher-nojit-3.14.0a3+-f098037 |
|------------------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 28.3 ms                                                         | 25.7 ms: 1.10x faster                                                  |
| python_startup_no_site | 19.7 ms                                                         | 19.1 ms: 1.03x faster                                                  |
| Geometric mean         | (ref)                                                           | 1.06x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250107-pythonperf1_win32-x86-brandtbucher-nojit-3.14.0a3+-f098037 |
|-----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 7.09 ms                                                         | 7.59 ms: 1.07x slower                                                  |
| genshi_xml      | 50.1 ms                                                         | 55.1 ms: 1.10x slower                                                  |
| genshi_text     | 21.5 ms                                                         | 26.0 ms: 1.21x slower                                                  |
| django_template | 29.8 ms                                                         | 36.8 ms: 1.24x slower                                                  |
| Geometric mean  | (ref)                                                           | 1.15x slower                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250107-pythonperf1_win32-x86-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------:|
| thrift                     | 9.98 ms                                                         | 780 us: 12.80x faster                                                  |
| coverage                   | 324 ms                                                          | 51.9 ms: 6.24x faster                                                  |
| sqlglot_normalize          | 216 ms                                                          | 105 ms: 2.06x faster                                                   |
| async_tree_memoization_tg  | 282 ms                                                          | 241 ms: 1.17x faster                                                   |
| deepcopy                   | 314 us                                                          | 273 us: 1.15x faster                                                   |
| async_tree_none_tg         | 214 ms                                                          | 189 ms: 1.13x faster                                                   |
| async_tree_io              | 526 ms                                                          | 470 ms: 1.12x faster                                                   |
| deepcopy_memo              | 25.4 us                                                         | 22.8 us: 1.12x faster                                                  |
| async_tree_io_tg           | 494 ms                                                          | 444 ms: 1.11x faster                                                   |
| python_startup             | 28.3 ms                                                         | 25.7 ms: 1.10x faster                                                  |
| async_tree_none            | 245 ms                                                          | 223 ms: 1.10x faster                                                   |
| regex_effbot               | 1.80 ms                                                         | 1.65 ms: 1.09x faster                                                  |
| async_tree_memoization     | 297 ms                                                          | 273 ms: 1.09x faster                                                   |
| regex_v8                   | 16.8 ms                                                         | 15.7 ms: 1.07x faster                                                  |
| json_loads                 | 21.6 us                                                         | 20.6 us: 1.05x faster                                                  |
| deepcopy_reduce            | 2.92 us                                                         | 2.79 us: 1.05x faster                                                  |
| float                      | 54.6 ms                                                         | 52.2 ms: 1.05x faster                                                  |
| asyncio_websockets         | 363 ms                                                          | 349 ms: 1.04x faster                                                   |
| bench_mp_pool              | 90.6 ms                                                         | 87.4 ms: 1.04x faster                                                  |
| python_startup_no_site     | 19.7 ms                                                         | 19.1 ms: 1.03x faster                                                  |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 473 ms: 1.02x faster                                                   |
| sqlite_synth               | 1.95 us                                                         | 1.92 us: 1.02x faster                                                  |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 453 ms: 1.01x faster                                                   |
| pidigits                   | 201 ms                                                          | 201 ms: 1.00x slower                                                   |
| json                       | 4.27 ms                                                         | 4.34 ms: 1.02x slower                                                  |
| tomli_loads                | 1.71 sec                                                        | 1.76 sec: 1.02x slower                                                 |
| k_core                     | 1.38 sec                                                        | 1.41 sec: 1.02x slower                                                 |
| telco                      | 6.96 ms                                                         | 7.18 ms: 1.03x slower                                                  |
| coroutines                 | 16.2 ms                                                         | 16.8 ms: 1.03x slower                                                  |
| pylint                     | 227 ms                                                          | 234 ms: 1.03x slower                                                   |
| dulwich_log                | 48.8 ms                                                         | 50.5 ms: 1.04x slower                                                  |
| gc_traversal               | 1.75 ms                                                         | 1.82 ms: 1.04x slower                                                  |
| bench_thread_pool          | 1.00 ms                                                         | 1.04 ms: 1.04x slower                                                  |
| 2to3                       | 250 ms                                                          | 263 ms: 1.05x slower                                                   |
| logging_format             | 8.72 us                                                         | 9.18 us: 1.05x slower                                                  |
| xml_etree_iterparse        | 62.6 ms                                                         | 66.6 ms: 1.06x slower                                                  |
| logging_simple             | 7.99 us                                                         | 8.54 us: 1.07x slower                                                  |
| connected_components       | 267 ms                                                          | 285 ms: 1.07x slower                                                   |
| mako                       | 7.09 ms                                                         | 7.59 ms: 1.07x slower                                                  |
| spectral_norm              | 69.4 ms                                                         | 74.7 ms: 1.08x slower                                                  |
| sympy_sum                  | 106 ms                                                          | 114 ms: 1.08x slower                                                   |
| scimark_sor                | 85.9 ms                                                         | 92.7 ms: 1.08x slower                                                  |
| pycparser                  | 872 ms                                                          | 943 ms: 1.08x slower                                                   |
| shortest_path              | 290 ms                                                          | 314 ms: 1.08x slower                                                   |
| scimark_sparse_mat_mult    | 2.84 ms                                                         | 3.08 ms: 1.09x slower                                                  |
| sympy_expand               | 373 ms                                                          | 406 ms: 1.09x slower                                                   |
| regex_dna                  | 114 ms                                                          | 124 ms: 1.09x slower                                                   |
| docutils                   | 1.78 sec                                                        | 1.95 sec: 1.10x slower                                                 |
| sphinx                     | 719 ms                                                          | 790 ms: 1.10x slower                                                   |
| genshi_xml                 | 50.1 ms                                                         | 55.1 ms: 1.10x slower                                                  |
| sympy_str                  | 212 ms                                                          | 233 ms: 1.10x slower                                                   |
| regex_compile              | 101 ms                                                          | 112 ms: 1.11x slower                                                   |
| fannkuch                   | 299 ms                                                          | 334 ms: 1.12x slower                                                   |
| pprint_pformat             | 1.33 sec                                                        | 1.49 sec: 1.12x slower                                                 |
| bpe_tokeniser              | 3.46 sec                                                        | 3.89 sec: 1.13x slower                                                 |
| pprint_safe_repr           | 648 ms                                                          | 733 ms: 1.13x slower                                                   |
| mdp                        | 1.62 sec                                                        | 1.84 sec: 1.13x slower                                                 |
| go                         | 109 ms                                                          | 124 ms: 1.14x slower                                                   |
| sqlglot_parse              | 1.00 ms                                                         | 1.15 ms: 1.15x slower                                                  |
| sqlglot_transpile          | 1.24 ms                                                         | 1.42 ms: 1.15x slower                                                  |
| sympy_integrate            | 15.0 ms                                                         | 17.3 ms: 1.15x slower                                                  |
| typing_runtime_protocols   | 138 us                                                          | 159 us: 1.16x slower                                                   |
| scimark_fft                | 205 ms                                                          | 240 ms: 1.17x slower                                                   |
| meteor_contest             | 74.6 ms                                                         | 88.3 ms: 1.18x slower                                                  |
| xml_etree_generate         | 61.4 ms                                                         | 72.8 ms: 1.19x slower                                                  |
| scimark_lu                 | 60.2 ms                                                         | 72.5 ms: 1.20x slower                                                  |
| xml_etree_process          | 44.2 ms                                                         | 53.3 ms: 1.21x slower                                                  |
| async_generators           | 270 ms                                                          | 326 ms: 1.21x slower                                                   |
| sqlglot_optimize           | 41.4 ms                                                         | 50.1 ms: 1.21x slower                                                  |
| genshi_text                | 21.5 ms                                                         | 26.0 ms: 1.21x slower                                                  |
| crypto_pyaes               | 56.9 ms                                                         | 68.9 ms: 1.21x slower                                                  |
| django_template            | 29.8 ms                                                         | 36.8 ms: 1.24x slower                                                  |
| pyflate                    | 320 ms                                                          | 399 ms: 1.25x slower                                                   |
| json_dumps                 | 7.30 ms                                                         | 9.18 ms: 1.26x slower                                                  |
| unpickle_pure_python       | 160 us                                                          | 203 us: 1.27x slower                                                   |
| pickle_pure_python         | 231 us                                                          | 294 us: 1.27x slower                                                   |
| nbody                      | 80.0 ms                                                         | 102 ms: 1.27x slower                                                   |
| many_optionals             | 436 us                                                          | 560 us: 1.28x slower                                                   |
| chaos                      | 50.2 ms                                                         | 64.7 ms: 1.29x slower                                                  |
| scimark_monte_carlo        | 47.7 ms                                                         | 61.7 ms: 1.29x slower                                                  |
| richards_super             | 36.7 ms                                                         | 48.1 ms: 1.31x slower                                                  |
| richards                   | 32.7 ms                                                         | 43.5 ms: 1.33x slower                                                  |
| nqueens                    | 72.1 ms                                                         | 96.5 ms: 1.34x slower                                                  |
| deltablue                  | 2.33 ms                                                         | 3.17 ms: 1.36x slower                                                  |
| logging_silent             | 60.3 ns                                                         | 84.3 ns: 1.40x slower                                                  |
| subparsers                 | 14.8 ms                                                         | 21.2 ms: 1.43x slower                                                  |
| comprehensions             | 12.5 us                                                         | 18.5 us: 1.48x slower                                                  |
| raytrace                   | 201 ms                                                          | 307 ms: 1.53x slower                                                   |
| hexiom                     | 4.44 ms                                                         | 7.10 ms: 1.60x slower                                                  |
| generators                 | 21.8 ms                                                         | 37.6 ms: 1.73x slower                                                  |
| Geometric mean             | (ref)                                                           | 1.04x slower                                                           |

Benchmark hidden because not significant (4): pathlib, xml_etree_parse, create_gc_cycles, html5lib
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (1) of results/bm-20250107-3.14.0a3+-f098037-JIT/bm-20250107-pythonperf1_win32-x86-brandtbucher-nojit-3.14.0a3+-f098037.json: mypy2

- Geometric mean (including insignificant results): 1.041x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.07x
- 95% likely to have a slowdown of 1.06x
- 99% likely to have a slowdown of 1.04x

# Memory
- memory change: unknown