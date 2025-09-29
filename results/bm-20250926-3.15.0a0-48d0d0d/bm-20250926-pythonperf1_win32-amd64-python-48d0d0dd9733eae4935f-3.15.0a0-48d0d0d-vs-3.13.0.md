# Results vs. 3.13.0

- fork: python
- ref: 48d0d0dd9733eae4935f
- machine: windows-amd64
- commit hash: 48d0d0d
- commit date: 2025-09-26
- overall geometric mean: 1.256x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.15x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250926-pythonperf1_win32-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 250 ms                                                          | 214 ms: 1.17x faster                                                             |
| docutils       | 1.78 sec                                                        | 1.62 sec: 1.10x faster                                                           |
| html5lib       | 47.5 ms                                                         | 38.7 ms: 1.23x faster                                                            |
| sphinx         | 719 ms                                                          | 632 ms: 1.14x faster                                                             |
| Geometric mean | (ref)                                                           | 1.16x faster                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250926-pythonperf1_win32-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| asyncio_websockets         | 363 ms                                                          | 167 ms: 2.18x faster                                                             |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 326 ms: 1.48x faster                                                             |
| async_tree_memoization     | 297 ms                                                          | 204 ms: 1.46x faster                                                             |
| async_tree_none            | 245 ms                                                          | 173 ms: 1.41x faster                                                             |
| async_tree_io              | 526 ms                                                          | 381 ms: 1.38x faster                                                             |
| async_tree_memoization_tg  | 282 ms                                                          | 206 ms: 1.37x faster                                                             |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 336 ms: 1.36x faster                                                             |
| async_tree_io_tg           | 494 ms                                                          | 384 ms: 1.29x faster                                                             |
| async_tree_none_tg         | 214 ms                                                          | 168 ms: 1.27x faster                                                             |
| async_generators           | 270 ms                                                          | 230 ms: 1.17x faster                                                             |
| coroutines                 | 16.2 ms                                                         | 14.5 ms: 1.12x faster                                                            |
| Geometric mean             | (ref)                                                           | 1.39x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250926-pythonperf1_win32-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pidigits       | 201 ms                                                          | 151 ms: 1.33x faster                                                             |
| float          | 54.6 ms                                                         | 44.7 ms: 1.22x faster                                                            |
| nbody          | 80.0 ms                                                         | 68.5 ms: 1.17x faster                                                            |
| Geometric mean | (ref)                                                           | 1.24x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250926-pythonperf1_win32-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 101 ms                                                          | 81.4 ms: 1.24x faster                                                            |
| regex_v8       | 16.8 ms                                                         | 14.3 ms: 1.17x faster                                                            |
| regex_effbot   | 1.80 ms                                                         | 1.55 ms: 1.16x faster                                                            |
| regex_dna      | 114 ms                                                          | 121 ms: 1.06x slower                                                             |
| Geometric mean | (ref)                                                           | 1.12x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250926-pythonperf1_win32-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| json_loads           | 21.6 us                                                         | 14.4 us: 1.50x faster                                                            |
| json_dumps           | 7.30 ms                                                         | 5.41 ms: 1.35x faster                                                            |
| tomli_loads          | 1.71 sec                                                        | 1.41 sec: 1.22x faster                                                           |
| xml_etree_parse      | 107 ms                                                          | 90.2 ms: 1.19x faster                                                            |
| unpickle_pure_python | 160 us                                                          | 138 us: 1.16x faster                                                             |
| xml_etree_process    | 44.2 ms                                                         | 39.5 ms: 1.12x faster                                                            |
| xml_etree_generate   | 61.4 ms                                                         | 56.8 ms: 1.08x faster                                                            |
| pickle_pure_python   | 231 us                                                          | 218 us: 1.06x faster                                                             |
| xml_etree_iterparse  | 62.6 ms                                                         | 64.9 ms: 1.04x slower                                                            |
| Geometric mean       | (ref)                                                           | 1.17x faster                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250926-pythonperf1_win32-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup         | 28.3 ms                                                         | 25.4 ms: 1.11x faster                                                            |
| python_startup_no_site | 19.7 ms                                                         | 19.0 ms: 1.04x faster                                                            |
| Geometric mean         | (ref)                                                           | 1.07x faster                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250926-pythonperf1_win32-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| genshi_xml      | 50.1 ms                                                         | 34.5 ms: 1.45x faster                                                            |
| genshi_text     | 21.5 ms                                                         | 15.7 ms: 1.37x faster                                                            |
| django_template | 29.8 ms                                                         | 24.7 ms: 1.21x faster                                                            |
| mako            | 7.09 ms                                                         | 6.89 ms: 1.03x faster                                                            |
| Geometric mean  | (ref)                                                           | 1.25x faster                                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250926-pythonperf1_win32-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| thrift                     | 9.98 ms                                                         | 501 us: 19.90x faster                                                            |
| coverage                   | 324 ms                                                          | 49.3 ms: 6.56x faster                                                            |
| pathlib                    | 82.9 ms                                                         | 29.7 ms: 2.79x faster                                                            |
| asyncio_websockets         | 363 ms                                                          | 167 ms: 2.18x faster                                                             |
| mdp                        | 1.62 sec                                                        | 814 ms: 2.00x faster                                                             |
| deepcopy                   | 314 us                                                          | 167 us: 1.87x faster                                                             |
| telco                      | 6.96 ms                                                         | 4.29 ms: 1.62x faster                                                            |
| deepcopy_reduce            | 2.92 us                                                         | 1.81 us: 1.61x faster                                                            |
| json_loads                 | 21.6 us                                                         | 14.4 us: 1.50x faster                                                            |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 326 ms: 1.48x faster                                                             |
| json                       | 4.27 ms                                                         | 2.92 ms: 1.46x faster                                                            |
| async_tree_memoization     | 297 ms                                                          | 204 ms: 1.46x faster                                                             |
| genshi_xml                 | 50.1 ms                                                         | 34.5 ms: 1.45x faster                                                            |
| deepcopy_memo              | 25.4 us                                                         | 17.5 us: 1.45x faster                                                            |
| async_tree_none            | 245 ms                                                          | 173 ms: 1.41x faster                                                             |
| go                         | 109 ms                                                          | 78.8 ms: 1.38x faster                                                            |
| async_tree_io              | 526 ms                                                          | 381 ms: 1.38x faster                                                             |
| genshi_text                | 21.5 ms                                                         | 15.7 ms: 1.37x faster                                                            |
| async_tree_memoization_tg  | 282 ms                                                          | 206 ms: 1.37x faster                                                             |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 336 ms: 1.36x faster                                                             |
| logging_format             | 8.72 us                                                         | 6.45 us: 1.35x faster                                                            |
| json_dumps                 | 7.30 ms                                                         | 5.41 ms: 1.35x faster                                                            |
| logging_simple             | 7.99 us                                                         | 5.99 us: 1.33x faster                                                            |
| pidigits                   | 201 ms                                                          | 151 ms: 1.33x faster                                                             |
| sympy_expand               | 373 ms                                                          | 286 ms: 1.31x faster                                                             |
| typing_runtime_protocols   | 138 us                                                          | 106 us: 1.30x faster                                                             |
| pprint_pformat             | 1.33 sec                                                        | 1.02 sec: 1.30x faster                                                           |
| pprint_safe_repr           | 648 ms                                                          | 501 ms: 1.29x faster                                                             |
| async_tree_io_tg           | 494 ms                                                          | 384 ms: 1.29x faster                                                             |
| async_tree_none_tg         | 214 ms                                                          | 168 ms: 1.27x faster                                                             |
| sympy_str                  | 212 ms                                                          | 168 ms: 1.26x faster                                                             |
| pycparser                  | 872 ms                                                          | 702 ms: 1.24x faster                                                             |
| regex_compile              | 101 ms                                                          | 81.4 ms: 1.24x faster                                                            |
| dulwich_log                | 48.8 ms                                                         | 39.6 ms: 1.23x faster                                                            |
| sqlite_synth               | 1.95 us                                                         | 1.59 us: 1.23x faster                                                            |
| html5lib                   | 47.5 ms                                                         | 38.7 ms: 1.23x faster                                                            |
| float                      | 54.6 ms                                                         | 44.7 ms: 1.22x faster                                                            |
| tomli_loads                | 1.71 sec                                                        | 1.41 sec: 1.22x faster                                                           |
| sympy_sum                  | 106 ms                                                          | 87.4 ms: 1.21x faster                                                            |
| django_template            | 29.8 ms                                                         | 24.7 ms: 1.21x faster                                                            |
| chaos                      | 50.2 ms                                                         | 41.8 ms: 1.20x faster                                                            |
| crypto_pyaes               | 56.9 ms                                                         | 47.8 ms: 1.19x faster                                                            |
| xml_etree_parse            | 107 ms                                                          | 90.2 ms: 1.19x faster                                                            |
| sympy_integrate            | 15.0 ms                                                         | 12.6 ms: 1.19x faster                                                            |
| bench_thread_pool          | 1.00 ms                                                         | 852 us: 1.18x faster                                                             |
| regex_v8                   | 16.8 ms                                                         | 14.3 ms: 1.17x faster                                                            |
| async_generators           | 270 ms                                                          | 230 ms: 1.17x faster                                                             |
| richards_super             | 36.7 ms                                                         | 31.3 ms: 1.17x faster                                                            |
| richards                   | 32.7 ms                                                         | 27.9 ms: 1.17x faster                                                            |
| 2to3                       | 250 ms                                                          | 214 ms: 1.17x faster                                                             |
| nbody                      | 80.0 ms                                                         | 68.5 ms: 1.17x faster                                                            |
| unpickle_pure_python       | 160 us                                                          | 138 us: 1.16x faster                                                             |
| regex_effbot               | 1.80 ms                                                         | 1.55 ms: 1.16x faster                                                            |
| scimark_monte_carlo        | 47.7 ms                                                         | 41.2 ms: 1.16x faster                                                            |
| bpe_tokeniser              | 3.46 sec                                                        | 2.99 sec: 1.16x faster                                                           |
| scimark_fft                | 205 ms                                                          | 177 ms: 1.16x faster                                                             |
| pylint                     | 227 ms                                                          | 197 ms: 1.15x faster                                                             |
| nqueens                    | 72.1 ms                                                         | 63.0 ms: 1.14x faster                                                            |
| sphinx                     | 719 ms                                                          | 632 ms: 1.14x faster                                                             |
| scimark_sparse_mat_mult    | 2.84 ms                                                         | 2.53 ms: 1.12x faster                                                            |
| xml_etree_process          | 44.2 ms                                                         | 39.5 ms: 1.12x faster                                                            |
| raytrace                   | 201 ms                                                          | 180 ms: 1.12x faster                                                             |
| fannkuch                   | 299 ms                                                          | 268 ms: 1.12x faster                                                             |
| coroutines                 | 16.2 ms                                                         | 14.5 ms: 1.12x faster                                                            |
| python_startup             | 28.3 ms                                                         | 25.4 ms: 1.11x faster                                                            |
| generators                 | 21.8 ms                                                         | 19.7 ms: 1.11x faster                                                            |
| pyflate                    | 320 ms                                                          | 290 ms: 1.10x faster                                                             |
| comprehensions             | 12.5 us                                                         | 11.3 us: 1.10x faster                                                            |
| docutils                   | 1.78 sec                                                        | 1.62 sec: 1.10x faster                                                           |
| scimark_sor                | 85.9 ms                                                         | 78.5 ms: 1.09x faster                                                            |
| xml_etree_generate         | 61.4 ms                                                         | 56.8 ms: 1.08x faster                                                            |
| hexiom                     | 4.44 ms                                                         | 4.14 ms: 1.07x faster                                                            |
| pickle_pure_python         | 231 us                                                          | 218 us: 1.06x faster                                                             |
| deltablue                  | 2.33 ms                                                         | 2.23 ms: 1.04x faster                                                            |
| python_startup_no_site     | 19.7 ms                                                         | 19.0 ms: 1.04x faster                                                            |
| spectral_norm              | 69.4 ms                                                         | 67.1 ms: 1.03x faster                                                            |
| logging_silent             | 60.3 ns                                                         | 58.4 ns: 1.03x faster                                                            |
| mako                       | 7.09 ms                                                         | 6.89 ms: 1.03x faster                                                            |
| meteor_contest             | 74.6 ms                                                         | 73.9 ms: 1.01x faster                                                            |
| xml_etree_iterparse        | 62.6 ms                                                         | 64.9 ms: 1.04x slower                                                            |
| regex_dna                  | 114 ms                                                          | 121 ms: 1.06x slower                                                             |
| gc_traversal               | 1.75 ms                                                         | 2.10 ms: 1.20x slower                                                            |
| create_gc_cycles           | 1.06 ms                                                         | 1.28 ms: 1.21x slower                                                            |
| k_core                     | 1.38 sec                                                        | 1.69 sec: 1.23x slower                                                           |
| connected_components       | 267 ms                                                          | 333 ms: 1.25x slower                                                             |
| shortest_path              | 290 ms                                                          | 363 ms: 1.25x slower                                                             |
| many_optionals             | 436 us                                                          | 562 us: 1.29x slower                                                             |
| subparsers                 | 14.8 ms                                                         | 30.4 ms: 2.06x slower                                                            |
| Geometric mean             | (ref)                                                           | 1.25x faster                                                                     |

Benchmark hidden because not significant (2): bench_mp_pool, scimark_lu
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250926-3.15.0a0-48d0d0d/bm-20250926-pythonperf1_win32-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.256x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.16x
- 95% likely to have a speedup of 1.16x
- 99% likely to have a speedup of 1.15x

# Memory
- memory change: unknown