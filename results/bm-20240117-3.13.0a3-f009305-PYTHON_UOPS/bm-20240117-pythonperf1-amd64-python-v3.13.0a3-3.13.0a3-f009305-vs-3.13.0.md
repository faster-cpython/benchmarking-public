# Results vs. 3.13.0

- fork: python
- ref: v3.13.0a3
- machine: windows-amd64
- commit hash: f009305
- commit date: 2024-01-17
- overall geometric mean: 1.06x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240117-pythonperf1-amd64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| chameleon      | 4.72 ms                                                     | 5.10 ms: 1.08x slower                                           |
| docutils       | 1.57 sec                                                    | 1.59 sec: 1.01x slower                                          |
| tornado_http   | 92.8 ms                                                     | 88.2 ms: 1.05x faster                                           |
| Geometric mean | (ref)                                                       | 1.01x slower                                                    |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240117-pythonperf1-amd64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| asyncio_tcp                | 654 ms                                                      | 468 ms: 1.40x faster                                            |
| async_generators           | 223 ms                                                      | 227 ms: 1.02x slower                                            |
| coroutines                 | 12.5 ms                                                     | 12.9 ms: 1.03x slower                                           |
| async_tree_cpu_io_mixed    | 387 ms                                                      | 450 ms: 1.16x slower                                            |
| async_tree_none            | 223 ms                                                      | 266 ms: 1.19x slower                                            |
| async_tree_memoization_tg  | 288 ms                                                      | 354 ms: 1.23x slower                                            |
| async_tree_cpu_io_mixed_tg | 375 ms                                                      | 469 ms: 1.25x slower                                            |
| async_tree_memoization     | 271 ms                                                      | 341 ms: 1.26x slower                                            |
| async_tree_none_tg         | 206 ms                                                      | 275 ms: 1.33x slower                                            |
| async_tree_io              | 521 ms                                                      | 722 ms: 1.39x slower                                            |
| async_tree_io_tg           | 512 ms                                                      | 748 ms: 1.46x slower                                            |
| Geometric mean             | (ref)                                                       | 1.15x slower                                                    |

Benchmark hidden because not significant (1): asyncio_tcp_ssl

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240117-pythonperf1-amd64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| pidigits       | 148 ms                                                      | 148 ms: 1.01x faster                                            |
| float          | 48.1 ms                                                     | 55.5 ms: 1.15x slower                                           |
| nbody          | 64.5 ms                                                     | 79.2 ms: 1.23x slower                                           |
| Geometric mean | (ref)                                                       | 1.12x slower                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240117-pythonperf1-amd64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_effbot   | 1.62 ms                                                     | 1.60 ms: 1.01x faster                                           |
| regex_compile  | 80.1 ms                                                     | 84.2 ms: 1.05x slower                                           |
| regex_v8       | 14.7 ms                                                     | 15.5 ms: 1.06x slower                                           |
| regex_dna      | 114 ms                                                      | 122 ms: 1.06x slower                                            |
| Geometric mean | (ref)                                                       | 1.04x slower                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240117-pythonperf1-amd64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| json_loads           | 14.3 us                                                     | 13.6 us: 1.06x faster                                           |
| unpickle             | 8.63 us                                                     | 8.21 us: 1.05x faster                                           |
| json_dumps           | 5.76 ms                                                     | 5.59 ms: 1.03x faster                                           |
| pickle_pure_python   | 183 us                                                      | 182 us: 1.01x faster                                            |
| pickle               | 7.34 us                                                     | 7.37 us: 1.00x slower                                           |
| xml_etree_parse      | 93.2 ms                                                     | 94.0 ms: 1.01x slower                                           |
| tomli_loads          | 1.36 sec                                                    | 1.38 sec: 1.02x slower                                          |
| xml_etree_process    | 36.5 ms                                                     | 37.3 ms: 1.02x slower                                           |
| xml_etree_generate   | 53.3 ms                                                     | 55.2 ms: 1.04x slower                                           |
| pickle_dict          | 18.0 us                                                     | 18.8 us: 1.04x slower                                           |
| pickle_list          | 2.89 us                                                     | 3.08 us: 1.06x slower                                           |
| unpickle_pure_python | 127 us                                                      | 137 us: 1.08x slower                                            |
| xml_etree_iterparse  | 62.3 ms                                                     | 67.5 ms: 1.08x slower                                           |
| Geometric mean       | (ref)                                                       | 1.01x slower                                                    |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240117-pythonperf1-amd64-python-v3.13.0a3-3.13.0a3-f009305 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup         | 22.2 ms                                                     | 20.7 ms: 1.07x faster                                           |
| python_startup_no_site | 17.8 ms                                                     | 18.5 ms: 1.04x slower                                           |
| Geometric mean         | (ref)                                                       | 1.02x faster                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240117-pythonperf1-amd64-python-v3.13.0a3-3.13.0a3-f009305 |
|-----------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| mako      | 6.24 ms                                                     | 7.29 ms: 1.17x slower                                           |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240117-pythonperf1-amd64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| asyncio_tcp                | 654 ms                                                      | 468 ms: 1.40x faster                                            |
| typing_runtime_protocols   | 100 us                                                      | 74.9 us: 1.34x faster                                           |
| pycparser                  | 758 ms                                                      | 675 ms: 1.12x faster                                            |
| create_gc_cycles           | 829 us                                                      | 738 us: 1.12x faster                                            |
| python_startup             | 22.2 ms                                                     | 20.7 ms: 1.07x faster                                           |
| json_loads                 | 14.3 us                                                     | 13.6 us: 1.06x faster                                           |
| tornado_http               | 92.8 ms                                                     | 88.2 ms: 1.05x faster                                           |
| unpickle                   | 8.63 us                                                     | 8.21 us: 1.05x faster                                           |
| gc_traversal               | 1.55 ms                                                     | 1.49 ms: 1.04x faster                                           |
| telco                      | 4.85 ms                                                     | 4.66 ms: 1.04x faster                                           |
| bench_mp_pool              | 69.6 ms                                                     | 67.1 ms: 1.04x faster                                           |
| pathlib                    | 81.2 ms                                                     | 78.3 ms: 1.04x faster                                           |
| json_dumps                 | 5.76 ms                                                     | 5.59 ms: 1.03x faster                                           |
| unpack_sequence            | 40.0 ns                                                     | 39.1 ns: 1.02x faster                                           |
| sympy_expand               | 285 ms                                                      | 279 ms: 1.02x faster                                            |
| sqlite_synth               | 1.60 us                                                     | 1.57 us: 1.02x faster                                           |
| coverage                   | 46.7 ms                                                     | 46.0 ms: 1.02x faster                                           |
| mypy2                      | 429 ms                                                      | 424 ms: 1.01x faster                                            |
| regex_effbot               | 1.62 ms                                                     | 1.60 ms: 1.01x faster                                           |
| pickle_pure_python         | 183 us                                                      | 182 us: 1.01x faster                                            |
| pidigits                   | 148 ms                                                      | 148 ms: 1.01x faster                                            |
| pickle                     | 7.34 us                                                     | 7.37 us: 1.00x slower                                           |
| xml_etree_parse            | 93.2 ms                                                     | 94.0 ms: 1.01x slower                                           |
| docutils                   | 1.57 sec                                                    | 1.59 sec: 1.01x slower                                          |
| tomli_loads                | 1.36 sec                                                    | 1.38 sec: 1.02x slower                                          |
| async_generators           | 223 ms                                                      | 227 ms: 1.02x slower                                            |
| xml_etree_process          | 36.5 ms                                                     | 37.3 ms: 1.02x slower                                           |
| sqlglot_parse              | 761 us                                                      | 778 us: 1.02x slower                                            |
| deepcopy                   | 223 us                                                      | 230 us: 1.03x slower                                            |
| coroutines                 | 12.5 ms                                                     | 12.9 ms: 1.03x slower                                           |
| xml_etree_generate         | 53.3 ms                                                     | 55.2 ms: 1.04x slower                                           |
| richards                   | 26.0 ms                                                     | 27.0 ms: 1.04x slower                                           |
| richards_super             | 29.3 ms                                                     | 30.5 ms: 1.04x slower                                           |
| python_startup_no_site     | 17.8 ms                                                     | 18.5 ms: 1.04x slower                                           |
| pickle_dict                | 18.0 us                                                     | 18.8 us: 1.04x slower                                           |
| sqlglot_optimize           | 33.1 ms                                                     | 34.6 ms: 1.05x slower                                           |
| bench_thread_pool          | 828 us                                                      | 867 us: 1.05x slower                                            |
| regex_compile              | 80.1 ms                                                     | 84.2 ms: 1.05x slower                                           |
| sqlglot_transpile          | 952 us                                                      | 1000 us: 1.05x slower                                           |
| sqlglot_normalize          | 171 ms                                                      | 180 ms: 1.05x slower                                            |
| meteor_contest             | 72.3 ms                                                     | 76.2 ms: 1.05x slower                                           |
| scimark_lu                 | 54.0 ms                                                     | 56.9 ms: 1.05x slower                                           |
| dulwich_log                | 40.4 ms                                                     | 42.6 ms: 1.06x slower                                           |
| generators                 | 19.5 ms                                                     | 20.6 ms: 1.06x slower                                           |
| regex_v8                   | 14.7 ms                                                     | 15.5 ms: 1.06x slower                                           |
| mdp                        | 1.38 sec                                                    | 1.47 sec: 1.06x slower                                          |
| pickle_list                | 2.89 us                                                     | 3.08 us: 1.06x slower                                           |
| regex_dna                  | 114 ms                                                      | 122 ms: 1.06x slower                                            |
| sympy_integrate            | 12.3 ms                                                     | 13.1 ms: 1.07x slower                                           |
| pprint_safe_repr           | 493 ms                                                      | 528 ms: 1.07x slower                                            |
| go                         | 84.6 ms                                                     | 90.8 ms: 1.07x slower                                           |
| unpickle_pure_python       | 127 us                                                      | 137 us: 1.08x slower                                            |
| fannkuch                   | 245 ms                                                      | 264 ms: 1.08x slower                                            |
| chameleon                  | 4.72 ms                                                     | 5.10 ms: 1.08x slower                                           |
| logging_silent             | 51.0 ns                                                     | 55.3 ns: 1.08x slower                                           |
| xml_etree_iterparse        | 62.3 ms                                                     | 67.5 ms: 1.08x slower                                           |
| deepcopy_memo              | 21.8 us                                                     | 23.7 us: 1.09x slower                                           |
| logging_simple             | 5.72 us                                                     | 6.23 us: 1.09x slower                                           |
| logging_format             | 6.15 us                                                     | 6.70 us: 1.09x slower                                           |
| pprint_pformat             | 991 ms                                                      | 1.09 sec: 1.10x slower                                          |
| scimark_sor                | 72.0 ms                                                     | 79.9 ms: 1.11x slower                                           |
| crypto_pyaes               | 42.8 ms                                                     | 47.7 ms: 1.11x slower                                           |
| raytrace                   | 156 ms                                                      | 174 ms: 1.11x slower                                            |
| nqueens                    | 55.5 ms                                                     | 63.0 ms: 1.13x slower                                           |
| float                      | 48.1 ms                                                     | 55.5 ms: 1.15x slower                                           |
| chaos                      | 37.9 ms                                                     | 44.0 ms: 1.16x slower                                           |
| async_tree_cpu_io_mixed    | 387 ms                                                      | 450 ms: 1.16x slower                                            |
| scimark_fft                | 174 ms                                                      | 203 ms: 1.16x slower                                            |
| mako                       | 6.24 ms                                                     | 7.29 ms: 1.17x slower                                           |
| pyflate                    | 275 ms                                                      | 323 ms: 1.17x slower                                            |
| scimark_monte_carlo        | 40.3 ms                                                     | 47.5 ms: 1.18x slower                                           |
| json                       | 2.98 ms                                                     | 3.52 ms: 1.18x slower                                           |
| async_tree_none            | 223 ms                                                      | 266 ms: 1.19x slower                                            |
| async_tree_memoization_tg  | 288 ms                                                      | 354 ms: 1.23x slower                                            |
| nbody                      | 64.5 ms                                                     | 79.2 ms: 1.23x slower                                           |
| comprehensions             | 10.2 us                                                     | 12.7 us: 1.24x slower                                           |
| async_tree_cpu_io_mixed_tg | 375 ms                                                      | 469 ms: 1.25x slower                                            |
| async_tree_memoization     | 271 ms                                                      | 341 ms: 1.26x slower                                            |
| scimark_sparse_mat_mult    | 2.34 ms                                                     | 2.95 ms: 1.26x slower                                           |
| hexiom                     | 3.69 ms                                                     | 4.82 ms: 1.31x slower                                           |
| async_tree_none_tg         | 206 ms                                                      | 275 ms: 1.33x slower                                            |
| spectral_norm              | 59.2 ms                                                     | 79.9 ms: 1.35x slower                                           |
| async_tree_io              | 521 ms                                                      | 722 ms: 1.39x slower                                            |
| deltablue                  | 1.86 ms                                                     | 2.60 ms: 1.39x slower                                           |
| async_tree_io_tg           | 512 ms                                                      | 748 ms: 1.46x slower                                            |
| Geometric mean             | (ref)                                                       | 1.06x slower                                                    |

Benchmark hidden because not significant (6): asyncio_tcp_ssl, sympy_str, 2to3, unpickle_list, deepcopy_reduce, sympy_sum
Ignored benchmarks (8) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, django_template, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
Ignored benchmarks (1) of results/bm-20240117-3.13.0a3-f009305-PYTHON_UOPS/bm-20240117-pythonperf1-amd64-python-v3.13.0a3-3.13.0a3-f009305.json: dask

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.05x
- 95% likely to have a slowdown of 1.05x
- 99% likely to have a slowdown of 1.04x

# Memory
- memory change: unknown