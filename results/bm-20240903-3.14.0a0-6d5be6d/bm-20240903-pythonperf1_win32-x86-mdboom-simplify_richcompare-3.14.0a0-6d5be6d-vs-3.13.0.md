# Results vs. 3.13.0

- fork: mdboom
- ref: simplify_richcompare
- machine: windows-x86
- commit hash: 6d5be6d
- commit date: 2024-09-03
- overall geometric mean: 1.027x faster
- HPT reliability: 99.42%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240903-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 255 ms                                                          | 249 ms: 1.02x faster                                                           |
| docutils       | 1.80 sec                                                        | 1.86 sec: 1.03x slower                                                         |
| html5lib       | 47.1 ms                                                         | 46.1 ms: 1.02x faster                                                          |
| Geometric mean | (ref)                                                           | 1.00x faster                                                                   |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240903-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 287 ms                                                          | 247 ms: 1.16x faster                                                           |
| async_tree_none            | 245 ms                                                          | 216 ms: 1.14x faster                                                           |
| async_tree_memoization     | 302 ms                                                          | 272 ms: 1.11x faster                                                           |
| async_tree_none_tg         | 216 ms                                                          | 198 ms: 1.09x faster                                                           |
| async_tree_cpu_io_mixed    | 490 ms                                                          | 465 ms: 1.05x faster                                                           |
| async_tree_cpu_io_mixed_tg | 469 ms                                                          | 463 ms: 1.01x faster                                                           |
| async_tree_io_tg           | 499 ms                                                          | 509 ms: 1.02x slower                                                           |
| coroutines                 | 16.1 ms                                                         | 17.8 ms: 1.10x slower                                                          |
| async_generators           | 267 ms                                                          | 297 ms: 1.11x slower                                                           |
| Geometric mean             | (ref)                                                           | 1.03x faster                                                                   |

Benchmark hidden because not significant (1): async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240903-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pidigits       | 204 ms                                                          | 202 ms: 1.01x faster                                                           |
| float          | 56.4 ms                                                         | 61.5 ms: 1.09x slower                                                          |
| nbody          | 81.4 ms                                                         | 96.0 ms: 1.18x slower                                                          |
| Geometric mean | (ref)                                                           | 1.08x slower                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240903-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_v8       | 15.5 ms                                                         | 16.4 ms: 1.06x slower                                                          |
| regex_compile  | 101 ms                                                          | 107 ms: 1.06x slower                                                           |
| regex_effbot   | 1.82 ms                                                         | 1.93 ms: 1.06x slower                                                          |
| regex_dna      | 112 ms                                                          | 121 ms: 1.08x slower                                                           |
| Geometric mean | (ref)                                                           | 1.06x slower                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240903-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| json_loads           | 21.7 us                                                         | 21.1 us: 1.03x faster                                                          |
| json_dumps           | 7.53 ms                                                         | 7.46 ms: 1.01x faster                                                          |
| xml_etree_parse      | 102 ms                                                          | 107 ms: 1.05x slower                                                           |
| pickle_pure_python   | 239 us                                                          | 251 us: 1.05x slower                                                           |
| tomli_loads          | 1.74 sec                                                        | 1.86 sec: 1.07x slower                                                         |
| xml_etree_generate   | 61.9 ms                                                         | 67.3 ms: 1.09x slower                                                          |
| xml_etree_iterparse  | 61.3 ms                                                         | 67.7 ms: 1.11x slower                                                          |
| unpickle_pure_python | 162 us                                                          | 179 us: 1.11x slower                                                           |
| xml_etree_process    | 44.6 ms                                                         | 50.0 ms: 1.12x slower                                                          |
| Geometric mean       | (ref)                                                           | 1.06x slower                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240903-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 28.3 ms                                                         | 23.8 ms: 1.19x faster                                                          |
| python_startup_no_site | 20.2 ms                                                         | 19.7 ms: 1.02x faster                                                          |
| Geometric mean         | (ref)                                                           | 1.10x faster                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240903-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| genshi_xml      | 49.0 ms                                                         | 46.1 ms: 1.06x faster                                                          |
| genshi_text     | 21.7 ms                                                         | 21.9 ms: 1.01x slower                                                          |
| django_template | 32.0 ms                                                         | 32.9 ms: 1.03x slower                                                          |
| mako            | 7.02 ms                                                         | 8.20 ms: 1.17x slower                                                          |
| Geometric mean  | (ref)                                                           | 1.03x slower                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240903-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| thrift                     | 10.3 ms                                                         | 741 us: 13.85x faster                                                          |
| coverage                   | 326 ms                                                          | 51.8 ms: 6.30x faster                                                          |
| create_gc_cycles           | 1.08 ms                                                         | 754 us: 1.44x faster                                                           |
| deepcopy                   | 311 us                                                          | 238 us: 1.30x faster                                                           |
| bench_mp_pool              | 93.6 ms                                                         | 73.2 ms: 1.28x faster                                                          |
| gc_traversal               | 1.76 ms                                                         | 1.44 ms: 1.23x faster                                                          |
| deepcopy_reduce            | 2.94 us                                                         | 2.46 us: 1.20x faster                                                          |
| python_startup             | 28.3 ms                                                         | 23.8 ms: 1.19x faster                                                          |
| deepcopy_memo              | 26.2 us                                                         | 22.0 us: 1.19x faster                                                          |
| async_tree_memoization_tg  | 287 ms                                                          | 247 ms: 1.16x faster                                                           |
| async_tree_none            | 245 ms                                                          | 216 ms: 1.14x faster                                                           |
| async_tree_memoization     | 302 ms                                                          | 272 ms: 1.11x faster                                                           |
| async_tree_none_tg         | 216 ms                                                          | 198 ms: 1.09x faster                                                           |
| go                         | 111 ms                                                          | 104 ms: 1.07x faster                                                           |
| genshi_xml                 | 49.0 ms                                                         | 46.1 ms: 1.06x faster                                                          |
| async_tree_cpu_io_mixed    | 490 ms                                                          | 465 ms: 1.05x faster                                                           |
| bench_thread_pool          | 1.04 ms                                                         | 1.01 ms: 1.03x faster                                                          |
| json_loads                 | 21.7 us                                                         | 21.1 us: 1.03x faster                                                          |
| json                       | 4.40 ms                                                         | 4.28 ms: 1.03x faster                                                          |
| pathlib                    | 89.1 ms                                                         | 86.9 ms: 1.02x faster                                                          |
| pprint_safe_repr           | 658 ms                                                          | 643 ms: 1.02x faster                                                           |
| 2to3                       | 255 ms                                                          | 249 ms: 1.02x faster                                                           |
| html5lib                   | 47.1 ms                                                         | 46.1 ms: 1.02x faster                                                          |
| python_startup_no_site     | 20.2 ms                                                         | 19.7 ms: 1.02x faster                                                          |
| dulwich_log                | 50.2 ms                                                         | 49.2 ms: 1.02x faster                                                          |
| async_tree_cpu_io_mixed_tg | 469 ms                                                          | 463 ms: 1.01x faster                                                           |
| json_dumps                 | 7.53 ms                                                         | 7.46 ms: 1.01x faster                                                          |
| sympy_sum                  | 108 ms                                                          | 107 ms: 1.01x faster                                                           |
| pidigits                   | 204 ms                                                          | 202 ms: 1.01x faster                                                           |
| logging_format             | 8.59 us                                                         | 8.65 us: 1.01x slower                                                          |
| genshi_text                | 21.7 ms                                                         | 21.9 ms: 1.01x slower                                                          |
| sympy_str                  | 214 ms                                                          | 216 ms: 1.01x slower                                                           |
| sqlglot_optimize           | 42.4 ms                                                         | 42.9 ms: 1.01x slower                                                          |
| sympy_integrate            | 15.2 ms                                                         | 15.5 ms: 1.02x slower                                                          |
| async_tree_io_tg           | 499 ms                                                          | 509 ms: 1.02x slower                                                           |
| sympy_expand               | 377 ms                                                          | 384 ms: 1.02x slower                                                           |
| pycparser                  | 869 ms                                                          | 888 ms: 1.02x slower                                                           |
| django_template            | 32.0 ms                                                         | 32.9 ms: 1.03x slower                                                          |
| docutils                   | 1.80 sec                                                        | 1.86 sec: 1.03x slower                                                         |
| comprehensions             | 13.1 us                                                         | 13.6 us: 1.03x slower                                                          |
| xml_etree_parse            | 102 ms                                                          | 107 ms: 1.05x slower                                                           |
| pylint                     | 225 ms                                                          | 235 ms: 1.05x slower                                                           |
| pickle_pure_python         | 239 us                                                          | 251 us: 1.05x slower                                                           |
| meteor_contest             | 78.1 ms                                                         | 82.0 ms: 1.05x slower                                                          |
| crypto_pyaes               | 56.6 ms                                                         | 59.5 ms: 1.05x slower                                                          |
| sqlglot_parse              | 1.02 ms                                                         | 1.07 ms: 1.05x slower                                                          |
| nqueens                    | 75.1 ms                                                         | 79.3 ms: 1.06x slower                                                          |
| typing_runtime_protocols   | 141 us                                                          | 149 us: 1.06x slower                                                           |
| regex_v8                   | 15.5 ms                                                         | 16.4 ms: 1.06x slower                                                          |
| sqlglot_transpile          | 1.26 ms                                                         | 1.33 ms: 1.06x slower                                                          |
| regex_compile              | 101 ms                                                          | 107 ms: 1.06x slower                                                           |
| regex_effbot               | 1.82 ms                                                         | 1.93 ms: 1.06x slower                                                          |
| tomli_loads                | 1.74 sec                                                        | 1.86 sec: 1.07x slower                                                         |
| regex_dna                  | 112 ms                                                          | 121 ms: 1.08x slower                                                           |
| telco                      | 6.27 ms                                                         | 6.77 ms: 1.08x slower                                                          |
| xml_etree_generate         | 61.9 ms                                                         | 67.3 ms: 1.09x slower                                                          |
| float                      | 56.4 ms                                                         | 61.5 ms: 1.09x slower                                                          |
| scimark_sparse_mat_mult    | 2.88 ms                                                         | 3.15 ms: 1.09x slower                                                          |
| chaos                      | 49.4 ms                                                         | 54.1 ms: 1.10x slower                                                          |
| spectral_norm              | 70.0 ms                                                         | 76.9 ms: 1.10x slower                                                          |
| coroutines                 | 16.1 ms                                                         | 17.8 ms: 1.10x slower                                                          |
| xml_etree_iterparse        | 61.3 ms                                                         | 67.7 ms: 1.11x slower                                                          |
| unpickle_pure_python       | 162 us                                                          | 179 us: 1.11x slower                                                           |
| pyflate                    | 322 ms                                                          | 358 ms: 1.11x slower                                                           |
| async_generators           | 267 ms                                                          | 297 ms: 1.11x slower                                                           |
| xml_etree_process          | 44.6 ms                                                         | 50.0 ms: 1.12x slower                                                          |
| raytrace                   | 203 ms                                                          | 231 ms: 1.14x slower                                                           |
| scimark_lu                 | 60.7 ms                                                         | 70.0 ms: 1.15x slower                                                          |
| scimark_monte_carlo        | 48.7 ms                                                         | 56.4 ms: 1.16x slower                                                          |
| scimark_fft                | 204 ms                                                          | 237 ms: 1.16x slower                                                           |
| hexiom                     | 4.60 ms                                                         | 5.36 ms: 1.17x slower                                                          |
| mako                       | 7.02 ms                                                         | 8.20 ms: 1.17x slower                                                          |
| deltablue                  | 2.35 ms                                                         | 2.75 ms: 1.17x slower                                                          |
| nbody                      | 81.4 ms                                                         | 96.0 ms: 1.18x slower                                                          |
| fannkuch                   | 288 ms                                                          | 342 ms: 1.19x slower                                                           |
| scimark_sor                | 85.8 ms                                                         | 102 ms: 1.19x slower                                                           |
| logging_silent             | 62.4 ns                                                         | 74.8 ns: 1.20x slower                                                          |
| richards                   | 33.4 ms                                                         | 41.9 ms: 1.25x slower                                                          |
| richards_super             | 37.0 ms                                                         | 46.9 ms: 1.27x slower                                                          |
| generators                 | 21.5 ms                                                         | 27.6 ms: 1.29x slower                                                          |
| Geometric mean             | (ref)                                                           | 1.03x faster                                                                   |

Benchmark hidden because not significant (6): tornado_http, mdp, async_tree_io, sqlglot_normalize, pprint_pformat, logging_simple
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: asyncio_websockets, bpe_tokeniser, chameleon, connected_components, gevent_hub, k_core, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (2) of results/bm-20240903-3.14.0a0-6d5be6d/bm-20240903-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-6d5be6d.json: asyncio_tcp, asyncio_tcp_ssl

- Geometric mean (including insignificant results): 1.027x faster
# HPT report

- Reliability score: 99.42% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown