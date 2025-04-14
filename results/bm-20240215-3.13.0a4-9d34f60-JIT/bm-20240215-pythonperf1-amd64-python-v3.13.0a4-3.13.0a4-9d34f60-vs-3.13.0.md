# Results vs. 3.13.0

- fork: python
- ref: v3.13.0a4
- machine: windows-amd64
- commit hash: 9d34f60
- commit date: 2024-02-15
- overall geometric mean: 1.001x slower
- HPT reliability: 77.92%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240215-pythonperf1-amd64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| 2to3           | 221 ms                                                      | 217 ms: 1.02x faster                                            |
| chameleon      | 4.82 ms                                                     | 4.74 ms: 1.02x faster                                           |
| docutils       | 1.57 sec                                                    | 1.56 sec: 1.01x faster                                          |
| tornado_http   | 93.0 ms                                                     | 85.5 ms: 1.09x faster                                           |
| Geometric mean | (ref)                                                       | 1.03x faster                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240215-pythonperf1-amd64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| coroutines                 | 12.8 ms                                                     | 13.2 ms: 1.03x slower                                           |
| async_generators           | 223 ms                                                      | 238 ms: 1.07x slower                                            |
| async_tree_none            | 226 ms                                                      | 266 ms: 1.18x slower                                            |
| async_tree_cpu_io_mixed    | 383 ms                                                      | 455 ms: 1.19x slower                                            |
| async_tree_memoization_tg  | 288 ms                                                      | 350 ms: 1.21x slower                                            |
| async_tree_memoization     | 276 ms                                                      | 341 ms: 1.24x slower                                            |
| async_tree_cpu_io_mixed_tg | 377 ms                                                      | 472 ms: 1.25x slower                                            |
| async_tree_none_tg         | 209 ms                                                      | 272 ms: 1.30x slower                                            |
| async_tree_io              | 521 ms                                                      | 726 ms: 1.39x slower                                            |
| async_tree_io_tg           | 518 ms                                                      | 759 ms: 1.46x slower                                            |
| Geometric mean             | (ref)                                                       | 1.23x slower                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240215-pythonperf1-amd64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| nbody          | 68.4 ms                                                     | 61.0 ms: 1.12x faster                                           |
| pidigits       | 148 ms                                                      | 151 ms: 1.02x slower                                            |
| float          | 49.9 ms                                                     | 51.4 ms: 1.03x slower                                           |
| Geometric mean | (ref)                                                       | 1.02x faster                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240215-pythonperf1-amd64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_v8       | 21.4 ms                                                     | 14.3 ms: 1.50x faster                                           |
| regex_compile  | 80.5 ms                                                     | 79.3 ms: 1.02x faster                                           |
| regex_effbot   | 1.58 ms                                                     | 1.56 ms: 1.01x faster                                           |
| regex_dna      | 115 ms                                                      | 118 ms: 1.02x slower                                            |
| Geometric mean | (ref)                                                       | 1.11x faster                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240215-pythonperf1-amd64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| json_loads           | 15.1 us                                                     | 13.8 us: 1.09x faster                                           |
| pickle_pure_python   | 190 us                                                      | 174 us: 1.09x faster                                            |
| tomli_loads          | 1.39 sec                                                    | 1.30 sec: 1.07x faster                                          |
| json_dumps           | 5.92 ms                                                     | 5.54 ms: 1.07x faster                                           |
| unpickle_pure_python | 133 us                                                      | 126 us: 1.06x faster                                            |
| xml_etree_generate   | 54.0 ms                                                     | 51.9 ms: 1.04x faster                                           |
| xml_etree_process    | 37.0 ms                                                     | 35.9 ms: 1.03x faster                                           |
| xml_etree_parse      | 93.6 ms                                                     | 91.2 ms: 1.03x faster                                           |
| xml_etree_iterparse  | 61.8 ms                                                     | 62.9 ms: 1.02x slower                                           |
| Geometric mean       | (ref)                                                       | 1.05x faster                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240215-pythonperf1-amd64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup         | 25.4 ms                                                     | 20.5 ms: 1.24x faster                                           |
| python_startup_no_site | 18.1 ms                                                     | 18.5 ms: 1.02x slower                                           |
| Geometric mean         | (ref)                                                       | 1.10x faster                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240215-pythonperf1-amd64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|-----------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| mako      | 6.35 ms                                                     | 6.71 ms: 1.06x slower                                           |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240215-pythonperf1-amd64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| create_gc_cycles           | 1.26 ms                                                     | 736 us: 1.71x faster                                            |
| mypy2                      | 679 ms                                                      | 423 ms: 1.61x faster                                            |
| typing_runtime_protocols   | 105 us                                                      | 69.7 us: 1.51x faster                                           |
| regex_v8                   | 21.4 ms                                                     | 14.3 ms: 1.50x faster                                           |
| gc_traversal               | 1.97 ms                                                     | 1.51 ms: 1.31x faster                                           |
| bench_mp_pool              | 86.4 ms                                                     | 66.6 ms: 1.30x faster                                           |
| python_startup             | 25.4 ms                                                     | 20.5 ms: 1.24x faster                                           |
| nbody                      | 68.4 ms                                                     | 61.0 ms: 1.12x faster                                           |
| richards                   | 27.3 ms                                                     | 24.8 ms: 1.10x faster                                           |
| richards_super             | 30.9 ms                                                     | 28.2 ms: 1.10x faster                                           |
| json_loads                 | 15.1 us                                                     | 13.8 us: 1.09x faster                                           |
| deepcopy_memo              | 23.3 us                                                     | 21.3 us: 1.09x faster                                           |
| pickle_pure_python         | 190 us                                                      | 174 us: 1.09x faster                                            |
| tornado_http               | 93.0 ms                                                     | 85.5 ms: 1.09x faster                                           |
| deepcopy_reduce            | 2.06 us                                                     | 1.92 us: 1.08x faster                                           |
| pathlib                    | 80.9 ms                                                     | 75.3 ms: 1.07x faster                                           |
| tomli_loads                | 1.39 sec                                                    | 1.30 sec: 1.07x faster                                          |
| json_dumps                 | 5.92 ms                                                     | 5.54 ms: 1.07x faster                                           |
| unpickle_pure_python       | 133 us                                                      | 126 us: 1.06x faster                                            |
| sympy_expand               | 291 ms                                                      | 277 ms: 1.05x faster                                            |
| telco                      | 4.79 ms                                                     | 4.57 ms: 1.05x faster                                           |
| fannkuch                   | 253 ms                                                      | 242 ms: 1.05x faster                                            |
| deepcopy                   | 226 us                                                      | 217 us: 1.04x faster                                            |
| xml_etree_generate         | 54.0 ms                                                     | 51.9 ms: 1.04x faster                                           |
| sympy_str                  | 169 ms                                                      | 163 ms: 1.03x faster                                            |
| xml_etree_process          | 37.0 ms                                                     | 35.9 ms: 1.03x faster                                           |
| pprint_safe_repr           | 494 ms                                                      | 480 ms: 1.03x faster                                            |
| xml_etree_parse            | 93.6 ms                                                     | 91.2 ms: 1.03x faster                                           |
| sqlglot_parse              | 771 us                                                      | 755 us: 1.02x faster                                            |
| pprint_pformat             | 999 ms                                                      | 980 ms: 1.02x faster                                            |
| 2to3                       | 221 ms                                                      | 217 ms: 1.02x faster                                            |
| chameleon                  | 4.82 ms                                                     | 4.74 ms: 1.02x faster                                           |
| regex_compile              | 80.5 ms                                                     | 79.3 ms: 1.02x faster                                           |
| logging_silent             | 54.6 ns                                                     | 54.0 ns: 1.01x faster                                           |
| dulwich_log                | 40.8 ms                                                     | 40.4 ms: 1.01x faster                                           |
| regex_effbot               | 1.58 ms                                                     | 1.56 ms: 1.01x faster                                           |
| sqlglot_normalize          | 175 ms                                                      | 173 ms: 1.01x faster                                            |
| docutils                   | 1.57 sec                                                    | 1.56 sec: 1.01x faster                                          |
| spectral_norm              | 62.8 ms                                                     | 63.3 ms: 1.01x slower                                           |
| crypto_pyaes               | 45.4 ms                                                     | 45.8 ms: 1.01x slower                                           |
| xml_etree_iterparse        | 61.8 ms                                                     | 62.9 ms: 1.02x slower                                           |
| sqlglot_optimize           | 32.9 ms                                                     | 33.5 ms: 1.02x slower                                           |
| generators                 | 19.5 ms                                                     | 19.9 ms: 1.02x slower                                           |
| logging_format             | 6.26 us                                                     | 6.39 us: 1.02x slower                                           |
| python_startup_no_site     | 18.1 ms                                                     | 18.5 ms: 1.02x slower                                           |
| sqlglot_transpile          | 956 us                                                      | 978 us: 1.02x slower                                            |
| regex_dna                  | 115 ms                                                      | 118 ms: 1.02x slower                                            |
| pidigits                   | 148 ms                                                      | 151 ms: 1.02x slower                                            |
| sympy_integrate            | 12.5 ms                                                     | 12.8 ms: 1.03x slower                                           |
| float                      | 49.9 ms                                                     | 51.4 ms: 1.03x slower                                           |
| coroutines                 | 12.8 ms                                                     | 13.2 ms: 1.03x slower                                           |
| raytrace                   | 160 ms                                                      | 166 ms: 1.03x slower                                            |
| comprehensions             | 10.3 us                                                     | 10.6 us: 1.04x slower                                           |
| deltablue                  | 1.92 ms                                                     | 1.99 ms: 1.04x slower                                           |
| meteor_contest             | 73.5 ms                                                     | 76.7 ms: 1.04x slower                                           |
| scimark_lu                 | 53.0 ms                                                     | 55.3 ms: 1.04x slower                                           |
| nqueens                    | 56.7 ms                                                     | 59.7 ms: 1.05x slower                                           |
| mako                       | 6.35 ms                                                     | 6.71 ms: 1.06x slower                                           |
| coverage                   | 45.6 ms                                                     | 48.4 ms: 1.06x slower                                           |
| async_generators           | 223 ms                                                      | 238 ms: 1.07x slower                                            |
| mdp                        | 1.39 sec                                                    | 1.49 sec: 1.07x slower                                          |
| scimark_sparse_mat_mult    | 2.46 ms                                                     | 2.65 ms: 1.08x slower                                           |
| chaos                      | 38.5 ms                                                     | 41.7 ms: 1.08x slower                                           |
| pyflate                    | 283 ms                                                      | 308 ms: 1.09x slower                                            |
| go                         | 87.0 ms                                                     | 94.8 ms: 1.09x slower                                           |
| pycparser                  | 683 ms                                                      | 748 ms: 1.09x slower                                            |
| scimark_fft                | 172 ms                                                      | 189 ms: 1.10x slower                                            |
| async_tree_none            | 226 ms                                                      | 266 ms: 1.18x slower                                            |
| async_tree_cpu_io_mixed    | 383 ms                                                      | 455 ms: 1.19x slower                                            |
| async_tree_memoization_tg  | 288 ms                                                      | 350 ms: 1.21x slower                                            |
| async_tree_memoization     | 276 ms                                                      | 341 ms: 1.24x slower                                            |
| async_tree_cpu_io_mixed_tg | 377 ms                                                      | 472 ms: 1.25x slower                                            |
| async_tree_none_tg         | 209 ms                                                      | 272 ms: 1.30x slower                                            |
| hexiom                     | 3.89 ms                                                     | 5.14 ms: 1.32x slower                                           |
| async_tree_io              | 521 ms                                                      | 726 ms: 1.39x slower                                            |
| scimark_monte_carlo        | 40.8 ms                                                     | 56.9 ms: 1.39x slower                                           |
| async_tree_io_tg           | 518 ms                                                      | 759 ms: 1.46x slower                                            |
| Geometric mean             | (ref)                                                       | 1.00x faster                                                    |

Benchmark hidden because not significant (5): json, bench_thread_pool, scimark_sor, sympy_sum, logging_simple
Ignored benchmarks (15) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: asyncio_websockets, bpe_tokeniser, connected_components, django_template, genshi_text, genshi_xml, gevent_hub, html5lib, k_core, pylint, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, thrift
Ignored benchmarks (10) of results/bm-20240215-3.13.0a4-9d34f60-JIT/bm-20240215-pythonperf1-amd64-python-v3.13.0a4-3.13.0a4-9d34f60.json: asyncio_tcp, asyncio_tcp_ssl, dask, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.001x slower
# HPT report

- Reliability score: 77.92% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown