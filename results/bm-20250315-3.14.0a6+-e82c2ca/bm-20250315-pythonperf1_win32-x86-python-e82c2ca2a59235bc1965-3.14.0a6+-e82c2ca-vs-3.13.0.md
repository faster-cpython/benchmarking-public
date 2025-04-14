# Results vs. 3.13.0

- fork: python
- ref: e82c2ca2a59235bc1965
- machine: windows-x86
- commit hash: e82c2ca
- commit date: 2025-03-15
- overall geometric mean: 1.005x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250315-pythonperf1_win32-x86-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 250 ms                                                          | 264 ms: 1.05x slower                                                            |
| docutils       | 1.78 sec                                                        | 1.88 sec: 1.06x slower                                                          |
| html5lib       | 47.5 ms                                                         | 48.8 ms: 1.03x slower                                                           |
| sphinx         | 719 ms                                                          | 768 ms: 1.07x slower                                                            |
| Geometric mean | (ref)                                                           | 1.05x slower                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250315-pythonperf1_win32-x86-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 282 ms                                                          | 253 ms: 1.11x faster                                                            |
| async_tree_memoization     | 297 ms                                                          | 269 ms: 1.10x faster                                                            |
| async_tree_io              | 526 ms                                                          | 481 ms: 1.09x faster                                                            |
| async_tree_none            | 245 ms                                                          | 224 ms: 1.09x faster                                                            |
| async_tree_io_tg           | 494 ms                                                          | 462 ms: 1.07x faster                                                            |
| async_tree_none_tg         | 214 ms                                                          | 204 ms: 1.05x faster                                                            |
| asyncio_websockets         | 363 ms                                                          | 353 ms: 1.03x faster                                                            |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 481 ms: 1.01x faster                                                            |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 461 ms: 1.01x slower                                                            |
| coroutines                 | 16.2 ms                                                         | 16.6 ms: 1.02x slower                                                           |
| async_generators           | 270 ms                                                          | 311 ms: 1.15x slower                                                            |
| Geometric mean             | (ref)                                                           | 1.03x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250315-pythonperf1_win32-x86-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pidigits       | 201 ms                                                          | 204 ms: 1.02x slower                                                            |
| nbody          | 80.0 ms                                                         | 82.5 ms: 1.03x slower                                                           |
| Geometric mean | (ref)                                                           | 1.02x slower                                                                    |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250315-pythonperf1_win32-x86-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_effbot   | 1.80 ms                                                         | 1.59 ms: 1.13x faster                                                           |
| regex_v8       | 16.8 ms                                                         | 15.3 ms: 1.10x faster                                                           |
| regex_compile  | 101 ms                                                          | 109 ms: 1.08x slower                                                            |
| regex_dna      | 114 ms                                                          | 126 ms: 1.11x slower                                                            |
| Geometric mean | (ref)                                                           | 1.01x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250315-pythonperf1_win32-x86-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| xml_etree_parse      | 107 ms                                                          | 108 ms: 1.01x slower                                                            |
| json_loads           | 21.6 us                                                         | 22.2 us: 1.03x slower                                                           |
| tomli_loads          | 1.71 sec                                                        | 1.78 sec: 1.04x slower                                                          |
| xml_etree_iterparse  | 62.6 ms                                                         | 66.3 ms: 1.06x slower                                                           |
| unpickle_pure_python | 160 us                                                          | 182 us: 1.14x slower                                                            |
| json_dumps           | 7.30 ms                                                         | 8.48 ms: 1.16x slower                                                           |
| xml_etree_generate   | 61.4 ms                                                         | 72.2 ms: 1.18x slower                                                           |
| xml_etree_process    | 44.2 ms                                                         | 53.3 ms: 1.21x slower                                                           |
| pickle_pure_python   | 231 us                                                          | 291 us: 1.26x slower                                                            |
| Geometric mean       | (ref)                                                           | 1.12x slower                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250315-pythonperf1_win32-x86-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 28.3 ms                                                         | 29.0 ms: 1.02x slower                                                           |
| python_startup_no_site | 19.7 ms                                                         | 22.8 ms: 1.16x slower                                                           |
| Geometric mean         | (ref)                                                           | 1.09x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250315-pythonperf1_win32-x86-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_xml      | 50.1 ms                                                         | 54.3 ms: 1.08x slower                                                           |
| genshi_text     | 21.5 ms                                                         | 23.9 ms: 1.11x slower                                                           |
| mako            | 7.09 ms                                                         | 8.18 ms: 1.15x slower                                                           |
| django_template | 29.8 ms                                                         | 35.4 ms: 1.19x slower                                                           |
| Geometric mean  | (ref)                                                           | 1.13x slower                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250315-pythonperf1_win32-x86-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| thrift                     | 9.98 ms                                                         | 779 us: 12.81x faster                                                           |
| coverage                   | 324 ms                                                          | 53.3 ms: 6.08x faster                                                           |
| pathlib                    | 82.9 ms                                                         | 37.9 ms: 2.19x faster                                                           |
| deepcopy                   | 314 us                                                          | 249 us: 1.26x faster                                                            |
| deepcopy_memo              | 25.4 us                                                         | 21.5 us: 1.18x faster                                                           |
| regex_effbot               | 1.80 ms                                                         | 1.59 ms: 1.13x faster                                                           |
| async_tree_memoization_tg  | 282 ms                                                          | 253 ms: 1.11x faster                                                            |
| async_tree_memoization     | 297 ms                                                          | 269 ms: 1.10x faster                                                            |
| regex_v8                   | 16.8 ms                                                         | 15.3 ms: 1.10x faster                                                           |
| async_tree_io              | 526 ms                                                          | 481 ms: 1.09x faster                                                            |
| async_tree_none            | 245 ms                                                          | 224 ms: 1.09x faster                                                            |
| async_tree_io_tg           | 494 ms                                                          | 462 ms: 1.07x faster                                                            |
| deepcopy_reduce            | 2.92 us                                                         | 2.74 us: 1.06x faster                                                           |
| async_tree_none_tg         | 214 ms                                                          | 204 ms: 1.05x faster                                                            |
| asyncio_websockets         | 363 ms                                                          | 353 ms: 1.03x faster                                                            |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 481 ms: 1.01x faster                                                            |
| telco                      | 6.96 ms                                                         | 6.92 ms: 1.01x faster                                                           |
| xml_etree_parse            | 107 ms                                                          | 108 ms: 1.01x slower                                                            |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 461 ms: 1.01x slower                                                            |
| pidigits                   | 201 ms                                                          | 204 ms: 1.02x slower                                                            |
| go                         | 109 ms                                                          | 111 ms: 1.02x slower                                                            |
| coroutines                 | 16.2 ms                                                         | 16.6 ms: 1.02x slower                                                           |
| python_startup             | 28.3 ms                                                         | 29.0 ms: 1.02x slower                                                           |
| json_loads                 | 21.6 us                                                         | 22.2 us: 1.03x slower                                                           |
| html5lib                   | 47.5 ms                                                         | 48.8 ms: 1.03x slower                                                           |
| pprint_safe_repr           | 648 ms                                                          | 667 ms: 1.03x slower                                                            |
| pprint_pformat             | 1.33 sec                                                        | 1.37 sec: 1.03x slower                                                          |
| gc_traversal               | 1.75 ms                                                         | 1.81 ms: 1.03x slower                                                           |
| nbody                      | 80.0 ms                                                         | 82.5 ms: 1.03x slower                                                           |
| tomli_loads                | 1.71 sec                                                        | 1.78 sec: 1.04x slower                                                          |
| spectral_norm              | 69.4 ms                                                         | 72.9 ms: 1.05x slower                                                           |
| sympy_sum                  | 106 ms                                                          | 111 ms: 1.05x slower                                                            |
| mdp                        | 1.62 sec                                                        | 1.71 sec: 1.05x slower                                                          |
| 2to3                       | 250 ms                                                          | 264 ms: 1.05x slower                                                            |
| docutils                   | 1.78 sec                                                        | 1.88 sec: 1.06x slower                                                          |
| xml_etree_iterparse        | 62.6 ms                                                         | 66.3 ms: 1.06x slower                                                           |
| bench_mp_pool              | 90.6 ms                                                         | 96.0 ms: 1.06x slower                                                           |
| connected_components       | 267 ms                                                          | 283 ms: 1.06x slower                                                            |
| sympy_str                  | 212 ms                                                          | 225 ms: 1.06x slower                                                            |
| json                       | 4.27 ms                                                         | 4.56 ms: 1.07x slower                                                           |
| sphinx                     | 719 ms                                                          | 768 ms: 1.07x slower                                                            |
| dulwich_log                | 48.8 ms                                                         | 52.1 ms: 1.07x slower                                                           |
| k_core                     | 1.38 sec                                                        | 1.47 sec: 1.07x slower                                                          |
| sympy_expand               | 373 ms                                                          | 401 ms: 1.07x slower                                                            |
| fannkuch                   | 299 ms                                                          | 321 ms: 1.07x slower                                                            |
| regex_compile              | 101 ms                                                          | 109 ms: 1.08x slower                                                            |
| pycparser                  | 872 ms                                                          | 939 ms: 1.08x slower                                                            |
| shortest_path              | 290 ms                                                          | 313 ms: 1.08x slower                                                            |
| sympy_integrate            | 15.0 ms                                                         | 16.2 ms: 1.08x slower                                                           |
| genshi_xml                 | 50.1 ms                                                         | 54.3 ms: 1.08x slower                                                           |
| bpe_tokeniser              | 3.46 sec                                                        | 3.75 sec: 1.08x slower                                                          |
| scimark_sor                | 85.9 ms                                                         | 93.5 ms: 1.09x slower                                                           |
| typing_runtime_protocols   | 138 us                                                          | 150 us: 1.09x slower                                                            |
| logging_simple             | 7.99 us                                                         | 8.79 us: 1.10x slower                                                           |
| scimark_lu                 | 60.2 ms                                                         | 66.4 ms: 1.10x slower                                                           |
| regex_dna                  | 114 ms                                                          | 126 ms: 1.11x slower                                                            |
| logging_format             | 8.72 us                                                         | 9.67 us: 1.11x slower                                                           |
| genshi_text                | 21.5 ms                                                         | 23.9 ms: 1.11x slower                                                           |
| scimark_monte_carlo        | 47.7 ms                                                         | 53.1 ms: 1.11x slower                                                           |
| logging_silent             | 60.3 ns                                                         | 67.3 ns: 1.12x slower                                                           |
| pyflate                    | 320 ms                                                          | 357 ms: 1.12x slower                                                            |
| scimark_fft                | 205 ms                                                          | 231 ms: 1.13x slower                                                            |
| unpickle_pure_python       | 160 us                                                          | 182 us: 1.14x slower                                                            |
| meteor_contest             | 74.6 ms                                                         | 84.9 ms: 1.14x slower                                                           |
| generators                 | 21.8 ms                                                         | 25.0 ms: 1.15x slower                                                           |
| richards                   | 32.7 ms                                                         | 37.5 ms: 1.15x slower                                                           |
| async_generators           | 270 ms                                                          | 311 ms: 1.15x slower                                                            |
| mako                       | 7.09 ms                                                         | 8.18 ms: 1.15x slower                                                           |
| python_startup_no_site     | 19.7 ms                                                         | 22.8 ms: 1.16x slower                                                           |
| crypto_pyaes               | 56.9 ms                                                         | 66.1 ms: 1.16x slower                                                           |
| json_dumps                 | 7.30 ms                                                         | 8.48 ms: 1.16x slower                                                           |
| richards_super             | 36.7 ms                                                         | 42.7 ms: 1.16x slower                                                           |
| scimark_sparse_mat_mult    | 2.84 ms                                                         | 3.32 ms: 1.17x slower                                                           |
| hexiom                     | 4.44 ms                                                         | 5.21 ms: 1.17x slower                                                           |
| comprehensions             | 12.5 us                                                         | 14.7 us: 1.17x slower                                                           |
| nqueens                    | 72.1 ms                                                         | 84.6 ms: 1.17x slower                                                           |
| xml_etree_generate         | 61.4 ms                                                         | 72.2 ms: 1.18x slower                                                           |
| django_template            | 29.8 ms                                                         | 35.4 ms: 1.19x slower                                                           |
| deltablue                  | 2.33 ms                                                         | 2.79 ms: 1.20x slower                                                           |
| xml_etree_process          | 44.2 ms                                                         | 53.3 ms: 1.21x slower                                                           |
| chaos                      | 50.2 ms                                                         | 60.9 ms: 1.21x slower                                                           |
| pickle_pure_python         | 231 us                                                          | 291 us: 1.26x slower                                                            |
| many_optionals             | 436 us                                                          | 549 us: 1.26x slower                                                            |
| bench_thread_pool          | 1.00 ms                                                         | 1.29 ms: 1.29x slower                                                           |
| raytrace                   | 201 ms                                                          | 266 ms: 1.32x slower                                                            |
| subparsers                 | 14.8 ms                                                         | 22.2 ms: 1.50x slower                                                           |
| Geometric mean             | (ref)                                                           | 1.01x slower                                                                    |

Benchmark hidden because not significant (4): sqlite_synth, create_gc_cycles, float, pylint
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250315-3.14.0a6+-e82c2ca/bm-20250315-pythonperf1_win32-x86-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.005x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.05x
- 95% likely to have a slowdown of 1.04x
- 99% likely to have a slowdown of 1.03x

# Memory
- memory change: unknown