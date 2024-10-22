# Results vs. 3.13.0

- fork: python
- ref: v3.13.0a4
- machine: windows-amd64
- commit hash: 9d34f60
- commit date: 2024-02-15
- overall geometric mean: 1.03x slower
- HPT reliability: 98.10%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240215-pythonperf1-amd64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| docutils       | 1.57 sec                                                    | 1.56 sec: 1.01x faster                                          |
| tornado_http   | 92.8 ms                                                     | 85.5 ms: 1.09x faster                                           |
| Geometric mean | (ref)                                                       | 1.02x faster                                                    |

Benchmark hidden because not significant (2): 2to3, chameleon

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240215-pythonperf1-amd64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| asyncio_tcp                | 654 ms                                                      | 477 ms: 1.37x faster                                            |
| coroutines                 | 12.5 ms                                                     | 13.2 ms: 1.05x slower                                           |
| async_generators           | 223 ms                                                      | 238 ms: 1.07x slower                                            |
| async_tree_cpu_io_mixed    | 387 ms                                                      | 455 ms: 1.17x slower                                            |
| async_tree_none            | 223 ms                                                      | 266 ms: 1.19x slower                                            |
| async_tree_memoization_tg  | 288 ms                                                      | 350 ms: 1.21x slower                                            |
| async_tree_memoization     | 271 ms                                                      | 341 ms: 1.26x slower                                            |
| async_tree_cpu_io_mixed_tg | 375 ms                                                      | 472 ms: 1.26x slower                                            |
| async_tree_none_tg         | 206 ms                                                      | 272 ms: 1.32x slower                                            |
| async_tree_io              | 521 ms                                                      | 726 ms: 1.39x slower                                            |
| async_tree_io_tg           | 512 ms                                                      | 759 ms: 1.48x slower                                            |
| Geometric mean             | (ref)                                                       | 1.17x slower                                                    |

Benchmark hidden because not significant (1): asyncio_tcp_ssl

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240215-pythonperf1-amd64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| nbody          | 64.5 ms                                                     | 61.0 ms: 1.06x faster                                           |
| pidigits       | 148 ms                                                      | 151 ms: 1.02x slower                                            |
| float          | 48.1 ms                                                     | 51.4 ms: 1.07x slower                                           |
| Geometric mean | (ref)                                                       | 1.01x slower                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240215-pythonperf1-amd64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_effbot   | 1.62 ms                                                     | 1.56 ms: 1.04x faster                                           |
| regex_v8       | 14.7 ms                                                     | 14.3 ms: 1.03x faster                                           |
| regex_compile  | 80.1 ms                                                     | 79.3 ms: 1.01x faster                                           |
| regex_dna      | 114 ms                                                      | 118 ms: 1.03x slower                                            |
| Geometric mean | (ref)                                                       | 1.01x faster                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240215-pythonperf1-amd64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| pickle_pure_python   | 183 us                                                      | 174 us: 1.06x faster                                            |
| tomli_loads          | 1.36 sec                                                    | 1.30 sec: 1.05x faster                                          |
| pickle_list          | 2.89 us                                                     | 2.78 us: 1.04x faster                                           |
| json_dumps           | 5.76 ms                                                     | 5.54 ms: 1.04x faster                                           |
| json_loads           | 14.3 us                                                     | 13.8 us: 1.04x faster                                           |
| xml_etree_generate   | 53.3 ms                                                     | 51.9 ms: 1.03x faster                                           |
| pickle_dict          | 18.0 us                                                     | 17.6 us: 1.03x faster                                           |
| unpickle             | 8.63 us                                                     | 8.41 us: 1.03x faster                                           |
| xml_etree_parse      | 93.2 ms                                                     | 91.2 ms: 1.02x faster                                           |
| xml_etree_process    | 36.5 ms                                                     | 35.9 ms: 1.02x faster                                           |
| unpickle_pure_python | 127 us                                                      | 126 us: 1.00x faster                                            |
| unpickle_list        | 2.72 us                                                     | 2.74 us: 1.00x slower                                           |
| Geometric mean       | (ref)                                                       | 1.02x faster                                                    |

Benchmark hidden because not significant (2): pickle, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240215-pythonperf1-amd64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup         | 22.2 ms                                                     | 20.5 ms: 1.08x faster                                           |
| python_startup_no_site | 17.8 ms                                                     | 18.5 ms: 1.04x slower                                           |
| Geometric mean         | (ref)                                                       | 1.02x faster                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240215-pythonperf1-amd64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|-----------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| mako      | 6.24 ms                                                     | 6.71 ms: 1.08x slower                                           |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240215-pythonperf1-amd64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| typing_runtime_protocols   | 100 us                                                      | 69.7 us: 1.44x faster                                           |
| asyncio_tcp                | 654 ms                                                      | 477 ms: 1.37x faster                                            |
| create_gc_cycles           | 829 us                                                      | 736 us: 1.13x faster                                            |
| tornado_http               | 92.8 ms                                                     | 85.5 ms: 1.09x faster                                           |
| python_startup             | 22.2 ms                                                     | 20.5 ms: 1.08x faster                                           |
| pathlib                    | 81.2 ms                                                     | 75.3 ms: 1.08x faster                                           |
| telco                      | 4.85 ms                                                     | 4.57 ms: 1.06x faster                                           |
| nbody                      | 64.5 ms                                                     | 61.0 ms: 1.06x faster                                           |
| pickle_pure_python         | 183 us                                                      | 174 us: 1.06x faster                                            |
| sqlite_synth               | 1.60 us                                                     | 1.51 us: 1.05x faster                                           |
| deepcopy_reduce            | 2.02 us                                                     | 1.92 us: 1.05x faster                                           |
| richards                   | 26.0 ms                                                     | 24.8 ms: 1.05x faster                                           |
| tomli_loads                | 1.36 sec                                                    | 1.30 sec: 1.05x faster                                          |
| bench_mp_pool              | 69.6 ms                                                     | 66.6 ms: 1.05x faster                                           |
| richards_super             | 29.3 ms                                                     | 28.2 ms: 1.04x faster                                           |
| pickle_list                | 2.89 us                                                     | 2.78 us: 1.04x faster                                           |
| json_dumps                 | 5.76 ms                                                     | 5.54 ms: 1.04x faster                                           |
| regex_effbot               | 1.62 ms                                                     | 1.56 ms: 1.04x faster                                           |
| json_loads                 | 14.3 us                                                     | 13.8 us: 1.04x faster                                           |
| gc_traversal               | 1.55 ms                                                     | 1.51 ms: 1.03x faster                                           |
| deepcopy                   | 223 us                                                      | 217 us: 1.03x faster                                            |
| sympy_expand               | 285 ms                                                      | 277 ms: 1.03x faster                                            |
| xml_etree_generate         | 53.3 ms                                                     | 51.9 ms: 1.03x faster                                           |
| pickle_dict                | 18.0 us                                                     | 17.6 us: 1.03x faster                                           |
| unpickle                   | 8.63 us                                                     | 8.41 us: 1.03x faster                                           |
| pprint_safe_repr           | 493 ms                                                      | 480 ms: 1.03x faster                                            |
| regex_v8                   | 14.7 ms                                                     | 14.3 ms: 1.03x faster                                           |
| deepcopy_memo              | 21.8 us                                                     | 21.3 us: 1.02x faster                                           |
| xml_etree_parse            | 93.2 ms                                                     | 91.2 ms: 1.02x faster                                           |
| sympy_str                  | 166 ms                                                      | 163 ms: 1.02x faster                                            |
| xml_etree_process          | 36.5 ms                                                     | 35.9 ms: 1.02x faster                                           |
| mypy2                      | 429 ms                                                      | 423 ms: 1.01x faster                                            |
| docutils                   | 1.57 sec                                                    | 1.56 sec: 1.01x faster                                          |
| pprint_pformat             | 991 ms                                                      | 980 ms: 1.01x faster                                            |
| regex_compile              | 80.1 ms                                                     | 79.3 ms: 1.01x faster                                           |
| fannkuch                   | 245 ms                                                      | 242 ms: 1.01x faster                                            |
| sqlglot_parse              | 761 us                                                      | 755 us: 1.01x faster                                            |
| unpickle_pure_python       | 127 us                                                      | 126 us: 1.00x faster                                            |
| unpickle_list              | 2.72 us                                                     | 2.74 us: 1.00x slower                                           |
| sqlglot_normalize          | 171 ms                                                      | 173 ms: 1.01x slower                                            |
| sqlglot_optimize           | 33.1 ms                                                     | 33.5 ms: 1.01x slower                                           |
| pidigits                   | 148 ms                                                      | 151 ms: 1.02x slower                                            |
| generators                 | 19.5 ms                                                     | 19.9 ms: 1.02x slower                                           |
| scimark_lu                 | 54.0 ms                                                     | 55.3 ms: 1.02x slower                                           |
| sqlglot_transpile          | 952 us                                                      | 978 us: 1.03x slower                                            |
| regex_dna                  | 114 ms                                                      | 118 ms: 1.03x slower                                            |
| coverage                   | 46.7 ms                                                     | 48.4 ms: 1.04x slower                                           |
| comprehensions             | 10.2 us                                                     | 10.6 us: 1.04x slower                                           |
| logging_format             | 6.15 us                                                     | 6.39 us: 1.04x slower                                           |
| logging_simple             | 5.72 us                                                     | 5.95 us: 1.04x slower                                           |
| python_startup_no_site     | 17.8 ms                                                     | 18.5 ms: 1.04x slower                                           |
| sympy_integrate            | 12.3 ms                                                     | 12.8 ms: 1.05x slower                                           |
| coroutines                 | 12.5 ms                                                     | 13.2 ms: 1.05x slower                                           |
| scimark_sor                | 72.0 ms                                                     | 76.0 ms: 1.06x slower                                           |
| logging_silent             | 51.0 ns                                                     | 54.0 ns: 1.06x slower                                           |
| raytrace                   | 156 ms                                                      | 166 ms: 1.06x slower                                            |
| meteor_contest             | 72.3 ms                                                     | 76.7 ms: 1.06x slower                                           |
| deltablue                  | 1.86 ms                                                     | 1.99 ms: 1.07x slower                                           |
| float                      | 48.1 ms                                                     | 51.4 ms: 1.07x slower                                           |
| async_generators           | 223 ms                                                      | 238 ms: 1.07x slower                                            |
| spectral_norm              | 59.2 ms                                                     | 63.3 ms: 1.07x slower                                           |
| crypto_pyaes               | 42.8 ms                                                     | 45.8 ms: 1.07x slower                                           |
| mdp                        | 1.38 sec                                                    | 1.49 sec: 1.07x slower                                          |
| mako                       | 6.24 ms                                                     | 6.71 ms: 1.08x slower                                           |
| nqueens                    | 55.5 ms                                                     | 59.7 ms: 1.08x slower                                           |
| scimark_fft                | 174 ms                                                      | 189 ms: 1.08x slower                                            |
| chaos                      | 37.9 ms                                                     | 41.7 ms: 1.10x slower                                           |
| pyflate                    | 275 ms                                                      | 308 ms: 1.12x slower                                            |
| go                         | 84.6 ms                                                     | 94.8 ms: 1.12x slower                                           |
| scimark_sparse_mat_mult    | 2.34 ms                                                     | 2.65 ms: 1.13x slower                                           |
| async_tree_cpu_io_mixed    | 387 ms                                                      | 455 ms: 1.17x slower                                            |
| async_tree_none            | 223 ms                                                      | 266 ms: 1.19x slower                                            |
| async_tree_memoization_tg  | 288 ms                                                      | 350 ms: 1.21x slower                                            |
| async_tree_memoization     | 271 ms                                                      | 341 ms: 1.26x slower                                            |
| async_tree_cpu_io_mixed_tg | 375 ms                                                      | 472 ms: 1.26x slower                                            |
| async_tree_none_tg         | 206 ms                                                      | 272 ms: 1.32x slower                                            |
| hexiom                     | 3.69 ms                                                     | 5.14 ms: 1.39x slower                                           |
| async_tree_io              | 521 ms                                                      | 726 ms: 1.39x slower                                            |
| scimark_monte_carlo        | 40.3 ms                                                     | 56.9 ms: 1.41x slower                                           |
| async_tree_io_tg           | 512 ms                                                      | 759 ms: 1.48x slower                                            |
| Geometric mean             | (ref)                                                       | 1.03x slower                                                    |

Benchmark hidden because not significant (11): pycparser, bench_thread_pool, pickle, unpack_sequence, 2to3, dulwich_log, sympy_sum, chameleon, xml_etree_iterparse, json, asyncio_tcp_ssl
Ignored benchmarks (8) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, django_template, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
Ignored benchmarks (1) of results/bm-20240215-3.13.0a4-9d34f60-JIT/bm-20240215-pythonperf1-amd64-python-v3.13.0a4-3.13.0a4-9d34f60.json: dask

# HPT report

- Reliability score: 98.10% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown