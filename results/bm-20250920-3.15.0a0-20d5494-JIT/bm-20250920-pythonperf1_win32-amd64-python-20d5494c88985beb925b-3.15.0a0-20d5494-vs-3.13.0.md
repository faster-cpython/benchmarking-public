# Results vs. 3.13.0

- fork: python
- ref: 20d5494c88985beb925b
- machine: windows-amd64
- commit hash: 20d5494
- commit date: 2025-09-20
- overall geometric mean: 1.301x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.19x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250920-pythonperf1_win32-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 250 ms                                                          | 222 ms: 1.13x faster                                                             |
| docutils       | 1.78 sec                                                        | 1.66 sec: 1.07x faster                                                           |
| html5lib       | 47.5 ms                                                         | 37.7 ms: 1.26x faster                                                            |
| sphinx         | 719 ms                                                          | 639 ms: 1.12x faster                                                             |
| Geometric mean | (ref)                                                           | 1.14x faster                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250920-pythonperf1_win32-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494 |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| asyncio_websockets         | 363 ms                                                          | 161 ms: 2.25x faster                                                             |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 331 ms: 1.46x faster                                                             |
| async_tree_memoization     | 297 ms                                                          | 206 ms: 1.44x faster                                                             |
| async_tree_none            | 245 ms                                                          | 173 ms: 1.42x faster                                                             |
| async_tree_io              | 526 ms                                                          | 386 ms: 1.36x faster                                                             |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 339 ms: 1.35x faster                                                             |
| async_tree_memoization_tg  | 282 ms                                                          | 210 ms: 1.34x faster                                                             |
| async_tree_none_tg         | 214 ms                                                          | 165 ms: 1.30x faster                                                             |
| async_tree_io_tg           | 494 ms                                                          | 385 ms: 1.28x faster                                                             |
| coroutines                 | 16.2 ms                                                         | 14.4 ms: 1.12x faster                                                            |
| async_generators           | 270 ms                                                          | 246 ms: 1.10x faster                                                             |
| Geometric mean             | (ref)                                                           | 1.38x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250920-pythonperf1_win32-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| nbody          | 80.0 ms                                                         | 55.0 ms: 1.46x faster                                                            |
| float          | 54.6 ms                                                         | 39.7 ms: 1.38x faster                                                            |
| pidigits       | 201 ms                                                          | 148 ms: 1.36x faster                                                             |
| Geometric mean | (ref)                                                           | 1.40x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250920-pythonperf1_win32-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 101 ms                                                          | 77.8 ms: 1.30x faster                                                            |
| regex_v8       | 16.8 ms                                                         | 14.2 ms: 1.18x faster                                                            |
| regex_effbot   | 1.80 ms                                                         | 1.54 ms: 1.17x faster                                                            |
| regex_dna      | 114 ms                                                          | 121 ms: 1.07x slower                                                             |
| Geometric mean | (ref)                                                           | 1.14x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250920-pythonperf1_win32-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494 |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| tomli_loads          | 1.71 sec                                                        | 1.10 sec: 1.56x faster                                                           |
| json_loads           | 21.6 us                                                         | 14.0 us: 1.54x faster                                                            |
| unpickle_pure_python | 160 us                                                          | 107 us: 1.50x faster                                                             |
| json_dumps           | 7.30 ms                                                         | 5.38 ms: 1.36x faster                                                            |
| xml_etree_process    | 44.2 ms                                                         | 35.2 ms: 1.26x faster                                                            |
| xml_etree_parse      | 107 ms                                                          | 86.2 ms: 1.25x faster                                                            |
| xml_etree_generate   | 61.4 ms                                                         | 49.8 ms: 1.23x faster                                                            |
| pickle_pure_python   | 231 us                                                          | 199 us: 1.16x faster                                                             |
| xml_etree_iterparse  | 62.6 ms                                                         | 61.7 ms: 1.01x faster                                                            |
| Geometric mean       | (ref)                                                           | 1.31x faster                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250920-pythonperf1_win32-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494 |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup         | 28.3 ms                                                         | 25.5 ms: 1.11x faster                                                            |
| python_startup_no_site | 19.7 ms                                                         | 19.3 ms: 1.02x faster                                                            |
| Geometric mean         | (ref)                                                           | 1.06x faster                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250920-pythonperf1_win32-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494 |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| genshi_xml      | 50.1 ms                                                         | 35.1 ms: 1.43x faster                                                            |
| genshi_text     | 21.5 ms                                                         | 15.5 ms: 1.38x faster                                                            |
| mako            | 7.09 ms                                                         | 5.26 ms: 1.35x faster                                                            |
| django_template | 29.8 ms                                                         | 24.1 ms: 1.23x faster                                                            |
| Geometric mean  | (ref)                                                           | 1.35x faster                                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250920-pythonperf1_win32-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494 |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| thrift                     | 9.98 ms                                                         | 517 us: 19.28x faster                                                            |
| coverage                   | 324 ms                                                          | 49.1 ms: 6.59x faster                                                            |
| pathlib                    | 82.9 ms                                                         | 29.6 ms: 2.80x faster                                                            |
| asyncio_websockets         | 363 ms                                                          | 161 ms: 2.25x faster                                                             |
| mdp                        | 1.62 sec                                                        | 820 ms: 1.98x faster                                                             |
| deepcopy                   | 314 us                                                          | 167 us: 1.88x faster                                                             |
| telco                      | 6.96 ms                                                         | 3.98 ms: 1.75x faster                                                            |
| deepcopy_reduce            | 2.92 us                                                         | 1.81 us: 1.61x faster                                                            |
| tomli_loads                | 1.71 sec                                                        | 1.10 sec: 1.56x faster                                                           |
| json_loads                 | 21.6 us                                                         | 14.0 us: 1.54x faster                                                            |
| pprint_pformat             | 1.33 sec                                                        | 873 ms: 1.52x faster                                                             |
| pprint_safe_repr           | 648 ms                                                          | 430 ms: 1.51x faster                                                             |
| unpickle_pure_python       | 160 us                                                          | 107 us: 1.50x faster                                                             |
| deepcopy_memo              | 25.4 us                                                         | 16.9 us: 1.50x faster                                                            |
| json                       | 4.27 ms                                                         | 2.91 ms: 1.47x faster                                                            |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 331 ms: 1.46x faster                                                             |
| nbody                      | 80.0 ms                                                         | 55.0 ms: 1.46x faster                                                            |
| async_tree_memoization     | 297 ms                                                          | 206 ms: 1.44x faster                                                             |
| genshi_xml                 | 50.1 ms                                                         | 35.1 ms: 1.43x faster                                                            |
| go                         | 109 ms                                                          | 76.4 ms: 1.42x faster                                                            |
| async_tree_none            | 245 ms                                                          | 173 ms: 1.42x faster                                                             |
| fannkuch                   | 299 ms                                                          | 212 ms: 1.41x faster                                                             |
| genshi_text                | 21.5 ms                                                         | 15.5 ms: 1.38x faster                                                            |
| float                      | 54.6 ms                                                         | 39.7 ms: 1.38x faster                                                            |
| scimark_fft                | 205 ms                                                          | 149 ms: 1.38x faster                                                             |
| bpe_tokeniser              | 3.46 sec                                                        | 2.52 sec: 1.37x faster                                                           |
| async_tree_io              | 526 ms                                                          | 386 ms: 1.36x faster                                                             |
| pidigits                   | 201 ms                                                          | 148 ms: 1.36x faster                                                             |
| json_dumps                 | 7.30 ms                                                         | 5.38 ms: 1.36x faster                                                            |
| typing_runtime_protocols   | 138 us                                                          | 102 us: 1.35x faster                                                             |
| logging_format             | 8.72 us                                                         | 6.47 us: 1.35x faster                                                            |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 339 ms: 1.35x faster                                                             |
| mako                       | 7.09 ms                                                         | 5.26 ms: 1.35x faster                                                            |
| async_tree_memoization_tg  | 282 ms                                                          | 210 ms: 1.34x faster                                                             |
| logging_simple             | 7.99 us                                                         | 6.03 us: 1.32x faster                                                            |
| async_tree_none_tg         | 214 ms                                                          | 165 ms: 1.30x faster                                                             |
| regex_compile              | 101 ms                                                          | 77.8 ms: 1.30x faster                                                            |
| async_tree_io_tg           | 494 ms                                                          | 385 ms: 1.28x faster                                                             |
| pyflate                    | 320 ms                                                          | 253 ms: 1.26x faster                                                             |
| sqlite_synth               | 1.95 us                                                         | 1.55 us: 1.26x faster                                                            |
| html5lib                   | 47.5 ms                                                         | 37.7 ms: 1.26x faster                                                            |
| sympy_expand               | 373 ms                                                          | 296 ms: 1.26x faster                                                             |
| xml_etree_process          | 44.2 ms                                                         | 35.2 ms: 1.26x faster                                                            |
| xml_etree_parse            | 107 ms                                                          | 86.2 ms: 1.25x faster                                                            |
| pycparser                  | 872 ms                                                          | 701 ms: 1.24x faster                                                             |
| sympy_str                  | 212 ms                                                          | 171 ms: 1.24x faster                                                             |
| crypto_pyaes               | 56.9 ms                                                         | 46.0 ms: 1.24x faster                                                            |
| django_template            | 29.8 ms                                                         | 24.1 ms: 1.23x faster                                                            |
| xml_etree_generate         | 61.4 ms                                                         | 49.8 ms: 1.23x faster                                                            |
| scimark_sparse_mat_mult    | 2.84 ms                                                         | 2.32 ms: 1.22x faster                                                            |
| chaos                      | 50.2 ms                                                         | 41.1 ms: 1.22x faster                                                            |
| sympy_sum                  | 106 ms                                                          | 87.4 ms: 1.21x faster                                                            |
| dulwich_log                | 48.8 ms                                                         | 40.8 ms: 1.20x faster                                                            |
| richards                   | 32.7 ms                                                         | 27.5 ms: 1.19x faster                                                            |
| richards_super             | 36.7 ms                                                         | 31.0 ms: 1.18x faster                                                            |
| regex_v8                   | 16.8 ms                                                         | 14.2 ms: 1.18x faster                                                            |
| scimark_monte_carlo        | 47.7 ms                                                         | 40.5 ms: 1.18x faster                                                            |
| sympy_integrate            | 15.0 ms                                                         | 12.7 ms: 1.18x faster                                                            |
| bench_thread_pool          | 1.00 ms                                                         | 851 us: 1.18x faster                                                             |
| nqueens                    | 72.1 ms                                                         | 61.3 ms: 1.18x faster                                                            |
| regex_effbot               | 1.80 ms                                                         | 1.54 ms: 1.17x faster                                                            |
| comprehensions             | 12.5 us                                                         | 10.7 us: 1.16x faster                                                            |
| pickle_pure_python         | 231 us                                                          | 199 us: 1.16x faster                                                             |
| pylint                     | 227 ms                                                          | 199 ms: 1.14x faster                                                             |
| raytrace                   | 201 ms                                                          | 177 ms: 1.14x faster                                                             |
| 2to3                       | 250 ms                                                          | 222 ms: 1.13x faster                                                             |
| sphinx                     | 719 ms                                                          | 639 ms: 1.12x faster                                                             |
| coroutines                 | 16.2 ms                                                         | 14.4 ms: 1.12x faster                                                            |
| generators                 | 21.8 ms                                                         | 19.5 ms: 1.12x faster                                                            |
| logging_silent             | 60.3 ns                                                         | 54.2 ns: 1.11x faster                                                            |
| python_startup             | 28.3 ms                                                         | 25.5 ms: 1.11x faster                                                            |
| async_generators           | 270 ms                                                          | 246 ms: 1.10x faster                                                             |
| scimark_sor                | 85.9 ms                                                         | 78.5 ms: 1.09x faster                                                            |
| hexiom                     | 4.44 ms                                                         | 4.12 ms: 1.08x faster                                                            |
| docutils                   | 1.78 sec                                                        | 1.66 sec: 1.07x faster                                                           |
| deltablue                  | 2.33 ms                                                         | 2.22 ms: 1.05x faster                                                            |
| scimark_lu                 | 60.2 ms                                                         | 57.8 ms: 1.04x faster                                                            |
| spectral_norm              | 69.4 ms                                                         | 67.2 ms: 1.03x faster                                                            |
| meteor_contest             | 74.6 ms                                                         | 72.7 ms: 1.03x faster                                                            |
| python_startup_no_site     | 19.7 ms                                                         | 19.3 ms: 1.02x faster                                                            |
| xml_etree_iterparse        | 62.6 ms                                                         | 61.7 ms: 1.01x faster                                                            |
| bench_mp_pool              | 90.6 ms                                                         | 91.1 ms: 1.01x slower                                                            |
| regex_dna                  | 114 ms                                                          | 121 ms: 1.07x slower                                                             |
| k_core                     | 1.38 sec                                                        | 1.61 sec: 1.17x slower                                                           |
| connected_components       | 267 ms                                                          | 323 ms: 1.21x slower                                                             |
| create_gc_cycles           | 1.06 ms                                                         | 1.29 ms: 1.22x slower                                                            |
| gc_traversal               | 1.75 ms                                                         | 2.14 ms: 1.22x slower                                                            |
| shortest_path              | 290 ms                                                          | 357 ms: 1.23x slower                                                             |
| many_optionals             | 436 us                                                          | 587 us: 1.34x slower                                                             |
| subparsers                 | 14.8 ms                                                         | 31.4 ms: 2.13x slower                                                            |
| Geometric mean             | (ref)                                                           | 1.30x faster                                                                     |
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250920-3.15.0a0-20d5494-JIT/bm-20250920-pythonperf1_win32-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.301x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.22x
- 95% likely to have a speedup of 1.21x
- 99% likely to have a speedup of 1.19x

# Memory
- memory change: unknown