# Results vs. 3.13.0

- fork: python
- ref: c9932a9ec8a3077933a8
- machine: windows-x86
- commit hash: c9932a9
- commit date: 2025-03-01
- overall geometric mean: 1.081x faster
- HPT reliability: 97.71%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250301-pythonperf1_win32-x86-python-c9932a9ec8a3077933a8-3.14.0a5+-c9932a9 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| docutils       | 1.78 sec                                                        | 1.79 sec: 1.01x slower                                                          |
| html5lib       | 47.5 ms                                                         | 43.6 ms: 1.09x faster                                                           |
| sphinx         | 719 ms                                                          | 733 ms: 1.02x slower                                                            |
| Geometric mean | (ref)                                                           | 1.01x faster                                                                    |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250301-pythonperf1_win32-x86-python-c9932a9ec8a3077933a8-3.14.0a5+-c9932a9 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_memoization     | 297 ms                                                          | 227 ms: 1.31x faster                                                            |
| async_tree_none            | 245 ms                                                          | 188 ms: 1.30x faster                                                            |
| async_tree_memoization_tg  | 282 ms                                                          | 217 ms: 1.30x faster                                                            |
| async_tree_io              | 526 ms                                                          | 409 ms: 1.28x faster                                                            |
| async_tree_io_tg           | 494 ms                                                          | 396 ms: 1.25x faster                                                            |
| async_tree_none_tg         | 214 ms                                                          | 172 ms: 1.24x faster                                                            |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 441 ms: 1.10x faster                                                            |
| async_generators           | 270 ms                                                          | 247 ms: 1.09x faster                                                            |
| coroutines                 | 16.2 ms                                                         | 15.0 ms: 1.08x faster                                                           |
| asyncio_websockets         | 363 ms                                                          | 346 ms: 1.05x faster                                                            |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 441 ms: 1.03x faster                                                            |
| Geometric mean             | (ref)                                                           | 1.18x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250301-pythonperf1_win32-x86-python-c9932a9ec8a3077933a8-3.14.0a5+-c9932a9 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 54.6 ms                                                         | 48.8 ms: 1.12x faster                                                           |
| nbody          | 80.0 ms                                                         | 73.5 ms: 1.09x faster                                                           |
| pidigits       | 201 ms                                                          | 216 ms: 1.08x slower                                                            |
| Geometric mean | (ref)                                                           | 1.04x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250301-pythonperf1_win32-x86-python-c9932a9ec8a3077933a8-3.14.0a5+-c9932a9 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 101 ms                                                          | 98.4 ms: 1.03x faster                                                           |
| regex_effbot   | 1.80 ms                                                         | 1.93 ms: 1.07x slower                                                           |
| regex_dna      | 114 ms                                                          | 127 ms: 1.11x slower                                                            |
| Geometric mean | (ref)                                                           | 1.05x slower                                                                    |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250301-pythonperf1_win32-x86-python-c9932a9ec8a3077933a8-3.14.0a5+-c9932a9 |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 1.71 sec                                                        | 1.57 sec: 1.09x faster                                                          |
| json_loads           | 21.6 us                                                         | 21.5 us: 1.01x faster                                                           |
| unpickle_pure_python | 160 us                                                          | 166 us: 1.04x slower                                                            |
| json_dumps           | 7.30 ms                                                         | 7.60 ms: 1.04x slower                                                           |
| xml_etree_parse      | 107 ms                                                          | 113 ms: 1.05x slower                                                            |
| pickle_pure_python   | 231 us                                                          | 248 us: 1.07x slower                                                            |
| xml_etree_process    | 44.2 ms                                                         | 48.9 ms: 1.11x slower                                                           |
| xml_etree_generate   | 61.4 ms                                                         | 69.5 ms: 1.13x slower                                                           |
| xml_etree_iterparse  | 62.6 ms                                                         | 72.8 ms: 1.16x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.05x slower                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250301-pythonperf1_win32-x86-python-c9932a9ec8a3077933a8-3.14.0a5+-c9932a9 |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 28.3 ms                                                         | 29.6 ms: 1.05x slower                                                           |
| python_startup_no_site | 19.7 ms                                                         | 22.6 ms: 1.15x slower                                                           |
| Geometric mean         | (ref)                                                           | 1.10x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250301-pythonperf1_win32-x86-python-c9932a9ec8a3077933a8-3.14.0a5+-c9932a9 |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_xml      | 50.1 ms                                                         | 41.6 ms: 1.20x faster                                                           |
| genshi_text     | 21.5 ms                                                         | 18.2 ms: 1.18x faster                                                           |
| django_template | 29.8 ms                                                         | 30.5 ms: 1.03x slower                                                           |
| mako            | 7.09 ms                                                         | 8.31 ms: 1.17x slower                                                           |
| Geometric mean  | (ref)                                                           | 1.04x faster                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250301-pythonperf1_win32-x86-python-c9932a9ec8a3077933a8-3.14.0a5+-c9932a9 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| thrift                     | 9.98 ms                                                         | 678 us: 14.72x faster                                                           |
| coverage                   | 324 ms                                                          | 57.6 ms: 5.62x faster                                                           |
| pathlib                    | 82.9 ms                                                         | 35.1 ms: 2.36x faster                                                           |
| deepcopy                   | 314 us                                                          | 212 us: 1.48x faster                                                            |
| deepcopy_reduce            | 2.92 us                                                         | 2.10 us: 1.39x faster                                                           |
| async_tree_memoization     | 297 ms                                                          | 227 ms: 1.31x faster                                                            |
| async_tree_none            | 245 ms                                                          | 188 ms: 1.30x faster                                                            |
| async_tree_memoization_tg  | 282 ms                                                          | 217 ms: 1.30x faster                                                            |
| async_tree_io              | 526 ms                                                          | 409 ms: 1.28x faster                                                            |
| async_tree_io_tg           | 494 ms                                                          | 396 ms: 1.25x faster                                                            |
| deepcopy_memo              | 25.4 us                                                         | 20.4 us: 1.24x faster                                                           |
| async_tree_none_tg         | 214 ms                                                          | 172 ms: 1.24x faster                                                            |
| genshi_xml                 | 50.1 ms                                                         | 41.6 ms: 1.20x faster                                                           |
| go                         | 109 ms                                                          | 90.7 ms: 1.20x faster                                                           |
| genshi_text                | 21.5 ms                                                         | 18.2 ms: 1.18x faster                                                           |
| telco                      | 6.96 ms                                                         | 6.01 ms: 1.16x faster                                                           |
| pprint_safe_repr           | 648 ms                                                          | 567 ms: 1.14x faster                                                            |
| pprint_pformat             | 1.33 sec                                                        | 1.17 sec: 1.13x faster                                                          |
| float                      | 54.6 ms                                                         | 48.8 ms: 1.12x faster                                                           |
| generators                 | 21.8 ms                                                         | 19.6 ms: 1.11x faster                                                           |
| spectral_norm              | 69.4 ms                                                         | 62.5 ms: 1.11x faster                                                           |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 441 ms: 1.10x faster                                                            |
| sympy_expand               | 373 ms                                                          | 342 ms: 1.09x faster                                                            |
| async_generators           | 270 ms                                                          | 247 ms: 1.09x faster                                                            |
| tomli_loads                | 1.71 sec                                                        | 1.57 sec: 1.09x faster                                                          |
| html5lib                   | 47.5 ms                                                         | 43.6 ms: 1.09x faster                                                           |
| nbody                      | 80.0 ms                                                         | 73.5 ms: 1.09x faster                                                           |
| coroutines                 | 16.2 ms                                                         | 15.0 ms: 1.08x faster                                                           |
| sympy_str                  | 212 ms                                                          | 199 ms: 1.07x faster                                                            |
| pylint                     | 227 ms                                                          | 214 ms: 1.06x faster                                                            |
| pycparser                  | 872 ms                                                          | 823 ms: 1.06x faster                                                            |
| typing_runtime_protocols   | 138 us                                                          | 130 us: 1.06x faster                                                            |
| scimark_sor                | 85.9 ms                                                         | 81.4 ms: 1.06x faster                                                           |
| scimark_monte_carlo        | 47.7 ms                                                         | 45.3 ms: 1.05x faster                                                           |
| asyncio_websockets         | 363 ms                                                          | 346 ms: 1.05x faster                                                            |
| sqlite_synth               | 1.95 us                                                         | 1.87 us: 1.04x faster                                                           |
| sqlglot_parse              | 1.00 ms                                                         | 961 us: 1.04x faster                                                            |
| logging_format             | 8.72 us                                                         | 8.37 us: 1.04x faster                                                           |
| sympy_sum                  | 106 ms                                                          | 102 ms: 1.04x faster                                                            |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 441 ms: 1.03x faster                                                            |
| scimark_sparse_mat_mult    | 2.84 ms                                                         | 2.76 ms: 1.03x faster                                                           |
| sqlglot_transpile          | 1.24 ms                                                         | 1.20 ms: 1.03x faster                                                           |
| regex_compile              | 101 ms                                                          | 98.4 ms: 1.03x faster                                                           |
| deltablue                  | 2.33 ms                                                         | 2.28 ms: 1.02x faster                                                           |
| sqlglot_normalize          | 216 ms                                                          | 212 ms: 1.02x faster                                                            |
| sympy_integrate            | 15.0 ms                                                         | 14.7 ms: 1.02x faster                                                           |
| logging_simple             | 7.99 us                                                         | 7.88 us: 1.01x faster                                                           |
| chaos                      | 50.2 ms                                                         | 49.8 ms: 1.01x faster                                                           |
| json_loads                 | 21.6 us                                                         | 21.5 us: 1.01x faster                                                           |
| bpe_tokeniser              | 3.46 sec                                                        | 3.44 sec: 1.01x faster                                                          |
| docutils                   | 1.78 sec                                                        | 1.79 sec: 1.01x slower                                                          |
| pyflate                    | 320 ms                                                          | 324 ms: 1.01x slower                                                            |
| fannkuch                   | 299 ms                                                          | 302 ms: 1.01x slower                                                            |
| json                       | 4.27 ms                                                         | 4.36 ms: 1.02x slower                                                           |
| sphinx                     | 719 ms                                                          | 733 ms: 1.02x slower                                                            |
| django_template            | 29.8 ms                                                         | 30.5 ms: 1.03x slower                                                           |
| scimark_fft                | 205 ms                                                          | 211 ms: 1.03x slower                                                            |
| unpickle_pure_python       | 160 us                                                          | 166 us: 1.04x slower                                                            |
| json_dumps                 | 7.30 ms                                                         | 7.60 ms: 1.04x slower                                                           |
| bench_mp_pool              | 90.6 ms                                                         | 94.5 ms: 1.04x slower                                                           |
| python_startup             | 28.3 ms                                                         | 29.6 ms: 1.05x slower                                                           |
| xml_etree_parse            | 107 ms                                                          | 113 ms: 1.05x slower                                                            |
| nqueens                    | 72.1 ms                                                         | 75.7 ms: 1.05x slower                                                           |
| comprehensions             | 12.5 us                                                         | 13.3 us: 1.06x slower                                                           |
| raytrace                   | 201 ms                                                          | 214 ms: 1.06x slower                                                            |
| regex_effbot               | 1.80 ms                                                         | 1.93 ms: 1.07x slower                                                           |
| pickle_pure_python         | 231 us                                                          | 248 us: 1.07x slower                                                            |
| pidigits                   | 201 ms                                                          | 216 ms: 1.08x slower                                                            |
| hexiom                     | 4.44 ms                                                         | 4.79 ms: 1.08x slower                                                           |
| meteor_contest             | 74.6 ms                                                         | 81.9 ms: 1.10x slower                                                           |
| create_gc_cycles           | 1.06 ms                                                         | 1.16 ms: 1.10x slower                                                           |
| xml_etree_process          | 44.2 ms                                                         | 48.9 ms: 1.11x slower                                                           |
| mdp                        | 1.62 sec                                                        | 1.80 sec: 1.11x slower                                                          |
| crypto_pyaes               | 56.9 ms                                                         | 63.3 ms: 1.11x slower                                                           |
| regex_dna                  | 114 ms                                                          | 127 ms: 1.11x slower                                                            |
| richards_super             | 36.7 ms                                                         | 41.0 ms: 1.12x slower                                                           |
| richards                   | 32.7 ms                                                         | 36.6 ms: 1.12x slower                                                           |
| logging_silent             | 60.3 ns                                                         | 67.9 ns: 1.13x slower                                                           |
| xml_etree_generate         | 61.4 ms                                                         | 69.5 ms: 1.13x slower                                                           |
| scimark_lu                 | 60.2 ms                                                         | 69.2 ms: 1.15x slower                                                           |
| python_startup_no_site     | 19.7 ms                                                         | 22.6 ms: 1.15x slower                                                           |
| xml_etree_iterparse        | 62.6 ms                                                         | 72.8 ms: 1.16x slower                                                           |
| many_optionals             | 436 us                                                          | 509 us: 1.17x slower                                                            |
| mako                       | 7.09 ms                                                         | 8.31 ms: 1.17x slower                                                           |
| bench_thread_pool          | 1.00 ms                                                         | 1.33 ms: 1.33x slower                                                           |
| subparsers                 | 14.8 ms                                                         | 20.0 ms: 1.35x slower                                                           |
| gc_traversal               | 1.75 ms                                                         | 2.44 ms: 1.39x slower                                                           |
| Geometric mean             | (ref)                                                           | 1.07x faster                                                                    |

Benchmark hidden because not significant (7): connected_components, shortest_path, dulwich_log, sqlglot_optimize, k_core, 2to3, regex_v8
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (8) of results/bm-20250301-3.14.0a5+-c9932a9-CLANG/bm-20250301-pythonperf1_win32-x86-python-c9932a9ec8a3077933a8-3.14.0a5+-c9932a9.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.081x faster

# HPT report

- Reliability score: 97.71% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown