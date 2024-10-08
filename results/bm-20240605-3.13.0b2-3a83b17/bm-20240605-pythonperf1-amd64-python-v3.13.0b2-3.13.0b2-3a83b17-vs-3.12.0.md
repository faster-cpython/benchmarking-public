# Results vs. 3.12.0

- fork: python
- ref: v3.13.0b2
- machine: windows-amd64
- commit hash: 3a83b17
- commit date: 2024-06-05
- overall geometric mean: 1.08x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 207 ms: 1.05x faster                                            |
| chameleon      | 4.98 ms                                                     | 4.80 ms: 1.04x faster                                           |
| docutils       | 1.66 sec                                                    | 1.63 sec: 1.02x faster                                          |
| tornado_http   | 89.5 ms                                                     | 81.8 ms: 1.09x faster                                           |
| Geometric mean | (ref)                                                       | 1.05x faster                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| async_tree_memoization_tg  | 367 ms                                                      | 258 ms: 1.42x faster                                            |
| async_tree_none_tg         | 285 ms                                                      | 202 ms: 1.41x faster                                            |
| async_tree_none            | 291 ms                                                      | 218 ms: 1.34x faster                                            |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 382 ms: 1.31x faster                                            |
| async_tree_memoization     | 339 ms                                                      | 264 ms: 1.28x faster                                            |
| async_tree_io_tg           | 771 ms                                                      | 605 ms: 1.27x faster                                            |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 389 ms: 1.26x faster                                            |
| async_tree_io              | 731 ms                                                      | 588 ms: 1.24x faster                                            |
| Geometric mean             | (ref)                                                       | 1.32x faster                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 49.7 ms: 1.14x faster                                           |
| nbody          | 71.9 ms                                                     | 67.6 ms: 1.06x faster                                           |
| pidigits       | 152 ms                                                      | 150 ms: 1.02x faster                                            |
| Geometric mean | (ref)                                                       | 1.07x faster                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_compile  | 87.5 ms                                                     | 78.0 ms: 1.12x faster                                           |
| regex_dna      | 126 ms                                                      | 119 ms: 1.06x faster                                            |
| regex_effbot   | 1.62 ms                                                     | 1.58 ms: 1.02x faster                                           |
| regex_v8       | 14.2 ms                                                     | 15.8 ms: 1.11x slower                                           |
| Geometric mean | (ref)                                                       | 1.02x faster                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| pickle_pure_python   | 195 us                                                      | 175 us: 1.11x faster                                            |
| unpickle_pure_python | 133 us                                                      | 122 us: 1.09x faster                                            |
| xml_etree_generate   | 55.8 ms                                                     | 53.2 ms: 1.05x faster                                           |
| unpickle_list        | 2.75 us                                                     | 2.62 us: 1.05x faster                                           |
| xml_etree_iterparse  | 65.2 ms                                                     | 62.3 ms: 1.05x faster                                           |
| pickle               | 7.43 us                                                     | 7.11 us: 1.04x faster                                           |
| xml_etree_process    | 37.7 ms                                                     | 36.4 ms: 1.03x faster                                           |
| xml_etree_parse      | 93.0 ms                                                     | 90.9 ms: 1.02x faster                                           |
| json_dumps           | 5.70 ms                                                     | 5.61 ms: 1.01x faster                                           |
| pickle_dict          | 18.4 us                                                     | 18.1 us: 1.01x faster                                           |
| tomli_loads          | 1.37 sec                                                    | 1.35 sec: 1.01x faster                                          |
| json_loads           | 13.9 us                                                     | 14.2 us: 1.02x slower                                           |
| unpickle             | 8.18 us                                                     | 8.40 us: 1.03x slower                                           |
| pickle_list          | 2.83 us                                                     | 2.90 us: 1.03x slower                                           |
| Geometric mean       | (ref)                                                       | 1.03x faster                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup | 19.5 ms                                                     | 20.3 ms: 1.04x slower                                           |
| Geometric mean | (ref)                                                       | 1.02x slower                                                    |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 6.36 ms: 1.11x faster                                           |
| django_template | 22.9 ms                                                     | 21.7 ms: 1.06x faster                                           |
| Geometric mean  | (ref)                                                       | 1.09x faster                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| async_tree_memoization_tg  | 367 ms                                                      | 258 ms: 1.42x faster                                            |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.48 sec: 1.41x faster                                          |
| async_tree_none_tg         | 285 ms                                                      | 202 ms: 1.41x faster                                            |
| comprehensions             | 14.1 us                                                     | 10.4 us: 1.36x faster                                           |
| async_tree_none            | 291 ms                                                      | 218 ms: 1.34x faster                                            |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 382 ms: 1.31x faster                                            |
| async_tree_memoization     | 339 ms                                                      | 264 ms: 1.28x faster                                            |
| async_tree_io_tg           | 771 ms                                                      | 605 ms: 1.27x faster                                            |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 389 ms: 1.26x faster                                            |
| async_tree_io              | 731 ms                                                      | 588 ms: 1.24x faster                                            |
| mypy2                      | 509 ms                                                      | 418 ms: 1.22x faster                                            |
| raytrace                   | 192 ms                                                      | 162 ms: 1.19x faster                                            |
| dulwich_log                | 44.3 ms                                                     | 38.0 ms: 1.16x faster                                           |
| generators                 | 22.5 ms                                                     | 19.6 ms: 1.15x faster                                           |
| deltablue                  | 2.16 ms                                                     | 1.88 ms: 1.15x faster                                           |
| logging_silent             | 60.5 ns                                                     | 52.9 ns: 1.14x faster                                           |
| float                      | 56.8 ms                                                     | 49.7 ms: 1.14x faster                                           |
| chaos                      | 43.3 ms                                                     | 38.4 ms: 1.13x faster                                           |
| regex_compile              | 87.5 ms                                                     | 78.0 ms: 1.12x faster                                           |
| coroutines                 | 14.3 ms                                                     | 12.8 ms: 1.12x faster                                           |
| scimark_monte_carlo        | 43.7 ms                                                     | 39.1 ms: 1.12x faster                                           |
| go                         | 91.6 ms                                                     | 82.1 ms: 1.12x faster                                           |
| bench_thread_pool          | 857 us                                                      | 768 us: 1.12x faster                                            |
| mako                       | 7.09 ms                                                     | 6.36 ms: 1.11x faster                                           |
| pickle_pure_python         | 195 us                                                      | 175 us: 1.11x faster                                            |
| nqueens                    | 62.8 ms                                                     | 56.7 ms: 1.11x faster                                           |
| sqlite_synth               | 1.76 us                                                     | 1.60 us: 1.10x faster                                           |
| hexiom                     | 4.10 ms                                                     | 3.72 ms: 1.10x faster                                           |
| sympy_str                  | 175 ms                                                      | 159 ms: 1.10x faster                                            |
| tornado_http               | 89.5 ms                                                     | 81.8 ms: 1.09x faster                                           |
| unpickle_pure_python       | 133 us                                                      | 122 us: 1.09x faster                                            |
| logging_simple             | 6.28 us                                                     | 5.78 us: 1.09x faster                                           |
| sympy_sum                  | 91.5 ms                                                     | 84.4 ms: 1.08x faster                                           |
| deepcopy                   | 238 us                                                      | 220 us: 1.08x faster                                            |
| pprint_safe_repr           | 513 ms                                                      | 474 ms: 1.08x faster                                            |
| pprint_pformat             | 1.05 sec                                                    | 966 ms: 1.08x faster                                            |
| sqlglot_normalize          | 187 ms                                                      | 173 ms: 1.08x faster                                            |
| logging_format             | 6.72 us                                                     | 6.22 us: 1.08x faster                                           |
| scimark_fft                | 184 ms                                                      | 171 ms: 1.08x faster                                            |
| sqlglot_parse              | 804 us                                                      | 748 us: 1.07x faster                                            |
| deepcopy_memo              | 23.7 us                                                     | 22.1 us: 1.07x faster                                           |
| async_generators           | 239 ms                                                      | 223 ms: 1.07x faster                                            |
| sqlglot_transpile          | 1.02 ms                                                     | 955 us: 1.07x faster                                            |
| bench_mp_pool              | 69.2 ms                                                     | 64.8 ms: 1.07x faster                                           |
| meteor_contest             | 74.6 ms                                                     | 69.9 ms: 1.07x faster                                           |
| crypto_pyaes               | 48.5 ms                                                     | 45.5 ms: 1.07x faster                                           |
| richards_super             | 32.1 ms                                                     | 30.2 ms: 1.06x faster                                           |
| nbody                      | 71.9 ms                                                     | 67.6 ms: 1.06x faster                                           |
| regex_dna                  | 126 ms                                                      | 119 ms: 1.06x faster                                            |
| richards                   | 28.4 ms                                                     | 26.7 ms: 1.06x faster                                           |
| pathlib                    | 80.5 ms                                                     | 75.9 ms: 1.06x faster                                           |
| sympy_integrate            | 13.0 ms                                                     | 12.2 ms: 1.06x faster                                           |
| django_template            | 22.9 ms                                                     | 21.7 ms: 1.06x faster                                           |
| pyflate                    | 295 ms                                                      | 279 ms: 1.06x faster                                            |
| sqlglot_optimize           | 34.5 ms                                                     | 32.7 ms: 1.06x faster                                           |
| 2to3                       | 218 ms                                                      | 207 ms: 1.05x faster                                            |
| spectral_norm              | 66.9 ms                                                     | 63.7 ms: 1.05x faster                                           |
| xml_etree_generate         | 55.8 ms                                                     | 53.2 ms: 1.05x faster                                           |
| deepcopy_reduce            | 2.09 us                                                     | 1.99 us: 1.05x faster                                           |
| unpickle_list              | 2.75 us                                                     | 2.62 us: 1.05x faster                                           |
| sympy_expand               | 284 ms                                                      | 271 ms: 1.05x faster                                            |
| mdp                        | 1.37 sec                                                    | 1.31 sec: 1.05x faster                                          |
| scimark_sor                | 78.8 ms                                                     | 75.3 ms: 1.05x faster                                           |
| xml_etree_iterparse        | 65.2 ms                                                     | 62.3 ms: 1.05x faster                                           |
| pickle                     | 7.43 us                                                     | 7.11 us: 1.04x faster                                           |
| scimark_lu                 | 58.9 ms                                                     | 56.6 ms: 1.04x faster                                           |
| chameleon                  | 4.98 ms                                                     | 4.80 ms: 1.04x faster                                           |
| xml_etree_process          | 37.7 ms                                                     | 36.4 ms: 1.03x faster                                           |
| asyncio_tcp                | 487 ms                                                      | 471 ms: 1.03x faster                                            |
| xml_etree_parse            | 93.0 ms                                                     | 90.9 ms: 1.02x faster                                           |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.50 ms: 1.02x faster                                           |
| docutils                   | 1.66 sec                                                    | 1.63 sec: 1.02x faster                                          |
| regex_effbot               | 1.62 ms                                                     | 1.58 ms: 1.02x faster                                           |
| pidigits                   | 152 ms                                                      | 150 ms: 1.02x faster                                            |
| json_dumps                 | 5.70 ms                                                     | 5.61 ms: 1.01x faster                                           |
| pickle_dict                | 18.4 us                                                     | 18.1 us: 1.01x faster                                           |
| fannkuch                   | 247 ms                                                      | 243 ms: 1.01x faster                                            |
| tomli_loads                | 1.37 sec                                                    | 1.35 sec: 1.01x faster                                          |
| json_loads                 | 13.9 us                                                     | 14.2 us: 1.02x slower                                           |
| gc_traversal               | 1.52 ms                                                     | 1.55 ms: 1.02x slower                                           |
| unpickle                   | 8.18 us                                                     | 8.40 us: 1.03x slower                                           |
| pickle_list                | 2.83 us                                                     | 2.90 us: 1.03x slower                                           |
| coverage                   | 40.8 ms                                                     | 42.1 ms: 1.03x slower                                           |
| python_startup             | 19.5 ms                                                     | 20.3 ms: 1.04x slower                                           |
| json                       | 3.05 ms                                                     | 3.19 ms: 1.05x slower                                           |
| typing_runtime_protocols   | 95.1 us                                                     | 101 us: 1.06x slower                                            |
| pycparser                  | 699 ms                                                      | 754 ms: 1.08x slower                                            |
| regex_v8                   | 14.2 ms                                                     | 15.8 ms: 1.11x slower                                           |
| telco                      | 4.13 ms                                                     | 4.67 ms: 1.13x slower                                           |
| create_gc_cycles           | 752 us                                                      | 888 us: 1.18x slower                                            |
| Geometric mean             | (ref)                                                       | 1.08x faster                                                    |

Benchmark hidden because not significant (2): python_startup_no_site, aiohttp
Ignored benchmarks (4) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: dask, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (6) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17.json: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.06x
- 99% likely to have a speedup of 1.05x

# Memory
- memory change: unknown