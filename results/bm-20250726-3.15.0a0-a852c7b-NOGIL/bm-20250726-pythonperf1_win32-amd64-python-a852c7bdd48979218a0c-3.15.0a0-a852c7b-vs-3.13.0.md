# Results vs. 3.13.0

- fork: python
- ref: a852c7bdd48979218a0c
- machine: windows-amd64
- commit hash: a852c7b
- commit date: 2025-07-26
- overall geometric mean: 1.103x faster
- HPT reliability: 99.40%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250726-pythonperf1_win32-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 250 ms                                                          | 231 ms: 1.08x faster                                                             |
| docutils       | 1.78 sec                                                        | 3.03 sec: 1.70x slower                                                           |
| html5lib       | 47.5 ms                                                         | 41.4 ms: 1.15x faster                                                            |
| Geometric mean | (ref)                                                           | 1.09x slower                                                                     |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250726-pythonperf1_win32-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| asyncio_websockets         | 363 ms                                                          | 140 ms: 2.59x faster                                                             |
| async_tree_io_tg           | 494 ms                                                          | 331 ms: 1.49x faster                                                             |
| async_tree_none_tg         | 214 ms                                                          | 148 ms: 1.45x faster                                                             |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 334 ms: 1.45x faster                                                             |
| async_tree_io              | 526 ms                                                          | 365 ms: 1.44x faster                                                             |
| async_tree_memoization_tg  | 282 ms                                                          | 197 ms: 1.43x faster                                                             |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 323 ms: 1.41x faster                                                             |
| async_tree_none            | 245 ms                                                          | 176 ms: 1.39x faster                                                             |
| async_tree_memoization     | 297 ms                                                          | 218 ms: 1.36x faster                                                             |
| coroutines                 | 16.2 ms                                                         | 14.3 ms: 1.13x faster                                                            |
| Geometric mean             | (ref)                                                           | 1.43x faster                                                                     |

Benchmark hidden because not significant (1): async_generators

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250726-pythonperf1_win32-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pidigits       | 201 ms                                                          | 138 ms: 1.45x faster                                                             |
| float          | 54.6 ms                                                         | 46.9 ms: 1.16x faster                                                            |
| nbody          | 80.0 ms                                                         | 83.7 ms: 1.05x slower                                                            |
| Geometric mean | (ref)                                                           | 1.17x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250726-pythonperf1_win32-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_v8       | 16.8 ms                                                         | 12.9 ms: 1.31x faster                                                            |
| regex_effbot   | 1.80 ms                                                         | 1.52 ms: 1.18x faster                                                            |
| regex_compile  | 101 ms                                                          | 95.2 ms: 1.06x faster                                                            |
| regex_dna      | 114 ms                                                          | 112 ms: 1.01x faster                                                             |
| Geometric mean | (ref)                                                           | 1.13x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250726-pythonperf1_win32-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| json_loads           | 21.6 us                                                         | 15.8 us: 1.37x faster                                                            |
| xml_etree_parse      | 107 ms                                                          | 93.4 ms: 1.15x faster                                                            |
| json_dumps           | 7.30 ms                                                         | 6.75 ms: 1.08x faster                                                            |
| xml_etree_iterparse  | 62.6 ms                                                         | 59.9 ms: 1.04x faster                                                            |
| unpickle_pure_python | 160 us                                                          | 158 us: 1.02x faster                                                             |
| pickle_pure_python   | 231 us                                                          | 237 us: 1.02x slower                                                             |
| xml_etree_generate   | 61.4 ms                                                         | 63.2 ms: 1.03x slower                                                            |
| tomli_loads          | 1.71 sec                                                        | 2.83 sec: 1.65x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.00x faster                                                                     |

Benchmark hidden because not significant (1): xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250726-pythonperf1_win32-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup         | 28.3 ms                                                         | 27.2 ms: 1.04x faster                                                            |
| python_startup_no_site | 19.7 ms                                                         | 20.2 ms: 1.03x slower                                                            |
| Geometric mean         | (ref)                                                           | 1.01x faster                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250726-pythonperf1_win32-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| genshi_xml      | 50.1 ms                                                         | 40.7 ms: 1.23x faster                                                            |
| genshi_text     | 21.5 ms                                                         | 19.6 ms: 1.09x faster                                                            |
| django_template | 29.8 ms                                                         | 27.3 ms: 1.09x faster                                                            |
| mako            | 7.09 ms                                                         | 9.64 ms: 1.36x slower                                                            |
| Geometric mean  | (ref)                                                           | 1.02x faster                                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250726-pythonperf1_win32-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| thrift                     | 9.98 ms                                                         | 573 us: 17.41x faster                                                            |
| coverage                   | 324 ms                                                          | 68.4 ms: 4.73x faster                                                            |
| asyncio_websockets         | 363 ms                                                          | 140 ms: 2.59x faster                                                             |
| pathlib                    | 82.9 ms                                                         | 33.9 ms: 2.45x faster                                                            |
| deepcopy                   | 314 us                                                          | 204 us: 1.54x faster                                                             |
| async_tree_io_tg           | 494 ms                                                          | 331 ms: 1.49x faster                                                             |
| pidigits                   | 201 ms                                                          | 138 ms: 1.45x faster                                                             |
| sqlite_synth               | 1.95 us                                                         | 1.35 us: 1.45x faster                                                            |
| async_tree_none_tg         | 214 ms                                                          | 148 ms: 1.45x faster                                                             |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 334 ms: 1.45x faster                                                             |
| async_tree_io              | 526 ms                                                          | 365 ms: 1.44x faster                                                             |
| async_tree_memoization_tg  | 282 ms                                                          | 197 ms: 1.43x faster                                                             |
| gc_traversal               | 1.75 ms                                                         | 1.23 ms: 1.42x faster                                                            |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 323 ms: 1.41x faster                                                             |
| async_tree_none            | 245 ms                                                          | 176 ms: 1.39x faster                                                             |
| json                       | 4.27 ms                                                         | 3.08 ms: 1.39x faster                                                            |
| json_loads                 | 21.6 us                                                         | 15.8 us: 1.37x faster                                                            |
| async_tree_memoization     | 297 ms                                                          | 218 ms: 1.36x faster                                                             |
| deepcopy_reduce            | 2.92 us                                                         | 2.18 us: 1.34x faster                                                            |
| mdp                        | 1.62 sec                                                        | 1.22 sec: 1.33x faster                                                           |
| telco                      | 6.96 ms                                                         | 5.24 ms: 1.33x faster                                                            |
| regex_v8                   | 16.8 ms                                                         | 12.9 ms: 1.31x faster                                                            |
| genshi_xml                 | 50.1 ms                                                         | 40.7 ms: 1.23x faster                                                            |
| deepcopy_memo              | 25.4 us                                                         | 21.2 us: 1.20x faster                                                            |
| pycparser                  | 872 ms                                                          | 729 ms: 1.20x faster                                                             |
| regex_effbot               | 1.80 ms                                                         | 1.52 ms: 1.18x faster                                                            |
| logging_format             | 8.72 us                                                         | 7.41 us: 1.18x faster                                                            |
| go                         | 109 ms                                                          | 93.0 ms: 1.17x faster                                                            |
| logging_simple             | 7.99 us                                                         | 6.85 us: 1.17x faster                                                            |
| float                      | 54.6 ms                                                         | 46.9 ms: 1.16x faster                                                            |
| xml_etree_parse            | 107 ms                                                          | 93.4 ms: 1.15x faster                                                            |
| html5lib                   | 47.5 ms                                                         | 41.4 ms: 1.15x faster                                                            |
| pprint_safe_repr           | 648 ms                                                          | 566 ms: 1.15x faster                                                             |
| sympy_expand               | 373 ms                                                          | 326 ms: 1.14x faster                                                             |
| coroutines                 | 16.2 ms                                                         | 14.3 ms: 1.13x faster                                                            |
| bench_mp_pool              | 90.6 ms                                                         | 79.9 ms: 1.13x faster                                                            |
| sympy_str                  | 212 ms                                                          | 189 ms: 1.12x faster                                                             |
| genshi_text                | 21.5 ms                                                         | 19.6 ms: 1.09x faster                                                            |
| django_template            | 29.8 ms                                                         | 27.3 ms: 1.09x faster                                                            |
| pylint                     | 227 ms                                                          | 208 ms: 1.09x faster                                                             |
| 2to3                       | 250 ms                                                          | 231 ms: 1.08x faster                                                             |
| json_dumps                 | 7.30 ms                                                         | 6.75 ms: 1.08x faster                                                            |
| sympy_sum                  | 106 ms                                                          | 98.2 ms: 1.07x faster                                                            |
| dulwich_log                | 48.8 ms                                                         | 45.5 ms: 1.07x faster                                                            |
| regex_compile              | 101 ms                                                          | 95.2 ms: 1.06x faster                                                            |
| chaos                      | 50.2 ms                                                         | 47.6 ms: 1.06x faster                                                            |
| xml_etree_iterparse        | 62.6 ms                                                         | 59.9 ms: 1.04x faster                                                            |
| python_startup             | 28.3 ms                                                         | 27.2 ms: 1.04x faster                                                            |
| sympy_integrate            | 15.0 ms                                                         | 14.4 ms: 1.04x faster                                                            |
| pyflate                    | 320 ms                                                          | 313 ms: 1.02x faster                                                             |
| unpickle_pure_python       | 160 us                                                          | 158 us: 1.02x faster                                                             |
| regex_dna                  | 114 ms                                                          | 112 ms: 1.01x faster                                                             |
| nqueens                    | 72.1 ms                                                         | 71.4 ms: 1.01x faster                                                            |
| richards                   | 32.7 ms                                                         | 33.4 ms: 1.02x slower                                                            |
| pickle_pure_python         | 231 us                                                          | 237 us: 1.02x slower                                                             |
| python_startup_no_site     | 19.7 ms                                                         | 20.2 ms: 1.03x slower                                                            |
| scimark_sor                | 85.9 ms                                                         | 88.3 ms: 1.03x slower                                                            |
| xml_etree_generate         | 61.4 ms                                                         | 63.2 ms: 1.03x slower                                                            |
| scimark_fft                | 205 ms                                                          | 211 ms: 1.03x slower                                                             |
| generators                 | 21.8 ms                                                         | 22.7 ms: 1.04x slower                                                            |
| nbody                      | 80.0 ms                                                         | 83.7 ms: 1.05x slower                                                            |
| fannkuch                   | 299 ms                                                          | 315 ms: 1.05x slower                                                             |
| hexiom                     | 4.44 ms                                                         | 4.68 ms: 1.05x slower                                                            |
| spectral_norm              | 69.4 ms                                                         | 73.7 ms: 1.06x slower                                                            |
| logging_silent             | 60.3 ns                                                         | 64.8 ns: 1.07x slower                                                            |
| richards_super             | 36.7 ms                                                         | 39.4 ms: 1.07x slower                                                            |
| scimark_sparse_mat_mult    | 2.84 ms                                                         | 3.05 ms: 1.08x slower                                                            |
| scimark_monte_carlo        | 47.7 ms                                                         | 51.5 ms: 1.08x slower                                                            |
| deltablue                  | 2.33 ms                                                         | 2.52 ms: 1.08x slower                                                            |
| raytrace                   | 201 ms                                                          | 218 ms: 1.08x slower                                                             |
| scimark_lu                 | 60.2 ms                                                         | 65.3 ms: 1.08x slower                                                            |
| bench_thread_pool          | 1.00 ms                                                         | 1.12 ms: 1.12x slower                                                            |
| meteor_contest             | 74.6 ms                                                         | 87.4 ms: 1.17x slower                                                            |
| pprint_pformat             | 1.33 sec                                                        | 1.80 sec: 1.35x slower                                                           |
| mako                       | 7.09 ms                                                         | 9.64 ms: 1.36x slower                                                            |
| many_optionals             | 436 us                                                          | 650 us: 1.49x slower                                                             |
| bpe_tokeniser              | 3.46 sec                                                        | 5.57 sec: 1.61x slower                                                           |
| tomli_loads                | 1.71 sec                                                        | 2.83 sec: 1.65x slower                                                           |
| docutils                   | 1.78 sec                                                        | 3.03 sec: 1.70x slower                                                           |
| k_core                     | 1.38 sec                                                        | 2.76 sec: 2.00x slower                                                           |
| shortest_path              | 290 ms                                                          | 675 ms: 2.33x slower                                                             |
| connected_components       | 267 ms                                                          | 639 ms: 2.40x slower                                                             |
| subparsers                 | 14.8 ms                                                         | 36.2 ms: 2.45x slower                                                            |
| Geometric mean             | (ref)                                                           | 1.10x faster                                                                     |

Benchmark hidden because not significant (7): create_gc_cycles, async_generators, typing_runtime_protocols, crypto_pyaes, comprehensions, xml_etree_process, sphinx
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250726-3.15.0a0-a852c7b-NOGIL/bm-20250726-pythonperf1_win32-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.103x faster

# HPT report

- Reliability score: 99.40% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown