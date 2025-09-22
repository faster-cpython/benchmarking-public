# Results vs. 3.13.0

- fork: python
- ref: 20d5494c88985beb925b
- machine: windows-amd64
- commit hash: 20d5494
- commit date: 2025-09-20
- overall geometric mean: 1.252x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.16x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250920-pythonperf1_win32-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 250 ms                                                          | 215 ms: 1.16x faster                                                             |
| docutils       | 1.78 sec                                                        | 1.59 sec: 1.12x faster                                                           |
| html5lib       | 47.5 ms                                                         | 37.4 ms: 1.27x faster                                                            |
| sphinx         | 719 ms                                                          | 625 ms: 1.15x faster                                                             |
| Geometric mean | (ref)                                                           | 1.17x faster                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250920-pythonperf1_win32-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494 |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| asyncio_websockets         | 363 ms                                                          | 160 ms: 2.27x faster                                                             |
| async_tree_memoization     | 297 ms                                                          | 200 ms: 1.48x faster                                                             |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 328 ms: 1.48x faster                                                             |
| async_tree_none            | 245 ms                                                          | 169 ms: 1.45x faster                                                             |
| async_tree_io              | 526 ms                                                          | 381 ms: 1.38x faster                                                             |
| async_tree_memoization_tg  | 282 ms                                                          | 205 ms: 1.38x faster                                                             |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 332 ms: 1.37x faster                                                             |
| async_tree_io_tg           | 494 ms                                                          | 379 ms: 1.31x faster                                                             |
| async_tree_none_tg         | 214 ms                                                          | 165 ms: 1.30x faster                                                             |
| async_generators           | 270 ms                                                          | 227 ms: 1.19x faster                                                             |
| coroutines                 | 16.2 ms                                                         | 14.5 ms: 1.12x faster                                                            |
| Geometric mean             | (ref)                                                           | 1.41x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250920-pythonperf1_win32-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pidigits       | 201 ms                                                          | 148 ms: 1.35x faster                                                             |
| float          | 54.6 ms                                                         | 42.0 ms: 1.30x faster                                                            |
| nbody          | 80.0 ms                                                         | 63.9 ms: 1.25x faster                                                            |
| Geometric mean | (ref)                                                           | 1.30x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250920-pythonperf1_win32-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 101 ms                                                          | 78.0 ms: 1.29x faster                                                            |
| regex_v8       | 16.8 ms                                                         | 13.9 ms: 1.21x faster                                                            |
| regex_effbot   | 1.80 ms                                                         | 1.53 ms: 1.18x faster                                                            |
| regex_dna      | 114 ms                                                          | 120 ms: 1.05x slower                                                             |
| Geometric mean | (ref)                                                           | 1.15x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250920-pythonperf1_win32-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494 |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| json_loads           | 21.6 us                                                         | 14.3 us: 1.51x faster                                                            |
| json_dumps           | 7.30 ms                                                         | 5.31 ms: 1.37x faster                                                            |
| tomli_loads          | 1.71 sec                                                        | 1.33 sec: 1.28x faster                                                           |
| xml_etree_parse      | 107 ms                                                          | 85.3 ms: 1.26x faster                                                            |
| unpickle_pure_python | 160 us                                                          | 132 us: 1.21x faster                                                             |
| xml_etree_process    | 44.2 ms                                                         | 38.3 ms: 1.15x faster                                                            |
| xml_etree_generate   | 61.4 ms                                                         | 55.0 ms: 1.12x faster                                                            |
| pickle_pure_python   | 231 us                                                          | 213 us: 1.09x faster                                                             |
| Geometric mean       | (ref)                                                           | 1.21x faster                                                                     |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250920-pythonperf1_win32-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494 |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup         | 28.3 ms                                                         | 25.3 ms: 1.12x faster                                                            |
| python_startup_no_site | 19.7 ms                                                         | 19.1 ms: 1.03x faster                                                            |
| Geometric mean         | (ref)                                                           | 1.07x faster                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250920-pythonperf1_win32-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494 |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| genshi_xml      | 50.1 ms                                                         | 34.3 ms: 1.46x faster                                                            |
| genshi_text     | 21.5 ms                                                         | 15.4 ms: 1.39x faster                                                            |
| django_template | 29.8 ms                                                         | 24.1 ms: 1.24x faster                                                            |
| mako            | 7.09 ms                                                         | 6.66 ms: 1.06x faster                                                            |
| Geometric mean  | (ref)                                                           | 1.28x faster                                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250920-pythonperf1_win32-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494 |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| thrift                     | 9.98 ms                                                         | 511 us: 19.52x faster                                                            |
| coverage                   | 324 ms                                                          | 50.4 ms: 6.42x faster                                                            |
| pathlib                    | 82.9 ms                                                         | 29.3 ms: 2.83x faster                                                            |
| asyncio_websockets         | 363 ms                                                          | 160 ms: 2.27x faster                                                             |
| mdp                        | 1.62 sec                                                        | 793 ms: 2.05x faster                                                             |
| deepcopy                   | 314 us                                                          | 164 us: 1.91x faster                                                             |
| deepcopy_reduce            | 2.92 us                                                         | 1.76 us: 1.66x faster                                                            |
| telco                      | 6.96 ms                                                         | 4.29 ms: 1.62x faster                                                            |
| deepcopy_memo              | 25.4 us                                                         | 16.7 us: 1.52x faster                                                            |
| json_loads                 | 21.6 us                                                         | 14.3 us: 1.51x faster                                                            |
| async_tree_memoization     | 297 ms                                                          | 200 ms: 1.48x faster                                                             |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 328 ms: 1.48x faster                                                             |
| go                         | 109 ms                                                          | 74.2 ms: 1.47x faster                                                            |
| json                       | 4.27 ms                                                         | 2.92 ms: 1.46x faster                                                            |
| genshi_xml                 | 50.1 ms                                                         | 34.3 ms: 1.46x faster                                                            |
| async_tree_none            | 245 ms                                                          | 169 ms: 1.45x faster                                                             |
| genshi_text                | 21.5 ms                                                         | 15.4 ms: 1.39x faster                                                            |
| async_tree_io              | 526 ms                                                          | 381 ms: 1.38x faster                                                             |
| async_tree_memoization_tg  | 282 ms                                                          | 205 ms: 1.38x faster                                                             |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 332 ms: 1.37x faster                                                             |
| json_dumps                 | 7.30 ms                                                         | 5.31 ms: 1.37x faster                                                            |
| logging_simple             | 7.99 us                                                         | 5.86 us: 1.36x faster                                                            |
| typing_runtime_protocols   | 138 us                                                          | 101 us: 1.36x faster                                                             |
| logging_format             | 8.72 us                                                         | 6.40 us: 1.36x faster                                                            |
| pidigits                   | 201 ms                                                          | 148 ms: 1.35x faster                                                             |
| pprint_pformat             | 1.33 sec                                                        | 995 ms: 1.34x faster                                                             |
| pprint_safe_repr           | 648 ms                                                          | 490 ms: 1.32x faster                                                             |
| sympy_expand               | 373 ms                                                          | 283 ms: 1.32x faster                                                             |
| async_tree_io_tg           | 494 ms                                                          | 379 ms: 1.31x faster                                                             |
| float                      | 54.6 ms                                                         | 42.0 ms: 1.30x faster                                                            |
| async_tree_none_tg         | 214 ms                                                          | 165 ms: 1.30x faster                                                             |
| regex_compile              | 101 ms                                                          | 78.0 ms: 1.29x faster                                                            |
| tomli_loads                | 1.71 sec                                                        | 1.33 sec: 1.28x faster                                                           |
| html5lib                   | 47.5 ms                                                         | 37.4 ms: 1.27x faster                                                            |
| sympy_str                  | 212 ms                                                          | 167 ms: 1.27x faster                                                             |
| sqlite_synth               | 1.95 us                                                         | 1.55 us: 1.26x faster                                                            |
| xml_etree_parse            | 107 ms                                                          | 85.3 ms: 1.26x faster                                                            |
| chaos                      | 50.2 ms                                                         | 40.1 ms: 1.25x faster                                                            |
| richards                   | 32.7 ms                                                         | 26.1 ms: 1.25x faster                                                            |
| nbody                      | 80.0 ms                                                         | 63.9 ms: 1.25x faster                                                            |
| dulwich_log                | 48.8 ms                                                         | 38.9 ms: 1.25x faster                                                            |
| pycparser                  | 872 ms                                                          | 699 ms: 1.25x faster                                                             |
| sympy_sum                  | 106 ms                                                          | 85.0 ms: 1.24x faster                                                            |
| richards_super             | 36.7 ms                                                         | 29.6 ms: 1.24x faster                                                            |
| django_template            | 29.8 ms                                                         | 24.1 ms: 1.24x faster                                                            |
| sympy_integrate            | 15.0 ms                                                         | 12.2 ms: 1.23x faster                                                            |
| unpickle_pure_python       | 160 us                                                          | 132 us: 1.21x faster                                                             |
| crypto_pyaes               | 56.9 ms                                                         | 47.0 ms: 1.21x faster                                                            |
| regex_v8                   | 16.8 ms                                                         | 13.9 ms: 1.21x faster                                                            |
| async_generators           | 270 ms                                                          | 227 ms: 1.19x faster                                                             |
| regex_effbot               | 1.80 ms                                                         | 1.53 ms: 1.18x faster                                                            |
| nqueens                    | 72.1 ms                                                         | 61.3 ms: 1.18x faster                                                            |
| scimark_monte_carlo        | 47.7 ms                                                         | 40.6 ms: 1.17x faster                                                            |
| bpe_tokeniser              | 3.46 sec                                                        | 2.96 sec: 1.17x faster                                                           |
| 2to3                       | 250 ms                                                          | 215 ms: 1.16x faster                                                             |
| fannkuch                   | 299 ms                                                          | 257 ms: 1.16x faster                                                             |
| scimark_sor                | 85.9 ms                                                         | 74.2 ms: 1.16x faster                                                            |
| xml_etree_process          | 44.2 ms                                                         | 38.3 ms: 1.15x faster                                                            |
| pylint                     | 227 ms                                                          | 197 ms: 1.15x faster                                                             |
| sphinx                     | 719 ms                                                          | 625 ms: 1.15x faster                                                             |
| comprehensions             | 12.5 us                                                         | 10.9 us: 1.15x faster                                                            |
| raytrace                   | 201 ms                                                          | 176 ms: 1.15x faster                                                             |
| scimark_fft                | 205 ms                                                          | 179 ms: 1.14x faster                                                             |
| pyflate                    | 320 ms                                                          | 280 ms: 1.14x faster                                                             |
| generators                 | 21.8 ms                                                         | 19.2 ms: 1.14x faster                                                            |
| spectral_norm              | 69.4 ms                                                         | 61.9 ms: 1.12x faster                                                            |
| docutils                   | 1.78 sec                                                        | 1.59 sec: 1.12x faster                                                           |
| python_startup             | 28.3 ms                                                         | 25.3 ms: 1.12x faster                                                            |
| coroutines                 | 16.2 ms                                                         | 14.5 ms: 1.12x faster                                                            |
| xml_etree_generate         | 61.4 ms                                                         | 55.0 ms: 1.12x faster                                                            |
| scimark_sparse_mat_mult    | 2.84 ms                                                         | 2.55 ms: 1.11x faster                                                            |
| hexiom                     | 4.44 ms                                                         | 4.00 ms: 1.11x faster                                                            |
| logging_silent             | 60.3 ns                                                         | 55.4 ns: 1.09x faster                                                            |
| deltablue                  | 2.33 ms                                                         | 2.14 ms: 1.09x faster                                                            |
| pickle_pure_python         | 231 us                                                          | 213 us: 1.09x faster                                                             |
| mako                       | 7.09 ms                                                         | 6.66 ms: 1.06x faster                                                            |
| meteor_contest             | 74.6 ms                                                         | 71.5 ms: 1.04x faster                                                            |
| python_startup_no_site     | 19.7 ms                                                         | 19.1 ms: 1.03x faster                                                            |
| scimark_lu                 | 60.2 ms                                                         | 58.7 ms: 1.03x faster                                                            |
| regex_dna                  | 114 ms                                                          | 120 ms: 1.05x slower                                                             |
| create_gc_cycles           | 1.06 ms                                                         | 1.27 ms: 1.20x slower                                                            |
| gc_traversal               | 1.75 ms                                                         | 2.10 ms: 1.20x slower                                                            |
| k_core                     | 1.38 sec                                                        | 1.67 sec: 1.22x slower                                                           |
| connected_components       | 267 ms                                                          | 324 ms: 1.22x slower                                                             |
| shortest_path              | 290 ms                                                          | 355 ms: 1.22x slower                                                             |
| many_optionals             | 436 us                                                          | 561 us: 1.29x slower                                                             |
| subparsers                 | 14.8 ms                                                         | 30.3 ms: 2.05x slower                                                            |
| bench_thread_pool          | 1.00 ms                                                         | 8.12 ms: 8.11x slower                                                            |
| Geometric mean             | (ref)                                                           | 1.25x faster                                                                     |

Benchmark hidden because not significant (2): xml_etree_iterparse, bench_mp_pool
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250920-3.15.0a0-20d5494/bm-20250920-pythonperf1_win32-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.252x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.19x
- 95% likely to have a speedup of 1.17x
- 99% likely to have a speedup of 1.16x

# Memory
- memory change: unknown