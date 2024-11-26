# Results vs. 3.13.0

- fork: mdboom
- ref: simplify_richcompare
- machine: windows-x86
- commit hash: 15b187e
- commit date: 2024-08-29
- overall geometric mean: 1.026x faster
- HPT reliability: 99.68%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240829-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 255 ms                                                          | 251 ms: 1.02x faster                                                           |
| docutils       | 1.80 sec                                                        | 1.86 sec: 1.03x slower                                                         |
| html5lib       | 47.1 ms                                                         | 46.5 ms: 1.01x faster                                                          |
| Geometric mean | (ref)                                                           | 1.00x slower                                                                   |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240829-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_none            | 245 ms                                                          | 215 ms: 1.14x faster                                                           |
| async_tree_memoization_tg  | 287 ms                                                          | 253 ms: 1.13x faster                                                           |
| async_tree_memoization     | 302 ms                                                          | 276 ms: 1.10x faster                                                           |
| async_tree_none_tg         | 216 ms                                                          | 199 ms: 1.08x faster                                                           |
| async_tree_cpu_io_mixed    | 490 ms                                                          | 465 ms: 1.05x faster                                                           |
| async_tree_cpu_io_mixed_tg | 469 ms                                                          | 465 ms: 1.01x faster                                                           |
| async_tree_io_tg           | 499 ms                                                          | 518 ms: 1.04x slower                                                           |
| coroutines                 | 16.1 ms                                                         | 17.5 ms: 1.09x slower                                                          |
| async_generators           | 267 ms                                                          | 307 ms: 1.15x slower                                                           |
| Geometric mean             | (ref)                                                           | 1.02x faster                                                                   |

Benchmark hidden because not significant (1): async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240829-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pidigits       | 204 ms                                                          | 202 ms: 1.01x faster                                                           |
| float          | 56.4 ms                                                         | 62.0 ms: 1.10x slower                                                          |
| nbody          | 81.4 ms                                                         | 95.8 ms: 1.18x slower                                                          |
| Geometric mean | (ref)                                                           | 1.09x slower                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240829-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_v8       | 15.5 ms                                                         | 16.2 ms: 1.05x slower                                                          |
| regex_compile  | 101 ms                                                          | 107 ms: 1.06x slower                                                           |
| regex_effbot   | 1.82 ms                                                         | 1.94 ms: 1.07x slower                                                          |
| regex_dna      | 112 ms                                                          | 122 ms: 1.09x slower                                                           |
| Geometric mean | (ref)                                                           | 1.06x slower                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240829-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| json_loads           | 21.7 us                                                         | 20.4 us: 1.06x faster                                                          |
| json_dumps           | 7.53 ms                                                         | 7.74 ms: 1.03x slower                                                          |
| xml_etree_parse      | 102 ms                                                          | 107 ms: 1.05x slower                                                           |
| pickle_pure_python   | 239 us                                                          | 254 us: 1.06x slower                                                           |
| tomli_loads          | 1.74 sec                                                        | 1.86 sec: 1.07x slower                                                         |
| unpickle_pure_python | 162 us                                                          | 179 us: 1.10x slower                                                           |
| xml_etree_generate   | 61.9 ms                                                         | 68.4 ms: 1.11x slower                                                          |
| xml_etree_iterparse  | 61.3 ms                                                         | 67.9 ms: 1.11x slower                                                          |
| xml_etree_process    | 44.6 ms                                                         | 51.0 ms: 1.14x slower                                                          |
| Geometric mean       | (ref)                                                           | 1.07x slower                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240829-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 28.3 ms                                                         | 24.1 ms: 1.18x faster                                                          |
| python_startup_no_site | 20.2 ms                                                         | 19.7 ms: 1.02x faster                                                          |
| Geometric mean         | (ref)                                                           | 1.10x faster                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240829-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| genshi_xml      | 49.0 ms                                                         | 46.8 ms: 1.05x faster                                                          |
| django_template | 32.0 ms                                                         | 32.8 ms: 1.02x slower                                                          |
| mako            | 7.02 ms                                                         | 8.41 ms: 1.20x slower                                                          |
| Geometric mean  | (ref)                                                           | 1.04x slower                                                                   |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240829-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| thrift                     | 10.3 ms                                                         | 727 us: 14.11x faster                                                          |
| coverage                   | 326 ms                                                          | 54.0 ms: 6.04x faster                                                          |
| create_gc_cycles           | 1.08 ms                                                         | 751 us: 1.44x faster                                                           |
| bench_mp_pool              | 93.6 ms                                                         | 72.8 ms: 1.29x faster                                                          |
| deepcopy                   | 311 us                                                          | 246 us: 1.26x faster                                                           |
| gc_traversal               | 1.76 ms                                                         | 1.44 ms: 1.23x faster                                                          |
| deepcopy_memo              | 26.2 us                                                         | 22.0 us: 1.19x faster                                                          |
| python_startup             | 28.3 ms                                                         | 24.1 ms: 1.18x faster                                                          |
| deepcopy_reduce            | 2.94 us                                                         | 2.51 us: 1.17x faster                                                          |
| async_tree_none            | 245 ms                                                          | 215 ms: 1.14x faster                                                           |
| async_tree_memoization_tg  | 287 ms                                                          | 253 ms: 1.13x faster                                                           |
| async_tree_memoization     | 302 ms                                                          | 276 ms: 1.10x faster                                                           |
| async_tree_none_tg         | 216 ms                                                          | 199 ms: 1.08x faster                                                           |
| go                         | 111 ms                                                          | 103 ms: 1.08x faster                                                           |
| json_loads                 | 21.7 us                                                         | 20.4 us: 1.06x faster                                                          |
| async_tree_cpu_io_mixed    | 490 ms                                                          | 465 ms: 1.05x faster                                                           |
| genshi_xml                 | 49.0 ms                                                         | 46.8 ms: 1.05x faster                                                          |
| bench_thread_pool          | 1.04 ms                                                         | 1.01 ms: 1.03x faster                                                          |
| json                       | 4.40 ms                                                         | 4.27 ms: 1.03x faster                                                          |
| pathlib                    | 89.1 ms                                                         | 86.9 ms: 1.03x faster                                                          |
| python_startup_no_site     | 20.2 ms                                                         | 19.7 ms: 1.02x faster                                                          |
| 2to3                       | 255 ms                                                          | 251 ms: 1.02x faster                                                           |
| pycparser                  | 869 ms                                                          | 857 ms: 1.01x faster                                                           |
| html5lib                   | 47.1 ms                                                         | 46.5 ms: 1.01x faster                                                          |
| async_tree_cpu_io_mixed_tg | 469 ms                                                          | 465 ms: 1.01x faster                                                           |
| sympy_sum                  | 108 ms                                                          | 107 ms: 1.01x faster                                                           |
| pidigits                   | 204 ms                                                          | 202 ms: 1.01x faster                                                           |
| sympy_integrate            | 15.2 ms                                                         | 15.3 ms: 1.01x slower                                                          |
| pprint_pformat             | 1.32 sec                                                        | 1.33 sec: 1.01x slower                                                         |
| sympy_str                  | 214 ms                                                          | 216 ms: 1.01x slower                                                           |
| nqueens                    | 75.1 ms                                                         | 75.9 ms: 1.01x slower                                                          |
| sympy_expand               | 377 ms                                                          | 381 ms: 1.01x slower                                                           |
| logging_simple             | 7.89 us                                                         | 8.02 us: 1.02x slower                                                          |
| logging_format             | 8.59 us                                                         | 8.78 us: 1.02x slower                                                          |
| meteor_contest             | 78.1 ms                                                         | 79.9 ms: 1.02x slower                                                          |
| django_template            | 32.0 ms                                                         | 32.8 ms: 1.02x slower                                                          |
| sqlglot_optimize           | 42.4 ms                                                         | 43.5 ms: 1.02x slower                                                          |
| crypto_pyaes               | 56.6 ms                                                         | 58.2 ms: 1.03x slower                                                          |
| json_dumps                 | 7.53 ms                                                         | 7.74 ms: 1.03x slower                                                          |
| comprehensions             | 13.1 us                                                         | 13.5 us: 1.03x slower                                                          |
| docutils                   | 1.80 sec                                                        | 1.86 sec: 1.03x slower                                                         |
| async_tree_io_tg           | 499 ms                                                          | 518 ms: 1.04x slower                                                           |
| pylint                     | 225 ms                                                          | 233 ms: 1.04x slower                                                           |
| sqlglot_transpile          | 1.26 ms                                                         | 1.32 ms: 1.05x slower                                                          |
| typing_runtime_protocols   | 141 us                                                          | 148 us: 1.05x slower                                                           |
| xml_etree_parse            | 102 ms                                                          | 107 ms: 1.05x slower                                                           |
| regex_v8                   | 15.5 ms                                                         | 16.2 ms: 1.05x slower                                                          |
| sqlglot_parse              | 1.02 ms                                                         | 1.07 ms: 1.05x slower                                                          |
| regex_compile              | 101 ms                                                          | 107 ms: 1.06x slower                                                           |
| pickle_pure_python         | 239 us                                                          | 254 us: 1.06x slower                                                           |
| tomli_loads                | 1.74 sec                                                        | 1.86 sec: 1.07x slower                                                         |
| regex_effbot               | 1.82 ms                                                         | 1.94 ms: 1.07x slower                                                          |
| spectral_norm              | 70.0 ms                                                         | 75.6 ms: 1.08x slower                                                          |
| chaos                      | 49.4 ms                                                         | 53.5 ms: 1.08x slower                                                          |
| coroutines                 | 16.1 ms                                                         | 17.5 ms: 1.09x slower                                                          |
| regex_dna                  | 112 ms                                                          | 122 ms: 1.09x slower                                                           |
| float                      | 56.4 ms                                                         | 62.0 ms: 1.10x slower                                                          |
| unpickle_pure_python       | 162 us                                                          | 179 us: 1.10x slower                                                           |
| xml_etree_generate         | 61.9 ms                                                         | 68.4 ms: 1.11x slower                                                          |
| xml_etree_iterparse        | 61.3 ms                                                         | 67.9 ms: 1.11x slower                                                          |
| scimark_sparse_mat_mult    | 2.88 ms                                                         | 3.19 ms: 1.11x slower                                                          |
| pyflate                    | 322 ms                                                          | 358 ms: 1.11x slower                                                           |
| telco                      | 6.27 ms                                                         | 7.08 ms: 1.13x slower                                                          |
| xml_etree_process          | 44.6 ms                                                         | 51.0 ms: 1.14x slower                                                          |
| hexiom                     | 4.60 ms                                                         | 5.29 ms: 1.15x slower                                                          |
| fannkuch                   | 288 ms                                                          | 332 ms: 1.15x slower                                                           |
| async_generators           | 267 ms                                                          | 307 ms: 1.15x slower                                                           |
| deltablue                  | 2.35 ms                                                         | 2.72 ms: 1.16x slower                                                          |
| scimark_fft                | 204 ms                                                          | 237 ms: 1.16x slower                                                           |
| scimark_lu                 | 60.7 ms                                                         | 70.6 ms: 1.16x slower                                                          |
| scimark_monte_carlo        | 48.7 ms                                                         | 56.6 ms: 1.16x slower                                                          |
| raytrace                   | 203 ms                                                          | 236 ms: 1.16x slower                                                           |
| richards                   | 33.4 ms                                                         | 39.0 ms: 1.17x slower                                                          |
| nbody                      | 81.4 ms                                                         | 95.8 ms: 1.18x slower                                                          |
| scimark_sor                | 85.8 ms                                                         | 102 ms: 1.19x slower                                                           |
| logging_silent             | 62.4 ns                                                         | 74.5 ns: 1.19x slower                                                          |
| mako                       | 7.02 ms                                                         | 8.41 ms: 1.20x slower                                                          |
| richards_super             | 37.0 ms                                                         | 44.8 ms: 1.21x slower                                                          |
| generators                 | 21.5 ms                                                         | 27.9 ms: 1.30x slower                                                          |
| Geometric mean             | (ref)                                                           | 1.03x faster                                                                   |

Benchmark hidden because not significant (7): pprint_safe_repr, dulwich_log, tornado_http, mdp, sqlglot_normalize, genshi_text, async_tree_io
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: asyncio_websockets, bpe_tokeniser, chameleon, connected_components, gevent_hub, k_core, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (2) of results/bm-20240829-3.14.0a0-15b187e/bm-20240829-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-15b187e.json: asyncio_tcp, asyncio_tcp_ssl

- Geometric mean (including insignificant results): 1.026x faster
# HPT report

- Reliability score: 99.68% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown