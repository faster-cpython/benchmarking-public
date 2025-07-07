# Results vs. 3.13.0

- fork: python
- ref: 1953713d0d67a4f54ff7
- machine: windows-amd64
- commit hash: 1953713
- commit date: 2025-07-05
- overall geometric mean: 1.127x faster
- HPT reliability: 99.57%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250705-pythonperf1_win32-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 250 ms                                                          | 225 ms: 1.11x faster                                                             |
| docutils       | 1.78 sec                                                        | 2.88 sec: 1.62x slower                                                           |
| html5lib       | 47.5 ms                                                         | 41.3 ms: 1.15x faster                                                            |
| sphinx         | 719 ms                                                          | 664 ms: 1.08x faster                                                             |
| Geometric mean | (ref)                                                           | 1.04x slower                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250705-pythonperf1_win32-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713 |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| asyncio_websockets         | 363 ms                                                          | 138 ms: 2.64x faster                                                             |
| async_tree_io_tg           | 494 ms                                                          | 331 ms: 1.49x faster                                                             |
| async_tree_io              | 526 ms                                                          | 356 ms: 1.47x faster                                                             |
| async_tree_memoization_tg  | 282 ms                                                          | 193 ms: 1.46x faster                                                             |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 312 ms: 1.46x faster                                                             |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 334 ms: 1.45x faster                                                             |
| async_tree_none_tg         | 214 ms                                                          | 149 ms: 1.44x faster                                                             |
| async_tree_none            | 245 ms                                                          | 174 ms: 1.41x faster                                                             |
| async_tree_memoization     | 297 ms                                                          | 214 ms: 1.39x faster                                                             |
| coroutines                 | 16.2 ms                                                         | 14.7 ms: 1.11x faster                                                            |
| async_generators           | 270 ms                                                          | 262 ms: 1.03x faster                                                             |
| Geometric mean             | (ref)                                                           | 1.45x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250705-pythonperf1_win32-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pidigits       | 201 ms                                                          | 136 ms: 1.48x faster                                                             |
| float          | 54.6 ms                                                         | 45.9 ms: 1.19x faster                                                            |
| nbody          | 80.0 ms                                                         | 82.8 ms: 1.04x slower                                                            |
| Geometric mean | (ref)                                                           | 1.19x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250705-pythonperf1_win32-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_v8       | 16.8 ms                                                         | 13.4 ms: 1.26x faster                                                            |
| regex_effbot   | 1.80 ms                                                         | 1.58 ms: 1.14x faster                                                            |
| regex_compile  | 101 ms                                                          | 94.1 ms: 1.07x faster                                                            |
| regex_dna      | 114 ms                                                          | 115 ms: 1.01x slower                                                             |
| Geometric mean | (ref)                                                           | 1.11x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250705-pythonperf1_win32-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713 |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| json_loads           | 21.6 us                                                         | 16.1 us: 1.34x faster                                                            |
| xml_etree_parse      | 107 ms                                                          | 90.8 ms: 1.18x faster                                                            |
| json_dumps           | 7.30 ms                                                         | 6.65 ms: 1.10x faster                                                            |
| xml_etree_iterparse  | 62.6 ms                                                         | 58.7 ms: 1.07x faster                                                            |
| unpickle_pure_python | 160 us                                                          | 159 us: 1.01x faster                                                             |
| xml_etree_process    | 44.2 ms                                                         | 44.4 ms: 1.00x slower                                                            |
| xml_etree_generate   | 61.4 ms                                                         | 62.4 ms: 1.02x slower                                                            |
| tomli_loads          | 1.71 sec                                                        | 2.71 sec: 1.58x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.02x faster                                                                     |

Benchmark hidden because not significant (1): pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250705-pythonperf1_win32-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713 |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup         | 28.3 ms                                                         | 26.1 ms: 1.09x faster                                                            |
| python_startup_no_site | 19.7 ms                                                         | 19.4 ms: 1.01x faster                                                            |
| Geometric mean         | (ref)                                                           | 1.05x faster                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250705-pythonperf1_win32-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713 |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| genshi_xml      | 50.1 ms                                                         | 40.5 ms: 1.24x faster                                                            |
| genshi_text     | 21.5 ms                                                         | 19.7 ms: 1.09x faster                                                            |
| django_template | 29.8 ms                                                         | 27.5 ms: 1.08x faster                                                            |
| mako            | 7.09 ms                                                         | 9.74 ms: 1.37x slower                                                            |
| Geometric mean  | (ref)                                                           | 1.02x faster                                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250705-pythonperf1_win32-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713 |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| thrift                     | 9.98 ms                                                         | 570 us: 17.50x faster                                                            |
| coverage                   | 324 ms                                                          | 68.9 ms: 4.70x faster                                                            |
| asyncio_websockets         | 363 ms                                                          | 138 ms: 2.64x faster                                                             |
| pathlib                    | 82.9 ms                                                         | 32.5 ms: 2.55x faster                                                            |
| deepcopy                   | 314 us                                                          | 202 us: 1.56x faster                                                             |
| async_tree_io_tg           | 494 ms                                                          | 331 ms: 1.49x faster                                                             |
| pidigits                   | 201 ms                                                          | 136 ms: 1.48x faster                                                             |
| async_tree_io              | 526 ms                                                          | 356 ms: 1.47x faster                                                             |
| sqlite_synth               | 1.95 us                                                         | 1.33 us: 1.47x faster                                                            |
| async_tree_memoization_tg  | 282 ms                                                          | 193 ms: 1.46x faster                                                             |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 312 ms: 1.46x faster                                                             |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 334 ms: 1.45x faster                                                             |
| mdp                        | 1.62 sec                                                        | 1.13 sec: 1.44x faster                                                           |
| async_tree_none_tg         | 214 ms                                                          | 149 ms: 1.44x faster                                                             |
| gc_traversal               | 1.75 ms                                                         | 1.23 ms: 1.43x faster                                                            |
| async_tree_none            | 245 ms                                                          | 174 ms: 1.41x faster                                                             |
| async_tree_memoization     | 297 ms                                                          | 214 ms: 1.39x faster                                                             |
| json                       | 4.27 ms                                                         | 3.11 ms: 1.37x faster                                                            |
| deepcopy_reduce            | 2.92 us                                                         | 2.15 us: 1.36x faster                                                            |
| json_loads                 | 21.6 us                                                         | 16.1 us: 1.34x faster                                                            |
| telco                      | 6.96 ms                                                         | 5.44 ms: 1.28x faster                                                            |
| regex_v8                   | 16.8 ms                                                         | 13.4 ms: 1.26x faster                                                            |
| genshi_xml                 | 50.1 ms                                                         | 40.5 ms: 1.24x faster                                                            |
| deepcopy_memo              | 25.4 us                                                         | 20.7 us: 1.23x faster                                                            |
| pycparser                  | 872 ms                                                          | 725 ms: 1.20x faster                                                             |
| logging_format             | 8.72 us                                                         | 7.31 us: 1.19x faster                                                            |
| float                      | 54.6 ms                                                         | 45.9 ms: 1.19x faster                                                            |
| xml_etree_parse            | 107 ms                                                          | 90.8 ms: 1.18x faster                                                            |
| go                         | 109 ms                                                          | 92.3 ms: 1.18x faster                                                            |
| logging_simple             | 7.99 us                                                         | 6.78 us: 1.18x faster                                                            |
| dulwich_log                | 48.8 ms                                                         | 41.6 ms: 1.17x faster                                                            |
| sympy_expand               | 373 ms                                                          | 321 ms: 1.17x faster                                                             |
| html5lib                   | 47.5 ms                                                         | 41.3 ms: 1.15x faster                                                            |
| bench_mp_pool              | 90.6 ms                                                         | 79.2 ms: 1.14x faster                                                            |
| regex_effbot               | 1.80 ms                                                         | 1.58 ms: 1.14x faster                                                            |
| pprint_safe_repr           | 648 ms                                                          | 569 ms: 1.14x faster                                                             |
| sympy_str                  | 212 ms                                                          | 189 ms: 1.12x faster                                                             |
| 2to3                       | 250 ms                                                          | 225 ms: 1.11x faster                                                             |
| coroutines                 | 16.2 ms                                                         | 14.7 ms: 1.11x faster                                                            |
| json_dumps                 | 7.30 ms                                                         | 6.65 ms: 1.10x faster                                                            |
| genshi_text                | 21.5 ms                                                         | 19.7 ms: 1.09x faster                                                            |
| chaos                      | 50.2 ms                                                         | 46.2 ms: 1.09x faster                                                            |
| python_startup             | 28.3 ms                                                         | 26.1 ms: 1.09x faster                                                            |
| django_template            | 29.8 ms                                                         | 27.5 ms: 1.08x faster                                                            |
| sphinx                     | 719 ms                                                          | 664 ms: 1.08x faster                                                             |
| sympy_sum                  | 106 ms                                                          | 98.0 ms: 1.08x faster                                                            |
| typing_runtime_protocols   | 138 us                                                          | 128 us: 1.07x faster                                                             |
| regex_compile              | 101 ms                                                          | 94.1 ms: 1.07x faster                                                            |
| xml_etree_iterparse        | 62.6 ms                                                         | 58.7 ms: 1.07x faster                                                            |
| sympy_integrate            | 15.0 ms                                                         | 14.1 ms: 1.06x faster                                                            |
| pylint                     | 227 ms                                                          | 214 ms: 1.06x faster                                                             |
| async_generators           | 270 ms                                                          | 262 ms: 1.03x faster                                                             |
| comprehensions             | 12.5 us                                                         | 12.2 us: 1.03x faster                                                            |
| create_gc_cycles           | 1.06 ms                                                         | 1.03 ms: 1.03x faster                                                            |
| pyflate                    | 320 ms                                                          | 312 ms: 1.03x faster                                                             |
| nqueens                    | 72.1 ms                                                         | 70.7 ms: 1.02x faster                                                            |
| python_startup_no_site     | 19.7 ms                                                         | 19.4 ms: 1.01x faster                                                            |
| unpickle_pure_python       | 160 us                                                          | 159 us: 1.01x faster                                                             |
| xml_etree_process          | 44.2 ms                                                         | 44.4 ms: 1.00x slower                                                            |
| regex_dna                  | 114 ms                                                          | 115 ms: 1.01x slower                                                             |
| crypto_pyaes               | 56.9 ms                                                         | 57.7 ms: 1.01x slower                                                            |
| xml_etree_generate         | 61.4 ms                                                         | 62.4 ms: 1.02x slower                                                            |
| richards                   | 32.7 ms                                                         | 33.4 ms: 1.02x slower                                                            |
| scimark_sor                | 85.9 ms                                                         | 88.2 ms: 1.03x slower                                                            |
| logging_silent             | 60.3 ns                                                         | 62.2 ns: 1.03x slower                                                            |
| nbody                      | 80.0 ms                                                         | 82.8 ms: 1.04x slower                                                            |
| deltablue                  | 2.33 ms                                                         | 2.43 ms: 1.04x slower                                                            |
| raytrace                   | 201 ms                                                          | 210 ms: 1.04x slower                                                             |
| hexiom                     | 4.44 ms                                                         | 4.63 ms: 1.04x slower                                                            |
| scimark_monte_carlo        | 47.7 ms                                                         | 50.1 ms: 1.05x slower                                                            |
| generators                 | 21.8 ms                                                         | 22.9 ms: 1.05x slower                                                            |
| spectral_norm              | 69.4 ms                                                         | 73.8 ms: 1.06x slower                                                            |
| scimark_fft                | 205 ms                                                          | 218 ms: 1.06x slower                                                             |
| scimark_lu                 | 60.2 ms                                                         | 64.4 ms: 1.07x slower                                                            |
| many_optionals             | 436 us                                                          | 473 us: 1.08x slower                                                             |
| richards_super             | 36.7 ms                                                         | 40.2 ms: 1.10x slower                                                            |
| scimark_sparse_mat_mult    | 2.84 ms                                                         | 3.12 ms: 1.10x slower                                                            |
| bench_thread_pool          | 1.00 ms                                                         | 1.10 ms: 1.10x slower                                                            |
| meteor_contest             | 74.6 ms                                                         | 85.7 ms: 1.15x slower                                                            |
| pprint_pformat             | 1.33 sec                                                        | 1.69 sec: 1.27x slower                                                           |
| subparsers                 | 14.8 ms                                                         | 19.1 ms: 1.29x slower                                                            |
| mako                       | 7.09 ms                                                         | 9.74 ms: 1.37x slower                                                            |
| tomli_loads                | 1.71 sec                                                        | 2.71 sec: 1.58x slower                                                           |
| bpe_tokeniser              | 3.46 sec                                                        | 5.51 sec: 1.59x slower                                                           |
| docutils                   | 1.78 sec                                                        | 2.88 sec: 1.62x slower                                                           |
| k_core                     | 1.38 sec                                                        | 2.71 sec: 1.97x slower                                                           |
| shortest_path              | 290 ms                                                          | 645 ms: 2.22x slower                                                             |
| connected_components       | 267 ms                                                          | 609 ms: 2.29x slower                                                             |
| Geometric mean             | (ref)                                                           | 1.13x faster                                                                     |

Benchmark hidden because not significant (2): pickle_pure_python, fannkuch
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250705-3.15.0a0-1953713-NOGIL/bm-20250705-pythonperf1_win32-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.127x faster

# HPT report

- Reliability score: 99.57% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown