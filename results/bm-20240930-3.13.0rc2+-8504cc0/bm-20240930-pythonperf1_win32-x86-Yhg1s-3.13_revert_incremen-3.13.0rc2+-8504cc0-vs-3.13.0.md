# Results vs. 3.13.0

- fork: Yhg1s
- ref: 3.13_revert_incremen
- machine: windows-x86
- commit hash: 8504cc0
- commit date: 2024-09-30
- overall geometric mean: 1.040x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240930-pythonperf1_win32-x86-Yhg1s-3.13_revert_incremen-3.13.0rc2+-8504cc0 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 255 ms                                                          | 243 ms: 1.05x faster                                                            |
| chameleon      | 6.24 ms                                                         | 5.73 ms: 1.09x faster                                                           |
| docutils       | 1.80 sec                                                        | 1.79 sec: 1.00x faster                                                          |
| html5lib       | 47.1 ms                                                         | 45.7 ms: 1.03x faster                                                           |
| Geometric mean | (ref)                                                           | 1.04x faster                                                                    |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240930-pythonperf1_win32-x86-Yhg1s-3.13_revert_incremen-3.13.0rc2+-8504cc0 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_memoization     | 302 ms                                                          | 290 ms: 1.04x faster                                                            |
| async_tree_cpu_io_mixed_tg | 469 ms                                                          | 454 ms: 1.03x faster                                                            |
| coroutines                 | 16.1 ms                                                         | 15.7 ms: 1.03x faster                                                           |
| async_tree_io              | 530 ms                                                          | 515 ms: 1.03x faster                                                            |
| async_tree_none            | 245 ms                                                          | 238 ms: 1.03x faster                                                            |
| async_tree_memoization_tg  | 287 ms                                                          | 280 ms: 1.02x faster                                                            |
| async_tree_cpu_io_mixed    | 490 ms                                                          | 480 ms: 1.02x faster                                                            |
| async_tree_io_tg           | 499 ms                                                          | 490 ms: 1.02x faster                                                            |
| async_tree_none_tg         | 216 ms                                                          | 214 ms: 1.01x faster                                                            |
| async_generators           | 267 ms                                                          | 274 ms: 1.03x slower                                                            |
| Geometric mean             | (ref)                                                           | 1.02x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240930-pythonperf1_win32-x86-Yhg1s-3.13_revert_incremen-3.13.0rc2+-8504cc0 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 81.4 ms                                                         | 75.5 ms: 1.08x faster                                                           |
| pidigits       | 204 ms                                                          | 196 ms: 1.04x faster                                                            |
| float          | 56.4 ms                                                         | 54.8 ms: 1.03x faster                                                           |
| Geometric mean | (ref)                                                           | 1.05x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240930-pythonperf1_win32-x86-Yhg1s-3.13_revert_incremen-3.13.0rc2+-8504cc0 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 101 ms                                                          | 100 ms: 1.01x faster                                                            |
| regex_v8       | 15.5 ms                                                         | 15.8 ms: 1.02x slower                                                           |
| regex_effbot   | 1.82 ms                                                         | 1.91 ms: 1.05x slower                                                           |
| regex_dna      | 112 ms                                                          | 119 ms: 1.06x slower                                                            |
| Geometric mean | (ref)                                                           | 1.03x slower                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240930-pythonperf1_win32-x86-Yhg1s-3.13_revert_incremen-3.13.0rc2+-8504cc0 |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| unpickle_pure_python | 162 us                                                          | 150 us: 1.07x faster                                                            |
| json_dumps           | 7.53 ms                                                         | 7.06 ms: 1.07x faster                                                           |
| pickle_pure_python   | 239 us                                                          | 225 us: 1.06x faster                                                            |
| json_loads           | 21.7 us                                                         | 20.9 us: 1.04x faster                                                           |
| xml_etree_generate   | 61.9 ms                                                         | 60.1 ms: 1.03x faster                                                           |
| tomli_loads          | 1.74 sec                                                        | 1.69 sec: 1.03x faster                                                          |
| xml_etree_process    | 44.6 ms                                                         | 43.9 ms: 1.02x faster                                                           |
| xml_etree_iterparse  | 61.3 ms                                                         | 62.0 ms: 1.01x slower                                                           |
| xml_etree_parse      | 102 ms                                                          | 106 ms: 1.03x slower                                                            |
| Geometric mean       | (ref)                                                           | 1.03x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240930-pythonperf1_win32-x86-Yhg1s-3.13_revert_incremen-3.13.0rc2+-8504cc0 |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 28.3 ms                                                         | 24.1 ms: 1.17x faster                                                           |
| python_startup_no_site | 20.2 ms                                                         | 19.9 ms: 1.01x faster                                                           |
| Geometric mean         | (ref)                                                           | 1.09x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240930-pythonperf1_win32-x86-Yhg1s-3.13_revert_incremen-3.13.0rc2+-8504cc0 |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_xml      | 49.0 ms                                                         | 44.4 ms: 1.10x faster                                                           |
| genshi_text     | 21.7 ms                                                         | 20.3 ms: 1.07x faster                                                           |
| django_template | 32.0 ms                                                         | 30.1 ms: 1.06x faster                                                           |
| mako            | 7.02 ms                                                         | 6.90 ms: 1.02x faster                                                           |
| Geometric mean  | (ref)                                                           | 1.06x faster                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240930-pythonperf1_win32-x86-Yhg1s-3.13_revert_incremen-3.13.0rc2+-8504cc0 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| create_gc_cycles           | 1.08 ms                                                         | 691 us: 1.57x faster                                                            |
| bench_mp_pool              | 93.6 ms                                                         | 74.1 ms: 1.26x faster                                                           |
| gc_traversal               | 1.76 ms                                                         | 1.44 ms: 1.22x faster                                                           |
| python_startup             | 28.3 ms                                                         | 24.1 ms: 1.17x faster                                                           |
| pprint_safe_repr           | 658 ms                                                          | 591 ms: 1.11x faster                                                            |
| genshi_xml                 | 49.0 ms                                                         | 44.4 ms: 1.10x faster                                                           |
| deepcopy_reduce            | 2.94 us                                                         | 2.67 us: 1.10x faster                                                           |
| pprint_pformat             | 1.32 sec                                                        | 1.21 sec: 1.09x faster                                                          |
| chameleon                  | 6.24 ms                                                         | 5.73 ms: 1.09x faster                                                           |
| nqueens                    | 75.1 ms                                                         | 69.0 ms: 1.09x faster                                                           |
| deepcopy                   | 311 us                                                          | 287 us: 1.08x faster                                                            |
| comprehensions             | 13.1 us                                                         | 12.2 us: 1.08x faster                                                           |
| nbody                      | 81.4 ms                                                         | 75.5 ms: 1.08x faster                                                           |
| unpickle_pure_python       | 162 us                                                          | 150 us: 1.07x faster                                                            |
| genshi_text                | 21.7 ms                                                         | 20.3 ms: 1.07x faster                                                           |
| raytrace                   | 203 ms                                                          | 189 ms: 1.07x faster                                                            |
| logging_silent             | 62.4 ns                                                         | 58.4 ns: 1.07x faster                                                           |
| json_dumps                 | 7.53 ms                                                         | 7.06 ms: 1.07x faster                                                           |
| sqlglot_normalize          | 223 ms                                                          | 209 ms: 1.06x faster                                                            |
| django_template            | 32.0 ms                                                         | 30.1 ms: 1.06x faster                                                           |
| pickle_pure_python         | 239 us                                                          | 225 us: 1.06x faster                                                            |
| deepcopy_memo              | 26.2 us                                                         | 24.7 us: 1.06x faster                                                           |
| sqlglot_parse              | 1.02 ms                                                         | 962 us: 1.06x faster                                                            |
| bench_thread_pool          | 1.04 ms                                                         | 983 us: 1.06x faster                                                            |
| sqlglot_transpile          | 1.26 ms                                                         | 1.19 ms: 1.06x faster                                                           |
| deltablue                  | 2.35 ms                                                         | 2.23 ms: 1.05x faster                                                           |
| hexiom                     | 4.60 ms                                                         | 4.38 ms: 1.05x faster                                                           |
| 2to3                       | 255 ms                                                          | 243 ms: 1.05x faster                                                            |
| meteor_contest             | 78.1 ms                                                         | 74.8 ms: 1.05x faster                                                           |
| scimark_monte_carlo        | 48.7 ms                                                         | 46.6 ms: 1.04x faster                                                           |
| chaos                      | 49.4 ms                                                         | 47.3 ms: 1.04x faster                                                           |
| async_tree_memoization     | 302 ms                                                          | 290 ms: 1.04x faster                                                            |
| pycparser                  | 869 ms                                                          | 834 ms: 1.04x faster                                                            |
| mdp                        | 1.70 sec                                                        | 1.63 sec: 1.04x faster                                                          |
| logging_simple             | 7.89 us                                                         | 7.58 us: 1.04x faster                                                           |
| go                         | 111 ms                                                          | 106 ms: 1.04x faster                                                            |
| logging_format             | 8.59 us                                                         | 8.26 us: 1.04x faster                                                           |
| fannkuch                   | 288 ms                                                          | 277 ms: 1.04x faster                                                            |
| pidigits                   | 204 ms                                                          | 196 ms: 1.04x faster                                                            |
| json                       | 4.40 ms                                                         | 4.23 ms: 1.04x faster                                                           |
| json_loads                 | 21.7 us                                                         | 20.9 us: 1.04x faster                                                           |
| sqlglot_optimize           | 42.4 ms                                                         | 41.0 ms: 1.04x faster                                                           |
| async_tree_cpu_io_mixed_tg | 469 ms                                                          | 454 ms: 1.03x faster                                                            |
| richards                   | 33.4 ms                                                         | 32.3 ms: 1.03x faster                                                           |
| html5lib                   | 47.1 ms                                                         | 45.7 ms: 1.03x faster                                                           |
| xml_etree_generate         | 61.9 ms                                                         | 60.1 ms: 1.03x faster                                                           |
| coroutines                 | 16.1 ms                                                         | 15.7 ms: 1.03x faster                                                           |
| async_tree_io              | 530 ms                                                          | 515 ms: 1.03x faster                                                            |
| float                      | 56.4 ms                                                         | 54.8 ms: 1.03x faster                                                           |
| tomli_loads                | 1.74 sec                                                        | 1.69 sec: 1.03x faster                                                          |
| async_tree_none            | 245 ms                                                          | 238 ms: 1.03x faster                                                            |
| async_tree_memoization_tg  | 287 ms                                                          | 280 ms: 1.02x faster                                                            |
| sympy_integrate            | 15.2 ms                                                         | 14.9 ms: 1.02x faster                                                           |
| dulwich_log                | 50.2 ms                                                         | 49.1 ms: 1.02x faster                                                           |
| sympy_sum                  | 108 ms                                                          | 106 ms: 1.02x faster                                                            |
| scimark_sparse_mat_mult    | 2.88 ms                                                         | 2.82 ms: 1.02x faster                                                           |
| async_tree_cpu_io_mixed    | 490 ms                                                          | 480 ms: 1.02x faster                                                            |
| async_tree_io_tg           | 499 ms                                                          | 490 ms: 1.02x faster                                                            |
| thrift                     | 10.3 ms                                                         | 10.1 ms: 1.02x faster                                                           |
| coverage                   | 326 ms                                                          | 320 ms: 1.02x faster                                                            |
| scimark_fft                | 204 ms                                                          | 200 ms: 1.02x faster                                                            |
| spectral_norm              | 70.0 ms                                                         | 68.8 ms: 1.02x faster                                                           |
| typing_runtime_protocols   | 141 us                                                          | 138 us: 1.02x faster                                                            |
| mako                       | 7.02 ms                                                         | 6.90 ms: 1.02x faster                                                           |
| xml_etree_process          | 44.6 ms                                                         | 43.9 ms: 1.02x faster                                                           |
| crypto_pyaes               | 56.6 ms                                                         | 55.8 ms: 1.02x faster                                                           |
| richards_super             | 37.0 ms                                                         | 36.5 ms: 1.01x faster                                                           |
| scimark_sor                | 85.8 ms                                                         | 84.6 ms: 1.01x faster                                                           |
| python_startup_no_site     | 20.2 ms                                                         | 19.9 ms: 1.01x faster                                                           |
| async_tree_none_tg         | 216 ms                                                          | 214 ms: 1.01x faster                                                            |
| regex_compile              | 101 ms                                                          | 100 ms: 1.01x faster                                                            |
| sympy_str                  | 214 ms                                                          | 212 ms: 1.01x faster                                                            |
| sympy_expand               | 377 ms                                                          | 374 ms: 1.01x faster                                                            |
| generators                 | 21.5 ms                                                         | 21.4 ms: 1.01x faster                                                           |
| pathlib                    | 89.1 ms                                                         | 88.6 ms: 1.01x faster                                                           |
| docutils                   | 1.80 sec                                                        | 1.79 sec: 1.00x faster                                                          |
| scimark_lu                 | 60.7 ms                                                         | 61.0 ms: 1.01x slower                                                           |
| xml_etree_iterparse        | 61.3 ms                                                         | 62.0 ms: 1.01x slower                                                           |
| regex_v8                   | 15.5 ms                                                         | 15.8 ms: 1.02x slower                                                           |
| async_generators           | 267 ms                                                          | 274 ms: 1.03x slower                                                            |
| xml_etree_parse            | 102 ms                                                          | 106 ms: 1.03x slower                                                            |
| telco                      | 6.27 ms                                                         | 6.55 ms: 1.04x slower                                                           |
| regex_effbot               | 1.82 ms                                                         | 1.91 ms: 1.05x slower                                                           |
| regex_dna                  | 112 ms                                                          | 119 ms: 1.06x slower                                                            |
| Geometric mean             | (ref)                                                           | 1.04x faster                                                                    |

Benchmark hidden because not significant (3): pylint, tornado_http, pyflate
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: asyncio_websockets, bpe_tokeniser, connected_components, gevent_hub, k_core, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (10) of results/bm-20240930-3.13.0rc2+-8504cc0/bm-20240930-pythonperf1_win32-x86-Yhg1s-3.13_revert_incremen-3.13.0rc2+-8504cc0.json: asyncio_tcp, asyncio_tcp_ssl, flaskblogging, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.040x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: unknown