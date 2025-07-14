# Results vs. 3.13.0

- fork: python
- ref: 47b01da4ccedd9c00fad
- machine: windows-amd64
- commit hash: 47b01da
- commit date: 2025-07-12
- overall geometric mean: 1.132x faster
- HPT reliability: 99.79%
- HPT 99th percentile: 1.01x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250712-pythonperf1_win32-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 250 ms                                                          | 228 ms: 1.10x faster                                                             |
| docutils       | 1.78 sec                                                        | 2.85 sec: 1.60x slower                                                           |
| html5lib       | 47.5 ms                                                         | 40.1 ms: 1.18x faster                                                            |
| sphinx         | 719 ms                                                          | 666 ms: 1.08x faster                                                             |
| Geometric mean | (ref)                                                           | 1.03x slower                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250712-pythonperf1_win32-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| asyncio_websockets         | 363 ms                                                          | 138 ms: 2.63x faster                                                             |
| async_tree_io_tg           | 494 ms                                                          | 328 ms: 1.51x faster                                                             |
| async_tree_io              | 526 ms                                                          | 353 ms: 1.49x faster                                                             |
| async_tree_memoization_tg  | 282 ms                                                          | 191 ms: 1.48x faster                                                             |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 311 ms: 1.46x faster                                                             |
| async_tree_none_tg         | 214 ms                                                          | 147 ms: 1.46x faster                                                             |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 333 ms: 1.46x faster                                                             |
| async_tree_none            | 245 ms                                                          | 169 ms: 1.45x faster                                                             |
| async_tree_memoization     | 297 ms                                                          | 212 ms: 1.40x faster                                                             |
| coroutines                 | 16.2 ms                                                         | 14.0 ms: 1.16x faster                                                            |
| async_generators           | 270 ms                                                          | 264 ms: 1.02x faster                                                             |
| Geometric mean             | (ref)                                                           | 1.46x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250712-pythonperf1_win32-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pidigits       | 201 ms                                                          | 136 ms: 1.48x faster                                                             |
| float          | 54.6 ms                                                         | 46.8 ms: 1.17x faster                                                            |
| nbody          | 80.0 ms                                                         | 84.9 ms: 1.06x slower                                                            |
| Geometric mean | (ref)                                                           | 1.18x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250712-pythonperf1_win32-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_v8       | 16.8 ms                                                         | 12.8 ms: 1.31x faster                                                            |
| regex_effbot   | 1.80 ms                                                         | 1.50 ms: 1.20x faster                                                            |
| regex_compile  | 101 ms                                                          | 95.3 ms: 1.06x faster                                                            |
| regex_dna      | 114 ms                                                          | 112 ms: 1.02x faster                                                             |
| Geometric mean | (ref)                                                           | 1.14x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250712-pythonperf1_win32-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| json_loads           | 21.6 us                                                         | 16.1 us: 1.34x faster                                                            |
| xml_etree_parse      | 107 ms                                                          | 90.0 ms: 1.19x faster                                                            |
| json_dumps           | 7.30 ms                                                         | 6.62 ms: 1.10x faster                                                            |
| xml_etree_iterparse  | 62.6 ms                                                         | 58.4 ms: 1.07x faster                                                            |
| unpickle_pure_python | 160 us                                                          | 154 us: 1.04x faster                                                             |
| pickle_pure_python   | 231 us                                                          | 234 us: 1.01x slower                                                             |
| xml_etree_generate   | 61.4 ms                                                         | 62.6 ms: 1.02x slower                                                            |
| tomli_loads          | 1.71 sec                                                        | 2.64 sec: 1.54x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.02x faster                                                                     |

Benchmark hidden because not significant (1): xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250712-pythonperf1_win32-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup | 28.3 ms                                                         | 26.0 ms: 1.09x faster                                                            |
| Geometric mean | (ref)                                                           | 1.05x faster                                                                     |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250712-pythonperf1_win32-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| genshi_xml      | 50.1 ms                                                         | 39.4 ms: 1.27x faster                                                            |
| genshi_text     | 21.5 ms                                                         | 19.1 ms: 1.12x faster                                                            |
| django_template | 29.8 ms                                                         | 27.3 ms: 1.09x faster                                                            |
| mako            | 7.09 ms                                                         | 9.84 ms: 1.39x slower                                                            |
| Geometric mean  | (ref)                                                           | 1.03x faster                                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250712-pythonperf1_win32-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| thrift                     | 9.98 ms                                                         | 577 us: 17.30x faster                                                            |
| coverage                   | 324 ms                                                          | 68.2 ms: 4.75x faster                                                            |
| pathlib                    | 82.9 ms                                                         | 30.5 ms: 2.72x faster                                                            |
| asyncio_websockets         | 363 ms                                                          | 138 ms: 2.63x faster                                                             |
| deepcopy                   | 314 us                                                          | 200 us: 1.57x faster                                                             |
| async_tree_io_tg           | 494 ms                                                          | 328 ms: 1.51x faster                                                             |
| async_tree_io              | 526 ms                                                          | 353 ms: 1.49x faster                                                             |
| async_tree_memoization_tg  | 282 ms                                                          | 191 ms: 1.48x faster                                                             |
| pidigits                   | 201 ms                                                          | 136 ms: 1.48x faster                                                             |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 311 ms: 1.46x faster                                                             |
| mdp                        | 1.62 sec                                                        | 1.11 sec: 1.46x faster                                                           |
| async_tree_none_tg         | 214 ms                                                          | 147 ms: 1.46x faster                                                             |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 333 ms: 1.46x faster                                                             |
| async_tree_none            | 245 ms                                                          | 169 ms: 1.45x faster                                                             |
| gc_traversal               | 1.75 ms                                                         | 1.21 ms: 1.44x faster                                                            |
| sqlite_synth               | 1.95 us                                                         | 1.36 us: 1.43x faster                                                            |
| async_tree_memoization     | 297 ms                                                          | 212 ms: 1.40x faster                                                             |
| deepcopy_reduce            | 2.92 us                                                         | 2.15 us: 1.36x faster                                                            |
| json_loads                 | 21.6 us                                                         | 16.1 us: 1.34x faster                                                            |
| json                       | 4.27 ms                                                         | 3.19 ms: 1.34x faster                                                            |
| regex_v8                   | 16.8 ms                                                         | 12.8 ms: 1.31x faster                                                            |
| telco                      | 6.96 ms                                                         | 5.43 ms: 1.28x faster                                                            |
| genshi_xml                 | 50.1 ms                                                         | 39.4 ms: 1.27x faster                                                            |
| pycparser                  | 872 ms                                                          | 710 ms: 1.23x faster                                                             |
| logging_format             | 8.72 us                                                         | 7.22 us: 1.21x faster                                                            |
| regex_effbot               | 1.80 ms                                                         | 1.50 ms: 1.20x faster                                                            |
| deepcopy_memo              | 25.4 us                                                         | 21.2 us: 1.20x faster                                                            |
| xml_etree_parse            | 107 ms                                                          | 90.0 ms: 1.19x faster                                                            |
| logging_simple             | 7.99 us                                                         | 6.74 us: 1.18x faster                                                            |
| html5lib                   | 47.5 ms                                                         | 40.1 ms: 1.18x faster                                                            |
| float                      | 54.6 ms                                                         | 46.8 ms: 1.17x faster                                                            |
| go                         | 109 ms                                                          | 93.9 ms: 1.16x faster                                                            |
| coroutines                 | 16.2 ms                                                         | 14.0 ms: 1.16x faster                                                            |
| sympy_expand               | 373 ms                                                          | 323 ms: 1.16x faster                                                             |
| pprint_safe_repr           | 648 ms                                                          | 563 ms: 1.15x faster                                                             |
| dulwich_log                | 48.8 ms                                                         | 42.3 ms: 1.15x faster                                                            |
| bench_mp_pool              | 90.6 ms                                                         | 79.3 ms: 1.14x faster                                                            |
| sympy_str                  | 212 ms                                                          | 187 ms: 1.13x faster                                                             |
| genshi_text                | 21.5 ms                                                         | 19.1 ms: 1.12x faster                                                            |
| json_dumps                 | 7.30 ms                                                         | 6.62 ms: 1.10x faster                                                            |
| 2to3                       | 250 ms                                                          | 228 ms: 1.10x faster                                                             |
| django_template            | 29.8 ms                                                         | 27.3 ms: 1.09x faster                                                            |
| python_startup             | 28.3 ms                                                         | 26.0 ms: 1.09x faster                                                            |
| chaos                      | 50.2 ms                                                         | 46.3 ms: 1.08x faster                                                            |
| sympy_sum                  | 106 ms                                                          | 97.3 ms: 1.08x faster                                                            |
| sphinx                     | 719 ms                                                          | 666 ms: 1.08x faster                                                             |
| xml_etree_iterparse        | 62.6 ms                                                         | 58.4 ms: 1.07x faster                                                            |
| pylint                     | 227 ms                                                          | 212 ms: 1.07x faster                                                             |
| sympy_integrate            | 15.0 ms                                                         | 14.1 ms: 1.06x faster                                                            |
| regex_compile              | 101 ms                                                          | 95.3 ms: 1.06x faster                                                            |
| typing_runtime_protocols   | 138 us                                                          | 130 us: 1.05x faster                                                             |
| comprehensions             | 12.5 us                                                         | 12.0 us: 1.04x faster                                                            |
| unpickle_pure_python       | 160 us                                                          | 154 us: 1.04x faster                                                             |
| create_gc_cycles           | 1.06 ms                                                         | 1.03 ms: 1.03x faster                                                            |
| pyflate                    | 320 ms                                                          | 312 ms: 1.03x faster                                                             |
| async_generators           | 270 ms                                                          | 264 ms: 1.02x faster                                                             |
| regex_dna                  | 114 ms                                                          | 112 ms: 1.02x faster                                                             |
| fannkuch                   | 299 ms                                                          | 296 ms: 1.01x faster                                                             |
| crypto_pyaes               | 56.9 ms                                                         | 56.5 ms: 1.01x faster                                                            |
| pickle_pure_python         | 231 us                                                          | 234 us: 1.01x slower                                                             |
| nqueens                    | 72.1 ms                                                         | 72.9 ms: 1.01x slower                                                            |
| xml_etree_generate         | 61.4 ms                                                         | 62.6 ms: 1.02x slower                                                            |
| logging_silent             | 60.3 ns                                                         | 61.7 ns: 1.02x slower                                                            |
| scimark_monte_carlo        | 47.7 ms                                                         | 49.0 ms: 1.03x slower                                                            |
| richards                   | 32.7 ms                                                         | 33.7 ms: 1.03x slower                                                            |
| generators                 | 21.8 ms                                                         | 22.5 ms: 1.03x slower                                                            |
| scimark_fft                | 205 ms                                                          | 214 ms: 1.04x slower                                                             |
| hexiom                     | 4.44 ms                                                         | 4.65 ms: 1.05x slower                                                            |
| raytrace                   | 201 ms                                                          | 211 ms: 1.05x slower                                                             |
| nbody                      | 80.0 ms                                                         | 84.9 ms: 1.06x slower                                                            |
| spectral_norm              | 69.4 ms                                                         | 73.7 ms: 1.06x slower                                                            |
| deltablue                  | 2.33 ms                                                         | 2.48 ms: 1.06x slower                                                            |
| richards_super             | 36.7 ms                                                         | 39.3 ms: 1.07x slower                                                            |
| bench_thread_pool          | 1.00 ms                                                         | 1.09 ms: 1.08x slower                                                            |
| scimark_sparse_mat_mult    | 2.84 ms                                                         | 3.12 ms: 1.10x slower                                                            |
| many_optionals             | 436 us                                                          | 481 us: 1.10x slower                                                             |
| scimark_lu                 | 60.2 ms                                                         | 68.3 ms: 1.13x slower                                                            |
| meteor_contest             | 74.6 ms                                                         | 86.4 ms: 1.16x slower                                                            |
| pprint_pformat             | 1.33 sec                                                        | 1.68 sec: 1.27x slower                                                           |
| subparsers                 | 14.8 ms                                                         | 19.4 ms: 1.32x slower                                                            |
| mako                       | 7.09 ms                                                         | 9.84 ms: 1.39x slower                                                            |
| tomli_loads                | 1.71 sec                                                        | 2.64 sec: 1.54x slower                                                           |
| bpe_tokeniser              | 3.46 sec                                                        | 5.53 sec: 1.60x slower                                                           |
| docutils                   | 1.78 sec                                                        | 2.85 sec: 1.60x slower                                                           |
| k_core                     | 1.38 sec                                                        | 2.69 sec: 1.95x slower                                                           |
| shortest_path              | 290 ms                                                          | 643 ms: 2.22x slower                                                             |
| connected_components       | 267 ms                                                          | 613 ms: 2.30x slower                                                             |
| Geometric mean             | (ref)                                                           | 1.13x faster                                                                     |

Benchmark hidden because not significant (3): python_startup_no_site, scimark_sor, xml_etree_process
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250712-3.15.0a0-47b01da-NOGIL/bm-20250712-pythonperf1_win32-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.132x faster

# HPT report

- Reliability score: 99.79% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: unknown