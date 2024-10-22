# Results vs. 3.13.0

- fork: python
- ref: v3.13.0a1
- machine: windows-amd64
- commit hash: ad056f0
- commit date: 2023-10-13
- overall geometric mean: 1.06x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20231013-pythonperf1-amd64-python-v3.13.0a1-3.13.0a1-ad056f0 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| 2to3           | 217 ms                                                      | 216 ms: 1.01x faster                                            |
| chameleon      | 4.72 ms                                                     | 4.98 ms: 1.06x slower                                           |
| docutils       | 1.57 sec                                                    | 1.61 sec: 1.02x slower                                          |
| tornado_http   | 92.8 ms                                                     | 89.1 ms: 1.04x faster                                           |
| Geometric mean | (ref)                                                       | 1.01x slower                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20231013-pythonperf1-amd64-python-v3.13.0a1-3.13.0a1-ad056f0 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| asyncio_tcp                | 654 ms                                                      | 470 ms: 1.39x faster                                            |
| async_generators           | 223 ms                                                      | 236 ms: 1.06x slower                                            |
| asyncio_tcp_ssl            | 1.64 sec                                                    | 1.89 sec: 1.15x slower                                          |
| coroutines                 | 12.5 ms                                                     | 14.7 ms: 1.17x slower                                           |
| async_tree_cpu_io_mixed    | 387 ms                                                      | 455 ms: 1.17x slower                                            |
| async_tree_none            | 223 ms                                                      | 267 ms: 1.19x slower                                            |
| async_tree_memoization_tg  | 288 ms                                                      | 359 ms: 1.25x slower                                            |
| async_tree_memoization     | 271 ms                                                      | 340 ms: 1.25x slower                                            |
| async_tree_cpu_io_mixed_tg | 375 ms                                                      | 486 ms: 1.30x slower                                            |
| async_tree_none_tg         | 206 ms                                                      | 285 ms: 1.38x slower                                            |
| async_tree_io              | 521 ms                                                      | 723 ms: 1.39x slower                                            |
| async_tree_io_tg           | 512 ms                                                      | 772 ms: 1.51x slower                                            |
| Geometric mean             | (ref)                                                       | 1.19x slower                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20231013-pythonperf1-amd64-python-v3.13.0a1-3.13.0a1-ad056f0 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| pidigits       | 148 ms                                                      | 150 ms: 1.01x slower                                            |
| float          | 48.1 ms                                                     | 53.6 ms: 1.11x slower                                           |
| nbody          | 64.5 ms                                                     | 72.2 ms: 1.12x slower                                           |
| Geometric mean | (ref)                                                       | 1.08x slower                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20231013-pythonperf1-amd64-python-v3.13.0a1-3.13.0a1-ad056f0 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_effbot   | 1.62 ms                                                     | 1.60 ms: 1.01x faster                                           |
| regex_v8       | 14.7 ms                                                     | 14.8 ms: 1.01x slower                                           |
| regex_dna      | 114 ms                                                      | 119 ms: 1.04x slower                                            |
| regex_compile  | 80.1 ms                                                     | 90.8 ms: 1.13x slower                                           |
| Geometric mean | (ref)                                                       | 1.04x slower                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20231013-pythonperf1-amd64-python-v3.13.0a1-3.13.0a1-ad056f0 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| unpickle             | 8.63 us                                                     | 8.12 us: 1.06x faster                                           |
| json_loads           | 14.3 us                                                     | 13.5 us: 1.06x faster                                           |
| pickle               | 7.34 us                                                     | 6.98 us: 1.05x faster                                           |
| json_dumps           | 5.76 ms                                                     | 5.60 ms: 1.03x faster                                           |
| xml_etree_parse      | 93.2 ms                                                     | 91.6 ms: 1.02x faster                                           |
| pickle_dict          | 18.0 us                                                     | 18.4 us: 1.02x slower                                           |
| xml_etree_iterparse  | 62.3 ms                                                     | 64.0 ms: 1.03x slower                                           |
| pickle_pure_python   | 183 us                                                      | 190 us: 1.03x slower                                            |
| xml_etree_generate   | 53.3 ms                                                     | 55.4 ms: 1.04x slower                                           |
| xml_etree_process    | 36.5 ms                                                     | 38.2 ms: 1.05x slower                                           |
| tomli_loads          | 1.36 sec                                                    | 1.48 sec: 1.08x slower                                          |
| unpickle_pure_python | 127 us                                                      | 137 us: 1.08x slower                                            |
| Geometric mean       | (ref)                                                       | 1.01x slower                                                    |

Benchmark hidden because not significant (2): unpickle_list, pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20231013-pythonperf1-amd64-python-v3.13.0a1-3.13.0a1-ad056f0 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup         | 22.2 ms                                                     | 19.7 ms: 1.13x faster                                           |
| python_startup_no_site | 17.8 ms                                                     | 16.2 ms: 1.10x faster                                           |
| Geometric mean         | (ref)                                                       | 1.11x faster                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20231013-pythonperf1-amd64-python-v3.13.0a1-3.13.0a1-ad056f0 |
|-----------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| mako      | 6.24 ms                                                     | 7.20 ms: 1.15x slower                                           |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20231013-pythonperf1-amd64-python-v3.13.0a1-3.13.0a1-ad056f0 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| asyncio_tcp                | 654 ms                                                      | 470 ms: 1.39x faster                                            |
| create_gc_cycles           | 829 us                                                      | 728 us: 1.14x faster                                            |
| python_startup             | 22.2 ms                                                     | 19.7 ms: 1.13x faster                                           |
| python_startup_no_site     | 17.8 ms                                                     | 16.2 ms: 1.10x faster                                           |
| bench_mp_pool              | 69.6 ms                                                     | 64.0 ms: 1.09x faster                                           |
| unpickle                   | 8.63 us                                                     | 8.12 us: 1.06x faster                                           |
| json_loads                 | 14.3 us                                                     | 13.5 us: 1.06x faster                                           |
| pickle                     | 7.34 us                                                     | 6.98 us: 1.05x faster                                           |
| gc_traversal               | 1.55 ms                                                     | 1.49 ms: 1.05x faster                                           |
| typing_runtime_protocols   | 100 us                                                      | 96.3 us: 1.04x faster                                           |
| tornado_http               | 92.8 ms                                                     | 89.1 ms: 1.04x faster                                           |
| unpack_sequence            | 40.0 ns                                                     | 38.5 ns: 1.04x faster                                           |
| pathlib                    | 81.2 ms                                                     | 78.5 ms: 1.03x faster                                           |
| coverage                   | 46.7 ms                                                     | 45.4 ms: 1.03x faster                                           |
| json_dumps                 | 5.76 ms                                                     | 5.60 ms: 1.03x faster                                           |
| telco                      | 4.85 ms                                                     | 4.73 ms: 1.03x faster                                           |
| xml_etree_parse            | 93.2 ms                                                     | 91.6 ms: 1.02x faster                                           |
| regex_effbot               | 1.62 ms                                                     | 1.60 ms: 1.01x faster                                           |
| 2to3                       | 217 ms                                                      | 216 ms: 1.01x faster                                            |
| sympy_expand               | 285 ms                                                      | 287 ms: 1.00x slower                                            |
| scimark_fft                | 174 ms                                                      | 176 ms: 1.01x slower                                            |
| crypto_pyaes               | 42.8 ms                                                     | 43.3 ms: 1.01x slower                                           |
| pidigits                   | 148 ms                                                      | 150 ms: 1.01x slower                                            |
| regex_v8                   | 14.7 ms                                                     | 14.8 ms: 1.01x slower                                           |
| scimark_monte_carlo        | 40.3 ms                                                     | 41.0 ms: 1.02x slower                                           |
| pickle_dict                | 18.0 us                                                     | 18.4 us: 1.02x slower                                           |
| fannkuch                   | 245 ms                                                      | 249 ms: 1.02x slower                                            |
| docutils                   | 1.57 sec                                                    | 1.61 sec: 1.02x slower                                          |
| deepcopy_reduce            | 2.02 us                                                     | 2.07 us: 1.03x slower                                           |
| xml_etree_iterparse        | 62.3 ms                                                     | 64.0 ms: 1.03x slower                                           |
| pprint_safe_repr           | 493 ms                                                      | 507 ms: 1.03x slower                                            |
| deepcopy                   | 223 us                                                      | 230 us: 1.03x slower                                            |
| meteor_contest             | 72.3 ms                                                     | 74.5 ms: 1.03x slower                                           |
| sqlite_synth               | 1.60 us                                                     | 1.65 us: 1.03x slower                                           |
| pickle_pure_python         | 183 us                                                      | 190 us: 1.03x slower                                            |
| xml_etree_generate         | 53.3 ms                                                     | 55.4 ms: 1.04x slower                                           |
| regex_dna                  | 114 ms                                                      | 119 ms: 1.04x slower                                            |
| pprint_pformat             | 991 ms                                                      | 1.03 sec: 1.04x slower                                          |
| scimark_sparse_mat_mult    | 2.34 ms                                                     | 2.45 ms: 1.05x slower                                           |
| xml_etree_process          | 36.5 ms                                                     | 38.2 ms: 1.05x slower                                           |
| sympy_str                  | 166 ms                                                      | 175 ms: 1.05x slower                                            |
| sqlglot_optimize           | 33.1 ms                                                     | 34.8 ms: 1.05x slower                                           |
| sympy_sum                  | 86.4 ms                                                     | 91.1 ms: 1.05x slower                                           |
| chameleon                  | 4.72 ms                                                     | 4.98 ms: 1.06x slower                                           |
| async_generators           | 223 ms                                                      | 236 ms: 1.06x slower                                            |
| spectral_norm              | 59.2 ms                                                     | 63.0 ms: 1.06x slower                                           |
| nqueens                    | 55.5 ms                                                     | 59.1 ms: 1.06x slower                                           |
| go                         | 84.6 ms                                                     | 90.0 ms: 1.06x slower                                           |
| sqlglot_parse              | 761 us                                                      | 811 us: 1.07x slower                                            |
| chaos                      | 37.9 ms                                                     | 40.4 ms: 1.07x slower                                           |
| scimark_sor                | 72.0 ms                                                     | 77.0 ms: 1.07x slower                                           |
| sympy_integrate            | 12.3 ms                                                     | 13.1 ms: 1.07x slower                                           |
| sqlglot_normalize          | 171 ms                                                      | 184 ms: 1.07x slower                                            |
| mdp                        | 1.38 sec                                                    | 1.49 sec: 1.08x slower                                          |
| sqlglot_transpile          | 952 us                                                      | 1.03 ms: 1.08x slower                                           |
| pyflate                    | 275 ms                                                      | 298 ms: 1.08x slower                                            |
| tomli_loads                | 1.36 sec                                                    | 1.48 sec: 1.08x slower                                          |
| unpickle_pure_python       | 127 us                                                      | 137 us: 1.08x slower                                            |
| scimark_lu                 | 54.0 ms                                                     | 58.6 ms: 1.09x slower                                           |
| richards_super             | 29.3 ms                                                     | 32.0 ms: 1.09x slower                                           |
| logging_format             | 6.15 us                                                     | 6.81 us: 1.11x slower                                           |
| richards                   | 26.0 ms                                                     | 28.8 ms: 1.11x slower                                           |
| hexiom                     | 3.69 ms                                                     | 4.09 ms: 1.11x slower                                           |
| float                      | 48.1 ms                                                     | 53.6 ms: 1.11x slower                                           |
| raytrace                   | 156 ms                                                      | 174 ms: 1.12x slower                                            |
| logging_simple             | 5.72 us                                                     | 6.40 us: 1.12x slower                                           |
| dulwich_log                | 40.4 ms                                                     | 45.2 ms: 1.12x slower                                           |
| nbody                      | 64.5 ms                                                     | 72.2 ms: 1.12x slower                                           |
| regex_compile              | 80.1 ms                                                     | 90.8 ms: 1.13x slower                                           |
| deepcopy_memo              | 21.8 us                                                     | 24.8 us: 1.13x slower                                           |
| pycparser                  | 758 ms                                                      | 861 ms: 1.14x slower                                            |
| generators                 | 19.5 ms                                                     | 22.3 ms: 1.15x slower                                           |
| asyncio_tcp_ssl            | 1.64 sec                                                    | 1.89 sec: 1.15x slower                                          |
| mako                       | 6.24 ms                                                     | 7.20 ms: 1.15x slower                                           |
| coroutines                 | 12.5 ms                                                     | 14.7 ms: 1.17x slower                                           |
| deltablue                  | 1.86 ms                                                     | 2.19 ms: 1.17x slower                                           |
| async_tree_cpu_io_mixed    | 387 ms                                                      | 455 ms: 1.17x slower                                            |
| async_tree_none            | 223 ms                                                      | 267 ms: 1.19x slower                                            |
| logging_silent             | 51.0 ns                                                     | 63.2 ns: 1.24x slower                                           |
| async_tree_memoization_tg  | 288 ms                                                      | 359 ms: 1.25x slower                                            |
| async_tree_memoization     | 271 ms                                                      | 340 ms: 1.25x slower                                            |
| async_tree_cpu_io_mixed_tg | 375 ms                                                      | 486 ms: 1.30x slower                                            |
| comprehensions             | 10.2 us                                                     | 14.2 us: 1.38x slower                                           |
| async_tree_none_tg         | 206 ms                                                      | 285 ms: 1.38x slower                                            |
| async_tree_io              | 521 ms                                                      | 723 ms: 1.39x slower                                            |
| async_tree_io_tg           | 512 ms                                                      | 772 ms: 1.51x slower                                            |
| Geometric mean             | (ref)                                                       | 1.06x slower                                                    |

Benchmark hidden because not significant (4): unpickle_list, json, bench_thread_pool, pickle_list
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, django_template, flaskblogging, genshi_text, genshi_xml, html5lib, mypy2, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.04x
- 95% likely to have a slowdown of 1.04x
- 99% likely to have a slowdown of 1.03x

# Memory
- memory change: unknown