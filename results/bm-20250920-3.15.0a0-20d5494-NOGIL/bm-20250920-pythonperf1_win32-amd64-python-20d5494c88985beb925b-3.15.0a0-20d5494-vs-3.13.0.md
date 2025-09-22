# Results vs. 3.13.0

- fork: python
- ref: 20d5494c88985beb925b
- machine: windows-amd64
- commit hash: 20d5494
- commit date: 2025-09-20
- overall geometric mean: 1.118x faster
- HPT reliability: 99.00%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250920-pythonperf1_win32-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 250 ms                                                          | 228 ms: 1.10x faster                                                             |
| docutils       | 1.78 sec                                                        | 2.90 sec: 1.63x slower                                                           |
| html5lib       | 47.5 ms                                                         | 40.7 ms: 1.17x faster                                                            |
| sphinx         | 719 ms                                                          | 668 ms: 1.08x faster                                                             |
| Geometric mean | (ref)                                                           | 1.04x slower                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250920-pythonperf1_win32-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494 |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| asyncio_websockets         | 363 ms                                                          | 144 ms: 2.53x faster                                                             |
| async_tree_io_tg           | 494 ms                                                          | 334 ms: 1.48x faster                                                             |
| async_tree_memoization_tg  | 282 ms                                                          | 192 ms: 1.47x faster                                                             |
| async_tree_io              | 526 ms                                                          | 359 ms: 1.46x faster                                                             |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 312 ms: 1.46x faster                                                             |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 333 ms: 1.45x faster                                                             |
| async_tree_none_tg         | 214 ms                                                          | 149 ms: 1.43x faster                                                             |
| async_tree_none            | 245 ms                                                          | 172 ms: 1.42x faster                                                             |
| async_tree_memoization     | 297 ms                                                          | 214 ms: 1.38x faster                                                             |
| coroutines                 | 16.2 ms                                                         | 15.1 ms: 1.07x faster                                                            |
| async_generators           | 270 ms                                                          | 264 ms: 1.02x faster                                                             |
| Geometric mean             | (ref)                                                           | 1.43x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250920-pythonperf1_win32-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pidigits       | 201 ms                                                          | 136 ms: 1.47x faster                                                             |
| float          | 54.6 ms                                                         | 46.5 ms: 1.17x faster                                                            |
| nbody          | 80.0 ms                                                         | 82.1 ms: 1.03x slower                                                            |
| Geometric mean | (ref)                                                           | 1.19x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250920-pythonperf1_win32-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_v8       | 16.8 ms                                                         | 13.4 ms: 1.25x faster                                                            |
| regex_effbot   | 1.80 ms                                                         | 1.65 ms: 1.09x faster                                                            |
| regex_compile  | 101 ms                                                          | 93.9 ms: 1.08x faster                                                            |
| regex_dna      | 114 ms                                                          | 112 ms: 1.01x faster                                                             |
| Geometric mean | (ref)                                                           | 1.10x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250920-pythonperf1_win32-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494 |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| json_loads           | 21.6 us                                                         | 15.9 us: 1.36x faster                                                            |
| xml_etree_parse      | 107 ms                                                          | 91.3 ms: 1.18x faster                                                            |
| json_dumps           | 7.30 ms                                                         | 6.28 ms: 1.16x faster                                                            |
| unpickle_pure_python | 160 us                                                          | 158 us: 1.02x faster                                                             |
| xml_etree_iterparse  | 62.6 ms                                                         | 61.7 ms: 1.01x faster                                                            |
| pickle_pure_python   | 231 us                                                          | 236 us: 1.02x slower                                                             |
| xml_etree_process    | 44.2 ms                                                         | 45.9 ms: 1.04x slower                                                            |
| xml_etree_generate   | 61.4 ms                                                         | 64.0 ms: 1.04x slower                                                            |
| tomli_loads          | 1.71 sec                                                        | 2.41 sec: 1.41x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.02x faster                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250920-pythonperf1_win32-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494 |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup         | 28.3 ms                                                         | 25.8 ms: 1.10x faster                                                            |
| python_startup_no_site | 19.7 ms                                                         | 19.2 ms: 1.02x faster                                                            |
| Geometric mean         | (ref)                                                           | 1.06x faster                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250920-pythonperf1_win32-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494 |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| genshi_xml      | 50.1 ms                                                         | 40.4 ms: 1.24x faster                                                            |
| django_template | 29.8 ms                                                         | 27.2 ms: 1.09x faster                                                            |
| genshi_text     | 21.5 ms                                                         | 19.9 ms: 1.08x faster                                                            |
| mako            | 7.09 ms                                                         | 10.1 ms: 1.42x slower                                                            |
| Geometric mean  | (ref)                                                           | 1.01x faster                                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250920-pythonperf1_win32-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494 |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| thrift                     | 9.98 ms                                                         | 579 us: 17.24x faster                                                            |
| coverage                   | 324 ms                                                          | 70.4 ms: 4.60x faster                                                            |
| pathlib                    | 82.9 ms                                                         | 29.7 ms: 2.79x faster                                                            |
| asyncio_websockets         | 363 ms                                                          | 144 ms: 2.53x faster                                                             |
| deepcopy                   | 314 us                                                          | 190 us: 1.65x faster                                                             |
| gc_traversal               | 1.75 ms                                                         | 1.16 ms: 1.51x faster                                                            |
| async_tree_io_tg           | 494 ms                                                          | 334 ms: 1.48x faster                                                             |
| pidigits                   | 201 ms                                                          | 136 ms: 1.47x faster                                                             |
| async_tree_memoization_tg  | 282 ms                                                          | 192 ms: 1.47x faster                                                             |
| async_tree_io              | 526 ms                                                          | 359 ms: 1.46x faster                                                             |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 312 ms: 1.46x faster                                                             |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 333 ms: 1.45x faster                                                             |
| sqlite_synth               | 1.95 us                                                         | 1.36 us: 1.44x faster                                                            |
| async_tree_none_tg         | 214 ms                                                          | 149 ms: 1.43x faster                                                             |
| mdp                        | 1.62 sec                                                        | 1.13 sec: 1.43x faster                                                           |
| async_tree_none            | 245 ms                                                          | 172 ms: 1.42x faster                                                             |
| deepcopy_reduce            | 2.92 us                                                         | 2.08 us: 1.40x faster                                                            |
| async_tree_memoization     | 297 ms                                                          | 214 ms: 1.38x faster                                                             |
| telco                      | 6.96 ms                                                         | 5.03 ms: 1.38x faster                                                            |
| json                       | 4.27 ms                                                         | 3.13 ms: 1.37x faster                                                            |
| json_loads                 | 21.6 us                                                         | 15.9 us: 1.36x faster                                                            |
| deepcopy_memo              | 25.4 us                                                         | 19.4 us: 1.31x faster                                                            |
| regex_v8                   | 16.8 ms                                                         | 13.4 ms: 1.25x faster                                                            |
| genshi_xml                 | 50.1 ms                                                         | 40.4 ms: 1.24x faster                                                            |
| bench_mp_pool              | 90.6 ms                                                         | 75.1 ms: 1.21x faster                                                            |
| logging_format             | 8.72 us                                                         | 7.27 us: 1.20x faster                                                            |
| go                         | 109 ms                                                          | 91.2 ms: 1.19x faster                                                            |
| logging_simple             | 7.99 us                                                         | 6.78 us: 1.18x faster                                                            |
| pycparser                  | 872 ms                                                          | 741 ms: 1.18x faster                                                             |
| xml_etree_parse            | 107 ms                                                          | 91.3 ms: 1.18x faster                                                            |
| float                      | 54.6 ms                                                         | 46.5 ms: 1.17x faster                                                            |
| html5lib                   | 47.5 ms                                                         | 40.7 ms: 1.17x faster                                                            |
| json_dumps                 | 7.30 ms                                                         | 6.28 ms: 1.16x faster                                                            |
| pprint_safe_repr           | 648 ms                                                          | 558 ms: 1.16x faster                                                             |
| dulwich_log                | 48.8 ms                                                         | 42.2 ms: 1.16x faster                                                            |
| sympy_expand               | 373 ms                                                          | 324 ms: 1.15x faster                                                             |
| pylint                     | 227 ms                                                          | 202 ms: 1.12x faster                                                             |
| sympy_str                  | 212 ms                                                          | 189 ms: 1.12x faster                                                             |
| 2to3                       | 250 ms                                                          | 228 ms: 1.10x faster                                                             |
| python_startup             | 28.3 ms                                                         | 25.8 ms: 1.10x faster                                                            |
| django_template            | 29.8 ms                                                         | 27.2 ms: 1.09x faster                                                            |
| regex_effbot               | 1.80 ms                                                         | 1.65 ms: 1.09x faster                                                            |
| sympy_sum                  | 106 ms                                                          | 97.2 ms: 1.09x faster                                                            |
| chaos                      | 50.2 ms                                                         | 46.4 ms: 1.08x faster                                                            |
| genshi_text                | 21.5 ms                                                         | 19.9 ms: 1.08x faster                                                            |
| sphinx                     | 719 ms                                                          | 668 ms: 1.08x faster                                                             |
| regex_compile              | 101 ms                                                          | 93.9 ms: 1.08x faster                                                            |
| coroutines                 | 16.2 ms                                                         | 15.1 ms: 1.07x faster                                                            |
| sympy_integrate            | 15.0 ms                                                         | 14.3 ms: 1.05x faster                                                            |
| comprehensions             | 12.5 us                                                         | 12.0 us: 1.04x faster                                                            |
| typing_runtime_protocols   | 138 us                                                          | 132 us: 1.04x faster                                                             |
| create_gc_cycles           | 1.06 ms                                                         | 1.02 ms: 1.04x faster                                                            |
| pyflate                    | 320 ms                                                          | 311 ms: 1.03x faster                                                             |
| python_startup_no_site     | 19.7 ms                                                         | 19.2 ms: 1.02x faster                                                            |
| async_generators           | 270 ms                                                          | 264 ms: 1.02x faster                                                             |
| unpickle_pure_python       | 160 us                                                          | 158 us: 1.02x faster                                                             |
| regex_dna                  | 114 ms                                                          | 112 ms: 1.01x faster                                                             |
| xml_etree_iterparse        | 62.6 ms                                                         | 61.7 ms: 1.01x faster                                                            |
| crypto_pyaes               | 56.9 ms                                                         | 56.6 ms: 1.01x faster                                                            |
| nqueens                    | 72.1 ms                                                         | 73.0 ms: 1.01x slower                                                            |
| pickle_pure_python         | 231 us                                                          | 236 us: 1.02x slower                                                             |
| scimark_sor                | 85.9 ms                                                         | 88.0 ms: 1.02x slower                                                            |
| logging_silent             | 60.3 ns                                                         | 61.9 ns: 1.03x slower                                                            |
| nbody                      | 80.0 ms                                                         | 82.1 ms: 1.03x slower                                                            |
| fannkuch                   | 299 ms                                                          | 310 ms: 1.04x slower                                                             |
| xml_etree_process          | 44.2 ms                                                         | 45.9 ms: 1.04x slower                                                            |
| scimark_monte_carlo        | 47.7 ms                                                         | 49.6 ms: 1.04x slower                                                            |
| scimark_fft                | 205 ms                                                          | 213 ms: 1.04x slower                                                             |
| scimark_lu                 | 60.2 ms                                                         | 62.8 ms: 1.04x slower                                                            |
| hexiom                     | 4.44 ms                                                         | 4.63 ms: 1.04x slower                                                            |
| xml_etree_generate         | 61.4 ms                                                         | 64.0 ms: 1.04x slower                                                            |
| richards                   | 32.7 ms                                                         | 34.1 ms: 1.04x slower                                                            |
| raytrace                   | 201 ms                                                          | 213 ms: 1.06x slower                                                             |
| deltablue                  | 2.33 ms                                                         | 2.49 ms: 1.07x slower                                                            |
| richards_super             | 36.7 ms                                                         | 39.8 ms: 1.08x slower                                                            |
| generators                 | 21.8 ms                                                         | 23.6 ms: 1.09x slower                                                            |
| spectral_norm              | 69.4 ms                                                         | 75.5 ms: 1.09x slower                                                            |
| bench_thread_pool          | 1.00 ms                                                         | 1.11 ms: 1.11x slower                                                            |
| scimark_sparse_mat_mult    | 2.84 ms                                                         | 3.16 ms: 1.11x slower                                                            |
| meteor_contest             | 74.6 ms                                                         | 85.6 ms: 1.15x slower                                                            |
| pprint_pformat             | 1.33 sec                                                        | 1.69 sec: 1.27x slower                                                           |
| tomli_loads                | 1.71 sec                                                        | 2.41 sec: 1.41x slower                                                           |
| mako                       | 7.09 ms                                                         | 10.1 ms: 1.42x slower                                                            |
| many_optionals             | 436 us                                                          | 633 us: 1.45x slower                                                             |
| bpe_tokeniser              | 3.46 sec                                                        | 5.54 sec: 1.60x slower                                                           |
| docutils                   | 1.78 sec                                                        | 2.90 sec: 1.63x slower                                                           |
| k_core                     | 1.38 sec                                                        | 2.68 sec: 1.94x slower                                                           |
| shortest_path              | 290 ms                                                          | 651 ms: 2.25x slower                                                             |
| connected_components       | 267 ms                                                          | 621 ms: 2.33x slower                                                             |
| subparsers                 | 14.8 ms                                                         | 35.8 ms: 2.43x slower                                                            |
| Geometric mean             | (ref)                                                           | 1.12x faster                                                                     |
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250920-3.15.0a0-20d5494-NOGIL/bm-20250920-pythonperf1_win32-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.118x faster

# HPT report

- Reliability score: 99.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown