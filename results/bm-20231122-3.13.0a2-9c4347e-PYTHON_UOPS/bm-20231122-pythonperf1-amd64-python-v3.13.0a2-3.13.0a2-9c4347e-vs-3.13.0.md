# Results vs. 3.13.0

- fork: python
- ref: v3.13.0a2
- machine: windows-amd64
- commit hash: 9c4347e
- commit date: 2023-11-22
- overall geometric mean: 1.050x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20231122-pythonperf1-amd64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| 2to3           | 221 ms                                                      | 218 ms: 1.02x faster                                            |
| docutils       | 1.57 sec                                                    | 1.55 sec: 1.01x faster                                          |
| tornado_http   | 93.0 ms                                                     | 89.4 ms: 1.04x faster                                           |
| Geometric mean | (ref)                                                       | 1.02x faster                                                    |

Benchmark hidden because not significant (1): chameleon

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20231122-pythonperf1-amd64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| async_generators           | 223 ms                                                      | 228 ms: 1.02x slower                                            |
| coroutines                 | 12.8 ms                                                     | 13.3 ms: 1.04x slower                                           |
| async_tree_none            | 226 ms                                                      | 267 ms: 1.18x slower                                            |
| async_tree_cpu_io_mixed    | 383 ms                                                      | 454 ms: 1.18x slower                                            |
| async_tree_memoization     | 276 ms                                                      | 346 ms: 1.25x slower                                            |
| async_tree_memoization_tg  | 288 ms                                                      | 363 ms: 1.26x slower                                            |
| async_tree_cpu_io_mixed_tg | 377 ms                                                      | 481 ms: 1.28x slower                                            |
| async_tree_none_tg         | 209 ms                                                      | 281 ms: 1.35x slower                                            |
| async_tree_io              | 521 ms                                                      | 729 ms: 1.40x slower                                            |
| async_tree_io_tg           | 518 ms                                                      | 766 ms: 1.48x slower                                            |
| Geometric mean             | (ref)                                                       | 1.24x slower                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20231122-pythonperf1-amd64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| float          | 49.9 ms                                                     | 57.1 ms: 1.14x slower                                           |
| nbody          | 68.4 ms                                                     | 81.4 ms: 1.19x slower                                           |
| Geometric mean | (ref)                                                       | 1.11x slower                                                    |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20231122-pythonperf1-amd64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_v8       | 21.4 ms                                                     | 17.9 ms: 1.20x faster                                           |
| regex_dna      | 115 ms                                                      | 120 ms: 1.04x slower                                            |
| regex_compile  | 80.5 ms                                                     | 88.1 ms: 1.09x slower                                           |
| Geometric mean | (ref)                                                       | 1.01x faster                                                    |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20231122-pythonperf1-amd64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| json_loads           | 15.1 us                                                     | 13.4 us: 1.13x faster                                           |
| pickle_pure_python   | 190 us                                                      | 175 us: 1.09x faster                                            |
| json_dumps           | 5.92 ms                                                     | 5.46 ms: 1.08x faster                                           |
| xml_etree_process    | 37.0 ms                                                     | 37.6 ms: 1.02x slower                                           |
| unpickle_pure_python | 133 us                                                      | 136 us: 1.02x slower                                            |
| xml_etree_generate   | 54.0 ms                                                     | 55.1 ms: 1.02x slower                                           |
| tomli_loads          | 1.39 sec                                                    | 1.43 sec: 1.02x slower                                          |
| xml_etree_iterparse  | 61.8 ms                                                     | 67.5 ms: 1.09x slower                                           |
| Geometric mean       | (ref)                                                       | 1.01x faster                                                    |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20231122-pythonperf1-amd64-python-v3.13.0a2-3.13.0a2-9c4347e |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup         | 25.4 ms                                                     | 20.7 ms: 1.23x faster                                           |
| python_startup_no_site | 18.1 ms                                                     | 19.6 ms: 1.08x slower                                           |
| Geometric mean         | (ref)                                                       | 1.07x faster                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20231122-pythonperf1-amd64-python-v3.13.0a2-3.13.0a2-9c4347e |
|-----------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| mako      | 6.35 ms                                                     | 7.38 ms: 1.16x slower                                           |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20231122-pythonperf1-amd64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| create_gc_cycles           | 1.26 ms                                                     | 732 us: 1.72x faster                                            |
| typing_runtime_protocols   | 105 us                                                      | 77.0 us: 1.37x faster                                           |
| bench_mp_pool              | 86.4 ms                                                     | 64.9 ms: 1.33x faster                                           |
| gc_traversal               | 1.97 ms                                                     | 1.49 ms: 1.32x faster                                           |
| python_startup             | 25.4 ms                                                     | 20.7 ms: 1.23x faster                                           |
| regex_v8                   | 21.4 ms                                                     | 17.9 ms: 1.20x faster                                           |
| json_loads                 | 15.1 us                                                     | 13.4 us: 1.13x faster                                           |
| pickle_pure_python         | 190 us                                                      | 175 us: 1.09x faster                                            |
| json_dumps                 | 5.92 ms                                                     | 5.46 ms: 1.08x faster                                           |
| deepcopy_reduce            | 2.06 us                                                     | 1.94 us: 1.06x faster                                           |
| deepcopy                   | 226 us                                                      | 216 us: 1.05x faster                                            |
| tornado_http               | 93.0 ms                                                     | 89.4 ms: 1.04x faster                                           |
| sympy_expand               | 291 ms                                                      | 281 ms: 1.04x faster                                            |
| telco                      | 4.79 ms                                                     | 4.64 ms: 1.03x faster                                           |
| pathlib                    | 80.9 ms                                                     | 78.5 ms: 1.03x faster                                           |
| richards_super             | 30.9 ms                                                     | 30.1 ms: 1.03x faster                                           |
| deepcopy_memo              | 23.3 us                                                     | 22.9 us: 1.02x faster                                           |
| 2to3                       | 221 ms                                                      | 218 ms: 1.02x faster                                            |
| docutils                   | 1.57 sec                                                    | 1.55 sec: 1.01x faster                                          |
| pycparser                  | 683 ms                                                      | 675 ms: 1.01x faster                                            |
| richards                   | 27.3 ms                                                     | 27.0 ms: 1.01x faster                                           |
| coverage                   | 45.6 ms                                                     | 45.2 ms: 1.01x faster                                           |
| sqlglot_parse              | 771 us                                                      | 779 us: 1.01x slower                                            |
| logging_silent             | 54.6 ns                                                     | 55.5 ns: 1.02x slower                                           |
| xml_etree_process          | 37.0 ms                                                     | 37.6 ms: 1.02x slower                                           |
| unpickle_pure_python       | 133 us                                                      | 136 us: 1.02x slower                                            |
| xml_etree_generate         | 54.0 ms                                                     | 55.1 ms: 1.02x slower                                           |
| tomli_loads                | 1.39 sec                                                    | 1.43 sec: 1.02x slower                                          |
| async_generators           | 223 ms                                                      | 228 ms: 1.02x slower                                            |
| sympy_sum                  | 86.9 ms                                                     | 89.1 ms: 1.02x slower                                           |
| scimark_sor                | 76.2 ms                                                     | 78.6 ms: 1.03x slower                                           |
| mdp                        | 1.39 sec                                                    | 1.44 sec: 1.03x slower                                          |
| regex_dna                  | 115 ms                                                      | 120 ms: 1.04x slower                                            |
| coroutines                 | 12.8 ms                                                     | 13.3 ms: 1.04x slower                                           |
| generators                 | 19.5 ms                                                     | 20.3 ms: 1.04x slower                                           |
| logging_simple             | 5.96 us                                                     | 6.24 us: 1.05x slower                                           |
| sqlglot_normalize          | 175 ms                                                      | 183 ms: 1.05x slower                                            |
| dulwich_log                | 40.8 ms                                                     | 42.8 ms: 1.05x slower                                           |
| pprint_safe_repr           | 494 ms                                                      | 519 ms: 1.05x slower                                            |
| sqlglot_transpile          | 956 us                                                      | 1.01 ms: 1.05x slower                                           |
| meteor_contest             | 73.5 ms                                                     | 77.5 ms: 1.05x slower                                           |
| sqlglot_optimize           | 32.9 ms                                                     | 34.8 ms: 1.06x slower                                           |
| go                         | 87.0 ms                                                     | 92.1 ms: 1.06x slower                                           |
| sympy_integrate            | 12.5 ms                                                     | 13.3 ms: 1.06x slower                                           |
| pprint_pformat             | 999 ms                                                      | 1.07 sec: 1.07x slower                                          |
| logging_format             | 6.26 us                                                     | 6.76 us: 1.08x slower                                           |
| python_startup_no_site     | 18.1 ms                                                     | 19.6 ms: 1.08x slower                                           |
| crypto_pyaes               | 45.4 ms                                                     | 49.2 ms: 1.08x slower                                           |
| scimark_lu                 | 53.0 ms                                                     | 57.6 ms: 1.09x slower                                           |
| fannkuch                   | 253 ms                                                      | 277 ms: 1.09x slower                                            |
| xml_etree_iterparse        | 61.8 ms                                                     | 67.5 ms: 1.09x slower                                           |
| regex_compile              | 80.5 ms                                                     | 88.1 ms: 1.09x slower                                           |
| raytrace                   | 160 ms                                                      | 177 ms: 1.11x slower                                            |
| pyflate                    | 283 ms                                                      | 324 ms: 1.14x slower                                            |
| float                      | 49.9 ms                                                     | 57.1 ms: 1.14x slower                                           |
| nqueens                    | 56.7 ms                                                     | 65.3 ms: 1.15x slower                                           |
| chaos                      | 38.5 ms                                                     | 44.4 ms: 1.15x slower                                           |
| mako                       | 6.35 ms                                                     | 7.38 ms: 1.16x slower                                           |
| async_tree_none            | 226 ms                                                      | 267 ms: 1.18x slower                                            |
| async_tree_cpu_io_mixed    | 383 ms                                                      | 454 ms: 1.18x slower                                            |
| nbody                      | 68.4 ms                                                     | 81.4 ms: 1.19x slower                                           |
| scimark_monte_carlo        | 40.8 ms                                                     | 49.4 ms: 1.21x slower                                           |
| scimark_fft                | 172 ms                                                      | 213 ms: 1.24x slower                                            |
| async_tree_memoization     | 276 ms                                                      | 346 ms: 1.25x slower                                            |
| comprehensions             | 10.3 us                                                     | 12.9 us: 1.26x slower                                           |
| async_tree_memoization_tg  | 288 ms                                                      | 363 ms: 1.26x slower                                            |
| scimark_sparse_mat_mult    | 2.46 ms                                                     | 3.09 ms: 1.26x slower                                           |
| async_tree_cpu_io_mixed_tg | 377 ms                                                      | 481 ms: 1.28x slower                                            |
| hexiom                     | 3.89 ms                                                     | 5.03 ms: 1.29x slower                                           |
| spectral_norm              | 62.8 ms                                                     | 84.1 ms: 1.34x slower                                           |
| async_tree_none_tg         | 209 ms                                                      | 281 ms: 1.35x slower                                            |
| async_tree_io              | 521 ms                                                      | 729 ms: 1.40x slower                                            |
| deltablue                  | 1.92 ms                                                     | 2.72 ms: 1.42x slower                                           |
| async_tree_io_tg           | 518 ms                                                      | 766 ms: 1.48x slower                                            |
| Geometric mean             | (ref)                                                       | 1.05x slower                                                    |

Benchmark hidden because not significant (8): mypy2, json, xml_etree_parse, sympy_str, pidigits, regex_effbot, chameleon, bench_thread_pool
Ignored benchmarks (15) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: asyncio_websockets, bpe_tokeniser, connected_components, django_template, genshi_text, genshi_xml, gevent_hub, html5lib, k_core, pylint, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, thrift
Ignored benchmarks (10) of results/bm-20231122-3.13.0a2-9c4347e-PYTHON_UOPS/bm-20231122-pythonperf1-amd64-python-v3.13.0a2-3.13.0a2-9c4347e.json: asyncio_tcp, asyncio_tcp_ssl, dask, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.050x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.04x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.02x

# Memory
- memory change: unknown