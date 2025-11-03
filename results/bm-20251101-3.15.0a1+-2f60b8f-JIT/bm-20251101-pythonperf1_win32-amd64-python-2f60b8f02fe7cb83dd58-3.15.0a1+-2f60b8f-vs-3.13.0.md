# Results vs. 3.13.0

- fork: python
- ref: 2f60b8f02fe7cb83dd58
- machine: windows-amd64
- commit hash: 2f60b8f
- commit date: 2025-11-01
- overall geometric mean: 1.342x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.22x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20251101-pythonperf1_win32-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 250 ms                                                          | 213 ms: 1.17x faster                                                              |
| docutils       | 1.78 sec                                                        | 1.60 sec: 1.11x faster                                                            |
| html5lib       | 47.5 ms                                                         | 35.6 ms: 1.33x faster                                                             |
| sphinx         | 719 ms                                                          | 615 ms: 1.17x faster                                                              |
| Geometric mean | (ref)                                                           | 1.19x faster                                                                      |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20251101-pythonperf1_win32-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|----------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| asyncio_websockets         | 363 ms                                                          | 145 ms: 2.50x faster                                                              |
| async_tree_memoization     | 297 ms                                                          | 190 ms: 1.56x faster                                                              |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 321 ms: 1.51x faster                                                              |
| async_tree_none            | 245 ms                                                          | 164 ms: 1.49x faster                                                              |
| async_tree_memoization_tg  | 282 ms                                                          | 192 ms: 1.47x faster                                                              |
| async_tree_io              | 526 ms                                                          | 358 ms: 1.47x faster                                                              |
| async_tree_none_tg         | 214 ms                                                          | 152 ms: 1.41x faster                                                              |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 333 ms: 1.37x faster                                                              |
| async_tree_io_tg           | 494 ms                                                          | 361 ms: 1.37x faster                                                              |
| async_generators           | 270 ms                                                          | 241 ms: 1.12x faster                                                              |
| coroutines                 | 16.2 ms                                                         | 14.5 ms: 1.12x faster                                                             |
| Geometric mean             | (ref)                                                           | 1.46x faster                                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20251101-pythonperf1_win32-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| nbody          | 80.0 ms                                                         | 53.4 ms: 1.50x faster                                                             |
| float          | 54.6 ms                                                         | 38.8 ms: 1.41x faster                                                             |
| pidigits       | 201 ms                                                          | 143 ms: 1.40x faster                                                              |
| Geometric mean | (ref)                                                           | 1.43x faster                                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20251101-pythonperf1_win32-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_compile  | 101 ms                                                          | 77.0 ms: 1.31x faster                                                             |
| regex_v8       | 16.8 ms                                                         | 14.0 ms: 1.21x faster                                                             |
| regex_effbot   | 1.80 ms                                                         | 1.54 ms: 1.17x faster                                                             |
| regex_dna      | 114 ms                                                          | 117 ms: 1.03x slower                                                              |
| Geometric mean | (ref)                                                           | 1.16x faster                                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20251101-pythonperf1_win32-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|----------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| tomli_loads          | 1.71 sec                                                        | 1.09 sec: 1.57x faster                                                            |
| json_loads           | 21.6 us                                                         | 13.9 us: 1.55x faster                                                             |
| unpickle_pure_python | 160 us                                                          | 105 us: 1.52x faster                                                              |
| json_dumps           | 7.30 ms                                                         | 5.47 ms: 1.33x faster                                                             |
| xml_etree_generate   | 61.4 ms                                                         | 48.6 ms: 1.26x faster                                                             |
| xml_etree_process    | 44.2 ms                                                         | 35.0 ms: 1.26x faster                                                             |
| xml_etree_parse      | 107 ms                                                          | 85.6 ms: 1.25x faster                                                             |
| pickle_pure_python   | 231 us                                                          | 196 us: 1.18x faster                                                              |
| xml_etree_iterparse  | 62.6 ms                                                         | 56.5 ms: 1.11x faster                                                             |
| Geometric mean       | (ref)                                                           | 1.33x faster                                                                      |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20251101-pythonperf1_win32-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup         | 28.3 ms                                                         | 25.2 ms: 1.12x faster                                                             |
| python_startup_no_site | 19.7 ms                                                         | 19.0 ms: 1.03x faster                                                             |
| Geometric mean         | (ref)                                                           | 1.08x faster                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20251101-pythonperf1_win32-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|-----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| genshi_xml      | 50.1 ms                                                         | 34.7 ms: 1.44x faster                                                             |
| genshi_text     | 21.5 ms                                                         | 15.6 ms: 1.38x faster                                                             |
| mako            | 7.09 ms                                                         | 5.23 ms: 1.36x faster                                                             |
| django_template | 29.8 ms                                                         | 23.4 ms: 1.27x faster                                                             |
| Geometric mean  | (ref)                                                           | 1.36x faster                                                                      |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20251101-pythonperf1_win32-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|----------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| thrift                     | 9.98 ms                                                         | 490 us: 20.35x faster                                                             |
| coverage                   | 324 ms                                                          | 48.8 ms: 6.64x faster                                                             |
| pathlib                    | 82.9 ms                                                         | 28.7 ms: 2.89x faster                                                             |
| asyncio_websockets         | 363 ms                                                          | 145 ms: 2.50x faster                                                              |
| mdp                        | 1.62 sec                                                        | 779 ms: 2.08x faster                                                              |
| deepcopy                   | 314 us                                                          | 161 us: 1.95x faster                                                              |
| telco                      | 6.96 ms                                                         | 3.90 ms: 1.78x faster                                                             |
| deepcopy_reduce            | 2.92 us                                                         | 1.71 us: 1.70x faster                                                             |
| tomli_loads                | 1.71 sec                                                        | 1.09 sec: 1.57x faster                                                            |
| async_tree_memoization     | 297 ms                                                          | 190 ms: 1.56x faster                                                              |
| pprint_pformat             | 1.33 sec                                                        | 852 ms: 1.56x faster                                                              |
| json_loads                 | 21.6 us                                                         | 13.9 us: 1.55x faster                                                             |
| pprint_safe_repr           | 648 ms                                                          | 418 ms: 1.55x faster                                                              |
| scimark_fft                | 205 ms                                                          | 133 ms: 1.54x faster                                                              |
| unpickle_pure_python       | 160 us                                                          | 105 us: 1.52x faster                                                              |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 321 ms: 1.51x faster                                                              |
| nbody                      | 80.0 ms                                                         | 53.4 ms: 1.50x faster                                                             |
| async_tree_none            | 245 ms                                                          | 164 ms: 1.49x faster                                                              |
| deepcopy_memo              | 25.4 us                                                         | 17.1 us: 1.49x faster                                                             |
| json                       | 4.27 ms                                                         | 2.91 ms: 1.47x faster                                                             |
| async_tree_memoization_tg  | 282 ms                                                          | 192 ms: 1.47x faster                                                              |
| async_tree_io              | 526 ms                                                          | 358 ms: 1.47x faster                                                              |
| fannkuch                   | 299 ms                                                          | 204 ms: 1.47x faster                                                              |
| go                         | 109 ms                                                          | 74.3 ms: 1.46x faster                                                             |
| genshi_xml                 | 50.1 ms                                                         | 34.7 ms: 1.44x faster                                                             |
| async_tree_none_tg         | 214 ms                                                          | 152 ms: 1.41x faster                                                              |
| float                      | 54.6 ms                                                         | 38.8 ms: 1.41x faster                                                             |
| pidigits                   | 201 ms                                                          | 143 ms: 1.40x faster                                                              |
| bpe_tokeniser              | 3.46 sec                                                        | 2.49 sec: 1.39x faster                                                            |
| genshi_text                | 21.5 ms                                                         | 15.6 ms: 1.38x faster                                                             |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 333 ms: 1.37x faster                                                              |
| async_tree_io_tg           | 494 ms                                                          | 361 ms: 1.37x faster                                                              |
| logging_format             | 8.72 us                                                         | 6.42 us: 1.36x faster                                                             |
| mako                       | 7.09 ms                                                         | 5.23 ms: 1.36x faster                                                             |
| logging_simple             | 7.99 us                                                         | 5.91 us: 1.35x faster                                                             |
| scimark_sparse_mat_mult    | 2.84 ms                                                         | 2.12 ms: 1.34x faster                                                             |
| json_dumps                 | 7.30 ms                                                         | 5.47 ms: 1.33x faster                                                             |
| pycparser                  | 872 ms                                                          | 653 ms: 1.33x faster                                                              |
| html5lib                   | 47.5 ms                                                         | 35.6 ms: 1.33x faster                                                             |
| typing_runtime_protocols   | 138 us                                                          | 104 us: 1.32x faster                                                              |
| regex_compile              | 101 ms                                                          | 77.0 ms: 1.31x faster                                                             |
| chaos                      | 50.2 ms                                                         | 38.5 ms: 1.30x faster                                                             |
| sympy_expand               | 373 ms                                                          | 287 ms: 1.30x faster                                                              |
| pyflate                    | 320 ms                                                          | 248 ms: 1.29x faster                                                              |
| django_template            | 29.8 ms                                                         | 23.4 ms: 1.27x faster                                                             |
| crypto_pyaes               | 56.9 ms                                                         | 44.9 ms: 1.27x faster                                                             |
| sympy_str                  | 212 ms                                                          | 167 ms: 1.27x faster                                                              |
| sqlite_synth               | 1.95 us                                                         | 1.55 us: 1.26x faster                                                             |
| xml_etree_generate         | 61.4 ms                                                         | 48.6 ms: 1.26x faster                                                             |
| xml_etree_process          | 44.2 ms                                                         | 35.0 ms: 1.26x faster                                                             |
| dulwich_log                | 48.8 ms                                                         | 38.7 ms: 1.26x faster                                                             |
| xml_etree_parse            | 107 ms                                                          | 85.6 ms: 1.25x faster                                                             |
| richards                   | 32.7 ms                                                         | 26.1 ms: 1.25x faster                                                             |
| sympy_sum                  | 106 ms                                                          | 85.0 ms: 1.24x faster                                                             |
| richards_super             | 36.7 ms                                                         | 29.7 ms: 1.23x faster                                                             |
| comprehensions             | 12.5 us                                                         | 10.2 us: 1.22x faster                                                             |
| regex_v8                   | 16.8 ms                                                         | 14.0 ms: 1.21x faster                                                             |
| bench_thread_pool          | 1.00 ms                                                         | 834 us: 1.20x faster                                                              |
| nqueens                    | 72.1 ms                                                         | 60.1 ms: 1.20x faster                                                             |
| sympy_integrate            | 15.0 ms                                                         | 12.5 ms: 1.20x faster                                                             |
| raytrace                   | 201 ms                                                          | 169 ms: 1.19x faster                                                              |
| pickle_pure_python         | 231 us                                                          | 196 us: 1.18x faster                                                              |
| scimark_sor                | 85.9 ms                                                         | 73.0 ms: 1.18x faster                                                             |
| 2to3                       | 250 ms                                                          | 213 ms: 1.17x faster                                                              |
| regex_effbot               | 1.80 ms                                                         | 1.54 ms: 1.17x faster                                                             |
| sphinx                     | 719 ms                                                          | 615 ms: 1.17x faster                                                              |
| pylint                     | 227 ms                                                          | 198 ms: 1.15x faster                                                              |
| generators                 | 21.8 ms                                                         | 19.1 ms: 1.14x faster                                                             |
| hexiom                     | 4.44 ms                                                         | 3.91 ms: 1.14x faster                                                             |
| scimark_monte_carlo        | 47.7 ms                                                         | 42.2 ms: 1.13x faster                                                             |
| python_startup             | 28.3 ms                                                         | 25.2 ms: 1.12x faster                                                             |
| async_generators           | 270 ms                                                          | 241 ms: 1.12x faster                                                              |
| coroutines                 | 16.2 ms                                                         | 14.5 ms: 1.12x faster                                                             |
| docutils                   | 1.78 sec                                                        | 1.60 sec: 1.11x faster                                                            |
| logging_silent             | 60.3 ns                                                         | 54.4 ns: 1.11x faster                                                             |
| xml_etree_iterparse        | 62.6 ms                                                         | 56.5 ms: 1.11x faster                                                             |
| deltablue                  | 2.33 ms                                                         | 2.17 ms: 1.07x faster                                                             |
| spectral_norm              | 69.4 ms                                                         | 64.8 ms: 1.07x faster                                                             |
| meteor_contest             | 74.6 ms                                                         | 69.8 ms: 1.07x faster                                                             |
| scimark_lu                 | 60.2 ms                                                         | 57.8 ms: 1.04x faster                                                             |
| python_startup_no_site     | 19.7 ms                                                         | 19.0 ms: 1.03x faster                                                             |
| bench_mp_pool              | 90.6 ms                                                         | 88.6 ms: 1.02x faster                                                             |
| regex_dna                  | 114 ms                                                          | 117 ms: 1.03x slower                                                              |
| k_core                     | 1.38 sec                                                        | 1.46 sec: 1.06x slower                                                            |
| gc_traversal               | 1.75 ms                                                         | 2.05 ms: 1.17x slower                                                             |
| connected_components       | 267 ms                                                          | 313 ms: 1.17x slower                                                              |
| shortest_path              | 290 ms                                                          | 348 ms: 1.20x slower                                                              |
| create_gc_cycles           | 1.06 ms                                                         | 1.30 ms: 1.23x slower                                                             |
| many_optionals             | 436 us                                                          | 547 us: 1.25x slower                                                              |
| subparsers                 | 14.8 ms                                                         | 29.7 ms: 2.01x slower                                                             |
| Geometric mean             | (ref)                                                           | 1.34x faster                                                                      |
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20251101-3.15.0a1+-2f60b8f-JIT/bm-20251101-pythonperf1_win32-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.342x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.26x
- 95% likely to have a speedup of 1.25x
- 99% likely to have a speedup of 1.22x

# Memory
- memory change: unknown