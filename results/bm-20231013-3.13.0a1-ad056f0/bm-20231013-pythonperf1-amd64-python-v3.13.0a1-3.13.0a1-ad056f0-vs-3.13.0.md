# Results vs. 3.13.0

- fork: python
- ref: v3.13.0a1
- machine: windows-amd64
- commit hash: ad056f0
- commit date: 2023-10-13
- overall geometric mean: 1.039x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20231013-pythonperf1-amd64-python-v3.13.0a1-3.13.0a1-ad056f0 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| 2to3           | 221 ms                                                      | 216 ms: 1.03x faster                                            |
| chameleon      | 4.82 ms                                                     | 4.98 ms: 1.03x slower                                           |
| docutils       | 1.57 sec                                                    | 1.61 sec: 1.03x slower                                          |
| tornado_http   | 93.0 ms                                                     | 89.1 ms: 1.04x faster                                           |
| Geometric mean | (ref)                                                       | 1.00x faster                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20231013-pythonperf1-amd64-python-v3.13.0a1-3.13.0a1-ad056f0 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| async_generators           | 223 ms                                                      | 236 ms: 1.06x slower                                            |
| coroutines                 | 12.8 ms                                                     | 14.7 ms: 1.15x slower                                           |
| async_tree_none            | 226 ms                                                      | 267 ms: 1.18x slower                                            |
| async_tree_cpu_io_mixed    | 383 ms                                                      | 455 ms: 1.19x slower                                            |
| async_tree_memoization     | 276 ms                                                      | 340 ms: 1.23x slower                                            |
| async_tree_memoization_tg  | 288 ms                                                      | 359 ms: 1.25x slower                                            |
| async_tree_cpu_io_mixed_tg | 377 ms                                                      | 486 ms: 1.29x slower                                            |
| async_tree_none_tg         | 209 ms                                                      | 285 ms: 1.36x slower                                            |
| async_tree_io              | 521 ms                                                      | 723 ms: 1.39x slower                                            |
| async_tree_io_tg           | 518 ms                                                      | 772 ms: 1.49x slower                                            |
| Geometric mean             | (ref)                                                       | 1.25x slower                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20231013-pythonperf1-amd64-python-v3.13.0a1-3.13.0a1-ad056f0 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| pidigits       | 148 ms                                                      | 150 ms: 1.02x slower                                            |
| nbody          | 68.4 ms                                                     | 72.2 ms: 1.06x slower                                           |
| float          | 49.9 ms                                                     | 53.6 ms: 1.07x slower                                           |
| Geometric mean | (ref)                                                       | 1.05x slower                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20231013-pythonperf1-amd64-python-v3.13.0a1-3.13.0a1-ad056f0 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_v8       | 21.4 ms                                                     | 14.8 ms: 1.44x faster                                           |
| regex_effbot   | 1.58 ms                                                     | 1.60 ms: 1.01x slower                                           |
| regex_dna      | 115 ms                                                      | 119 ms: 1.03x slower                                            |
| regex_compile  | 80.5 ms                                                     | 90.8 ms: 1.13x slower                                           |
| Geometric mean | (ref)                                                       | 1.05x faster                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20231013-pythonperf1-amd64-python-v3.13.0a1-3.13.0a1-ad056f0 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| json_loads           | 15.1 us                                                     | 13.5 us: 1.12x faster                                           |
| json_dumps           | 5.92 ms                                                     | 5.60 ms: 1.06x faster                                           |
| xml_etree_parse      | 93.6 ms                                                     | 91.6 ms: 1.02x faster                                           |
| xml_etree_generate   | 54.0 ms                                                     | 55.4 ms: 1.03x slower                                           |
| unpickle_pure_python | 133 us                                                      | 137 us: 1.03x slower                                            |
| xml_etree_process    | 37.0 ms                                                     | 38.2 ms: 1.03x slower                                           |
| xml_etree_iterparse  | 61.8 ms                                                     | 64.0 ms: 1.04x slower                                           |
| tomli_loads          | 1.39 sec                                                    | 1.48 sec: 1.06x slower                                          |
| Geometric mean       | (ref)                                                       | 1.00x faster                                                    |

Benchmark hidden because not significant (1): pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20231013-pythonperf1-amd64-python-v3.13.0a1-3.13.0a1-ad056f0 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup         | 25.4 ms                                                     | 19.7 ms: 1.29x faster                                           |
| python_startup_no_site | 18.1 ms                                                     | 16.2 ms: 1.12x faster                                           |
| Geometric mean         | (ref)                                                       | 1.20x faster                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20231013-pythonperf1-amd64-python-v3.13.0a1-3.13.0a1-ad056f0 |
|-----------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| mako      | 6.35 ms                                                     | 7.20 ms: 1.13x slower                                           |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20231013-pythonperf1-amd64-python-v3.13.0a1-3.13.0a1-ad056f0 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| create_gc_cycles           | 1.26 ms                                                     | 728 us: 1.73x faster                                            |
| regex_v8                   | 21.4 ms                                                     | 14.8 ms: 1.44x faster                                           |
| bench_mp_pool              | 86.4 ms                                                     | 64.0 ms: 1.35x faster                                           |
| gc_traversal               | 1.97 ms                                                     | 1.49 ms: 1.32x faster                                           |
| python_startup             | 25.4 ms                                                     | 19.7 ms: 1.29x faster                                           |
| json_loads                 | 15.1 us                                                     | 13.5 us: 1.12x faster                                           |
| python_startup_no_site     | 18.1 ms                                                     | 16.2 ms: 1.12x faster                                           |
| typing_runtime_protocols   | 105 us                                                      | 96.3 us: 1.10x faster                                           |
| json_dumps                 | 5.92 ms                                                     | 5.60 ms: 1.06x faster                                           |
| crypto_pyaes               | 45.4 ms                                                     | 43.3 ms: 1.05x faster                                           |
| tornado_http               | 93.0 ms                                                     | 89.1 ms: 1.04x faster                                           |
| pathlib                    | 80.9 ms                                                     | 78.5 ms: 1.03x faster                                           |
| 2to3                       | 221 ms                                                      | 216 ms: 1.03x faster                                            |
| xml_etree_parse            | 93.6 ms                                                     | 91.6 ms: 1.02x faster                                           |
| sympy_expand               | 291 ms                                                      | 287 ms: 1.02x faster                                            |
| fannkuch                   | 253 ms                                                      | 249 ms: 1.02x faster                                            |
| telco                      | 4.79 ms                                                     | 4.73 ms: 1.01x faster                                           |
| coverage                   | 45.6 ms                                                     | 45.4 ms: 1.00x faster                                           |
| scimark_monte_carlo        | 40.8 ms                                                     | 41.0 ms: 1.00x slower                                           |
| deepcopy_reduce            | 2.06 us                                                     | 2.07 us: 1.01x slower                                           |
| scimark_sor                | 76.2 ms                                                     | 77.0 ms: 1.01x slower                                           |
| meteor_contest             | 73.5 ms                                                     | 74.5 ms: 1.01x slower                                           |
| regex_effbot               | 1.58 ms                                                     | 1.60 ms: 1.01x slower                                           |
| deepcopy                   | 226 us                                                      | 230 us: 1.02x slower                                            |
| pidigits                   | 148 ms                                                      | 150 ms: 1.02x slower                                            |
| scimark_fft                | 172 ms                                                      | 176 ms: 1.02x slower                                            |
| docutils                   | 1.57 sec                                                    | 1.61 sec: 1.03x slower                                          |
| xml_etree_generate         | 54.0 ms                                                     | 55.4 ms: 1.03x slower                                           |
| pprint_safe_repr           | 494 ms                                                      | 507 ms: 1.03x slower                                            |
| unpickle_pure_python       | 133 us                                                      | 137 us: 1.03x slower                                            |
| regex_dna                  | 115 ms                                                      | 119 ms: 1.03x slower                                            |
| pprint_pformat             | 999 ms                                                      | 1.03 sec: 1.03x slower                                          |
| xml_etree_process          | 37.0 ms                                                     | 38.2 ms: 1.03x slower                                           |
| chameleon                  | 4.82 ms                                                     | 4.98 ms: 1.03x slower                                           |
| go                         | 87.0 ms                                                     | 90.0 ms: 1.04x slower                                           |
| sympy_str                  | 169 ms                                                      | 175 ms: 1.04x slower                                            |
| xml_etree_iterparse        | 61.8 ms                                                     | 64.0 ms: 1.04x slower                                           |
| richards_super             | 30.9 ms                                                     | 32.0 ms: 1.04x slower                                           |
| nqueens                    | 56.7 ms                                                     | 59.1 ms: 1.04x slower                                           |
| chaos                      | 38.5 ms                                                     | 40.4 ms: 1.05x slower                                           |
| sympy_sum                  | 86.9 ms                                                     | 91.1 ms: 1.05x slower                                           |
| hexiom                     | 3.89 ms                                                     | 4.09 ms: 1.05x slower                                           |
| sympy_integrate            | 12.5 ms                                                     | 13.1 ms: 1.05x slower                                           |
| sqlglot_normalize          | 175 ms                                                      | 184 ms: 1.05x slower                                            |
| sqlglot_parse              | 771 us                                                      | 811 us: 1.05x slower                                            |
| pyflate                    | 283 ms                                                      | 298 ms: 1.05x slower                                            |
| nbody                      | 68.4 ms                                                     | 72.2 ms: 1.06x slower                                           |
| richards                   | 27.3 ms                                                     | 28.8 ms: 1.06x slower                                           |
| sqlglot_optimize           | 32.9 ms                                                     | 34.8 ms: 1.06x slower                                           |
| async_generators           | 223 ms                                                      | 236 ms: 1.06x slower                                            |
| tomli_loads                | 1.39 sec                                                    | 1.48 sec: 1.06x slower                                          |
| deepcopy_memo              | 23.3 us                                                     | 24.8 us: 1.06x slower                                           |
| float                      | 49.9 ms                                                     | 53.6 ms: 1.07x slower                                           |
| sqlglot_transpile          | 956 us                                                      | 1.03 ms: 1.08x slower                                           |
| logging_simple             | 5.96 us                                                     | 6.40 us: 1.08x slower                                           |
| mdp                        | 1.39 sec                                                    | 1.49 sec: 1.08x slower                                          |
| logging_format             | 6.26 us                                                     | 6.81 us: 1.09x slower                                           |
| raytrace                   | 160 ms                                                      | 174 ms: 1.09x slower                                            |
| dulwich_log                | 40.8 ms                                                     | 45.2 ms: 1.11x slower                                           |
| scimark_lu                 | 53.0 ms                                                     | 58.6 ms: 1.11x slower                                           |
| regex_compile              | 80.5 ms                                                     | 90.8 ms: 1.13x slower                                           |
| mako                       | 6.35 ms                                                     | 7.20 ms: 1.13x slower                                           |
| deltablue                  | 1.92 ms                                                     | 2.19 ms: 1.14x slower                                           |
| generators                 | 19.5 ms                                                     | 22.3 ms: 1.14x slower                                           |
| coroutines                 | 12.8 ms                                                     | 14.7 ms: 1.15x slower                                           |
| logging_silent             | 54.6 ns                                                     | 63.2 ns: 1.16x slower                                           |
| async_tree_none            | 226 ms                                                      | 267 ms: 1.18x slower                                            |
| async_tree_cpu_io_mixed    | 383 ms                                                      | 455 ms: 1.19x slower                                            |
| async_tree_memoization     | 276 ms                                                      | 340 ms: 1.23x slower                                            |
| async_tree_memoization_tg  | 288 ms                                                      | 359 ms: 1.25x slower                                            |
| pycparser                  | 683 ms                                                      | 861 ms: 1.26x slower                                            |
| async_tree_cpu_io_mixed_tg | 377 ms                                                      | 486 ms: 1.29x slower                                            |
| async_tree_none_tg         | 209 ms                                                      | 285 ms: 1.36x slower                                            |
| comprehensions             | 10.3 us                                                     | 14.2 us: 1.38x slower                                           |
| async_tree_io              | 521 ms                                                      | 723 ms: 1.39x slower                                            |
| async_tree_io_tg           | 518 ms                                                      | 772 ms: 1.49x slower                                            |
| Geometric mean             | (ref)                                                       | 1.04x slower                                                    |

Benchmark hidden because not significant (5): json, bench_thread_pool, scimark_sparse_mat_mult, pickle_pure_python, spectral_norm
Ignored benchmarks (16) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: asyncio_websockets, bpe_tokeniser, connected_components, django_template, genshi_text, genshi_xml, gevent_hub, html5lib, k_core, mypy2, pylint, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, thrift
Ignored benchmarks (9) of results/bm-20231013-3.13.0a1-ad056f0/bm-20231013-pythonperf1-amd64-python-v3.13.0a1-3.13.0a1-ad056f0.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.039x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.02x

# Memory
- memory change: unknown