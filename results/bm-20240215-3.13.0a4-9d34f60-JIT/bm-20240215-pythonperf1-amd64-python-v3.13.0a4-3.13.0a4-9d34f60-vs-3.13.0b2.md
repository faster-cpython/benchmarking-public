# Results vs. 3.13.0b2

- fork: python
- ref: v3.13.0a4
- machine: windows-amd64
- commit hash: 9d34f60
- commit date: 2024-02-15
- overall geometric mean: 1.04x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240215-pythonperf1-amd64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| 2to3           | 207 ms                                                          | 217 ms: 1.05x slower                                            |
| chameleon      | 4.80 ms                                                         | 4.74 ms: 1.01x faster                                           |
| docutils       | 1.63 sec                                                        | 1.56 sec: 1.05x faster                                          |
| tornado_http   | 81.8 ms                                                         | 85.5 ms: 1.04x slower                                           |
| Geometric mean | (ref)                                                           | 1.01x slower                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240215-pythonperf1-amd64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| async_tree_cpu_io_mixed    | 389 ms                                                          | 455 ms: 1.17x slower                                            |
| async_tree_none            | 218 ms                                                          | 266 ms: 1.22x slower                                            |
| async_tree_cpu_io_mixed_tg | 382 ms                                                          | 472 ms: 1.23x slower                                            |
| async_tree_io              | 588 ms                                                          | 726 ms: 1.24x slower                                            |
| async_tree_io_tg           | 605 ms                                                          | 759 ms: 1.25x slower                                            |
| async_tree_memoization     | 264 ms                                                          | 341 ms: 1.29x slower                                            |
| async_tree_none_tg         | 202 ms                                                          | 272 ms: 1.35x slower                                            |
| async_tree_memoization_tg  | 258 ms                                                          | 350 ms: 1.35x slower                                            |
| Geometric mean             | (ref)                                                           | 1.26x slower                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240215-pythonperf1-amd64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| nbody          | 67.6 ms                                                         | 61.0 ms: 1.11x faster                                           |
| pidigits       | 150 ms                                                          | 151 ms: 1.01x slower                                            |
| float          | 49.7 ms                                                         | 51.4 ms: 1.03x slower                                           |
| Geometric mean | (ref)                                                           | 1.02x faster                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240215-pythonperf1-amd64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_v8       | 15.8 ms                                                         | 14.3 ms: 1.10x faster                                           |
| regex_effbot   | 1.58 ms                                                         | 1.56 ms: 1.02x faster                                           |
| regex_dna      | 119 ms                                                          | 118 ms: 1.01x faster                                            |
| regex_compile  | 78.0 ms                                                         | 79.3 ms: 1.02x slower                                           |
| Geometric mean | (ref)                                                           | 1.03x faster                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240215-pythonperf1-amd64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| pickle_list          | 2.90 us                                                         | 2.78 us: 1.04x faster                                           |
| tomli_loads          | 1.35 sec                                                        | 1.30 sec: 1.04x faster                                          |
| pickle_dict          | 18.1 us                                                         | 17.6 us: 1.03x faster                                           |
| json_loads           | 14.2 us                                                         | 13.8 us: 1.03x faster                                           |
| xml_etree_generate   | 53.2 ms                                                         | 51.9 ms: 1.02x faster                                           |
| xml_etree_process    | 36.4 ms                                                         | 35.9 ms: 1.02x faster                                           |
| json_dumps           | 5.61 ms                                                         | 5.54 ms: 1.01x faster                                           |
| pickle_pure_python   | 175 us                                                          | 174 us: 1.01x faster                                            |
| xml_etree_iterparse  | 62.3 ms                                                         | 62.9 ms: 1.01x slower                                           |
| pickle               | 7.11 us                                                         | 7.32 us: 1.03x slower                                           |
| unpickle_pure_python | 122 us                                                          | 126 us: 1.04x slower                                            |
| unpickle_list        | 2.62 us                                                         | 2.74 us: 1.04x slower                                           |
| Geometric mean       | (ref)                                                           | 1.01x faster                                                    |

Benchmark hidden because not significant (2): unpickle, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240215-pythonperf1-amd64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup         | 20.3 ms                                                         | 20.5 ms: 1.01x slower                                           |
| python_startup_no_site | 16.2 ms                                                         | 18.5 ms: 1.14x slower                                           |
| Geometric mean         | (ref)                                                           | 1.07x slower                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240215-pythonperf1-amd64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|-----------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| mako      | 6.36 ms                                                         | 6.71 ms: 1.06x slower                                           |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240215-pythonperf1-amd64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| typing_runtime_protocols   | 101 us                                                          | 69.7 us: 1.45x faster                                           |
| create_gc_cycles           | 888 us                                                          | 736 us: 1.21x faster                                            |
| nbody                      | 67.6 ms                                                         | 61.0 ms: 1.11x faster                                           |
| regex_v8                   | 15.8 ms                                                         | 14.3 ms: 1.10x faster                                           |
| richards                   | 26.7 ms                                                         | 24.8 ms: 1.08x faster                                           |
| richards_super             | 30.2 ms                                                         | 28.2 ms: 1.07x faster                                           |
| sqlite_synth               | 1.60 us                                                         | 1.51 us: 1.06x faster                                           |
| docutils                   | 1.63 sec                                                        | 1.56 sec: 1.05x faster                                          |
| pickle_list                | 2.90 us                                                         | 2.78 us: 1.04x faster                                           |
| deepcopy_reduce            | 1.99 us                                                         | 1.92 us: 1.04x faster                                           |
| tomli_loads                | 1.35 sec                                                        | 1.30 sec: 1.04x faster                                          |
| deepcopy_memo              | 22.1 us                                                         | 21.3 us: 1.04x faster                                           |
| pickle_dict                | 18.1 us                                                         | 17.6 us: 1.03x faster                                           |
| gc_traversal               | 1.55 ms                                                         | 1.51 ms: 1.03x faster                                           |
| json_loads                 | 14.2 us                                                         | 13.8 us: 1.03x faster                                           |
| xml_etree_generate         | 53.2 ms                                                         | 51.9 ms: 1.02x faster                                           |
| scimark_lu                 | 56.6 ms                                                         | 55.3 ms: 1.02x faster                                           |
| telco                      | 4.67 ms                                                         | 4.57 ms: 1.02x faster                                           |
| regex_effbot               | 1.58 ms                                                         | 1.56 ms: 1.02x faster                                           |
| xml_etree_process          | 36.4 ms                                                         | 35.9 ms: 1.02x faster                                           |
| json_dumps                 | 5.61 ms                                                         | 5.54 ms: 1.01x faster                                           |
| chameleon                  | 4.80 ms                                                         | 4.74 ms: 1.01x faster                                           |
| deepcopy                   | 220 us                                                          | 217 us: 1.01x faster                                            |
| pickle_pure_python         | 175 us                                                          | 174 us: 1.01x faster                                            |
| regex_dna                  | 119 ms                                                          | 118 ms: 1.01x faster                                            |
| spectral_norm              | 63.7 ms                                                         | 63.3 ms: 1.01x faster                                           |
| pathlib                    | 75.9 ms                                                         | 75.3 ms: 1.01x faster                                           |
| fannkuch                   | 243 ms                                                          | 242 ms: 1.00x faster                                            |
| pidigits                   | 150 ms                                                          | 151 ms: 1.01x slower                                            |
| scimark_sor                | 75.3 ms                                                         | 76.0 ms: 1.01x slower                                           |
| sqlglot_parse              | 748 us                                                          | 755 us: 1.01x slower                                            |
| python_startup             | 20.3 ms                                                         | 20.5 ms: 1.01x slower                                           |
| xml_etree_iterparse        | 62.3 ms                                                         | 62.9 ms: 1.01x slower                                           |
| mypy2                      | 418 ms                                                          | 423 ms: 1.01x slower                                            |
| pprint_safe_repr           | 474 ms                                                          | 480 ms: 1.01x slower                                            |
| pprint_pformat             | 966 ms                                                          | 980 ms: 1.01x slower                                            |
| generators                 | 19.6 ms                                                         | 19.9 ms: 1.02x slower                                           |
| regex_compile              | 78.0 ms                                                         | 79.3 ms: 1.02x slower                                           |
| logging_silent             | 52.9 ns                                                         | 54.0 ns: 1.02x slower                                           |
| raytrace                   | 162 ms                                                          | 166 ms: 1.02x slower                                            |
| comprehensions             | 10.4 us                                                         | 10.6 us: 1.02x slower                                           |
| sqlglot_transpile          | 955 us                                                          | 978 us: 1.02x slower                                            |
| sympy_str                  | 159 ms                                                          | 163 ms: 1.02x slower                                            |
| sqlglot_optimize           | 32.7 ms                                                         | 33.5 ms: 1.03x slower                                           |
| sympy_expand               | 271 ms                                                          | 277 ms: 1.03x slower                                            |
| logging_format             | 6.22 us                                                         | 6.39 us: 1.03x slower                                           |
| bench_mp_pool              | 64.8 ms                                                         | 66.6 ms: 1.03x slower                                           |
| sympy_sum                  | 84.4 ms                                                         | 86.8 ms: 1.03x slower                                           |
| pickle                     | 7.11 us                                                         | 7.32 us: 1.03x slower                                           |
| logging_simple             | 5.78 us                                                         | 5.95 us: 1.03x slower                                           |
| coroutines                 | 12.8 ms                                                         | 13.2 ms: 1.03x slower                                           |
| float                      | 49.7 ms                                                         | 51.4 ms: 1.03x slower                                           |
| unpickle_pure_python       | 122 us                                                          | 126 us: 1.04x slower                                            |
| tornado_http               | 81.8 ms                                                         | 85.5 ms: 1.04x slower                                           |
| unpickle_list              | 2.62 us                                                         | 2.74 us: 1.04x slower                                           |
| 2to3                       | 207 ms                                                          | 217 ms: 1.05x slower                                            |
| sympy_integrate            | 12.2 ms                                                         | 12.8 ms: 1.05x slower                                           |
| nqueens                    | 56.7 ms                                                         | 59.7 ms: 1.05x slower                                           |
| mako                       | 6.36 ms                                                         | 6.71 ms: 1.06x slower                                           |
| deltablue                  | 1.88 ms                                                         | 1.99 ms: 1.06x slower                                           |
| scimark_sparse_mat_mult    | 2.50 ms                                                         | 2.65 ms: 1.06x slower                                           |
| dulwich_log                | 38.0 ms                                                         | 40.4 ms: 1.06x slower                                           |
| bench_thread_pool          | 768 us                                                          | 817 us: 1.06x slower                                            |
| async_generators           | 223 ms                                                          | 238 ms: 1.07x slower                                            |
| chaos                      | 38.4 ms                                                         | 41.7 ms: 1.09x slower                                           |
| meteor_contest             | 69.9 ms                                                         | 76.7 ms: 1.10x slower                                           |
| scimark_fft                | 171 ms                                                          | 189 ms: 1.11x slower                                            |
| pyflate                    | 279 ms                                                          | 308 ms: 1.11x slower                                            |
| mdp                        | 1.31 sec                                                        | 1.49 sec: 1.13x slower                                          |
| python_startup_no_site     | 16.2 ms                                                         | 18.5 ms: 1.14x slower                                           |
| coverage                   | 42.1 ms                                                         | 48.4 ms: 1.15x slower                                           |
| asyncio_tcp_ssl            | 1.48 sec                                                        | 1.70 sec: 1.15x slower                                          |
| go                         | 82.1 ms                                                         | 94.8 ms: 1.15x slower                                           |
| async_tree_cpu_io_mixed    | 389 ms                                                          | 455 ms: 1.17x slower                                            |
| async_tree_none            | 218 ms                                                          | 266 ms: 1.22x slower                                            |
| async_tree_cpu_io_mixed_tg | 382 ms                                                          | 472 ms: 1.23x slower                                            |
| async_tree_io              | 588 ms                                                          | 726 ms: 1.24x slower                                            |
| async_tree_io_tg           | 605 ms                                                          | 759 ms: 1.25x slower                                            |
| async_tree_memoization     | 264 ms                                                          | 341 ms: 1.29x slower                                            |
| async_tree_none_tg         | 202 ms                                                          | 272 ms: 1.35x slower                                            |
| async_tree_memoization_tg  | 258 ms                                                          | 350 ms: 1.35x slower                                            |
| hexiom                     | 3.72 ms                                                         | 5.14 ms: 1.38x slower                                           |
| scimark_monte_carlo        | 39.1 ms                                                         | 56.9 ms: 1.45x slower                                           |
| Geometric mean             | (ref)                                                           | 1.04x slower                                                    |

Benchmark hidden because not significant (7): json, pycparser, sqlglot_normalize, unpickle, xml_etree_parse, crypto_pyaes, asyncio_tcp
Ignored benchmarks (8) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, django_template, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
Ignored benchmarks (2) of results/bm-20240215-3.13.0a4-9d34f60-JIT/bm-20240215-pythonperf1-amd64-python-v3.13.0a4-3.13.0a4-9d34f60.json: dask, unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: unknown