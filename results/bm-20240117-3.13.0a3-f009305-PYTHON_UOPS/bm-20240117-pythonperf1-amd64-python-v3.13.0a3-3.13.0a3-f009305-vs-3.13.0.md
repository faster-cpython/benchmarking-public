# Results vs. 3.13.0

- fork: python
- ref: v3.13.0a3
- machine: windows-amd64
- commit hash: f009305
- commit date: 2024-01-17
- overall geometric mean: 1.039x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240117-pythonperf1-amd64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| 2to3           | 221 ms                                                      | 217 ms: 1.02x faster                                            |
| chameleon      | 4.82 ms                                                     | 5.10 ms: 1.06x slower                                           |
| docutils       | 1.57 sec                                                    | 1.59 sec: 1.01x slower                                          |
| tornado_http   | 93.0 ms                                                     | 88.2 ms: 1.05x faster                                           |
| Geometric mean | (ref)                                                       | 1.00x faster                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240117-pythonperf1-amd64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| coroutines                 | 12.8 ms                                                     | 12.9 ms: 1.01x slower                                           |
| async_generators           | 223 ms                                                      | 227 ms: 1.02x slower                                            |
| async_tree_cpu_io_mixed    | 383 ms                                                      | 450 ms: 1.18x slower                                            |
| async_tree_none            | 226 ms                                                      | 266 ms: 1.18x slower                                            |
| async_tree_memoization_tg  | 288 ms                                                      | 354 ms: 1.23x slower                                            |
| async_tree_memoization     | 276 ms                                                      | 341 ms: 1.24x slower                                            |
| async_tree_cpu_io_mixed_tg | 377 ms                                                      | 469 ms: 1.24x slower                                            |
| async_tree_none_tg         | 209 ms                                                      | 275 ms: 1.31x slower                                            |
| async_tree_io              | 521 ms                                                      | 722 ms: 1.39x slower                                            |
| async_tree_io_tg           | 518 ms                                                      | 748 ms: 1.44x slower                                            |
| Geometric mean             | (ref)                                                       | 1.22x slower                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240117-pythonperf1-amd64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| float          | 49.9 ms                                                     | 55.5 ms: 1.11x slower                                           |
| nbody          | 68.4 ms                                                     | 79.2 ms: 1.16x slower                                           |
| Geometric mean | (ref)                                                       | 1.09x slower                                                    |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240117-pythonperf1-amd64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_v8       | 21.4 ms                                                     | 15.5 ms: 1.38x faster                                           |
| regex_effbot   | 1.58 ms                                                     | 1.60 ms: 1.02x slower                                           |
| regex_compile  | 80.5 ms                                                     | 84.2 ms: 1.05x slower                                           |
| regex_dna      | 115 ms                                                      | 122 ms: 1.06x slower                                            |
| Geometric mean | (ref)                                                       | 1.05x faster                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240117-pythonperf1-amd64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| json_loads           | 15.1 us                                                     | 13.6 us: 1.12x faster                                           |
| json_dumps           | 5.92 ms                                                     | 5.59 ms: 1.06x faster                                           |
| pickle_pure_python   | 190 us                                                      | 182 us: 1.04x faster                                            |
| tomli_loads          | 1.39 sec                                                    | 1.38 sec: 1.01x faster                                          |
| xml_etree_process    | 37.0 ms                                                     | 37.3 ms: 1.01x slower                                           |
| xml_etree_generate   | 54.0 ms                                                     | 55.2 ms: 1.02x slower                                           |
| unpickle_pure_python | 133 us                                                      | 137 us: 1.02x slower                                            |
| xml_etree_iterparse  | 61.8 ms                                                     | 67.5 ms: 1.09x slower                                           |
| Geometric mean       | (ref)                                                       | 1.01x faster                                                    |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240117-pythonperf1-amd64-python-v3.13.0a3-3.13.0a3-f009305 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup         | 25.4 ms                                                     | 20.7 ms: 1.23x faster                                           |
| python_startup_no_site | 18.1 ms                                                     | 18.5 ms: 1.02x slower                                           |
| Geometric mean         | (ref)                                                       | 1.10x faster                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240117-pythonperf1-amd64-python-v3.13.0a3-3.13.0a3-f009305 |
|-----------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| mako      | 6.35 ms                                                     | 7.29 ms: 1.15x slower                                           |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240117-pythonperf1-amd64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| create_gc_cycles           | 1.26 ms                                                     | 738 us: 1.71x faster                                            |
| mypy2                      | 679 ms                                                      | 424 ms: 1.60x faster                                            |
| typing_runtime_protocols   | 105 us                                                      | 74.9 us: 1.41x faster                                           |
| regex_v8                   | 21.4 ms                                                     | 15.5 ms: 1.38x faster                                           |
| gc_traversal               | 1.97 ms                                                     | 1.49 ms: 1.32x faster                                           |
| bench_mp_pool              | 86.4 ms                                                     | 67.1 ms: 1.29x faster                                           |
| python_startup             | 25.4 ms                                                     | 20.7 ms: 1.23x faster                                           |
| json_loads                 | 15.1 us                                                     | 13.6 us: 1.12x faster                                           |
| json_dumps                 | 5.92 ms                                                     | 5.59 ms: 1.06x faster                                           |
| tornado_http               | 93.0 ms                                                     | 88.2 ms: 1.05x faster                                           |
| sympy_expand               | 291 ms                                                      | 279 ms: 1.04x faster                                            |
| pickle_pure_python         | 190 us                                                      | 182 us: 1.04x faster                                            |
| pathlib                    | 80.9 ms                                                     | 78.3 ms: 1.03x faster                                           |
| telco                      | 4.79 ms                                                     | 4.66 ms: 1.03x faster                                           |
| deepcopy_reduce            | 2.06 us                                                     | 2.02 us: 1.02x faster                                           |
| 2to3                       | 221 ms                                                      | 217 ms: 1.02x faster                                            |
| sympy_str                  | 169 ms                                                      | 166 ms: 1.02x faster                                            |
| richards_super             | 30.9 ms                                                     | 30.5 ms: 1.01x faster                                           |
| pycparser                  | 683 ms                                                      | 675 ms: 1.01x faster                                            |
| richards                   | 27.3 ms                                                     | 27.0 ms: 1.01x faster                                           |
| tomli_loads                | 1.39 sec                                                    | 1.38 sec: 1.01x faster                                          |
| xml_etree_process          | 37.0 ms                                                     | 37.3 ms: 1.01x slower                                           |
| sqlglot_parse              | 771 us                                                      | 778 us: 1.01x slower                                            |
| coverage                   | 45.6 ms                                                     | 46.0 ms: 1.01x slower                                           |
| logging_silent             | 54.6 ns                                                     | 55.3 ns: 1.01x slower                                           |
| docutils                   | 1.57 sec                                                    | 1.59 sec: 1.01x slower                                          |
| coroutines                 | 12.8 ms                                                     | 12.9 ms: 1.01x slower                                           |
| regex_effbot               | 1.58 ms                                                     | 1.60 ms: 1.02x slower                                           |
| deepcopy                   | 226 us                                                      | 230 us: 1.02x slower                                            |
| async_generators           | 223 ms                                                      | 227 ms: 1.02x slower                                            |
| deepcopy_memo              | 23.3 us                                                     | 23.7 us: 1.02x slower                                           |
| python_startup_no_site     | 18.1 ms                                                     | 18.5 ms: 1.02x slower                                           |
| xml_etree_generate         | 54.0 ms                                                     | 55.2 ms: 1.02x slower                                           |
| unpickle_pure_python       | 133 us                                                      | 137 us: 1.02x slower                                            |
| sqlglot_normalize          | 175 ms                                                      | 180 ms: 1.03x slower                                            |
| meteor_contest             | 73.5 ms                                                     | 76.2 ms: 1.04x slower                                           |
| fannkuch                   | 253 ms                                                      | 264 ms: 1.04x slower                                            |
| go                         | 87.0 ms                                                     | 90.8 ms: 1.04x slower                                           |
| dulwich_log                | 40.8 ms                                                     | 42.6 ms: 1.04x slower                                           |
| sqlglot_transpile          | 956 us                                                      | 1000 us: 1.05x slower                                           |
| logging_simple             | 5.96 us                                                     | 6.23 us: 1.05x slower                                           |
| regex_compile              | 80.5 ms                                                     | 84.2 ms: 1.05x slower                                           |
| sympy_integrate            | 12.5 ms                                                     | 13.1 ms: 1.05x slower                                           |
| scimark_sor                | 76.2 ms                                                     | 79.9 ms: 1.05x slower                                           |
| crypto_pyaes               | 45.4 ms                                                     | 47.7 ms: 1.05x slower                                           |
| sqlglot_optimize           | 32.9 ms                                                     | 34.6 ms: 1.05x slower                                           |
| generators                 | 19.5 ms                                                     | 20.6 ms: 1.05x slower                                           |
| regex_dna                  | 115 ms                                                      | 122 ms: 1.06x slower                                            |
| chameleon                  | 4.82 ms                                                     | 5.10 ms: 1.06x slower                                           |
| mdp                        | 1.39 sec                                                    | 1.47 sec: 1.06x slower                                          |
| pprint_safe_repr           | 494 ms                                                      | 528 ms: 1.07x slower                                            |
| logging_format             | 6.26 us                                                     | 6.70 us: 1.07x slower                                           |
| scimark_lu                 | 53.0 ms                                                     | 56.9 ms: 1.07x slower                                           |
| raytrace                   | 160 ms                                                      | 174 ms: 1.09x slower                                            |
| xml_etree_iterparse        | 61.8 ms                                                     | 67.5 ms: 1.09x slower                                           |
| pprint_pformat             | 999 ms                                                      | 1.09 sec: 1.09x slower                                          |
| json                       | 3.19 ms                                                     | 3.52 ms: 1.11x slower                                           |
| nqueens                    | 56.7 ms                                                     | 63.0 ms: 1.11x slower                                           |
| float                      | 49.9 ms                                                     | 55.5 ms: 1.11x slower                                           |
| pyflate                    | 283 ms                                                      | 323 ms: 1.14x slower                                            |
| chaos                      | 38.5 ms                                                     | 44.0 ms: 1.14x slower                                           |
| mako                       | 6.35 ms                                                     | 7.29 ms: 1.15x slower                                           |
| nbody                      | 68.4 ms                                                     | 79.2 ms: 1.16x slower                                           |
| scimark_monte_carlo        | 40.8 ms                                                     | 47.5 ms: 1.16x slower                                           |
| async_tree_cpu_io_mixed    | 383 ms                                                      | 450 ms: 1.18x slower                                            |
| scimark_fft                | 172 ms                                                      | 203 ms: 1.18x slower                                            |
| async_tree_none            | 226 ms                                                      | 266 ms: 1.18x slower                                            |
| scimark_sparse_mat_mult    | 2.46 ms                                                     | 2.95 ms: 1.20x slower                                           |
| async_tree_memoization_tg  | 288 ms                                                      | 354 ms: 1.23x slower                                            |
| comprehensions             | 10.3 us                                                     | 12.7 us: 1.24x slower                                           |
| async_tree_memoization     | 276 ms                                                      | 341 ms: 1.24x slower                                            |
| hexiom                     | 3.89 ms                                                     | 4.82 ms: 1.24x slower                                           |
| async_tree_cpu_io_mixed_tg | 377 ms                                                      | 469 ms: 1.24x slower                                            |
| spectral_norm              | 62.8 ms                                                     | 79.9 ms: 1.27x slower                                           |
| async_tree_none_tg         | 209 ms                                                      | 275 ms: 1.31x slower                                            |
| deltablue                  | 1.92 ms                                                     | 2.60 ms: 1.35x slower                                           |
| async_tree_io              | 521 ms                                                      | 722 ms: 1.39x slower                                            |
| async_tree_io_tg           | 518 ms                                                      | 748 ms: 1.44x slower                                            |
| Geometric mean             | (ref)                                                       | 1.04x slower                                                    |

Benchmark hidden because not significant (4): sympy_sum, pidigits, xml_etree_parse, bench_thread_pool
Ignored benchmarks (15) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: asyncio_websockets, bpe_tokeniser, connected_components, django_template, genshi_text, genshi_xml, gevent_hub, html5lib, k_core, pylint, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, thrift
Ignored benchmarks (10) of results/bm-20240117-3.13.0a3-f009305-PYTHON_UOPS/bm-20240117-pythonperf1-amd64-python-v3.13.0a3-3.13.0a3-f009305.json: asyncio_tcp, asyncio_tcp_ssl, dask, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.039x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.02x

# Memory
- memory change: unknown