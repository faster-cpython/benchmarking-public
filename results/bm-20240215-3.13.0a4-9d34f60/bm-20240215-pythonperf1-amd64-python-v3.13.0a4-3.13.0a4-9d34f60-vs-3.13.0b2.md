# Results vs. 3.13.0b2

- fork: python
- ref: v3.13.0a4
- machine: windows-amd64
- commit hash: 9d34f60
- commit date: 2024-02-15
- overall geometric mean: 1.04x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240215-pythonperf1-amd64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| 2to3           | 207 ms                                                          | 214 ms: 1.04x slower                                            |
| chameleon      | 4.80 ms                                                         | 5.01 ms: 1.04x slower                                           |
| docutils       | 1.63 sec                                                        | 1.55 sec: 1.05x faster                                          |
| html5lib       | 35.0 ms                                                         | 36.9 ms: 1.05x slower                                           |
| tornado_http   | 81.8 ms                                                         | 84.3 ms: 1.03x slower                                           |
| Geometric mean | (ref)                                                           | 1.02x slower                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240215-pythonperf1-amd64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| async_tree_cpu_io_mixed    | 389 ms                                                          | 453 ms: 1.16x slower                                            |
| async_tree_none            | 218 ms                                                          | 266 ms: 1.22x slower                                            |
| async_tree_cpu_io_mixed_tg | 382 ms                                                          | 472 ms: 1.23x slower                                            |
| async_tree_io              | 588 ms                                                          | 732 ms: 1.25x slower                                            |
| async_tree_io_tg           | 605 ms                                                          | 758 ms: 1.25x slower                                            |
| async_tree_memoization     | 264 ms                                                          | 340 ms: 1.29x slower                                            |
| async_tree_memoization_tg  | 258 ms                                                          | 349 ms: 1.35x slower                                            |
| async_tree_none_tg         | 202 ms                                                          | 274 ms: 1.36x slower                                            |
| Geometric mean             | (ref)                                                           | 1.26x slower                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240215-pythonperf1-amd64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| pidigits       | 150 ms                                                          | 148 ms: 1.02x faster                                            |
| float          | 49.7 ms                                                         | 51.0 ms: 1.02x slower                                           |
| nbody          | 67.6 ms                                                         | 73.2 ms: 1.08x slower                                           |
| Geometric mean | (ref)                                                           | 1.03x slower                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240215-pythonperf1-amd64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_v8       | 15.8 ms                                                         | 14.4 ms: 1.09x faster                                           |
| regex_dna      | 119 ms                                                          | 115 ms: 1.04x faster                                            |
| regex_effbot   | 1.58 ms                                                         | 1.56 ms: 1.01x faster                                           |
| Geometric mean | (ref)                                                           | 1.04x faster                                                    |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240215-pythonperf1-amd64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| json_loads           | 14.2 us                                                         | 13.7 us: 1.04x faster                                           |
| json_dumps           | 5.61 ms                                                         | 5.58 ms: 1.01x faster                                           |
| pickle_dict          | 18.1 us                                                         | 18.4 us: 1.01x slower                                           |
| xml_etree_parse      | 90.9 ms                                                         | 92.2 ms: 1.01x slower                                           |
| xml_etree_process    | 36.4 ms                                                         | 37.1 ms: 1.02x slower                                           |
| unpickle_list        | 2.62 us                                                         | 2.68 us: 1.02x slower                                           |
| xml_etree_generate   | 53.2 ms                                                         | 54.5 ms: 1.03x slower                                           |
| pickle               | 7.11 us                                                         | 7.32 us: 1.03x slower                                           |
| unpickle             | 8.40 us                                                         | 8.66 us: 1.03x slower                                           |
| xml_etree_iterparse  | 62.3 ms                                                         | 65.1 ms: 1.04x slower                                           |
| tomli_loads          | 1.35 sec                                                        | 1.43 sec: 1.06x slower                                          |
| pickle_pure_python   | 175 us                                                          | 186 us: 1.06x slower                                            |
| unpickle_pure_python | 122 us                                                          | 129 us: 1.06x slower                                            |
| Geometric mean       | (ref)                                                           | 1.02x slower                                                    |

Benchmark hidden because not significant (1): pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240215-pythonperf1-amd64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                         | 17.8 ms: 1.10x slower                                           |
| Geometric mean         | (ref)                                                           | 1.04x slower                                                    |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240215-pythonperf1-amd64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|-----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| mako            | 6.36 ms                                                         | 6.29 ms: 1.01x faster                                           |
| django_template | 21.7 ms                                                         | 22.5 ms: 1.04x slower                                           |
| genshi_xml      | 31.6 ms                                                         | 35.1 ms: 1.11x slower                                           |
| genshi_text     | 14.4 ms                                                         | 16.0 ms: 1.11x slower                                           |
| Geometric mean  | (ref)                                                           | 1.06x slower                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240215-pythonperf1-amd64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| typing_runtime_protocols   | 101 us                                                          | 71.0 us: 1.42x faster                                           |
| create_gc_cycles           | 888 us                                                          | 743 us: 1.19x faster                                            |
| json                       | 3.19 ms                                                         | 2.91 ms: 1.10x faster                                           |
| regex_v8                   | 15.8 ms                                                         | 14.4 ms: 1.09x faster                                           |
| spectral_norm              | 63.7 ms                                                         | 59.0 ms: 1.08x faster                                           |
| crypto_pyaes               | 45.5 ms                                                         | 42.8 ms: 1.06x faster                                           |
| docutils                   | 1.63 sec                                                        | 1.55 sec: 1.05x faster                                          |
| sqlite_synth               | 1.60 us                                                         | 1.53 us: 1.04x faster                                           |
| gc_traversal               | 1.55 ms                                                         | 1.50 ms: 1.04x faster                                           |
| regex_dna                  | 119 ms                                                          | 115 ms: 1.04x faster                                            |
| json_loads                 | 14.2 us                                                         | 13.7 us: 1.04x faster                                           |
| scimark_lu                 | 56.6 ms                                                         | 55.0 ms: 1.03x faster                                           |
| pidigits                   | 150 ms                                                          | 148 ms: 1.02x faster                                            |
| regex_effbot               | 1.58 ms                                                         | 1.56 ms: 1.01x faster                                           |
| mako                       | 6.36 ms                                                         | 6.29 ms: 1.01x faster                                           |
| sympy_sum                  | 84.4 ms                                                         | 83.5 ms: 1.01x faster                                           |
| json_dumps                 | 5.61 ms                                                         | 5.58 ms: 1.01x faster                                           |
| mypy2                      | 418 ms                                                          | 416 ms: 1.00x faster                                            |
| scimark_sparse_mat_mult    | 2.50 ms                                                         | 2.49 ms: 1.00x faster                                           |
| sympy_str                  | 159 ms                                                          | 160 ms: 1.00x slower                                            |
| thrift                     | 8.11 ms                                                         | 8.18 ms: 1.01x slower                                           |
| pickle_dict                | 18.1 us                                                         | 18.4 us: 1.01x slower                                           |
| sympy_expand               | 271 ms                                                          | 274 ms: 1.01x slower                                            |
| sympy_integrate            | 12.2 ms                                                         | 12.4 ms: 1.01x slower                                           |
| telco                      | 4.67 ms                                                         | 4.73 ms: 1.01x slower                                           |
| xml_etree_parse            | 90.9 ms                                                         | 92.2 ms: 1.01x slower                                           |
| raytrace                   | 162 ms                                                          | 165 ms: 1.01x slower                                            |
| sqlglot_normalize          | 173 ms                                                          | 176 ms: 1.02x slower                                            |
| xml_etree_process          | 36.4 ms                                                         | 37.1 ms: 1.02x slower                                           |
| sqlglot_optimize           | 32.7 ms                                                         | 33.4 ms: 1.02x slower                                           |
| mdp                        | 1.31 sec                                                        | 1.34 sec: 1.02x slower                                          |
| unpickle_list              | 2.62 us                                                         | 2.68 us: 1.02x slower                                           |
| pyflate                    | 279 ms                                                          | 285 ms: 1.02x slower                                            |
| float                      | 49.7 ms                                                         | 51.0 ms: 1.02x slower                                           |
| hexiom                     | 3.72 ms                                                         | 3.82 ms: 1.02x slower                                           |
| bench_mp_pool              | 64.8 ms                                                         | 66.4 ms: 1.03x slower                                           |
| xml_etree_generate         | 53.2 ms                                                         | 54.5 ms: 1.03x slower                                           |
| sqlglot_parse              | 748 us                                                          | 768 us: 1.03x slower                                            |
| fannkuch                   | 243 ms                                                          | 250 ms: 1.03x slower                                            |
| nqueens                    | 56.7 ms                                                         | 58.2 ms: 1.03x slower                                           |
| deepcopy_reduce            | 1.99 us                                                         | 2.05 us: 1.03x slower                                           |
| pickle                     | 7.11 us                                                         | 7.32 us: 1.03x slower                                           |
| chaos                      | 38.4 ms                                                         | 39.5 ms: 1.03x slower                                           |
| go                         | 82.1 ms                                                         | 84.4 ms: 1.03x slower                                           |
| sqlglot_transpile          | 955 us                                                          | 983 us: 1.03x slower                                            |
| async_generators           | 223 ms                                                          | 230 ms: 1.03x slower                                            |
| tornado_http               | 81.8 ms                                                         | 84.3 ms: 1.03x slower                                           |
| unpickle                   | 8.40 us                                                         | 8.66 us: 1.03x slower                                           |
| meteor_contest             | 69.9 ms                                                         | 72.2 ms: 1.03x slower                                           |
| scimark_sor                | 75.3 ms                                                         | 77.9 ms: 1.03x slower                                           |
| 2to3                       | 207 ms                                                          | 214 ms: 1.04x slower                                            |
| comprehensions             | 10.4 us                                                         | 10.8 us: 1.04x slower                                           |
| django_template            | 21.7 ms                                                         | 22.5 ms: 1.04x slower                                           |
| coroutines                 | 12.8 ms                                                         | 13.2 ms: 1.04x slower                                           |
| deepcopy_memo              | 22.1 us                                                         | 23.0 us: 1.04x slower                                           |
| scimark_monte_carlo        | 39.1 ms                                                         | 40.7 ms: 1.04x slower                                           |
| chameleon                  | 4.80 ms                                                         | 5.01 ms: 1.04x slower                                           |
| xml_etree_iterparse        | 62.3 ms                                                         | 65.1 ms: 1.04x slower                                           |
| richards                   | 26.7 ms                                                         | 28.0 ms: 1.05x slower                                           |
| scimark_fft                | 171 ms                                                          | 179 ms: 1.05x slower                                            |
| richards_super             | 30.2 ms                                                         | 31.6 ms: 1.05x slower                                           |
| html5lib                   | 35.0 ms                                                         | 36.9 ms: 1.05x slower                                           |
| deltablue                  | 1.88 ms                                                         | 1.98 ms: 1.05x slower                                           |
| pprint_safe_repr           | 474 ms                                                          | 500 ms: 1.05x slower                                            |
| logging_format             | 6.22 us                                                         | 6.57 us: 1.06x slower                                           |
| tomli_loads                | 1.35 sec                                                        | 1.43 sec: 1.06x slower                                          |
| pprint_pformat             | 966 ms                                                          | 1.02 sec: 1.06x slower                                          |
| deepcopy                   | 220 us                                                          | 233 us: 1.06x slower                                            |
| pickle_pure_python         | 175 us                                                          | 186 us: 1.06x slower                                            |
| unpickle_pure_python       | 122 us                                                          | 129 us: 1.06x slower                                            |
| generators                 | 19.6 ms                                                         | 20.8 ms: 1.06x slower                                           |
| logging_simple             | 5.78 us                                                         | 6.15 us: 1.06x slower                                           |
| pathlib                    | 75.9 ms                                                         | 80.8 ms: 1.07x slower                                           |
| bench_thread_pool          | 768 us                                                          | 824 us: 1.07x slower                                            |
| logging_silent             | 52.9 ns                                                         | 57.3 ns: 1.08x slower                                           |
| nbody                      | 67.6 ms                                                         | 73.2 ms: 1.08x slower                                           |
| dulwich_log                | 38.0 ms                                                         | 41.3 ms: 1.09x slower                                           |
| python_startup_no_site     | 16.2 ms                                                         | 17.8 ms: 1.10x slower                                           |
| genshi_xml                 | 31.6 ms                                                         | 35.1 ms: 1.11x slower                                           |
| genshi_text                | 14.4 ms                                                         | 16.0 ms: 1.11x slower                                           |
| coverage                   | 42.1 ms                                                         | 47.3 ms: 1.12x slower                                           |
| async_tree_cpu_io_mixed    | 389 ms                                                          | 453 ms: 1.16x slower                                            |
| asyncio_tcp_ssl            | 1.48 sec                                                        | 1.77 sec: 1.20x slower                                          |
| async_tree_none            | 218 ms                                                          | 266 ms: 1.22x slower                                            |
| async_tree_cpu_io_mixed_tg | 382 ms                                                          | 472 ms: 1.23x slower                                            |
| async_tree_io              | 588 ms                                                          | 732 ms: 1.25x slower                                            |
| async_tree_io_tg           | 605 ms                                                          | 758 ms: 1.25x slower                                            |
| async_tree_memoization     | 264 ms                                                          | 340 ms: 1.29x slower                                            |
| async_tree_memoization_tg  | 258 ms                                                          | 349 ms: 1.35x slower                                            |
| async_tree_none_tg         | 202 ms                                                          | 274 ms: 1.36x slower                                            |
| Geometric mean             | (ref)                                                           | 1.04x slower                                                    |

Benchmark hidden because not significant (8): python_startup, aiohttp, regex_compile, flaskblogging, pycparser, pylint, pickle_list, asyncio_tcp

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.02x

# Memory
- memory change: unknown