# Results vs. 3.13.0

- fork: python
- ref: e913d2c87f1ae4e7a4ae
- machine: windows-x86
- commit hash: e913d2c
- commit date: 2024-08-15
- overall geometric mean: 1.022x faster
- HPT reliability: 99.97%
- HPT 99th percentile: 1.01x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240815-pythonperf1_win32-x86-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 255 ms                                                          | 254 ms: 1.01x faster                                                           |
| docutils       | 1.80 sec                                                        | 1.94 sec: 1.08x slower                                                         |
| html5lib       | 47.1 ms                                                         | 48.6 ms: 1.03x slower                                                          |
| Geometric mean | (ref)                                                           | 1.03x slower                                                                   |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240815-pythonperf1_win32-x86-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 287 ms                                                          | 252 ms: 1.14x faster                                                           |
| async_tree_memoization     | 302 ms                                                          | 279 ms: 1.08x faster                                                           |
| async_tree_none_tg         | 216 ms                                                          | 200 ms: 1.08x faster                                                           |
| async_tree_none            | 245 ms                                                          | 228 ms: 1.08x faster                                                           |
| async_tree_cpu_io_mixed    | 490 ms                                                          | 472 ms: 1.04x faster                                                           |
| async_tree_cpu_io_mixed_tg | 469 ms                                                          | 462 ms: 1.02x faster                                                           |
| async_tree_io_tg           | 499 ms                                                          | 513 ms: 1.03x slower                                                           |
| async_tree_io              | 530 ms                                                          | 552 ms: 1.04x slower                                                           |
| coroutines                 | 16.1 ms                                                         | 17.6 ms: 1.09x slower                                                          |
| async_generators           | 267 ms                                                          | 307 ms: 1.15x slower                                                           |
| Geometric mean             | (ref)                                                           | 1.01x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240815-pythonperf1_win32-x86-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pidigits       | 204 ms                                                          | 198 ms: 1.03x faster                                                           |
| float          | 56.4 ms                                                         | 61.2 ms: 1.08x slower                                                          |
| nbody          | 81.4 ms                                                         | 93.3 ms: 1.15x slower                                                          |
| Geometric mean | (ref)                                                           | 1.06x slower                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240815-pythonperf1_win32-x86-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_v8       | 15.5 ms                                                         | 16.2 ms: 1.05x slower                                                          |
| regex_compile  | 101 ms                                                          | 107 ms: 1.06x slower                                                           |
| regex_effbot   | 1.82 ms                                                         | 1.93 ms: 1.06x slower                                                          |
| regex_dna      | 112 ms                                                          | 119 ms: 1.06x slower                                                           |
| Geometric mean | (ref)                                                           | 1.06x slower                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240815-pythonperf1_win32-x86-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| json_loads           | 21.7 us                                                         | 20.3 us: 1.07x faster                                                          |
| json_dumps           | 7.53 ms                                                         | 7.70 ms: 1.02x slower                                                          |
| xml_etree_parse      | 102 ms                                                          | 108 ms: 1.06x slower                                                           |
| pickle_pure_python   | 239 us                                                          | 254 us: 1.06x slower                                                           |
| tomli_loads          | 1.74 sec                                                        | 1.88 sec: 1.08x slower                                                         |
| unpickle_pure_python | 162 us                                                          | 178 us: 1.10x slower                                                           |
| xml_etree_iterparse  | 61.3 ms                                                         | 69.0 ms: 1.13x slower                                                          |
| xml_etree_generate   | 61.9 ms                                                         | 70.0 ms: 1.13x slower                                                          |
| xml_etree_process    | 44.6 ms                                                         | 51.2 ms: 1.15x slower                                                          |
| Geometric mean       | (ref)                                                           | 1.07x slower                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240815-pythonperf1_win32-x86-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 28.3 ms                                                         | 24.0 ms: 1.18x faster                                                          |
| python_startup_no_site | 20.2 ms                                                         | 19.9 ms: 1.02x faster                                                          |
| Geometric mean         | (ref)                                                           | 1.10x faster                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240815-pythonperf1_win32-x86-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| genshi_xml      | 49.0 ms                                                         | 46.8 ms: 1.05x faster                                                          |
| django_template | 32.0 ms                                                         | 31.8 ms: 1.01x faster                                                          |
| genshi_text     | 21.7 ms                                                         | 22.7 ms: 1.04x slower                                                          |
| mako            | 7.02 ms                                                         | 8.13 ms: 1.16x slower                                                          |
| Geometric mean  | (ref)                                                           | 1.03x slower                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240815-pythonperf1_win32-x86-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| thrift                     | 10.3 ms                                                         | 737 us: 13.92x faster                                                          |
| coverage                   | 326 ms                                                          | 53.0 ms: 6.16x faster                                                          |
| create_gc_cycles           | 1.08 ms                                                         | 746 us: 1.45x faster                                                           |
| bench_mp_pool              | 93.6 ms                                                         | 72.7 ms: 1.29x faster                                                          |
| gc_traversal               | 1.76 ms                                                         | 1.44 ms: 1.22x faster                                                          |
| deepcopy                   | 311 us                                                          | 255 us: 1.22x faster                                                           |
| python_startup             | 28.3 ms                                                         | 24.0 ms: 1.18x faster                                                          |
| deepcopy_reduce            | 2.94 us                                                         | 2.55 us: 1.15x faster                                                          |
| deepcopy_memo              | 26.2 us                                                         | 22.8 us: 1.15x faster                                                          |
| async_tree_memoization_tg  | 287 ms                                                          | 252 ms: 1.14x faster                                                           |
| async_tree_memoization     | 302 ms                                                          | 279 ms: 1.08x faster                                                           |
| async_tree_none_tg         | 216 ms                                                          | 200 ms: 1.08x faster                                                           |
| async_tree_none            | 245 ms                                                          | 228 ms: 1.08x faster                                                           |
| json_loads                 | 21.7 us                                                         | 20.3 us: 1.07x faster                                                          |
| genshi_xml                 | 49.0 ms                                                         | 46.8 ms: 1.05x faster                                                          |
| json                       | 4.40 ms                                                         | 4.22 ms: 1.04x faster                                                          |
| async_tree_cpu_io_mixed    | 490 ms                                                          | 472 ms: 1.04x faster                                                           |
| pidigits                   | 204 ms                                                          | 198 ms: 1.03x faster                                                           |
| pprint_safe_repr           | 658 ms                                                          | 639 ms: 1.03x faster                                                           |
| pathlib                    | 89.1 ms                                                         | 87.3 ms: 1.02x faster                                                          |
| python_startup_no_site     | 20.2 ms                                                         | 19.9 ms: 1.02x faster                                                          |
| async_tree_cpu_io_mixed_tg | 469 ms                                                          | 462 ms: 1.02x faster                                                           |
| pycparser                  | 869 ms                                                          | 858 ms: 1.01x faster                                                           |
| telco                      | 6.27 ms                                                         | 6.20 ms: 1.01x faster                                                          |
| django_template            | 32.0 ms                                                         | 31.8 ms: 1.01x faster                                                          |
| dulwich_log                | 50.2 ms                                                         | 49.8 ms: 1.01x faster                                                          |
| 2to3                       | 255 ms                                                          | 254 ms: 1.01x faster                                                           |
| mdp                        | 1.70 sec                                                        | 1.71 sec: 1.01x slower                                                         |
| logging_simple             | 7.89 us                                                         | 7.95 us: 1.01x slower                                                          |
| sympy_expand               | 377 ms                                                          | 382 ms: 1.01x slower                                                           |
| crypto_pyaes               | 56.6 ms                                                         | 57.6 ms: 1.02x slower                                                          |
| sympy_sum                  | 108 ms                                                          | 110 ms: 1.02x slower                                                           |
| json_dumps                 | 7.53 ms                                                         | 7.70 ms: 1.02x slower                                                          |
| sympy_str                  | 214 ms                                                          | 220 ms: 1.03x slower                                                           |
| async_tree_io_tg           | 499 ms                                                          | 513 ms: 1.03x slower                                                           |
| typing_runtime_protocols   | 141 us                                                          | 145 us: 1.03x slower                                                           |
| pprint_pformat             | 1.32 sec                                                        | 1.36 sec: 1.03x slower                                                         |
| sympy_integrate            | 15.2 ms                                                         | 15.7 ms: 1.03x slower                                                          |
| sqlglot_normalize          | 223 ms                                                          | 230 ms: 1.03x slower                                                           |
| html5lib                   | 47.1 ms                                                         | 48.6 ms: 1.03x slower                                                          |
| sqlglot_optimize           | 42.4 ms                                                         | 43.8 ms: 1.03x slower                                                          |
| async_tree_io              | 530 ms                                                          | 552 ms: 1.04x slower                                                           |
| genshi_text                | 21.7 ms                                                         | 22.7 ms: 1.04x slower                                                          |
| regex_v8                   | 15.5 ms                                                         | 16.2 ms: 1.05x slower                                                          |
| pylint                     | 225 ms                                                          | 236 ms: 1.05x slower                                                           |
| comprehensions             | 13.1 us                                                         | 13.8 us: 1.05x slower                                                          |
| chaos                      | 49.4 ms                                                         | 52.0 ms: 1.05x slower                                                          |
| regex_compile              | 101 ms                                                          | 107 ms: 1.06x slower                                                           |
| xml_etree_parse            | 102 ms                                                          | 108 ms: 1.06x slower                                                           |
| meteor_contest             | 78.1 ms                                                         | 82.9 ms: 1.06x slower                                                          |
| pickle_pure_python         | 239 us                                                          | 254 us: 1.06x slower                                                           |
| regex_effbot               | 1.82 ms                                                         | 1.93 ms: 1.06x slower                                                          |
| regex_dna                  | 112 ms                                                          | 119 ms: 1.06x slower                                                           |
| sqlglot_transpile          | 1.26 ms                                                         | 1.35 ms: 1.07x slower                                                          |
| sqlglot_parse              | 1.02 ms                                                         | 1.09 ms: 1.07x slower                                                          |
| go                         | 111 ms                                                          | 118 ms: 1.07x slower                                                           |
| nqueens                    | 75.1 ms                                                         | 80.6 ms: 1.07x slower                                                          |
| raytrace                   | 203 ms                                                          | 218 ms: 1.07x slower                                                           |
| docutils                   | 1.80 sec                                                        | 1.94 sec: 1.08x slower                                                         |
| tomli_loads                | 1.74 sec                                                        | 1.88 sec: 1.08x slower                                                         |
| scimark_sparse_mat_mult    | 2.88 ms                                                         | 3.12 ms: 1.08x slower                                                          |
| float                      | 56.4 ms                                                         | 61.2 ms: 1.08x slower                                                          |
| coroutines                 | 16.1 ms                                                         | 17.6 ms: 1.09x slower                                                          |
| unpickle_pure_python       | 162 us                                                          | 178 us: 1.10x slower                                                           |
| spectral_norm              | 70.0 ms                                                         | 78.2 ms: 1.12x slower                                                          |
| xml_etree_iterparse        | 61.3 ms                                                         | 69.0 ms: 1.13x slower                                                          |
| scimark_fft                | 204 ms                                                          | 230 ms: 1.13x slower                                                           |
| xml_etree_generate         | 61.9 ms                                                         | 70.0 ms: 1.13x slower                                                          |
| scimark_lu                 | 60.7 ms                                                         | 69.4 ms: 1.14x slower                                                          |
| nbody                      | 81.4 ms                                                         | 93.3 ms: 1.15x slower                                                          |
| xml_etree_process          | 44.6 ms                                                         | 51.2 ms: 1.15x slower                                                          |
| async_generators           | 267 ms                                                          | 307 ms: 1.15x slower                                                           |
| mako                       | 7.02 ms                                                         | 8.13 ms: 1.16x slower                                                          |
| deltablue                  | 2.35 ms                                                         | 2.72 ms: 1.16x slower                                                          |
| hexiom                     | 4.60 ms                                                         | 5.33 ms: 1.16x slower                                                          |
| scimark_sor                | 85.8 ms                                                         | 99.6 ms: 1.16x slower                                                          |
| richards                   | 33.4 ms                                                         | 38.8 ms: 1.16x slower                                                          |
| pyflate                    | 322 ms                                                          | 379 ms: 1.18x slower                                                           |
| richards_super             | 37.0 ms                                                         | 43.6 ms: 1.18x slower                                                          |
| scimark_monte_carlo        | 48.7 ms                                                         | 57.5 ms: 1.18x slower                                                          |
| fannkuch                   | 288 ms                                                          | 347 ms: 1.20x slower                                                           |
| logging_silent             | 62.4 ns                                                         | 77.1 ns: 1.24x slower                                                          |
| generators                 | 21.5 ms                                                         | 27.2 ms: 1.27x slower                                                          |
| Geometric mean             | (ref)                                                           | 1.02x faster                                                                   |

Benchmark hidden because not significant (3): bench_thread_pool, logging_format, tornado_http
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: asyncio_websockets, bpe_tokeniser, chameleon, connected_components, gevent_hub, k_core, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (2) of results/bm-20240815-3.14.0a0-e913d2c/bm-20240815-pythonperf1_win32-x86-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c.json: asyncio_tcp, asyncio_tcp_ssl

- Geometric mean (including insignificant results): 1.022x faster
# HPT report

- Reliability score: 99.97% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: unknown