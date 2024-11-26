# Results vs. 3.13.0

- fork: python
- ref: c8db0e817e7e0db50153
- machine: windows-x86
- commit hash: c8db0e8
- commit date: 2024-10-03
- overall geometric mean: 1.015x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241003-pythonperf1_win32-x86-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 255 ms                                                          | 250 ms: 1.02x faster                                                           |
| docutils       | 1.80 sec                                                        | 1.87 sec: 1.04x slower                                                         |
| html5lib       | 47.1 ms                                                         | 46.2 ms: 1.02x faster                                                          |
| Geometric mean | (ref)                                                           | 1.00x slower                                                                   |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241003-pythonperf1_win32-x86-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 287 ms                                                          | 257 ms: 1.12x faster                                                           |
| async_tree_none            | 245 ms                                                          | 220 ms: 1.11x faster                                                           |
| async_tree_memoization     | 302 ms                                                          | 276 ms: 1.09x faster                                                           |
| async_tree_none_tg         | 216 ms                                                          | 202 ms: 1.07x faster                                                           |
| async_tree_cpu_io_mixed_tg | 469 ms                                                          | 475 ms: 1.01x slower                                                           |
| async_tree_io              | 530 ms                                                          | 545 ms: 1.03x slower                                                           |
| async_tree_io_tg           | 499 ms                                                          | 527 ms: 1.05x slower                                                           |
| async_generators           | 267 ms                                                          | 302 ms: 1.13x slower                                                           |
| coroutines                 | 16.1 ms                                                         | 18.5 ms: 1.15x slower                                                          |
| Geometric mean             | (ref)                                                           | 1.00x faster                                                                   |

Benchmark hidden because not significant (1): async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241003-pythonperf1_win32-x86-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pidigits       | 204 ms                                                          | 200 ms: 1.02x faster                                                           |
| float          | 56.4 ms                                                         | 61.7 ms: 1.09x slower                                                          |
| nbody          | 81.4 ms                                                         | 91.6 ms: 1.13x slower                                                          |
| Geometric mean | (ref)                                                           | 1.06x slower                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241003-pythonperf1_win32-x86-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_v8       | 15.5 ms                                                         | 16.2 ms: 1.05x slower                                                          |
| regex_effbot   | 1.82 ms                                                         | 1.92 ms: 1.06x slower                                                          |
| regex_dna      | 112 ms                                                          | 120 ms: 1.07x slower                                                           |
| regex_compile  | 101 ms                                                          | 110 ms: 1.09x slower                                                           |
| Geometric mean | (ref)                                                           | 1.07x slower                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241003-pythonperf1_win32-x86-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| json_loads           | 21.7 us                                                         | 21.3 us: 1.02x faster                                                          |
| xml_etree_parse      | 102 ms                                                          | 108 ms: 1.05x slower                                                           |
| tomli_loads          | 1.74 sec                                                        | 1.92 sec: 1.10x slower                                                         |
| xml_etree_iterparse  | 61.3 ms                                                         | 68.0 ms: 1.11x slower                                                          |
| xml_etree_generate   | 61.9 ms                                                         | 69.1 ms: 1.12x slower                                                          |
| pickle_pure_python   | 239 us                                                          | 268 us: 1.12x slower                                                           |
| unpickle_pure_python | 162 us                                                          | 183 us: 1.13x slower                                                           |
| xml_etree_process    | 44.6 ms                                                         | 50.7 ms: 1.14x slower                                                          |
| Geometric mean       | (ref)                                                           | 1.08x slower                                                                   |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241003-pythonperf1_win32-x86-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 28.3 ms                                                         | 24.1 ms: 1.18x faster                                                          |
| python_startup_no_site | 20.2 ms                                                         | 19.7 ms: 1.02x faster                                                          |
| Geometric mean         | (ref)                                                           | 1.10x faster                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241003-pythonperf1_win32-x86-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| genshi_text     | 21.7 ms                                                         | 22.6 ms: 1.04x slower                                                          |
| django_template | 32.0 ms                                                         | 34.3 ms: 1.07x slower                                                          |
| mako            | 7.02 ms                                                         | 8.12 ms: 1.16x slower                                                          |
| Geometric mean  | (ref)                                                           | 1.06x slower                                                                   |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241003-pythonperf1_win32-x86-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| thrift                     | 10.3 ms                                                         | 769 us: 13.34x faster                                                          |
| coverage                   | 326 ms                                                          | 53.6 ms: 6.09x faster                                                          |
| create_gc_cycles           | 1.08 ms                                                         | 732 us: 1.48x faster                                                           |
| bench_mp_pool              | 93.6 ms                                                         | 72.9 ms: 1.29x faster                                                          |
| deepcopy                   | 311 us                                                          | 247 us: 1.26x faster                                                           |
| gc_traversal               | 1.76 ms                                                         | 1.43 ms: 1.24x faster                                                          |
| python_startup             | 28.3 ms                                                         | 24.1 ms: 1.18x faster                                                          |
| deepcopy_memo              | 26.2 us                                                         | 22.9 us: 1.15x faster                                                          |
| deepcopy_reduce            | 2.94 us                                                         | 2.58 us: 1.14x faster                                                          |
| async_tree_memoization_tg  | 287 ms                                                          | 257 ms: 1.12x faster                                                           |
| async_tree_none            | 245 ms                                                          | 220 ms: 1.11x faster                                                           |
| async_tree_memoization     | 302 ms                                                          | 276 ms: 1.09x faster                                                           |
| async_tree_none_tg         | 216 ms                                                          | 202 ms: 1.07x faster                                                           |
| pathlib                    | 89.1 ms                                                         | 86.5 ms: 1.03x faster                                                          |
| json                       | 4.40 ms                                                         | 4.28 ms: 1.03x faster                                                          |
| python_startup_no_site     | 20.2 ms                                                         | 19.7 ms: 1.02x faster                                                          |
| 2to3                       | 255 ms                                                          | 250 ms: 1.02x faster                                                           |
| html5lib                   | 47.1 ms                                                         | 46.2 ms: 1.02x faster                                                          |
| json_loads                 | 21.7 us                                                         | 21.3 us: 1.02x faster                                                          |
| pidigits                   | 204 ms                                                          | 200 ms: 1.02x faster                                                           |
| go                         | 111 ms                                                          | 110 ms: 1.01x faster                                                           |
| pycparser                  | 869 ms                                                          | 861 ms: 1.01x faster                                                           |
| async_tree_cpu_io_mixed_tg | 469 ms                                                          | 475 ms: 1.01x slower                                                           |
| sympy_str                  | 214 ms                                                          | 218 ms: 1.02x slower                                                           |
| sympy_expand               | 377 ms                                                          | 385 ms: 1.02x slower                                                           |
| crypto_pyaes               | 56.6 ms                                                         | 57.8 ms: 1.02x slower                                                          |
| meteor_contest             | 78.1 ms                                                         | 79.8 ms: 1.02x slower                                                          |
| async_tree_io              | 530 ms                                                          | 545 ms: 1.03x slower                                                           |
| sympy_integrate            | 15.2 ms                                                         | 15.7 ms: 1.03x slower                                                          |
| pprint_safe_repr           | 658 ms                                                          | 680 ms: 1.03x slower                                                           |
| telco                      | 6.27 ms                                                         | 6.48 ms: 1.03x slower                                                          |
| logging_simple             | 7.89 us                                                         | 8.18 us: 1.04x slower                                                          |
| logging_format             | 8.59 us                                                         | 8.92 us: 1.04x slower                                                          |
| docutils                   | 1.80 sec                                                        | 1.87 sec: 1.04x slower                                                         |
| genshi_text                | 21.7 ms                                                         | 22.6 ms: 1.04x slower                                                          |
| mdp                        | 1.70 sec                                                        | 1.77 sec: 1.04x slower                                                         |
| dulwich_log                | 50.2 ms                                                         | 52.5 ms: 1.05x slower                                                          |
| sqlglot_transpile          | 1.26 ms                                                         | 1.32 ms: 1.05x slower                                                          |
| regex_v8                   | 15.5 ms                                                         | 16.2 ms: 1.05x slower                                                          |
| pylint                     | 225 ms                                                          | 236 ms: 1.05x slower                                                           |
| typing_runtime_protocols   | 141 us                                                          | 148 us: 1.05x slower                                                           |
| sqlglot_parse              | 1.02 ms                                                         | 1.07 ms: 1.05x slower                                                          |
| xml_etree_parse            | 102 ms                                                          | 108 ms: 1.05x slower                                                           |
| async_tree_io_tg           | 499 ms                                                          | 527 ms: 1.05x slower                                                           |
| pprint_pformat             | 1.32 sec                                                        | 1.40 sec: 1.06x slower                                                         |
| regex_effbot               | 1.82 ms                                                         | 1.92 ms: 1.06x slower                                                          |
| sqlglot_normalize          | 223 ms                                                          | 236 ms: 1.06x slower                                                           |
| comprehensions             | 13.1 us                                                         | 14.0 us: 1.06x slower                                                          |
| django_template            | 32.0 ms                                                         | 34.3 ms: 1.07x slower                                                          |
| sqlglot_optimize           | 42.4 ms                                                         | 45.5 ms: 1.07x slower                                                          |
| regex_dna                  | 112 ms                                                          | 120 ms: 1.07x slower                                                           |
| scimark_sparse_mat_mult    | 2.88 ms                                                         | 3.11 ms: 1.08x slower                                                          |
| fannkuch                   | 288 ms                                                          | 313 ms: 1.09x slower                                                           |
| regex_compile              | 101 ms                                                          | 110 ms: 1.09x slower                                                           |
| float                      | 56.4 ms                                                         | 61.7 ms: 1.09x slower                                                          |
| tomli_loads                | 1.74 sec                                                        | 1.92 sec: 1.10x slower                                                         |
| xml_etree_iterparse        | 61.3 ms                                                         | 68.0 ms: 1.11x slower                                                          |
| xml_etree_generate         | 61.9 ms                                                         | 69.1 ms: 1.12x slower                                                          |
| pickle_pure_python         | 239 us                                                          | 268 us: 1.12x slower                                                           |
| spectral_norm              | 70.0 ms                                                         | 78.5 ms: 1.12x slower                                                          |
| nbody                      | 81.4 ms                                                         | 91.6 ms: 1.13x slower                                                          |
| async_generators           | 267 ms                                                          | 302 ms: 1.13x slower                                                           |
| unpickle_pure_python       | 162 us                                                          | 183 us: 1.13x slower                                                           |
| scimark_monte_carlo        | 48.7 ms                                                         | 55.3 ms: 1.13x slower                                                          |
| xml_etree_process          | 44.6 ms                                                         | 50.7 ms: 1.14x slower                                                          |
| hexiom                     | 4.60 ms                                                         | 5.23 ms: 1.14x slower                                                          |
| scimark_lu                 | 60.7 ms                                                         | 69.2 ms: 1.14x slower                                                          |
| chaos                      | 49.4 ms                                                         | 56.2 ms: 1.14x slower                                                          |
| scimark_fft                | 204 ms                                                          | 233 ms: 1.14x slower                                                           |
| pyflate                    | 322 ms                                                          | 370 ms: 1.15x slower                                                           |
| coroutines                 | 16.1 ms                                                         | 18.5 ms: 1.15x slower                                                          |
| scimark_sor                | 85.8 ms                                                         | 99.0 ms: 1.15x slower                                                          |
| mako                       | 7.02 ms                                                         | 8.12 ms: 1.16x slower                                                          |
| logging_silent             | 62.4 ns                                                         | 74.7 ns: 1.20x slower                                                          |
| deltablue                  | 2.35 ms                                                         | 2.82 ms: 1.20x slower                                                          |
| richards                   | 33.4 ms                                                         | 41.4 ms: 1.24x slower                                                          |
| generators                 | 21.5 ms                                                         | 26.7 ms: 1.24x slower                                                          |
| richards_super             | 37.0 ms                                                         | 46.2 ms: 1.25x slower                                                          |
| raytrace                   | 203 ms                                                          | 260 ms: 1.28x slower                                                           |
| Geometric mean             | (ref)                                                           | 1.02x faster                                                                   |

Benchmark hidden because not significant (7): bench_thread_pool, genshi_xml, nqueens, json_dumps, sympy_sum, tornado_http, async_tree_cpu_io_mixed
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: asyncio_websockets, bpe_tokeniser, chameleon, connected_components, gevent_hub, k_core, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20241003-3.14.0a0-c8db0e8/bm-20241003-pythonperf1_win32-x86-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.015x faster
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: unknown