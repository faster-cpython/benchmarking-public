# Results vs. 3.13.0b2

- fork: python
- ref: v3.13.0a2
- machine: windows-amd64
- commit hash: 9c4347e
- commit date: 2023-11-22
- overall geometric mean: 1.09x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231122-pythonperf1-amd64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| 2to3           | 207 ms                                                          | 218 ms: 1.05x slower                                            |
| chameleon      | 4.80 ms                                                         | 4.84 ms: 1.01x slower                                           |
| docutils       | 1.63 sec                                                        | 1.55 sec: 1.05x faster                                          |
| tornado_http   | 81.8 ms                                                         | 89.4 ms: 1.09x slower                                           |
| Geometric mean | (ref)                                                           | 1.02x slower                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231122-pythonperf1-amd64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| async_tree_cpu_io_mixed    | 389 ms                                                          | 454 ms: 1.17x slower                                            |
| async_tree_none            | 218 ms                                                          | 267 ms: 1.23x slower                                            |
| async_tree_io              | 588 ms                                                          | 729 ms: 1.24x slower                                            |
| async_tree_cpu_io_mixed_tg | 382 ms                                                          | 481 ms: 1.26x slower                                            |
| async_tree_io_tg           | 605 ms                                                          | 766 ms: 1.27x slower                                            |
| async_tree_memoization     | 264 ms                                                          | 346 ms: 1.31x slower                                            |
| async_tree_none_tg         | 202 ms                                                          | 281 ms: 1.39x slower                                            |
| async_tree_memoization_tg  | 258 ms                                                          | 363 ms: 1.41x slower                                            |
| Geometric mean             | (ref)                                                           | 1.28x slower                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231122-pythonperf1-amd64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| pidigits       | 150 ms                                                          | 148 ms: 1.01x faster                                            |
| float          | 49.7 ms                                                         | 57.1 ms: 1.15x slower                                           |
| nbody          | 67.6 ms                                                         | 81.4 ms: 1.20x slower                                           |
| Geometric mean | (ref)                                                           | 1.11x slower                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231122-pythonperf1-amd64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_effbot   | 1.58 ms                                                         | 1.58 ms: 1.00x faster                                           |
| regex_dna      | 119 ms                                                          | 120 ms: 1.01x slower                                            |
| regex_compile  | 78.0 ms                                                         | 88.1 ms: 1.13x slower                                           |
| regex_v8       | 15.8 ms                                                         | 17.9 ms: 1.13x slower                                           |
| Geometric mean | (ref)                                                           | 1.06x slower                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231122-pythonperf1-amd64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| json_loads           | 14.2 us                                                         | 13.4 us: 1.06x faster                                           |
| unpickle             | 8.40 us                                                         | 8.09 us: 1.04x faster                                           |
| json_dumps           | 5.61 ms                                                         | 5.46 ms: 1.03x faster                                           |
| pickle               | 7.11 us                                                         | 6.96 us: 1.02x faster                                           |
| pickle_pure_python   | 175 us                                                          | 175 us: 1.00x faster                                            |
| xml_etree_parse      | 90.9 ms                                                         | 93.0 ms: 1.02x slower                                           |
| pickle_dict          | 18.1 us                                                         | 18.6 us: 1.03x slower                                           |
| xml_etree_process    | 36.4 ms                                                         | 37.6 ms: 1.03x slower                                           |
| xml_etree_generate   | 53.2 ms                                                         | 55.1 ms: 1.04x slower                                           |
| tomli_loads          | 1.35 sec                                                        | 1.43 sec: 1.06x slower                                          |
| xml_etree_iterparse  | 62.3 ms                                                         | 67.5 ms: 1.08x slower                                           |
| unpickle_pure_python | 122 us                                                          | 136 us: 1.12x slower                                            |
| pickle_list          | 2.90 us                                                         | 3.32 us: 1.14x slower                                           |
| Geometric mean       | (ref)                                                           | 1.03x slower                                                    |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231122-pythonperf1-amd64-python-v3.13.0a2-3.13.0a2-9c4347e |
|------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup         | 20.3 ms                                                         | 20.7 ms: 1.02x slower                                           |
| python_startup_no_site | 16.2 ms                                                         | 19.6 ms: 1.21x slower                                           |
| Geometric mean         | (ref)                                                           | 1.11x slower                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231122-pythonperf1-amd64-python-v3.13.0a2-3.13.0a2-9c4347e |
|-----------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| mako      | 6.36 ms                                                         | 7.38 ms: 1.16x slower                                           |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231122-pythonperf1-amd64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| typing_runtime_protocols   | 101 us                                                          | 77.0 us: 1.31x faster                                           |
| create_gc_cycles           | 888 us                                                          | 732 us: 1.21x faster                                            |
| pycparser                  | 754 ms                                                          | 675 ms: 1.12x faster                                            |
| json_loads                 | 14.2 us                                                         | 13.4 us: 1.06x faster                                           |
| docutils                   | 1.63 sec                                                        | 1.55 sec: 1.05x faster                                          |
| gc_traversal               | 1.55 ms                                                         | 1.49 ms: 1.04x faster                                           |
| unpickle                   | 8.40 us                                                         | 8.09 us: 1.04x faster                                           |
| json_dumps                 | 5.61 ms                                                         | 5.46 ms: 1.03x faster                                           |
| deepcopy_reduce            | 1.99 us                                                         | 1.94 us: 1.03x faster                                           |
| pickle                     | 7.11 us                                                         | 6.96 us: 1.02x faster                                           |
| sqlite_synth               | 1.60 us                                                         | 1.57 us: 1.02x faster                                           |
| deepcopy                   | 220 us                                                          | 216 us: 1.02x faster                                            |
| pidigits                   | 150 ms                                                          | 148 ms: 1.01x faster                                            |
| telco                      | 4.67 ms                                                         | 4.64 ms: 1.01x faster                                           |
| pickle_pure_python         | 175 us                                                          | 175 us: 1.00x faster                                            |
| regex_effbot               | 1.58 ms                                                         | 1.58 ms: 1.00x faster                                           |
| chameleon                  | 4.80 ms                                                         | 4.84 ms: 1.01x slower                                           |
| regex_dna                  | 119 ms                                                          | 120 ms: 1.01x slower                                            |
| richards                   | 26.7 ms                                                         | 27.0 ms: 1.01x slower                                           |
| scimark_lu                 | 56.6 ms                                                         | 57.6 ms: 1.02x slower                                           |
| python_startup             | 20.3 ms                                                         | 20.7 ms: 1.02x slower                                           |
| xml_etree_parse            | 90.9 ms                                                         | 93.0 ms: 1.02x slower                                           |
| async_generators           | 223 ms                                                          | 228 ms: 1.02x slower                                            |
| pickle_dict                | 18.1 us                                                         | 18.6 us: 1.03x slower                                           |
| xml_etree_process          | 36.4 ms                                                         | 37.6 ms: 1.03x slower                                           |
| deepcopy_memo              | 22.1 us                                                         | 22.9 us: 1.03x slower                                           |
| pathlib                    | 75.9 ms                                                         | 78.5 ms: 1.04x slower                                           |
| xml_etree_generate         | 53.2 ms                                                         | 55.1 ms: 1.04x slower                                           |
| generators                 | 19.6 ms                                                         | 20.3 ms: 1.04x slower                                           |
| sympy_expand               | 271 ms                                                          | 281 ms: 1.04x slower                                            |
| sqlglot_parse              | 748 us                                                          | 779 us: 1.04x slower                                            |
| coroutines                 | 12.8 ms                                                         | 13.3 ms: 1.04x slower                                           |
| scimark_sor                | 75.3 ms                                                         | 78.6 ms: 1.04x slower                                           |
| logging_silent             | 52.9 ns                                                         | 55.5 ns: 1.05x slower                                           |
| 2to3                       | 207 ms                                                          | 218 ms: 1.05x slower                                            |
| sqlglot_transpile          | 955 us                                                          | 1.01 ms: 1.06x slower                                           |
| tomli_loads                | 1.35 sec                                                        | 1.43 sec: 1.06x slower                                          |
| sympy_sum                  | 84.4 ms                                                         | 89.1 ms: 1.06x slower                                           |
| sqlglot_normalize          | 173 ms                                                          | 183 ms: 1.06x slower                                            |
| sympy_str                  | 159 ms                                                          | 168 ms: 1.06x slower                                            |
| sqlglot_optimize           | 32.7 ms                                                         | 34.8 ms: 1.06x slower                                           |
| coverage                   | 42.1 ms                                                         | 45.2 ms: 1.07x slower                                           |
| logging_simple             | 5.78 us                                                         | 6.24 us: 1.08x slower                                           |
| crypto_pyaes               | 45.5 ms                                                         | 49.2 ms: 1.08x slower                                           |
| xml_etree_iterparse        | 62.3 ms                                                         | 67.5 ms: 1.08x slower                                           |
| sympy_integrate            | 12.2 ms                                                         | 13.3 ms: 1.08x slower                                           |
| logging_format             | 6.22 us                                                         | 6.76 us: 1.09x slower                                           |
| tornado_http               | 81.8 ms                                                         | 89.4 ms: 1.09x slower                                           |
| mdp                        | 1.31 sec                                                        | 1.44 sec: 1.09x slower                                          |
| raytrace                   | 162 ms                                                          | 177 ms: 1.09x slower                                            |
| pprint_safe_repr           | 474 ms                                                          | 519 ms: 1.10x slower                                            |
| meteor_contest             | 69.9 ms                                                         | 77.5 ms: 1.11x slower                                           |
| pprint_pformat             | 966 ms                                                          | 1.07 sec: 1.11x slower                                          |
| bench_thread_pool          | 768 us                                                          | 858 us: 1.12x slower                                            |
| unpickle_pure_python       | 122 us                                                          | 136 us: 1.12x slower                                            |
| go                         | 82.1 ms                                                         | 92.1 ms: 1.12x slower                                           |
| asyncio_tcp_ssl            | 1.48 sec                                                        | 1.66 sec: 1.12x slower                                          |
| dulwich_log                | 38.0 ms                                                         | 42.8 ms: 1.13x slower                                           |
| regex_compile              | 78.0 ms                                                         | 88.1 ms: 1.13x slower                                           |
| regex_v8                   | 15.8 ms                                                         | 17.9 ms: 1.13x slower                                           |
| fannkuch                   | 243 ms                                                          | 277 ms: 1.14x slower                                            |
| pickle_list                | 2.90 us                                                         | 3.32 us: 1.14x slower                                           |
| float                      | 49.7 ms                                                         | 57.1 ms: 1.15x slower                                           |
| nqueens                    | 56.7 ms                                                         | 65.3 ms: 1.15x slower                                           |
| chaos                      | 38.4 ms                                                         | 44.4 ms: 1.16x slower                                           |
| pyflate                    | 279 ms                                                          | 324 ms: 1.16x slower                                            |
| mako                       | 6.36 ms                                                         | 7.38 ms: 1.16x slower                                           |
| async_tree_cpu_io_mixed    | 389 ms                                                          | 454 ms: 1.17x slower                                            |
| nbody                      | 67.6 ms                                                         | 81.4 ms: 1.20x slower                                           |
| python_startup_no_site     | 16.2 ms                                                         | 19.6 ms: 1.21x slower                                           |
| async_tree_none            | 218 ms                                                          | 267 ms: 1.23x slower                                            |
| scimark_sparse_mat_mult    | 2.50 ms                                                         | 3.09 ms: 1.24x slower                                           |
| async_tree_io              | 588 ms                                                          | 729 ms: 1.24x slower                                            |
| comprehensions             | 10.4 us                                                         | 12.9 us: 1.24x slower                                           |
| scimark_fft                | 171 ms                                                          | 213 ms: 1.25x slower                                            |
| async_tree_cpu_io_mixed_tg | 382 ms                                                          | 481 ms: 1.26x slower                                            |
| scimark_monte_carlo        | 39.1 ms                                                         | 49.4 ms: 1.26x slower                                           |
| async_tree_io_tg           | 605 ms                                                          | 766 ms: 1.27x slower                                            |
| async_tree_memoization     | 264 ms                                                          | 346 ms: 1.31x slower                                            |
| spectral_norm              | 63.7 ms                                                         | 84.1 ms: 1.32x slower                                           |
| hexiom                     | 3.72 ms                                                         | 5.03 ms: 1.35x slower                                           |
| async_tree_none_tg         | 202 ms                                                          | 281 ms: 1.39x slower                                            |
| async_tree_memoization_tg  | 258 ms                                                          | 363 ms: 1.41x slower                                            |
| mypy2                      | 418 ms                                                          | 589 ms: 1.41x slower                                            |
| deltablue                  | 1.88 ms                                                         | 2.72 ms: 1.44x slower                                           |
| Geometric mean             | (ref)                                                           | 1.09x slower                                                    |

Benchmark hidden because not significant (5): json, richards_super, unpickle_list, bench_mp_pool, asyncio_tcp
Ignored benchmarks (8) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, django_template, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
Ignored benchmarks (2) of results/bm-20231122-3.13.0a2-9c4347e-PYTHON_UOPS/bm-20231122-pythonperf1-amd64-python-v3.13.0a2-3.13.0a2-9c4347e.json: dask, unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.06x
- 95% likely to have a slowdown of 1.05x
- 99% likely to have a slowdown of 1.05x

# Memory
- memory change: unknown