# Results vs. 3.13.0

- fork: python
- ref: 401fff7423ca3c8bf1d0
- machine: windows-x86
- commit hash: 401fff7
- commit date: 2024-09-14
- overall geometric mean: 1.025x faster
- HPT reliability: 99.96%
- HPT 99th percentile: 1.01x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240914-pythonperf1_win32-x86-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 255 ms                                                          | 249 ms: 1.03x faster                                                           |
| docutils       | 1.80 sec                                                        | 1.85 sec: 1.03x slower                                                         |
| html5lib       | 47.1 ms                                                         | 47.3 ms: 1.00x slower                                                          |
| tornado_http   | 105 ms                                                          | 95.2 ms: 1.10x faster                                                          |
| Geometric mean | (ref)                                                           | 1.02x faster                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240914-pythonperf1_win32-x86-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 287 ms                                                          | 253 ms: 1.14x faster                                                           |
| async_tree_none            | 245 ms                                                          | 221 ms: 1.11x faster                                                           |
| async_tree_memoization     | 302 ms                                                          | 276 ms: 1.09x faster                                                           |
| async_tree_none_tg         | 216 ms                                                          | 201 ms: 1.07x faster                                                           |
| async_tree_cpu_io_mixed    | 490 ms                                                          | 466 ms: 1.05x faster                                                           |
| async_tree_cpu_io_mixed_tg | 469 ms                                                          | 461 ms: 1.02x faster                                                           |
| async_tree_io              | 530 ms                                                          | 542 ms: 1.02x slower                                                           |
| async_tree_io_tg           | 499 ms                                                          | 522 ms: 1.04x slower                                                           |
| async_generators           | 267 ms                                                          | 291 ms: 1.09x slower                                                           |
| coroutines                 | 16.1 ms                                                         | 18.5 ms: 1.15x slower                                                          |
| Geometric mean             | (ref)                                                           | 1.02x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240914-pythonperf1_win32-x86-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pidigits       | 204 ms                                                          | 198 ms: 1.03x faster                                                           |
| float          | 56.4 ms                                                         | 61.6 ms: 1.09x slower                                                          |
| nbody          | 81.4 ms                                                         | 94.2 ms: 1.16x slower                                                          |
| Geometric mean | (ref)                                                           | 1.07x slower                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240914-pythonperf1_win32-x86-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_effbot   | 1.82 ms                                                         | 1.91 ms: 1.05x slower                                                          |
| regex_v8       | 15.5 ms                                                         | 16.3 ms: 1.06x slower                                                          |
| regex_dna      | 112 ms                                                          | 119 ms: 1.06x slower                                                           |
| regex_compile  | 101 ms                                                          | 109 ms: 1.08x slower                                                           |
| Geometric mean | (ref)                                                           | 1.06x slower                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240914-pythonperf1_win32-x86-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| json_loads           | 21.7 us                                                         | 20.7 us: 1.05x faster                                                          |
| json_dumps           | 7.53 ms                                                         | 7.43 ms: 1.01x faster                                                          |
| xml_etree_parse      | 102 ms                                                          | 108 ms: 1.06x slower                                                           |
| tomli_loads          | 1.74 sec                                                        | 1.87 sec: 1.08x slower                                                         |
| xml_etree_generate   | 61.9 ms                                                         | 67.8 ms: 1.10x slower                                                          |
| xml_etree_iterparse  | 61.3 ms                                                         | 67.8 ms: 1.11x slower                                                          |
| unpickle_pure_python | 162 us                                                          | 179 us: 1.11x slower                                                           |
| pickle_pure_python   | 239 us                                                          | 269 us: 1.12x slower                                                           |
| xml_etree_process    | 44.6 ms                                                         | 50.1 ms: 1.12x slower                                                          |
| Geometric mean       | (ref)                                                           | 1.07x slower                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240914-pythonperf1_win32-x86-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup | 28.3 ms                                                         | 23.9 ms: 1.18x faster                                                          |
| Geometric mean | (ref)                                                           | 1.09x faster                                                                   |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240914-pythonperf1_win32-x86-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| django_template | 32.0 ms                                                         | 34.7 ms: 1.08x slower                                                          |
| mako            | 7.02 ms                                                         | 8.00 ms: 1.14x slower                                                          |
| Geometric mean  | (ref)                                                           | 1.05x slower                                                                   |

Benchmark hidden because not significant (2): genshi_xml, genshi_text

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240914-pythonperf1_win32-x86-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| thrift                     | 10.3 ms                                                         | 748 us: 13.71x faster                                                          |
| coverage                   | 326 ms                                                          | 53.2 ms: 6.13x faster                                                          |
| create_gc_cycles           | 1.08 ms                                                         | 735 us: 1.47x faster                                                           |
| bench_mp_pool              | 93.6 ms                                                         | 71.5 ms: 1.31x faster                                                          |
| deepcopy                   | 311 us                                                          | 244 us: 1.28x faster                                                           |
| gc_traversal               | 1.76 ms                                                         | 1.41 ms: 1.25x faster                                                          |
| deepcopy_memo              | 26.2 us                                                         | 21.8 us: 1.20x faster                                                          |
| python_startup             | 28.3 ms                                                         | 23.9 ms: 1.18x faster                                                          |
| deepcopy_reduce            | 2.94 us                                                         | 2.53 us: 1.16x faster                                                          |
| async_tree_memoization_tg  | 287 ms                                                          | 253 ms: 1.14x faster                                                           |
| async_tree_none            | 245 ms                                                          | 221 ms: 1.11x faster                                                           |
| tornado_http               | 105 ms                                                          | 95.2 ms: 1.10x faster                                                          |
| async_tree_memoization     | 302 ms                                                          | 276 ms: 1.09x faster                                                           |
| pathlib                    | 89.1 ms                                                         | 82.9 ms: 1.08x faster                                                          |
| async_tree_none_tg         | 216 ms                                                          | 201 ms: 1.07x faster                                                           |
| async_tree_cpu_io_mixed    | 490 ms                                                          | 466 ms: 1.05x faster                                                           |
| json_loads                 | 21.7 us                                                         | 20.7 us: 1.05x faster                                                          |
| bench_thread_pool          | 1.04 ms                                                         | 1.00 ms: 1.04x faster                                                          |
| pidigits                   | 204 ms                                                          | 198 ms: 1.03x faster                                                           |
| 2to3                       | 255 ms                                                          | 249 ms: 1.03x faster                                                           |
| json                       | 4.40 ms                                                         | 4.29 ms: 1.02x faster                                                          |
| async_tree_cpu_io_mixed_tg | 469 ms                                                          | 461 ms: 1.02x faster                                                           |
| json_dumps                 | 7.53 ms                                                         | 7.43 ms: 1.01x faster                                                          |
| nqueens                    | 75.1 ms                                                         | 74.4 ms: 1.01x faster                                                          |
| sympy_sum                  | 108 ms                                                          | 107 ms: 1.01x faster                                                           |
| html5lib                   | 47.1 ms                                                         | 47.3 ms: 1.00x slower                                                          |
| pycparser                  | 869 ms                                                          | 876 ms: 1.01x slower                                                           |
| go                         | 111 ms                                                          | 112 ms: 1.01x slower                                                           |
| sympy_str                  | 214 ms                                                          | 217 ms: 1.01x slower                                                           |
| dulwich_log                | 50.2 ms                                                         | 50.9 ms: 1.01x slower                                                          |
| sympy_integrate            | 15.2 ms                                                         | 15.4 ms: 1.01x slower                                                          |
| pprint_safe_repr           | 658 ms                                                          | 670 ms: 1.02x slower                                                           |
| sympy_expand               | 377 ms                                                          | 385 ms: 1.02x slower                                                           |
| async_tree_io              | 530 ms                                                          | 542 ms: 1.02x slower                                                           |
| logging_format             | 8.59 us                                                         | 8.81 us: 1.03x slower                                                          |
| docutils                   | 1.80 sec                                                        | 1.85 sec: 1.03x slower                                                         |
| crypto_pyaes               | 56.6 ms                                                         | 58.3 ms: 1.03x slower                                                          |
| logging_simple             | 7.89 us                                                         | 8.15 us: 1.03x slower                                                          |
| sqlglot_normalize          | 223 ms                                                          | 230 ms: 1.03x slower                                                           |
| pprint_pformat             | 1.32 sec                                                        | 1.37 sec: 1.04x slower                                                         |
| sqlglot_parse              | 1.02 ms                                                         | 1.06 ms: 1.04x slower                                                          |
| meteor_contest             | 78.1 ms                                                         | 81.0 ms: 1.04x slower                                                          |
| sqlglot_transpile          | 1.26 ms                                                         | 1.32 ms: 1.04x slower                                                          |
| async_tree_io_tg           | 499 ms                                                          | 522 ms: 1.04x slower                                                           |
| sqlglot_optimize           | 42.4 ms                                                         | 44.4 ms: 1.05x slower                                                          |
| regex_effbot               | 1.82 ms                                                         | 1.91 ms: 1.05x slower                                                          |
| typing_runtime_protocols   | 141 us                                                          | 148 us: 1.05x slower                                                           |
| comprehensions             | 13.1 us                                                         | 13.9 us: 1.05x slower                                                          |
| regex_v8                   | 15.5 ms                                                         | 16.3 ms: 1.06x slower                                                          |
| xml_etree_parse            | 102 ms                                                          | 108 ms: 1.06x slower                                                           |
| regex_dna                  | 112 ms                                                          | 119 ms: 1.06x slower                                                           |
| mdp                        | 1.70 sec                                                        | 1.80 sec: 1.06x slower                                                         |
| tomli_loads                | 1.74 sec                                                        | 1.87 sec: 1.08x slower                                                         |
| spectral_norm              | 70.0 ms                                                         | 75.6 ms: 1.08x slower                                                          |
| scimark_sparse_mat_mult    | 2.88 ms                                                         | 3.12 ms: 1.08x slower                                                          |
| django_template            | 32.0 ms                                                         | 34.7 ms: 1.08x slower                                                          |
| regex_compile              | 101 ms                                                          | 109 ms: 1.08x slower                                                           |
| async_generators           | 267 ms                                                          | 291 ms: 1.09x slower                                                           |
| float                      | 56.4 ms                                                         | 61.6 ms: 1.09x slower                                                          |
| xml_etree_generate         | 61.9 ms                                                         | 67.8 ms: 1.10x slower                                                          |
| pyflate                    | 322 ms                                                          | 353 ms: 1.10x slower                                                           |
| xml_etree_iterparse        | 61.3 ms                                                         | 67.8 ms: 1.11x slower                                                          |
| unpickle_pure_python       | 162 us                                                          | 179 us: 1.11x slower                                                           |
| chaos                      | 49.4 ms                                                         | 54.7 ms: 1.11x slower                                                          |
| fannkuch                   | 288 ms                                                          | 322 ms: 1.12x slower                                                           |
| telco                      | 6.27 ms                                                         | 7.04 ms: 1.12x slower                                                          |
| pickle_pure_python         | 239 us                                                          | 269 us: 1.12x slower                                                           |
| xml_etree_process          | 44.6 ms                                                         | 50.1 ms: 1.12x slower                                                          |
| scimark_lu                 | 60.7 ms                                                         | 69.0 ms: 1.14x slower                                                          |
| mako                       | 7.02 ms                                                         | 8.00 ms: 1.14x slower                                                          |
| scimark_sor                | 85.8 ms                                                         | 98.3 ms: 1.15x slower                                                          |
| coroutines                 | 16.1 ms                                                         | 18.5 ms: 1.15x slower                                                          |
| hexiom                     | 4.60 ms                                                         | 5.27 ms: 1.15x slower                                                          |
| nbody                      | 81.4 ms                                                         | 94.2 ms: 1.16x slower                                                          |
| scimark_fft                | 204 ms                                                          | 236 ms: 1.16x slower                                                           |
| scimark_monte_carlo        | 48.7 ms                                                         | 56.9 ms: 1.17x slower                                                          |
| raytrace                   | 203 ms                                                          | 238 ms: 1.17x slower                                                           |
| deltablue                  | 2.35 ms                                                         | 2.79 ms: 1.19x slower                                                          |
| richards                   | 33.4 ms                                                         | 40.0 ms: 1.20x slower                                                          |
| logging_silent             | 62.4 ns                                                         | 75.0 ns: 1.20x slower                                                          |
| generators                 | 21.5 ms                                                         | 25.9 ms: 1.20x slower                                                          |
| richards_super             | 37.0 ms                                                         | 46.0 ms: 1.24x slower                                                          |
| Geometric mean             | (ref)                                                           | 1.03x faster                                                                   |

Benchmark hidden because not significant (4): genshi_xml, genshi_text, python_startup_no_site, pylint
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: asyncio_websockets, bpe_tokeniser, chameleon, connected_components, gevent_hub, k_core, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20240914-3.14.0a0-401fff7/bm-20240914-pythonperf1_win32-x86-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.025x faster
# HPT report

- Reliability score: 99.96% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: unknown