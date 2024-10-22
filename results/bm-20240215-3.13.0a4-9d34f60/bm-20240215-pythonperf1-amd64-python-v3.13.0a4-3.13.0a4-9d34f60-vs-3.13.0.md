# Results vs. 3.13.0

- fork: python
- ref: v3.13.0a4
- machine: windows-amd64
- commit hash: 9d34f60
- commit date: 2024-02-15
- overall geometric mean: 1.02x slower
- HPT reliability: 99.90%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240215-pythonperf1-amd64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| 2to3           | 217 ms                                                      | 214 ms: 1.01x faster                                            |
| chameleon      | 4.72 ms                                                     | 5.01 ms: 1.06x slower                                           |
| docutils       | 1.57 sec                                                    | 1.55 sec: 1.02x faster                                          |
| html5lib       | 38.6 ms                                                     | 36.9 ms: 1.05x faster                                           |
| tornado_http   | 92.8 ms                                                     | 84.3 ms: 1.10x faster                                           |
| Geometric mean | (ref)                                                       | 1.02x faster                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240215-pythonperf1-amd64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| asyncio_tcp                | 654 ms                                                      | 481 ms: 1.36x faster                                            |
| async_generators           | 223 ms                                                      | 230 ms: 1.03x slower                                            |
| coroutines                 | 12.5 ms                                                     | 13.2 ms: 1.06x slower                                           |
| asyncio_tcp_ssl            | 1.64 sec                                                    | 1.77 sec: 1.08x slower                                          |
| async_tree_cpu_io_mixed    | 387 ms                                                      | 453 ms: 1.17x slower                                            |
| async_tree_none            | 223 ms                                                      | 266 ms: 1.19x slower                                            |
| async_tree_memoization_tg  | 288 ms                                                      | 349 ms: 1.21x slower                                            |
| async_tree_memoization     | 271 ms                                                      | 340 ms: 1.25x slower                                            |
| async_tree_cpu_io_mixed_tg | 375 ms                                                      | 472 ms: 1.26x slower                                            |
| async_tree_none_tg         | 206 ms                                                      | 274 ms: 1.33x slower                                            |
| async_tree_io              | 521 ms                                                      | 732 ms: 1.41x slower                                            |
| async_tree_io_tg           | 512 ms                                                      | 758 ms: 1.48x slower                                            |
| Geometric mean             | (ref)                                                       | 1.17x slower                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240215-pythonperf1-amd64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| pidigits       | 148 ms                                                      | 148 ms: 1.01x faster                                            |
| float          | 48.1 ms                                                     | 51.0 ms: 1.06x slower                                           |
| nbody          | 64.5 ms                                                     | 73.2 ms: 1.14x slower                                           |
| Geometric mean | (ref)                                                       | 1.06x slower                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240215-pythonperf1-amd64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_effbot   | 1.62 ms                                                     | 1.56 ms: 1.03x faster                                           |
| regex_compile  | 80.1 ms                                                     | 77.8 ms: 1.03x faster                                           |
| regex_v8       | 14.7 ms                                                     | 14.4 ms: 1.02x faster                                           |
| Geometric mean | (ref)                                                       | 1.02x faster                                                    |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240215-pythonperf1-amd64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| json_loads           | 14.3 us                                                     | 13.7 us: 1.05x faster                                           |
| json_dumps           | 5.76 ms                                                     | 5.58 ms: 1.03x faster                                           |
| unpickle_list        | 2.72 us                                                     | 2.68 us: 1.02x faster                                           |
| xml_etree_parse      | 93.2 ms                                                     | 92.2 ms: 1.01x faster                                           |
| pickle_pure_python   | 183 us                                                      | 186 us: 1.01x slower                                            |
| xml_etree_process    | 36.5 ms                                                     | 37.1 ms: 1.02x slower                                           |
| pickle_dict          | 18.0 us                                                     | 18.4 us: 1.02x slower                                           |
| unpickle_pure_python | 127 us                                                      | 129 us: 1.02x slower                                            |
| xml_etree_generate   | 53.3 ms                                                     | 54.5 ms: 1.02x slower                                           |
| xml_etree_iterparse  | 62.3 ms                                                     | 65.1 ms: 1.05x slower                                           |
| tomli_loads          | 1.36 sec                                                    | 1.43 sec: 1.05x slower                                          |
| Geometric mean       | (ref)                                                       | 1.01x slower                                                    |

Benchmark hidden because not significant (3): pickle, unpickle, pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240215-pythonperf1-amd64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup | 22.2 ms                                                     | 20.2 ms: 1.10x faster                                           |
| Geometric mean | (ref)                                                       | 1.05x faster                                                    |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240215-pythonperf1-amd64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| django_template | 21.8 ms                                                     | 22.5 ms: 1.03x slower                                           |
| genshi_xml      | 32.8 ms                                                     | 35.1 ms: 1.07x slower                                           |
| genshi_text     | 14.9 ms                                                     | 16.0 ms: 1.08x slower                                           |
| Geometric mean  | (ref)                                                       | 1.05x slower                                                    |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240215-pythonperf1-amd64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| typing_runtime_protocols   | 100 us                                                      | 71.0 us: 1.42x faster                                           |
| asyncio_tcp                | 654 ms                                                      | 481 ms: 1.36x faster                                            |
| create_gc_cycles           | 829 us                                                      | 743 us: 1.11x faster                                            |
| tornado_http               | 92.8 ms                                                     | 84.3 ms: 1.10x faster                                           |
| python_startup             | 22.2 ms                                                     | 20.2 ms: 1.10x faster                                           |
| thrift                     | 8.68 ms                                                     | 8.18 ms: 1.06x faster                                           |
| aiohttp                    | 932 us                                                      | 885 us: 1.05x faster                                            |
| bench_mp_pool              | 69.6 ms                                                     | 66.4 ms: 1.05x faster                                           |
| html5lib                   | 38.6 ms                                                     | 36.9 ms: 1.05x faster                                           |
| json_loads                 | 14.3 us                                                     | 13.7 us: 1.05x faster                                           |
| sqlite_synth               | 1.60 us                                                     | 1.53 us: 1.04x faster                                           |
| sympy_expand               | 285 ms                                                      | 274 ms: 1.04x faster                                            |
| sympy_str                  | 166 ms                                                      | 160 ms: 1.04x faster                                            |
| gc_traversal               | 1.55 ms                                                     | 1.50 ms: 1.04x faster                                           |
| sympy_sum                  | 86.4 ms                                                     | 83.5 ms: 1.03x faster                                           |
| mdp                        | 1.38 sec                                                    | 1.34 sec: 1.03x faster                                          |
| json_dumps                 | 5.76 ms                                                     | 5.58 ms: 1.03x faster                                           |
| regex_effbot               | 1.62 ms                                                     | 1.56 ms: 1.03x faster                                           |
| mypy2                      | 429 ms                                                      | 416 ms: 1.03x faster                                            |
| regex_compile              | 80.1 ms                                                     | 77.8 ms: 1.03x faster                                           |
| json                       | 2.98 ms                                                     | 2.91 ms: 1.03x faster                                           |
| telco                      | 4.85 ms                                                     | 4.73 ms: 1.02x faster                                           |
| docutils                   | 1.57 sec                                                    | 1.55 sec: 1.02x faster                                          |
| regex_v8                   | 14.7 ms                                                     | 14.4 ms: 1.02x faster                                           |
| unpickle_list              | 2.72 us                                                     | 2.68 us: 1.02x faster                                           |
| 2to3                       | 217 ms                                                      | 214 ms: 1.01x faster                                            |
| xml_etree_parse            | 93.2 ms                                                     | 92.2 ms: 1.01x faster                                           |
| pidigits                   | 148 ms                                                      | 148 ms: 1.01x faster                                            |
| flaskblogging              | 2.04 sec                                                    | 2.03 sec: 1.01x faster                                          |
| sqlglot_parse              | 761 us                                                      | 768 us: 1.01x slower                                            |
| sympy_integrate            | 12.3 ms                                                     | 12.4 ms: 1.01x slower                                           |
| sqlglot_optimize           | 33.1 ms                                                     | 33.4 ms: 1.01x slower                                           |
| scimark_monte_carlo        | 40.3 ms                                                     | 40.7 ms: 1.01x slower                                           |
| coverage                   | 46.7 ms                                                     | 47.3 ms: 1.01x slower                                           |
| pickle_pure_python         | 183 us                                                      | 186 us: 1.01x slower                                            |
| deepcopy_reduce            | 2.02 us                                                     | 2.05 us: 1.01x slower                                           |
| pprint_safe_repr           | 493 ms                                                      | 500 ms: 1.02x slower                                            |
| xml_etree_process          | 36.5 ms                                                     | 37.1 ms: 1.02x slower                                           |
| pickle_dict                | 18.0 us                                                     | 18.4 us: 1.02x slower                                           |
| unpickle_pure_python       | 127 us                                                      | 129 us: 1.02x slower                                            |
| scimark_lu                 | 54.0 ms                                                     | 55.0 ms: 1.02x slower                                           |
| fannkuch                   | 245 ms                                                      | 250 ms: 1.02x slower                                            |
| xml_etree_generate         | 53.3 ms                                                     | 54.5 ms: 1.02x slower                                           |
| dulwich_log                | 40.4 ms                                                     | 41.3 ms: 1.02x slower                                           |
| sqlglot_normalize          | 171 ms                                                      | 176 ms: 1.03x slower                                            |
| scimark_fft                | 174 ms                                                      | 179 ms: 1.03x slower                                            |
| pprint_pformat             | 991 ms                                                      | 1.02 sec: 1.03x slower                                          |
| async_generators           | 223 ms                                                      | 230 ms: 1.03x slower                                            |
| django_template            | 21.8 ms                                                     | 22.5 ms: 1.03x slower                                           |
| sqlglot_transpile          | 952 us                                                      | 983 us: 1.03x slower                                            |
| hexiom                     | 3.69 ms                                                     | 3.82 ms: 1.03x slower                                           |
| pyflate                    | 275 ms                                                      | 285 ms: 1.04x slower                                            |
| chaos                      | 37.9 ms                                                     | 39.5 ms: 1.04x slower                                           |
| deepcopy                   | 223 us                                                      | 233 us: 1.04x slower                                            |
| xml_etree_iterparse        | 62.3 ms                                                     | 65.1 ms: 1.05x slower                                           |
| nqueens                    | 55.5 ms                                                     | 58.2 ms: 1.05x slower                                           |
| tomli_loads                | 1.36 sec                                                    | 1.43 sec: 1.05x slower                                          |
| comprehensions             | 10.2 us                                                     | 10.8 us: 1.05x slower                                           |
| deepcopy_memo              | 21.8 us                                                     | 23.0 us: 1.05x slower                                           |
| raytrace                   | 156 ms                                                      | 165 ms: 1.05x slower                                            |
| coroutines                 | 12.5 ms                                                     | 13.2 ms: 1.06x slower                                           |
| float                      | 48.1 ms                                                     | 51.0 ms: 1.06x slower                                           |
| chameleon                  | 4.72 ms                                                     | 5.01 ms: 1.06x slower                                           |
| deltablue                  | 1.86 ms                                                     | 1.98 ms: 1.06x slower                                           |
| scimark_sparse_mat_mult    | 2.34 ms                                                     | 2.49 ms: 1.07x slower                                           |
| generators                 | 19.5 ms                                                     | 20.8 ms: 1.07x slower                                           |
| logging_format             | 6.15 us                                                     | 6.57 us: 1.07x slower                                           |
| genshi_xml                 | 32.8 ms                                                     | 35.1 ms: 1.07x slower                                           |
| logging_simple             | 5.72 us                                                     | 6.15 us: 1.07x slower                                           |
| richards                   | 26.0 ms                                                     | 28.0 ms: 1.08x slower                                           |
| genshi_text                | 14.9 ms                                                     | 16.0 ms: 1.08x slower                                           |
| richards_super             | 29.3 ms                                                     | 31.6 ms: 1.08x slower                                           |
| asyncio_tcp_ssl            | 1.64 sec                                                    | 1.77 sec: 1.08x slower                                          |
| scimark_sor                | 72.0 ms                                                     | 77.9 ms: 1.08x slower                                           |
| logging_silent             | 51.0 ns                                                     | 57.3 ns: 1.12x slower                                           |
| nbody                      | 64.5 ms                                                     | 73.2 ms: 1.14x slower                                           |
| async_tree_cpu_io_mixed    | 387 ms                                                      | 453 ms: 1.17x slower                                            |
| async_tree_none            | 223 ms                                                      | 266 ms: 1.19x slower                                            |
| async_tree_memoization_tg  | 288 ms                                                      | 349 ms: 1.21x slower                                            |
| async_tree_memoization     | 271 ms                                                      | 340 ms: 1.25x slower                                            |
| async_tree_cpu_io_mixed_tg | 375 ms                                                      | 472 ms: 1.26x slower                                            |
| async_tree_none_tg         | 206 ms                                                      | 274 ms: 1.33x slower                                            |
| async_tree_io              | 521 ms                                                      | 732 ms: 1.41x slower                                            |
| async_tree_io_tg           | 512 ms                                                      | 758 ms: 1.48x slower                                            |
| Geometric mean             | (ref)                                                       | 1.02x slower                                                    |

Benchmark hidden because not significant (14): pylint, pycparser, pathlib, bench_thread_pool, spectral_norm, pickle, go, crypto_pyaes, meteor_contest, python_startup_no_site, unpickle, regex_dna, mako, pickle_list
Ignored benchmarks (1) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: unpack_sequence

# HPT report

- Reliability score: 99.90% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown