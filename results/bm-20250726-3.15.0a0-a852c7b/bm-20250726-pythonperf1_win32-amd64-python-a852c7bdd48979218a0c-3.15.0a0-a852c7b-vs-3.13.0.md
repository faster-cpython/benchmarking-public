# Results vs. 3.13.0

- fork: python
- ref: a852c7bdd48979218a0c
- machine: windows-amd64
- commit hash: a852c7b
- commit date: 2025-07-26
- overall geometric mean: 1.233x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.13x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250726-pythonperf1_win32-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 250 ms                                                          | 227 ms: 1.10x faster                                                             |
| docutils       | 1.78 sec                                                        | 1.64 sec: 1.09x faster                                                           |
| html5lib       | 47.5 ms                                                         | 38.9 ms: 1.22x faster                                                            |
| sphinx         | 719 ms                                                          | 653 ms: 1.10x faster                                                             |
| Geometric mean | (ref)                                                           | 1.13x faster                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250726-pythonperf1_win32-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| asyncio_websockets         | 363 ms                                                          | 172 ms: 2.10x faster                                                             |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 338 ms: 1.43x faster                                                             |
| async_tree_memoization     | 297 ms                                                          | 213 ms: 1.39x faster                                                             |
| async_tree_none            | 245 ms                                                          | 179 ms: 1.37x faster                                                             |
| async_tree_io              | 526 ms                                                          | 394 ms: 1.33x faster                                                             |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 349 ms: 1.31x faster                                                             |
| async_tree_memoization_tg  | 282 ms                                                          | 221 ms: 1.28x faster                                                             |
| async_tree_io_tg           | 494 ms                                                          | 393 ms: 1.26x faster                                                             |
| async_tree_none_tg         | 214 ms                                                          | 178 ms: 1.21x faster                                                             |
| async_generators           | 270 ms                                                          | 241 ms: 1.12x faster                                                             |
| coroutines                 | 16.2 ms                                                         | 14.6 ms: 1.11x faster                                                            |
| Geometric mean             | (ref)                                                           | 1.34x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250726-pythonperf1_win32-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pidigits       | 201 ms                                                          | 150 ms: 1.34x faster                                                             |
| float          | 54.6 ms                                                         | 44.9 ms: 1.22x faster                                                            |
| nbody          | 80.0 ms                                                         | 67.9 ms: 1.18x faster                                                            |
| Geometric mean | (ref)                                                           | 1.24x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250726-pythonperf1_win32-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 101 ms                                                          | 81.5 ms: 1.24x faster                                                            |
| regex_effbot   | 1.80 ms                                                         | 1.55 ms: 1.16x faster                                                            |
| regex_v8       | 16.8 ms                                                         | 14.6 ms: 1.15x faster                                                            |
| regex_dna      | 114 ms                                                          | 126 ms: 1.11x slower                                                             |
| Geometric mean | (ref)                                                           | 1.11x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250726-pythonperf1_win32-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| json_loads           | 21.6 us                                                         | 15.0 us: 1.44x faster                                                            |
| xml_etree_parse      | 107 ms                                                          | 89.6 ms: 1.20x faster                                                            |
| tomli_loads          | 1.71 sec                                                        | 1.44 sec: 1.19x faster                                                           |
| unpickle_pure_python | 160 us                                                          | 136 us: 1.18x faster                                                             |
| json_dumps           | 7.30 ms                                                         | 6.52 ms: 1.12x faster                                                            |
| xml_etree_process    | 44.2 ms                                                         | 40.2 ms: 1.10x faster                                                            |
| xml_etree_generate   | 61.4 ms                                                         | 57.8 ms: 1.06x faster                                                            |
| pickle_pure_python   | 231 us                                                          | 223 us: 1.04x faster                                                             |
| xml_etree_iterparse  | 62.6 ms                                                         | 66.7 ms: 1.07x slower                                                            |
| Geometric mean       | (ref)                                                           | 1.13x faster                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250726-pythonperf1_win32-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup         | 28.3 ms                                                         | 26.6 ms: 1.06x faster                                                            |
| python_startup_no_site | 19.7 ms                                                         | 20.1 ms: 1.02x slower                                                            |
| Geometric mean         | (ref)                                                           | 1.02x faster                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250726-pythonperf1_win32-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| genshi_xml      | 50.1 ms                                                         | 34.9 ms: 1.44x faster                                                            |
| genshi_text     | 21.5 ms                                                         | 15.6 ms: 1.38x faster                                                            |
| django_template | 29.8 ms                                                         | 25.4 ms: 1.17x faster                                                            |
| mako            | 7.09 ms                                                         | 6.84 ms: 1.04x faster                                                            |
| Geometric mean  | (ref)                                                           | 1.25x faster                                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250726-pythonperf1_win32-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| thrift                     | 9.98 ms                                                         | 514 us: 19.42x faster                                                            |
| coverage                   | 324 ms                                                          | 50.5 ms: 6.41x faster                                                            |
| pathlib                    | 82.9 ms                                                         | 33.5 ms: 2.47x faster                                                            |
| asyncio_websockets         | 363 ms                                                          | 172 ms: 2.10x faster                                                             |
| mdp                        | 1.62 sec                                                        | 819 ms: 1.98x faster                                                             |
| deepcopy                   | 314 us                                                          | 173 us: 1.82x faster                                                             |
| deepcopy_reduce            | 2.92 us                                                         | 1.87 us: 1.56x faster                                                            |
| telco                      | 6.96 ms                                                         | 4.78 ms: 1.46x faster                                                            |
| json_loads                 | 21.6 us                                                         | 15.0 us: 1.44x faster                                                            |
| genshi_xml                 | 50.1 ms                                                         | 34.9 ms: 1.44x faster                                                            |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 338 ms: 1.43x faster                                                             |
| go                         | 109 ms                                                          | 77.6 ms: 1.40x faster                                                            |
| async_tree_memoization     | 297 ms                                                          | 213 ms: 1.39x faster                                                             |
| json                       | 4.27 ms                                                         | 3.07 ms: 1.39x faster                                                            |
| genshi_text                | 21.5 ms                                                         | 15.6 ms: 1.38x faster                                                            |
| async_tree_none            | 245 ms                                                          | 179 ms: 1.37x faster                                                             |
| pidigits                   | 201 ms                                                          | 150 ms: 1.34x faster                                                             |
| deepcopy_memo              | 25.4 us                                                         | 19.0 us: 1.34x faster                                                            |
| async_tree_io              | 526 ms                                                          | 394 ms: 1.33x faster                                                             |
| typing_runtime_protocols   | 138 us                                                          | 104 us: 1.33x faster                                                             |
| pprint_pformat             | 1.33 sec                                                        | 1.01 sec: 1.31x faster                                                           |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 349 ms: 1.31x faster                                                             |
| pprint_safe_repr           | 648 ms                                                          | 496 ms: 1.31x faster                                                             |
| sympy_expand               | 373 ms                                                          | 287 ms: 1.30x faster                                                             |
| logging_format             | 8.72 us                                                         | 6.79 us: 1.28x faster                                                            |
| async_tree_memoization_tg  | 282 ms                                                          | 221 ms: 1.28x faster                                                             |
| logging_simple             | 7.99 us                                                         | 6.27 us: 1.27x faster                                                            |
| async_tree_io_tg           | 494 ms                                                          | 393 ms: 1.26x faster                                                             |
| regex_compile              | 101 ms                                                          | 81.5 ms: 1.24x faster                                                            |
| sqlite_synth               | 1.95 us                                                         | 1.58 us: 1.23x faster                                                            |
| sympy_str                  | 212 ms                                                          | 173 ms: 1.22x faster                                                             |
| html5lib                   | 47.5 ms                                                         | 38.9 ms: 1.22x faster                                                            |
| pycparser                  | 872 ms                                                          | 717 ms: 1.22x faster                                                             |
| float                      | 54.6 ms                                                         | 44.9 ms: 1.22x faster                                                            |
| async_tree_none_tg         | 214 ms                                                          | 178 ms: 1.21x faster                                                             |
| sympy_sum                  | 106 ms                                                          | 87.9 ms: 1.20x faster                                                            |
| xml_etree_parse            | 107 ms                                                          | 89.6 ms: 1.20x faster                                                            |
| dulwich_log                | 48.8 ms                                                         | 40.8 ms: 1.20x faster                                                            |
| crypto_pyaes               | 56.9 ms                                                         | 47.8 ms: 1.19x faster                                                            |
| tomli_loads                | 1.71 sec                                                        | 1.44 sec: 1.19x faster                                                           |
| sympy_integrate            | 15.0 ms                                                         | 12.6 ms: 1.19x faster                                                            |
| unpickle_pure_python       | 160 us                                                          | 136 us: 1.18x faster                                                             |
| richards                   | 32.7 ms                                                         | 27.8 ms: 1.18x faster                                                            |
| nbody                      | 80.0 ms                                                         | 67.9 ms: 1.18x faster                                                            |
| chaos                      | 50.2 ms                                                         | 42.7 ms: 1.18x faster                                                            |
| django_template            | 29.8 ms                                                         | 25.4 ms: 1.17x faster                                                            |
| regex_effbot               | 1.80 ms                                                         | 1.55 ms: 1.16x faster                                                            |
| bpe_tokeniser              | 3.46 sec                                                        | 2.97 sec: 1.16x faster                                                           |
| bench_thread_pool          | 1.00 ms                                                         | 861 us: 1.16x faster                                                             |
| scimark_monte_carlo        | 47.7 ms                                                         | 41.2 ms: 1.16x faster                                                            |
| richards_super             | 36.7 ms                                                         | 31.8 ms: 1.15x faster                                                            |
| regex_v8                   | 16.8 ms                                                         | 14.6 ms: 1.15x faster                                                            |
| fannkuch                   | 299 ms                                                          | 261 ms: 1.14x faster                                                             |
| nqueens                    | 72.1 ms                                                         | 63.8 ms: 1.13x faster                                                            |
| pylint                     | 227 ms                                                          | 201 ms: 1.13x faster                                                             |
| json_dumps                 | 7.30 ms                                                         | 6.52 ms: 1.12x faster                                                            |
| async_generators           | 270 ms                                                          | 241 ms: 1.12x faster                                                             |
| pyflate                    | 320 ms                                                          | 286 ms: 1.12x faster                                                             |
| coroutines                 | 16.2 ms                                                         | 14.6 ms: 1.11x faster                                                            |
| raytrace                   | 201 ms                                                          | 181 ms: 1.11x faster                                                             |
| generators                 | 21.8 ms                                                         | 19.7 ms: 1.10x faster                                                            |
| 2to3                       | 250 ms                                                          | 227 ms: 1.10x faster                                                             |
| sphinx                     | 719 ms                                                          | 653 ms: 1.10x faster                                                             |
| xml_etree_process          | 44.2 ms                                                         | 40.2 ms: 1.10x faster                                                            |
| scimark_sparse_mat_mult    | 2.84 ms                                                         | 2.59 ms: 1.09x faster                                                            |
| scimark_sor                | 85.9 ms                                                         | 78.6 ms: 1.09x faster                                                            |
| comprehensions             | 12.5 us                                                         | 11.5 us: 1.09x faster                                                            |
| docutils                   | 1.78 sec                                                        | 1.64 sec: 1.09x faster                                                           |
| spectral_norm              | 69.4 ms                                                         | 63.9 ms: 1.09x faster                                                            |
| scimark_fft                | 205 ms                                                          | 190 ms: 1.08x faster                                                             |
| hexiom                     | 4.44 ms                                                         | 4.13 ms: 1.07x faster                                                            |
| python_startup             | 28.3 ms                                                         | 26.6 ms: 1.06x faster                                                            |
| xml_etree_generate         | 61.4 ms                                                         | 57.8 ms: 1.06x faster                                                            |
| logging_silent             | 60.3 ns                                                         | 57.9 ns: 1.04x faster                                                            |
| mako                       | 7.09 ms                                                         | 6.84 ms: 1.04x faster                                                            |
| pickle_pure_python         | 231 us                                                          | 223 us: 1.04x faster                                                             |
| deltablue                  | 2.33 ms                                                         | 2.29 ms: 1.02x faster                                                            |
| meteor_contest             | 74.6 ms                                                         | 75.5 ms: 1.01x slower                                                            |
| python_startup_no_site     | 19.7 ms                                                         | 20.1 ms: 1.02x slower                                                            |
| scimark_lu                 | 60.2 ms                                                         | 63.2 ms: 1.05x slower                                                            |
| bench_mp_pool              | 90.6 ms                                                         | 96.1 ms: 1.06x slower                                                            |
| xml_etree_iterparse        | 62.6 ms                                                         | 66.7 ms: 1.07x slower                                                            |
| regex_dna                  | 114 ms                                                          | 126 ms: 1.11x slower                                                             |
| create_gc_cycles           | 1.06 ms                                                         | 1.32 ms: 1.25x slower                                                            |
| k_core                     | 1.38 sec                                                        | 1.72 sec: 1.25x slower                                                           |
| shortest_path              | 290 ms                                                          | 364 ms: 1.25x slower                                                             |
| connected_components       | 267 ms                                                          | 335 ms: 1.26x slower                                                             |
| gc_traversal               | 1.75 ms                                                         | 2.20 ms: 1.26x slower                                                            |
| many_optionals             | 436 us                                                          | 568 us: 1.30x slower                                                             |
| subparsers                 | 14.8 ms                                                         | 30.7 ms: 2.08x slower                                                            |
| Geometric mean             | (ref)                                                           | 1.23x faster                                                                     |
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250726-3.15.0a0-a852c7b/bm-20250726-pythonperf1_win32-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.233x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.16x
- 95% likely to have a speedup of 1.15x
- 99% likely to have a speedup of 1.13x

# Memory
- memory change: unknown