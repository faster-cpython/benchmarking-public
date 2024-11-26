# Results vs. 3.13.0

- fork: python
- ref: 401fff7423ca3c8bf1d0
- machine: windows-x86
- commit hash: 401fff7
- commit date: 2024-09-14
- overall geometric mean: 1.112x faster
- HPT reliability: 94.89%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240914-pythonperf1_win32-x86-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 255 ms                                                          | 257 ms: 1.01x slower                                                           |
| docutils       | 1.80 sec                                                        | 2.00 sec: 1.11x slower                                                         |
| tornado_http   | 105 ms                                                          | 99.7 ms: 1.05x faster                                                          |
| Geometric mean | (ref)                                                           | 1.02x slower                                                                   |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240914-pythonperf1_win32-x86-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 287 ms                                                          | 258 ms: 1.11x faster                                                           |
| async_tree_none            | 245 ms                                                          | 223 ms: 1.10x faster                                                           |
| async_tree_memoization     | 302 ms                                                          | 281 ms: 1.07x faster                                                           |
| async_tree_none_tg         | 216 ms                                                          | 204 ms: 1.06x faster                                                           |
| async_tree_cpu_io_mixed    | 490 ms                                                          | 485 ms: 1.01x faster                                                           |
| async_tree_cpu_io_mixed_tg | 469 ms                                                          | 476 ms: 1.01x slower                                                           |
| async_tree_io              | 530 ms                                                          | 547 ms: 1.03x slower                                                           |
| async_tree_io_tg           | 499 ms                                                          | 524 ms: 1.05x slower                                                           |
| coroutines                 | 16.1 ms                                                         | 18.5 ms: 1.14x slower                                                          |
| async_generators           | 267 ms                                                          | 320 ms: 1.20x slower                                                           |
| Geometric mean             | (ref)                                                           | 1.01x slower                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240914-pythonperf1_win32-x86-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| nbody          | 81.4 ms                                                         | 50.6 ms: 1.61x faster                                                          |
| float          | 56.4 ms                                                         | 43.8 ms: 1.29x faster                                                          |
| pidigits       | 204 ms                                                          | 195 ms: 1.04x faster                                                           |
| Geometric mean | (ref)                                                           | 1.29x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240914-pythonperf1_win32-x86-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_compile  | 101 ms                                                          | 103 ms: 1.02x slower                                                           |
| regex_v8       | 15.5 ms                                                         | 15.9 ms: 1.03x slower                                                          |
| regex_dna      | 112 ms                                                          | 116 ms: 1.04x slower                                                           |
| regex_effbot   | 1.82 ms                                                         | 1.95 ms: 1.07x slower                                                          |
| Geometric mean | (ref)                                                           | 1.04x slower                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240914-pythonperf1_win32-x86-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| xml_etree_generate   | 61.9 ms                                                         | 52.7 ms: 1.17x faster                                                          |
| tomli_loads          | 1.74 sec                                                        | 1.50 sec: 1.16x faster                                                         |
| xml_etree_process    | 44.6 ms                                                         | 39.5 ms: 1.13x faster                                                          |
| json_dumps           | 7.53 ms                                                         | 6.71 ms: 1.12x faster                                                          |
| json_loads           | 21.7 us                                                         | 20.6 us: 1.05x faster                                                          |
| xml_etree_iterparse  | 61.3 ms                                                         | 61.7 ms: 1.01x slower                                                          |
| unpickle_pure_python | 162 us                                                          | 164 us: 1.01x slower                                                           |
| xml_etree_parse      | 102 ms                                                          | 104 ms: 1.01x slower                                                           |
| pickle_pure_python   | 239 us                                                          | 247 us: 1.03x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.06x faster                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240914-pythonperf1_win32-x86-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 28.3 ms                                                         | 23.7 ms: 1.19x faster                                                          |
| python_startup_no_site | 20.2 ms                                                         | 19.5 ms: 1.03x faster                                                          |
| Geometric mean         | (ref)                                                           | 1.11x faster                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240914-pythonperf1_win32-x86-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 7.02 ms                                                         | 5.47 ms: 1.28x faster                                                          |
| django_template | 32.0 ms                                                         | 35.1 ms: 1.09x slower                                                          |
| genshi_xml      | 49.0 ms                                                         | 56.0 ms: 1.14x slower                                                          |
| genshi_text     | 21.7 ms                                                         | 25.8 ms: 1.19x slower                                                          |
| Geometric mean  | (ref)                                                           | 1.04x slower                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240914-pythonperf1_win32-x86-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| thrift                     | 10.3 ms                                                         | 768 us: 13.36x faster                                                          |
| coverage                   | 326 ms                                                          | 53.8 ms: 6.06x faster                                                          |
| sqlglot_normalize          | 223 ms                                                          | 100.0 ms: 2.23x faster                                                         |
| deepcopy_memo              | 26.2 us                                                         | 15.2 us: 1.72x faster                                                          |
| nbody                      | 81.4 ms                                                         | 50.6 ms: 1.61x faster                                                          |
| spectral_norm              | 70.0 ms                                                         | 46.0 ms: 1.52x faster                                                          |
| create_gc_cycles           | 1.08 ms                                                         | 750 us: 1.44x faster                                                           |
| deepcopy                   | 311 us                                                          | 233 us: 1.33x faster                                                           |
| float                      | 56.4 ms                                                         | 43.8 ms: 1.29x faster                                                          |
| mako                       | 7.02 ms                                                         | 5.47 ms: 1.28x faster                                                          |
| bench_mp_pool              | 93.6 ms                                                         | 75.0 ms: 1.25x faster                                                          |
| scimark_sor                | 85.8 ms                                                         | 68.7 ms: 1.25x faster                                                          |
| gc_traversal               | 1.76 ms                                                         | 1.42 ms: 1.24x faster                                                          |
| fannkuch                   | 288 ms                                                          | 238 ms: 1.21x faster                                                           |
| scimark_sparse_mat_mult    | 2.88 ms                                                         | 2.39 ms: 1.21x faster                                                          |
| python_startup             | 28.3 ms                                                         | 23.7 ms: 1.19x faster                                                          |
| crypto_pyaes               | 56.6 ms                                                         | 47.5 ms: 1.19x faster                                                          |
| scimark_fft                | 204 ms                                                          | 174 ms: 1.17x faster                                                           |
| xml_etree_generate         | 61.9 ms                                                         | 52.7 ms: 1.17x faster                                                          |
| pyflate                    | 322 ms                                                          | 274 ms: 1.17x faster                                                           |
| deepcopy_reduce            | 2.94 us                                                         | 2.52 us: 1.17x faster                                                          |
| comprehensions             | 13.1 us                                                         | 11.3 us: 1.17x faster                                                          |
| tomli_loads                | 1.74 sec                                                        | 1.50 sec: 1.16x faster                                                         |
| xml_etree_process          | 44.6 ms                                                         | 39.5 ms: 1.13x faster                                                          |
| deltablue                  | 2.35 ms                                                         | 2.09 ms: 1.13x faster                                                          |
| json_dumps                 | 7.53 ms                                                         | 6.71 ms: 1.12x faster                                                          |
| async_tree_memoization_tg  | 287 ms                                                          | 258 ms: 1.11x faster                                                           |
| async_tree_none            | 245 ms                                                          | 223 ms: 1.10x faster                                                           |
| json                       | 4.40 ms                                                         | 4.01 ms: 1.10x faster                                                          |
| pprint_safe_repr           | 658 ms                                                          | 600 ms: 1.10x faster                                                           |
| pathlib                    | 89.1 ms                                                         | 82.2 ms: 1.08x faster                                                          |
| meteor_contest             | 78.1 ms                                                         | 72.7 ms: 1.07x faster                                                          |
| go                         | 111 ms                                                          | 103 ms: 1.07x faster                                                           |
| async_tree_memoization     | 302 ms                                                          | 281 ms: 1.07x faster                                                           |
| async_tree_none_tg         | 216 ms                                                          | 204 ms: 1.06x faster                                                           |
| bench_thread_pool          | 1.04 ms                                                         | 984 us: 1.06x faster                                                           |
| json_loads                 | 21.7 us                                                         | 20.6 us: 1.05x faster                                                          |
| tornado_http               | 105 ms                                                          | 99.7 ms: 1.05x faster                                                          |
| pidigits                   | 204 ms                                                          | 195 ms: 1.04x faster                                                           |
| dulwich_log                | 50.2 ms                                                         | 48.3 ms: 1.04x faster                                                          |
| pprint_pformat             | 1.32 sec                                                        | 1.27 sec: 1.04x faster                                                         |
| pycparser                  | 869 ms                                                          | 839 ms: 1.04x faster                                                           |
| logging_silent             | 62.4 ns                                                         | 60.3 ns: 1.03x faster                                                          |
| python_startup_no_site     | 20.2 ms                                                         | 19.5 ms: 1.03x faster                                                          |
| richards_super             | 37.0 ms                                                         | 36.4 ms: 1.02x faster                                                          |
| scimark_lu                 | 60.7 ms                                                         | 59.9 ms: 1.01x faster                                                          |
| richards                   | 33.4 ms                                                         | 33.0 ms: 1.01x faster                                                          |
| telco                      | 6.27 ms                                                         | 6.20 ms: 1.01x faster                                                          |
| async_tree_cpu_io_mixed    | 490 ms                                                          | 485 ms: 1.01x faster                                                           |
| logging_simple             | 7.89 us                                                         | 7.93 us: 1.00x slower                                                          |
| 2to3                       | 255 ms                                                          | 257 ms: 1.01x slower                                                           |
| xml_etree_iterparse        | 61.3 ms                                                         | 61.7 ms: 1.01x slower                                                          |
| unpickle_pure_python       | 162 us                                                          | 164 us: 1.01x slower                                                           |
| xml_etree_parse            | 102 ms                                                          | 104 ms: 1.01x slower                                                           |
| async_tree_cpu_io_mixed_tg | 469 ms                                                          | 476 ms: 1.01x slower                                                           |
| regex_compile              | 101 ms                                                          | 103 ms: 1.02x slower                                                           |
| scimark_monte_carlo        | 48.7 ms                                                         | 49.9 ms: 1.02x slower                                                          |
| regex_v8                   | 15.5 ms                                                         | 15.9 ms: 1.03x slower                                                          |
| sqlglot_parse              | 1.02 ms                                                         | 1.05 ms: 1.03x slower                                                          |
| async_tree_io              | 530 ms                                                          | 547 ms: 1.03x slower                                                           |
| pickle_pure_python         | 239 us                                                          | 247 us: 1.03x slower                                                           |
| sympy_str                  | 214 ms                                                          | 222 ms: 1.04x slower                                                           |
| regex_dna                  | 112 ms                                                          | 116 ms: 1.04x slower                                                           |
| nqueens                    | 75.1 ms                                                         | 78.7 ms: 1.05x slower                                                          |
| async_tree_io_tg           | 499 ms                                                          | 524 ms: 1.05x slower                                                           |
| sympy_sum                  | 108 ms                                                          | 114 ms: 1.05x slower                                                           |
| sympy_expand               | 377 ms                                                          | 402 ms: 1.06x slower                                                           |
| hexiom                     | 4.60 ms                                                         | 4.91 ms: 1.07x slower                                                          |
| typing_runtime_protocols   | 141 us                                                          | 151 us: 1.07x slower                                                           |
| regex_effbot               | 1.82 ms                                                         | 1.95 ms: 1.07x slower                                                          |
| sqlglot_transpile          | 1.26 ms                                                         | 1.36 ms: 1.08x slower                                                          |
| mdp                        | 1.70 sec                                                        | 1.83 sec: 1.08x slower                                                         |
| django_template            | 32.0 ms                                                         | 35.1 ms: 1.09x slower                                                          |
| sqlglot_optimize           | 42.4 ms                                                         | 46.4 ms: 1.09x slower                                                          |
| sympy_integrate            | 15.2 ms                                                         | 16.8 ms: 1.10x slower                                                          |
| chaos                      | 49.4 ms                                                         | 54.6 ms: 1.10x slower                                                          |
| docutils                   | 1.80 sec                                                        | 2.00 sec: 1.11x slower                                                         |
| generators                 | 21.5 ms                                                         | 24.0 ms: 1.11x slower                                                          |
| genshi_xml                 | 49.0 ms                                                         | 56.0 ms: 1.14x slower                                                          |
| coroutines                 | 16.1 ms                                                         | 18.5 ms: 1.14x slower                                                          |
| pylint                     | 225 ms                                                          | 265 ms: 1.18x slower                                                           |
| genshi_text                | 21.7 ms                                                         | 25.8 ms: 1.19x slower                                                          |
| async_generators           | 267 ms                                                          | 320 ms: 1.20x slower                                                           |
| raytrace                   | 203 ms                                                          | 248 ms: 1.22x slower                                                           |
| Geometric mean             | (ref)                                                           | 1.11x faster                                                                   |

Benchmark hidden because not significant (2): logging_format, html5lib
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: asyncio_websockets, bpe_tokeniser, chameleon, connected_components, gevent_hub, k_core, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20240914-3.14.0a0-401fff7-JIT/bm-20240914-pythonperf1_win32-x86-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.112x faster
# HPT report

- Reliability score: 94.89% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown