# Results vs. 3.13.0

- fork: python
- ref: cebae977a63f32c3c03d
- machine: windows-amd64
- commit hash: cebae97
- commit date: 2025-06-01
- overall geometric mean: 1.198x faster
- HPT reliability: 99.87%
- HPT 99th percentile: 1.02x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250601-pythonperf1_win32-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 250 ms                                                          | 285 ms: 1.14x slower                                                             |
| docutils       | 1.78 sec                                                        | 2.06 sec: 1.16x slower                                                           |
| html5lib       | 47.5 ms                                                         | 51.3 ms: 1.08x slower                                                            |
| sphinx         | 719 ms                                                          | 842 ms: 1.17x slower                                                             |
| Geometric mean | (ref)                                                           | 1.14x slower                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250601-pythonperf1_win32-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| asyncio_websockets         | 363 ms                                                          | 158 ms: 2.29x faster                                                             |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 426 ms: 1.14x faster                                                             |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 424 ms: 1.08x faster                                                             |
| async_tree_none            | 245 ms                                                          | 230 ms: 1.06x faster                                                             |
| async_tree_memoization     | 297 ms                                                          | 281 ms: 1.05x faster                                                             |
| async_tree_memoization_tg  | 282 ms                                                          | 279 ms: 1.01x faster                                                             |
| async_tree_io              | 526 ms                                                          | 535 ms: 1.02x slower                                                             |
| async_tree_none_tg         | 214 ms                                                          | 228 ms: 1.06x slower                                                             |
| async_tree_io_tg           | 494 ms                                                          | 537 ms: 1.09x slower                                                             |
| async_generators           | 270 ms                                                          | 352 ms: 1.30x slower                                                             |
| coroutines                 | 16.2 ms                                                         | 25.1 ms: 1.55x slower                                                            |
| Geometric mean             | (ref)                                                           | 1.03x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250601-pythonperf1_win32-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| nbody          | 80.0 ms                                                         | 55.8 ms: 1.43x faster                                                            |
| pidigits       | 201 ms                                                          | 145 ms: 1.38x faster                                                             |
| float          | 54.6 ms                                                         | 78.1 ms: 1.43x slower                                                            |
| Geometric mean | (ref)                                                           | 1.12x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250601-pythonperf1_win32-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_effbot   | 1.80 ms                                                         | 1.78 ms: 1.01x faster                                                            |
| regex_dna      | 114 ms                                                          | 117 ms: 1.03x slower                                                             |
| regex_compile  | 101 ms                                                          | 112 ms: 1.11x slower                                                             |
| Geometric mean | (ref)                                                           | 1.02x slower                                                                     |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250601-pythonperf1_win32-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| tomli_loads          | 1.71 sec                                                        | 1.55 sec: 1.11x faster                                                           |
| json_loads           | 21.6 us                                                         | 20.3 us: 1.06x faster                                                            |
| xml_etree_parse      | 107 ms                                                          | 103 ms: 1.04x faster                                                             |
| unpickle_pure_python | 160 us                                                          | 155 us: 1.03x faster                                                             |
| xml_etree_generate   | 61.4 ms                                                         | 69.5 ms: 1.13x slower                                                            |
| xml_etree_process    | 44.2 ms                                                         | 50.9 ms: 1.15x slower                                                            |
| json_dumps           | 7.30 ms                                                         | 8.76 ms: 1.20x slower                                                            |
| xml_etree_iterparse  | 62.6 ms                                                         | 84.8 ms: 1.36x slower                                                            |
| pickle_pure_python   | 231 us                                                          | 318 us: 1.38x slower                                                             |
| Geometric mean       | (ref)                                                           | 1.10x slower                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250601-pythonperf1_win32-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup         | 28.3 ms                                                         | 27.2 ms: 1.04x faster                                                            |
| python_startup_no_site | 19.7 ms                                                         | 19.9 ms: 1.01x slower                                                            |
| Geometric mean         | (ref)                                                           | 1.01x faster                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250601-pythonperf1_win32-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| genshi_xml      | 50.1 ms                                                         | 49.0 ms: 1.02x faster                                                            |
| genshi_text     | 21.5 ms                                                         | 24.1 ms: 1.12x slower                                                            |
| django_template | 29.8 ms                                                         | 37.3 ms: 1.25x slower                                                            |
| Geometric mean  | (ref)                                                           | 1.08x slower                                                                     |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250601-pythonperf1_win32-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pprint_pformat             | 1.33 sec                                                        | 1.56 us: 850217.50x faster                                                       |
| pprint_safe_repr           | 648 ms                                                          | 900 ns: 720675.39x faster                                                        |
| pathlib                    | 82.9 ms                                                         | 33.8 ms: 2.45x faster                                                            |
| asyncio_websockets         | 363 ms                                                          | 158 ms: 2.29x faster                                                             |
| nbody                      | 80.0 ms                                                         | 55.8 ms: 1.43x faster                                                            |
| pidigits                   | 201 ms                                                          | 145 ms: 1.38x faster                                                             |
| mdp                        | 1.62 sec                                                        | 1.20 sec: 1.36x faster                                                           |
| telco                      | 6.96 ms                                                         | 5.13 ms: 1.36x faster                                                            |
| deepcopy                   | 314 us                                                          | 269 us: 1.17x faster                                                             |
| bpe_tokeniser              | 3.46 sec                                                        | 3.03 sec: 1.14x faster                                                           |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 426 ms: 1.14x faster                                                             |
| sqlite_synth               | 1.95 us                                                         | 1.73 us: 1.13x faster                                                            |
| scimark_fft                | 205 ms                                                          | 184 ms: 1.11x faster                                                             |
| tomli_loads                | 1.71 sec                                                        | 1.55 sec: 1.11x faster                                                           |
| scimark_sparse_mat_mult    | 2.84 ms                                                         | 2.61 ms: 1.09x faster                                                            |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 424 ms: 1.08x faster                                                             |
| json                       | 4.27 ms                                                         | 4.01 ms: 1.07x faster                                                            |
| json_loads                 | 21.6 us                                                         | 20.3 us: 1.06x faster                                                            |
| async_tree_none            | 245 ms                                                          | 230 ms: 1.06x faster                                                             |
| async_tree_memoization     | 297 ms                                                          | 281 ms: 1.05x faster                                                             |
| fannkuch                   | 299 ms                                                          | 285 ms: 1.05x faster                                                             |
| deepcopy_reduce            | 2.92 us                                                         | 2.80 us: 1.04x faster                                                            |
| python_startup             | 28.3 ms                                                         | 27.2 ms: 1.04x faster                                                            |
| xml_etree_parse            | 107 ms                                                          | 103 ms: 1.04x faster                                                             |
| unpickle_pure_python       | 160 us                                                          | 155 us: 1.03x faster                                                             |
| genshi_xml                 | 50.1 ms                                                         | 49.0 ms: 1.02x faster                                                            |
| bench_thread_pool          | 1.00 ms                                                         | 981 us: 1.02x faster                                                             |
| async_tree_memoization_tg  | 282 ms                                                          | 279 ms: 1.01x faster                                                             |
| regex_effbot               | 1.80 ms                                                         | 1.78 ms: 1.01x faster                                                            |
| python_startup_no_site     | 19.7 ms                                                         | 19.9 ms: 1.01x slower                                                            |
| async_tree_io              | 526 ms                                                          | 535 ms: 1.02x slower                                                             |
| regex_dna                  | 114 ms                                                          | 117 ms: 1.03x slower                                                             |
| typing_runtime_protocols   | 138 us                                                          | 144 us: 1.05x slower                                                             |
| async_tree_none_tg         | 214 ms                                                          | 228 ms: 1.06x slower                                                             |
| pycparser                  | 872 ms                                                          | 930 ms: 1.07x slower                                                             |
| sympy_sum                  | 106 ms                                                          | 113 ms: 1.07x slower                                                             |
| dulwich_log                | 48.8 ms                                                         | 52.2 ms: 1.07x slower                                                            |
| sympy_expand               | 373 ms                                                          | 403 ms: 1.08x slower                                                             |
| html5lib                   | 47.5 ms                                                         | 51.3 ms: 1.08x slower                                                            |
| async_tree_io_tg           | 494 ms                                                          | 537 ms: 1.09x slower                                                             |
| crypto_pyaes               | 56.9 ms                                                         | 62.0 ms: 1.09x slower                                                            |
| sympy_str                  | 212 ms                                                          | 231 ms: 1.09x slower                                                             |
| pylint                     | 227 ms                                                          | 247 ms: 1.09x slower                                                             |
| meteor_contest             | 74.6 ms                                                         | 82.2 ms: 1.10x slower                                                            |
| regex_compile              | 101 ms                                                          | 112 ms: 1.11x slower                                                             |
| sympy_integrate            | 15.0 ms                                                         | 16.7 ms: 1.12x slower                                                            |
| genshi_text                | 21.5 ms                                                         | 24.1 ms: 1.12x slower                                                            |
| xml_etree_generate         | 61.4 ms                                                         | 69.5 ms: 1.13x slower                                                            |
| bench_mp_pool              | 90.6 ms                                                         | 103 ms: 1.13x slower                                                             |
| logging_format             | 8.72 us                                                         | 9.89 us: 1.13x slower                                                            |
| 2to3                       | 250 ms                                                          | 285 ms: 1.14x slower                                                             |
| xml_etree_process          | 44.2 ms                                                         | 50.9 ms: 1.15x slower                                                            |
| docutils                   | 1.78 sec                                                        | 2.06 sec: 1.16x slower                                                           |
| sphinx                     | 719 ms                                                          | 842 ms: 1.17x slower                                                             |
| logging_simple             | 7.99 us                                                         | 9.40 us: 1.18x slower                                                            |
| connected_components       | 267 ms                                                          | 317 ms: 1.19x slower                                                             |
| pyflate                    | 320 ms                                                          | 383 ms: 1.20x slower                                                             |
| json_dumps                 | 7.30 ms                                                         | 8.76 ms: 1.20x slower                                                            |
| k_core                     | 1.38 sec                                                        | 1.67 sec: 1.21x slower                                                           |
| go                         | 109 ms                                                          | 132 ms: 1.22x slower                                                             |
| comprehensions             | 12.5 us                                                         | 15.4 us: 1.23x slower                                                            |
| shortest_path              | 290 ms                                                          | 359 ms: 1.24x slower                                                             |
| django_template            | 29.8 ms                                                         | 37.3 ms: 1.25x slower                                                            |
| nqueens                    | 72.1 ms                                                         | 91.1 ms: 1.26x slower                                                            |
| chaos                      | 50.2 ms                                                         | 64.9 ms: 1.29x slower                                                            |
| many_optionals             | 436 us                                                          | 565 us: 1.29x slower                                                             |
| async_generators           | 270 ms                                                          | 352 ms: 1.30x slower                                                             |
| create_gc_cycles           | 1.06 ms                                                         | 1.41 ms: 1.33x slower                                                            |
| deepcopy_memo              | 25.4 us                                                         | 34.2 us: 1.35x slower                                                            |
| xml_etree_iterparse        | 62.6 ms                                                         | 84.8 ms: 1.36x slower                                                            |
| pickle_pure_python         | 231 us                                                          | 318 us: 1.38x slower                                                             |
| float                      | 54.6 ms                                                         | 78.1 ms: 1.43x slower                                                            |
| coverage                   | 324 ms                                                          | 479 ms: 1.48x slower                                                             |
| raytrace                   | 201 ms                                                          | 299 ms: 1.49x slower                                                             |
| subparsers                 | 14.8 ms                                                         | 22.5 ms: 1.53x slower                                                            |
| scimark_sor                | 85.9 ms                                                         | 131 ms: 1.53x slower                                                             |
| coroutines                 | 16.2 ms                                                         | 25.1 ms: 1.55x slower                                                            |
| scimark_monte_carlo        | 47.7 ms                                                         | 73.8 ms: 1.55x slower                                                            |
| gc_traversal               | 1.75 ms                                                         | 2.72 ms: 1.56x slower                                                            |
| richards                   | 32.7 ms                                                         | 51.4 ms: 1.57x slower                                                            |
| richards_super             | 36.7 ms                                                         | 58.2 ms: 1.59x slower                                                            |
| generators                 | 21.8 ms                                                         | 36.3 ms: 1.67x slower                                                            |
| spectral_norm              | 69.4 ms                                                         | 116 ms: 1.67x slower                                                             |
| hexiom                     | 4.44 ms                                                         | 7.69 ms: 1.73x slower                                                            |
| deltablue                  | 2.33 ms                                                         | 4.30 ms: 1.84x slower                                                            |
| scimark_lu                 | 60.2 ms                                                         | 120 ms: 2.00x slower                                                             |
| logging_silent             | 60.3 ns                                                         | 498 ns: 8.25x slower                                                             |
| thrift                     | 9.98 ms                                                         | 98.5 ms: 9.87x slower                                                            |
| Geometric mean             | (ref)                                                           | 1.17x faster                                                                     |

Benchmark hidden because not significant (2): regex_v8, mako
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250601-3.15.0a0-cebae97-JIT/bm-20250601-pythonperf1_win32-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.198x faster

# HPT report

- Reliability score: 99.87% likely to be slow
- 90% likely to have a slowdown of 1.07x
- 95% likely to have a slowdown of 1.05x
- 99% likely to have a slowdown of 1.02x

# Memory
- memory change: unknown