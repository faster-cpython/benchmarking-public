# Results vs. 3.13.0

- fork: python
- ref: v3.13.0a4
- machine: windows-x86
- commit hash: 9d34f60
- commit date: 2024-02-15
- overall geometric mean: 1.034x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240215-pythonperf1_win32-x86-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| chameleon      | 6.24 ms                                                         | 6.01 ms: 1.04x faster                                               |
| docutils       | 1.80 sec                                                        | 1.82 sec: 1.01x slower                                              |
| tornado_http   | 105 ms                                                          | 99.9 ms: 1.05x faster                                               |
| Geometric mean | (ref)                                                           | 1.02x faster                                                        |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240215-pythonperf1_win32-x86-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| coroutines                 | 16.1 ms                                                         | 14.9 ms: 1.08x faster                                               |
| async_tree_cpu_io_mixed    | 490 ms                                                          | 515 ms: 1.05x slower                                                |
| async_tree_none            | 245 ms                                                          | 260 ms: 1.06x slower                                                |
| async_tree_cpu_io_mixed_tg | 469 ms                                                          | 503 ms: 1.07x slower                                                |
| async_tree_memoization     | 302 ms                                                          | 325 ms: 1.08x slower                                                |
| async_tree_memoization_tg  | 287 ms                                                          | 313 ms: 1.09x slower                                                |
| async_generators           | 267 ms                                                          | 300 ms: 1.12x slower                                                |
| async_tree_none_tg         | 216 ms                                                          | 246 ms: 1.14x slower                                                |
| async_tree_io              | 530 ms                                                          | 624 ms: 1.18x slower                                                |
| async_tree_io_tg           | 499 ms                                                          | 612 ms: 1.22x slower                                                |
| Geometric mean             | (ref)                                                           | 1.09x slower                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240215-pythonperf1_win32-x86-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 56.4 ms                                                         | 53.9 ms: 1.05x faster                                               |
| pidigits       | 204 ms                                                          | 202 ms: 1.01x faster                                                |
| nbody          | 81.4 ms                                                         | 89.7 ms: 1.10x slower                                               |
| Geometric mean | (ref)                                                           | 1.01x slower                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240215-pythonperf1_win32-x86-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_v8       | 15.5 ms                                                         | 16.2 ms: 1.05x slower                                               |
| regex_effbot   | 1.82 ms                                                         | 1.91 ms: 1.05x slower                                               |
| regex_dna      | 112 ms                                                          | 120 ms: 1.07x slower                                                |
| regex_compile  | 101 ms                                                          | 110 ms: 1.09x slower                                                |
| Geometric mean | (ref)                                                           | 1.06x slower                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240215-pythonperf1_win32-x86-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| json_dumps           | 7.53 ms                                                         | 6.95 ms: 1.08x faster                                               |
| pickle_pure_python   | 239 us                                                          | 223 us: 1.07x faster                                                |
| json_loads           | 21.7 us                                                         | 20.3 us: 1.07x faster                                               |
| tomli_loads          | 1.74 sec                                                        | 1.65 sec: 1.06x faster                                              |
| xml_etree_process    | 44.6 ms                                                         | 42.8 ms: 1.04x faster                                               |
| unpickle_pure_python | 162 us                                                          | 156 us: 1.04x faster                                                |
| xml_etree_generate   | 61.9 ms                                                         | 60.2 ms: 1.03x faster                                               |
| xml_etree_parse      | 102 ms                                                          | 109 ms: 1.07x slower                                                |
| xml_etree_iterparse  | 61.3 ms                                                         | 65.9 ms: 1.08x slower                                               |
| Geometric mean       | (ref)                                                           | 1.03x faster                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240215-pythonperf1_win32-x86-python-v3.13.0a4-3.13.0a4-9d34f60 |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 28.3 ms                                                         | 22.5 ms: 1.26x faster                                               |
| python_startup_no_site | 20.2 ms                                                         | 20.3 ms: 1.01x slower                                               |
| Geometric mean         | (ref)                                                           | 1.12x faster                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240215-pythonperf1_win32-x86-python-v3.13.0a4-3.13.0a4-9d34f60 |
|-----------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| mako      | 7.02 ms                                                         | 7.43 ms: 1.06x slower                                               |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240215-pythonperf1_win32-x86-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| create_gc_cycles           | 1.08 ms                                                         | 646 us: 1.68x faster                                                |
| typing_runtime_protocols   | 141 us                                                          | 98.7 us: 1.43x faster                                               |
| bench_mp_pool              | 93.6 ms                                                         | 71.5 ms: 1.31x faster                                               |
| python_startup             | 28.3 ms                                                         | 22.5 ms: 1.26x faster                                               |
| gc_traversal               | 1.76 ms                                                         | 1.42 ms: 1.25x faster                                               |
| deepcopy_reduce            | 2.94 us                                                         | 2.51 us: 1.17x faster                                               |
| deepcopy                   | 311 us                                                          | 285 us: 1.09x faster                                                |
| json_dumps                 | 7.53 ms                                                         | 6.95 ms: 1.08x faster                                               |
| coroutines                 | 16.1 ms                                                         | 14.9 ms: 1.08x faster                                               |
| pickle_pure_python         | 239 us                                                          | 223 us: 1.07x faster                                                |
| json_loads                 | 21.7 us                                                         | 20.3 us: 1.07x faster                                               |
| sqlglot_parse              | 1.02 ms                                                         | 961 us: 1.06x faster                                                |
| pathlib                    | 89.1 ms                                                         | 84.3 ms: 1.06x faster                                               |
| tomli_loads                | 1.74 sec                                                        | 1.65 sec: 1.06x faster                                              |
| tornado_http               | 105 ms                                                          | 99.9 ms: 1.05x faster                                               |
| float                      | 56.4 ms                                                         | 53.9 ms: 1.05x faster                                               |
| sqlglot_transpile          | 1.26 ms                                                         | 1.21 ms: 1.04x faster                                               |
| xml_etree_process          | 44.6 ms                                                         | 42.8 ms: 1.04x faster                                               |
| chameleon                  | 6.24 ms                                                         | 6.01 ms: 1.04x faster                                               |
| unpickle_pure_python       | 162 us                                                          | 156 us: 1.04x faster                                                |
| richards                   | 33.4 ms                                                         | 32.2 ms: 1.04x faster                                               |
| deepcopy_memo              | 26.2 us                                                         | 25.3 us: 1.04x faster                                               |
| json                       | 4.40 ms                                                         | 4.27 ms: 1.03x faster                                               |
| xml_etree_generate         | 61.9 ms                                                         | 60.2 ms: 1.03x faster                                               |
| richards_super             | 37.0 ms                                                         | 36.5 ms: 1.02x faster                                               |
| pidigits                   | 204 ms                                                          | 202 ms: 1.01x faster                                                |
| sqlglot_normalize          | 223 ms                                                          | 224 ms: 1.00x slower                                                |
| sympy_expand               | 377 ms                                                          | 379 ms: 1.01x slower                                                |
| python_startup_no_site     | 20.2 ms                                                         | 20.3 ms: 1.01x slower                                               |
| docutils                   | 1.80 sec                                                        | 1.82 sec: 1.01x slower                                              |
| sympy_str                  | 214 ms                                                          | 218 ms: 1.02x slower                                                |
| sympy_sum                  | 108 ms                                                          | 110 ms: 1.02x slower                                                |
| pycparser                  | 869 ms                                                          | 891 ms: 1.03x slower                                                |
| sqlglot_optimize           | 42.4 ms                                                         | 43.7 ms: 1.03x slower                                               |
| logging_format             | 8.59 us                                                         | 8.97 us: 1.04x slower                                               |
| telco                      | 6.27 ms                                                         | 6.55 ms: 1.04x slower                                               |
| scimark_sor                | 85.8 ms                                                         | 89.6 ms: 1.04x slower                                               |
| regex_v8                   | 15.5 ms                                                         | 16.2 ms: 1.05x slower                                               |
| spectral_norm              | 70.0 ms                                                         | 73.2 ms: 1.05x slower                                               |
| sympy_integrate            | 15.2 ms                                                         | 16.0 ms: 1.05x slower                                               |
| async_tree_cpu_io_mixed    | 490 ms                                                          | 515 ms: 1.05x slower                                                |
| regex_effbot               | 1.82 ms                                                         | 1.91 ms: 1.05x slower                                               |
| logging_simple             | 7.89 us                                                         | 8.35 us: 1.06x slower                                               |
| mako                       | 7.02 ms                                                         | 7.43 ms: 1.06x slower                                               |
| async_tree_none            | 245 ms                                                          | 260 ms: 1.06x slower                                                |
| regex_dna                  | 112 ms                                                          | 120 ms: 1.07x slower                                                |
| xml_etree_parse            | 102 ms                                                          | 109 ms: 1.07x slower                                                |
| async_tree_cpu_io_mixed_tg | 469 ms                                                          | 503 ms: 1.07x slower                                                |
| meteor_contest             | 78.1 ms                                                         | 83.8 ms: 1.07x slower                                               |
| comprehensions             | 13.1 us                                                         | 14.1 us: 1.07x slower                                               |
| logging_silent             | 62.4 ns                                                         | 67.1 ns: 1.08x slower                                               |
| async_tree_memoization     | 302 ms                                                          | 325 ms: 1.08x slower                                                |
| xml_etree_iterparse        | 61.3 ms                                                         | 65.9 ms: 1.08x slower                                               |
| crypto_pyaes               | 56.6 ms                                                         | 61.0 ms: 1.08x slower                                               |
| scimark_lu                 | 60.7 ms                                                         | 65.6 ms: 1.08x slower                                               |
| scimark_sparse_mat_mult    | 2.88 ms                                                         | 3.12 ms: 1.08x slower                                               |
| pprint_safe_repr           | 658 ms                                                          | 713 ms: 1.08x slower                                                |
| mdp                        | 1.70 sec                                                        | 1.85 sec: 1.09x slower                                              |
| async_tree_memoization_tg  | 287 ms                                                          | 313 ms: 1.09x slower                                                |
| regex_compile              | 101 ms                                                          | 110 ms: 1.09x slower                                                |
| deltablue                  | 2.35 ms                                                         | 2.58 ms: 1.10x slower                                               |
| nbody                      | 81.4 ms                                                         | 89.7 ms: 1.10x slower                                               |
| go                         | 111 ms                                                          | 123 ms: 1.11x slower                                                |
| fannkuch                   | 288 ms                                                          | 322 ms: 1.12x slower                                                |
| pprint_pformat             | 1.32 sec                                                        | 1.47 sec: 1.12x slower                                              |
| async_generators           | 267 ms                                                          | 300 ms: 1.12x slower                                                |
| async_tree_none_tg         | 216 ms                                                          | 246 ms: 1.14x slower                                                |
| generators                 | 21.5 ms                                                         | 24.6 ms: 1.14x slower                                               |
| pyflate                    | 322 ms                                                          | 370 ms: 1.15x slower                                                |
| scimark_fft                | 204 ms                                                          | 239 ms: 1.17x slower                                                |
| async_tree_io              | 530 ms                                                          | 624 ms: 1.18x slower                                                |
| nqueens                    | 75.1 ms                                                         | 88.7 ms: 1.18x slower                                               |
| raytrace                   | 203 ms                                                          | 240 ms: 1.18x slower                                                |
| async_tree_io_tg           | 499 ms                                                          | 612 ms: 1.22x slower                                                |
| chaos                      | 49.4 ms                                                         | 61.0 ms: 1.24x slower                                               |
| coverage                   | 326 ms                                                          | 464 ms: 1.42x slower                                                |
| hexiom                     | 4.60 ms                                                         | 6.61 ms: 1.44x slower                                               |
| scimark_monte_carlo        | 48.7 ms                                                         | 71.6 ms: 1.47x slower                                               |
| Geometric mean             | (ref)                                                           | 1.03x slower                                                        |

Benchmark hidden because not significant (2): bench_thread_pool, 2to3
Ignored benchmarks (16) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: asyncio_websockets, bpe_tokeniser, connected_components, django_template, dulwich_log, genshi_text, genshi_xml, gevent_hub, html5lib, k_core, pylint, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, thrift
Ignored benchmarks (10) of results/bm-20240215-3.13.0a4-9d34f60-JIT/bm-20240215-pythonperf1_win32-x86-python-v3.13.0a4-3.13.0a4-9d34f60.json: asyncio_tcp, asyncio_tcp_ssl, dask, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.034x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.04x
- 95% likely to have a slowdown of 1.04x
- 99% likely to have a slowdown of 1.03x

# Memory
- memory change: unknown