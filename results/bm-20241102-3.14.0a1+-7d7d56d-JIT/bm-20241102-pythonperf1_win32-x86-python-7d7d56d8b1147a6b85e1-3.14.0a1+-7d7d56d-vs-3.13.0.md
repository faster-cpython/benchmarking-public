# Results vs. 3.13.0

- fork: python
- ref: 7d7d56d8b1147a6b85e1
- machine: windows-x86
- commit hash: 7d7d56d
- commit date: 2024-11-02
- overall geometric mean: 1.072x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.08x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241102-pythonperf1_win32-x86-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 255 ms                                                          | 293 ms: 1.15x slower                                                            |
| docutils       | 1.80 sec                                                        | 2.15 sec: 1.19x slower                                                          |
| html5lib       | 47.1 ms                                                         | 49.7 ms: 1.06x slower                                                           |
| sphinx         | 729 ms                                                          | 913 ms: 1.25x slower                                                            |
| tornado_http   | 105 ms                                                          | 110 ms: 1.05x slower                                                            |
| Geometric mean | (ref)                                                           | 1.14x slower                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241102-pythonperf1_win32-x86-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d |
|---------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_memoization_tg | 287 ms                                                          | 270 ms: 1.06x faster                                                            |
| async_tree_cpu_io_mixed   | 490 ms                                                          | 500 ms: 1.02x slower                                                            |
| async_tree_none_tg        | 216 ms                                                          | 222 ms: 1.03x slower                                                            |
| coroutines                | 16.1 ms                                                         | 16.6 ms: 1.03x slower                                                           |
| asyncio_websockets        | 352 ms                                                          | 376 ms: 1.07x slower                                                            |
| async_tree_io             | 530 ms                                                          | 573 ms: 1.08x slower                                                            |
| async_tree_io_tg          | 499 ms                                                          | 572 ms: 1.15x slower                                                            |
| async_generators          | 267 ms                                                          | 332 ms: 1.24x slower                                                            |
| Geometric mean            | (ref)                                                           | 1.05x slower                                                                    |

Benchmark hidden because not significant (3): async_tree_memoization, async_tree_none, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241102-pythonperf1_win32-x86-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pidigits       | 204 ms                                                          | 202 ms: 1.01x faster                                                            |
| nbody          | 81.4 ms                                                         | 95.8 ms: 1.18x slower                                                           |
| Geometric mean | (ref)                                                           | 1.05x slower                                                                    |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241102-pythonperf1_win32-x86-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_v8       | 15.5 ms                                                         | 16.1 ms: 1.04x slower                                                           |
| regex_compile  | 101 ms                                                          | 124 ms: 1.23x slower                                                            |
| Geometric mean | (ref)                                                           | 1.06x slower                                                                    |

Benchmark hidden because not significant (2): regex_dna, regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241102-pythonperf1_win32-x86-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 1.74 sec                                                        | 1.84 sec: 1.06x slower                                                          |
| xml_etree_parse      | 102 ms                                                          | 112 ms: 1.09x slower                                                            |
| xml_etree_iterparse  | 61.3 ms                                                         | 69.6 ms: 1.14x slower                                                           |
| json_dumps           | 7.53 ms                                                         | 8.86 ms: 1.18x slower                                                           |
| xml_etree_generate   | 61.9 ms                                                         | 74.2 ms: 1.20x slower                                                           |
| unpickle_pure_python | 162 us                                                          | 194 us: 1.20x slower                                                            |
| xml_etree_process    | 44.6 ms                                                         | 56.0 ms: 1.26x slower                                                           |
| pickle_pure_python   | 239 us                                                          | 301 us: 1.26x slower                                                            |
| Geometric mean       | (ref)                                                           | 1.15x slower                                                                    |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241102-pythonperf1_win32-x86-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 28.3 ms                                                         | 25.9 ms: 1.09x faster                                                           |
| python_startup_no_site | 20.2 ms                                                         | 19.9 ms: 1.01x faster                                                           |
| Geometric mean         | (ref)                                                           | 1.05x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241102-pythonperf1_win32-x86-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 7.02 ms                                                         | 7.33 ms: 1.04x slower                                                           |
| django_template | 32.0 ms                                                         | 37.2 ms: 1.16x slower                                                           |
| genshi_xml      | 49.0 ms                                                         | 60.0 ms: 1.22x slower                                                           |
| genshi_text     | 21.7 ms                                                         | 27.7 ms: 1.27x slower                                                           |
| Geometric mean  | (ref)                                                           | 1.17x slower                                                                    |

All benchmarks:
===============

| Benchmark                 | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241102-pythonperf1_win32-x86-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d |
|---------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| thrift                    | 10.3 ms                                                         | 792 us: 12.95x faster                                                           |
| coverage                  | 326 ms                                                          | 50.7 ms: 6.44x faster                                                           |
| sqlglot_normalize         | 223 ms                                                          | 115 ms: 1.93x faster                                                            |
| deepcopy                  | 311 us                                                          | 274 us: 1.13x faster                                                            |
| python_startup            | 28.3 ms                                                         | 25.9 ms: 1.09x faster                                                           |
| deepcopy_memo             | 26.2 us                                                         | 24.0 us: 1.09x faster                                                           |
| deepcopy_reduce           | 2.94 us                                                         | 2.73 us: 1.08x faster                                                           |
| async_tree_memoization_tg | 287 ms                                                          | 270 ms: 1.06x faster                                                            |
| pathlib                   | 89.1 ms                                                         | 86.9 ms: 1.03x faster                                                           |
| python_startup_no_site    | 20.2 ms                                                         | 19.9 ms: 1.01x faster                                                           |
| pidigits                  | 204 ms                                                          | 202 ms: 1.01x faster                                                            |
| gc_traversal              | 1.76 ms                                                         | 1.79 ms: 1.01x slower                                                           |
| dulwich_log               | 50.2 ms                                                         | 50.8 ms: 1.01x slower                                                           |
| async_tree_cpu_io_mixed   | 490 ms                                                          | 500 ms: 1.02x slower                                                            |
| async_tree_none_tg        | 216 ms                                                          | 222 ms: 1.03x slower                                                            |
| coroutines                | 16.1 ms                                                         | 16.6 ms: 1.03x slower                                                           |
| regex_v8                  | 15.5 ms                                                         | 16.1 ms: 1.04x slower                                                           |
| mako                      | 7.02 ms                                                         | 7.33 ms: 1.04x slower                                                           |
| logging_format            | 8.59 us                                                         | 9.02 us: 1.05x slower                                                           |
| tornado_http              | 105 ms                                                          | 110 ms: 1.05x slower                                                            |
| html5lib                  | 47.1 ms                                                         | 49.7 ms: 1.06x slower                                                           |
| json                      | 4.40 ms                                                         | 4.65 ms: 1.06x slower                                                           |
| tomli_loads               | 1.74 sec                                                        | 1.84 sec: 1.06x slower                                                          |
| logging_simple            | 7.89 us                                                         | 8.40 us: 1.06x slower                                                           |
| asyncio_websockets        | 352 ms                                                          | 376 ms: 1.07x slower                                                            |
| bpe_tokeniser             | 3.49 sec                                                        | 3.74 sec: 1.07x slower                                                          |
| async_tree_io             | 530 ms                                                          | 573 ms: 1.08x slower                                                            |
| create_gc_cycles          | 1.08 ms                                                         | 1.17 ms: 1.08x slower                                                           |
| shortest_path             | 298 ms                                                          | 322 ms: 1.08x slower                                                            |
| pycparser                 | 869 ms                                                          | 942 ms: 1.08x slower                                                            |
| xml_etree_parse           | 102 ms                                                          | 112 ms: 1.09x slower                                                            |
| connected_components      | 266 ms                                                          | 292 ms: 1.10x slower                                                            |
| pprint_safe_repr          | 658 ms                                                          | 729 ms: 1.11x slower                                                            |
| mdp                       | 1.70 sec                                                        | 1.89 sec: 1.11x slower                                                          |
| scimark_sparse_mat_mult   | 2.88 ms                                                         | 3.21 ms: 1.11x slower                                                           |
| meteor_contest            | 78.1 ms                                                         | 87.9 ms: 1.12x slower                                                           |
| sympy_expand              | 377 ms                                                          | 427 ms: 1.13x slower                                                            |
| xml_etree_iterparse       | 61.3 ms                                                         | 69.6 ms: 1.14x slower                                                           |
| pprint_pformat            | 1.32 sec                                                        | 1.50 sec: 1.14x slower                                                          |
| spectral_norm             | 70.0 ms                                                         | 79.9 ms: 1.14x slower                                                           |
| async_tree_io_tg          | 499 ms                                                          | 572 ms: 1.15x slower                                                            |
| 2to3                      | 255 ms                                                          | 293 ms: 1.15x slower                                                            |
| fannkuch                  | 288 ms                                                          | 333 ms: 1.15x slower                                                            |
| sqlglot_parse             | 1.02 ms                                                         | 1.18 ms: 1.16x slower                                                           |
| django_template           | 32.0 ms                                                         | 37.2 ms: 1.16x slower                                                           |
| sympy_sum                 | 108 ms                                                          | 126 ms: 1.16x slower                                                            |
| sympy_str                 | 214 ms                                                          | 251 ms: 1.17x slower                                                            |
| json_dumps                | 7.53 ms                                                         | 8.86 ms: 1.18x slower                                                           |
| nbody                     | 81.4 ms                                                         | 95.8 ms: 1.18x slower                                                           |
| crypto_pyaes              | 56.6 ms                                                         | 67.0 ms: 1.18x slower                                                           |
| go                        | 111 ms                                                          | 131 ms: 1.18x slower                                                            |
| telco                     | 6.27 ms                                                         | 7.45 ms: 1.19x slower                                                           |
| docutils                  | 1.80 sec                                                        | 2.15 sec: 1.19x slower                                                          |
| xml_etree_generate        | 61.9 ms                                                         | 74.2 ms: 1.20x slower                                                           |
| unpickle_pure_python      | 162 us                                                          | 194 us: 1.20x slower                                                            |
| typing_runtime_protocols  | 141 us                                                          | 169 us: 1.20x slower                                                            |
| sqlglot_transpile         | 1.26 ms                                                         | 1.53 ms: 1.21x slower                                                           |
| genshi_xml                | 49.0 ms                                                         | 60.0 ms: 1.22x slower                                                           |
| scimark_lu                | 60.7 ms                                                         | 74.4 ms: 1.23x slower                                                           |
| regex_compile             | 101 ms                                                          | 124 ms: 1.23x slower                                                            |
| scimark_fft               | 204 ms                                                          | 251 ms: 1.23x slower                                                            |
| pyflate                   | 322 ms                                                          | 397 ms: 1.23x slower                                                            |
| logging_silent            | 62.4 ns                                                         | 77.2 ns: 1.24x slower                                                           |
| async_generators          | 267 ms                                                          | 332 ms: 1.24x slower                                                            |
| pylint                    | 225 ms                                                          | 279 ms: 1.24x slower                                                            |
| sphinx                    | 729 ms                                                          | 913 ms: 1.25x slower                                                            |
| xml_etree_process         | 44.6 ms                                                         | 56.0 ms: 1.26x slower                                                           |
| pickle_pure_python        | 239 us                                                          | 301 us: 1.26x slower                                                            |
| scimark_sor               | 85.8 ms                                                         | 108 ms: 1.26x slower                                                            |
| genshi_text               | 21.7 ms                                                         | 27.7 ms: 1.27x slower                                                           |
| sympy_integrate           | 15.2 ms                                                         | 19.8 ms: 1.30x slower                                                           |
| scimark_monte_carlo       | 48.7 ms                                                         | 63.9 ms: 1.31x slower                                                           |
| chaos                     | 49.4 ms                                                         | 65.9 ms: 1.33x slower                                                           |
| nqueens                   | 75.1 ms                                                         | 100 ms: 1.34x slower                                                            |
| sqlglot_optimize          | 42.4 ms                                                         | 56.9 ms: 1.34x slower                                                           |
| richards_super            | 37.0 ms                                                         | 50.2 ms: 1.35x slower                                                           |
| richards                  | 33.4 ms                                                         | 45.6 ms: 1.37x slower                                                           |
| comprehensions            | 13.1 us                                                         | 18.6 us: 1.41x slower                                                           |
| deltablue                 | 2.35 ms                                                         | 3.36 ms: 1.43x slower                                                           |
| k_core                    | 1.43 sec                                                        | 2.06 sec: 1.44x slower                                                          |
| hexiom                    | 4.60 ms                                                         | 7.33 ms: 1.60x slower                                                           |
| raytrace                  | 203 ms                                                          | 323 ms: 1.60x slower                                                            |
| generators                | 21.5 ms                                                         | 36.9 ms: 1.72x slower                                                           |
| Geometric mean            | (ref)                                                           | 1.08x slower                                                                    |

Benchmark hidden because not significant (9): bench_thread_pool, async_tree_memoization, regex_dna, regex_effbot, async_tree_none, json_loads, float, async_tree_cpu_io_mixed_tg, bench_mp_pool
Ignored benchmarks (4) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (1) of results/bm-20241102-3.14.0a1+-7d7d56d-JIT/bm-20241102-pythonperf1_win32-x86-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d.json: sqlite_synth

- Geometric mean (including insignificant results): 1.072x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.10x
- 95% likely to have a slowdown of 1.09x
- 99% likely to have a slowdown of 1.08x

# Memory
- memory change: unknown