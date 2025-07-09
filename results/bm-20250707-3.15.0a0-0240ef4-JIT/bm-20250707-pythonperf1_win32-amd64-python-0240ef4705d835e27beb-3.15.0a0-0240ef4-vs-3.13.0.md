# Results vs. 3.13.0

- fork: python
- ref: 0240ef4705d835e27beb
- machine: windows-amd64
- commit hash: 0240ef4
- commit date: 2025-07-07
- overall geometric mean: 1.310x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.20x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250707-pythonperf1_win32-amd64-python-0240ef4705d835e27beb-3.15.0a0-0240ef4 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 250 ms                                                          | 216 ms: 1.16x faster                                                             |
| docutils       | 1.78 sec                                                        | 1.65 sec: 1.08x faster                                                           |
| html5lib       | 47.5 ms                                                         | 37.8 ms: 1.26x faster                                                            |
| sphinx         | 719 ms                                                          | 635 ms: 1.13x faster                                                             |
| Geometric mean | (ref)                                                           | 1.15x faster                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250707-pythonperf1_win32-amd64-python-0240ef4705d835e27beb-3.15.0a0-0240ef4 |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| asyncio_websockets         | 363 ms                                                          | 158 ms: 2.30x faster                                                             |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 332 ms: 1.46x faster                                                             |
| async_tree_none            | 245 ms                                                          | 168 ms: 1.45x faster                                                             |
| async_tree_memoization     | 297 ms                                                          | 204 ms: 1.45x faster                                                             |
| async_tree_memoization_tg  | 282 ms                                                          | 208 ms: 1.36x faster                                                             |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 341 ms: 1.34x faster                                                             |
| async_tree_io              | 526 ms                                                          | 394 ms: 1.33x faster                                                             |
| async_tree_io_tg           | 494 ms                                                          | 383 ms: 1.29x faster                                                             |
| async_tree_none_tg         | 214 ms                                                          | 169 ms: 1.27x faster                                                             |
| coroutines                 | 16.2 ms                                                         | 14.5 ms: 1.12x faster                                                            |
| async_generators           | 270 ms                                                          | 243 ms: 1.11x faster                                                             |
| Geometric mean             | (ref)                                                           | 1.38x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250707-pythonperf1_win32-amd64-python-0240ef4705d835e27beb-3.15.0a0-0240ef4 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| nbody          | 80.0 ms                                                         | 53.7 ms: 1.49x faster                                                            |
| pidigits       | 201 ms                                                          | 147 ms: 1.37x faster                                                             |
| float          | 54.6 ms                                                         | 43.4 ms: 1.26x faster                                                            |
| Geometric mean | (ref)                                                           | 1.37x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250707-pythonperf1_win32-amd64-python-0240ef4705d835e27beb-3.15.0a0-0240ef4 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 101 ms                                                          | 78.2 ms: 1.29x faster                                                            |
| regex_v8       | 16.8 ms                                                         | 14.3 ms: 1.18x faster                                                            |
| regex_effbot   | 1.80 ms                                                         | 1.58 ms: 1.14x faster                                                            |
| regex_dna      | 114 ms                                                          | 118 ms: 1.04x slower                                                             |
| Geometric mean | (ref)                                                           | 1.14x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250707-pythonperf1_win32-amd64-python-0240ef4705d835e27beb-3.15.0a0-0240ef4 |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| tomli_loads          | 1.71 sec                                                        | 1.13 sec: 1.52x faster                                                           |
| json_loads           | 21.6 us                                                         | 14.5 us: 1.50x faster                                                            |
| unpickle_pure_python | 160 us                                                          | 108 us: 1.48x faster                                                             |
| xml_etree_process    | 44.2 ms                                                         | 34.9 ms: 1.26x faster                                                            |
| xml_etree_parse      | 107 ms                                                          | 86.1 ms: 1.25x faster                                                            |
| xml_etree_generate   | 61.4 ms                                                         | 49.9 ms: 1.23x faster                                                            |
| json_dumps           | 7.30 ms                                                         | 6.32 ms: 1.16x faster                                                            |
| pickle_pure_python   | 231 us                                                          | 205 us: 1.13x faster                                                             |
| xml_etree_iterparse  | 62.6 ms                                                         | 61.7 ms: 1.01x faster                                                            |
| Geometric mean       | (ref)                                                           | 1.27x faster                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250707-pythonperf1_win32-amd64-python-0240ef4705d835e27beb-3.15.0a0-0240ef4 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup | 28.3 ms                                                         | 25.6 ms: 1.10x faster                                                            |
| Geometric mean | (ref)                                                           | 1.05x faster                                                                     |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250707-pythonperf1_win32-amd64-python-0240ef4705d835e27beb-3.15.0a0-0240ef4 |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| genshi_xml      | 50.1 ms                                                         | 33.7 ms: 1.49x faster                                                            |
| genshi_text     | 21.5 ms                                                         | 15.1 ms: 1.42x faster                                                            |
| mako            | 7.09 ms                                                         | 5.46 ms: 1.30x faster                                                            |
| django_template | 29.8 ms                                                         | 24.5 ms: 1.22x faster                                                            |
| Geometric mean  | (ref)                                                           | 1.35x faster                                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250707-pythonperf1_win32-amd64-python-0240ef4705d835e27beb-3.15.0a0-0240ef4 |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| thrift                     | 9.98 ms                                                         | 491 us: 20.30x faster                                                            |
| coverage                   | 324 ms                                                          | 50.6 ms: 6.40x faster                                                            |
| pathlib                    | 82.9 ms                                                         | 29.1 ms: 2.85x faster                                                            |
| asyncio_websockets         | 363 ms                                                          | 158 ms: 2.30x faster                                                             |
| mdp                        | 1.62 sec                                                        | 793 ms: 2.05x faster                                                             |
| deepcopy                   | 314 us                                                          | 170 us: 1.84x faster                                                             |
| telco                      | 6.96 ms                                                         | 4.30 ms: 1.62x faster                                                            |
| deepcopy_reduce            | 2.92 us                                                         | 1.82 us: 1.60x faster                                                            |
| tomli_loads                | 1.71 sec                                                        | 1.13 sec: 1.52x faster                                                           |
| json_loads                 | 21.6 us                                                         | 14.5 us: 1.50x faster                                                            |
| nbody                      | 80.0 ms                                                         | 53.7 ms: 1.49x faster                                                            |
| genshi_xml                 | 50.1 ms                                                         | 33.7 ms: 1.49x faster                                                            |
| unpickle_pure_python       | 160 us                                                          | 108 us: 1.48x faster                                                             |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 332 ms: 1.46x faster                                                             |
| async_tree_none            | 245 ms                                                          | 168 ms: 1.45x faster                                                             |
| async_tree_memoization     | 297 ms                                                          | 204 ms: 1.45x faster                                                             |
| pprint_safe_repr           | 648 ms                                                          | 447 ms: 1.45x faster                                                             |
| pprint_pformat             | 1.33 sec                                                        | 923 ms: 1.44x faster                                                             |
| json                       | 4.27 ms                                                         | 2.97 ms: 1.44x faster                                                            |
| go                         | 109 ms                                                          | 76.2 ms: 1.43x faster                                                            |
| genshi_text                | 21.5 ms                                                         | 15.1 ms: 1.42x faster                                                            |
| deepcopy_memo              | 25.4 us                                                         | 18.0 us: 1.42x faster                                                            |
| pidigits                   | 201 ms                                                          | 147 ms: 1.37x faster                                                             |
| fannkuch                   | 299 ms                                                          | 219 ms: 1.37x faster                                                             |
| async_tree_memoization_tg  | 282 ms                                                          | 208 ms: 1.36x faster                                                             |
| scimark_fft                | 205 ms                                                          | 152 ms: 1.34x faster                                                             |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 341 ms: 1.34x faster                                                             |
| bpe_tokeniser              | 3.46 sec                                                        | 2.59 sec: 1.34x faster                                                           |
| async_tree_io              | 526 ms                                                          | 394 ms: 1.33x faster                                                             |
| logging_format             | 8.72 us                                                         | 6.69 us: 1.30x faster                                                            |
| mako                       | 7.09 ms                                                         | 5.46 ms: 1.30x faster                                                            |
| typing_runtime_protocols   | 138 us                                                          | 106 us: 1.30x faster                                                             |
| regex_compile              | 101 ms                                                          | 78.2 ms: 1.29x faster                                                            |
| logging_simple             | 7.99 us                                                         | 6.19 us: 1.29x faster                                                            |
| async_tree_io_tg           | 494 ms                                                          | 383 ms: 1.29x faster                                                             |
| sympy_expand               | 373 ms                                                          | 294 ms: 1.27x faster                                                             |
| async_tree_none_tg         | 214 ms                                                          | 169 ms: 1.27x faster                                                             |
| pyflate                    | 320 ms                                                          | 252 ms: 1.27x faster                                                             |
| xml_etree_process          | 44.2 ms                                                         | 34.9 ms: 1.26x faster                                                            |
| chaos                      | 50.2 ms                                                         | 39.9 ms: 1.26x faster                                                            |
| float                      | 54.6 ms                                                         | 43.4 ms: 1.26x faster                                                            |
| html5lib                   | 47.5 ms                                                         | 37.8 ms: 1.26x faster                                                            |
| pycparser                  | 872 ms                                                          | 698 ms: 1.25x faster                                                             |
| sqlite_synth               | 1.95 us                                                         | 1.57 us: 1.25x faster                                                            |
| xml_etree_parse            | 107 ms                                                          | 86.1 ms: 1.25x faster                                                            |
| sympy_str                  | 212 ms                                                          | 170 ms: 1.25x faster                                                             |
| crypto_pyaes               | 56.9 ms                                                         | 45.8 ms: 1.24x faster                                                            |
| scimark_sparse_mat_mult    | 2.84 ms                                                         | 2.29 ms: 1.24x faster                                                            |
| nqueens                    | 72.1 ms                                                         | 58.5 ms: 1.23x faster                                                            |
| xml_etree_generate         | 61.4 ms                                                         | 49.9 ms: 1.23x faster                                                            |
| richards                   | 32.7 ms                                                         | 26.7 ms: 1.23x faster                                                            |
| django_template            | 29.8 ms                                                         | 24.5 ms: 1.22x faster                                                            |
| sympy_sum                  | 106 ms                                                          | 87.0 ms: 1.21x faster                                                            |
| richards_super             | 36.7 ms                                                         | 30.4 ms: 1.21x faster                                                            |
| comprehensions             | 12.5 us                                                         | 10.5 us: 1.20x faster                                                            |
| dulwich_log                | 48.8 ms                                                         | 40.8 ms: 1.19x faster                                                            |
| sympy_integrate            | 15.0 ms                                                         | 12.6 ms: 1.19x faster                                                            |
| regex_v8                   | 16.8 ms                                                         | 14.3 ms: 1.18x faster                                                            |
| scimark_monte_carlo        | 47.7 ms                                                         | 40.8 ms: 1.17x faster                                                            |
| 2to3                       | 250 ms                                                          | 216 ms: 1.16x faster                                                             |
| json_dumps                 | 7.30 ms                                                         | 6.32 ms: 1.16x faster                                                            |
| pylint                     | 227 ms                                                          | 198 ms: 1.14x faster                                                             |
| scimark_sor                | 85.9 ms                                                         | 75.3 ms: 1.14x faster                                                            |
| regex_effbot               | 1.80 ms                                                         | 1.58 ms: 1.14x faster                                                            |
| sphinx                     | 719 ms                                                          | 635 ms: 1.13x faster                                                             |
| pickle_pure_python         | 231 us                                                          | 205 us: 1.13x faster                                                             |
| raytrace                   | 201 ms                                                          | 179 ms: 1.12x faster                                                             |
| coroutines                 | 16.2 ms                                                         | 14.5 ms: 1.12x faster                                                            |
| generators                 | 21.8 ms                                                         | 19.4 ms: 1.12x faster                                                            |
| async_generators           | 270 ms                                                          | 243 ms: 1.11x faster                                                             |
| logging_silent             | 60.3 ns                                                         | 54.4 ns: 1.11x faster                                                            |
| python_startup             | 28.3 ms                                                         | 25.6 ms: 1.10x faster                                                            |
| deltablue                  | 2.33 ms                                                         | 2.13 ms: 1.10x faster                                                            |
| spectral_norm              | 69.4 ms                                                         | 63.5 ms: 1.09x faster                                                            |
| hexiom                     | 4.44 ms                                                         | 4.09 ms: 1.09x faster                                                            |
| docutils                   | 1.78 sec                                                        | 1.65 sec: 1.08x faster                                                           |
| meteor_contest             | 74.6 ms                                                         | 71.1 ms: 1.05x faster                                                            |
| xml_etree_iterparse        | 62.6 ms                                                         | 61.7 ms: 1.01x faster                                                            |
| scimark_lu                 | 60.2 ms                                                         | 61.1 ms: 1.01x slower                                                            |
| many_optionals             | 436 us                                                          | 447 us: 1.02x slower                                                             |
| regex_dna                  | 114 ms                                                          | 118 ms: 1.04x slower                                                             |
| subparsers                 | 14.8 ms                                                         | 17.1 ms: 1.16x slower                                                            |
| k_core                     | 1.38 sec                                                        | 1.62 sec: 1.18x slower                                                           |
| gc_traversal               | 1.75 ms                                                         | 2.11 ms: 1.20x slower                                                            |
| connected_components       | 267 ms                                                          | 324 ms: 1.21x slower                                                             |
| shortest_path              | 290 ms                                                          | 357 ms: 1.23x slower                                                             |
| create_gc_cycles           | 1.06 ms                                                         | 1.31 ms: 1.24x slower                                                            |
| Geometric mean             | (ref)                                                           | 1.31x faster                                                                     |

Benchmark hidden because not significant (1): python_startup_no_site
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250707-3.15.0a0-0240ef4-JIT/bm-20250707-pythonperf1_win32-amd64-python-0240ef4705d835e27beb-3.15.0a0-0240ef4.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.310x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.23x
- 95% likely to have a speedup of 1.22x
- 99% likely to have a speedup of 1.20x

# Memory
- memory change: unknown