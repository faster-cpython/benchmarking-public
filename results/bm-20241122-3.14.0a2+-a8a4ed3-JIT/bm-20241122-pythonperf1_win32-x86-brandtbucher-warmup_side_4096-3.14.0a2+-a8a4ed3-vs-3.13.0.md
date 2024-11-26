# Results vs. 3.13.0

- fork: brandtbucher
- ref: warmup_side_4096
- machine: windows-x86
- commit hash: a8a4ed3
- commit date: 2024-11-22
- overall geometric mean: 1.044x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241122-pythonperf1_win32-x86-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 255 ms                                                          | 260 ms: 1.02x slower                                                              |
| docutils       | 1.80 sec                                                        | 1.95 sec: 1.08x slower                                                            |
| html5lib       | 47.1 ms                                                         | 49.2 ms: 1.05x slower                                                             |
| sphinx         | 729 ms                                                          | 801 ms: 1.10x slower                                                              |
| Geometric mean | (ref)                                                           | 1.06x slower                                                                      |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241122-pythonperf1_win32-x86-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|----------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 287 ms                                                          | 264 ms: 1.09x faster                                                              |
| async_tree_none            | 245 ms                                                          | 240 ms: 1.02x faster                                                              |
| asyncio_websockets         | 352 ms                                                          | 349 ms: 1.01x faster                                                              |
| async_tree_cpu_io_mixed_tg | 469 ms                                                          | 474 ms: 1.01x slower                                                              |
| async_tree_cpu_io_mixed    | 490 ms                                                          | 500 ms: 1.02x slower                                                              |
| coroutines                 | 16.1 ms                                                         | 16.5 ms: 1.03x slower                                                             |
| async_tree_io              | 530 ms                                                          | 567 ms: 1.07x slower                                                              |
| async_tree_io_tg           | 499 ms                                                          | 542 ms: 1.08x slower                                                              |
| async_generators           | 267 ms                                                          | 319 ms: 1.20x slower                                                              |
| Geometric mean             | (ref)                                                           | 1.02x slower                                                                      |

Benchmark hidden because not significant (2): async_tree_none_tg, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241122-pythonperf1_win32-x86-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| pidigits       | 204 ms                                                          | 203 ms: 1.00x faster                                                              |
| nbody          | 81.4 ms                                                         | 94.9 ms: 1.17x slower                                                             |
| Geometric mean | (ref)                                                           | 1.05x slower                                                                      |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241122-pythonperf1_win32-x86-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_effbot   | 1.82 ms                                                         | 1.55 ms: 1.17x faster                                                             |
| regex_v8       | 15.5 ms                                                         | 15.6 ms: 1.01x slower                                                             |
| regex_compile  | 101 ms                                                          | 113 ms: 1.12x slower                                                              |
| Geometric mean | (ref)                                                           | 1.01x faster                                                                      |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241122-pythonperf1_win32-x86-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|----------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| json_loads           | 21.7 us                                                         | 21.3 us: 1.02x faster                                                             |
| tomli_loads          | 1.74 sec                                                        | 1.84 sec: 1.06x slower                                                            |
| xml_etree_parse      | 102 ms                                                          | 113 ms: 1.10x slower                                                              |
| xml_etree_iterparse  | 61.3 ms                                                         | 68.3 ms: 1.11x slower                                                             |
| xml_etree_generate   | 61.9 ms                                                         | 72.7 ms: 1.17x slower                                                             |
| json_dumps           | 7.53 ms                                                         | 9.01 ms: 1.20x slower                                                             |
| xml_etree_process    | 44.6 ms                                                         | 53.7 ms: 1.20x slower                                                             |
| pickle_pure_python   | 239 us                                                          | 296 us: 1.24x slower                                                              |
| unpickle_pure_python | 162 us                                                          | 207 us: 1.28x slower                                                              |
| Geometric mean       | (ref)                                                           | 1.15x slower                                                                      |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241122-pythonperf1_win32-x86-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup         | 28.3 ms                                                         | 25.7 ms: 1.10x faster                                                             |
| python_startup_no_site | 20.2 ms                                                         | 19.5 ms: 1.03x faster                                                             |
| Geometric mean         | (ref)                                                           | 1.07x faster                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241122-pythonperf1_win32-x86-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|-----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| mako            | 7.02 ms                                                         | 7.39 ms: 1.05x slower                                                             |
| django_template | 32.0 ms                                                         | 37.0 ms: 1.16x slower                                                             |
| genshi_xml      | 49.0 ms                                                         | 57.2 ms: 1.17x slower                                                             |
| genshi_text     | 21.7 ms                                                         | 25.9 ms: 1.19x slower                                                             |
| Geometric mean  | (ref)                                                           | 1.14x slower                                                                      |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241122-pythonperf1_win32-x86-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|----------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| thrift                     | 10.3 ms                                                         | 786 us: 13.06x faster                                                             |
| coverage                   | 326 ms                                                          | 55.0 ms: 5.93x faster                                                             |
| sqlglot_normalize          | 223 ms                                                          | 108 ms: 2.07x faster                                                              |
| regex_effbot               | 1.82 ms                                                         | 1.55 ms: 1.17x faster                                                             |
| deepcopy                   | 311 us                                                          | 278 us: 1.12x faster                                                              |
| python_startup             | 28.3 ms                                                         | 25.7 ms: 1.10x faster                                                             |
| deepcopy_memo              | 26.2 us                                                         | 24.0 us: 1.09x faster                                                             |
| async_tree_memoization_tg  | 287 ms                                                          | 264 ms: 1.09x faster                                                              |
| bench_mp_pool              | 93.6 ms                                                         | 87.2 ms: 1.07x faster                                                             |
| pathlib                    | 89.1 ms                                                         | 83.4 ms: 1.07x faster                                                             |
| gc_traversal               | 1.76 ms                                                         | 1.70 ms: 1.04x faster                                                             |
| python_startup_no_site     | 20.2 ms                                                         | 19.5 ms: 1.03x faster                                                             |
| deepcopy_reduce            | 2.94 us                                                         | 2.86 us: 1.03x faster                                                             |
| json_loads                 | 21.7 us                                                         | 21.3 us: 1.02x faster                                                             |
| async_tree_none            | 245 ms                                                          | 240 ms: 1.02x faster                                                              |
| asyncio_websockets         | 352 ms                                                          | 349 ms: 1.01x faster                                                              |
| dulwich_log                | 50.2 ms                                                         | 49.8 ms: 1.01x faster                                                             |
| pidigits                   | 204 ms                                                          | 203 ms: 1.00x faster                                                              |
| regex_v8                   | 15.5 ms                                                         | 15.6 ms: 1.01x slower                                                             |
| async_tree_cpu_io_mixed_tg | 469 ms                                                          | 474 ms: 1.01x slower                                                              |
| 2to3                       | 255 ms                                                          | 260 ms: 1.02x slower                                                              |
| async_tree_cpu_io_mixed    | 490 ms                                                          | 500 ms: 1.02x slower                                                              |
| coroutines                 | 16.1 ms                                                         | 16.5 ms: 1.03x slower                                                             |
| html5lib                   | 47.1 ms                                                         | 49.2 ms: 1.05x slower                                                             |
| logging_format             | 8.59 us                                                         | 9.01 us: 1.05x slower                                                             |
| json                       | 4.40 ms                                                         | 4.63 ms: 1.05x slower                                                             |
| mako                       | 7.02 ms                                                         | 7.39 ms: 1.05x slower                                                             |
| create_gc_cycles           | 1.08 ms                                                         | 1.15 ms: 1.06x slower                                                             |
| tomli_loads                | 1.74 sec                                                        | 1.84 sec: 1.06x slower                                                            |
| logging_simple             | 7.89 us                                                         | 8.40 us: 1.06x slower                                                             |
| sympy_sum                  | 108 ms                                                          | 115 ms: 1.07x slower                                                              |
| sympy_expand               | 377 ms                                                          | 403 ms: 1.07x slower                                                              |
| async_tree_io              | 530 ms                                                          | 567 ms: 1.07x slower                                                              |
| pycparser                  | 869 ms                                                          | 931 ms: 1.07x slower                                                              |
| shortest_path              | 298 ms                                                          | 319 ms: 1.07x slower                                                              |
| bpe_tokeniser              | 3.49 sec                                                        | 3.78 sec: 1.08x slower                                                            |
| docutils                   | 1.80 sec                                                        | 1.95 sec: 1.08x slower                                                            |
| async_tree_io_tg           | 499 ms                                                          | 542 ms: 1.08x slower                                                              |
| connected_components       | 266 ms                                                          | 289 ms: 1.09x slower                                                              |
| sympy_str                  | 214 ms                                                          | 233 ms: 1.09x slower                                                              |
| mdp                        | 1.70 sec                                                        | 1.85 sec: 1.09x slower                                                            |
| go                         | 111 ms                                                          | 121 ms: 1.09x slower                                                              |
| sphinx                     | 729 ms                                                          | 801 ms: 1.10x slower                                                              |
| xml_etree_parse            | 102 ms                                                          | 113 ms: 1.10x slower                                                              |
| pprint_safe_repr           | 658 ms                                                          | 731 ms: 1.11x slower                                                              |
| xml_etree_iterparse        | 61.3 ms                                                         | 68.3 ms: 1.11x slower                                                             |
| scimark_sparse_mat_mult    | 2.88 ms                                                         | 3.21 ms: 1.12x slower                                                             |
| sqlglot_transpile          | 1.26 ms                                                         | 1.42 ms: 1.12x slower                                                             |
| regex_compile              | 101 ms                                                          | 113 ms: 1.12x slower                                                              |
| sqlglot_parse              | 1.02 ms                                                         | 1.15 ms: 1.13x slower                                                             |
| meteor_contest             | 78.1 ms                                                         | 88.3 ms: 1.13x slower                                                             |
| pprint_pformat             | 1.32 sec                                                        | 1.51 sec: 1.14x slower                                                            |
| telco                      | 6.27 ms                                                         | 7.17 ms: 1.14x slower                                                             |
| fannkuch                   | 288 ms                                                          | 330 ms: 1.15x slower                                                              |
| sympy_integrate            | 15.2 ms                                                         | 17.5 ms: 1.15x slower                                                             |
| django_template            | 32.0 ms                                                         | 37.0 ms: 1.16x slower                                                             |
| nbody                      | 81.4 ms                                                         | 94.9 ms: 1.17x slower                                                             |
| genshi_xml                 | 49.0 ms                                                         | 57.2 ms: 1.17x slower                                                             |
| xml_etree_generate         | 61.9 ms                                                         | 72.7 ms: 1.17x slower                                                             |
| crypto_pyaes               | 56.6 ms                                                         | 66.7 ms: 1.18x slower                                                             |
| genshi_text                | 21.7 ms                                                         | 25.9 ms: 1.19x slower                                                             |
| spectral_norm              | 70.0 ms                                                         | 83.5 ms: 1.19x slower                                                             |
| async_generators           | 267 ms                                                          | 319 ms: 1.20x slower                                                              |
| typing_runtime_protocols   | 141 us                                                          | 169 us: 1.20x slower                                                              |
| json_dumps                 | 7.53 ms                                                         | 9.01 ms: 1.20x slower                                                             |
| sqlglot_optimize           | 42.4 ms                                                         | 50.8 ms: 1.20x slower                                                             |
| k_core                     | 1.43 sec                                                        | 1.72 sec: 1.20x slower                                                            |
| xml_etree_process          | 44.6 ms                                                         | 53.7 ms: 1.20x slower                                                             |
| scimark_lu                 | 60.7 ms                                                         | 74.0 ms: 1.22x slower                                                             |
| scimark_fft                | 204 ms                                                          | 250 ms: 1.23x slower                                                              |
| pickle_pure_python         | 239 us                                                          | 296 us: 1.24x slower                                                              |
| scimark_sor                | 85.8 ms                                                         | 106 ms: 1.24x slower                                                              |
| richards                   | 33.4 ms                                                         | 41.6 ms: 1.25x slower                                                             |
| pyflate                    | 322 ms                                                          | 408 ms: 1.27x slower                                                              |
| richards_super             | 37.0 ms                                                         | 47.4 ms: 1.28x slower                                                             |
| unpickle_pure_python       | 162 us                                                          | 207 us: 1.28x slower                                                              |
| scimark_monte_carlo        | 48.7 ms                                                         | 64.1 ms: 1.32x slower                                                             |
| nqueens                    | 75.1 ms                                                         | 98.9 ms: 1.32x slower                                                             |
| chaos                      | 49.4 ms                                                         | 65.7 ms: 1.33x slower                                                             |
| deltablue                  | 2.35 ms                                                         | 3.21 ms: 1.37x slower                                                             |
| comprehensions             | 13.1 us                                                         | 18.4 us: 1.40x slower                                                             |
| logging_silent             | 62.4 ns                                                         | 87.9 ns: 1.41x slower                                                             |
| raytrace                   | 203 ms                                                          | 303 ms: 1.49x slower                                                              |
| hexiom                     | 4.60 ms                                                         | 7.00 ms: 1.52x slower                                                             |
| generators                 | 21.5 ms                                                         | 36.7 ms: 1.71x slower                                                             |
| Geometric mean             | (ref)                                                           | 1.05x slower                                                                      |

Benchmark hidden because not significant (6): bench_thread_pool, async_tree_none_tg, async_tree_memoization, float, regex_dna, pylint
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (3) of results/bm-20241122-3.14.0a2+-a8a4ed3-JIT/bm-20241122-pythonperf1_win32-x86-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3.json: many_optionals, sqlite_synth, subparsers

- Geometric mean (including insignificant results): 1.044x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.07x
- 95% likely to have a slowdown of 1.07x
- 99% likely to have a slowdown of 1.06x

# Memory
- memory change: unknown