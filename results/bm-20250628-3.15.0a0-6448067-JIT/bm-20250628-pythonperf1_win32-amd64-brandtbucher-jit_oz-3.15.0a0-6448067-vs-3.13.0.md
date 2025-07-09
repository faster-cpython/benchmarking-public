# Results vs. 3.13.0

- fork: brandtbucher
- ref: jit_oz
- machine: windows-amd64
- commit hash: 6448067
- commit date: 2025-06-28
- overall geometric mean: 1.300x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.19x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250628-pythonperf1_win32-amd64-brandtbucher-jit_oz-3.15.0a0-6448067 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 250 ms                                                          | 218 ms: 1.15x faster                                                     |
| docutils       | 1.78 sec                                                        | 1.64 sec: 1.08x faster                                                   |
| html5lib       | 47.5 ms                                                         | 38.4 ms: 1.24x faster                                                    |
| sphinx         | 719 ms                                                          | 641 ms: 1.12x faster                                                     |
| Geometric mean | (ref)                                                           | 1.15x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250628-pythonperf1_win32-amd64-brandtbucher-jit_oz-3.15.0a0-6448067 |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------:|
| asyncio_websockets         | 363 ms                                                          | 160 ms: 2.26x faster                                                     |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 329 ms: 1.47x faster                                                     |
| async_tree_memoization     | 297 ms                                                          | 204 ms: 1.45x faster                                                     |
| async_tree_none            | 245 ms                                                          | 170 ms: 1.44x faster                                                     |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 336 ms: 1.36x faster                                                     |
| async_tree_io              | 526 ms                                                          | 391 ms: 1.34x faster                                                     |
| async_tree_memoization_tg  | 282 ms                                                          | 210 ms: 1.34x faster                                                     |
| async_tree_io_tg           | 494 ms                                                          | 381 ms: 1.30x faster                                                     |
| async_tree_none_tg         | 214 ms                                                          | 165 ms: 1.30x faster                                                     |
| coroutines                 | 16.2 ms                                                         | 14.4 ms: 1.12x faster                                                    |
| async_generators           | 270 ms                                                          | 246 ms: 1.10x faster                                                     |
| Geometric mean             | (ref)                                                           | 1.38x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250628-pythonperf1_win32-amd64-brandtbucher-jit_oz-3.15.0a0-6448067 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------:|
| nbody          | 80.0 ms                                                         | 52.1 ms: 1.53x faster                                                    |
| pidigits       | 201 ms                                                          | 147 ms: 1.37x faster                                                     |
| float          | 54.6 ms                                                         | 43.4 ms: 1.26x faster                                                    |
| Geometric mean | (ref)                                                           | 1.38x faster                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250628-pythonperf1_win32-amd64-brandtbucher-jit_oz-3.15.0a0-6448067 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 101 ms                                                          | 78.6 ms: 1.29x faster                                                    |
| regex_effbot   | 1.80 ms                                                         | 1.56 ms: 1.16x faster                                                    |
| regex_v8       | 16.8 ms                                                         | 14.6 ms: 1.15x faster                                                    |
| regex_dna      | 114 ms                                                          | 121 ms: 1.06x slower                                                     |
| Geometric mean | (ref)                                                           | 1.13x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250628-pythonperf1_win32-amd64-brandtbucher-jit_oz-3.15.0a0-6448067 |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------:|
| json_loads           | 21.6 us                                                         | 14.3 us: 1.51x faster                                                    |
| unpickle_pure_python | 160 us                                                          | 111 us: 1.44x faster                                                     |
| tomli_loads          | 1.71 sec                                                        | 1.23 sec: 1.40x faster                                                   |
| xml_etree_process    | 44.2 ms                                                         | 35.6 ms: 1.24x faster                                                    |
| xml_etree_generate   | 61.4 ms                                                         | 49.9 ms: 1.23x faster                                                    |
| xml_etree_parse      | 107 ms                                                          | 88.0 ms: 1.22x faster                                                    |
| json_dumps           | 7.30 ms                                                         | 6.16 ms: 1.19x faster                                                    |
| pickle_pure_python   | 231 us                                                          | 206 us: 1.12x faster                                                     |
| xml_etree_iterparse  | 62.6 ms                                                         | 61.6 ms: 1.02x faster                                                    |
| Geometric mean       | (ref)                                                           | 1.25x faster                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250628-pythonperf1_win32-amd64-brandtbucher-jit_oz-3.15.0a0-6448067 |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 28.3 ms                                                         | 26.1 ms: 1.08x faster                                                    |
| python_startup_no_site | 19.7 ms                                                         | 19.1 ms: 1.03x faster                                                    |
| Geometric mean         | (ref)                                                           | 1.05x faster                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250628-pythonperf1_win32-amd64-brandtbucher-jit_oz-3.15.0a0-6448067 |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_xml      | 50.1 ms                                                         | 34.9 ms: 1.44x faster                                                    |
| genshi_text     | 21.5 ms                                                         | 15.6 ms: 1.37x faster                                                    |
| mako            | 7.09 ms                                                         | 5.41 ms: 1.31x faster                                                    |
| django_template | 29.8 ms                                                         | 24.0 ms: 1.24x faster                                                    |
| Geometric mean  | (ref)                                                           | 1.34x faster                                                             |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250628-pythonperf1_win32-amd64-brandtbucher-jit_oz-3.15.0a0-6448067 |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------:|
| thrift                     | 9.98 ms                                                         | 508 us: 19.66x faster                                                    |
| coverage                   | 324 ms                                                          | 50.3 ms: 6.44x faster                                                    |
| pathlib                    | 82.9 ms                                                         | 29.1 ms: 2.85x faster                                                    |
| asyncio_websockets         | 363 ms                                                          | 160 ms: 2.26x faster                                                     |
| mdp                        | 1.62 sec                                                        | 803 ms: 2.02x faster                                                     |
| deepcopy                   | 314 us                                                          | 169 us: 1.86x faster                                                     |
| telco                      | 6.96 ms                                                         | 4.31 ms: 1.62x faster                                                    |
| deepcopy_reduce            | 2.92 us                                                         | 1.84 us: 1.59x faster                                                    |
| nbody                      | 80.0 ms                                                         | 52.1 ms: 1.53x faster                                                    |
| json_loads                 | 21.6 us                                                         | 14.3 us: 1.51x faster                                                    |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 329 ms: 1.47x faster                                                     |
| async_tree_memoization     | 297 ms                                                          | 204 ms: 1.45x faster                                                     |
| async_tree_none            | 245 ms                                                          | 170 ms: 1.44x faster                                                     |
| unpickle_pure_python       | 160 us                                                          | 111 us: 1.44x faster                                                     |
| genshi_xml                 | 50.1 ms                                                         | 34.9 ms: 1.44x faster                                                    |
| deepcopy_memo              | 25.4 us                                                         | 17.8 us: 1.43x faster                                                    |
| go                         | 109 ms                                                          | 77.5 ms: 1.40x faster                                                    |
| tomli_loads                | 1.71 sec                                                        | 1.23 sec: 1.40x faster                                                   |
| pprint_safe_repr           | 648 ms                                                          | 464 ms: 1.40x faster                                                     |
| pprint_pformat             | 1.33 sec                                                        | 956 ms: 1.39x faster                                                     |
| genshi_text                | 21.5 ms                                                         | 15.6 ms: 1.37x faster                                                    |
| pidigits                   | 201 ms                                                          | 147 ms: 1.37x faster                                                     |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 336 ms: 1.36x faster                                                     |
| async_tree_io              | 526 ms                                                          | 391 ms: 1.34x faster                                                     |
| async_tree_memoization_tg  | 282 ms                                                          | 210 ms: 1.34x faster                                                     |
| json                       | 4.27 ms                                                         | 3.19 ms: 1.34x faster                                                    |
| logging_format             | 8.72 us                                                         | 6.62 us: 1.32x faster                                                    |
| mako                       | 7.09 ms                                                         | 5.41 ms: 1.31x faster                                                    |
| typing_runtime_protocols   | 138 us                                                          | 105 us: 1.31x faster                                                     |
| logging_simple             | 7.99 us                                                         | 6.15 us: 1.30x faster                                                    |
| async_tree_io_tg           | 494 ms                                                          | 381 ms: 1.30x faster                                                     |
| async_tree_none_tg         | 214 ms                                                          | 165 ms: 1.30x faster                                                     |
| bpe_tokeniser              | 3.46 sec                                                        | 2.68 sec: 1.29x faster                                                   |
| scimark_fft                | 205 ms                                                          | 159 ms: 1.29x faster                                                     |
| regex_compile              | 101 ms                                                          | 78.6 ms: 1.29x faster                                                    |
| sympy_expand               | 373 ms                                                          | 295 ms: 1.27x faster                                                     |
| sqlite_synth               | 1.95 us                                                         | 1.55 us: 1.26x faster                                                    |
| float                      | 54.6 ms                                                         | 43.4 ms: 1.26x faster                                                    |
| pyflate                    | 320 ms                                                          | 257 ms: 1.25x faster                                                     |
| sympy_str                  | 212 ms                                                          | 170 ms: 1.25x faster                                                     |
| pycparser                  | 872 ms                                                          | 702 ms: 1.24x faster                                                     |
| xml_etree_process          | 44.2 ms                                                         | 35.6 ms: 1.24x faster                                                    |
| django_template            | 29.8 ms                                                         | 24.0 ms: 1.24x faster                                                    |
| html5lib                   | 47.5 ms                                                         | 38.4 ms: 1.24x faster                                                    |
| chaos                      | 50.2 ms                                                         | 40.7 ms: 1.23x faster                                                    |
| xml_etree_generate         | 61.4 ms                                                         | 49.9 ms: 1.23x faster                                                    |
| scimark_sparse_mat_mult    | 2.84 ms                                                         | 2.31 ms: 1.23x faster                                                    |
| xml_etree_parse            | 107 ms                                                          | 88.0 ms: 1.22x faster                                                    |
| sympy_sum                  | 106 ms                                                          | 86.6 ms: 1.22x faster                                                    |
| scimark_monte_carlo        | 47.7 ms                                                         | 39.2 ms: 1.21x faster                                                    |
| crypto_pyaes               | 56.9 ms                                                         | 46.9 ms: 1.21x faster                                                    |
| richards                   | 32.7 ms                                                         | 27.0 ms: 1.21x faster                                                    |
| fannkuch                   | 299 ms                                                          | 247 ms: 1.21x faster                                                     |
| dulwich_log                | 48.8 ms                                                         | 40.3 ms: 1.21x faster                                                    |
| richards_super             | 36.7 ms                                                         | 30.4 ms: 1.21x faster                                                    |
| json_dumps                 | 7.30 ms                                                         | 6.16 ms: 1.19x faster                                                    |
| sympy_integrate            | 15.0 ms                                                         | 12.7 ms: 1.18x faster                                                    |
| nqueens                    | 72.1 ms                                                         | 61.8 ms: 1.17x faster                                                    |
| regex_effbot               | 1.80 ms                                                         | 1.56 ms: 1.16x faster                                                    |
| 2to3                       | 250 ms                                                          | 218 ms: 1.15x faster                                                     |
| regex_v8                   | 16.8 ms                                                         | 14.6 ms: 1.15x faster                                                    |
| pylint                     | 227 ms                                                          | 198 ms: 1.14x faster                                                     |
| comprehensions             | 12.5 us                                                         | 11.0 us: 1.13x faster                                                    |
| scimark_sor                | 85.9 ms                                                         | 75.8 ms: 1.13x faster                                                    |
| raytrace                   | 201 ms                                                          | 178 ms: 1.13x faster                                                     |
| pickle_pure_python         | 231 us                                                          | 206 us: 1.12x faster                                                     |
| coroutines                 | 16.2 ms                                                         | 14.4 ms: 1.12x faster                                                    |
| sphinx                     | 719 ms                                                          | 641 ms: 1.12x faster                                                     |
| generators                 | 21.8 ms                                                         | 19.4 ms: 1.12x faster                                                    |
| logging_silent             | 60.3 ns                                                         | 54.8 ns: 1.10x faster                                                    |
| async_generators           | 270 ms                                                          | 246 ms: 1.10x faster                                                     |
| spectral_norm              | 69.4 ms                                                         | 63.4 ms: 1.09x faster                                                    |
| python_startup             | 28.3 ms                                                         | 26.1 ms: 1.08x faster                                                    |
| docutils                   | 1.78 sec                                                        | 1.64 sec: 1.08x faster                                                   |
| hexiom                     | 4.44 ms                                                         | 4.17 ms: 1.06x faster                                                    |
| deltablue                  | 2.33 ms                                                         | 2.21 ms: 1.06x faster                                                    |
| meteor_contest             | 74.6 ms                                                         | 71.5 ms: 1.04x faster                                                    |
| python_startup_no_site     | 19.7 ms                                                         | 19.1 ms: 1.03x faster                                                    |
| xml_etree_iterparse        | 62.6 ms                                                         | 61.6 ms: 1.02x faster                                                    |
| scimark_lu                 | 60.2 ms                                                         | 59.6 ms: 1.01x faster                                                    |
| many_optionals             | 436 us                                                          | 445 us: 1.02x slower                                                     |
| regex_dna                  | 114 ms                                                          | 121 ms: 1.06x slower                                                     |
| subparsers                 | 14.8 ms                                                         | 16.9 ms: 1.14x slower                                                    |
| k_core                     | 1.38 sec                                                        | 1.62 sec: 1.18x slower                                                   |
| gc_traversal               | 1.75 ms                                                         | 2.10 ms: 1.20x slower                                                    |
| connected_components       | 267 ms                                                          | 322 ms: 1.21x slower                                                     |
| create_gc_cycles           | 1.06 ms                                                         | 1.30 ms: 1.23x slower                                                    |
| shortest_path              | 290 ms                                                          | 357 ms: 1.23x slower                                                     |
| Geometric mean             | (ref)                                                           | 1.30x faster                                                             |
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250628-3.15.0a0-6448067-JIT/bm-20250628-pythonperf1_win32-amd64-brandtbucher-jit_oz-3.15.0a0-6448067.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.300x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.21x
- 95% likely to have a speedup of 1.21x
- 99% likely to have a speedup of 1.19x

# Memory
- memory change: unknown