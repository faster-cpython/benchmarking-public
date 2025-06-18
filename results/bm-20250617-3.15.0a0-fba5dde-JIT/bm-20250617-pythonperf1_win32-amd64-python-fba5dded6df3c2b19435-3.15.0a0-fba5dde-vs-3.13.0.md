# Results vs. 3.13.0

- fork: python
- ref: fba5dded6df3c2b19435
- machine: windows-amd64
- commit hash: fba5dde
- commit date: 2025-06-17
- overall geometric mean: 1.067x slower
- HPT reliability: 99.98%
- HPT 99th percentile: 1.03x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250617-pythonperf1_win32-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 250 ms                                                          | 288 ms: 1.15x slower                                                             |
| docutils       | 1.78 sec                                                        | 2.11 sec: 1.19x slower                                                           |
| html5lib       | 47.5 ms                                                         | 53.0 ms: 1.11x slower                                                            |
| sphinx         | 719 ms                                                          | 859 ms: 1.20x slower                                                             |
| Geometric mean | (ref)                                                           | 1.16x slower                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250617-pythonperf1_win32-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| asyncio_websockets         | 363 ms                                                          | 158 ms: 2.29x faster                                                             |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 433 ms: 1.12x faster                                                             |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 429 ms: 1.06x faster                                                             |
| async_tree_none            | 245 ms                                                          | 235 ms: 1.04x faster                                                             |
| async_tree_memoization     | 297 ms                                                          | 288 ms: 1.03x faster                                                             |
| async_tree_memoization_tg  | 282 ms                                                          | 285 ms: 1.01x slower                                                             |
| async_tree_io              | 526 ms                                                          | 536 ms: 1.02x slower                                                             |
| async_tree_none_tg         | 214 ms                                                          | 229 ms: 1.07x slower                                                             |
| async_tree_io_tg           | 494 ms                                                          | 555 ms: 1.12x slower                                                             |
| async_generators           | 270 ms                                                          | 354 ms: 1.31x slower                                                             |
| coroutines                 | 16.2 ms                                                         | 26.8 ms: 1.65x slower                                                            |
| Geometric mean             | (ref)                                                           | 1.01x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250617-pythonperf1_win32-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| nbody          | 80.0 ms                                                         | 53.4 ms: 1.50x faster                                                            |
| pidigits       | 201 ms                                                          | 147 ms: 1.37x faster                                                             |
| float          | 54.6 ms                                                         | 78.5 ms: 1.44x slower                                                            |
| Geometric mean | (ref)                                                           | 1.13x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250617-pythonperf1_win32-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_effbot   | 1.80 ms                                                         | 1.74 ms: 1.04x faster                                                            |
| regex_dna      | 114 ms                                                          | 117 ms: 1.03x slower                                                             |
| regex_compile  | 101 ms                                                          | 122 ms: 1.21x slower                                                             |
| Geometric mean | (ref)                                                           | 1.05x slower                                                                     |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250617-pythonperf1_win32-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| tomli_loads          | 1.71 sec                                                        | 1.59 sec: 1.08x faster                                                           |
| json_loads           | 21.6 us                                                         | 20.8 us: 1.04x faster                                                            |
| xml_etree_parse      | 107 ms                                                          | 105 ms: 1.02x faster                                                             |
| unpickle_pure_python | 160 us                                                          | 158 us: 1.02x faster                                                             |
| xml_etree_generate   | 61.4 ms                                                         | 72.2 ms: 1.18x slower                                                            |
| json_dumps           | 7.30 ms                                                         | 8.68 ms: 1.19x slower                                                            |
| xml_etree_process    | 44.2 ms                                                         | 53.0 ms: 1.20x slower                                                            |
| xml_etree_iterparse  | 62.6 ms                                                         | 88.1 ms: 1.41x slower                                                            |
| pickle_pure_python   | 231 us                                                          | 329 us: 1.42x slower                                                             |
| Geometric mean       | (ref)                                                           | 1.12x slower                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250617-pythonperf1_win32-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup         | 28.3 ms                                                         | 27.3 ms: 1.03x faster                                                            |
| python_startup_no_site | 19.7 ms                                                         | 20.0 ms: 1.02x slower                                                            |
| Geometric mean         | (ref)                                                           | 1.01x faster                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250617-pythonperf1_win32-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| genshi_xml      | 50.1 ms                                                         | 51.1 ms: 1.02x slower                                                            |
| genshi_text     | 21.5 ms                                                         | 25.4 ms: 1.18x slower                                                            |
| django_template | 29.8 ms                                                         | 38.7 ms: 1.30x slower                                                            |
| Geometric mean  | (ref)                                                           | 1.12x slower                                                                     |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250617-pythonperf1_win32-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| thrift                     | 9.98 ms                                                         | 719 us: 13.87x faster                                                            |
| coverage                   | 324 ms                                                          | 62.6 ms: 5.17x faster                                                            |
| pathlib                    | 82.9 ms                                                         | 34.9 ms: 2.37x faster                                                            |
| asyncio_websockets         | 363 ms                                                          | 158 ms: 2.29x faster                                                             |
| nbody                      | 80.0 ms                                                         | 53.4 ms: 1.50x faster                                                            |
| pidigits                   | 201 ms                                                          | 147 ms: 1.37x faster                                                             |
| mdp                        | 1.62 sec                                                        | 1.20 sec: 1.35x faster                                                           |
| telco                      | 6.96 ms                                                         | 5.44 ms: 1.28x faster                                                            |
| deepcopy                   | 314 us                                                          | 273 us: 1.15x faster                                                             |
| sqlite_synth               | 1.95 us                                                         | 1.74 us: 1.12x faster                                                            |
| bpe_tokeniser              | 3.46 sec                                                        | 3.09 sec: 1.12x faster                                                           |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 433 ms: 1.12x faster                                                             |
| scimark_fft                | 205 ms                                                          | 184 ms: 1.11x faster                                                             |
| tomli_loads                | 1.71 sec                                                        | 1.59 sec: 1.08x faster                                                           |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 429 ms: 1.06x faster                                                             |
| fannkuch                   | 299 ms                                                          | 284 ms: 1.05x faster                                                             |
| json                       | 4.27 ms                                                         | 4.07 ms: 1.05x faster                                                            |
| scimark_sparse_mat_mult    | 2.84 ms                                                         | 2.72 ms: 1.04x faster                                                            |
| json_loads                 | 21.6 us                                                         | 20.8 us: 1.04x faster                                                            |
| async_tree_none            | 245 ms                                                          | 235 ms: 1.04x faster                                                             |
| regex_effbot               | 1.80 ms                                                         | 1.74 ms: 1.04x faster                                                            |
| python_startup             | 28.3 ms                                                         | 27.3 ms: 1.03x faster                                                            |
| async_tree_memoization     | 297 ms                                                          | 288 ms: 1.03x faster                                                             |
| deepcopy_reduce            | 2.92 us                                                         | 2.83 us: 1.03x faster                                                            |
| xml_etree_parse            | 107 ms                                                          | 105 ms: 1.02x faster                                                             |
| bench_thread_pool          | 1.00 ms                                                         | 984 us: 1.02x faster                                                             |
| unpickle_pure_python       | 160 us                                                          | 158 us: 1.02x faster                                                             |
| async_tree_memoization_tg  | 282 ms                                                          | 285 ms: 1.01x slower                                                             |
| python_startup_no_site     | 19.7 ms                                                         | 20.0 ms: 1.02x slower                                                            |
| genshi_xml                 | 50.1 ms                                                         | 51.1 ms: 1.02x slower                                                            |
| async_tree_io              | 526 ms                                                          | 536 ms: 1.02x slower                                                             |
| pprint_pformat             | 1.33 sec                                                        | 1.37 sec: 1.03x slower                                                           |
| regex_dna                  | 114 ms                                                          | 117 ms: 1.03x slower                                                             |
| pprint_safe_repr           | 648 ms                                                          | 671 ms: 1.03x slower                                                             |
| typing_runtime_protocols   | 138 us                                                          | 144 us: 1.05x slower                                                             |
| async_tree_none_tg         | 214 ms                                                          | 229 ms: 1.07x slower                                                             |
| dulwich_log                | 48.8 ms                                                         | 52.4 ms: 1.08x slower                                                            |
| crypto_pyaes               | 56.9 ms                                                         | 62.2 ms: 1.09x slower                                                            |
| sympy_expand               | 373 ms                                                          | 410 ms: 1.10x slower                                                             |
| pycparser                  | 872 ms                                                          | 958 ms: 1.10x slower                                                             |
| sympy_sum                  | 106 ms                                                          | 116 ms: 1.10x slower                                                             |
| meteor_contest             | 74.6 ms                                                         | 83.0 ms: 1.11x slower                                                            |
| html5lib                   | 47.5 ms                                                         | 53.0 ms: 1.11x slower                                                            |
| pylint                     | 227 ms                                                          | 253 ms: 1.12x slower                                                             |
| sympy_str                  | 212 ms                                                          | 236 ms: 1.12x slower                                                             |
| async_tree_io_tg           | 494 ms                                                          | 555 ms: 1.12x slower                                                             |
| sympy_integrate            | 15.0 ms                                                         | 17.0 ms: 1.14x slower                                                            |
| 2to3                       | 250 ms                                                          | 288 ms: 1.15x slower                                                             |
| logging_format             | 8.72 us                                                         | 10.1 us: 1.16x slower                                                            |
| bench_mp_pool              | 90.6 ms                                                         | 106 ms: 1.17x slower                                                             |
| xml_etree_generate         | 61.4 ms                                                         | 72.2 ms: 1.18x slower                                                            |
| genshi_text                | 21.5 ms                                                         | 25.4 ms: 1.18x slower                                                            |
| docutils                   | 1.78 sec                                                        | 2.11 sec: 1.19x slower                                                           |
| json_dumps                 | 7.30 ms                                                         | 8.68 ms: 1.19x slower                                                            |
| sphinx                     | 719 ms                                                          | 859 ms: 1.20x slower                                                             |
| xml_etree_process          | 44.2 ms                                                         | 53.0 ms: 1.20x slower                                                            |
| logging_simple             | 7.99 us                                                         | 9.59 us: 1.20x slower                                                            |
| regex_compile              | 101 ms                                                          | 122 ms: 1.21x slower                                                             |
| connected_components       | 267 ms                                                          | 322 ms: 1.21x slower                                                             |
| pyflate                    | 320 ms                                                          | 390 ms: 1.22x slower                                                             |
| k_core                     | 1.38 sec                                                        | 1.68 sec: 1.22x slower                                                           |
| go                         | 109 ms                                                          | 136 ms: 1.25x slower                                                             |
| shortest_path              | 290 ms                                                          | 365 ms: 1.26x slower                                                             |
| comprehensions             | 12.5 us                                                         | 15.9 us: 1.27x slower                                                            |
| nqueens                    | 72.1 ms                                                         | 91.8 ms: 1.27x slower                                                            |
| django_template            | 29.8 ms                                                         | 38.7 ms: 1.30x slower                                                            |
| many_optionals             | 436 us                                                          | 572 us: 1.31x slower                                                             |
| chaos                      | 50.2 ms                                                         | 65.9 ms: 1.31x slower                                                            |
| async_generators           | 270 ms                                                          | 354 ms: 1.31x slower                                                             |
| create_gc_cycles           | 1.06 ms                                                         | 1.47 ms: 1.39x slower                                                            |
| deepcopy_memo              | 25.4 us                                                         | 35.5 us: 1.40x slower                                                            |
| xml_etree_iterparse        | 62.6 ms                                                         | 88.1 ms: 1.41x slower                                                            |
| pickle_pure_python         | 231 us                                                          | 329 us: 1.42x slower                                                             |
| float                      | 54.6 ms                                                         | 78.5 ms: 1.44x slower                                                            |
| raytrace                   | 201 ms                                                          | 306 ms: 1.52x slower                                                             |
| subparsers                 | 14.8 ms                                                         | 23.0 ms: 1.56x slower                                                            |
| scimark_monte_carlo        | 47.7 ms                                                         | 74.8 ms: 1.57x slower                                                            |
| scimark_sor                | 85.9 ms                                                         | 137 ms: 1.59x slower                                                             |
| richards                   | 32.7 ms                                                         | 53.9 ms: 1.65x slower                                                            |
| richards_super             | 36.7 ms                                                         | 60.6 ms: 1.65x slower                                                            |
| coroutines                 | 16.2 ms                                                         | 26.8 ms: 1.65x slower                                                            |
| spectral_norm              | 69.4 ms                                                         | 115 ms: 1.66x slower                                                             |
| gc_traversal               | 1.75 ms                                                         | 2.99 ms: 1.71x slower                                                            |
| generators                 | 21.8 ms                                                         | 38.2 ms: 1.76x slower                                                            |
| hexiom                     | 4.44 ms                                                         | 7.98 ms: 1.80x slower                                                            |
| deltablue                  | 2.33 ms                                                         | 4.52 ms: 1.94x slower                                                            |
| scimark_lu                 | 60.2 ms                                                         | 126 ms: 2.09x slower                                                             |
| logging_silent             | 60.3 ns                                                         | 507 ns: 8.40x slower                                                             |
| Geometric mean             | (ref)                                                           | 1.10x slower                                                                     |

Benchmark hidden because not significant (2): regex_v8, mako
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250617-3.15.0a0-fba5dde-JIT/bm-20250617-pythonperf1_win32-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.067x slower

# HPT report

- Reliability score: 99.98% likely to be slow
- 90% likely to have a slowdown of 1.06x
- 95% likely to have a slowdown of 1.05x
- 99% likely to have a slowdown of 1.03x

# Memory
- memory change: unknown