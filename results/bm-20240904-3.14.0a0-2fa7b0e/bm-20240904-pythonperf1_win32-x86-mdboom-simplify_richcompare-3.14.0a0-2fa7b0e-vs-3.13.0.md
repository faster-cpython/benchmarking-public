# Results vs. 3.13.0

- fork: mdboom
- ref: simplify_richcompare
- machine: windows-x86
- commit hash: 2fa7b0e
- commit date: 2024-09-04
- overall geometric mean: 1.031x faster
- HPT reliability: 99.36%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240904-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 255 ms                                                          | 251 ms: 1.01x faster                                                           |
| docutils       | 1.80 sec                                                        | 1.86 sec: 1.03x slower                                                         |
| html5lib       | 47.1 ms                                                         | 46.5 ms: 1.01x faster                                                          |
| Geometric mean | (ref)                                                           | 1.00x slower                                                                   |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240904-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 287 ms                                                          | 249 ms: 1.15x faster                                                           |
| async_tree_none            | 245 ms                                                          | 217 ms: 1.13x faster                                                           |
| async_tree_memoization     | 302 ms                                                          | 273 ms: 1.10x faster                                                           |
| async_tree_none_tg         | 216 ms                                                          | 198 ms: 1.09x faster                                                           |
| async_tree_cpu_io_mixed    | 490 ms                                                          | 460 ms: 1.06x faster                                                           |
| async_tree_cpu_io_mixed_tg | 469 ms                                                          | 456 ms: 1.03x faster                                                           |
| async_tree_io_tg           | 499 ms                                                          | 516 ms: 1.03x slower                                                           |
| coroutines                 | 16.1 ms                                                         | 17.5 ms: 1.09x slower                                                          |
| async_generators           | 267 ms                                                          | 299 ms: 1.12x slower                                                           |
| Geometric mean             | (ref)                                                           | 1.03x faster                                                                   |

Benchmark hidden because not significant (1): async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240904-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pidigits       | 204 ms                                                          | 201 ms: 1.01x faster                                                           |
| float          | 56.4 ms                                                         | 60.8 ms: 1.08x slower                                                          |
| nbody          | 81.4 ms                                                         | 96.8 ms: 1.19x slower                                                          |
| Geometric mean | (ref)                                                           | 1.08x slower                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240904-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_v8       | 15.5 ms                                                         | 16.3 ms: 1.05x slower                                                          |
| regex_effbot   | 1.82 ms                                                         | 1.93 ms: 1.06x slower                                                          |
| regex_compile  | 101 ms                                                          | 107 ms: 1.06x slower                                                           |
| regex_dna      | 112 ms                                                          | 123 ms: 1.10x slower                                                           |
| Geometric mean | (ref)                                                           | 1.07x slower                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240904-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| json_loads           | 21.7 us                                                         | 20.4 us: 1.06x faster                                                          |
| json_dumps           | 7.53 ms                                                         | 7.42 ms: 1.01x faster                                                          |
| xml_etree_parse      | 102 ms                                                          | 108 ms: 1.05x slower                                                           |
| unpickle_pure_python | 162 us                                                          | 171 us: 1.06x slower                                                           |
| pickle_pure_python   | 239 us                                                          | 254 us: 1.06x slower                                                           |
| tomli_loads          | 1.74 sec                                                        | 1.89 sec: 1.09x slower                                                         |
| xml_etree_generate   | 61.9 ms                                                         | 67.9 ms: 1.10x slower                                                          |
| xml_etree_process    | 44.6 ms                                                         | 49.3 ms: 1.11x slower                                                          |
| xml_etree_iterparse  | 61.3 ms                                                         | 67.9 ms: 1.11x slower                                                          |
| Geometric mean       | (ref)                                                           | 1.05x slower                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240904-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup | 28.3 ms                                                         | 24.2 ms: 1.17x faster                                                          |
| Geometric mean | (ref)                                                           | 1.09x faster                                                                   |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240904-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| genshi_xml      | 49.0 ms                                                         | 46.5 ms: 1.05x faster                                                          |
| genshi_text     | 21.7 ms                                                         | 21.6 ms: 1.01x faster                                                          |
| django_template | 32.0 ms                                                         | 32.3 ms: 1.01x slower                                                          |
| mako            | 7.02 ms                                                         | 8.38 ms: 1.19x slower                                                          |
| Geometric mean  | (ref)                                                           | 1.03x slower                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240904-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| thrift                     | 10.3 ms                                                         | 735 us: 13.95x faster                                                          |
| coverage                   | 326 ms                                                          | 51.5 ms: 6.34x faster                                                          |
| create_gc_cycles           | 1.08 ms                                                         | 751 us: 1.44x faster                                                           |
| deepcopy                   | 311 us                                                          | 247 us: 1.26x faster                                                           |
| bench_mp_pool              | 93.6 ms                                                         | 74.9 ms: 1.25x faster                                                          |
| gc_traversal               | 1.76 ms                                                         | 1.42 ms: 1.24x faster                                                          |
| deepcopy_reduce            | 2.94 us                                                         | 2.43 us: 1.21x faster                                                          |
| python_startup             | 28.3 ms                                                         | 24.2 ms: 1.17x faster                                                          |
| deepcopy_memo              | 26.2 us                                                         | 22.5 us: 1.17x faster                                                          |
| async_tree_memoization_tg  | 287 ms                                                          | 249 ms: 1.15x faster                                                           |
| async_tree_none            | 245 ms                                                          | 217 ms: 1.13x faster                                                           |
| async_tree_memoization     | 302 ms                                                          | 273 ms: 1.10x faster                                                           |
| async_tree_none_tg         | 216 ms                                                          | 198 ms: 1.09x faster                                                           |
| go                         | 111 ms                                                          | 102 ms: 1.09x faster                                                           |
| json_loads                 | 21.7 us                                                         | 20.4 us: 1.06x faster                                                          |
| async_tree_cpu_io_mixed    | 490 ms                                                          | 460 ms: 1.06x faster                                                           |
| genshi_xml                 | 49.0 ms                                                         | 46.5 ms: 1.05x faster                                                          |
| json                       | 4.40 ms                                                         | 4.19 ms: 1.05x faster                                                          |
| async_tree_cpu_io_mixed_tg | 469 ms                                                          | 456 ms: 1.03x faster                                                           |
| pathlib                    | 89.1 ms                                                         | 87.8 ms: 1.02x faster                                                          |
| json_dumps                 | 7.53 ms                                                         | 7.42 ms: 1.01x faster                                                          |
| pidigits                   | 204 ms                                                          | 201 ms: 1.01x faster                                                           |
| 2to3                       | 255 ms                                                          | 251 ms: 1.01x faster                                                           |
| html5lib                   | 47.1 ms                                                         | 46.5 ms: 1.01x faster                                                          |
| dulwich_log                | 50.2 ms                                                         | 49.7 ms: 1.01x faster                                                          |
| pprint_safe_repr           | 658 ms                                                          | 651 ms: 1.01x faster                                                           |
| sympy_sum                  | 108 ms                                                          | 107 ms: 1.01x faster                                                           |
| genshi_text                | 21.7 ms                                                         | 21.6 ms: 1.01x faster                                                          |
| mdp                        | 1.70 sec                                                        | 1.70 sec: 1.00x slower                                                         |
| sqlglot_normalize          | 223 ms                                                          | 223 ms: 1.00x slower                                                           |
| sympy_expand               | 377 ms                                                          | 379 ms: 1.00x slower                                                           |
| sqlglot_optimize           | 42.4 ms                                                         | 42.8 ms: 1.01x slower                                                          |
| django_template            | 32.0 ms                                                         | 32.3 ms: 1.01x slower                                                          |
| pycparser                  | 869 ms                                                          | 878 ms: 1.01x slower                                                           |
| sympy_str                  | 214 ms                                                          | 217 ms: 1.01x slower                                                           |
| nqueens                    | 75.1 ms                                                         | 76.1 ms: 1.01x slower                                                          |
| pprint_pformat             | 1.32 sec                                                        | 1.34 sec: 1.01x slower                                                         |
| sympy_integrate            | 15.2 ms                                                         | 15.5 ms: 1.02x slower                                                          |
| crypto_pyaes               | 56.6 ms                                                         | 57.8 ms: 1.02x slower                                                          |
| comprehensions             | 13.1 us                                                         | 13.5 us: 1.03x slower                                                          |
| docutils                   | 1.80 sec                                                        | 1.86 sec: 1.03x slower                                                         |
| async_tree_io_tg           | 499 ms                                                          | 516 ms: 1.03x slower                                                           |
| pylint                     | 225 ms                                                          | 235 ms: 1.05x slower                                                           |
| sqlglot_transpile          | 1.26 ms                                                         | 1.33 ms: 1.05x slower                                                          |
| regex_v8                   | 15.5 ms                                                         | 16.3 ms: 1.05x slower                                                          |
| meteor_contest             | 78.1 ms                                                         | 82.2 ms: 1.05x slower                                                          |
| xml_etree_parse            | 102 ms                                                          | 108 ms: 1.05x slower                                                           |
| sqlglot_parse              | 1.02 ms                                                         | 1.08 ms: 1.06x slower                                                          |
| unpickle_pure_python       | 162 us                                                          | 171 us: 1.06x slower                                                           |
| regex_effbot               | 1.82 ms                                                         | 1.93 ms: 1.06x slower                                                          |
| regex_compile              | 101 ms                                                          | 107 ms: 1.06x slower                                                           |
| pickle_pure_python         | 239 us                                                          | 254 us: 1.06x slower                                                           |
| typing_runtime_protocols   | 141 us                                                          | 151 us: 1.07x slower                                                           |
| float                      | 56.4 ms                                                         | 60.8 ms: 1.08x slower                                                          |
| scimark_sparse_mat_mult    | 2.88 ms                                                         | 3.12 ms: 1.08x slower                                                          |
| spectral_norm              | 70.0 ms                                                         | 75.8 ms: 1.08x slower                                                          |
| tomli_loads                | 1.74 sec                                                        | 1.89 sec: 1.09x slower                                                         |
| coroutines                 | 16.1 ms                                                         | 17.5 ms: 1.09x slower                                                          |
| xml_etree_generate         | 61.9 ms                                                         | 67.9 ms: 1.10x slower                                                          |
| regex_dna                  | 112 ms                                                          | 123 ms: 1.10x slower                                                           |
| telco                      | 6.27 ms                                                         | 6.92 ms: 1.10x slower                                                          |
| xml_etree_process          | 44.6 ms                                                         | 49.3 ms: 1.11x slower                                                          |
| chaos                      | 49.4 ms                                                         | 54.6 ms: 1.11x slower                                                          |
| pyflate                    | 322 ms                                                          | 357 ms: 1.11x slower                                                           |
| xml_etree_iterparse        | 61.3 ms                                                         | 67.9 ms: 1.11x slower                                                          |
| async_generators           | 267 ms                                                          | 299 ms: 1.12x slower                                                           |
| deltablue                  | 2.35 ms                                                         | 2.64 ms: 1.12x slower                                                          |
| scimark_monte_carlo        | 48.7 ms                                                         | 55.0 ms: 1.13x slower                                                          |
| fannkuch                   | 288 ms                                                          | 328 ms: 1.14x slower                                                           |
| hexiom                     | 4.60 ms                                                         | 5.27 ms: 1.15x slower                                                          |
| scimark_sor                | 85.8 ms                                                         | 98.5 ms: 1.15x slower                                                          |
| richards                   | 33.4 ms                                                         | 38.5 ms: 1.15x slower                                                          |
| scimark_lu                 | 60.7 ms                                                         | 70.2 ms: 1.16x slower                                                          |
| raytrace                   | 203 ms                                                          | 236 ms: 1.16x slower                                                           |
| richards_super             | 37.0 ms                                                         | 43.3 ms: 1.17x slower                                                          |
| scimark_fft                | 204 ms                                                          | 241 ms: 1.18x slower                                                           |
| nbody                      | 81.4 ms                                                         | 96.8 ms: 1.19x slower                                                          |
| mako                       | 7.02 ms                                                         | 8.38 ms: 1.19x slower                                                          |
| logging_silent             | 62.4 ns                                                         | 74.7 ns: 1.20x slower                                                          |
| generators                 | 21.5 ms                                                         | 27.7 ms: 1.29x slower                                                          |
| Geometric mean             | (ref)                                                           | 1.03x faster                                                                   |

Benchmark hidden because not significant (6): bench_thread_pool, python_startup_no_site, logging_format, logging_simple, tornado_http, async_tree_io
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: asyncio_websockets, bpe_tokeniser, chameleon, connected_components, gevent_hub, k_core, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (2) of results/bm-20240904-3.14.0a0-2fa7b0e/bm-20240904-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e.json: asyncio_tcp, asyncio_tcp_ssl

- Geometric mean (including insignificant results): 1.031x faster
# HPT report

- Reliability score: 99.36% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown