# Results vs. 3.13.0

- fork: python
- ref: v3.14.0a1
- machine: windows-x86
- commit hash: 8cdaca8
- commit date: 2024-10-15
- overall geometric mean: 1.015x faster
- HPT reliability: 99.95%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241015-pythonperf1_win32-x86-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 255 ms                                                          | 246 ms: 1.04x faster                                                |
| docutils       | 1.80 sec                                                        | 1.85 sec: 1.03x slower                                              |
| html5lib       | 47.1 ms                                                         | 44.9 ms: 1.05x faster                                               |
| sphinx         | 729 ms                                                          | 758 ms: 1.04x slower                                                |
| Geometric mean | (ref)                                                           | 1.01x faster                                                        |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241015-pythonperf1_win32-x86-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_memoization_tg  | 287 ms                                                          | 256 ms: 1.12x faster                                                |
| async_tree_none            | 245 ms                                                          | 223 ms: 1.10x faster                                                |
| async_tree_memoization     | 302 ms                                                          | 280 ms: 1.08x faster                                                |
| async_tree_none_tg         | 216 ms                                                          | 205 ms: 1.05x faster                                                |
| async_tree_cpu_io_mixed    | 490 ms                                                          | 467 ms: 1.05x faster                                                |
| async_tree_cpu_io_mixed_tg | 469 ms                                                          | 465 ms: 1.01x faster                                                |
| coroutines                 | 16.1 ms                                                         | 17.1 ms: 1.06x slower                                               |
| async_tree_io_tg           | 499 ms                                                          | 558 ms: 1.12x slower                                                |
| async_generators           | 267 ms                                                          | 306 ms: 1.14x slower                                                |
| Geometric mean             | (ref)                                                           | 1.01x faster                                                        |

Benchmark hidden because not significant (1): async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241015-pythonperf1_win32-x86-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| pidigits       | 204 ms                                                          | 199 ms: 1.02x faster                                                |
| nbody          | 81.4 ms                                                         | 87.2 ms: 1.07x slower                                               |
| float          | 56.4 ms                                                         | 61.9 ms: 1.10x slower                                               |
| Geometric mean | (ref)                                                           | 1.05x slower                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241015-pythonperf1_win32-x86-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_v8       | 15.5 ms                                                         | 15.8 ms: 1.02x slower                                               |
| regex_compile  | 101 ms                                                          | 105 ms: 1.04x slower                                                |
| regex_dna      | 112 ms                                                          | 118 ms: 1.05x slower                                                |
| Geometric mean | (ref)                                                           | 1.03x slower                                                        |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241015-pythonperf1_win32-x86-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| json_loads           | 21.7 us                                                         | 20.5 us: 1.06x faster                                               |
| xml_etree_process    | 44.6 ms                                                         | 47.6 ms: 1.07x slower                                               |
| tomli_loads          | 1.74 sec                                                        | 1.87 sec: 1.07x slower                                              |
| xml_etree_generate   | 61.9 ms                                                         | 66.5 ms: 1.07x slower                                               |
| unpickle_pure_python | 162 us                                                          | 178 us: 1.10x slower                                                |
| xml_etree_parse      | 102 ms                                                          | 113 ms: 1.10x slower                                                |
| pickle_pure_python   | 239 us                                                          | 265 us: 1.11x slower                                                |
| xml_etree_iterparse  | 61.3 ms                                                         | 69.5 ms: 1.13x slower                                               |
| json_dumps           | 7.53 ms                                                         | 9.09 ms: 1.21x slower                                               |
| Geometric mean       | (ref)                                                           | 1.09x slower                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241015-pythonperf1_win32-x86-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup | 28.3 ms                                                         | 26.6 ms: 1.06x faster                                               |
| Geometric mean | (ref)                                                           | 1.03x faster                                                        |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241015-pythonperf1_win32-x86-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| genshi_xml      | 49.0 ms                                                         | 45.9 ms: 1.07x faster                                               |
| genshi_text     | 21.7 ms                                                         | 20.6 ms: 1.05x faster                                               |
| django_template | 32.0 ms                                                         | 32.5 ms: 1.01x slower                                               |
| mako            | 7.02 ms                                                         | 7.83 ms: 1.11x slower                                               |
| Geometric mean  | (ref)                                                           | 1.00x slower                                                        |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241015-pythonperf1_win32-x86-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| thrift                     | 10.3 ms                                                         | 762 us: 13.47x faster                                               |
| coverage                   | 326 ms                                                          | 51.9 ms: 6.29x faster                                               |
| deepcopy                   | 311 us                                                          | 242 us: 1.28x faster                                                |
| deepcopy_memo              | 26.2 us                                                         | 22.3 us: 1.18x faster                                               |
| deepcopy_reduce            | 2.94 us                                                         | 2.55 us: 1.15x faster                                               |
| async_tree_memoization_tg  | 287 ms                                                          | 256 ms: 1.12x faster                                                |
| go                         | 111 ms                                                          | 99.5 ms: 1.11x faster                                               |
| async_tree_none            | 245 ms                                                          | 223 ms: 1.10x faster                                                |
| async_tree_memoization     | 302 ms                                                          | 280 ms: 1.08x faster                                                |
| genshi_xml                 | 49.0 ms                                                         | 45.9 ms: 1.07x faster                                               |
| python_startup             | 28.3 ms                                                         | 26.6 ms: 1.06x faster                                               |
| json_loads                 | 21.7 us                                                         | 20.5 us: 1.06x faster                                               |
| genshi_text                | 21.7 ms                                                         | 20.6 ms: 1.05x faster                                               |
| pycparser                  | 869 ms                                                          | 825 ms: 1.05x faster                                                |
| bench_mp_pool              | 93.6 ms                                                         | 89.0 ms: 1.05x faster                                               |
| async_tree_none_tg         | 216 ms                                                          | 205 ms: 1.05x faster                                                |
| html5lib                   | 47.1 ms                                                         | 44.9 ms: 1.05x faster                                               |
| async_tree_cpu_io_mixed    | 490 ms                                                          | 467 ms: 1.05x faster                                                |
| bench_thread_pool          | 1.04 ms                                                         | 997 us: 1.04x faster                                                |
| 2to3                       | 255 ms                                                          | 246 ms: 1.04x faster                                                |
| pidigits                   | 204 ms                                                          | 199 ms: 1.02x faster                                                |
| async_tree_cpu_io_mixed_tg | 469 ms                                                          | 465 ms: 1.01x faster                                                |
| pathlib                    | 89.1 ms                                                         | 88.2 ms: 1.01x faster                                               |
| sympy_sum                  | 108 ms                                                          | 107 ms: 1.01x faster                                                |
| nqueens                    | 75.1 ms                                                         | 74.5 ms: 1.01x faster                                               |
| sqlglot_normalize          | 223 ms                                                          | 224 ms: 1.01x slower                                                |
| pprint_safe_repr           | 658 ms                                                          | 662 ms: 1.01x slower                                                |
| logging_simple             | 7.89 us                                                         | 7.95 us: 1.01x slower                                               |
| mdp                        | 1.70 sec                                                        | 1.72 sec: 1.01x slower                                              |
| logging_format             | 8.59 us                                                         | 8.70 us: 1.01x slower                                               |
| django_template            | 32.0 ms                                                         | 32.5 ms: 1.01x slower                                               |
| sympy_str                  | 214 ms                                                          | 218 ms: 1.02x slower                                                |
| comprehensions             | 13.1 us                                                         | 13.4 us: 1.02x slower                                               |
| typing_runtime_protocols   | 141 us                                                          | 143 us: 1.02x slower                                                |
| sympy_integrate            | 15.2 ms                                                         | 15.5 ms: 1.02x slower                                               |
| regex_v8                   | 15.5 ms                                                         | 15.8 ms: 1.02x slower                                               |
| gc_traversal               | 1.76 ms                                                         | 1.81 ms: 1.03x slower                                               |
| sympy_expand               | 377 ms                                                          | 387 ms: 1.03x slower                                                |
| meteor_contest             | 78.1 ms                                                         | 80.3 ms: 1.03x slower                                               |
| docutils                   | 1.80 sec                                                        | 1.85 sec: 1.03x slower                                              |
| sqlglot_optimize           | 42.4 ms                                                         | 43.6 ms: 1.03x slower                                               |
| pprint_pformat             | 1.32 sec                                                        | 1.37 sec: 1.04x slower                                              |
| sphinx                     | 729 ms                                                          | 758 ms: 1.04x slower                                                |
| regex_compile              | 101 ms                                                          | 105 ms: 1.04x slower                                                |
| sqlglot_parse              | 1.02 ms                                                         | 1.06 ms: 1.04x slower                                               |
| sqlglot_transpile          | 1.26 ms                                                         | 1.32 ms: 1.04x slower                                               |
| dulwich_log                | 50.2 ms                                                         | 52.5 ms: 1.05x slower                                               |
| regex_dna                  | 112 ms                                                          | 118 ms: 1.05x slower                                                |
| telco                      | 6.27 ms                                                         | 6.58 ms: 1.05x slower                                               |
| coroutines                 | 16.1 ms                                                         | 17.1 ms: 1.06x slower                                               |
| crypto_pyaes               | 56.6 ms                                                         | 60.0 ms: 1.06x slower                                               |
| xml_etree_process          | 44.6 ms                                                         | 47.6 ms: 1.07x slower                                               |
| nbody                      | 81.4 ms                                                         | 87.2 ms: 1.07x slower                                               |
| tomli_loads                | 1.74 sec                                                        | 1.87 sec: 1.07x slower                                              |
| xml_etree_generate         | 61.9 ms                                                         | 66.5 ms: 1.07x slower                                               |
| float                      | 56.4 ms                                                         | 61.9 ms: 1.10x slower                                               |
| unpickle_pure_python       | 162 us                                                          | 178 us: 1.10x slower                                                |
| hexiom                     | 4.60 ms                                                         | 5.05 ms: 1.10x slower                                               |
| scimark_sparse_mat_mult    | 2.88 ms                                                         | 3.17 ms: 1.10x slower                                               |
| xml_etree_parse            | 102 ms                                                          | 113 ms: 1.10x slower                                                |
| create_gc_cycles           | 1.08 ms                                                         | 1.19 ms: 1.10x slower                                               |
| spectral_norm              | 70.0 ms                                                         | 77.3 ms: 1.10x slower                                               |
| pickle_pure_python         | 239 us                                                          | 265 us: 1.11x slower                                                |
| scimark_lu                 | 60.7 ms                                                         | 67.6 ms: 1.11x slower                                               |
| logging_silent             | 62.4 ns                                                         | 69.5 ns: 1.11x slower                                               |
| mako                       | 7.02 ms                                                         | 7.83 ms: 1.11x slower                                               |
| async_tree_io_tg           | 499 ms                                                          | 558 ms: 1.12x slower                                                |
| generators                 | 21.5 ms                                                         | 24.1 ms: 1.12x slower                                               |
| chaos                      | 49.4 ms                                                         | 55.4 ms: 1.12x slower                                               |
| scimark_fft                | 204 ms                                                          | 230 ms: 1.13x slower                                                |
| fannkuch                   | 288 ms                                                          | 325 ms: 1.13x slower                                                |
| xml_etree_iterparse        | 61.3 ms                                                         | 69.5 ms: 1.13x slower                                               |
| deltablue                  | 2.35 ms                                                         | 2.68 ms: 1.14x slower                                               |
| pyflate                    | 322 ms                                                          | 368 ms: 1.14x slower                                                |
| async_generators           | 267 ms                                                          | 306 ms: 1.14x slower                                                |
| raytrace                   | 203 ms                                                          | 236 ms: 1.17x slower                                                |
| scimark_monte_carlo        | 48.7 ms                                                         | 58.2 ms: 1.19x slower                                               |
| scimark_sor                | 85.8 ms                                                         | 103 ms: 1.20x slower                                                |
| json_dumps                 | 7.53 ms                                                         | 9.09 ms: 1.21x slower                                               |
| richards                   | 33.4 ms                                                         | 41.5 ms: 1.24x slower                                               |
| richards_super             | 37.0 ms                                                         | 47.3 ms: 1.28x slower                                               |
| json                       | 4.40 ms                                                         | 5.97 ms: 1.36x slower                                               |
| Geometric mean             | (ref)                                                           | 1.01x faster                                                        |

Benchmark hidden because not significant (5): tornado_http, python_startup_no_site, regex_effbot, async_tree_io, pylint
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: asyncio_websockets, bpe_tokeniser, chameleon, connected_components, gevent_hub, k_core, shortest_path, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20241015-3.14.0a1-8cdaca8/bm-20241015-pythonperf1_win32-x86-python-v3.14.0a1-3.14.0a1-8cdaca8.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.015x faster
# HPT report

- Reliability score: 99.95% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown