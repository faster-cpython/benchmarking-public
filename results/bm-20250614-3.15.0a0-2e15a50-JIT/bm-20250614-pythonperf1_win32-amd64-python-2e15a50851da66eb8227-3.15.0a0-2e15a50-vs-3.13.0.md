# Results vs. 3.13.0

- fork: python
- ref: 2e15a50851da66eb8227
- machine: windows-amd64
- commit hash: 2e15a50
- commit date: 2025-06-14
- overall geometric mean: 1.132x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250614-pythonperf1_win32-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 250 ms                                                          | 286 ms: 1.14x slower                                                             |
| docutils       | 1.78 sec                                                        | 2.11 sec: 1.18x slower                                                           |
| html5lib       | 47.5 ms                                                         | 51.9 ms: 1.09x slower                                                            |
| sphinx         | 719 ms                                                          | 852 ms: 1.19x slower                                                             |
| Geometric mean | (ref)                                                           | 1.15x slower                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250614-pythonperf1_win32-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50 |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| asyncio_websockets         | 363 ms                                                          | 159 ms: 2.29x faster                                                             |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 432 ms: 1.12x faster                                                             |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 430 ms: 1.06x faster                                                             |
| async_tree_none            | 245 ms                                                          | 232 ms: 1.05x faster                                                             |
| async_tree_memoization     | 297 ms                                                          | 285 ms: 1.04x faster                                                             |
| async_tree_memoization_tg  | 282 ms                                                          | 285 ms: 1.01x slower                                                             |
| async_tree_io              | 526 ms                                                          | 532 ms: 1.01x slower                                                             |
| async_tree_none_tg         | 214 ms                                                          | 227 ms: 1.06x slower                                                             |
| async_tree_io_tg           | 494 ms                                                          | 550 ms: 1.11x slower                                                             |
| async_generators           | 270 ms                                                          | 354 ms: 1.31x slower                                                             |
| coroutines                 | 16.2 ms                                                         | 25.6 ms: 1.58x slower                                                            |
| Geometric mean             | (ref)                                                           | 1.02x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250614-pythonperf1_win32-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| nbody          | 80.0 ms                                                         | 56.2 ms: 1.42x faster                                                            |
| pidigits       | 201 ms                                                          | 146 ms: 1.37x faster                                                             |
| float          | 54.6 ms                                                         | 78.1 ms: 1.43x slower                                                            |
| Geometric mean | (ref)                                                           | 1.11x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250614-pythonperf1_win32-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_effbot   | 1.80 ms                                                         | 1.74 ms: 1.03x faster                                                            |
| regex_dna      | 114 ms                                                          | 116 ms: 1.02x slower                                                             |
| regex_compile  | 101 ms                                                          | 120 ms: 1.19x slower                                                             |
| Geometric mean | (ref)                                                           | 1.04x slower                                                                     |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250614-pythonperf1_win32-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50 |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| tomli_loads          | 1.71 sec                                                        | 1.57 sec: 1.09x faster                                                           |
| json_loads           | 21.6 us                                                         | 20.9 us: 1.03x faster                                                            |
| xml_etree_parse      | 107 ms                                                          | 105 ms: 1.02x faster                                                             |
| unpickle_pure_python | 160 us                                                          | 158 us: 1.01x faster                                                             |
| xml_etree_generate   | 61.4 ms                                                         | 71.8 ms: 1.17x slower                                                            |
| xml_etree_process    | 44.2 ms                                                         | 52.2 ms: 1.18x slower                                                            |
| json_dumps           | 7.30 ms                                                         | 8.67 ms: 1.19x slower                                                            |
| xml_etree_iterparse  | 62.6 ms                                                         | 86.8 ms: 1.39x slower                                                            |
| pickle_pure_python   | 231 us                                                          | 330 us: 1.43x slower                                                             |
| Geometric mean       | (ref)                                                           | 1.12x slower                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250614-pythonperf1_win32-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50 |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup         | 28.3 ms                                                         | 27.3 ms: 1.03x faster                                                            |
| python_startup_no_site | 19.7 ms                                                         | 19.9 ms: 1.01x slower                                                            |
| Geometric mean         | (ref)                                                           | 1.01x faster                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250614-pythonperf1_win32-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50 |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                         | 7.24 ms: 1.02x slower                                                            |
| genshi_text     | 21.5 ms                                                         | 24.7 ms: 1.15x slower                                                            |
| django_template | 29.8 ms                                                         | 37.8 ms: 1.27x slower                                                            |
| Geometric mean  | (ref)                                                           | 1.11x slower                                                                     |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250614-pythonperf1_win32-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50 |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pathlib                    | 82.9 ms                                                         | 34.7 ms: 2.39x faster                                                            |
| asyncio_websockets         | 363 ms                                                          | 159 ms: 2.29x faster                                                             |
| nbody                      | 80.0 ms                                                         | 56.2 ms: 1.42x faster                                                            |
| pidigits                   | 201 ms                                                          | 146 ms: 1.37x faster                                                             |
| mdp                        | 1.62 sec                                                        | 1.20 sec: 1.36x faster                                                           |
| telco                      | 6.96 ms                                                         | 5.26 ms: 1.32x faster                                                            |
| deepcopy                   | 314 us                                                          | 270 us: 1.16x faster                                                             |
| bpe_tokeniser              | 3.46 sec                                                        | 3.06 sec: 1.13x faster                                                           |
| sqlite_synth               | 1.95 us                                                         | 1.74 us: 1.12x faster                                                            |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 432 ms: 1.12x faster                                                             |
| tomli_loads                | 1.71 sec                                                        | 1.57 sec: 1.09x faster                                                           |
| scimark_fft                | 205 ms                                                          | 188 ms: 1.09x faster                                                             |
| json                       | 4.27 ms                                                         | 3.99 ms: 1.07x faster                                                            |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 430 ms: 1.06x faster                                                             |
| async_tree_none            | 245 ms                                                          | 232 ms: 1.05x faster                                                             |
| fannkuch                   | 299 ms                                                          | 285 ms: 1.05x faster                                                             |
| deepcopy_reduce            | 2.92 us                                                         | 2.79 us: 1.05x faster                                                            |
| async_tree_memoization     | 297 ms                                                          | 285 ms: 1.04x faster                                                             |
| regex_effbot               | 1.80 ms                                                         | 1.74 ms: 1.03x faster                                                            |
| python_startup             | 28.3 ms                                                         | 27.3 ms: 1.03x faster                                                            |
| json_loads                 | 21.6 us                                                         | 20.9 us: 1.03x faster                                                            |
| bench_thread_pool          | 1.00 ms                                                         | 978 us: 1.02x faster                                                             |
| xml_etree_parse            | 107 ms                                                          | 105 ms: 1.02x faster                                                             |
| scimark_sparse_mat_mult    | 2.84 ms                                                         | 2.80 ms: 1.02x faster                                                            |
| unpickle_pure_python       | 160 us                                                          | 158 us: 1.01x faster                                                             |
| async_tree_memoization_tg  | 282 ms                                                          | 285 ms: 1.01x slower                                                             |
| async_tree_io              | 526 ms                                                          | 532 ms: 1.01x slower                                                             |
| python_startup_no_site     | 19.7 ms                                                         | 19.9 ms: 1.01x slower                                                            |
| mako                       | 7.09 ms                                                         | 7.24 ms: 1.02x slower                                                            |
| regex_dna                  | 114 ms                                                          | 116 ms: 1.02x slower                                                             |
| pprint_safe_repr           | 648 ms                                                          | 666 ms: 1.03x slower                                                             |
| pprint_pformat             | 1.33 sec                                                        | 1.38 sec: 1.04x slower                                                           |
| typing_runtime_protocols   | 138 us                                                          | 145 us: 1.05x slower                                                             |
| async_tree_none_tg         | 214 ms                                                          | 227 ms: 1.06x slower                                                             |
| dulwich_log                | 48.8 ms                                                         | 51.8 ms: 1.06x slower                                                            |
| pycparser                  | 872 ms                                                          | 940 ms: 1.08x slower                                                             |
| sympy_expand               | 373 ms                                                          | 404 ms: 1.08x slower                                                             |
| html5lib                   | 47.5 ms                                                         | 51.9 ms: 1.09x slower                                                            |
| crypto_pyaes               | 56.9 ms                                                         | 62.2 ms: 1.09x slower                                                            |
| meteor_contest             | 74.6 ms                                                         | 81.7 ms: 1.09x slower                                                            |
| sympy_str                  | 212 ms                                                          | 233 ms: 1.10x slower                                                             |
| pylint                     | 227 ms                                                          | 250 ms: 1.10x slower                                                             |
| async_tree_io_tg           | 494 ms                                                          | 550 ms: 1.11x slower                                                             |
| sympy_sum                  | 106 ms                                                          | 120 ms: 1.14x slower                                                             |
| 2to3                       | 250 ms                                                          | 286 ms: 1.14x slower                                                             |
| logging_format             | 8.72 us                                                         | 9.97 us: 1.14x slower                                                            |
| genshi_text                | 21.5 ms                                                         | 24.7 ms: 1.15x slower                                                            |
| bench_mp_pool              | 90.6 ms                                                         | 105 ms: 1.15x slower                                                             |
| sympy_integrate            | 15.0 ms                                                         | 17.3 ms: 1.16x slower                                                            |
| xml_etree_generate         | 61.4 ms                                                         | 71.8 ms: 1.17x slower                                                            |
| xml_etree_process          | 44.2 ms                                                         | 52.2 ms: 1.18x slower                                                            |
| logging_simple             | 7.99 us                                                         | 9.45 us: 1.18x slower                                                            |
| docutils                   | 1.78 sec                                                        | 2.11 sec: 1.18x slower                                                           |
| sphinx                     | 719 ms                                                          | 852 ms: 1.19x slower                                                             |
| json_dumps                 | 7.30 ms                                                         | 8.67 ms: 1.19x slower                                                            |
| regex_compile              | 101 ms                                                          | 120 ms: 1.19x slower                                                             |
| pyflate                    | 320 ms                                                          | 387 ms: 1.21x slower                                                             |
| connected_components       | 267 ms                                                          | 323 ms: 1.21x slower                                                             |
| k_core                     | 1.38 sec                                                        | 1.68 sec: 1.22x slower                                                           |
| nqueens                    | 72.1 ms                                                         | 90.4 ms: 1.25x slower                                                            |
| shortest_path              | 290 ms                                                          | 365 ms: 1.26x slower                                                             |
| go                         | 109 ms                                                          | 137 ms: 1.26x slower                                                             |
| comprehensions             | 12.5 us                                                         | 15.8 us: 1.26x slower                                                            |
| django_template            | 29.8 ms                                                         | 37.8 ms: 1.27x slower                                                            |
| many_optionals             | 436 us                                                          | 568 us: 1.30x slower                                                             |
| async_generators           | 270 ms                                                          | 354 ms: 1.31x slower                                                             |
| chaos                      | 50.2 ms                                                         | 65.9 ms: 1.31x slower                                                            |
| deepcopy_memo              | 25.4 us                                                         | 35.0 us: 1.38x slower                                                            |
| xml_etree_iterparse        | 62.6 ms                                                         | 86.8 ms: 1.39x slower                                                            |
| create_gc_cycles           | 1.06 ms                                                         | 1.47 ms: 1.39x slower                                                            |
| pickle_pure_python         | 231 us                                                          | 330 us: 1.43x slower                                                             |
| float                      | 54.6 ms                                                         | 78.1 ms: 1.43x slower                                                            |
| coverage                   | 324 ms                                                          | 473 ms: 1.46x slower                                                             |
| raytrace                   | 201 ms                                                          | 307 ms: 1.53x slower                                                             |
| subparsers                 | 14.8 ms                                                         | 22.6 ms: 1.53x slower                                                            |
| scimark_monte_carlo        | 47.7 ms                                                         | 74.0 ms: 1.55x slower                                                            |
| scimark_sor                | 85.9 ms                                                         | 134 ms: 1.56x slower                                                             |
| coroutines                 | 16.2 ms                                                         | 25.6 ms: 1.58x slower                                                            |
| richards                   | 32.7 ms                                                         | 51.6 ms: 1.58x slower                                                            |
| richards_super             | 36.7 ms                                                         | 58.6 ms: 1.60x slower                                                            |
| gc_traversal               | 1.75 ms                                                         | 2.83 ms: 1.62x slower                                                            |
| spectral_norm              | 69.4 ms                                                         | 116 ms: 1.67x slower                                                             |
| generators                 | 21.8 ms                                                         | 37.3 ms: 1.71x slower                                                            |
| hexiom                     | 4.44 ms                                                         | 7.80 ms: 1.76x slower                                                            |
| deltablue                  | 2.33 ms                                                         | 4.55 ms: 1.95x slower                                                            |
| scimark_lu                 | 60.2 ms                                                         | 122 ms: 2.02x slower                                                             |
| logging_silent             | 60.3 ns                                                         | 502 ns: 8.33x slower                                                             |
| thrift                     | 9.98 ms                                                         | 103 ms: 10.30x slower                                                            |
| Geometric mean             | (ref)                                                           | 1.18x slower                                                                     |

Benchmark hidden because not significant (2): regex_v8, genshi_xml
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250614-3.15.0a0-2e15a50-JIT/bm-20250614-pythonperf1_win32-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.132x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.08x
- 95% likely to have a slowdown of 1.06x
- 99% likely to have a slowdown of 1.04x

# Memory
- memory change: unknown