# Results vs. 3.13.0

- fork: python
- ref: 800d37feca2e0ea33439
- machine: windows-amd64
- commit hash: 800d37f
- commit date: 2025-07-19
- overall geometric mean: 1.268x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.14x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250719-pythonperf1_win32-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 250 ms                                                          | 221 ms: 1.13x faster                                                             |
| docutils       | 1.78 sec                                                        | 1.62 sec: 1.10x faster                                                           |
| html5lib       | 47.5 ms                                                         | 39.4 ms: 1.21x faster                                                            |
| sphinx         | 719 ms                                                          | 639 ms: 1.12x faster                                                             |
| Geometric mean | (ref)                                                           | 1.14x faster                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250719-pythonperf1_win32-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| asyncio_websockets         | 363 ms                                                          | 168 ms: 2.16x faster                                                             |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 328 ms: 1.48x faster                                                             |
| async_tree_memoization     | 297 ms                                                          | 205 ms: 1.45x faster                                                             |
| async_tree_none            | 245 ms                                                          | 170 ms: 1.44x faster                                                             |
| async_tree_memoization_tg  | 282 ms                                                          | 209 ms: 1.35x faster                                                             |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 339 ms: 1.35x faster                                                             |
| async_tree_io              | 526 ms                                                          | 393 ms: 1.34x faster                                                             |
| async_tree_none_tg         | 214 ms                                                          | 170 ms: 1.26x faster                                                             |
| async_tree_io_tg           | 494 ms                                                          | 392 ms: 1.26x faster                                                             |
| async_generators           | 270 ms                                                          | 233 ms: 1.16x faster                                                             |
| coroutines                 | 16.2 ms                                                         | 14.4 ms: 1.13x faster                                                            |
| Geometric mean             | (ref)                                                           | 1.38x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250719-pythonperf1_win32-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pidigits       | 201 ms                                                          | 146 ms: 1.37x faster                                                             |
| float          | 54.6 ms                                                         | 43.4 ms: 1.26x faster                                                            |
| nbody          | 80.0 ms                                                         | 64.2 ms: 1.25x faster                                                            |
| Geometric mean | (ref)                                                           | 1.29x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250719-pythonperf1_win32-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 101 ms                                                          | 79.9 ms: 1.26x faster                                                            |
| regex_v8       | 16.8 ms                                                         | 14.3 ms: 1.18x faster                                                            |
| regex_effbot   | 1.80 ms                                                         | 1.57 ms: 1.15x faster                                                            |
| regex_dna      | 114 ms                                                          | 120 ms: 1.06x slower                                                             |
| Geometric mean | (ref)                                                           | 1.13x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250719-pythonperf1_win32-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| json_loads           | 21.6 us                                                         | 14.1 us: 1.54x faster                                                            |
| xml_etree_parse      | 107 ms                                                          | 86.8 ms: 1.24x faster                                                            |
| tomli_loads          | 1.71 sec                                                        | 1.41 sec: 1.22x faster                                                           |
| unpickle_pure_python | 160 us                                                          | 135 us: 1.19x faster                                                             |
| json_dumps           | 7.30 ms                                                         | 6.31 ms: 1.16x faster                                                            |
| xml_etree_process    | 44.2 ms                                                         | 38.5 ms: 1.15x faster                                                            |
| xml_etree_generate   | 61.4 ms                                                         | 55.9 ms: 1.10x faster                                                            |
| pickle_pure_python   | 231 us                                                          | 213 us: 1.09x faster                                                             |
| xml_etree_iterparse  | 62.6 ms                                                         | 63.1 ms: 1.01x slower                                                            |
| Geometric mean       | (ref)                                                           | 1.18x faster                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250719-pythonperf1_win32-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup         | 28.3 ms                                                         | 25.8 ms: 1.10x faster                                                            |
| python_startup_no_site | 19.7 ms                                                         | 19.3 ms: 1.02x faster                                                            |
| Geometric mean         | (ref)                                                           | 1.06x faster                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250719-pythonperf1_win32-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| genshi_xml      | 50.1 ms                                                         | 34.0 ms: 1.48x faster                                                            |
| genshi_text     | 21.5 ms                                                         | 15.1 ms: 1.42x faster                                                            |
| django_template | 29.8 ms                                                         | 24.6 ms: 1.21x faster                                                            |
| mako            | 7.09 ms                                                         | 6.53 ms: 1.09x faster                                                            |
| Geometric mean  | (ref)                                                           | 1.29x faster                                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250719-pythonperf1_win32-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| thrift                     | 9.98 ms                                                         | 505 us: 19.76x faster                                                            |
| coverage                   | 324 ms                                                          | 51.8 ms: 6.25x faster                                                            |
| pathlib                    | 82.9 ms                                                         | 30.5 ms: 2.72x faster                                                            |
| asyncio_websockets         | 363 ms                                                          | 168 ms: 2.16x faster                                                             |
| mdp                        | 1.62 sec                                                        | 804 ms: 2.02x faster                                                             |
| deepcopy                   | 314 us                                                          | 171 us: 1.83x faster                                                             |
| deepcopy_reduce            | 2.92 us                                                         | 1.85 us: 1.58x faster                                                            |
| json_loads                 | 21.6 us                                                         | 14.1 us: 1.54x faster                                                            |
| telco                      | 6.96 ms                                                         | 4.60 ms: 1.51x faster                                                            |
| json                       | 4.27 ms                                                         | 2.88 ms: 1.49x faster                                                            |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 328 ms: 1.48x faster                                                             |
| genshi_xml                 | 50.1 ms                                                         | 34.0 ms: 1.48x faster                                                            |
| async_tree_memoization     | 297 ms                                                          | 205 ms: 1.45x faster                                                             |
| async_tree_none            | 245 ms                                                          | 170 ms: 1.44x faster                                                             |
| genshi_text                | 21.5 ms                                                         | 15.1 ms: 1.42x faster                                                            |
| go                         | 109 ms                                                          | 77.1 ms: 1.41x faster                                                            |
| deepcopy_memo              | 25.4 us                                                         | 18.3 us: 1.39x faster                                                            |
| pidigits                   | 201 ms                                                          | 146 ms: 1.37x faster                                                             |
| async_tree_memoization_tg  | 282 ms                                                          | 209 ms: 1.35x faster                                                             |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 339 ms: 1.35x faster                                                             |
| async_tree_io              | 526 ms                                                          | 393 ms: 1.34x faster                                                             |
| typing_runtime_protocols   | 138 us                                                          | 105 us: 1.31x faster                                                             |
| pprint_pformat             | 1.33 sec                                                        | 1.02 sec: 1.30x faster                                                           |
| logging_format             | 8.72 us                                                         | 6.75 us: 1.29x faster                                                            |
| sympy_expand               | 373 ms                                                          | 289 ms: 1.29x faster                                                             |
| pprint_safe_repr           | 648 ms                                                          | 508 ms: 1.28x faster                                                             |
| logging_simple             | 7.99 us                                                         | 6.29 us: 1.27x faster                                                            |
| regex_compile              | 101 ms                                                          | 79.9 ms: 1.26x faster                                                            |
| async_tree_none_tg         | 214 ms                                                          | 170 ms: 1.26x faster                                                             |
| async_tree_io_tg           | 494 ms                                                          | 392 ms: 1.26x faster                                                             |
| float                      | 54.6 ms                                                         | 43.4 ms: 1.26x faster                                                            |
| sympy_str                  | 212 ms                                                          | 169 ms: 1.25x faster                                                             |
| nbody                      | 80.0 ms                                                         | 64.2 ms: 1.25x faster                                                            |
| sqlite_synth               | 1.95 us                                                         | 1.58 us: 1.24x faster                                                            |
| xml_etree_parse            | 107 ms                                                          | 86.8 ms: 1.24x faster                                                            |
| chaos                      | 50.2 ms                                                         | 41.0 ms: 1.22x faster                                                            |
| pycparser                  | 872 ms                                                          | 714 ms: 1.22x faster                                                             |
| tomli_loads                | 1.71 sec                                                        | 1.41 sec: 1.22x faster                                                           |
| django_template            | 29.8 ms                                                         | 24.6 ms: 1.21x faster                                                            |
| sympy_integrate            | 15.0 ms                                                         | 12.4 ms: 1.21x faster                                                            |
| html5lib                   | 47.5 ms                                                         | 39.4 ms: 1.21x faster                                                            |
| dulwich_log                | 48.8 ms                                                         | 40.4 ms: 1.21x faster                                                            |
| sympy_sum                  | 106 ms                                                          | 87.8 ms: 1.20x faster                                                            |
| unpickle_pure_python       | 160 us                                                          | 135 us: 1.19x faster                                                             |
| bpe_tokeniser              | 3.46 sec                                                        | 2.92 sec: 1.18x faster                                                           |
| scimark_monte_carlo        | 47.7 ms                                                         | 40.4 ms: 1.18x faster                                                            |
| bench_thread_pool          | 1.00 ms                                                         | 849 us: 1.18x faster                                                             |
| regex_v8                   | 16.8 ms                                                         | 14.3 ms: 1.18x faster                                                            |
| crypto_pyaes               | 56.9 ms                                                         | 48.4 ms: 1.18x faster                                                            |
| richards                   | 32.7 ms                                                         | 27.8 ms: 1.17x faster                                                            |
| comprehensions             | 12.5 us                                                         | 10.7 us: 1.17x faster                                                            |
| nqueens                    | 72.1 ms                                                         | 62.2 ms: 1.16x faster                                                            |
| async_generators           | 270 ms                                                          | 233 ms: 1.16x faster                                                             |
| json_dumps                 | 7.30 ms                                                         | 6.31 ms: 1.16x faster                                                            |
| pylint                     | 227 ms                                                          | 196 ms: 1.16x faster                                                             |
| regex_effbot               | 1.80 ms                                                         | 1.57 ms: 1.15x faster                                                            |
| richards_super             | 36.7 ms                                                         | 31.9 ms: 1.15x faster                                                            |
| xml_etree_process          | 44.2 ms                                                         | 38.5 ms: 1.15x faster                                                            |
| scimark_sparse_mat_mult    | 2.84 ms                                                         | 2.50 ms: 1.14x faster                                                            |
| 2to3                       | 250 ms                                                          | 221 ms: 1.13x faster                                                             |
| coroutines                 | 16.2 ms                                                         | 14.4 ms: 1.13x faster                                                            |
| generators                 | 21.8 ms                                                         | 19.3 ms: 1.13x faster                                                            |
| sphinx                     | 719 ms                                                          | 639 ms: 1.12x faster                                                             |
| fannkuch                   | 299 ms                                                          | 269 ms: 1.11x faster                                                             |
| pyflate                    | 320 ms                                                          | 289 ms: 1.11x faster                                                             |
| xml_etree_generate         | 61.4 ms                                                         | 55.9 ms: 1.10x faster                                                            |
| python_startup             | 28.3 ms                                                         | 25.8 ms: 1.10x faster                                                            |
| docutils                   | 1.78 sec                                                        | 1.62 sec: 1.10x faster                                                           |
| raytrace                   | 201 ms                                                          | 184 ms: 1.09x faster                                                             |
| hexiom                     | 4.44 ms                                                         | 4.08 ms: 1.09x faster                                                            |
| pickle_pure_python         | 231 us                                                          | 213 us: 1.09x faster                                                             |
| mako                       | 7.09 ms                                                         | 6.53 ms: 1.09x faster                                                            |
| logging_silent             | 60.3 ns                                                         | 55.6 ns: 1.09x faster                                                            |
| scimark_sor                | 85.9 ms                                                         | 79.2 ms: 1.08x faster                                                            |
| scimark_fft                | 205 ms                                                          | 189 ms: 1.08x faster                                                             |
| spectral_norm              | 69.4 ms                                                         | 64.5 ms: 1.08x faster                                                            |
| deltablue                  | 2.33 ms                                                         | 2.21 ms: 1.05x faster                                                            |
| meteor_contest             | 74.6 ms                                                         | 72.6 ms: 1.03x faster                                                            |
| scimark_lu                 | 60.2 ms                                                         | 58.6 ms: 1.03x faster                                                            |
| python_startup_no_site     | 19.7 ms                                                         | 19.3 ms: 1.02x faster                                                            |
| xml_etree_iterparse        | 62.6 ms                                                         | 63.1 ms: 1.01x slower                                                            |
| bench_mp_pool              | 90.6 ms                                                         | 94.2 ms: 1.04x slower                                                            |
| regex_dna                  | 114 ms                                                          | 120 ms: 1.06x slower                                                             |
| subparsers                 | 14.8 ms                                                         | 17.2 ms: 1.16x slower                                                            |
| gc_traversal               | 1.75 ms                                                         | 2.11 ms: 1.21x slower                                                            |
| create_gc_cycles           | 1.06 ms                                                         | 1.30 ms: 1.23x slower                                                            |
| k_core                     | 1.38 sec                                                        | 1.70 sec: 1.24x slower                                                           |
| connected_components       | 267 ms                                                          | 332 ms: 1.24x slower                                                             |
| shortest_path              | 290 ms                                                          | 361 ms: 1.24x slower                                                             |
| Geometric mean             | (ref)                                                           | 1.26x faster                                                                     |

Benchmark hidden because not significant (1): many_optionals
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250719-3.15.0a0-800d37f/bm-20250719-pythonperf1_win32-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.268x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.17x
- 95% likely to have a speedup of 1.16x
- 99% likely to have a speedup of 1.14x

# Memory
- memory change: unknown