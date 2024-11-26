# Results vs. 3.13.0

- fork: mdboom
- ref: marshal_slice
- machine: windows-x86
- commit hash: 0e19ac7
- commit date: 2024-10-07
- overall geometric mean: 1.007x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241007-pythonperf1_win32-x86-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| docutils       | 1.80 sec                                                        | 1.90 sec: 1.05x slower                                                  |
| html5lib       | 47.1 ms                                                         | 46.2 ms: 1.02x faster                                                   |
| Geometric mean | (ref)                                                           | 1.01x slower                                                            |

Benchmark hidden because not significant (2): 2to3, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241007-pythonperf1_win32-x86-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 287 ms                                                          | 254 ms: 1.13x faster                                                    |
| async_tree_none            | 245 ms                                                          | 218 ms: 1.12x faster                                                    |
| async_tree_memoization     | 302 ms                                                          | 274 ms: 1.10x faster                                                    |
| async_tree_none_tg         | 216 ms                                                          | 199 ms: 1.08x faster                                                    |
| async_tree_cpu_io_mixed    | 490 ms                                                          | 473 ms: 1.03x faster                                                    |
| async_tree_cpu_io_mixed_tg | 469 ms                                                          | 460 ms: 1.02x faster                                                    |
| async_tree_io_tg           | 499 ms                                                          | 518 ms: 1.04x slower                                                    |
| coroutines                 | 16.1 ms                                                         | 18.4 ms: 1.14x slower                                                   |
| async_generators           | 267 ms                                                          | 305 ms: 1.14x slower                                                    |
| Geometric mean             | (ref)                                                           | 1.02x faster                                                            |

Benchmark hidden because not significant (1): async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241007-pythonperf1_win32-x86-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pidigits       | 204 ms                                                          | 201 ms: 1.01x faster                                                    |
| float          | 56.4 ms                                                         | 63.6 ms: 1.13x slower                                                   |
| nbody          | 81.4 ms                                                         | 96.4 ms: 1.18x slower                                                   |
| Geometric mean | (ref)                                                           | 1.10x slower                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241007-pythonperf1_win32-x86-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_dna      | 112 ms                                                          | 116 ms: 1.04x slower                                                    |
| regex_v8       | 15.5 ms                                                         | 16.1 ms: 1.04x slower                                                   |
| regex_effbot   | 1.82 ms                                                         | 1.91 ms: 1.05x slower                                                   |
| regex_compile  | 101 ms                                                          | 111 ms: 1.10x slower                                                    |
| Geometric mean | (ref)                                                           | 1.05x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241007-pythonperf1_win32-x86-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| json_loads           | 21.7 us                                                         | 20.9 us: 1.04x faster                                                   |
| json_dumps           | 7.53 ms                                                         | 7.75 ms: 1.03x slower                                                   |
| xml_etree_parse      | 102 ms                                                          | 107 ms: 1.05x slower                                                    |
| tomli_loads          | 1.74 sec                                                        | 1.91 sec: 1.09x slower                                                  |
| xml_etree_iterparse  | 61.3 ms                                                         | 67.8 ms: 1.11x slower                                                   |
| xml_etree_generate   | 61.9 ms                                                         | 69.3 ms: 1.12x slower                                                   |
| pickle_pure_python   | 239 us                                                          | 268 us: 1.12x slower                                                    |
| unpickle_pure_python | 162 us                                                          | 190 us: 1.17x slower                                                    |
| xml_etree_process    | 44.6 ms                                                         | 52.5 ms: 1.18x slower                                                   |
| Geometric mean       | (ref)                                                           | 1.09x slower                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241007-pythonperf1_win32-x86-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|------------------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 28.3 ms                                                         | 23.8 ms: 1.19x faster                                                   |
| python_startup_no_site | 20.2 ms                                                         | 19.7 ms: 1.02x faster                                                   |
| Geometric mean         | (ref)                                                           | 1.10x faster                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241007-pythonperf1_win32-x86-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|-----------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_xml      | 49.0 ms                                                         | 46.6 ms: 1.05x faster                                                   |
| genshi_text     | 21.7 ms                                                         | 23.0 ms: 1.06x slower                                                   |
| django_template | 32.0 ms                                                         | 35.2 ms: 1.10x slower                                                   |
| mako            | 7.02 ms                                                         | 8.22 ms: 1.17x slower                                                   |
| Geometric mean  | (ref)                                                           | 1.07x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241007-pythonperf1_win32-x86-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| thrift                     | 10.3 ms                                                         | 745 us: 13.76x faster                                                   |
| coverage                   | 326 ms                                                          | 54.0 ms: 6.04x faster                                                   |
| create_gc_cycles           | 1.08 ms                                                         | 764 us: 1.42x faster                                                    |
| bench_mp_pool              | 93.6 ms                                                         | 73.1 ms: 1.28x faster                                                   |
| deepcopy                   | 311 us                                                          | 244 us: 1.28x faster                                                    |
| gc_traversal               | 1.76 ms                                                         | 1.45 ms: 1.21x faster                                                   |
| python_startup             | 28.3 ms                                                         | 23.8 ms: 1.19x faster                                                   |
| deepcopy_memo              | 26.2 us                                                         | 22.1 us: 1.18x faster                                                   |
| deepcopy_reduce            | 2.94 us                                                         | 2.58 us: 1.14x faster                                                   |
| async_tree_memoization_tg  | 287 ms                                                          | 254 ms: 1.13x faster                                                    |
| async_tree_none            | 245 ms                                                          | 218 ms: 1.12x faster                                                    |
| async_tree_memoization     | 302 ms                                                          | 274 ms: 1.10x faster                                                    |
| async_tree_none_tg         | 216 ms                                                          | 199 ms: 1.08x faster                                                    |
| genshi_xml                 | 49.0 ms                                                         | 46.6 ms: 1.05x faster                                                   |
| bench_thread_pool          | 1.04 ms                                                         | 999 us: 1.04x faster                                                    |
| json_loads                 | 21.7 us                                                         | 20.9 us: 1.04x faster                                                   |
| async_tree_cpu_io_mixed    | 490 ms                                                          | 473 ms: 1.03x faster                                                    |
| pathlib                    | 89.1 ms                                                         | 86.5 ms: 1.03x faster                                                   |
| python_startup_no_site     | 20.2 ms                                                         | 19.7 ms: 1.02x faster                                                   |
| async_tree_cpu_io_mixed_tg | 469 ms                                                          | 460 ms: 1.02x faster                                                    |
| html5lib                   | 47.1 ms                                                         | 46.2 ms: 1.02x faster                                                   |
| pidigits                   | 204 ms                                                          | 201 ms: 1.01x faster                                                    |
| pycparser                  | 869 ms                                                          | 875 ms: 1.01x slower                                                    |
| sympy_sum                  | 108 ms                                                          | 109 ms: 1.01x slower                                                    |
| meteor_contest             | 78.1 ms                                                         | 80.1 ms: 1.02x slower                                                   |
| json_dumps                 | 7.53 ms                                                         | 7.75 ms: 1.03x slower                                                   |
| nqueens                    | 75.1 ms                                                         | 77.5 ms: 1.03x slower                                                   |
| pprint_safe_repr           | 658 ms                                                          | 679 ms: 1.03x slower                                                    |
| regex_dna                  | 112 ms                                                          | 116 ms: 1.04x slower                                                    |
| logging_format             | 8.59 us                                                         | 8.90 us: 1.04x slower                                                   |
| sympy_str                  | 214 ms                                                          | 222 ms: 1.04x slower                                                    |
| dulwich_log                | 50.2 ms                                                         | 52.1 ms: 1.04x slower                                                   |
| async_tree_io_tg           | 499 ms                                                          | 518 ms: 1.04x slower                                                    |
| typing_runtime_protocols   | 141 us                                                          | 146 us: 1.04x slower                                                    |
| regex_v8                   | 15.5 ms                                                         | 16.1 ms: 1.04x slower                                                   |
| crypto_pyaes               | 56.6 ms                                                         | 59.0 ms: 1.04x slower                                                   |
| logging_simple             | 7.89 us                                                         | 8.23 us: 1.04x slower                                                   |
| sympy_expand               | 377 ms                                                          | 394 ms: 1.04x slower                                                    |
| xml_etree_parse            | 102 ms                                                          | 107 ms: 1.05x slower                                                    |
| regex_effbot               | 1.82 ms                                                         | 1.91 ms: 1.05x slower                                                   |
| sympy_integrate            | 15.2 ms                                                         | 16.0 ms: 1.05x slower                                                   |
| pylint                     | 225 ms                                                          | 236 ms: 1.05x slower                                                    |
| docutils                   | 1.80 sec                                                        | 1.90 sec: 1.05x slower                                                  |
| genshi_text                | 21.7 ms                                                         | 23.0 ms: 1.06x slower                                                   |
| comprehensions             | 13.1 us                                                         | 14.1 us: 1.07x slower                                                   |
| sqlglot_normalize          | 223 ms                                                          | 240 ms: 1.08x slower                                                    |
| pprint_pformat             | 1.32 sec                                                        | 1.44 sec: 1.09x slower                                                  |
| sqlglot_transpile          | 1.26 ms                                                         | 1.37 ms: 1.09x slower                                                   |
| telco                      | 6.27 ms                                                         | 6.85 ms: 1.09x slower                                                   |
| sqlglot_parse              | 1.02 ms                                                         | 1.12 ms: 1.09x slower                                                   |
| sqlglot_optimize           | 42.4 ms                                                         | 46.4 ms: 1.09x slower                                                   |
| tomli_loads                | 1.74 sec                                                        | 1.91 sec: 1.09x slower                                                  |
| regex_compile              | 101 ms                                                          | 111 ms: 1.10x slower                                                    |
| django_template            | 32.0 ms                                                         | 35.2 ms: 1.10x slower                                                   |
| xml_etree_iterparse        | 61.3 ms                                                         | 67.8 ms: 1.11x slower                                                   |
| xml_etree_generate         | 61.9 ms                                                         | 69.3 ms: 1.12x slower                                                   |
| pickle_pure_python         | 239 us                                                          | 268 us: 1.12x slower                                                    |
| fannkuch                   | 288 ms                                                          | 324 ms: 1.12x slower                                                    |
| float                      | 56.4 ms                                                         | 63.6 ms: 1.13x slower                                                   |
| chaos                      | 49.4 ms                                                         | 56.1 ms: 1.14x slower                                                   |
| coroutines                 | 16.1 ms                                                         | 18.4 ms: 1.14x slower                                                   |
| scimark_sparse_mat_mult    | 2.88 ms                                                         | 3.29 ms: 1.14x slower                                                   |
| async_generators           | 267 ms                                                          | 305 ms: 1.14x slower                                                    |
| pyflate                    | 322 ms                                                          | 369 ms: 1.15x slower                                                    |
| spectral_norm              | 70.0 ms                                                         | 80.5 ms: 1.15x slower                                                   |
| scimark_fft                | 204 ms                                                          | 237 ms: 1.16x slower                                                    |
| hexiom                     | 4.60 ms                                                         | 5.34 ms: 1.16x slower                                                   |
| scimark_lu                 | 60.7 ms                                                         | 71.1 ms: 1.17x slower                                                   |
| mako                       | 7.02 ms                                                         | 8.22 ms: 1.17x slower                                                   |
| unpickle_pure_python       | 162 us                                                          | 190 us: 1.17x slower                                                    |
| xml_etree_process          | 44.6 ms                                                         | 52.5 ms: 1.18x slower                                                   |
| nbody                      | 81.4 ms                                                         | 96.4 ms: 1.18x slower                                                   |
| scimark_sor                | 85.8 ms                                                         | 103 ms: 1.20x slower                                                    |
| deltablue                  | 2.35 ms                                                         | 2.82 ms: 1.20x slower                                                   |
| scimark_monte_carlo        | 48.7 ms                                                         | 58.6 ms: 1.20x slower                                                   |
| logging_silent             | 62.4 ns                                                         | 75.6 ns: 1.21x slower                                                   |
| richards                   | 33.4 ms                                                         | 40.8 ms: 1.22x slower                                                   |
| richards_super             | 37.0 ms                                                         | 47.0 ms: 1.27x slower                                                   |
| raytrace                   | 203 ms                                                          | 259 ms: 1.28x slower                                                    |
| generators                 | 21.5 ms                                                         | 27.5 ms: 1.28x slower                                                   |
| Geometric mean             | (ref)                                                           | 1.01x faster                                                            |

Benchmark hidden because not significant (6): json, 2to3, mdp, go, tornado_http, async_tree_io
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: asyncio_websockets, bpe_tokeniser, chameleon, connected_components, gevent_hub, k_core, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20241007-3.14.0a0-0e19ac7/bm-20241007-pythonperf1_win32-x86-mdboom-marshal_slice-3.14.0a0-0e19ac7.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.007x faster
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.02x

# Memory
- memory change: unknown