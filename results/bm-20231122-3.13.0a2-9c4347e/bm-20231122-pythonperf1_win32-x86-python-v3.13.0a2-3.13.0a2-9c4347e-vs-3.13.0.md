# Results vs. 3.13.0

- fork: python
- ref: v3.13.0a2
- machine: windows-x86
- commit hash: 9c4347e
- commit date: 2023-11-22
- overall geometric mean: 1.011x slower
- HPT reliability: 99.42%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20231122-pythonperf1_win32-x86-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 255 ms                                                          | 246 ms: 1.04x faster                                                |
| chameleon      | 6.24 ms                                                         | 5.96 ms: 1.05x faster                                               |
| docutils       | 1.80 sec                                                        | 1.78 sec: 1.01x faster                                              |
| html5lib       | 47.1 ms                                                         | 45.7 ms: 1.03x faster                                               |
| tornado_http   | 105 ms                                                          | 98.2 ms: 1.07x faster                                               |
| Geometric mean | (ref)                                                           | 1.04x faster                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20231122-pythonperf1_win32-x86-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_none            | 245 ms                                                          | 254 ms: 1.04x slower                                                |
| coroutines                 | 16.1 ms                                                         | 16.7 ms: 1.04x slower                                               |
| async_generators           | 267 ms                                                          | 278 ms: 1.04x slower                                                |
| async_tree_cpu_io_mixed    | 490 ms                                                          | 511 ms: 1.04x slower                                                |
| async_tree_memoization     | 302 ms                                                          | 317 ms: 1.05x slower                                                |
| async_tree_cpu_io_mixed_tg | 469 ms                                                          | 506 ms: 1.08x slower                                                |
| async_tree_memoization_tg  | 287 ms                                                          | 312 ms: 1.09x slower                                                |
| async_tree_none_tg         | 216 ms                                                          | 248 ms: 1.15x slower                                                |
| async_tree_io              | 530 ms                                                          | 623 ms: 1.17x slower                                                |
| async_tree_io_tg           | 499 ms                                                          | 619 ms: 1.24x slower                                                |
| Geometric mean             | (ref)                                                           | 1.09x slower                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20231122-pythonperf1_win32-x86-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| pidigits       | 204 ms                                                          | 200 ms: 1.02x faster                                                |
| float          | 56.4 ms                                                         | 59.8 ms: 1.06x slower                                               |
| nbody          | 81.4 ms                                                         | 88.9 ms: 1.09x slower                                               |
| Geometric mean | (ref)                                                           | 1.04x slower                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20231122-pythonperf1_win32-x86-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 101 ms                                                          | 106 ms: 1.05x slower                                                |
| regex_v8       | 15.5 ms                                                         | 16.2 ms: 1.05x slower                                               |
| regex_effbot   | 1.82 ms                                                         | 1.92 ms: 1.06x slower                                               |
| regex_dna      | 112 ms                                                          | 120 ms: 1.07x slower                                                |
| Geometric mean | (ref)                                                           | 1.06x slower                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20231122-pythonperf1_win32-x86-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| json_loads           | 21.7 us                                                         | 19.8 us: 1.10x faster                                               |
| json_dumps           | 7.53 ms                                                         | 6.96 ms: 1.08x faster                                               |
| pickle_pure_python   | 239 us                                                          | 231 us: 1.04x faster                                                |
| unpickle_pure_python | 162 us                                                          | 156 us: 1.04x faster                                                |
| xml_etree_generate   | 61.9 ms                                                         | 62.8 ms: 1.01x slower                                               |
| xml_etree_process    | 44.6 ms                                                         | 45.8 ms: 1.03x slower                                               |
| tomli_loads          | 1.74 sec                                                        | 1.81 sec: 1.04x slower                                              |
| xml_etree_parse      | 102 ms                                                          | 108 ms: 1.05x slower                                                |
| xml_etree_iterparse  | 61.3 ms                                                         | 69.5 ms: 1.13x slower                                               |
| Geometric mean       | (ref)                                                           | 1.00x slower                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20231122-pythonperf1_win32-x86-python-v3.13.0a2-3.13.0a2-9c4347e |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 28.3 ms                                                         | 22.2 ms: 1.27x faster                                               |
| python_startup_no_site | 20.2 ms                                                         | 20.0 ms: 1.01x faster                                               |
| Geometric mean         | (ref)                                                           | 1.13x faster                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20231122-pythonperf1_win32-x86-python-v3.13.0a2-3.13.0a2-9c4347e |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| django_template | 32.0 ms                                                         | 31.2 ms: 1.03x faster                                               |
| mako            | 7.02 ms                                                         | 7.72 ms: 1.10x slower                                               |
| Geometric mean  | (ref)                                                           | 1.01x slower                                                        |

Benchmark hidden because not significant (2): genshi_xml, genshi_text

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20231122-pythonperf1_win32-x86-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| create_gc_cycles           | 1.08 ms                                                         | 645 us: 1.68x faster                                                |
| typing_runtime_protocols   | 141 us                                                          | 98.7 us: 1.43x faster                                               |
| bench_mp_pool              | 93.6 ms                                                         | 69.3 ms: 1.35x faster                                               |
| python_startup             | 28.3 ms                                                         | 22.2 ms: 1.27x faster                                               |
| gc_traversal               | 1.76 ms                                                         | 1.39 ms: 1.27x faster                                               |
| deepcopy_reduce            | 2.94 us                                                         | 2.63 us: 1.12x faster                                               |
| json_loads                 | 21.7 us                                                         | 19.8 us: 1.10x faster                                               |
| json_dumps                 | 7.53 ms                                                         | 6.96 ms: 1.08x faster                                               |
| sqlglot_parse              | 1.02 ms                                                         | 953 us: 1.07x faster                                                |
| tornado_http               | 105 ms                                                          | 98.2 ms: 1.07x faster                                               |
| json                       | 4.40 ms                                                         | 4.14 ms: 1.06x faster                                               |
| pprint_safe_repr           | 658 ms                                                          | 621 ms: 1.06x faster                                                |
| deepcopy                   | 311 us                                                          | 295 us: 1.05x faster                                                |
| sqlglot_normalize          | 223 ms                                                          | 212 ms: 1.05x faster                                                |
| chameleon                  | 6.24 ms                                                         | 5.96 ms: 1.05x faster                                               |
| comprehensions             | 13.1 us                                                         | 12.6 us: 1.05x faster                                               |
| sqlglot_transpile          | 1.26 ms                                                         | 1.21 ms: 1.05x faster                                               |
| sympy_expand               | 377 ms                                                          | 362 ms: 1.04x faster                                                |
| sympy_sum                  | 108 ms                                                          | 104 ms: 1.04x faster                                                |
| 2to3                       | 255 ms                                                          | 246 ms: 1.04x faster                                                |
| pickle_pure_python         | 239 us                                                          | 231 us: 1.04x faster                                                |
| unpickle_pure_python       | 162 us                                                          | 156 us: 1.04x faster                                                |
| pprint_pformat             | 1.32 sec                                                        | 1.28 sec: 1.04x faster                                              |
| sympy_str                  | 214 ms                                                          | 207 ms: 1.03x faster                                                |
| telco                      | 6.27 ms                                                         | 6.08 ms: 1.03x faster                                               |
| html5lib                   | 47.1 ms                                                         | 45.7 ms: 1.03x faster                                               |
| go                         | 111 ms                                                          | 108 ms: 1.03x faster                                                |
| django_template            | 32.0 ms                                                         | 31.2 ms: 1.03x faster                                               |
| crypto_pyaes               | 56.6 ms                                                         | 55.4 ms: 1.02x faster                                               |
| sqlglot_optimize           | 42.4 ms                                                         | 41.5 ms: 1.02x faster                                               |
| sympy_integrate            | 15.2 ms                                                         | 14.9 ms: 1.02x faster                                               |
| pidigits                   | 204 ms                                                          | 200 ms: 1.02x faster                                                |
| docutils                   | 1.80 sec                                                        | 1.78 sec: 1.01x faster                                              |
| python_startup_no_site     | 20.2 ms                                                         | 20.0 ms: 1.01x faster                                               |
| pycparser                  | 869 ms                                                          | 862 ms: 1.01x faster                                                |
| mdp                        | 1.70 sec                                                        | 1.70 sec: 1.00x slower                                              |
| pathlib                    | 89.1 ms                                                         | 89.7 ms: 1.01x slower                                               |
| richards                   | 33.4 ms                                                         | 33.7 ms: 1.01x slower                                               |
| xml_etree_generate         | 61.9 ms                                                         | 62.8 ms: 1.01x slower                                               |
| deepcopy_memo              | 26.2 us                                                         | 26.6 us: 1.02x slower                                               |
| richards_super             | 37.0 ms                                                         | 38.0 ms: 1.03x slower                                               |
| xml_etree_process          | 44.6 ms                                                         | 45.8 ms: 1.03x slower                                               |
| meteor_contest             | 78.1 ms                                                         | 80.4 ms: 1.03x slower                                               |
| logging_format             | 8.59 us                                                         | 8.90 us: 1.04x slower                                               |
| async_tree_none            | 245 ms                                                          | 254 ms: 1.04x slower                                                |
| coroutines                 | 16.1 ms                                                         | 16.7 ms: 1.04x slower                                               |
| scimark_monte_carlo        | 48.7 ms                                                         | 50.6 ms: 1.04x slower                                               |
| tomli_loads                | 1.74 sec                                                        | 1.81 sec: 1.04x slower                                              |
| async_generators           | 267 ms                                                          | 278 ms: 1.04x slower                                                |
| thrift                     | 10.3 ms                                                         | 10.7 ms: 1.04x slower                                               |
| pyflate                    | 322 ms                                                          | 335 ms: 1.04x slower                                                |
| async_tree_cpu_io_mixed    | 490 ms                                                          | 511 ms: 1.04x slower                                                |
| regex_compile              | 101 ms                                                          | 106 ms: 1.05x slower                                                |
| fannkuch                   | 288 ms                                                          | 302 ms: 1.05x slower                                                |
| chaos                      | 49.4 ms                                                         | 51.8 ms: 1.05x slower                                               |
| regex_v8                   | 15.5 ms                                                         | 16.2 ms: 1.05x slower                                               |
| async_tree_memoization     | 302 ms                                                          | 317 ms: 1.05x slower                                                |
| xml_etree_parse            | 102 ms                                                          | 108 ms: 1.05x slower                                                |
| regex_effbot               | 1.82 ms                                                         | 1.92 ms: 1.06x slower                                               |
| logging_simple             | 7.89 us                                                         | 8.35 us: 1.06x slower                                               |
| float                      | 56.4 ms                                                         | 59.8 ms: 1.06x slower                                               |
| scimark_sparse_mat_mult    | 2.88 ms                                                         | 3.07 ms: 1.06x slower                                               |
| nqueens                    | 75.1 ms                                                         | 80.1 ms: 1.07x slower                                               |
| spectral_norm              | 70.0 ms                                                         | 75.0 ms: 1.07x slower                                               |
| regex_dna                  | 112 ms                                                          | 120 ms: 1.07x slower                                                |
| async_tree_cpu_io_mixed_tg | 469 ms                                                          | 506 ms: 1.08x slower                                                |
| scimark_fft                | 204 ms                                                          | 220 ms: 1.08x slower                                                |
| hexiom                     | 4.60 ms                                                         | 4.97 ms: 1.08x slower                                               |
| deltablue                  | 2.35 ms                                                         | 2.55 ms: 1.09x slower                                               |
| async_tree_memoization_tg  | 287 ms                                                          | 312 ms: 1.09x slower                                                |
| nbody                      | 81.4 ms                                                         | 88.9 ms: 1.09x slower                                               |
| raytrace                   | 203 ms                                                          | 223 ms: 1.10x slower                                                |
| mako                       | 7.02 ms                                                         | 7.72 ms: 1.10x slower                                               |
| logging_silent             | 62.4 ns                                                         | 70.3 ns: 1.13x slower                                               |
| xml_etree_iterparse        | 61.3 ms                                                         | 69.5 ms: 1.13x slower                                               |
| scimark_lu                 | 60.7 ms                                                         | 69.0 ms: 1.14x slower                                               |
| scimark_sor                | 85.8 ms                                                         | 97.7 ms: 1.14x slower                                               |
| async_tree_none_tg         | 216 ms                                                          | 248 ms: 1.15x slower                                                |
| async_tree_io              | 530 ms                                                          | 623 ms: 1.17x slower                                                |
| async_tree_io_tg           | 499 ms                                                          | 619 ms: 1.24x slower                                                |
| generators                 | 21.5 ms                                                         | 27.0 ms: 1.25x slower                                               |
| coverage                   | 326 ms                                                          | 512 ms: 1.57x slower                                                |
| Geometric mean             | (ref)                                                           | 1.01x slower                                                        |

Benchmark hidden because not significant (4): genshi_xml, genshi_text, bench_thread_pool, pylint
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: asyncio_websockets, bpe_tokeniser, connected_components, dulwich_log, gevent_hub, k_core, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20231122-3.13.0a2-9c4347e/bm-20231122-pythonperf1_win32-x86-python-v3.13.0a2-3.13.0a2-9c4347e.json: asyncio_tcp, asyncio_tcp_ssl, flaskblogging, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.011x slower
# HPT report

- Reliability score: 99.42% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown