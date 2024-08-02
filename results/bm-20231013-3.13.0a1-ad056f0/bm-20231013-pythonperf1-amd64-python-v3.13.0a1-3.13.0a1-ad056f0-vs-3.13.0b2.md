# Results vs. 3.13.0b2

- fork: python
- ref: v3.13.0a1
- machine: windows-amd64
- commit hash: ad056f0
- commit date: 2023-10-13
- overall geometric mean: 1.07x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231013-pythonperf1-amd64-python-v3.13.0a1-3.13.0a1-ad056f0 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| 2to3           | 207 ms                                                          | 216 ms: 1.04x slower                                            |
| chameleon      | 4.80 ms                                                         | 4.98 ms: 1.04x slower                                           |
| docutils       | 1.63 sec                                                        | 1.61 sec: 1.01x faster                                          |
| tornado_http   | 81.8 ms                                                         | 89.1 ms: 1.09x slower                                           |
| Geometric mean | (ref)                                                           | 1.04x slower                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231013-pythonperf1-amd64-python-v3.13.0a1-3.13.0a1-ad056f0 |
|----------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| async_tree_cpu_io_mixed    | 389 ms                                                          | 455 ms: 1.17x slower                                            |
| async_tree_none            | 218 ms                                                          | 267 ms: 1.22x slower                                            |
| async_tree_io              | 588 ms                                                          | 723 ms: 1.23x slower                                            |
| async_tree_cpu_io_mixed_tg | 382 ms                                                          | 486 ms: 1.27x slower                                            |
| async_tree_io_tg           | 605 ms                                                          | 772 ms: 1.27x slower                                            |
| async_tree_memoization     | 264 ms                                                          | 340 ms: 1.29x slower                                            |
| async_tree_memoization_tg  | 258 ms                                                          | 359 ms: 1.39x slower                                            |
| async_tree_none_tg         | 202 ms                                                          | 285 ms: 1.41x slower                                            |
| Geometric mean             | (ref)                                                           | 1.28x slower                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231013-pythonperf1-amd64-python-v3.13.0a1-3.13.0a1-ad056f0 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| nbody          | 67.6 ms                                                         | 72.2 ms: 1.07x slower                                           |
| float          | 49.7 ms                                                         | 53.6 ms: 1.08x slower                                           |
| Geometric mean | (ref)                                                           | 1.05x slower                                                    |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231013-pythonperf1-amd64-python-v3.13.0a1-3.13.0a1-ad056f0 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_effbot   | 1.58 ms                                                         | 1.60 ms: 1.01x slower                                           |
| regex_compile  | 78.0 ms                                                         | 90.8 ms: 1.16x slower                                           |
| Geometric mean | (ref)                                                           | 1.03x slower                                                    |

Benchmark hidden because not significant (2): regex_v8, regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231013-pythonperf1-amd64-python-v3.13.0a1-3.13.0a1-ad056f0 |
|----------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| json_loads           | 14.2 us                                                         | 13.5 us: 1.05x faster                                           |
| unpickle             | 8.40 us                                                         | 8.12 us: 1.03x faster                                           |
| pickle               | 7.11 us                                                         | 6.98 us: 1.02x faster                                           |
| xml_etree_parse      | 90.9 ms                                                         | 91.6 ms: 1.01x slower                                           |
| pickle_dict          | 18.1 us                                                         | 18.4 us: 1.01x slower                                           |
| xml_etree_iterparse  | 62.3 ms                                                         | 64.0 ms: 1.03x slower                                           |
| xml_etree_generate   | 53.2 ms                                                         | 55.4 ms: 1.04x slower                                           |
| unpickle_list        | 2.62 us                                                         | 2.74 us: 1.04x slower                                           |
| xml_etree_process    | 36.4 ms                                                         | 38.2 ms: 1.05x slower                                           |
| pickle_pure_python   | 175 us                                                          | 190 us: 1.08x slower                                            |
| tomli_loads          | 1.35 sec                                                        | 1.48 sec: 1.09x slower                                          |
| unpickle_pure_python | 122 us                                                          | 137 us: 1.13x slower                                            |
| Geometric mean       | (ref)                                                           | 1.03x slower                                                    |

Benchmark hidden because not significant (2): json_dumps, pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231013-pythonperf1-amd64-python-v3.13.0a1-3.13.0a1-ad056f0 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup | 20.3 ms                                                         | 19.7 ms: 1.03x faster                                           |
| Geometric mean | (ref)                                                           | 1.02x faster                                                    |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231013-pythonperf1-amd64-python-v3.13.0a1-3.13.0a1-ad056f0 |
|-----------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| mako      | 6.36 ms                                                         | 7.20 ms: 1.13x slower                                           |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231013-pythonperf1-amd64-python-v3.13.0a1-3.13.0a1-ad056f0 |
|----------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| create_gc_cycles           | 888 us                                                          | 728 us: 1.22x faster                                            |
| crypto_pyaes               | 45.5 ms                                                         | 43.3 ms: 1.05x faster                                           |
| json_loads                 | 14.2 us                                                         | 13.5 us: 1.05x faster                                           |
| typing_runtime_protocols   | 101 us                                                          | 96.3 us: 1.05x faster                                           |
| gc_traversal               | 1.55 ms                                                         | 1.49 ms: 1.05x faster                                           |
| unpickle                   | 8.40 us                                                         | 8.12 us: 1.03x faster                                           |
| python_startup             | 20.3 ms                                                         | 19.7 ms: 1.03x faster                                           |
| scimark_sparse_mat_mult    | 2.50 ms                                                         | 2.45 ms: 1.02x faster                                           |
| pickle                     | 7.11 us                                                         | 6.98 us: 1.02x faster                                           |
| spectral_norm              | 63.7 ms                                                         | 63.0 ms: 1.01x faster                                           |
| bench_mp_pool              | 64.8 ms                                                         | 64.0 ms: 1.01x faster                                           |
| docutils                   | 1.63 sec                                                        | 1.61 sec: 1.01x faster                                          |
| xml_etree_parse            | 90.9 ms                                                         | 91.6 ms: 1.01x slower                                           |
| regex_effbot               | 1.58 ms                                                         | 1.60 ms: 1.01x slower                                           |
| pickle_dict                | 18.1 us                                                         | 18.4 us: 1.01x slower                                           |
| telco                      | 4.67 ms                                                         | 4.73 ms: 1.01x slower                                           |
| scimark_sor                | 75.3 ms                                                         | 77.0 ms: 1.02x slower                                           |
| fannkuch                   | 243 ms                                                          | 249 ms: 1.02x slower                                            |
| xml_etree_iterparse        | 62.3 ms                                                         | 64.0 ms: 1.03x slower                                           |
| scimark_fft                | 171 ms                                                          | 176 ms: 1.03x slower                                            |
| sqlite_synth               | 1.60 us                                                         | 1.65 us: 1.03x slower                                           |
| pathlib                    | 75.9 ms                                                         | 78.5 ms: 1.04x slower                                           |
| scimark_lu                 | 56.6 ms                                                         | 58.6 ms: 1.04x slower                                           |
| chameleon                  | 4.80 ms                                                         | 4.98 ms: 1.04x slower                                           |
| deepcopy_reduce            | 1.99 us                                                         | 2.07 us: 1.04x slower                                           |
| xml_etree_generate         | 53.2 ms                                                         | 55.4 ms: 1.04x slower                                           |
| nqueens                    | 56.7 ms                                                         | 59.1 ms: 1.04x slower                                           |
| 2to3                       | 207 ms                                                          | 216 ms: 1.04x slower                                            |
| unpickle_list              | 2.62 us                                                         | 2.74 us: 1.04x slower                                           |
| deepcopy                   | 220 us                                                          | 230 us: 1.05x slower                                            |
| scimark_monte_carlo        | 39.1 ms                                                         | 41.0 ms: 1.05x slower                                           |
| xml_etree_process          | 36.4 ms                                                         | 38.2 ms: 1.05x slower                                           |
| chaos                      | 38.4 ms                                                         | 40.4 ms: 1.05x slower                                           |
| async_generators           | 223 ms                                                          | 236 ms: 1.06x slower                                            |
| sympy_expand               | 271 ms                                                          | 287 ms: 1.06x slower                                            |
| sqlglot_normalize          | 173 ms                                                          | 184 ms: 1.06x slower                                            |
| richards_super             | 30.2 ms                                                         | 32.0 ms: 1.06x slower                                           |
| sqlglot_optimize           | 32.7 ms                                                         | 34.8 ms: 1.06x slower                                           |
| meteor_contest             | 69.9 ms                                                         | 74.5 ms: 1.07x slower                                           |
| pprint_pformat             | 966 ms                                                          | 1.03 sec: 1.07x slower                                          |
| nbody                      | 67.6 ms                                                         | 72.2 ms: 1.07x slower                                           |
| pprint_safe_repr           | 474 ms                                                          | 507 ms: 1.07x slower                                            |
| pyflate                    | 279 ms                                                          | 298 ms: 1.07x slower                                            |
| sympy_integrate            | 12.2 ms                                                         | 13.1 ms: 1.07x slower                                           |
| raytrace                   | 162 ms                                                          | 174 ms: 1.07x slower                                            |
| sqlglot_transpile          | 955 us                                                          | 1.03 ms: 1.08x slower                                           |
| float                      | 49.7 ms                                                         | 53.6 ms: 1.08x slower                                           |
| coverage                   | 42.1 ms                                                         | 45.4 ms: 1.08x slower                                           |
| sympy_sum                  | 84.4 ms                                                         | 91.1 ms: 1.08x slower                                           |
| richards                   | 26.7 ms                                                         | 28.8 ms: 1.08x slower                                           |
| pickle_pure_python         | 175 us                                                          | 190 us: 1.08x slower                                            |
| sqlglot_parse              | 748 us                                                          | 811 us: 1.08x slower                                            |
| tornado_http               | 81.8 ms                                                         | 89.1 ms: 1.09x slower                                           |
| bench_thread_pool          | 768 us                                                          | 836 us: 1.09x slower                                            |
| tomli_loads                | 1.35 sec                                                        | 1.48 sec: 1.09x slower                                          |
| logging_format             | 6.22 us                                                         | 6.81 us: 1.09x slower                                           |
| go                         | 82.1 ms                                                         | 90.0 ms: 1.10x slower                                           |
| sympy_str                  | 159 ms                                                          | 175 ms: 1.10x slower                                            |
| hexiom                     | 3.72 ms                                                         | 4.09 ms: 1.10x slower                                           |
| logging_simple             | 5.78 us                                                         | 6.40 us: 1.11x slower                                           |
| deepcopy_memo              | 22.1 us                                                         | 24.8 us: 1.12x slower                                           |
| unpickle_pure_python       | 122 us                                                          | 137 us: 1.13x slower                                            |
| mako                       | 6.36 ms                                                         | 7.20 ms: 1.13x slower                                           |
| mdp                        | 1.31 sec                                                        | 1.49 sec: 1.14x slower                                          |
| generators                 | 19.6 ms                                                         | 22.3 ms: 1.14x slower                                           |
| pycparser                  | 754 ms                                                          | 861 ms: 1.14x slower                                            |
| coroutines                 | 12.8 ms                                                         | 14.7 ms: 1.15x slower                                           |
| deltablue                  | 1.88 ms                                                         | 2.19 ms: 1.16x slower                                           |
| regex_compile              | 78.0 ms                                                         | 90.8 ms: 1.16x slower                                           |
| async_tree_cpu_io_mixed    | 389 ms                                                          | 455 ms: 1.17x slower                                            |
| dulwich_log                | 38.0 ms                                                         | 45.2 ms: 1.19x slower                                           |
| logging_silent             | 52.9 ns                                                         | 63.2 ns: 1.19x slower                                           |
| async_tree_none            | 218 ms                                                          | 267 ms: 1.22x slower                                            |
| async_tree_io              | 588 ms                                                          | 723 ms: 1.23x slower                                            |
| async_tree_cpu_io_mixed_tg | 382 ms                                                          | 486 ms: 1.27x slower                                            |
| async_tree_io_tg           | 605 ms                                                          | 772 ms: 1.27x slower                                            |
| asyncio_tcp_ssl            | 1.48 sec                                                        | 1.89 sec: 1.28x slower                                          |
| async_tree_memoization     | 264 ms                                                          | 340 ms: 1.29x slower                                            |
| comprehensions             | 10.4 us                                                         | 14.2 us: 1.36x slower                                           |
| async_tree_memoization_tg  | 258 ms                                                          | 359 ms: 1.39x slower                                            |
| async_tree_none_tg         | 202 ms                                                          | 285 ms: 1.41x slower                                            |
| Geometric mean             | (ref)                                                           | 1.07x slower                                                    |

Benchmark hidden because not significant (8): regex_v8, json, json_dumps, asyncio_tcp, regex_dna, python_startup_no_site, pidigits, pickle_list
Ignored benchmarks (9) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, django_template, flaskblogging, genshi_text, genshi_xml, html5lib, mypy2, pylint, thrift
Ignored benchmarks (1) of results/bm-20231013-3.13.0a1-ad056f0/bm-20231013-pythonperf1-amd64-python-v3.13.0a1-3.13.0a1-ad056f0.json: unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.05x
- 95% likely to have a slowdown of 1.05x
- 99% likely to have a slowdown of 1.04x

# Memory
- memory change: unknown