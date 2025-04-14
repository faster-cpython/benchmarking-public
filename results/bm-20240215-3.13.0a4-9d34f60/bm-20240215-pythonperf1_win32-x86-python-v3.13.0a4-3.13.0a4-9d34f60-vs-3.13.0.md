# Results vs. 3.13.0

- fork: python
- ref: v3.13.0a4
- machine: windows-x86
- commit hash: 9d34f60
- commit date: 2024-02-15
- overall geometric mean: 1.074x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240215-pythonperf1_win32-x86-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 255 ms                                                          | 230 ms: 1.11x faster                                                |
| chameleon      | 6.24 ms                                                         | 5.61 ms: 1.11x faster                                               |
| docutils       | 1.80 sec                                                        | 1.71 sec: 1.05x faster                                              |
| html5lib       | 47.1 ms                                                         | 43.9 ms: 1.07x faster                                               |
| tornado_http   | 105 ms                                                          | 93.5 ms: 1.12x faster                                               |
| Geometric mean | (ref)                                                           | 1.09x faster                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240215-pythonperf1_win32-x86-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| coroutines                 | 16.1 ms                                                         | 14.1 ms: 1.14x faster                                               |
| async_tree_none            | 245 ms                                                          | 239 ms: 1.03x faster                                                |
| async_generators           | 267 ms                                                          | 262 ms: 1.02x faster                                                |
| async_tree_memoization_tg  | 287 ms                                                          | 284 ms: 1.01x faster                                                |
| async_tree_cpu_io_mixed    | 490 ms                                                          | 496 ms: 1.01x slower                                                |
| async_tree_cpu_io_mixed_tg | 469 ms                                                          | 489 ms: 1.04x slower                                                |
| async_tree_none_tg         | 216 ms                                                          | 225 ms: 1.04x slower                                                |
| async_tree_io              | 530 ms                                                          | 584 ms: 1.10x slower                                                |
| async_tree_io_tg           | 499 ms                                                          | 570 ms: 1.14x slower                                                |
| Geometric mean             | (ref)                                                           | 1.01x slower                                                        |

Benchmark hidden because not significant (1): async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240215-pythonperf1_win32-x86-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 56.4 ms                                                         | 52.8 ms: 1.07x faster                                               |
| nbody          | 81.4 ms                                                         | 76.8 ms: 1.06x faster                                               |
| pidigits       | 204 ms                                                          | 197 ms: 1.04x faster                                                |
| Geometric mean | (ref)                                                           | 1.05x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240215-pythonperf1_win32-x86-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 101 ms                                                          | 93.4 ms: 1.08x faster                                               |
| regex_dna      | 112 ms                                                          | 116 ms: 1.03x slower                                                |
| regex_v8       | 15.5 ms                                                         | 16.0 ms: 1.04x slower                                               |
| regex_effbot   | 1.82 ms                                                         | 1.89 ms: 1.04x slower                                               |
| Geometric mean | (ref)                                                           | 1.01x slower                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240215-pythonperf1_win32-x86-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| unpickle_pure_python | 162 us                                                          | 140 us: 1.15x faster                                                |
| pickle_pure_python   | 239 us                                                          | 210 us: 1.14x faster                                                |
| json_dumps           | 7.53 ms                                                         | 6.71 ms: 1.12x faster                                               |
| xml_etree_process    | 44.6 ms                                                         | 41.2 ms: 1.08x faster                                               |
| tomli_loads          | 1.74 sec                                                        | 1.62 sec: 1.08x faster                                              |
| json_loads           | 21.7 us                                                         | 20.2 us: 1.07x faster                                               |
| xml_etree_generate   | 61.9 ms                                                         | 60.0 ms: 1.03x faster                                               |
| xml_etree_parse      | 102 ms                                                          | 110 ms: 1.07x slower                                                |
| xml_etree_iterparse  | 61.3 ms                                                         | 66.2 ms: 1.08x slower                                               |
| Geometric mean       | (ref)                                                           | 1.06x faster                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240215-pythonperf1_win32-x86-python-v3.13.0a4-3.13.0a4-9d34f60 |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 28.3 ms                                                         | 22.0 ms: 1.29x faster                                               |
| python_startup_no_site | 20.2 ms                                                         | 19.7 ms: 1.02x faster                                               |
| Geometric mean         | (ref)                                                           | 1.15x faster                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240215-pythonperf1_win32-x86-python-v3.13.0a4-3.13.0a4-9d34f60 |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| genshi_xml      | 49.0 ms                                                         | 41.8 ms: 1.17x faster                                               |
| genshi_text     | 21.7 ms                                                         | 18.9 ms: 1.15x faster                                               |
| django_template | 32.0 ms                                                         | 30.4 ms: 1.06x faster                                               |
| mako            | 7.02 ms                                                         | 6.76 ms: 1.04x faster                                               |
| Geometric mean  | (ref)                                                           | 1.10x faster                                                        |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240215-pythonperf1_win32-x86-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| create_gc_cycles           | 1.08 ms                                                         | 662 us: 1.63x faster                                                |
| typing_runtime_protocols   | 141 us                                                          | 87.8 us: 1.60x faster                                               |
| bench_mp_pool              | 93.6 ms                                                         | 70.4 ms: 1.33x faster                                               |
| python_startup             | 28.3 ms                                                         | 22.0 ms: 1.29x faster                                               |
| gc_traversal               | 1.76 ms                                                         | 1.39 ms: 1.27x faster                                               |
| deepcopy_reduce            | 2.94 us                                                         | 2.32 us: 1.27x faster                                               |
| deepcopy_memo              | 26.2 us                                                         | 22.0 us: 1.19x faster                                               |
| deepcopy                   | 311 us                                                          | 261 us: 1.19x faster                                                |
| richards                   | 33.4 ms                                                         | 28.4 ms: 1.18x faster                                               |
| sqlglot_parse              | 1.02 ms                                                         | 868 us: 1.18x faster                                                |
| genshi_xml                 | 49.0 ms                                                         | 41.8 ms: 1.17x faster                                               |
| go                         | 111 ms                                                          | 95.1 ms: 1.16x faster                                               |
| pprint_safe_repr           | 658 ms                                                          | 568 ms: 1.16x faster                                                |
| unpickle_pure_python       | 162 us                                                          | 140 us: 1.15x faster                                                |
| genshi_text                | 21.7 ms                                                         | 18.9 ms: 1.15x faster                                               |
| comprehensions             | 13.1 us                                                         | 11.5 us: 1.15x faster                                               |
| sqlglot_transpile          | 1.26 ms                                                         | 1.10 ms: 1.14x faster                                               |
| coroutines                 | 16.1 ms                                                         | 14.1 ms: 1.14x faster                                               |
| pickle_pure_python         | 239 us                                                          | 210 us: 1.14x faster                                                |
| pprint_pformat             | 1.32 sec                                                        | 1.16 sec: 1.13x faster                                              |
| nqueens                    | 75.1 ms                                                         | 66.9 ms: 1.12x faster                                               |
| json_dumps                 | 7.53 ms                                                         | 6.71 ms: 1.12x faster                                               |
| tornado_http               | 105 ms                                                          | 93.5 ms: 1.12x faster                                               |
| chameleon                  | 6.24 ms                                                         | 5.61 ms: 1.11x faster                                               |
| 2to3                       | 255 ms                                                          | 230 ms: 1.11x faster                                                |
| sqlglot_normalize          | 223 ms                                                          | 201 ms: 1.11x faster                                                |
| pycparser                  | 869 ms                                                          | 784 ms: 1.11x faster                                                |
| sympy_expand               | 377 ms                                                          | 341 ms: 1.11x faster                                                |
| sympy_str                  | 214 ms                                                          | 194 ms: 1.10x faster                                                |
| richards_super             | 37.0 ms                                                         | 33.7 ms: 1.10x faster                                               |
| sqlglot_optimize           | 42.4 ms                                                         | 38.6 ms: 1.10x faster                                               |
| logging_silent             | 62.4 ns                                                         | 56.9 ns: 1.10x faster                                               |
| hexiom                     | 4.60 ms                                                         | 4.20 ms: 1.09x faster                                               |
| telco                      | 6.27 ms                                                         | 5.76 ms: 1.09x faster                                               |
| sympy_sum                  | 108 ms                                                          | 99.4 ms: 1.09x faster                                               |
| scimark_monte_carlo        | 48.7 ms                                                         | 44.9 ms: 1.09x faster                                               |
| sympy_integrate            | 15.2 ms                                                         | 14.0 ms: 1.08x faster                                               |
| deltablue                  | 2.35 ms                                                         | 2.17 ms: 1.08x faster                                               |
| xml_etree_process          | 44.6 ms                                                         | 41.2 ms: 1.08x faster                                               |
| regex_compile              | 101 ms                                                          | 93.4 ms: 1.08x faster                                               |
| mdp                        | 1.70 sec                                                        | 1.57 sec: 1.08x faster                                              |
| tomli_loads                | 1.74 sec                                                        | 1.62 sec: 1.08x faster                                              |
| crypto_pyaes               | 56.6 ms                                                         | 52.6 ms: 1.08x faster                                               |
| html5lib                   | 47.1 ms                                                         | 43.9 ms: 1.07x faster                                               |
| json_loads                 | 21.7 us                                                         | 20.2 us: 1.07x faster                                               |
| spectral_norm              | 70.0 ms                                                         | 65.4 ms: 1.07x faster                                               |
| float                      | 56.4 ms                                                         | 52.8 ms: 1.07x faster                                               |
| chaos                      | 49.4 ms                                                         | 46.3 ms: 1.07x faster                                               |
| fannkuch                   | 288 ms                                                          | 271 ms: 1.06x faster                                                |
| raytrace                   | 203 ms                                                          | 191 ms: 1.06x faster                                                |
| scimark_sor                | 85.8 ms                                                         | 80.9 ms: 1.06x faster                                               |
| logging_format             | 8.59 us                                                         | 8.10 us: 1.06x faster                                               |
| nbody                      | 81.4 ms                                                         | 76.8 ms: 1.06x faster                                               |
| logging_simple             | 7.89 us                                                         | 7.46 us: 1.06x faster                                               |
| bench_thread_pool          | 1.04 ms                                                         | 984 us: 1.06x faster                                                |
| json                       | 4.40 ms                                                         | 4.16 ms: 1.06x faster                                               |
| django_template            | 32.0 ms                                                         | 30.4 ms: 1.06x faster                                               |
| docutils                   | 1.80 sec                                                        | 1.71 sec: 1.05x faster                                              |
| pyflate                    | 322 ms                                                          | 307 ms: 1.05x faster                                                |
| thrift                     | 10.3 ms                                                         | 9.86 ms: 1.04x faster                                               |
| mako                       | 7.02 ms                                                         | 6.76 ms: 1.04x faster                                               |
| pylint                     | 225 ms                                                          | 217 ms: 1.04x faster                                                |
| pidigits                   | 204 ms                                                          | 197 ms: 1.04x faster                                                |
| xml_etree_generate         | 61.9 ms                                                         | 60.0 ms: 1.03x faster                                               |
| scimark_lu                 | 60.7 ms                                                         | 59.0 ms: 1.03x faster                                               |
| scimark_fft                | 204 ms                                                          | 198 ms: 1.03x faster                                                |
| async_tree_none            | 245 ms                                                          | 239 ms: 1.03x faster                                                |
| python_startup_no_site     | 20.2 ms                                                         | 19.7 ms: 1.02x faster                                               |
| async_generators           | 267 ms                                                          | 262 ms: 1.02x faster                                                |
| async_tree_memoization_tg  | 287 ms                                                          | 284 ms: 1.01x faster                                                |
| meteor_contest             | 78.1 ms                                                         | 77.4 ms: 1.01x faster                                               |
| pathlib                    | 89.1 ms                                                         | 88.6 ms: 1.01x faster                                               |
| async_tree_cpu_io_mixed    | 490 ms                                                          | 496 ms: 1.01x slower                                                |
| regex_dna                  | 112 ms                                                          | 116 ms: 1.03x slower                                                |
| regex_v8                   | 15.5 ms                                                         | 16.0 ms: 1.04x slower                                               |
| regex_effbot               | 1.82 ms                                                         | 1.89 ms: 1.04x slower                                               |
| async_tree_cpu_io_mixed_tg | 469 ms                                                          | 489 ms: 1.04x slower                                                |
| async_tree_none_tg         | 216 ms                                                          | 225 ms: 1.04x slower                                                |
| generators                 | 21.5 ms                                                         | 22.7 ms: 1.06x slower                                               |
| xml_etree_parse            | 102 ms                                                          | 110 ms: 1.07x slower                                                |
| xml_etree_iterparse        | 61.3 ms                                                         | 66.2 ms: 1.08x slower                                               |
| async_tree_io              | 530 ms                                                          | 584 ms: 1.10x slower                                                |
| async_tree_io_tg           | 499 ms                                                          | 570 ms: 1.14x slower                                                |
| coverage                   | 326 ms                                                          | 460 ms: 1.41x slower                                                |
| Geometric mean             | (ref)                                                           | 1.08x faster                                                        |

Benchmark hidden because not significant (2): async_tree_memoization, scimark_sparse_mat_mult
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: asyncio_websockets, bpe_tokeniser, connected_components, dulwich_log, gevent_hub, k_core, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20240215-3.13.0a4-9d34f60/bm-20240215-pythonperf1_win32-x86-python-v3.13.0a4-3.13.0a4-9d34f60.json: asyncio_tcp, asyncio_tcp_ssl, flaskblogging, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.074x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: unknown