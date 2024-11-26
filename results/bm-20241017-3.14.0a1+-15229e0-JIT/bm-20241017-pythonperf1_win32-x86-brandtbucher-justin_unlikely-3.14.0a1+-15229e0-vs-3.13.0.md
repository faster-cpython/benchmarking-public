# Results vs. 3.13.0

- fork: brandtbucher
- ref: justin_unlikely
- machine: windows-x86
- commit hash: 15229e0
- commit date: 2024-10-17
- overall geometric mean: 1.075x faster
- HPT reliability: 72.40%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241017-pythonperf1_win32-x86-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 255 ms                                                          | 264 ms: 1.04x slower                                                             |
| docutils       | 1.80 sec                                                        | 2.05 sec: 1.14x slower                                                           |
| html5lib       | 47.1 ms                                                         | 46.6 ms: 1.01x faster                                                            |
| sphinx         | 729 ms                                                          | 848 ms: 1.16x slower                                                             |
| tornado_http   | 105 ms                                                          | 110 ms: 1.05x slower                                                             |
| Geometric mean | (ref)                                                           | 1.07x slower                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241017-pythonperf1_win32-x86-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 287 ms                                                          | 255 ms: 1.12x faster                                                             |
| async_tree_none            | 245 ms                                                          | 218 ms: 1.12x faster                                                             |
| async_tree_memoization     | 302 ms                                                          | 278 ms: 1.08x faster                                                             |
| async_tree_cpu_io_mixed    | 490 ms                                                          | 462 ms: 1.06x faster                                                             |
| async_tree_none_tg         | 216 ms                                                          | 204 ms: 1.06x faster                                                             |
| async_tree_cpu_io_mixed_tg | 469 ms                                                          | 462 ms: 1.02x faster                                                             |
| coroutines                 | 16.1 ms                                                         | 17.4 ms: 1.08x slower                                                            |
| async_tree_io_tg           | 499 ms                                                          | 555 ms: 1.11x slower                                                             |
| async_generators           | 267 ms                                                          | 314 ms: 1.18x slower                                                             |
| Geometric mean             | (ref)                                                           | 1.01x faster                                                                     |

Benchmark hidden because not significant (1): async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241017-pythonperf1_win32-x86-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| nbody          | 81.4 ms                                                         | 57.1 ms: 1.42x faster                                                            |
| float          | 56.4 ms                                                         | 46.5 ms: 1.21x faster                                                            |
| pidigits       | 204 ms                                                          | 200 ms: 1.02x faster                                                             |
| Geometric mean | (ref)                                                           | 1.21x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241017-pythonperf1_win32-x86-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_v8       | 15.5 ms                                                         | 15.0 ms: 1.03x faster                                                            |
| regex_effbot   | 1.82 ms                                                         | 1.80 ms: 1.01x faster                                                            |
| regex_dna      | 112 ms                                                          | 113 ms: 1.01x slower                                                             |
| regex_compile  | 101 ms                                                          | 105 ms: 1.04x slower                                                             |
| Geometric mean | (ref)                                                           | 1.00x slower                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241017-pythonperf1_win32-x86-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| tomli_loads          | 1.74 sec                                                        | 1.49 sec: 1.17x faster                                                           |
| xml_etree_generate   | 61.9 ms                                                         | 55.0 ms: 1.13x faster                                                            |
| xml_etree_process    | 44.6 ms                                                         | 41.5 ms: 1.08x faster                                                            |
| json_loads           | 21.7 us                                                         | 20.5 us: 1.06x faster                                                            |
| unpickle_pure_python | 162 us                                                          | 156 us: 1.04x faster                                                             |
| pickle_pure_python   | 239 us                                                          | 244 us: 1.02x slower                                                             |
| xml_etree_iterparse  | 61.3 ms                                                         | 63.0 ms: 1.03x slower                                                            |
| json_dumps           | 7.53 ms                                                         | 7.95 ms: 1.06x slower                                                            |
| xml_etree_parse      | 102 ms                                                          | 109 ms: 1.07x slower                                                             |
| Geometric mean       | (ref)                                                           | 1.03x faster                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241017-pythonperf1_win32-x86-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup | 28.3 ms                                                         | 26.8 ms: 1.06x faster                                                            |
| Geometric mean | (ref)                                                           | 1.02x faster                                                                     |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241017-pythonperf1_win32-x86-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| mako            | 7.02 ms                                                         | 5.82 ms: 1.21x faster                                                            |
| django_template | 32.0 ms                                                         | 33.3 ms: 1.04x slower                                                            |
| genshi_xml      | 49.0 ms                                                         | 55.2 ms: 1.13x slower                                                            |
| genshi_text     | 21.7 ms                                                         | 24.6 ms: 1.13x slower                                                            |
| Geometric mean  | (ref)                                                           | 1.02x slower                                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241017-pythonperf1_win32-x86-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| thrift                     | 10.3 ms                                                         | 794 us: 12.92x faster                                                            |
| coverage                   | 326 ms                                                          | 53.8 ms: 6.07x faster                                                            |
| sqlglot_normalize          | 223 ms                                                          | 103 ms: 2.17x faster                                                             |
| deepcopy_memo              | 26.2 us                                                         | 15.9 us: 1.64x faster                                                            |
| nbody                      | 81.4 ms                                                         | 57.1 ms: 1.42x faster                                                            |
| deepcopy                   | 311 us                                                          | 225 us: 1.38x faster                                                             |
| deepcopy_reduce            | 2.94 us                                                         | 2.28 us: 1.29x faster                                                            |
| scimark_sor                | 85.8 ms                                                         | 68.1 ms: 1.26x faster                                                            |
| scimark_monte_carlo        | 48.7 ms                                                         | 39.6 ms: 1.23x faster                                                            |
| float                      | 56.4 ms                                                         | 46.5 ms: 1.21x faster                                                            |
| mako                       | 7.02 ms                                                         | 5.82 ms: 1.21x faster                                                            |
| spectral_norm              | 70.0 ms                                                         | 58.3 ms: 1.20x faster                                                            |
| fannkuch                   | 288 ms                                                          | 244 ms: 1.18x faster                                                             |
| tomli_loads                | 1.74 sec                                                        | 1.49 sec: 1.17x faster                                                           |
| go                         | 111 ms                                                          | 94.8 ms: 1.17x faster                                                            |
| pprint_safe_repr           | 658 ms                                                          | 564 ms: 1.17x faster                                                             |
| logging_silent             | 62.4 ns                                                         | 54.6 ns: 1.14x faster                                                            |
| crypto_pyaes               | 56.6 ms                                                         | 50.0 ms: 1.13x faster                                                            |
| pprint_pformat             | 1.32 sec                                                        | 1.17 sec: 1.13x faster                                                           |
| scimark_sparse_mat_mult    | 2.88 ms                                                         | 2.55 ms: 1.13x faster                                                            |
| xml_etree_generate         | 61.9 ms                                                         | 55.0 ms: 1.13x faster                                                            |
| async_tree_memoization_tg  | 287 ms                                                          | 255 ms: 1.12x faster                                                             |
| async_tree_none            | 245 ms                                                          | 218 ms: 1.12x faster                                                             |
| scimark_fft                | 204 ms                                                          | 183 ms: 1.12x faster                                                             |
| async_tree_memoization     | 302 ms                                                          | 278 ms: 1.08x faster                                                             |
| xml_etree_process          | 44.6 ms                                                         | 41.5 ms: 1.08x faster                                                            |
| meteor_contest             | 78.1 ms                                                         | 73.1 ms: 1.07x faster                                                            |
| async_tree_cpu_io_mixed    | 490 ms                                                          | 462 ms: 1.06x faster                                                             |
| async_tree_none_tg         | 216 ms                                                          | 204 ms: 1.06x faster                                                             |
| python_startup             | 28.3 ms                                                         | 26.8 ms: 1.06x faster                                                            |
| json_loads                 | 21.7 us                                                         | 20.5 us: 1.06x faster                                                            |
| telco                      | 6.27 ms                                                         | 5.95 ms: 1.05x faster                                                            |
| pycparser                  | 869 ms                                                          | 833 ms: 1.04x faster                                                             |
| unpickle_pure_python       | 162 us                                                          | 156 us: 1.04x faster                                                             |
| pyflate                    | 322 ms                                                          | 311 ms: 1.03x faster                                                             |
| logging_simple             | 7.89 us                                                         | 7.65 us: 1.03x faster                                                            |
| regex_v8                   | 15.5 ms                                                         | 15.0 ms: 1.03x faster                                                            |
| logging_format             | 8.59 us                                                         | 8.37 us: 1.03x faster                                                            |
| pidigits                   | 204 ms                                                          | 200 ms: 1.02x faster                                                             |
| async_tree_cpu_io_mixed_tg | 469 ms                                                          | 462 ms: 1.02x faster                                                             |
| pathlib                    | 89.1 ms                                                         | 87.7 ms: 1.02x faster                                                            |
| dulwich_log                | 50.2 ms                                                         | 49.5 ms: 1.01x faster                                                            |
| html5lib                   | 47.1 ms                                                         | 46.6 ms: 1.01x faster                                                            |
| typing_runtime_protocols   | 141 us                                                          | 139 us: 1.01x faster                                                             |
| regex_effbot               | 1.82 ms                                                         | 1.80 ms: 1.01x faster                                                            |
| regex_dna                  | 112 ms                                                          | 113 ms: 1.01x slower                                                             |
| pickle_pure_python         | 239 us                                                          | 244 us: 1.02x slower                                                             |
| bench_mp_pool              | 93.6 ms                                                         | 95.5 ms: 1.02x slower                                                            |
| xml_etree_iterparse        | 61.3 ms                                                         | 63.0 ms: 1.03x slower                                                            |
| nqueens                    | 75.1 ms                                                         | 77.4 ms: 1.03x slower                                                            |
| sqlglot_parse              | 1.02 ms                                                         | 1.05 ms: 1.03x slower                                                            |
| gc_traversal               | 1.76 ms                                                         | 1.83 ms: 1.04x slower                                                            |
| 2to3                       | 255 ms                                                          | 264 ms: 1.04x slower                                                             |
| django_template            | 32.0 ms                                                         | 33.3 ms: 1.04x slower                                                            |
| regex_compile              | 101 ms                                                          | 105 ms: 1.04x slower                                                             |
| tornado_http               | 105 ms                                                          | 110 ms: 1.05x slower                                                             |
| sympy_expand               | 377 ms                                                          | 397 ms: 1.05x slower                                                             |
| json_dumps                 | 7.53 ms                                                         | 7.95 ms: 1.06x slower                                                            |
| mdp                        | 1.70 sec                                                        | 1.80 sec: 1.06x slower                                                           |
| xml_etree_parse            | 102 ms                                                          | 109 ms: 1.07x slower                                                             |
| coroutines                 | 16.1 ms                                                         | 17.4 ms: 1.08x slower                                                            |
| sympy_str                  | 214 ms                                                          | 231 ms: 1.08x slower                                                             |
| sqlglot_transpile          | 1.26 ms                                                         | 1.37 ms: 1.08x slower                                                            |
| deltablue                  | 2.35 ms                                                         | 2.57 ms: 1.10x slower                                                            |
| create_gc_cycles           | 1.08 ms                                                         | 1.19 ms: 1.10x slower                                                            |
| sympy_sum                  | 108 ms                                                          | 119 ms: 1.10x slower                                                             |
| async_tree_io_tg           | 499 ms                                                          | 555 ms: 1.11x slower                                                             |
| chaos                      | 49.4 ms                                                         | 55.2 ms: 1.12x slower                                                            |
| genshi_xml                 | 49.0 ms                                                         | 55.2 ms: 1.13x slower                                                            |
| generators                 | 21.5 ms                                                         | 24.3 ms: 1.13x slower                                                            |
| genshi_text                | 21.7 ms                                                         | 24.6 ms: 1.13x slower                                                            |
| docutils                   | 1.80 sec                                                        | 2.05 sec: 1.14x slower                                                           |
| sympy_integrate            | 15.2 ms                                                         | 17.4 ms: 1.14x slower                                                            |
| json                       | 4.40 ms                                                         | 5.06 ms: 1.15x slower                                                            |
| sphinx                     | 729 ms                                                          | 848 ms: 1.16x slower                                                             |
| hexiom                     | 4.60 ms                                                         | 5.39 ms: 1.17x slower                                                            |
| async_generators           | 267 ms                                                          | 314 ms: 1.18x slower                                                             |
| richards                   | 33.4 ms                                                         | 39.3 ms: 1.18x slower                                                            |
| sqlglot_optimize           | 42.4 ms                                                         | 50.3 ms: 1.19x slower                                                            |
| richards_super             | 37.0 ms                                                         | 46.2 ms: 1.25x slower                                                            |
| pylint                     | 225 ms                                                          | 286 ms: 1.27x slower                                                             |
| raytrace                   | 203 ms                                                          | 273 ms: 1.35x slower                                                             |
| Geometric mean             | (ref)                                                           | 1.08x faster                                                                     |

Benchmark hidden because not significant (5): bench_thread_pool, async_tree_io, scimark_lu, comprehensions, python_startup_no_site
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: asyncio_websockets, bpe_tokeniser, chameleon, connected_components, gevent_hub, k_core, shortest_path, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20241017-3.14.0a1+-15229e0-JIT/bm-20241017-pythonperf1_win32-x86-brandtbucher-justin_unlikely-3.14.0a1+-15229e0.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.075x faster
# HPT report

- Reliability score: 72.40% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown