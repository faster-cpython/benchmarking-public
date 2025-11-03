# Results vs. 3.13.0

- fork: python
- ref: 2f60b8f02fe7cb83dd58
- machine: windows-amd64
- commit hash: 2f60b8f
- commit date: 2025-11-01
- overall geometric mean: 1.173x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20251101-pythonperf1_win32-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 250 ms                                                          | 213 ms: 1.17x faster                                                              |
| docutils       | 1.78 sec                                                        | 2.70 sec: 1.52x slower                                                            |
| html5lib       | 47.5 ms                                                         | 38.4 ms: 1.24x faster                                                             |
| sphinx         | 719 ms                                                          | 630 ms: 1.14x faster                                                              |
| Geometric mean | (ref)                                                           | 1.02x faster                                                                      |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20251101-pythonperf1_win32-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|----------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| asyncio_websockets         | 363 ms                                                          | 143 ms: 2.54x faster                                                              |
| async_tree_io_tg           | 494 ms                                                          | 313 ms: 1.58x faster                                                              |
| async_tree_io              | 526 ms                                                          | 332 ms: 1.58x faster                                                              |
| async_tree_memoization_tg  | 282 ms                                                          | 181 ms: 1.56x faster                                                              |
| async_tree_none_tg         | 214 ms                                                          | 140 ms: 1.53x faster                                                              |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 305 ms: 1.49x faster                                                              |
| async_tree_memoization     | 297 ms                                                          | 199 ms: 1.49x faster                                                              |
| async_tree_none            | 245 ms                                                          | 165 ms: 1.48x faster                                                              |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 331 ms: 1.46x faster                                                              |
| coroutines                 | 16.2 ms                                                         | 14.9 ms: 1.09x faster                                                             |
| async_generators           | 270 ms                                                          | 256 ms: 1.05x faster                                                              |
| Geometric mean             | (ref)                                                           | 1.50x faster                                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20251101-pythonperf1_win32-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| pidigits       | 201 ms                                                          | 135 ms: 1.49x faster                                                              |
| float          | 54.6 ms                                                         | 44.1 ms: 1.24x faster                                                             |
| nbody          | 80.0 ms                                                         | 76.7 ms: 1.04x faster                                                             |
| Geometric mean | (ref)                                                           | 1.24x faster                                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20251101-pythonperf1_win32-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_v8       | 16.8 ms                                                         | 13.2 ms: 1.27x faster                                                             |
| regex_effbot   | 1.80 ms                                                         | 1.53 ms: 1.18x faster                                                             |
| regex_compile  | 101 ms                                                          | 88.1 ms: 1.15x faster                                                             |
| Geometric mean | (ref)                                                           | 1.14x faster                                                                      |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20251101-pythonperf1_win32-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|----------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| json_loads           | 21.6 us                                                         | 15.6 us: 1.39x faster                                                             |
| json_dumps           | 7.30 ms                                                         | 5.95 ms: 1.23x faster                                                             |
| xml_etree_parse      | 107 ms                                                          | 89.0 ms: 1.21x faster                                                             |
| unpickle_pure_python | 160 us                                                          | 148 us: 1.08x faster                                                              |
| xml_etree_iterparse  | 62.6 ms                                                         | 60.4 ms: 1.04x faster                                                             |
| pickle_pure_python   | 231 us                                                          | 224 us: 1.03x faster                                                              |
| xml_etree_process    | 44.2 ms                                                         | 43.1 ms: 1.03x faster                                                             |
| xml_etree_generate   | 61.4 ms                                                         | 60.4 ms: 1.02x faster                                                             |
| tomli_loads          | 1.71 sec                                                        | 2.26 sec: 1.32x slower                                                            |
| Geometric mean       | (ref)                                                           | 1.07x faster                                                                      |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20251101-pythonperf1_win32-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup         | 28.3 ms                                                         | 25.2 ms: 1.12x faster                                                             |
| python_startup_no_site | 19.7 ms                                                         | 19.0 ms: 1.04x faster                                                             |
| Geometric mean         | (ref)                                                           | 1.08x faster                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20251101-pythonperf1_win32-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|-----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| genshi_xml      | 50.1 ms                                                         | 38.0 ms: 1.32x faster                                                             |
| genshi_text     | 21.5 ms                                                         | 18.4 ms: 1.17x faster                                                             |
| django_template | 29.8 ms                                                         | 25.8 ms: 1.15x faster                                                             |
| mako            | 7.09 ms                                                         | 9.61 ms: 1.36x slower                                                             |
| Geometric mean  | (ref)                                                           | 1.07x faster                                                                      |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20251101-pythonperf1_win32-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|----------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| thrift                     | 9.98 ms                                                         | 562 us: 17.75x faster                                                             |
| coverage                   | 324 ms                                                          | 66.3 ms: 4.88x faster                                                             |
| pathlib                    | 82.9 ms                                                         | 28.8 ms: 2.87x faster                                                             |
| asyncio_websockets         | 363 ms                                                          | 143 ms: 2.54x faster                                                              |
| deepcopy                   | 314 us                                                          | 182 us: 1.73x faster                                                              |
| mdp                        | 1.62 sec                                                        | 973 ms: 1.67x faster                                                              |
| async_tree_io_tg           | 494 ms                                                          | 313 ms: 1.58x faster                                                              |
| async_tree_io              | 526 ms                                                          | 332 ms: 1.58x faster                                                              |
| async_tree_memoization_tg  | 282 ms                                                          | 181 ms: 1.56x faster                                                              |
| async_tree_none_tg         | 214 ms                                                          | 140 ms: 1.53x faster                                                              |
| gc_traversal               | 1.75 ms                                                         | 1.15 ms: 1.52x faster                                                             |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 305 ms: 1.49x faster                                                              |
| pidigits                   | 201 ms                                                          | 135 ms: 1.49x faster                                                              |
| async_tree_memoization     | 297 ms                                                          | 199 ms: 1.49x faster                                                              |
| async_tree_none            | 245 ms                                                          | 165 ms: 1.48x faster                                                              |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 331 ms: 1.46x faster                                                              |
| deepcopy_reduce            | 2.92 us                                                         | 2.00 us: 1.46x faster                                                             |
| telco                      | 6.96 ms                                                         | 4.85 ms: 1.43x faster                                                             |
| json                       | 4.27 ms                                                         | 3.03 ms: 1.41x faster                                                             |
| sqlite_synth               | 1.95 us                                                         | 1.40 us: 1.40x faster                                                             |
| json_loads                 | 21.6 us                                                         | 15.6 us: 1.39x faster                                                             |
| deepcopy_memo              | 25.4 us                                                         | 18.9 us: 1.35x faster                                                             |
| genshi_xml                 | 50.1 ms                                                         | 38.0 ms: 1.32x faster                                                             |
| go                         | 109 ms                                                          | 85.6 ms: 1.27x faster                                                             |
| pycparser                  | 872 ms                                                          | 686 ms: 1.27x faster                                                              |
| regex_v8                   | 16.8 ms                                                         | 13.2 ms: 1.27x faster                                                             |
| logging_format             | 8.72 us                                                         | 6.92 us: 1.26x faster                                                             |
| bench_mp_pool              | 90.6 ms                                                         | 72.3 ms: 1.25x faster                                                             |
| logging_simple             | 7.99 us                                                         | 6.40 us: 1.25x faster                                                             |
| float                      | 54.6 ms                                                         | 44.1 ms: 1.24x faster                                                             |
| html5lib                   | 47.5 ms                                                         | 38.4 ms: 1.24x faster                                                             |
| sympy_expand               | 373 ms                                                          | 303 ms: 1.23x faster                                                              |
| json_dumps                 | 7.30 ms                                                         | 5.95 ms: 1.23x faster                                                             |
| dulwich_log                | 48.8 ms                                                         | 39.8 ms: 1.23x faster                                                             |
| pprint_safe_repr           | 648 ms                                                          | 535 ms: 1.21x faster                                                              |
| xml_etree_parse            | 107 ms                                                          | 89.0 ms: 1.21x faster                                                             |
| sympy_str                  | 212 ms                                                          | 178 ms: 1.19x faster                                                              |
| regex_effbot               | 1.80 ms                                                         | 1.53 ms: 1.18x faster                                                             |
| 2to3                       | 250 ms                                                          | 213 ms: 1.17x faster                                                              |
| genshi_text                | 21.5 ms                                                         | 18.4 ms: 1.17x faster                                                             |
| sympy_sum                  | 106 ms                                                          | 91.5 ms: 1.15x faster                                                             |
| django_template            | 29.8 ms                                                         | 25.8 ms: 1.15x faster                                                             |
| regex_compile              | 101 ms                                                          | 88.1 ms: 1.15x faster                                                             |
| sphinx                     | 719 ms                                                          | 630 ms: 1.14x faster                                                              |
| typing_runtime_protocols   | 138 us                                                          | 121 us: 1.14x faster                                                              |
| pylint                     | 227 ms                                                          | 202 ms: 1.12x faster                                                              |
| python_startup             | 28.3 ms                                                         | 25.2 ms: 1.12x faster                                                             |
| chaos                      | 50.2 ms                                                         | 44.7 ms: 1.12x faster                                                             |
| sympy_integrate            | 15.0 ms                                                         | 13.7 ms: 1.10x faster                                                             |
| coroutines                 | 16.2 ms                                                         | 14.9 ms: 1.09x faster                                                             |
| comprehensions             | 12.5 us                                                         | 11.5 us: 1.09x faster                                                             |
| unpickle_pure_python       | 160 us                                                          | 148 us: 1.08x faster                                                              |
| pyflate                    | 320 ms                                                          | 297 ms: 1.08x faster                                                              |
| scimark_fft                | 205 ms                                                          | 192 ms: 1.07x faster                                                              |
| async_generators           | 270 ms                                                          | 256 ms: 1.05x faster                                                              |
| create_gc_cycles           | 1.06 ms                                                         | 1.01 ms: 1.04x faster                                                             |
| nbody                      | 80.0 ms                                                         | 76.7 ms: 1.04x faster                                                             |
| richards                   | 32.7 ms                                                         | 31.3 ms: 1.04x faster                                                             |
| python_startup_no_site     | 19.7 ms                                                         | 19.0 ms: 1.04x faster                                                             |
| xml_etree_iterparse        | 62.6 ms                                                         | 60.4 ms: 1.04x faster                                                             |
| logging_silent             | 60.3 ns                                                         | 58.3 ns: 1.04x faster                                                             |
| pickle_pure_python         | 231 us                                                          | 224 us: 1.03x faster                                                              |
| generators                 | 21.8 ms                                                         | 21.1 ms: 1.03x faster                                                             |
| xml_etree_process          | 44.2 ms                                                         | 43.1 ms: 1.03x faster                                                             |
| xml_etree_generate         | 61.4 ms                                                         | 60.4 ms: 1.02x faster                                                             |
| scimark_sor                | 85.9 ms                                                         | 84.8 ms: 1.01x faster                                                             |
| crypto_pyaes               | 56.9 ms                                                         | 56.5 ms: 1.01x faster                                                             |
| spectral_norm              | 69.4 ms                                                         | 69.1 ms: 1.00x faster                                                             |
| raytrace                   | 201 ms                                                          | 203 ms: 1.01x slower                                                              |
| scimark_monte_carlo        | 47.7 ms                                                         | 49.3 ms: 1.03x slower                                                             |
| scimark_sparse_mat_mult    | 2.84 ms                                                         | 2.94 ms: 1.04x slower                                                             |
| scimark_lu                 | 60.2 ms                                                         | 63.2 ms: 1.05x slower                                                             |
| meteor_contest             | 74.6 ms                                                         | 85.1 ms: 1.14x slower                                                             |
| pprint_pformat             | 1.33 sec                                                        | 1.54 sec: 1.16x slower                                                            |
| tomli_loads                | 1.71 sec                                                        | 2.26 sec: 1.32x slower                                                            |
| mako                       | 7.09 ms                                                         | 9.61 ms: 1.36x slower                                                             |
| many_optionals             | 436 us                                                          | 596 us: 1.37x slower                                                              |
| docutils                   | 1.78 sec                                                        | 2.70 sec: 1.52x slower                                                            |
| bpe_tokeniser              | 3.46 sec                                                        | 5.28 sec: 1.53x slower                                                            |
| k_core                     | 1.38 sec                                                        | 2.62 sec: 1.90x slower                                                            |
| shortest_path              | 290 ms                                                          | 632 ms: 2.18x slower                                                              |
| connected_components       | 267 ms                                                          | 600 ms: 2.25x slower                                                              |
| subparsers                 | 14.8 ms                                                         | 34.9 ms: 2.37x slower                                                             |
| Geometric mean             | (ref)                                                           | 1.17x faster                                                                      |

Benchmark hidden because not significant (7): deltablue, richards_super, regex_dna, hexiom, nqueens, fannkuch, bench_thread_pool
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20251101-3.15.0a1+-2f60b8f-NOGIL/bm-20251101-pythonperf1_win32-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.173x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.07x
- 95% likely to have a speedup of 1.06x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: unknown