# Results vs. 3.13.0

- fork: brandtbucher
- ref: nojit
- machine: windows-x86
- commit hash: f098037
- commit date: 2025-01-07
- overall geometric mean: 1.035x faster
- HPT reliability: 93.04%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250107-pythonperf1_win32-x86-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 250 ms                                                          | 247 ms: 1.01x faster                                                   |
| docutils       | 1.78 sec                                                        | 1.84 sec: 1.04x slower                                                 |
| html5lib       | 47.5 ms                                                         | 44.7 ms: 1.06x faster                                                  |
| sphinx         | 719 ms                                                          | 739 ms: 1.03x slower                                                   |
| Geometric mean | (ref)                                                           | 1.00x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250107-pythonperf1_win32-x86-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 282 ms                                                          | 230 ms: 1.23x faster                                                   |
| async_tree_io              | 526 ms                                                          | 446 ms: 1.18x faster                                                   |
| async_tree_none            | 245 ms                                                          | 208 ms: 1.18x faster                                                   |
| async_tree_none_tg         | 214 ms                                                          | 183 ms: 1.17x faster                                                   |
| async_tree_memoization     | 297 ms                                                          | 254 ms: 1.17x faster                                                   |
| async_tree_io_tg           | 494 ms                                                          | 433 ms: 1.14x faster                                                   |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 451 ms: 1.07x faster                                                   |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 437 ms: 1.04x faster                                                   |
| asyncio_websockets         | 363 ms                                                          | 369 ms: 1.02x slower                                                   |
| coroutines                 | 16.2 ms                                                         | 16.5 ms: 1.02x slower                                                  |
| async_generators           | 270 ms                                                          | 295 ms: 1.10x slower                                                   |
| Geometric mean             | (ref)                                                           | 1.09x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250107-pythonperf1_win32-x86-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------:|
| pidigits       | 201 ms                                                          | 197 ms: 1.02x faster                                                   |
| float          | 54.6 ms                                                         | 55.6 ms: 1.02x slower                                                  |
| nbody          | 80.0 ms                                                         | 89.2 ms: 1.12x slower                                                  |
| Geometric mean | (ref)                                                           | 1.04x slower                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250107-pythonperf1_win32-x86-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_effbot   | 1.80 ms                                                         | 1.57 ms: 1.15x faster                                                  |
| regex_compile  | 101 ms                                                          | 104 ms: 1.03x slower                                                   |
| regex_dna      | 114 ms                                                          | 124 ms: 1.09x slower                                                   |
| Geometric mean | (ref)                                                           | 1.00x slower                                                           |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250107-pythonperf1_win32-x86-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 1.71 sec                                                        | 1.58 sec: 1.09x faster                                                 |
| json_loads           | 21.6 us                                                         | 20.7 us: 1.04x faster                                                  |
| xml_etree_parse      | 107 ms                                                          | 108 ms: 1.01x slower                                                   |
| unpickle_pure_python | 160 us                                                          | 166 us: 1.03x slower                                                   |
| xml_etree_iterparse  | 62.6 ms                                                         | 66.7 ms: 1.07x slower                                                  |
| xml_etree_process    | 44.2 ms                                                         | 48.8 ms: 1.11x slower                                                  |
| xml_etree_generate   | 61.4 ms                                                         | 68.0 ms: 1.11x slower                                                  |
| pickle_pure_python   | 231 us                                                          | 258 us: 1.12x slower                                                   |
| json_dumps           | 7.30 ms                                                         | 8.76 ms: 1.20x slower                                                  |
| Geometric mean       | (ref)                                                           | 1.05x slower                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250107-pythonperf1_win32-x86-brandtbucher-nojit-3.14.0a3+-f098037 |
|------------------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 28.3 ms                                                         | 25.4 ms: 1.12x faster                                                  |
| python_startup_no_site | 19.7 ms                                                         | 19.1 ms: 1.03x faster                                                  |
| Geometric mean         | (ref)                                                           | 1.07x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250107-pythonperf1_win32-x86-brandtbucher-nojit-3.14.0a3+-f098037 |
|-----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_xml      | 50.1 ms                                                         | 44.8 ms: 1.12x faster                                                  |
| genshi_text     | 21.5 ms                                                         | 21.1 ms: 1.02x faster                                                  |
| mako            | 7.09 ms                                                         | 7.74 ms: 1.09x slower                                                  |
| django_template | 29.8 ms                                                         | 33.3 ms: 1.12x slower                                                  |
| Geometric mean  | (ref)                                                           | 1.02x slower                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250107-pythonperf1_win32-x86-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------:|
| thrift                     | 9.98 ms                                                         | 732 us: 13.63x faster                                                  |
| coverage                   | 324 ms                                                          | 52.4 ms: 6.18x faster                                                  |
| deepcopy                   | 314 us                                                          | 225 us: 1.40x faster                                                   |
| deepcopy_memo              | 25.4 us                                                         | 20.7 us: 1.23x faster                                                  |
| async_tree_memoization_tg  | 282 ms                                                          | 230 ms: 1.23x faster                                                   |
| deepcopy_reduce            | 2.92 us                                                         | 2.38 us: 1.22x faster                                                  |
| async_tree_io              | 526 ms                                                          | 446 ms: 1.18x faster                                                   |
| async_tree_none            | 245 ms                                                          | 208 ms: 1.18x faster                                                   |
| async_tree_none_tg         | 214 ms                                                          | 183 ms: 1.17x faster                                                   |
| async_tree_memoization     | 297 ms                                                          | 254 ms: 1.17x faster                                                   |
| regex_effbot               | 1.80 ms                                                         | 1.57 ms: 1.15x faster                                                  |
| async_tree_io_tg           | 494 ms                                                          | 433 ms: 1.14x faster                                                   |
| genshi_xml                 | 50.1 ms                                                         | 44.8 ms: 1.12x faster                                                  |
| go                         | 109 ms                                                          | 97.4 ms: 1.12x faster                                                  |
| python_startup             | 28.3 ms                                                         | 25.4 ms: 1.12x faster                                                  |
| tomli_loads                | 1.71 sec                                                        | 1.58 sec: 1.09x faster                                                 |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 451 ms: 1.07x faster                                                   |
| html5lib                   | 47.5 ms                                                         | 44.7 ms: 1.06x faster                                                  |
| json_loads                 | 21.6 us                                                         | 20.7 us: 1.04x faster                                                  |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 437 ms: 1.04x faster                                                   |
| bench_mp_pool              | 90.6 ms                                                         | 87.3 ms: 1.04x faster                                                  |
| telco                      | 6.96 ms                                                         | 6.71 ms: 1.04x faster                                                  |
| pylint                     | 227 ms                                                          | 219 ms: 1.03x faster                                                   |
| python_startup_no_site     | 19.7 ms                                                         | 19.1 ms: 1.03x faster                                                  |
| connected_components       | 267 ms                                                          | 259 ms: 1.03x faster                                                   |
| genshi_text                | 21.5 ms                                                         | 21.1 ms: 1.02x faster                                                  |
| pprint_safe_repr           | 648 ms                                                          | 637 ms: 1.02x faster                                                   |
| pidigits                   | 201 ms                                                          | 197 ms: 1.02x faster                                                   |
| logging_simple             | 7.99 us                                                         | 7.87 us: 1.01x faster                                                  |
| 2to3                       | 250 ms                                                          | 247 ms: 1.01x faster                                                   |
| sqlglot_normalize          | 216 ms                                                          | 214 ms: 1.01x faster                                                   |
| json                       | 4.27 ms                                                         | 4.22 ms: 1.01x faster                                                  |
| pprint_pformat             | 1.33 sec                                                        | 1.31 sec: 1.01x faster                                                 |
| logging_format             | 8.72 us                                                         | 8.62 us: 1.01x faster                                                  |
| shortest_path              | 290 ms                                                          | 288 ms: 1.01x faster                                                   |
| sqlglot_optimize           | 41.4 ms                                                         | 41.3 ms: 1.00x faster                                                  |
| xml_etree_parse            | 107 ms                                                          | 108 ms: 1.01x slower                                                   |
| pathlib                    | 82.9 ms                                                         | 83.7 ms: 1.01x slower                                                  |
| sqlite_synth               | 1.95 us                                                         | 1.98 us: 1.01x slower                                                  |
| sympy_expand               | 373 ms                                                          | 378 ms: 1.01x slower                                                   |
| sympy_str                  | 212 ms                                                          | 215 ms: 1.01x slower                                                   |
| asyncio_websockets         | 363 ms                                                          | 369 ms: 1.02x slower                                                   |
| coroutines                 | 16.2 ms                                                         | 16.5 ms: 1.02x slower                                                  |
| typing_runtime_protocols   | 138 us                                                          | 140 us: 1.02x slower                                                   |
| float                      | 54.6 ms                                                         | 55.6 ms: 1.02x slower                                                  |
| gc_traversal               | 1.75 ms                                                         | 1.78 ms: 1.02x slower                                                  |
| bpe_tokeniser              | 3.46 sec                                                        | 3.56 sec: 1.03x slower                                                 |
| sphinx                     | 719 ms                                                          | 739 ms: 1.03x slower                                                   |
| regex_compile              | 101 ms                                                          | 104 ms: 1.03x slower                                                   |
| pycparser                  | 872 ms                                                          | 900 ms: 1.03x slower                                                   |
| unpickle_pure_python       | 160 us                                                          | 166 us: 1.03x slower                                                   |
| docutils                   | 1.78 sec                                                        | 1.84 sec: 1.04x slower                                                 |
| fannkuch                   | 299 ms                                                          | 309 ms: 1.04x slower                                                   |
| sympy_integrate            | 15.0 ms                                                         | 15.6 ms: 1.04x slower                                                  |
| dulwich_log                | 48.8 ms                                                         | 50.7 ms: 1.04x slower                                                  |
| nqueens                    | 72.1 ms                                                         | 75.2 ms: 1.04x slower                                                  |
| sqlglot_transpile          | 1.24 ms                                                         | 1.29 ms: 1.05x slower                                                  |
| comprehensions             | 12.5 us                                                         | 13.2 us: 1.05x slower                                                  |
| mdp                        | 1.62 sec                                                        | 1.72 sec: 1.06x slower                                                 |
| sqlglot_parse              | 1.00 ms                                                         | 1.06 ms: 1.06x slower                                                  |
| scimark_monte_carlo        | 47.7 ms                                                         | 50.5 ms: 1.06x slower                                                  |
| xml_etree_iterparse        | 62.6 ms                                                         | 66.7 ms: 1.07x slower                                                  |
| meteor_contest             | 74.6 ms                                                         | 79.6 ms: 1.07x slower                                                  |
| chaos                      | 50.2 ms                                                         | 54.0 ms: 1.08x slower                                                  |
| scimark_sor                | 85.9 ms                                                         | 93.1 ms: 1.08x slower                                                  |
| scimark_sparse_mat_mult    | 2.84 ms                                                         | 3.08 ms: 1.09x slower                                                  |
| richards                   | 32.7 ms                                                         | 35.6 ms: 1.09x slower                                                  |
| regex_dna                  | 114 ms                                                          | 124 ms: 1.09x slower                                                   |
| pyflate                    | 320 ms                                                          | 349 ms: 1.09x slower                                                   |
| mako                       | 7.09 ms                                                         | 7.74 ms: 1.09x slower                                                  |
| async_generators           | 270 ms                                                          | 295 ms: 1.10x slower                                                   |
| hexiom                     | 4.44 ms                                                         | 4.88 ms: 1.10x slower                                                  |
| xml_etree_process          | 44.2 ms                                                         | 48.8 ms: 1.11x slower                                                  |
| xml_etree_generate         | 61.4 ms                                                         | 68.0 ms: 1.11x slower                                                  |
| crypto_pyaes               | 56.9 ms                                                         | 63.0 ms: 1.11x slower                                                  |
| nbody                      | 80.0 ms                                                         | 89.2 ms: 1.12x slower                                                  |
| django_template            | 29.8 ms                                                         | 33.3 ms: 1.12x slower                                                  |
| pickle_pure_python         | 231 us                                                          | 258 us: 1.12x slower                                                   |
| scimark_fft                | 205 ms                                                          | 229 ms: 1.12x slower                                                   |
| richards_super             | 36.7 ms                                                         | 41.5 ms: 1.13x slower                                                  |
| scimark_lu                 | 60.2 ms                                                         | 68.2 ms: 1.13x slower                                                  |
| generators                 | 21.8 ms                                                         | 24.7 ms: 1.13x slower                                                  |
| deltablue                  | 2.33 ms                                                         | 2.68 ms: 1.15x slower                                                  |
| json_dumps                 | 7.30 ms                                                         | 8.76 ms: 1.20x slower                                                  |
| logging_silent             | 60.3 ns                                                         | 73.6 ns: 1.22x slower                                                  |
| many_optionals             | 436 us                                                          | 537 us: 1.23x slower                                                   |
| raytrace                   | 201 ms                                                          | 252 ms: 1.25x slower                                                   |
| subparsers                 | 14.8 ms                                                         | 20.9 ms: 1.41x slower                                                  |
| Geometric mean             | (ref)                                                           | 1.03x faster                                                           |

Benchmark hidden because not significant (6): k_core, bench_thread_pool, sympy_sum, spectral_norm, create_gc_cycles, regex_v8
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (1) of results/bm-20250107-3.14.0a3+-f098037/bm-20250107-pythonperf1_win32-x86-brandtbucher-nojit-3.14.0a3+-f098037.json: mypy2

- Geometric mean (including insignificant results): 1.035x faster

# HPT report

- Reliability score: 93.04% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown