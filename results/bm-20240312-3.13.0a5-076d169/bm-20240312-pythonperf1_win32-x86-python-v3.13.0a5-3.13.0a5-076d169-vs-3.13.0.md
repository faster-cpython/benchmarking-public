# Results vs. 3.13.0

- fork: python
- ref: v3.13.0a5
- machine: windows-x86
- commit hash: 076d169
- commit date: 2024-03-12
- overall geometric mean: 1.078x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240312-pythonperf1_win32-x86-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 255 ms                                                          | 237 ms: 1.08x faster                                                |
| chameleon      | 6.24 ms                                                         | 5.53 ms: 1.13x faster                                               |
| docutils       | 1.80 sec                                                        | 1.70 sec: 1.06x faster                                              |
| html5lib       | 47.1 ms                                                         | 42.0 ms: 1.12x faster                                               |
| tornado_http   | 105 ms                                                          | 93.5 ms: 1.12x faster                                               |
| Geometric mean | (ref)                                                           | 1.10x faster                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240312-pythonperf1_win32-x86-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| coroutines                 | 16.1 ms                                                         | 14.1 ms: 1.14x faster                                               |
| async_generators           | 267 ms                                                          | 261 ms: 1.02x faster                                                |
| async_tree_none            | 245 ms                                                          | 241 ms: 1.02x faster                                                |
| async_tree_cpu_io_mixed    | 490 ms                                                          | 484 ms: 1.01x faster                                                |
| async_tree_memoization_tg  | 287 ms                                                          | 291 ms: 1.01x slower                                                |
| async_tree_cpu_io_mixed_tg | 469 ms                                                          | 477 ms: 1.02x slower                                                |
| async_tree_none_tg         | 216 ms                                                          | 233 ms: 1.08x slower                                                |
| async_tree_io              | 530 ms                                                          | 591 ms: 1.12x slower                                                |
| async_tree_io_tg           | 499 ms                                                          | 574 ms: 1.15x slower                                                |
| Geometric mean             | (ref)                                                           | 1.02x slower                                                        |

Benchmark hidden because not significant (1): async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240312-pythonperf1_win32-x86-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| nbody          | 81.4 ms                                                         | 74.7 ms: 1.09x faster                                               |
| float          | 56.4 ms                                                         | 53.8 ms: 1.05x faster                                               |
| pidigits       | 204 ms                                                          | 196 ms: 1.04x faster                                                |
| Geometric mean | (ref)                                                           | 1.06x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240312-pythonperf1_win32-x86-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 101 ms                                                          | 94.7 ms: 1.07x faster                                               |
| regex_v8       | 15.5 ms                                                         | 15.9 ms: 1.03x slower                                               |
| regex_effbot   | 1.82 ms                                                         | 1.90 ms: 1.04x slower                                               |
| regex_dna      | 112 ms                                                          | 119 ms: 1.06x slower                                                |
| Geometric mean | (ref)                                                           | 1.02x slower                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240312-pythonperf1_win32-x86-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| unpickle_pure_python | 162 us                                                          | 139 us: 1.17x faster                                                |
| pickle_pure_python   | 239 us                                                          | 206 us: 1.16x faster                                                |
| json_dumps           | 7.53 ms                                                         | 6.67 ms: 1.13x faster                                               |
| tomli_loads          | 1.74 sec                                                        | 1.58 sec: 1.10x faster                                              |
| xml_etree_process    | 44.6 ms                                                         | 40.5 ms: 1.10x faster                                               |
| json_loads           | 21.7 us                                                         | 20.1 us: 1.08x faster                                               |
| xml_etree_generate   | 61.9 ms                                                         | 57.9 ms: 1.07x faster                                               |
| xml_etree_parse      | 102 ms                                                          | 107 ms: 1.05x slower                                                |
| xml_etree_iterparse  | 61.3 ms                                                         | 65.4 ms: 1.07x slower                                               |
| Geometric mean       | (ref)                                                           | 1.07x faster                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240312-pythonperf1_win32-x86-python-v3.13.0a5-3.13.0a5-076d169 |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 28.3 ms                                                         | 22.8 ms: 1.24x faster                                               |
| python_startup_no_site | 20.2 ms                                                         | 20.6 ms: 1.02x slower                                               |
| Geometric mean         | (ref)                                                           | 1.10x faster                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240312-pythonperf1_win32-x86-python-v3.13.0a5-3.13.0a5-076d169 |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| genshi_xml      | 49.0 ms                                                         | 41.0 ms: 1.19x faster                                               |
| genshi_text     | 21.7 ms                                                         | 18.3 ms: 1.19x faster                                               |
| django_template | 32.0 ms                                                         | 28.6 ms: 1.12x faster                                               |
| mako            | 7.02 ms                                                         | 6.75 ms: 1.04x faster                                               |
| Geometric mean  | (ref)                                                           | 1.13x faster                                                        |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240312-pythonperf1_win32-x86-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| create_gc_cycles           | 1.08 ms                                                         | 657 us: 1.65x faster                                                |
| typing_runtime_protocols   | 141 us                                                          | 90.2 us: 1.56x faster                                               |
| deepcopy_reduce            | 2.94 us                                                         | 2.32 us: 1.27x faster                                               |
| bench_mp_pool              | 93.6 ms                                                         | 74.1 ms: 1.26x faster                                               |
| gc_traversal               | 1.76 ms                                                         | 1.40 ms: 1.26x faster                                               |
| python_startup             | 28.3 ms                                                         | 22.8 ms: 1.24x faster                                               |
| genshi_xml                 | 49.0 ms                                                         | 41.0 ms: 1.19x faster                                               |
| comprehensions             | 13.1 us                                                         | 11.0 us: 1.19x faster                                               |
| sqlglot_parse              | 1.02 ms                                                         | 856 us: 1.19x faster                                                |
| deepcopy                   | 311 us                                                          | 261 us: 1.19x faster                                                |
| genshi_text                | 21.7 ms                                                         | 18.3 ms: 1.19x faster                                               |
| richards                   | 33.4 ms                                                         | 28.2 ms: 1.18x faster                                               |
| go                         | 111 ms                                                          | 94.3 ms: 1.17x faster                                               |
| deepcopy_memo              | 26.2 us                                                         | 22.4 us: 1.17x faster                                               |
| richards_super             | 37.0 ms                                                         | 31.8 ms: 1.17x faster                                               |
| unpickle_pure_python       | 162 us                                                          | 139 us: 1.17x faster                                                |
| pprint_safe_repr           | 658 ms                                                          | 565 ms: 1.16x faster                                                |
| sqlglot_transpile          | 1.26 ms                                                         | 1.08 ms: 1.16x faster                                               |
| pickle_pure_python         | 239 us                                                          | 206 us: 1.16x faster                                                |
| sqlglot_normalize          | 223 ms                                                          | 193 ms: 1.15x faster                                                |
| coroutines                 | 16.1 ms                                                         | 14.1 ms: 1.14x faster                                               |
| pprint_pformat             | 1.32 sec                                                        | 1.16 sec: 1.14x faster                                              |
| json_dumps                 | 7.53 ms                                                         | 6.67 ms: 1.13x faster                                               |
| sqlglot_optimize           | 42.4 ms                                                         | 37.6 ms: 1.13x faster                                               |
| chameleon                  | 6.24 ms                                                         | 5.53 ms: 1.13x faster                                               |
| html5lib                   | 47.1 ms                                                         | 42.0 ms: 1.12x faster                                               |
| django_template            | 32.0 ms                                                         | 28.6 ms: 1.12x faster                                               |
| pycparser                  | 869 ms                                                          | 777 ms: 1.12x faster                                                |
| tornado_http               | 105 ms                                                          | 93.5 ms: 1.12x faster                                               |
| nqueens                    | 75.1 ms                                                         | 67.6 ms: 1.11x faster                                               |
| sympy_expand               | 377 ms                                                          | 341 ms: 1.11x faster                                                |
| hexiom                     | 4.60 ms                                                         | 4.16 ms: 1.11x faster                                               |
| tomli_loads                | 1.74 sec                                                        | 1.58 sec: 1.10x faster                                              |
| deltablue                  | 2.35 ms                                                         | 2.13 ms: 1.10x faster                                               |
| xml_etree_process          | 44.6 ms                                                         | 40.5 ms: 1.10x faster                                               |
| sympy_str                  | 214 ms                                                          | 195 ms: 1.10x faster                                                |
| sympy_sum                  | 108 ms                                                          | 98.5 ms: 1.10x faster                                               |
| scimark_monte_carlo        | 48.7 ms                                                         | 44.5 ms: 1.09x faster                                               |
| nbody                      | 81.4 ms                                                         | 74.7 ms: 1.09x faster                                               |
| logging_silent             | 62.4 ns                                                         | 57.3 ns: 1.09x faster                                               |
| sympy_integrate            | 15.2 ms                                                         | 14.1 ms: 1.08x faster                                               |
| crypto_pyaes               | 56.6 ms                                                         | 52.3 ms: 1.08x faster                                               |
| scimark_sor                | 85.8 ms                                                         | 79.3 ms: 1.08x faster                                               |
| mdp                        | 1.70 sec                                                        | 1.58 sec: 1.08x faster                                              |
| json_loads                 | 21.7 us                                                         | 20.1 us: 1.08x faster                                               |
| 2to3                       | 255 ms                                                          | 237 ms: 1.08x faster                                                |
| fannkuch                   | 288 ms                                                          | 268 ms: 1.08x faster                                                |
| json                       | 4.40 ms                                                         | 4.10 ms: 1.07x faster                                               |
| xml_etree_generate         | 61.9 ms                                                         | 57.9 ms: 1.07x faster                                               |
| spectral_norm              | 70.0 ms                                                         | 65.6 ms: 1.07x faster                                               |
| regex_compile              | 101 ms                                                          | 94.7 ms: 1.07x faster                                               |
| docutils                   | 1.80 sec                                                        | 1.70 sec: 1.06x faster                                              |
| logging_format             | 8.59 us                                                         | 8.10 us: 1.06x faster                                               |
| raytrace                   | 203 ms                                                          | 192 ms: 1.06x faster                                                |
| bench_thread_pool          | 1.04 ms                                                         | 986 us: 1.06x faster                                                |
| float                      | 56.4 ms                                                         | 53.8 ms: 1.05x faster                                               |
| logging_simple             | 7.89 us                                                         | 7.53 us: 1.05x faster                                               |
| telco                      | 6.27 ms                                                         | 5.99 ms: 1.05x faster                                               |
| meteor_contest             | 78.1 ms                                                         | 74.9 ms: 1.04x faster                                               |
| pyflate                    | 322 ms                                                          | 309 ms: 1.04x faster                                                |
| chaos                      | 49.4 ms                                                         | 47.5 ms: 1.04x faster                                               |
| mako                       | 7.02 ms                                                         | 6.75 ms: 1.04x faster                                               |
| pidigits                   | 204 ms                                                          | 196 ms: 1.04x faster                                                |
| pylint                     | 225 ms                                                          | 217 ms: 1.03x faster                                                |
| scimark_lu                 | 60.7 ms                                                         | 58.7 ms: 1.03x faster                                               |
| async_generators           | 267 ms                                                          | 261 ms: 1.02x faster                                                |
| scimark_fft                | 204 ms                                                          | 201 ms: 1.02x faster                                                |
| thrift                     | 10.3 ms                                                         | 10.1 ms: 1.02x faster                                               |
| async_tree_none            | 245 ms                                                          | 241 ms: 1.02x faster                                                |
| async_tree_cpu_io_mixed    | 490 ms                                                          | 484 ms: 1.01x faster                                                |
| async_tree_memoization_tg  | 287 ms                                                          | 291 ms: 1.01x slower                                                |
| async_tree_cpu_io_mixed_tg | 469 ms                                                          | 477 ms: 1.02x slower                                                |
| generators                 | 21.5 ms                                                         | 21.9 ms: 1.02x slower                                               |
| python_startup_no_site     | 20.2 ms                                                         | 20.6 ms: 1.02x slower                                               |
| regex_v8                   | 15.5 ms                                                         | 15.9 ms: 1.03x slower                                               |
| regex_effbot               | 1.82 ms                                                         | 1.90 ms: 1.04x slower                                               |
| xml_etree_parse            | 102 ms                                                          | 107 ms: 1.05x slower                                                |
| regex_dna                  | 112 ms                                                          | 119 ms: 1.06x slower                                                |
| xml_etree_iterparse        | 61.3 ms                                                         | 65.4 ms: 1.07x slower                                               |
| async_tree_none_tg         | 216 ms                                                          | 233 ms: 1.08x slower                                                |
| async_tree_io              | 530 ms                                                          | 591 ms: 1.12x slower                                                |
| async_tree_io_tg           | 499 ms                                                          | 574 ms: 1.15x slower                                                |
| coverage                   | 326 ms                                                          | 497 ms: 1.52x slower                                                |
| Geometric mean             | (ref)                                                           | 1.08x faster                                                        |

Benchmark hidden because not significant (3): async_tree_memoization, pathlib, scimark_sparse_mat_mult
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: asyncio_websockets, bpe_tokeniser, connected_components, dulwich_log, gevent_hub, k_core, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20240312-3.13.0a5-076d169/bm-20240312-pythonperf1_win32-x86-python-v3.13.0a5-3.13.0a5-076d169.json: asyncio_tcp, asyncio_tcp_ssl, flaskblogging, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.078x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: unknown