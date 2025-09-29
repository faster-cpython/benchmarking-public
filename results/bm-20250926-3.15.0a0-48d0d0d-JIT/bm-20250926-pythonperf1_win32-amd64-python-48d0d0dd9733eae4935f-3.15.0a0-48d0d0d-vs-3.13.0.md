# Results vs. 3.13.0

- fork: python
- ref: 48d0d0dd9733eae4935f
- machine: windows-amd64
- commit hash: 48d0d0d
- commit date: 2025-09-26
- overall geometric mean: 1.323x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.21x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250926-pythonperf1_win32-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 250 ms                                                          | 214 ms: 1.17x faster                                                             |
| docutils       | 1.78 sec                                                        | 1.62 sec: 1.10x faster                                                           |
| html5lib       | 47.5 ms                                                         | 37.3 ms: 1.27x faster                                                            |
| sphinx         | 719 ms                                                          | 631 ms: 1.14x faster                                                             |
| Geometric mean | (ref)                                                           | 1.17x faster                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250926-pythonperf1_win32-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| asyncio_websockets         | 363 ms                                                          | 166 ms: 2.18x faster                                                             |
| async_tree_memoization     | 297 ms                                                          | 201 ms: 1.47x faster                                                             |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 330 ms: 1.47x faster                                                             |
| async_tree_none            | 245 ms                                                          | 170 ms: 1.44x faster                                                             |
| async_tree_io              | 526 ms                                                          | 383 ms: 1.37x faster                                                             |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 334 ms: 1.36x faster                                                             |
| async_tree_memoization_tg  | 282 ms                                                          | 210 ms: 1.34x faster                                                             |
| async_tree_io_tg           | 494 ms                                                          | 378 ms: 1.31x faster                                                             |
| async_tree_none_tg         | 214 ms                                                          | 166 ms: 1.29x faster                                                             |
| async_generators           | 270 ms                                                          | 238 ms: 1.13x faster                                                             |
| coroutines                 | 16.2 ms                                                         | 15.0 ms: 1.09x faster                                                            |
| Geometric mean             | (ref)                                                           | 1.38x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250926-pythonperf1_win32-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| nbody          | 80.0 ms                                                         | 53.8 ms: 1.49x faster                                                            |
| float          | 54.6 ms                                                         | 39.7 ms: 1.38x faster                                                            |
| pidigits       | 201 ms                                                          | 147 ms: 1.37x faster                                                             |
| Geometric mean | (ref)                                                           | 1.41x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250926-pythonperf1_win32-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 101 ms                                                          | 76.8 ms: 1.31x faster                                                            |
| regex_v8       | 16.8 ms                                                         | 14.4 ms: 1.17x faster                                                            |
| regex_effbot   | 1.80 ms                                                         | 1.54 ms: 1.17x faster                                                            |
| regex_dna      | 114 ms                                                          | 118 ms: 1.03x slower                                                             |
| Geometric mean | (ref)                                                           | 1.15x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250926-pythonperf1_win32-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| tomli_loads          | 1.71 sec                                                        | 1.09 sec: 1.57x faster                                                           |
| json_loads           | 21.6 us                                                         | 14.0 us: 1.54x faster                                                            |
| unpickle_pure_python | 160 us                                                          | 104 us: 1.54x faster                                                             |
| json_dumps           | 7.30 ms                                                         | 5.41 ms: 1.35x faster                                                            |
| xml_etree_process    | 44.2 ms                                                         | 34.7 ms: 1.27x faster                                                            |
| xml_etree_parse      | 107 ms                                                          | 86.0 ms: 1.25x faster                                                            |
| xml_etree_generate   | 61.4 ms                                                         | 49.7 ms: 1.23x faster                                                            |
| pickle_pure_python   | 231 us                                                          | 196 us: 1.18x faster                                                             |
| xml_etree_iterparse  | 62.6 ms                                                         | 60.9 ms: 1.03x faster                                                            |
| Geometric mean       | (ref)                                                           | 1.32x faster                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250926-pythonperf1_win32-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup         | 28.3 ms                                                         | 25.2 ms: 1.12x faster                                                            |
| python_startup_no_site | 19.7 ms                                                         | 18.9 ms: 1.04x faster                                                            |
| Geometric mean         | (ref)                                                           | 1.08x faster                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250926-pythonperf1_win32-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| genshi_xml      | 50.1 ms                                                         | 34.2 ms: 1.47x faster                                                            |
| genshi_text     | 21.5 ms                                                         | 15.7 ms: 1.37x faster                                                            |
| mako            | 7.09 ms                                                         | 5.31 ms: 1.34x faster                                                            |
| django_template | 29.8 ms                                                         | 24.0 ms: 1.24x faster                                                            |
| Geometric mean  | (ref)                                                           | 1.35x faster                                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250926-pythonperf1_win32-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| thrift                     | 9.98 ms                                                         | 501 us: 19.90x faster                                                            |
| coverage                   | 324 ms                                                          | 49.0 ms: 6.61x faster                                                            |
| pathlib                    | 82.9 ms                                                         | 29.3 ms: 2.83x faster                                                            |
| asyncio_websockets         | 363 ms                                                          | 166 ms: 2.18x faster                                                             |
| mdp                        | 1.62 sec                                                        | 787 ms: 2.06x faster                                                             |
| deepcopy                   | 314 us                                                          | 163 us: 1.93x faster                                                             |
| telco                      | 6.96 ms                                                         | 3.91 ms: 1.78x faster                                                            |
| deepcopy_reduce            | 2.92 us                                                         | 1.78 us: 1.64x faster                                                            |
| tomli_loads                | 1.71 sec                                                        | 1.09 sec: 1.57x faster                                                           |
| pprint_safe_repr           | 648 ms                                                          | 416 ms: 1.56x faster                                                             |
| pprint_pformat             | 1.33 sec                                                        | 856 ms: 1.55x faster                                                             |
| json_loads                 | 21.6 us                                                         | 14.0 us: 1.54x faster                                                            |
| unpickle_pure_python       | 160 us                                                          | 104 us: 1.54x faster                                                             |
| scimark_fft                | 205 ms                                                          | 135 ms: 1.52x faster                                                             |
| deepcopy_memo              | 25.4 us                                                         | 16.7 us: 1.52x faster                                                            |
| nbody                      | 80.0 ms                                                         | 53.8 ms: 1.49x faster                                                            |
| json                       | 4.27 ms                                                         | 2.89 ms: 1.48x faster                                                            |
| async_tree_memoization     | 297 ms                                                          | 201 ms: 1.47x faster                                                             |
| genshi_xml                 | 50.1 ms                                                         | 34.2 ms: 1.47x faster                                                            |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 330 ms: 1.47x faster                                                             |
| go                         | 109 ms                                                          | 75.5 ms: 1.44x faster                                                            |
| async_tree_none            | 245 ms                                                          | 170 ms: 1.44x faster                                                             |
| fannkuch                   | 299 ms                                                          | 209 ms: 1.43x faster                                                             |
| bpe_tokeniser              | 3.46 sec                                                        | 2.48 sec: 1.39x faster                                                           |
| float                      | 54.6 ms                                                         | 39.7 ms: 1.38x faster                                                            |
| async_tree_io              | 526 ms                                                          | 383 ms: 1.37x faster                                                             |
| pidigits                   | 201 ms                                                          | 147 ms: 1.37x faster                                                             |
| genshi_text                | 21.5 ms                                                         | 15.7 ms: 1.37x faster                                                            |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 334 ms: 1.36x faster                                                             |
| logging_format             | 8.72 us                                                         | 6.43 us: 1.35x faster                                                            |
| json_dumps                 | 7.30 ms                                                         | 5.41 ms: 1.35x faster                                                            |
| typing_runtime_protocols   | 138 us                                                          | 102 us: 1.35x faster                                                             |
| logging_simple             | 7.99 us                                                         | 5.94 us: 1.34x faster                                                            |
| async_tree_memoization_tg  | 282 ms                                                          | 210 ms: 1.34x faster                                                             |
| mako                       | 7.09 ms                                                         | 5.31 ms: 1.34x faster                                                            |
| regex_compile              | 101 ms                                                          | 76.8 ms: 1.31x faster                                                            |
| scimark_sparse_mat_mult    | 2.84 ms                                                         | 2.16 ms: 1.31x faster                                                            |
| async_tree_io_tg           | 494 ms                                                          | 378 ms: 1.31x faster                                                             |
| sympy_expand               | 373 ms                                                          | 288 ms: 1.30x faster                                                             |
| pyflate                    | 320 ms                                                          | 247 ms: 1.30x faster                                                             |
| async_tree_none_tg         | 214 ms                                                          | 166 ms: 1.29x faster                                                             |
| sqlite_synth               | 1.95 us                                                         | 1.52 us: 1.28x faster                                                            |
| sympy_str                  | 212 ms                                                          | 166 ms: 1.28x faster                                                             |
| pycparser                  | 872 ms                                                          | 683 ms: 1.28x faster                                                             |
| html5lib                   | 47.5 ms                                                         | 37.3 ms: 1.27x faster                                                            |
| xml_etree_process          | 44.2 ms                                                         | 34.7 ms: 1.27x faster                                                            |
| crypto_pyaes               | 56.9 ms                                                         | 44.8 ms: 1.27x faster                                                            |
| chaos                      | 50.2 ms                                                         | 40.0 ms: 1.26x faster                                                            |
| dulwich_log                | 48.8 ms                                                         | 38.9 ms: 1.25x faster                                                            |
| xml_etree_parse            | 107 ms                                                          | 86.0 ms: 1.25x faster                                                            |
| sympy_sum                  | 106 ms                                                          | 84.7 ms: 1.25x faster                                                            |
| django_template            | 29.8 ms                                                         | 24.0 ms: 1.24x faster                                                            |
| xml_etree_generate         | 61.4 ms                                                         | 49.7 ms: 1.23x faster                                                            |
| richards                   | 32.7 ms                                                         | 26.8 ms: 1.22x faster                                                            |
| sympy_integrate            | 15.0 ms                                                         | 12.3 ms: 1.22x faster                                                            |
| nqueens                    | 72.1 ms                                                         | 59.5 ms: 1.21x faster                                                            |
| richards_super             | 36.7 ms                                                         | 30.3 ms: 1.21x faster                                                            |
| bench_thread_pool          | 1.00 ms                                                         | 840 us: 1.19x faster                                                             |
| scimark_monte_carlo        | 47.7 ms                                                         | 40.0 ms: 1.19x faster                                                            |
| pickle_pure_python         | 231 us                                                          | 196 us: 1.18x faster                                                             |
| pylint                     | 227 ms                                                          | 193 ms: 1.18x faster                                                             |
| 2to3                       | 250 ms                                                          | 214 ms: 1.17x faster                                                             |
| regex_v8                   | 16.8 ms                                                         | 14.4 ms: 1.17x faster                                                            |
| regex_effbot               | 1.80 ms                                                         | 1.54 ms: 1.17x faster                                                            |
| comprehensions             | 12.5 us                                                         | 10.7 us: 1.16x faster                                                            |
| raytrace                   | 201 ms                                                          | 173 ms: 1.16x faster                                                             |
| sphinx                     | 719 ms                                                          | 631 ms: 1.14x faster                                                             |
| generators                 | 21.8 ms                                                         | 19.2 ms: 1.13x faster                                                            |
| async_generators           | 270 ms                                                          | 238 ms: 1.13x faster                                                             |
| hexiom                     | 4.44 ms                                                         | 3.93 ms: 1.13x faster                                                            |
| python_startup             | 28.3 ms                                                         | 25.2 ms: 1.12x faster                                                            |
| logging_silent             | 60.3 ns                                                         | 54.3 ns: 1.11x faster                                                            |
| docutils                   | 1.78 sec                                                        | 1.62 sec: 1.10x faster                                                           |
| scimark_sor                | 85.9 ms                                                         | 78.6 ms: 1.09x faster                                                            |
| deltablue                  | 2.33 ms                                                         | 2.14 ms: 1.09x faster                                                            |
| coroutines                 | 16.2 ms                                                         | 15.0 ms: 1.09x faster                                                            |
| spectral_norm              | 69.4 ms                                                         | 65.8 ms: 1.05x faster                                                            |
| python_startup_no_site     | 19.7 ms                                                         | 18.9 ms: 1.04x faster                                                            |
| meteor_contest             | 74.6 ms                                                         | 72.5 ms: 1.03x faster                                                            |
| scimark_lu                 | 60.2 ms                                                         | 58.6 ms: 1.03x faster                                                            |
| xml_etree_iterparse        | 62.6 ms                                                         | 60.9 ms: 1.03x faster                                                            |
| bench_mp_pool              | 90.6 ms                                                         | 89.3 ms: 1.01x faster                                                            |
| regex_dna                  | 114 ms                                                          | 118 ms: 1.03x slower                                                             |
| k_core                     | 1.38 sec                                                        | 1.59 sec: 1.15x slower                                                           |
| connected_components       | 267 ms                                                          | 317 ms: 1.19x slower                                                             |
| shortest_path              | 290 ms                                                          | 347 ms: 1.20x slower                                                             |
| gc_traversal               | 1.75 ms                                                         | 2.10 ms: 1.20x slower                                                            |
| create_gc_cycles           | 1.06 ms                                                         | 1.27 ms: 1.20x slower                                                            |
| many_optionals             | 436 us                                                          | 567 us: 1.30x slower                                                             |
| subparsers                 | 14.8 ms                                                         | 30.2 ms: 2.05x slower                                                            |
| Geometric mean             | (ref)                                                           | 1.32x faster                                                                     |
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250926-3.15.0a0-48d0d0d-JIT/bm-20250926-pythonperf1_win32-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.323x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.25x
- 95% likely to have a speedup of 1.24x
- 99% likely to have a speedup of 1.21x

# Memory
- memory change: unknown