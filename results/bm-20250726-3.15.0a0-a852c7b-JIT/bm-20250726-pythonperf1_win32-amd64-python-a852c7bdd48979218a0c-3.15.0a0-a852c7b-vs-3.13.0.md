# Results vs. 3.13.0

- fork: python
- ref: a852c7bdd48979218a0c
- machine: windows-amd64
- commit hash: a852c7b
- commit date: 2025-07-26
- overall geometric mean: 1.275x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.18x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250726-pythonperf1_win32-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 250 ms                                                          | 225 ms: 1.11x faster                                                             |
| docutils       | 1.78 sec                                                        | 1.67 sec: 1.07x faster                                                           |
| html5lib       | 47.5 ms                                                         | 39.2 ms: 1.21x faster                                                            |
| sphinx         | 719 ms                                                          | 644 ms: 1.12x faster                                                             |
| Geometric mean | (ref)                                                           | 1.13x faster                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250726-pythonperf1_win32-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| asyncio_websockets         | 363 ms                                                          | 163 ms: 2.22x faster                                                             |
| async_tree_memoization     | 297 ms                                                          | 203 ms: 1.46x faster                                                             |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 338 ms: 1.43x faster                                                             |
| async_tree_none            | 245 ms                                                          | 178 ms: 1.38x faster                                                             |
| async_tree_memoization_tg  | 282 ms                                                          | 212 ms: 1.33x faster                                                             |
| async_tree_io              | 526 ms                                                          | 401 ms: 1.31x faster                                                             |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 353 ms: 1.29x faster                                                             |
| async_tree_none_tg         | 214 ms                                                          | 167 ms: 1.28x faster                                                             |
| async_tree_io_tg           | 494 ms                                                          | 393 ms: 1.26x faster                                                             |
| coroutines                 | 16.2 ms                                                         | 14.6 ms: 1.11x faster                                                            |
| async_generators           | 270 ms                                                          | 255 ms: 1.06x faster                                                             |
| Geometric mean             | (ref)                                                           | 1.35x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250726-pythonperf1_win32-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| nbody          | 80.0 ms                                                         | 57.7 ms: 1.38x faster                                                            |
| pidigits       | 201 ms                                                          | 149 ms: 1.35x faster                                                             |
| float          | 54.6 ms                                                         | 43.1 ms: 1.27x faster                                                            |
| Geometric mean | (ref)                                                           | 1.33x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250726-pythonperf1_win32-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 101 ms                                                          | 79.7 ms: 1.27x faster                                                            |
| regex_v8       | 16.8 ms                                                         | 14.6 ms: 1.15x faster                                                            |
| regex_effbot   | 1.80 ms                                                         | 1.65 ms: 1.09x faster                                                            |
| regex_dna      | 114 ms                                                          | 121 ms: 1.07x slower                                                             |
| Geometric mean | (ref)                                                           | 1.11x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250726-pythonperf1_win32-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| tomli_loads          | 1.71 sec                                                        | 1.13 sec: 1.52x faster                                                           |
| json_loads           | 21.6 us                                                         | 14.3 us: 1.51x faster                                                            |
| unpickle_pure_python | 160 us                                                          | 108 us: 1.49x faster                                                             |
| xml_etree_process    | 44.2 ms                                                         | 35.9 ms: 1.23x faster                                                            |
| xml_etree_parse      | 107 ms                                                          | 88.8 ms: 1.21x faster                                                            |
| xml_etree_generate   | 61.4 ms                                                         | 52.4 ms: 1.17x faster                                                            |
| json_dumps           | 7.30 ms                                                         | 6.36 ms: 1.15x faster                                                            |
| pickle_pure_python   | 231 us                                                          | 208 us: 1.11x faster                                                             |
| Geometric mean       | (ref)                                                           | 1.25x faster                                                                     |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250726-pythonperf1_win32-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup         | 28.3 ms                                                         | 27.3 ms: 1.04x faster                                                            |
| python_startup_no_site | 19.7 ms                                                         | 19.9 ms: 1.01x slower                                                            |
| Geometric mean         | (ref)                                                           | 1.01x faster                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250726-pythonperf1_win32-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| genshi_xml      | 50.1 ms                                                         | 35.4 ms: 1.42x faster                                                            |
| genshi_text     | 21.5 ms                                                         | 16.0 ms: 1.34x faster                                                            |
| mako            | 7.09 ms                                                         | 5.32 ms: 1.33x faster                                                            |
| django_template | 29.8 ms                                                         | 24.5 ms: 1.22x faster                                                            |
| Geometric mean  | (ref)                                                           | 1.33x faster                                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250726-pythonperf1_win32-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| thrift                     | 9.98 ms                                                         | 506 us: 19.72x faster                                                            |
| coverage                   | 324 ms                                                          | 49.0 ms: 6.61x faster                                                            |
| pathlib                    | 82.9 ms                                                         | 32.8 ms: 2.53x faster                                                            |
| asyncio_websockets         | 363 ms                                                          | 163 ms: 2.22x faster                                                             |
| mdp                        | 1.62 sec                                                        | 797 ms: 2.04x faster                                                             |
| deepcopy                   | 314 us                                                          | 169 us: 1.85x faster                                                             |
| deepcopy_reduce            | 2.92 us                                                         | 1.81 us: 1.61x faster                                                            |
| telco                      | 6.96 ms                                                         | 4.43 ms: 1.57x faster                                                            |
| tomli_loads                | 1.71 sec                                                        | 1.13 sec: 1.52x faster                                                           |
| json_loads                 | 21.6 us                                                         | 14.3 us: 1.51x faster                                                            |
| unpickle_pure_python       | 160 us                                                          | 108 us: 1.49x faster                                                             |
| async_tree_memoization     | 297 ms                                                          | 203 ms: 1.46x faster                                                             |
| pprint_pformat             | 1.33 sec                                                        | 911 ms: 1.46x faster                                                             |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 338 ms: 1.43x faster                                                             |
| genshi_xml                 | 50.1 ms                                                         | 35.4 ms: 1.42x faster                                                            |
| json                       | 4.27 ms                                                         | 3.05 ms: 1.40x faster                                                            |
| deepcopy_memo              | 25.4 us                                                         | 18.2 us: 1.39x faster                                                            |
| fannkuch                   | 299 ms                                                          | 215 ms: 1.39x faster                                                             |
| nbody                      | 80.0 ms                                                         | 57.7 ms: 1.38x faster                                                            |
| pprint_safe_repr           | 648 ms                                                          | 469 ms: 1.38x faster                                                             |
| async_tree_none            | 245 ms                                                          | 178 ms: 1.38x faster                                                             |
| go                         | 109 ms                                                          | 79.7 ms: 1.36x faster                                                            |
| pidigits                   | 201 ms                                                          | 149 ms: 1.35x faster                                                             |
| bpe_tokeniser              | 3.46 sec                                                        | 2.57 sec: 1.35x faster                                                           |
| genshi_text                | 21.5 ms                                                         | 16.0 ms: 1.34x faster                                                            |
| logging_format             | 8.72 us                                                         | 6.49 us: 1.34x faster                                                            |
| mako                       | 7.09 ms                                                         | 5.32 ms: 1.33x faster                                                            |
| async_tree_memoization_tg  | 282 ms                                                          | 212 ms: 1.33x faster                                                             |
| scimark_fft                | 205 ms                                                          | 154 ms: 1.33x faster                                                             |
| typing_runtime_protocols   | 138 us                                                          | 105 us: 1.31x faster                                                             |
| async_tree_io              | 526 ms                                                          | 401 ms: 1.31x faster                                                             |
| logging_simple             | 7.99 us                                                         | 6.10 us: 1.31x faster                                                            |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 353 ms: 1.29x faster                                                             |
| async_tree_none_tg         | 214 ms                                                          | 167 ms: 1.28x faster                                                             |
| float                      | 54.6 ms                                                         | 43.1 ms: 1.27x faster                                                            |
| regex_compile              | 101 ms                                                          | 79.7 ms: 1.27x faster                                                            |
| async_tree_io_tg           | 494 ms                                                          | 393 ms: 1.26x faster                                                             |
| chaos                      | 50.2 ms                                                         | 40.3 ms: 1.25x faster                                                            |
| pycparser                  | 872 ms                                                          | 703 ms: 1.24x faster                                                             |
| scimark_sparse_mat_mult    | 2.84 ms                                                         | 2.30 ms: 1.23x faster                                                            |
| crypto_pyaes               | 56.9 ms                                                         | 46.1 ms: 1.23x faster                                                            |
| pyflate                    | 320 ms                                                          | 260 ms: 1.23x faster                                                             |
| xml_etree_process          | 44.2 ms                                                         | 35.9 ms: 1.23x faster                                                            |
| sympy_expand               | 373 ms                                                          | 305 ms: 1.22x faster                                                             |
| django_template            | 29.8 ms                                                         | 24.5 ms: 1.22x faster                                                            |
| html5lib                   | 47.5 ms                                                         | 39.2 ms: 1.21x faster                                                            |
| xml_etree_parse            | 107 ms                                                          | 88.8 ms: 1.21x faster                                                            |
| comprehensions             | 12.5 us                                                         | 10.4 us: 1.21x faster                                                            |
| sqlite_synth               | 1.95 us                                                         | 1.63 us: 1.20x faster                                                            |
| sympy_sum                  | 106 ms                                                          | 88.3 ms: 1.20x faster                                                            |
| sympy_str                  | 212 ms                                                          | 178 ms: 1.19x faster                                                             |
| nqueens                    | 72.1 ms                                                         | 60.7 ms: 1.19x faster                                                            |
| richards                   | 32.7 ms                                                         | 27.7 ms: 1.18x faster                                                            |
| dulwich_log                | 48.8 ms                                                         | 41.4 ms: 1.18x faster                                                            |
| bench_thread_pool          | 1.00 ms                                                         | 853 us: 1.17x faster                                                             |
| richards_super             | 36.7 ms                                                         | 31.3 ms: 1.17x faster                                                            |
| xml_etree_generate         | 61.4 ms                                                         | 52.4 ms: 1.17x faster                                                            |
| sympy_integrate            | 15.0 ms                                                         | 12.9 ms: 1.16x faster                                                            |
| regex_v8                   | 16.8 ms                                                         | 14.6 ms: 1.15x faster                                                            |
| json_dumps                 | 7.30 ms                                                         | 6.36 ms: 1.15x faster                                                            |
| scimark_monte_carlo        | 47.7 ms                                                         | 42.3 ms: 1.13x faster                                                            |
| sphinx                     | 719 ms                                                          | 644 ms: 1.12x faster                                                             |
| scimark_sor                | 85.9 ms                                                         | 77.3 ms: 1.11x faster                                                            |
| pylint                     | 227 ms                                                          | 204 ms: 1.11x faster                                                             |
| 2to3                       | 250 ms                                                          | 225 ms: 1.11x faster                                                             |
| pickle_pure_python         | 231 us                                                          | 208 us: 1.11x faster                                                             |
| coroutines                 | 16.2 ms                                                         | 14.6 ms: 1.11x faster                                                            |
| raytrace                   | 201 ms                                                          | 183 ms: 1.10x faster                                                             |
| logging_silent             | 60.3 ns                                                         | 55.2 ns: 1.09x faster                                                            |
| regex_effbot               | 1.80 ms                                                         | 1.65 ms: 1.09x faster                                                            |
| spectral_norm              | 69.4 ms                                                         | 64.1 ms: 1.08x faster                                                            |
| generators                 | 21.8 ms                                                         | 20.1 ms: 1.08x faster                                                            |
| hexiom                     | 4.44 ms                                                         | 4.16 ms: 1.07x faster                                                            |
| docutils                   | 1.78 sec                                                        | 1.67 sec: 1.07x faster                                                           |
| async_generators           | 270 ms                                                          | 255 ms: 1.06x faster                                                             |
| deltablue                  | 2.33 ms                                                         | 2.22 ms: 1.05x faster                                                            |
| meteor_contest             | 74.6 ms                                                         | 71.4 ms: 1.04x faster                                                            |
| python_startup             | 28.3 ms                                                         | 27.3 ms: 1.04x faster                                                            |
| python_startup_no_site     | 19.7 ms                                                         | 19.9 ms: 1.01x slower                                                            |
| bench_mp_pool              | 90.6 ms                                                         | 95.9 ms: 1.06x slower                                                            |
| regex_dna                  | 114 ms                                                          | 121 ms: 1.07x slower                                                             |
| k_core                     | 1.38 sec                                                        | 1.63 sec: 1.19x slower                                                           |
| connected_components       | 267 ms                                                          | 324 ms: 1.22x slower                                                             |
| shortest_path              | 290 ms                                                          | 356 ms: 1.23x slower                                                             |
| gc_traversal               | 1.75 ms                                                         | 2.16 ms: 1.23x slower                                                            |
| create_gc_cycles           | 1.06 ms                                                         | 1.33 ms: 1.26x slower                                                            |
| many_optionals             | 436 us                                                          | 596 us: 1.37x slower                                                             |
| subparsers                 | 14.8 ms                                                         | 31.4 ms: 2.13x slower                                                            |
| Geometric mean             | (ref)                                                           | 1.27x faster                                                                     |

Benchmark hidden because not significant (2): scimark_lu, xml_etree_iterparse
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250726-3.15.0a0-a852c7b-JIT/bm-20250726-pythonperf1_win32-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.275x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.20x
- 95% likely to have a speedup of 1.19x
- 99% likely to have a speedup of 1.18x

# Memory
- memory change: unknown