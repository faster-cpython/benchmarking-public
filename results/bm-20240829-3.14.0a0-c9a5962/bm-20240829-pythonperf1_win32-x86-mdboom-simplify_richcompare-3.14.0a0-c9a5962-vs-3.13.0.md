# Results vs. 3.13.0

- fork: mdboom
- ref: simplify_richcompare
- machine: windows-x86
- commit hash: c9a5962
- commit date: 2024-08-29
- overall geometric mean: 1.031x faster
- HPT reliability: 98.47%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240829-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 255 ms                                                          | 248 ms: 1.03x faster                                                           |
| docutils       | 1.80 sec                                                        | 1.86 sec: 1.03x slower                                                         |
| html5lib       | 47.1 ms                                                         | 45.8 ms: 1.03x faster                                                          |
| Geometric mean | (ref)                                                           | 1.01x faster                                                                   |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240829-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 287 ms                                                          | 249 ms: 1.15x faster                                                           |
| async_tree_none            | 245 ms                                                          | 213 ms: 1.15x faster                                                           |
| async_tree_memoization     | 302 ms                                                          | 274 ms: 1.10x faster                                                           |
| async_tree_none_tg         | 216 ms                                                          | 199 ms: 1.08x faster                                                           |
| async_tree_cpu_io_mixed    | 490 ms                                                          | 464 ms: 1.06x faster                                                           |
| async_tree_cpu_io_mixed_tg | 469 ms                                                          | 460 ms: 1.02x faster                                                           |
| async_tree_io_tg           | 499 ms                                                          | 515 ms: 1.03x slower                                                           |
| coroutines                 | 16.1 ms                                                         | 17.4 ms: 1.08x slower                                                          |
| async_generators           | 267 ms                                                          | 292 ms: 1.09x slower                                                           |
| Geometric mean             | (ref)                                                           | 1.03x faster                                                                   |

Benchmark hidden because not significant (1): async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240829-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pidigits       | 204 ms                                                          | 201 ms: 1.01x faster                                                           |
| float          | 56.4 ms                                                         | 62.2 ms: 1.10x slower                                                          |
| nbody          | 81.4 ms                                                         | 94.3 ms: 1.16x slower                                                          |
| Geometric mean | (ref)                                                           | 1.08x slower                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240829-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_v8       | 15.5 ms                                                         | 16.2 ms: 1.05x slower                                                          |
| regex_effbot   | 1.82 ms                                                         | 1.92 ms: 1.05x slower                                                          |
| regex_dna      | 112 ms                                                          | 118 ms: 1.06x slower                                                           |
| regex_compile  | 101 ms                                                          | 107 ms: 1.06x slower                                                           |
| Geometric mean | (ref)                                                           | 1.05x slower                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240829-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| json_loads           | 21.7 us                                                         | 20.3 us: 1.07x faster                                                          |
| json_dumps           | 7.53 ms                                                         | 7.39 ms: 1.02x faster                                                          |
| tomli_loads          | 1.74 sec                                                        | 1.84 sec: 1.06x slower                                                         |
| xml_etree_parse      | 102 ms                                                          | 109 ms: 1.06x slower                                                           |
| xml_etree_generate   | 61.9 ms                                                         | 67.5 ms: 1.09x slower                                                          |
| pickle_pure_python   | 239 us                                                          | 263 us: 1.10x slower                                                           |
| xml_etree_process    | 44.6 ms                                                         | 49.9 ms: 1.12x slower                                                          |
| xml_etree_iterparse  | 61.3 ms                                                         | 68.8 ms: 1.12x slower                                                          |
| unpickle_pure_python | 162 us                                                          | 183 us: 1.13x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.06x slower                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240829-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup | 28.3 ms                                                         | 24.0 ms: 1.18x faster                                                          |
| Geometric mean | (ref)                                                           | 1.09x faster                                                                   |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240829-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| genshi_xml     | 49.0 ms                                                         | 46.1 ms: 1.06x faster                                                          |
| genshi_text    | 21.7 ms                                                         | 22.0 ms: 1.01x slower                                                          |
| mako           | 7.02 ms                                                         | 8.24 ms: 1.17x slower                                                          |
| Geometric mean | (ref)                                                           | 1.03x slower                                                                   |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240829-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| thrift                     | 10.3 ms                                                         | 719 us: 14.27x faster                                                          |
| coverage                   | 326 ms                                                          | 53.6 ms: 6.09x faster                                                          |
| create_gc_cycles           | 1.08 ms                                                         | 744 us: 1.46x faster                                                           |
| deepcopy                   | 311 us                                                          | 242 us: 1.28x faster                                                           |
| bench_mp_pool              | 93.6 ms                                                         | 73.2 ms: 1.28x faster                                                          |
| gc_traversal               | 1.76 ms                                                         | 1.45 ms: 1.22x faster                                                          |
| deepcopy_reduce            | 2.94 us                                                         | 2.42 us: 1.22x faster                                                          |
| deepcopy_memo              | 26.2 us                                                         | 22.2 us: 1.18x faster                                                          |
| python_startup             | 28.3 ms                                                         | 24.0 ms: 1.18x faster                                                          |
| async_tree_memoization_tg  | 287 ms                                                          | 249 ms: 1.15x faster                                                           |
| async_tree_none            | 245 ms                                                          | 213 ms: 1.15x faster                                                           |
| async_tree_memoization     | 302 ms                                                          | 274 ms: 1.10x faster                                                           |
| async_tree_none_tg         | 216 ms                                                          | 199 ms: 1.08x faster                                                           |
| json_loads                 | 21.7 us                                                         | 20.3 us: 1.07x faster                                                          |
| genshi_xml                 | 49.0 ms                                                         | 46.1 ms: 1.06x faster                                                          |
| go                         | 111 ms                                                          | 104 ms: 1.06x faster                                                           |
| async_tree_cpu_io_mixed    | 490 ms                                                          | 464 ms: 1.06x faster                                                           |
| html5lib                   | 47.1 ms                                                         | 45.8 ms: 1.03x faster                                                          |
| 2to3                       | 255 ms                                                          | 248 ms: 1.03x faster                                                           |
| pprint_safe_repr           | 658 ms                                                          | 642 ms: 1.03x faster                                                           |
| json                       | 4.40 ms                                                         | 4.30 ms: 1.02x faster                                                          |
| async_tree_cpu_io_mixed_tg | 469 ms                                                          | 460 ms: 1.02x faster                                                           |
| pathlib                    | 89.1 ms                                                         | 87.4 ms: 1.02x faster                                                          |
| json_dumps                 | 7.53 ms                                                         | 7.39 ms: 1.02x faster                                                          |
| pidigits                   | 204 ms                                                          | 201 ms: 1.01x faster                                                           |
| pycparser                  | 869 ms                                                          | 862 ms: 1.01x faster                                                           |
| dulwich_log                | 50.2 ms                                                         | 49.9 ms: 1.01x faster                                                          |
| pprint_pformat             | 1.32 sec                                                        | 1.33 sec: 1.00x slower                                                         |
| logging_simple             | 7.89 us                                                         | 7.94 us: 1.01x slower                                                          |
| sqlglot_normalize          | 223 ms                                                          | 225 ms: 1.01x slower                                                           |
| genshi_text                | 21.7 ms                                                         | 22.0 ms: 1.01x slower                                                          |
| sympy_expand               | 377 ms                                                          | 383 ms: 1.01x slower                                                           |
| typing_runtime_protocols   | 141 us                                                          | 143 us: 1.02x slower                                                           |
| mdp                        | 1.70 sec                                                        | 1.72 sec: 1.02x slower                                                         |
| sympy_integrate            | 15.2 ms                                                         | 15.5 ms: 1.02x slower                                                          |
| async_tree_io_tg           | 499 ms                                                          | 515 ms: 1.03x slower                                                           |
| sqlglot_optimize           | 42.4 ms                                                         | 43.8 ms: 1.03x slower                                                          |
| docutils                   | 1.80 sec                                                        | 1.86 sec: 1.03x slower                                                         |
| comprehensions             | 13.1 us                                                         | 13.7 us: 1.04x slower                                                          |
| pylint                     | 225 ms                                                          | 234 ms: 1.04x slower                                                           |
| regex_v8                   | 15.5 ms                                                         | 16.2 ms: 1.05x slower                                                          |
| sqlglot_transpile          | 1.26 ms                                                         | 1.32 ms: 1.05x slower                                                          |
| sqlglot_parse              | 1.02 ms                                                         | 1.07 ms: 1.05x slower                                                          |
| regex_effbot               | 1.82 ms                                                         | 1.92 ms: 1.05x slower                                                          |
| regex_dna                  | 112 ms                                                          | 118 ms: 1.06x slower                                                           |
| tomli_loads                | 1.74 sec                                                        | 1.84 sec: 1.06x slower                                                         |
| meteor_contest             | 78.1 ms                                                         | 82.8 ms: 1.06x slower                                                          |
| xml_etree_parse            | 102 ms                                                          | 109 ms: 1.06x slower                                                           |
| regex_compile              | 101 ms                                                          | 107 ms: 1.06x slower                                                           |
| telco                      | 6.27 ms                                                         | 6.69 ms: 1.07x slower                                                          |
| chaos                      | 49.4 ms                                                         | 52.8 ms: 1.07x slower                                                          |
| coroutines                 | 16.1 ms                                                         | 17.4 ms: 1.08x slower                                                          |
| scimark_sparse_mat_mult    | 2.88 ms                                                         | 3.14 ms: 1.09x slower                                                          |
| xml_etree_generate         | 61.9 ms                                                         | 67.5 ms: 1.09x slower                                                          |
| async_generators           | 267 ms                                                          | 292 ms: 1.09x slower                                                           |
| pickle_pure_python         | 239 us                                                          | 263 us: 1.10x slower                                                           |
| pyflate                    | 322 ms                                                          | 354 ms: 1.10x slower                                                           |
| float                      | 56.4 ms                                                         | 62.2 ms: 1.10x slower                                                          |
| spectral_norm              | 70.0 ms                                                         | 77.6 ms: 1.11x slower                                                          |
| xml_etree_process          | 44.6 ms                                                         | 49.9 ms: 1.12x slower                                                          |
| xml_etree_iterparse        | 61.3 ms                                                         | 68.8 ms: 1.12x slower                                                          |
| raytrace                   | 203 ms                                                          | 229 ms: 1.13x slower                                                           |
| unpickle_pure_python       | 162 us                                                          | 183 us: 1.13x slower                                                           |
| scimark_lu                 | 60.7 ms                                                         | 68.7 ms: 1.13x slower                                                          |
| hexiom                     | 4.60 ms                                                         | 5.20 ms: 1.13x slower                                                          |
| deltablue                  | 2.35 ms                                                         | 2.71 ms: 1.15x slower                                                          |
| nbody                      | 81.4 ms                                                         | 94.3 ms: 1.16x slower                                                          |
| scimark_fft                | 204 ms                                                          | 237 ms: 1.16x slower                                                           |
| fannkuch                   | 288 ms                                                          | 336 ms: 1.17x slower                                                           |
| logging_silent             | 62.4 ns                                                         | 73.1 ns: 1.17x slower                                                          |
| mako                       | 7.02 ms                                                         | 8.24 ms: 1.17x slower                                                          |
| scimark_monte_carlo        | 48.7 ms                                                         | 57.4 ms: 1.18x slower                                                          |
| richards                   | 33.4 ms                                                         | 39.4 ms: 1.18x slower                                                          |
| richards_super             | 37.0 ms                                                         | 43.9 ms: 1.19x slower                                                          |
| scimark_sor                | 85.8 ms                                                         | 103 ms: 1.20x slower                                                           |
| generators                 | 21.5 ms                                                         | 26.8 ms: 1.25x slower                                                          |
| Geometric mean             | (ref)                                                           | 1.03x faster                                                                   |

Benchmark hidden because not significant (10): bench_thread_pool, sympy_sum, python_startup_no_site, tornado_http, django_template, crypto_pyaes, sympy_str, logging_format, nqueens, async_tree_io
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: asyncio_websockets, bpe_tokeniser, chameleon, connected_components, gevent_hub, k_core, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (2) of results/bm-20240829-3.14.0a0-c9a5962/bm-20240829-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-c9a5962.json: asyncio_tcp, asyncio_tcp_ssl

- Geometric mean (including insignificant results): 1.031x faster
# HPT report

- Reliability score: 98.47% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown