# Results vs. 3.13.0

- fork: python
- ref: v3.13.0b2
- machine: windows-x86
- commit hash: 3a83b17
- commit date: 2024-06-05
- overall geometric mean: 1.060x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 255 ms                                                          | 233 ms: 1.09x faster                                                |
| chameleon      | 6.24 ms                                                         | 5.71 ms: 1.09x faster                                               |
| docutils       | 1.80 sec                                                        | 1.81 sec: 1.01x slower                                              |
| html5lib       | 47.1 ms                                                         | 45.4 ms: 1.04x faster                                               |
| tornado_http   | 105 ms                                                          | 94.3 ms: 1.11x faster                                               |
| Geometric mean | (ref)                                                           | 1.06x faster                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_memoization_tg  | 287 ms                                                          | 254 ms: 1.13x faster                                                |
| async_tree_memoization     | 302 ms                                                          | 275 ms: 1.10x faster                                                |
| async_tree_none            | 245 ms                                                          | 228 ms: 1.07x faster                                                |
| async_tree_none_tg         | 216 ms                                                          | 203 ms: 1.06x faster                                                |
| async_tree_cpu_io_mixed_tg | 469 ms                                                          | 447 ms: 1.05x faster                                                |
| coroutines                 | 16.1 ms                                                         | 15.5 ms: 1.04x faster                                               |
| async_tree_cpu_io_mixed    | 490 ms                                                          | 471 ms: 1.04x faster                                                |
| async_generators           | 267 ms                                                          | 266 ms: 1.00x faster                                                |
| async_tree_io_tg           | 499 ms                                                          | 529 ms: 1.06x slower                                                |
| Geometric mean             | (ref)                                                           | 1.04x faster                                                        |

Benchmark hidden because not significant (1): async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 56.4 ms                                                         | 52.4 ms: 1.08x faster                                               |
| nbody          | 81.4 ms                                                         | 76.9 ms: 1.06x faster                                               |
| pidigits       | 204 ms                                                          | 199 ms: 1.03x faster                                                |
| Geometric mean | (ref)                                                           | 1.05x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 101 ms                                                          | 99.9 ms: 1.01x faster                                               |
| regex_v8       | 15.5 ms                                                         | 15.7 ms: 1.02x slower                                               |
| regex_effbot   | 1.82 ms                                                         | 1.88 ms: 1.04x slower                                               |
| regex_dna      | 112 ms                                                          | 118 ms: 1.05x slower                                                |
| Geometric mean | (ref)                                                           | 1.02x slower                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| pickle_pure_python   | 239 us                                                          | 213 us: 1.12x faster                                                |
| json_dumps           | 7.53 ms                                                         | 6.84 ms: 1.10x faster                                               |
| unpickle_pure_python | 162 us                                                          | 147 us: 1.10x faster                                                |
| xml_etree_process    | 44.6 ms                                                         | 42.1 ms: 1.06x faster                                               |
| tomli_loads          | 1.74 sec                                                        | 1.65 sec: 1.06x faster                                              |
| json_loads           | 21.7 us                                                         | 20.5 us: 1.06x faster                                               |
| xml_etree_generate   | 61.9 ms                                                         | 59.6 ms: 1.04x faster                                               |
| xml_etree_parse      | 102 ms                                                          | 104 ms: 1.02x slower                                                |
| xml_etree_iterparse  | 61.3 ms                                                         | 64.2 ms: 1.05x slower                                               |
| Geometric mean       | (ref)                                                           | 1.05x faster                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 28.3 ms                                                         | 22.2 ms: 1.27x faster                                               |
| python_startup_no_site | 20.2 ms                                                         | 18.2 ms: 1.11x faster                                               |
| Geometric mean         | (ref)                                                           | 1.19x faster                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| genshi_xml      | 49.0 ms                                                         | 44.3 ms: 1.11x faster                                               |
| genshi_text     | 21.7 ms                                                         | 20.1 ms: 1.08x faster                                               |
| django_template | 32.0 ms                                                         | 30.1 ms: 1.07x faster                                               |
| mako            | 7.02 ms                                                         | 6.94 ms: 1.01x faster                                               |
| Geometric mean  | (ref)                                                           | 1.07x faster                                                        |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| create_gc_cycles           | 1.08 ms                                                         | 756 us: 1.43x faster                                                |
| bench_mp_pool              | 93.6 ms                                                         | 69.4 ms: 1.35x faster                                               |
| python_startup             | 28.3 ms                                                         | 22.2 ms: 1.27x faster                                               |
| gc_traversal               | 1.76 ms                                                         | 1.43 ms: 1.23x faster                                               |
| deepcopy_reduce            | 2.94 us                                                         | 2.59 us: 1.14x faster                                               |
| async_tree_memoization_tg  | 287 ms                                                          | 254 ms: 1.13x faster                                                |
| pickle_pure_python         | 239 us                                                          | 213 us: 1.12x faster                                                |
| pycparser                  | 869 ms                                                          | 777 ms: 1.12x faster                                                |
| deepcopy_memo              | 26.2 us                                                         | 23.5 us: 1.12x faster                                               |
| deepcopy                   | 311 us                                                          | 280 us: 1.11x faster                                                |
| comprehensions             | 13.1 us                                                         | 11.9 us: 1.11x faster                                               |
| tornado_http               | 105 ms                                                          | 94.3 ms: 1.11x faster                                               |
| genshi_xml                 | 49.0 ms                                                         | 44.3 ms: 1.11x faster                                               |
| python_startup_no_site     | 20.2 ms                                                         | 18.2 ms: 1.11x faster                                               |
| json_dumps                 | 7.53 ms                                                         | 6.84 ms: 1.10x faster                                               |
| go                         | 111 ms                                                          | 101 ms: 1.10x faster                                                |
| unpickle_pure_python       | 162 us                                                          | 147 us: 1.10x faster                                                |
| async_tree_memoization     | 302 ms                                                          | 275 ms: 1.10x faster                                                |
| 2to3                       | 255 ms                                                          | 233 ms: 1.09x faster                                                |
| nqueens                    | 75.1 ms                                                         | 68.7 ms: 1.09x faster                                               |
| chameleon                  | 6.24 ms                                                         | 5.71 ms: 1.09x faster                                               |
| hexiom                     | 4.60 ms                                                         | 4.23 ms: 1.09x faster                                               |
| pprint_safe_repr           | 658 ms                                                          | 607 ms: 1.08x faster                                                |
| sqlglot_normalize          | 223 ms                                                          | 206 ms: 1.08x faster                                                |
| genshi_text                | 21.7 ms                                                         | 20.1 ms: 1.08x faster                                               |
| logging_silent             | 62.4 ns                                                         | 57.9 ns: 1.08x faster                                               |
| scimark_monte_carlo        | 48.7 ms                                                         | 45.2 ms: 1.08x faster                                               |
| float                      | 56.4 ms                                                         | 52.4 ms: 1.08x faster                                               |
| raytrace                   | 203 ms                                                          | 189 ms: 1.07x faster                                                |
| async_tree_none            | 245 ms                                                          | 228 ms: 1.07x faster                                                |
| json                       | 4.40 ms                                                         | 4.10 ms: 1.07x faster                                               |
| richards                   | 33.4 ms                                                         | 31.2 ms: 1.07x faster                                               |
| sqlglot_optimize           | 42.4 ms                                                         | 39.7 ms: 1.07x faster                                               |
| fannkuch                   | 288 ms                                                          | 270 ms: 1.07x faster                                                |
| django_template            | 32.0 ms                                                         | 30.1 ms: 1.07x faster                                               |
| pprint_pformat             | 1.32 sec                                                        | 1.24 sec: 1.07x faster                                              |
| async_tree_none_tg         | 216 ms                                                          | 203 ms: 1.06x faster                                                |
| pathlib                    | 89.1 ms                                                         | 83.9 ms: 1.06x faster                                               |
| coverage                   | 326 ms                                                          | 307 ms: 1.06x faster                                                |
| xml_etree_process          | 44.6 ms                                                         | 42.1 ms: 1.06x faster                                               |
| sqlglot_transpile          | 1.26 ms                                                         | 1.19 ms: 1.06x faster                                               |
| scimark_sor                | 85.8 ms                                                         | 81.0 ms: 1.06x faster                                               |
| mdp                        | 1.70 sec                                                        | 1.60 sec: 1.06x faster                                              |
| nbody                      | 81.4 ms                                                         | 76.9 ms: 1.06x faster                                               |
| sqlglot_parse              | 1.02 ms                                                         | 964 us: 1.06x faster                                                |
| logging_simple             | 7.89 us                                                         | 7.47 us: 1.06x faster                                               |
| bench_thread_pool          | 1.04 ms                                                         | 985 us: 1.06x faster                                                |
| tomli_loads                | 1.74 sec                                                        | 1.65 sec: 1.06x faster                                              |
| logging_format             | 8.59 us                                                         | 8.13 us: 1.06x faster                                               |
| json_loads                 | 21.7 us                                                         | 20.5 us: 1.06x faster                                               |
| meteor_contest             | 78.1 ms                                                         | 74.1 ms: 1.05x faster                                               |
| thrift                     | 10.3 ms                                                         | 9.73 ms: 1.05x faster                                               |
| deltablue                  | 2.35 ms                                                         | 2.23 ms: 1.05x faster                                               |
| async_tree_cpu_io_mixed_tg | 469 ms                                                          | 447 ms: 1.05x faster                                                |
| pyflate                    | 322 ms                                                          | 308 ms: 1.04x faster                                                |
| richards_super             | 37.0 ms                                                         | 35.5 ms: 1.04x faster                                               |
| coroutines                 | 16.1 ms                                                         | 15.5 ms: 1.04x faster                                               |
| telco                      | 6.27 ms                                                         | 6.03 ms: 1.04x faster                                               |
| sympy_integrate            | 15.2 ms                                                         | 14.6 ms: 1.04x faster                                               |
| async_tree_cpu_io_mixed    | 490 ms                                                          | 471 ms: 1.04x faster                                                |
| typing_runtime_protocols   | 141 us                                                          | 136 us: 1.04x faster                                                |
| xml_etree_generate         | 61.9 ms                                                         | 59.6 ms: 1.04x faster                                               |
| html5lib                   | 47.1 ms                                                         | 45.4 ms: 1.04x faster                                               |
| pylint                     | 225 ms                                                          | 217 ms: 1.03x faster                                                |
| spectral_norm              | 70.0 ms                                                         | 68.0 ms: 1.03x faster                                               |
| scimark_fft                | 204 ms                                                          | 198 ms: 1.03x faster                                                |
| chaos                      | 49.4 ms                                                         | 48.0 ms: 1.03x faster                                               |
| sympy_sum                  | 108 ms                                                          | 105 ms: 1.03x faster                                                |
| pidigits                   | 204 ms                                                          | 199 ms: 1.03x faster                                                |
| scimark_lu                 | 60.7 ms                                                         | 59.4 ms: 1.02x faster                                               |
| generators                 | 21.5 ms                                                         | 21.2 ms: 1.02x faster                                               |
| sympy_str                  | 214 ms                                                          | 211 ms: 1.01x faster                                                |
| crypto_pyaes               | 56.6 ms                                                         | 55.8 ms: 1.01x faster                                               |
| regex_compile              | 101 ms                                                          | 99.9 ms: 1.01x faster                                               |
| mako                       | 7.02 ms                                                         | 6.94 ms: 1.01x faster                                               |
| sympy_expand               | 377 ms                                                          | 375 ms: 1.01x faster                                                |
| async_generators           | 267 ms                                                          | 266 ms: 1.00x faster                                                |
| docutils                   | 1.80 sec                                                        | 1.81 sec: 1.01x slower                                              |
| regex_v8                   | 15.5 ms                                                         | 15.7 ms: 1.02x slower                                               |
| xml_etree_parse            | 102 ms                                                          | 104 ms: 1.02x slower                                                |
| regex_effbot               | 1.82 ms                                                         | 1.88 ms: 1.04x slower                                               |
| xml_etree_iterparse        | 61.3 ms                                                         | 64.2 ms: 1.05x slower                                               |
| regex_dna                  | 112 ms                                                          | 118 ms: 1.05x slower                                                |
| async_tree_io_tg           | 499 ms                                                          | 529 ms: 1.06x slower                                                |
| Geometric mean             | (ref)                                                           | 1.06x faster                                                        |

Benchmark hidden because not significant (2): scimark_sparse_mat_mult, async_tree_io
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: asyncio_websockets, bpe_tokeniser, connected_components, dulwich_log, gevent_hub, k_core, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17.json: asyncio_tcp, asyncio_tcp_ssl, flaskblogging, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.060x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: unknown