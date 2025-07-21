# Results vs. 3.13.0

- fork: python
- ref: 800d37feca2e0ea33439
- machine: windows-amd64
- commit hash: 800d37f
- commit date: 2025-07-19
- overall geometric mean: 1.135x faster
- HPT reliability: 99.58%
- HPT 99th percentile: 1.01x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250719-pythonperf1_win32-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 250 ms                                                          | 227 ms: 1.10x faster                                                             |
| docutils       | 1.78 sec                                                        | 2.87 sec: 1.61x slower                                                           |
| html5lib       | 47.5 ms                                                         | 40.2 ms: 1.18x faster                                                            |
| sphinx         | 719 ms                                                          | 670 ms: 1.07x faster                                                             |
| Geometric mean | (ref)                                                           | 1.04x slower                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250719-pythonperf1_win32-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| asyncio_websockets         | 363 ms                                                          | 138 ms: 2.63x faster                                                             |
| async_tree_io_tg           | 494 ms                                                          | 329 ms: 1.50x faster                                                             |
| async_tree_io              | 526 ms                                                          | 353 ms: 1.49x faster                                                             |
| async_tree_memoization_tg  | 282 ms                                                          | 192 ms: 1.47x faster                                                             |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 311 ms: 1.47x faster                                                             |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 332 ms: 1.46x faster                                                             |
| async_tree_none_tg         | 214 ms                                                          | 149 ms: 1.44x faster                                                             |
| async_tree_none            | 245 ms                                                          | 172 ms: 1.42x faster                                                             |
| async_tree_memoization     | 297 ms                                                          | 214 ms: 1.39x faster                                                             |
| coroutines                 | 16.2 ms                                                         | 14.1 ms: 1.15x faster                                                            |
| async_generators           | 270 ms                                                          | 255 ms: 1.06x faster                                                             |
| Geometric mean             | (ref)                                                           | 1.46x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250719-pythonperf1_win32-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pidigits       | 201 ms                                                          | 135 ms: 1.48x faster                                                             |
| float          | 54.6 ms                                                         | 46.0 ms: 1.19x faster                                                            |
| Geometric mean | (ref)                                                           | 1.21x faster                                                                     |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250719-pythonperf1_win32-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_v8       | 16.8 ms                                                         | 12.8 ms: 1.32x faster                                                            |
| regex_effbot   | 1.80 ms                                                         | 1.49 ms: 1.21x faster                                                            |
| regex_compile  | 101 ms                                                          | 95.4 ms: 1.06x faster                                                            |
| regex_dna      | 114 ms                                                          | 112 ms: 1.01x faster                                                             |
| Geometric mean | (ref)                                                           | 1.14x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250719-pythonperf1_win32-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| json_loads           | 21.6 us                                                         | 15.8 us: 1.37x faster                                                            |
| xml_etree_parse      | 107 ms                                                          | 89.9 ms: 1.19x faster                                                            |
| json_dumps           | 7.30 ms                                                         | 6.58 ms: 1.11x faster                                                            |
| xml_etree_iterparse  | 62.6 ms                                                         | 58.0 ms: 1.08x faster                                                            |
| unpickle_pure_python | 160 us                                                          | 155 us: 1.03x faster                                                             |
| pickle_pure_python   | 231 us                                                          | 233 us: 1.01x slower                                                             |
| xml_etree_process    | 44.2 ms                                                         | 45.1 ms: 1.02x slower                                                            |
| xml_etree_generate   | 61.4 ms                                                         | 63.7 ms: 1.04x slower                                                            |
| tomli_loads          | 1.71 sec                                                        | 2.73 sec: 1.59x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.02x faster                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250719-pythonperf1_win32-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup         | 28.3 ms                                                         | 25.7 ms: 1.10x faster                                                            |
| python_startup_no_site | 19.7 ms                                                         | 19.4 ms: 1.01x faster                                                            |
| Geometric mean         | (ref)                                                           | 1.06x faster                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250719-pythonperf1_win32-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| genshi_xml      | 50.1 ms                                                         | 39.9 ms: 1.26x faster                                                            |
| django_template | 29.8 ms                                                         | 27.1 ms: 1.10x faster                                                            |
| genshi_text     | 21.5 ms                                                         | 20.0 ms: 1.07x faster                                                            |
| mako            | 7.09 ms                                                         | 9.68 ms: 1.37x slower                                                            |
| Geometric mean  | (ref)                                                           | 1.02x faster                                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250719-pythonperf1_win32-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| thrift                     | 9.98 ms                                                         | 570 us: 17.51x faster                                                            |
| coverage                   | 324 ms                                                          | 68.3 ms: 4.74x faster                                                            |
| pathlib                    | 82.9 ms                                                         | 30.5 ms: 2.72x faster                                                            |
| asyncio_websockets         | 363 ms                                                          | 138 ms: 2.63x faster                                                             |
| deepcopy                   | 314 us                                                          | 200 us: 1.57x faster                                                             |
| gc_traversal               | 1.75 ms                                                         | 1.15 ms: 1.52x faster                                                            |
| async_tree_io_tg           | 494 ms                                                          | 329 ms: 1.50x faster                                                             |
| async_tree_io              | 526 ms                                                          | 353 ms: 1.49x faster                                                             |
| pidigits                   | 201 ms                                                          | 135 ms: 1.48x faster                                                             |
| async_tree_memoization_tg  | 282 ms                                                          | 192 ms: 1.47x faster                                                             |
| sqlite_synth               | 1.95 us                                                         | 1.33 us: 1.47x faster                                                            |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 311 ms: 1.47x faster                                                             |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 332 ms: 1.46x faster                                                             |
| async_tree_none_tg         | 214 ms                                                          | 149 ms: 1.44x faster                                                             |
| async_tree_none            | 245 ms                                                          | 172 ms: 1.42x faster                                                             |
| mdp                        | 1.62 sec                                                        | 1.16 sec: 1.40x faster                                                           |
| json                       | 4.27 ms                                                         | 3.06 ms: 1.40x faster                                                            |
| deepcopy_reduce            | 2.92 us                                                         | 2.10 us: 1.39x faster                                                            |
| async_tree_memoization     | 297 ms                                                          | 214 ms: 1.39x faster                                                             |
| json_loads                 | 21.6 us                                                         | 15.8 us: 1.37x faster                                                            |
| telco                      | 6.96 ms                                                         | 5.25 ms: 1.32x faster                                                            |
| regex_v8                   | 16.8 ms                                                         | 12.8 ms: 1.32x faster                                                            |
| genshi_xml                 | 50.1 ms                                                         | 39.9 ms: 1.26x faster                                                            |
| pycparser                  | 872 ms                                                          | 715 ms: 1.22x faster                                                             |
| deepcopy_memo              | 25.4 us                                                         | 21.0 us: 1.21x faster                                                            |
| regex_effbot               | 1.80 ms                                                         | 1.49 ms: 1.21x faster                                                            |
| xml_etree_parse            | 107 ms                                                          | 89.9 ms: 1.19x faster                                                            |
| logging_format             | 8.72 us                                                         | 7.32 us: 1.19x faster                                                            |
| go                         | 109 ms                                                          | 91.4 ms: 1.19x faster                                                            |
| float                      | 54.6 ms                                                         | 46.0 ms: 1.19x faster                                                            |
| html5lib                   | 47.5 ms                                                         | 40.2 ms: 1.18x faster                                                            |
| logging_simple             | 7.99 us                                                         | 6.86 us: 1.16x faster                                                            |
| sympy_expand               | 373 ms                                                          | 321 ms: 1.16x faster                                                             |
| dulwich_log                | 48.8 ms                                                         | 42.1 ms: 1.16x faster                                                            |
| coroutines                 | 16.2 ms                                                         | 14.1 ms: 1.15x faster                                                            |
| bench_mp_pool              | 90.6 ms                                                         | 78.5 ms: 1.15x faster                                                            |
| pprint_safe_repr           | 648 ms                                                          | 567 ms: 1.14x faster                                                             |
| sympy_str                  | 212 ms                                                          | 189 ms: 1.12x faster                                                             |
| json_dumps                 | 7.30 ms                                                         | 6.58 ms: 1.11x faster                                                            |
| 2to3                       | 250 ms                                                          | 227 ms: 1.10x faster                                                             |
| pylint                     | 227 ms                                                          | 205 ms: 1.10x faster                                                             |
| python_startup             | 28.3 ms                                                         | 25.7 ms: 1.10x faster                                                            |
| django_template            | 29.8 ms                                                         | 27.1 ms: 1.10x faster                                                            |
| sympy_sum                  | 106 ms                                                          | 97.0 ms: 1.09x faster                                                            |
| chaos                      | 50.2 ms                                                         | 46.2 ms: 1.09x faster                                                            |
| xml_etree_iterparse        | 62.6 ms                                                         | 58.0 ms: 1.08x faster                                                            |
| sphinx                     | 719 ms                                                          | 670 ms: 1.07x faster                                                             |
| genshi_text                | 21.5 ms                                                         | 20.0 ms: 1.07x faster                                                            |
| typing_runtime_protocols   | 138 us                                                          | 128 us: 1.07x faster                                                             |
| create_gc_cycles           | 1.06 ms                                                         | 996 us: 1.06x faster                                                             |
| sympy_integrate            | 15.0 ms                                                         | 14.1 ms: 1.06x faster                                                            |
| comprehensions             | 12.5 us                                                         | 11.8 us: 1.06x faster                                                            |
| regex_compile              | 101 ms                                                          | 95.4 ms: 1.06x faster                                                            |
| async_generators           | 270 ms                                                          | 255 ms: 1.06x faster                                                             |
| pyflate                    | 320 ms                                                          | 308 ms: 1.04x faster                                                             |
| unpickle_pure_python       | 160 us                                                          | 155 us: 1.03x faster                                                             |
| regex_dna                  | 114 ms                                                          | 112 ms: 1.01x faster                                                             |
| python_startup_no_site     | 19.7 ms                                                         | 19.4 ms: 1.01x faster                                                            |
| fannkuch                   | 299 ms                                                          | 300 ms: 1.00x slower                                                             |
| nqueens                    | 72.1 ms                                                         | 72.6 ms: 1.01x slower                                                            |
| scimark_sor                | 85.9 ms                                                         | 86.6 ms: 1.01x slower                                                            |
| pickle_pure_python         | 231 us                                                          | 233 us: 1.01x slower                                                             |
| xml_etree_process          | 44.2 ms                                                         | 45.1 ms: 1.02x slower                                                            |
| crypto_pyaes               | 56.9 ms                                                         | 58.3 ms: 1.02x slower                                                            |
| logging_silent             | 60.3 ns                                                         | 62.0 ns: 1.03x slower                                                            |
| deltablue                  | 2.33 ms                                                         | 2.41 ms: 1.03x slower                                                            |
| scimark_monte_carlo        | 47.7 ms                                                         | 49.3 ms: 1.03x slower                                                            |
| xml_etree_generate         | 61.4 ms                                                         | 63.7 ms: 1.04x slower                                                            |
| richards                   | 32.7 ms                                                         | 34.0 ms: 1.04x slower                                                            |
| scimark_fft                | 205 ms                                                          | 213 ms: 1.04x slower                                                             |
| hexiom                     | 4.44 ms                                                         | 4.64 ms: 1.04x slower                                                            |
| generators                 | 21.8 ms                                                         | 22.9 ms: 1.05x slower                                                            |
| raytrace                   | 201 ms                                                          | 214 ms: 1.06x slower                                                             |
| spectral_norm              | 69.4 ms                                                         | 74.6 ms: 1.07x slower                                                            |
| scimark_lu                 | 60.2 ms                                                         | 65.3 ms: 1.08x slower                                                            |
| many_optionals             | 436 us                                                          | 475 us: 1.09x slower                                                             |
| richards_super             | 36.7 ms                                                         | 40.2 ms: 1.10x slower                                                            |
| bench_thread_pool          | 1.00 ms                                                         | 1.10 ms: 1.10x slower                                                            |
| scimark_sparse_mat_mult    | 2.84 ms                                                         | 3.18 ms: 1.12x slower                                                            |
| meteor_contest             | 74.6 ms                                                         | 85.4 ms: 1.15x slower                                                            |
| pprint_pformat             | 1.33 sec                                                        | 1.69 sec: 1.28x slower                                                           |
| subparsers                 | 14.8 ms                                                         | 19.1 ms: 1.29x slower                                                            |
| mako                       | 7.09 ms                                                         | 9.68 ms: 1.37x slower                                                            |
| bpe_tokeniser              | 3.46 sec                                                        | 5.48 sec: 1.58x slower                                                           |
| tomli_loads                | 1.71 sec                                                        | 2.73 sec: 1.59x slower                                                           |
| docutils                   | 1.78 sec                                                        | 2.87 sec: 1.61x slower                                                           |
| k_core                     | 1.38 sec                                                        | 2.67 sec: 1.94x slower                                                           |
| shortest_path              | 290 ms                                                          | 650 ms: 2.24x slower                                                             |
| connected_components       | 267 ms                                                          | 614 ms: 2.30x slower                                                             |
| Geometric mean             | (ref)                                                           | 1.13x faster                                                                     |

Benchmark hidden because not significant (1): nbody
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250719-3.15.0a0-800d37f-NOGIL/bm-20250719-pythonperf1_win32-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.135x faster

# HPT report

- Reliability score: 99.58% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: unknown