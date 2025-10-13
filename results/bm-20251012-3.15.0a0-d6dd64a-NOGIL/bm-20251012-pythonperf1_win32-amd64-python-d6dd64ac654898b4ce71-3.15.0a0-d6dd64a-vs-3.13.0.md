# Results vs. 3.13.0

- fork: python
- ref: d6dd64ac654898b4ce71
- machine: windows-amd64
- commit hash: d6dd64a
- commit date: 2025-10-12
- overall geometric mean: 1.149x faster
- HPT reliability: 99.98%
- HPT 99th percentile: 1.02x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20251012-pythonperf1_win32-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 250 ms                                                          | 222 ms: 1.13x faster                                                             |
| docutils       | 1.78 sec                                                        | 2.84 sec: 1.60x slower                                                           |
| html5lib       | 47.5 ms                                                         | 40.3 ms: 1.18x faster                                                            |
| sphinx         | 719 ms                                                          | 665 ms: 1.08x faster                                                             |
| Geometric mean | (ref)                                                           | 1.03x slower                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20251012-pythonperf1_win32-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| asyncio_websockets         | 363 ms                                                          | 137 ms: 2.65x faster                                                             |
| async_tree_io_tg           | 494 ms                                                          | 321 ms: 1.54x faster                                                             |
| async_tree_memoization_tg  | 282 ms                                                          | 185 ms: 1.52x faster                                                             |
| async_tree_io              | 526 ms                                                          | 346 ms: 1.52x faster                                                             |
| async_tree_none_tg         | 214 ms                                                          | 143 ms: 1.50x faster                                                             |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 325 ms: 1.49x faster                                                             |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 307 ms: 1.49x faster                                                             |
| async_tree_none            | 245 ms                                                          | 167 ms: 1.46x faster                                                             |
| async_tree_memoization     | 297 ms                                                          | 204 ms: 1.46x faster                                                             |
| coroutines                 | 16.2 ms                                                         | 14.6 ms: 1.11x faster                                                            |
| async_generators           | 270 ms                                                          | 258 ms: 1.04x faster                                                             |
| Geometric mean             | (ref)                                                           | 1.49x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20251012-pythonperf1_win32-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pidigits       | 201 ms                                                          | 136 ms: 1.47x faster                                                             |
| float          | 54.6 ms                                                         | 45.9 ms: 1.19x faster                                                            |
| nbody          | 80.0 ms                                                         | 78.1 ms: 1.02x faster                                                            |
| Geometric mean | (ref)                                                           | 1.21x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20251012-pythonperf1_win32-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_v8       | 16.8 ms                                                         | 13.6 ms: 1.23x faster                                                            |
| regex_effbot   | 1.80 ms                                                         | 1.56 ms: 1.16x faster                                                            |
| regex_compile  | 101 ms                                                          | 90.0 ms: 1.12x faster                                                            |
| regex_dna      | 114 ms                                                          | 116 ms: 1.02x slower                                                             |
| Geometric mean | (ref)                                                           | 1.12x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20251012-pythonperf1_win32-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| json_loads           | 21.6 us                                                         | 16.1 us: 1.34x faster                                                            |
| json_dumps           | 7.30 ms                                                         | 6.05 ms: 1.21x faster                                                            |
| xml_etree_parse      | 107 ms                                                          | 92.2 ms: 1.16x faster                                                            |
| unpickle_pure_python | 160 us                                                          | 150 us: 1.07x faster                                                             |
| xml_etree_iterparse  | 62.6 ms                                                         | 59.3 ms: 1.05x faster                                                            |
| xml_etree_process    | 44.2 ms                                                         | 43.2 ms: 1.02x faster                                                            |
| pickle_pure_python   | 231 us                                                          | 226 us: 1.02x faster                                                             |
| xml_etree_generate   | 61.4 ms                                                         | 61.9 ms: 1.01x slower                                                            |
| tomli_loads          | 1.71 sec                                                        | 2.31 sec: 1.34x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.06x faster                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20251012-pythonperf1_win32-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup | 28.3 ms                                                         | 25.8 ms: 1.10x faster                                                            |
| Geometric mean | (ref)                                                           | 1.05x faster                                                                     |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20251012-pythonperf1_win32-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| genshi_xml      | 50.1 ms                                                         | 37.8 ms: 1.33x faster                                                            |
| genshi_text     | 21.5 ms                                                         | 18.5 ms: 1.16x faster                                                            |
| django_template | 29.8 ms                                                         | 27.2 ms: 1.10x faster                                                            |
| mako            | 7.09 ms                                                         | 9.66 ms: 1.36x slower                                                            |
| Geometric mean  | (ref)                                                           | 1.06x faster                                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20251012-pythonperf1_win32-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| thrift                     | 9.98 ms                                                         | 560 us: 17.80x faster                                                            |
| coverage                   | 324 ms                                                          | 66.2 ms: 4.89x faster                                                            |
| pathlib                    | 82.9 ms                                                         | 28.6 ms: 2.90x faster                                                            |
| asyncio_websockets         | 363 ms                                                          | 137 ms: 2.65x faster                                                             |
| deepcopy                   | 314 us                                                          | 186 us: 1.69x faster                                                             |
| async_tree_io_tg           | 494 ms                                                          | 321 ms: 1.54x faster                                                             |
| mdp                        | 1.62 sec                                                        | 1.06 sec: 1.53x faster                                                           |
| async_tree_memoization_tg  | 282 ms                                                          | 185 ms: 1.52x faster                                                             |
| async_tree_io              | 526 ms                                                          | 346 ms: 1.52x faster                                                             |
| async_tree_none_tg         | 214 ms                                                          | 143 ms: 1.50x faster                                                             |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 325 ms: 1.49x faster                                                             |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 307 ms: 1.49x faster                                                             |
| pidigits                   | 201 ms                                                          | 136 ms: 1.47x faster                                                             |
| async_tree_none            | 245 ms                                                          | 167 ms: 1.46x faster                                                             |
| async_tree_memoization     | 297 ms                                                          | 204 ms: 1.46x faster                                                             |
| deepcopy_reduce            | 2.92 us                                                         | 2.01 us: 1.45x faster                                                            |
| sqlite_synth               | 1.95 us                                                         | 1.36 us: 1.43x faster                                                            |
| gc_traversal               | 1.75 ms                                                         | 1.23 ms: 1.43x faster                                                            |
| json                       | 4.27 ms                                                         | 3.06 ms: 1.39x faster                                                            |
| telco                      | 6.96 ms                                                         | 5.00 ms: 1.39x faster                                                            |
| deepcopy_memo              | 25.4 us                                                         | 18.7 us: 1.36x faster                                                            |
| json_loads                 | 21.6 us                                                         | 16.1 us: 1.34x faster                                                            |
| genshi_xml                 | 50.1 ms                                                         | 37.8 ms: 1.33x faster                                                            |
| pycparser                  | 872 ms                                                          | 693 ms: 1.26x faster                                                             |
| logging_format             | 8.72 us                                                         | 7.00 us: 1.25x faster                                                            |
| regex_v8                   | 16.8 ms                                                         | 13.6 ms: 1.23x faster                                                            |
| logging_simple             | 7.99 us                                                         | 6.50 us: 1.23x faster                                                            |
| bench_mp_pool              | 90.6 ms                                                         | 74.4 ms: 1.22x faster                                                            |
| pprint_safe_repr           | 648 ms                                                          | 536 ms: 1.21x faster                                                             |
| go                         | 109 ms                                                          | 89.9 ms: 1.21x faster                                                            |
| json_dumps                 | 7.30 ms                                                         | 6.05 ms: 1.21x faster                                                            |
| sympy_expand               | 373 ms                                                          | 313 ms: 1.19x faster                                                             |
| float                      | 54.6 ms                                                         | 45.9 ms: 1.19x faster                                                            |
| dulwich_log                | 48.8 ms                                                         | 41.4 ms: 1.18x faster                                                            |
| html5lib                   | 47.5 ms                                                         | 40.3 ms: 1.18x faster                                                            |
| xml_etree_parse            | 107 ms                                                          | 92.2 ms: 1.16x faster                                                            |
| genshi_text                | 21.5 ms                                                         | 18.5 ms: 1.16x faster                                                            |
| sympy_str                  | 212 ms                                                          | 183 ms: 1.16x faster                                                             |
| regex_effbot               | 1.80 ms                                                         | 1.56 ms: 1.16x faster                                                            |
| 2to3                       | 250 ms                                                          | 222 ms: 1.13x faster                                                             |
| regex_compile              | 101 ms                                                          | 90.0 ms: 1.12x faster                                                            |
| pylint                     | 227 ms                                                          | 202 ms: 1.12x faster                                                             |
| sympy_sum                  | 106 ms                                                          | 94.8 ms: 1.11x faster                                                            |
| coroutines                 | 16.2 ms                                                         | 14.6 ms: 1.11x faster                                                            |
| chaos                      | 50.2 ms                                                         | 45.4 ms: 1.11x faster                                                            |
| python_startup             | 28.3 ms                                                         | 25.8 ms: 1.10x faster                                                            |
| django_template            | 29.8 ms                                                         | 27.2 ms: 1.10x faster                                                            |
| comprehensions             | 12.5 us                                                         | 11.5 us: 1.08x faster                                                            |
| sympy_integrate            | 15.0 ms                                                         | 13.8 ms: 1.08x faster                                                            |
| sphinx                     | 719 ms                                                          | 665 ms: 1.08x faster                                                             |
| unpickle_pure_python       | 160 us                                                          | 150 us: 1.07x faster                                                             |
| typing_runtime_protocols   | 138 us                                                          | 130 us: 1.06x faster                                                             |
| xml_etree_iterparse        | 62.6 ms                                                         | 59.3 ms: 1.05x faster                                                            |
| scimark_fft                | 205 ms                                                          | 194 ms: 1.05x faster                                                             |
| async_generators           | 270 ms                                                          | 258 ms: 1.04x faster                                                             |
| pyflate                    | 320 ms                                                          | 307 ms: 1.04x faster                                                             |
| nbody                      | 80.0 ms                                                         | 78.1 ms: 1.02x faster                                                            |
| generators                 | 21.8 ms                                                         | 21.3 ms: 1.02x faster                                                            |
| xml_etree_process          | 44.2 ms                                                         | 43.2 ms: 1.02x faster                                                            |
| pickle_pure_python         | 231 us                                                          | 226 us: 1.02x faster                                                             |
| crypto_pyaes               | 56.9 ms                                                         | 55.8 ms: 1.02x faster                                                            |
| create_gc_cycles           | 1.06 ms                                                         | 1.04 ms: 1.02x faster                                                            |
| logging_silent             | 60.3 ns                                                         | 59.6 ns: 1.01x faster                                                            |
| nqueens                    | 72.1 ms                                                         | 71.3 ms: 1.01x faster                                                            |
| xml_etree_generate         | 61.4 ms                                                         | 61.9 ms: 1.01x slower                                                            |
| scimark_sor                | 85.9 ms                                                         | 86.8 ms: 1.01x slower                                                            |
| richards_super             | 36.7 ms                                                         | 37.2 ms: 1.01x slower                                                            |
| hexiom                     | 4.44 ms                                                         | 4.52 ms: 1.02x slower                                                            |
| fannkuch                   | 299 ms                                                          | 304 ms: 1.02x slower                                                             |
| regex_dna                  | 114 ms                                                          | 116 ms: 1.02x slower                                                             |
| spectral_norm              | 69.4 ms                                                         | 71.2 ms: 1.03x slower                                                            |
| raytrace                   | 201 ms                                                          | 210 ms: 1.04x slower                                                             |
| deltablue                  | 2.33 ms                                                         | 2.44 ms: 1.04x slower                                                            |
| scimark_monte_carlo        | 47.7 ms                                                         | 50.2 ms: 1.05x slower                                                            |
| scimark_sparse_mat_mult    | 2.84 ms                                                         | 3.01 ms: 1.06x slower                                                            |
| scimark_lu                 | 60.2 ms                                                         | 64.0 ms: 1.06x slower                                                            |
| meteor_contest             | 74.6 ms                                                         | 84.3 ms: 1.13x slower                                                            |
| pprint_pformat             | 1.33 sec                                                        | 1.61 sec: 1.21x slower                                                           |
| tomli_loads                | 1.71 sec                                                        | 2.31 sec: 1.34x slower                                                           |
| mako                       | 7.09 ms                                                         | 9.66 ms: 1.36x slower                                                            |
| many_optionals             | 436 us                                                          | 617 us: 1.41x slower                                                             |
| bpe_tokeniser              | 3.46 sec                                                        | 5.41 sec: 1.56x slower                                                           |
| docutils                   | 1.78 sec                                                        | 2.84 sec: 1.60x slower                                                           |
| k_core                     | 1.38 sec                                                        | 2.67 sec: 1.94x slower                                                           |
| shortest_path              | 290 ms                                                          | 647 ms: 2.23x slower                                                             |
| connected_components       | 267 ms                                                          | 623 ms: 2.34x slower                                                             |
| subparsers                 | 14.8 ms                                                         | 34.5 ms: 2.34x slower                                                            |
| Geometric mean             | (ref)                                                           | 1.15x faster                                                                     |

Benchmark hidden because not significant (3): richards, python_startup_no_site, bench_thread_pool
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20251012-3.15.0a0-d6dd64a-NOGIL/bm-20251012-pythonperf1_win32-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.149x faster

# HPT report

- Reliability score: 99.98% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: unknown