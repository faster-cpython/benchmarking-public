# Results vs. 3.13.0

- fork: python
- ref: ad056f03aee8000a1564
- machine: windows-x86
- commit hash: ad056f0
- commit date: 2023-10-13
- overall geometric mean: 1.266x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.29x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20231013-pythonperf1_win32-x86-python-ad056f03aee8000a1564-3.13.0a1-ad056f0 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 255 ms                                                          | 309 ms: 1.21x slower                                                           |
| chameleon      | 6.24 ms                                                         | 9.20 ms: 1.47x slower                                                          |
| docutils       | 1.80 sec                                                        | 2.17 sec: 1.21x slower                                                         |
| tornado_http   | 105 ms                                                          | 116 ms: 1.11x slower                                                           |
| Geometric mean | (ref)                                                           | 1.24x slower                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20231013-pythonperf1_win32-x86-python-ad056f03aee8000a1564-3.13.0a1-ad056f0 |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed    | 490 ms                                                          | 579 ms: 1.18x slower                                                           |
| async_tree_cpu_io_mixed_tg | 469 ms                                                          | 569 ms: 1.21x slower                                                           |
| async_tree_none            | 245 ms                                                          | 317 ms: 1.30x slower                                                           |
| async_tree_memoization     | 302 ms                                                          | 396 ms: 1.31x slower                                                           |
| async_tree_memoization_tg  | 287 ms                                                          | 386 ms: 1.35x slower                                                           |
| async_generators           | 267 ms                                                          | 365 ms: 1.37x slower                                                           |
| async_tree_none_tg         | 216 ms                                                          | 304 ms: 1.41x slower                                                           |
| async_tree_io              | 530 ms                                                          | 757 ms: 1.43x slower                                                           |
| async_tree_io_tg           | 499 ms                                                          | 743 ms: 1.49x slower                                                           |
| coroutines                 | 16.1 ms                                                         | 28.2 ms: 1.75x slower                                                          |
| Geometric mean             | (ref)                                                           | 1.37x slower                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20231013-pythonperf1_win32-x86-python-ad056f03aee8000a1564-3.13.0a1-ad056f0 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pidigits       | 204 ms                                                          | 198 ms: 1.03x faster                                                           |
| float          | 56.4 ms                                                         | 92.7 ms: 1.64x slower                                                          |
| nbody          | 81.4 ms                                                         | 167 ms: 2.06x slower                                                           |
| Geometric mean | (ref)                                                           | 1.49x slower                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20231013-pythonperf1_win32-x86-python-ad056f03aee8000a1564-3.13.0a1-ad056f0 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_dna      | 112 ms                                                          | 119 ms: 1.06x slower                                                           |
| regex_effbot   | 1.82 ms                                                         | 1.93 ms: 1.06x slower                                                          |
| regex_v8       | 15.5 ms                                                         | 16.8 ms: 1.09x slower                                                          |
| regex_compile  | 101 ms                                                          | 159 ms: 1.58x slower                                                           |
| Geometric mean | (ref)                                                           | 1.18x slower                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20231013-pythonperf1_win32-x86-python-ad056f03aee8000a1564-3.13.0a1-ad056f0 |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| json_loads           | 21.7 us                                                         | 20.4 us: 1.06x faster                                                          |
| json_dumps           | 7.53 ms                                                         | 8.05 ms: 1.07x slower                                                          |
| xml_etree_parse      | 102 ms                                                          | 114 ms: 1.11x slower                                                           |
| xml_etree_generate   | 61.9 ms                                                         | 84.7 ms: 1.37x slower                                                          |
| xml_etree_iterparse  | 61.3 ms                                                         | 86.1 ms: 1.40x slower                                                          |
| xml_etree_process    | 44.6 ms                                                         | 64.0 ms: 1.43x slower                                                          |
| pickle_pure_python   | 239 us                                                          | 348 us: 1.45x slower                                                           |
| tomli_loads          | 1.74 sec                                                        | 2.79 sec: 1.60x slower                                                         |
| unpickle_pure_python | 162 us                                                          | 279 us: 1.73x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.32x slower                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20231013-pythonperf1_win32-x86-python-ad056f03aee8000a1564-3.13.0a1-ad056f0 |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 28.3 ms                                                         | 22.3 ms: 1.27x faster                                                          |
| python_startup_no_site | 20.2 ms                                                         | 19.6 ms: 1.03x faster                                                          |
| Geometric mean         | (ref)                                                           | 1.14x faster                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20231013-pythonperf1_win32-x86-python-ad056f03aee8000a1564-3.13.0a1-ad056f0 |
|-----------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako      | 7.02 ms                                                         | 12.4 ms: 1.77x slower                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20231013-pythonperf1_win32-x86-python-ad056f03aee8000a1564-3.13.0a1-ad056f0 |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| sqlglot_normalize          | 223 ms                                                          | 118 ms: 1.89x faster                                                           |
| create_gc_cycles           | 1.08 ms                                                         | 645 us: 1.68x faster                                                           |
| gc_traversal               | 1.76 ms                                                         | 1.39 ms: 1.27x faster                                                          |
| python_startup             | 28.3 ms                                                         | 22.3 ms: 1.27x faster                                                          |
| bench_mp_pool              | 93.6 ms                                                         | 73.9 ms: 1.27x faster                                                          |
| json_loads                 | 21.7 us                                                         | 20.4 us: 1.06x faster                                                          |
| pidigits                   | 204 ms                                                          | 198 ms: 1.03x faster                                                           |
| python_startup_no_site     | 20.2 ms                                                         | 19.6 ms: 1.03x faster                                                          |
| typing_runtime_protocols   | 141 us                                                          | 143 us: 1.01x slower                                                           |
| pathlib                    | 89.1 ms                                                         | 90.9 ms: 1.02x slower                                                          |
| regex_dna                  | 112 ms                                                          | 119 ms: 1.06x slower                                                           |
| regex_effbot               | 1.82 ms                                                         | 1.93 ms: 1.06x slower                                                          |
| json_dumps                 | 7.53 ms                                                         | 8.05 ms: 1.07x slower                                                          |
| regex_v8                   | 15.5 ms                                                         | 16.8 ms: 1.09x slower                                                          |
| telco                      | 6.27 ms                                                         | 6.92 ms: 1.10x slower                                                          |
| tornado_http               | 105 ms                                                          | 116 ms: 1.11x slower                                                           |
| xml_etree_parse            | 102 ms                                                          | 114 ms: 1.11x slower                                                           |
| bench_thread_pool          | 1.04 ms                                                         | 1.18 ms: 1.13x slower                                                          |
| async_tree_cpu_io_mixed    | 490 ms                                                          | 579 ms: 1.18x slower                                                           |
| docutils                   | 1.80 sec                                                        | 2.17 sec: 1.21x slower                                                         |
| 2to3                       | 255 ms                                                          | 309 ms: 1.21x slower                                                           |
| sympy_expand               | 377 ms                                                          | 457 ms: 1.21x slower                                                           |
| async_tree_cpu_io_mixed_tg | 469 ms                                                          | 569 ms: 1.21x slower                                                           |
| mdp                        | 1.70 sec                                                        | 2.06 sec: 1.21x slower                                                         |
| meteor_contest             | 78.1 ms                                                         | 96.7 ms: 1.24x slower                                                          |
| deepcopy_reduce            | 2.94 us                                                         | 3.73 us: 1.27x slower                                                          |
| sympy_sum                  | 108 ms                                                          | 139 ms: 1.29x slower                                                           |
| sympy_str                  | 214 ms                                                          | 276 ms: 1.29x slower                                                           |
| async_tree_none            | 245 ms                                                          | 317 ms: 1.30x slower                                                           |
| pycparser                  | 869 ms                                                          | 1.13 sec: 1.30x slower                                                         |
| async_tree_memoization     | 302 ms                                                          | 396 ms: 1.31x slower                                                           |
| sqlglot_optimize           | 42.4 ms                                                         | 55.9 ms: 1.32x slower                                                          |
| sympy_integrate            | 15.2 ms                                                         | 20.1 ms: 1.32x slower                                                          |
| crypto_pyaes               | 56.6 ms                                                         | 76.0 ms: 1.34x slower                                                          |
| logging_format             | 8.59 us                                                         | 11.6 us: 1.35x slower                                                          |
| async_tree_memoization_tg  | 287 ms                                                          | 386 ms: 1.35x slower                                                           |
| deepcopy                   | 311 us                                                          | 420 us: 1.35x slower                                                           |
| xml_etree_generate         | 61.9 ms                                                         | 84.7 ms: 1.37x slower                                                          |
| async_generators           | 267 ms                                                          | 365 ms: 1.37x slower                                                           |
| pprint_safe_repr           | 658 ms                                                          | 901 ms: 1.37x slower                                                           |
| logging_simple             | 7.89 us                                                         | 10.9 us: 1.38x slower                                                          |
| pprint_pformat             | 1.32 sec                                                        | 1.85 sec: 1.40x slower                                                         |
| xml_etree_iterparse        | 61.3 ms                                                         | 86.1 ms: 1.40x slower                                                          |
| async_tree_none_tg         | 216 ms                                                          | 304 ms: 1.41x slower                                                           |
| async_tree_io              | 530 ms                                                          | 757 ms: 1.43x slower                                                           |
| xml_etree_process          | 44.6 ms                                                         | 64.0 ms: 1.43x slower                                                          |
| sqlglot_transpile          | 1.26 ms                                                         | 1.82 ms: 1.44x slower                                                          |
| nqueens                    | 75.1 ms                                                         | 109 ms: 1.45x slower                                                           |
| pickle_pure_python         | 239 us                                                          | 348 us: 1.45x slower                                                           |
| chameleon                  | 6.24 ms                                                         | 9.20 ms: 1.47x slower                                                          |
| async_tree_io_tg           | 499 ms                                                          | 743 ms: 1.49x slower                                                           |
| sqlglot_parse              | 1.02 ms                                                         | 1.52 ms: 1.49x slower                                                          |
| regex_compile              | 101 ms                                                          | 159 ms: 1.58x slower                                                           |
| go                         | 111 ms                                                          | 175 ms: 1.58x slower                                                           |
| tomli_loads                | 1.74 sec                                                        | 2.79 sec: 1.60x slower                                                         |
| chaos                      | 49.4 ms                                                         | 80.1 ms: 1.62x slower                                                          |
| raytrace                   | 203 ms                                                          | 331 ms: 1.63x slower                                                           |
| float                      | 56.4 ms                                                         | 92.7 ms: 1.64x slower                                                          |
| scimark_fft                | 204 ms                                                          | 335 ms: 1.64x slower                                                           |
| fannkuch                   | 288 ms                                                          | 475 ms: 1.65x slower                                                           |
| scimark_sparse_mat_mult    | 2.88 ms                                                         | 4.77 ms: 1.65x slower                                                          |
| pyflate                    | 322 ms                                                          | 539 ms: 1.67x slower                                                           |
| scimark_monte_carlo        | 48.7 ms                                                         | 83.1 ms: 1.71x slower                                                          |
| unpickle_pure_python       | 162 us                                                          | 279 us: 1.73x slower                                                           |
| richards_super             | 37.0 ms                                                         | 64.1 ms: 1.73x slower                                                          |
| coroutines                 | 16.1 ms                                                         | 28.2 ms: 1.75x slower                                                          |
| mako                       | 7.02 ms                                                         | 12.4 ms: 1.77x slower                                                          |
| comprehensions             | 13.1 us                                                         | 23.3 us: 1.77x slower                                                          |
| richards                   | 33.4 ms                                                         | 59.1 ms: 1.77x slower                                                          |
| deepcopy_memo              | 26.2 us                                                         | 49.5 us: 1.89x slower                                                          |
| deltablue                  | 2.35 ms                                                         | 4.47 ms: 1.90x slower                                                          |
| hexiom                     | 4.60 ms                                                         | 8.81 ms: 1.92x slower                                                          |
| spectral_norm              | 70.0 ms                                                         | 135 ms: 1.93x slower                                                           |
| scimark_sor                | 85.8 ms                                                         | 168 ms: 1.96x slower                                                           |
| scimark_lu                 | 60.7 ms                                                         | 123 ms: 2.02x slower                                                           |
| nbody                      | 81.4 ms                                                         | 167 ms: 2.06x slower                                                           |
| coverage                   | 326 ms                                                          | 690 ms: 2.11x slower                                                           |
| logging_silent             | 62.4 ns                                                         | 138 ns: 2.21x slower                                                           |
| generators                 | 21.5 ms                                                         | 50.6 ms: 2.35x slower                                                          |
| Geometric mean             | (ref)                                                           | 1.36x slower                                                                   |

Benchmark hidden because not significant (1): json
Ignored benchmarks (16) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: asyncio_websockets, bpe_tokeniser, connected_components, django_template, dulwich_log, genshi_text, genshi_xml, gevent_hub, html5lib, k_core, pylint, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, thrift
Ignored benchmarks (9) of results/bm-20231013-3.13.0a1-ad056f0-PYTHON_UOPS/bm-20231013-pythonperf1_win32-x86-python-ad056f03aee8000a1564-3.13.0a1-ad056f0.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.266x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.34x
- 95% likely to have a slowdown of 1.32x
- 99% likely to have a slowdown of 1.29x

# Memory
- memory change: unknown