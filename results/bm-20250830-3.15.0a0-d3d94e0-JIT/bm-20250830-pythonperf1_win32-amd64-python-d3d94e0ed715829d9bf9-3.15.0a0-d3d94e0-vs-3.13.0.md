# Results vs. 3.13.0

- fork: python
- ref: d3d94e0ed715829d9bf9
- machine: windows-amd64
- commit hash: d3d94e0
- commit date: 2025-08-30
- overall geometric mean: 1.315x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.21x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250830-pythonperf1_win32-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 250 ms                                                          | 217 ms: 1.16x faster                                                             |
| docutils       | 1.78 sec                                                        | 1.61 sec: 1.10x faster                                                           |
| html5lib       | 47.5 ms                                                         | 38.0 ms: 1.25x faster                                                            |
| sphinx         | 719 ms                                                          | 624 ms: 1.15x faster                                                             |
| Geometric mean | (ref)                                                           | 1.16x faster                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250830-pythonperf1_win32-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| asyncio_websockets         | 363 ms                                                          | 159 ms: 2.28x faster                                                             |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 330 ms: 1.47x faster                                                             |
| async_tree_none            | 245 ms                                                          | 169 ms: 1.45x faster                                                             |
| async_tree_memoization     | 297 ms                                                          | 206 ms: 1.44x faster                                                             |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 333 ms: 1.37x faster                                                             |
| async_tree_io              | 526 ms                                                          | 386 ms: 1.36x faster                                                             |
| async_tree_memoization_tg  | 282 ms                                                          | 210 ms: 1.35x faster                                                             |
| async_tree_none_tg         | 214 ms                                                          | 167 ms: 1.29x faster                                                             |
| async_tree_io_tg           | 494 ms                                                          | 389 ms: 1.27x faster                                                             |
| coroutines                 | 16.2 ms                                                         | 14.2 ms: 1.14x faster                                                            |
| async_generators           | 270 ms                                                          | 242 ms: 1.12x faster                                                             |
| Geometric mean             | (ref)                                                           | 1.39x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250830-pythonperf1_win32-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| nbody          | 80.0 ms                                                         | 55.8 ms: 1.43x faster                                                            |
| pidigits       | 201 ms                                                          | 145 ms: 1.38x faster                                                             |
| float          | 54.6 ms                                                         | 44.4 ms: 1.23x faster                                                            |
| Geometric mean | (ref)                                                           | 1.35x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250830-pythonperf1_win32-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 101 ms                                                          | 78.2 ms: 1.29x faster                                                            |
| regex_v8       | 16.8 ms                                                         | 13.8 ms: 1.22x faster                                                            |
| regex_effbot   | 1.80 ms                                                         | 1.53 ms: 1.18x faster                                                            |
| regex_dna      | 114 ms                                                          | 117 ms: 1.03x slower                                                             |
| Geometric mean | (ref)                                                           | 1.16x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250830-pythonperf1_win32-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| tomli_loads          | 1.71 sec                                                        | 1.10 sec: 1.56x faster                                                           |
| json_loads           | 21.6 us                                                         | 14.0 us: 1.54x faster                                                            |
| unpickle_pure_python | 160 us                                                          | 107 us: 1.50x faster                                                             |
| json_dumps           | 7.30 ms                                                         | 5.36 ms: 1.36x faster                                                            |
| xml_etree_process    | 44.2 ms                                                         | 34.9 ms: 1.26x faster                                                            |
| xml_etree_parse      | 107 ms                                                          | 85.3 ms: 1.26x faster                                                            |
| xml_etree_generate   | 61.4 ms                                                         | 49.1 ms: 1.25x faster                                                            |
| pickle_pure_python   | 231 us                                                          | 201 us: 1.15x faster                                                             |
| xml_etree_iterparse  | 62.6 ms                                                         | 61.1 ms: 1.02x faster                                                            |
| Geometric mean       | (ref)                                                           | 1.31x faster                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250830-pythonperf1_win32-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup         | 28.3 ms                                                         | 25.5 ms: 1.11x faster                                                            |
| python_startup_no_site | 19.7 ms                                                         | 19.2 ms: 1.03x faster                                                            |
| Geometric mean         | (ref)                                                           | 1.07x faster                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250830-pythonperf1_win32-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| genshi_xml      | 50.1 ms                                                         | 34.6 ms: 1.45x faster                                                            |
| genshi_text     | 21.5 ms                                                         | 15.5 ms: 1.39x faster                                                            |
| mako            | 7.09 ms                                                         | 5.34 ms: 1.33x faster                                                            |
| django_template | 29.8 ms                                                         | 24.0 ms: 1.24x faster                                                            |
| Geometric mean  | (ref)                                                           | 1.35x faster                                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250830-pythonperf1_win32-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| thrift                     | 9.98 ms                                                         | 500 us: 19.95x faster                                                            |
| coverage                   | 324 ms                                                          | 49.4 ms: 6.55x faster                                                            |
| pathlib                    | 82.9 ms                                                         | 29.5 ms: 2.81x faster                                                            |
| asyncio_websockets         | 363 ms                                                          | 159 ms: 2.28x faster                                                             |
| mdp                        | 1.62 sec                                                        | 791 ms: 2.05x faster                                                             |
| telco                      | 6.96 ms                                                         | 3.75 ms: 1.86x faster                                                            |
| deepcopy                   | 314 us                                                          | 171 us: 1.84x faster                                                             |
| deepcopy_reduce            | 2.92 us                                                         | 1.83 us: 1.59x faster                                                            |
| tomli_loads                | 1.71 sec                                                        | 1.10 sec: 1.56x faster                                                           |
| json_loads                 | 21.6 us                                                         | 14.0 us: 1.54x faster                                                            |
| pprint_pformat             | 1.33 sec                                                        | 868 ms: 1.53x faster                                                             |
| pprint_safe_repr           | 648 ms                                                          | 429 ms: 1.51x faster                                                             |
| unpickle_pure_python       | 160 us                                                          | 107 us: 1.50x faster                                                             |
| fannkuch                   | 299 ms                                                          | 201 ms: 1.49x faster                                                             |
| json                       | 4.27 ms                                                         | 2.88 ms: 1.49x faster                                                            |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 330 ms: 1.47x faster                                                             |
| genshi_xml                 | 50.1 ms                                                         | 34.6 ms: 1.45x faster                                                            |
| async_tree_none            | 245 ms                                                          | 169 ms: 1.45x faster                                                             |
| async_tree_memoization     | 297 ms                                                          | 206 ms: 1.44x faster                                                             |
| nbody                      | 80.0 ms                                                         | 55.8 ms: 1.43x faster                                                            |
| go                         | 109 ms                                                          | 77.5 ms: 1.40x faster                                                            |
| scimark_fft                | 205 ms                                                          | 147 ms: 1.39x faster                                                             |
| genshi_text                | 21.5 ms                                                         | 15.5 ms: 1.39x faster                                                            |
| pidigits                   | 201 ms                                                          | 145 ms: 1.38x faster                                                             |
| bpe_tokeniser              | 3.46 sec                                                        | 2.52 sec: 1.38x faster                                                           |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 333 ms: 1.37x faster                                                             |
| logging_format             | 8.72 us                                                         | 6.39 us: 1.36x faster                                                            |
| async_tree_io              | 526 ms                                                          | 386 ms: 1.36x faster                                                             |
| json_dumps                 | 7.30 ms                                                         | 5.36 ms: 1.36x faster                                                            |
| logging_simple             | 7.99 us                                                         | 5.92 us: 1.35x faster                                                            |
| typing_runtime_protocols   | 138 us                                                          | 102 us: 1.35x faster                                                             |
| async_tree_memoization_tg  | 282 ms                                                          | 210 ms: 1.35x faster                                                             |
| mako                       | 7.09 ms                                                         | 5.34 ms: 1.33x faster                                                            |
| sympy_expand               | 373 ms                                                          | 289 ms: 1.29x faster                                                             |
| regex_compile              | 101 ms                                                          | 78.2 ms: 1.29x faster                                                            |
| async_tree_none_tg         | 214 ms                                                          | 167 ms: 1.29x faster                                                             |
| crypto_pyaes               | 56.9 ms                                                         | 44.6 ms: 1.28x faster                                                            |
| deepcopy_memo              | 25.4 us                                                         | 19.9 us: 1.27x faster                                                            |
| async_tree_io_tg           | 494 ms                                                          | 389 ms: 1.27x faster                                                             |
| pycparser                  | 872 ms                                                          | 688 ms: 1.27x faster                                                             |
| xml_etree_process          | 44.2 ms                                                         | 34.9 ms: 1.26x faster                                                            |
| sympy_str                  | 212 ms                                                          | 168 ms: 1.26x faster                                                             |
| sqlite_synth               | 1.95 us                                                         | 1.55 us: 1.26x faster                                                            |
| scimark_sparse_mat_mult    | 2.84 ms                                                         | 2.25 ms: 1.26x faster                                                            |
| dulwich_log                | 48.8 ms                                                         | 38.7 ms: 1.26x faster                                                            |
| xml_etree_parse            | 107 ms                                                          | 85.3 ms: 1.26x faster                                                            |
| chaos                      | 50.2 ms                                                         | 40.0 ms: 1.26x faster                                                            |
| xml_etree_generate         | 61.4 ms                                                         | 49.1 ms: 1.25x faster                                                            |
| html5lib                   | 47.5 ms                                                         | 38.0 ms: 1.25x faster                                                            |
| pyflate                    | 320 ms                                                          | 257 ms: 1.24x faster                                                             |
| django_template            | 29.8 ms                                                         | 24.0 ms: 1.24x faster                                                            |
| sympy_sum                  | 106 ms                                                          | 85.4 ms: 1.24x faster                                                            |
| float                      | 54.6 ms                                                         | 44.4 ms: 1.23x faster                                                            |
| nqueens                    | 72.1 ms                                                         | 58.9 ms: 1.22x faster                                                            |
| regex_v8                   | 16.8 ms                                                         | 13.8 ms: 1.22x faster                                                            |
| richards                   | 32.7 ms                                                         | 27.0 ms: 1.21x faster                                                            |
| comprehensions             | 12.5 us                                                         | 10.4 us: 1.21x faster                                                            |
| sympy_integrate            | 15.0 ms                                                         | 12.4 ms: 1.21x faster                                                            |
| richards_super             | 36.7 ms                                                         | 30.7 ms: 1.20x faster                                                            |
| scimark_monte_carlo        | 47.7 ms                                                         | 40.1 ms: 1.19x faster                                                            |
| bench_thread_pool          | 1.00 ms                                                         | 843 us: 1.19x faster                                                             |
| regex_effbot               | 1.80 ms                                                         | 1.53 ms: 1.18x faster                                                            |
| pylint                     | 227 ms                                                          | 194 ms: 1.17x faster                                                             |
| raytrace                   | 201 ms                                                          | 174 ms: 1.16x faster                                                             |
| 2to3                       | 250 ms                                                          | 217 ms: 1.16x faster                                                             |
| sphinx                     | 719 ms                                                          | 624 ms: 1.15x faster                                                             |
| pickle_pure_python         | 231 us                                                          | 201 us: 1.15x faster                                                             |
| coroutines                 | 16.2 ms                                                         | 14.2 ms: 1.14x faster                                                            |
| generators                 | 21.8 ms                                                         | 19.3 ms: 1.13x faster                                                            |
| logging_silent             | 60.3 ns                                                         | 53.6 ns: 1.13x faster                                                            |
| spectral_norm              | 69.4 ms                                                         | 61.9 ms: 1.12x faster                                                            |
| async_generators           | 270 ms                                                          | 242 ms: 1.12x faster                                                             |
| python_startup             | 28.3 ms                                                         | 25.5 ms: 1.11x faster                                                            |
| scimark_sor                | 85.9 ms                                                         | 77.8 ms: 1.10x faster                                                            |
| docutils                   | 1.78 sec                                                        | 1.61 sec: 1.10x faster                                                           |
| hexiom                     | 4.44 ms                                                         | 4.15 ms: 1.07x faster                                                            |
| deltablue                  | 2.33 ms                                                         | 2.20 ms: 1.06x faster                                                            |
| meteor_contest             | 74.6 ms                                                         | 71.2 ms: 1.05x faster                                                            |
| python_startup_no_site     | 19.7 ms                                                         | 19.2 ms: 1.03x faster                                                            |
| xml_etree_iterparse        | 62.6 ms                                                         | 61.1 ms: 1.02x faster                                                            |
| scimark_lu                 | 60.2 ms                                                         | 59.7 ms: 1.01x faster                                                            |
| bench_mp_pool              | 90.6 ms                                                         | 92.6 ms: 1.02x slower                                                            |
| regex_dna                  | 114 ms                                                          | 117 ms: 1.03x slower                                                             |
| k_core                     | 1.38 sec                                                        | 1.59 sec: 1.16x slower                                                           |
| connected_components       | 267 ms                                                          | 316 ms: 1.18x slower                                                             |
| create_gc_cycles           | 1.06 ms                                                         | 1.27 ms: 1.20x slower                                                            |
| shortest_path              | 290 ms                                                          | 350 ms: 1.21x slower                                                             |
| gc_traversal               | 1.75 ms                                                         | 2.11 ms: 1.21x slower                                                            |
| many_optionals             | 436 us                                                          | 553 us: 1.27x slower                                                             |
| subparsers                 | 14.8 ms                                                         | 29.1 ms: 1.97x slower                                                            |
| Geometric mean             | (ref)                                                           | 1.31x faster                                                                     |
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250830-3.15.0a0-d3d94e0-JIT/bm-20250830-pythonperf1_win32-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.315x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.23x
- 95% likely to have a speedup of 1.23x
- 99% likely to have a speedup of 1.21x

# Memory
- memory change: unknown