# Results vs. 3.13.0b2

- fork: python
- ref: v3.12.0
- machine: windows-amd64
- commit hash: 0fb18b0
- commit date: 2023-10-02
- overall geometric mean: 1.08x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 |
|----------------|:---------------------------------------------------------------:|:-----------------------------------------------------------:|
| 2to3           | 207 ms                                                          | 218 ms: 1.05x slower                                        |
| chameleon      | 4.80 ms                                                         | 4.98 ms: 1.04x slower                                       |
| docutils       | 1.63 sec                                                        | 1.66 sec: 1.02x slower                                      |
| tornado_http   | 81.8 ms                                                         | 89.5 ms: 1.09x slower                                       |
| Geometric mean | (ref)                                                           | 1.05x slower                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 |
|----------------------------|:---------------------------------------------------------------:|:-----------------------------------------------------------:|
| async_tree_io              | 588 ms                                                          | 731 ms: 1.24x slower                                        |
| async_tree_cpu_io_mixed    | 389 ms                                                          | 489 ms: 1.26x slower                                        |
| async_tree_io_tg           | 605 ms                                                          | 771 ms: 1.27x slower                                        |
| async_tree_memoization     | 264 ms                                                          | 339 ms: 1.28x slower                                        |
| async_tree_cpu_io_mixed_tg | 382 ms                                                          | 502 ms: 1.31x slower                                        |
| async_tree_none            | 218 ms                                                          | 291 ms: 1.34x slower                                        |
| async_tree_none_tg         | 202 ms                                                          | 285 ms: 1.41x slower                                        |
| async_tree_memoization_tg  | 258 ms                                                          | 367 ms: 1.42x slower                                        |
| Geometric mean             | (ref)                                                           | 1.32x slower                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 |
|----------------|:---------------------------------------------------------------:|:-----------------------------------------------------------:|
| pidigits       | 150 ms                                                          | 152 ms: 1.02x slower                                        |
| nbody          | 67.6 ms                                                         | 71.9 ms: 1.06x slower                                       |
| float          | 49.7 ms                                                         | 56.8 ms: 1.14x slower                                       |
| Geometric mean | (ref)                                                           | 1.07x slower                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 |
|----------------|:---------------------------------------------------------------:|:-----------------------------------------------------------:|
| regex_v8       | 15.8 ms                                                         | 14.2 ms: 1.11x faster                                       |
| regex_effbot   | 1.58 ms                                                         | 1.62 ms: 1.02x slower                                       |
| regex_dna      | 119 ms                                                          | 126 ms: 1.06x slower                                        |
| regex_compile  | 78.0 ms                                                         | 87.5 ms: 1.12x slower                                       |
| Geometric mean | (ref)                                                           | 1.02x slower                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 |
|----------------------|:---------------------------------------------------------------:|:-----------------------------------------------------------:|
| pickle_list          | 2.90 us                                                         | 2.83 us: 1.03x faster                                       |
| unpickle             | 8.40 us                                                         | 8.18 us: 1.03x faster                                       |
| json_loads           | 14.2 us                                                         | 13.9 us: 1.02x faster                                       |
| tomli_loads          | 1.35 sec                                                        | 1.37 sec: 1.01x slower                                      |
| pickle_dict          | 18.1 us                                                         | 18.4 us: 1.01x slower                                       |
| json_dumps           | 5.61 ms                                                         | 5.70 ms: 1.01x slower                                       |
| xml_etree_parse      | 90.9 ms                                                         | 93.0 ms: 1.02x slower                                       |
| xml_etree_process    | 36.4 ms                                                         | 37.7 ms: 1.03x slower                                       |
| pickle               | 7.11 us                                                         | 7.43 us: 1.04x slower                                       |
| xml_etree_iterparse  | 62.3 ms                                                         | 65.2 ms: 1.05x slower                                       |
| unpickle_list        | 2.62 us                                                         | 2.75 us: 1.05x slower                                       |
| xml_etree_generate   | 53.2 ms                                                         | 55.8 ms: 1.05x slower                                       |
| unpickle_pure_python | 122 us                                                          | 133 us: 1.09x slower                                        |
| pickle_pure_python   | 175 us                                                          | 195 us: 1.11x slower                                        |
| Geometric mean       | (ref)                                                           | 1.03x slower                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 |
|----------------|:---------------------------------------------------------------:|:-----------------------------------------------------------:|
| python_startup | 20.3 ms                                                         | 19.5 ms: 1.04x faster                                       |
| Geometric mean | (ref)                                                           | 1.02x faster                                                |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 |
|-----------------|:---------------------------------------------------------------:|:-----------------------------------------------------------:|
| django_template | 21.7 ms                                                         | 22.9 ms: 1.06x slower                                       |
| mako            | 6.36 ms                                                         | 7.09 ms: 1.11x slower                                       |
| Geometric mean  | (ref)                                                           | 1.09x slower                                                |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 |
|----------------------------|:---------------------------------------------------------------:|:-----------------------------------------------------------:|
| create_gc_cycles           | 888 us                                                          | 752 us: 1.18x faster                                        |
| telco                      | 4.67 ms                                                         | 4.13 ms: 1.13x faster                                       |
| regex_v8                   | 15.8 ms                                                         | 14.2 ms: 1.11x faster                                       |
| pycparser                  | 754 ms                                                          | 699 ms: 1.08x faster                                        |
| typing_runtime_protocols   | 101 us                                                          | 95.1 us: 1.06x faster                                       |
| json                       | 3.19 ms                                                         | 3.05 ms: 1.05x faster                                       |
| python_startup             | 20.3 ms                                                         | 19.5 ms: 1.04x faster                                       |
| coverage                   | 42.1 ms                                                         | 40.8 ms: 1.03x faster                                       |
| pickle_list                | 2.90 us                                                         | 2.83 us: 1.03x faster                                       |
| unpickle                   | 8.40 us                                                         | 8.18 us: 1.03x faster                                       |
| gc_traversal               | 1.55 ms                                                         | 1.52 ms: 1.02x faster                                       |
| json_loads                 | 14.2 us                                                         | 13.9 us: 1.02x faster                                       |
| tomli_loads                | 1.35 sec                                                        | 1.37 sec: 1.01x slower                                      |
| fannkuch                   | 243 ms                                                          | 247 ms: 1.01x slower                                        |
| pickle_dict                | 18.1 us                                                         | 18.4 us: 1.01x slower                                       |
| json_dumps                 | 5.61 ms                                                         | 5.70 ms: 1.01x slower                                       |
| pidigits                   | 150 ms                                                          | 152 ms: 1.02x slower                                        |
| regex_effbot               | 1.58 ms                                                         | 1.62 ms: 1.02x slower                                       |
| docutils                   | 1.63 sec                                                        | 1.66 sec: 1.02x slower                                      |
| scimark_sparse_mat_mult    | 2.50 ms                                                         | 2.56 ms: 1.02x slower                                       |
| xml_etree_parse            | 90.9 ms                                                         | 93.0 ms: 1.02x slower                                       |
| asyncio_tcp                | 471 ms                                                          | 487 ms: 1.03x slower                                        |
| xml_etree_process          | 36.4 ms                                                         | 37.7 ms: 1.03x slower                                       |
| chameleon                  | 4.80 ms                                                         | 4.98 ms: 1.04x slower                                       |
| scimark_lu                 | 56.6 ms                                                         | 58.9 ms: 1.04x slower                                       |
| pickle                     | 7.11 us                                                         | 7.43 us: 1.04x slower                                       |
| xml_etree_iterparse        | 62.3 ms                                                         | 65.2 ms: 1.05x slower                                       |
| scimark_sor                | 75.3 ms                                                         | 78.8 ms: 1.05x slower                                       |
| mdp                        | 1.31 sec                                                        | 1.37 sec: 1.05x slower                                      |
| sympy_expand               | 271 ms                                                          | 284 ms: 1.05x slower                                        |
| unpickle_list              | 2.62 us                                                         | 2.75 us: 1.05x slower                                       |
| deepcopy_reduce            | 1.99 us                                                         | 2.09 us: 1.05x slower                                       |
| xml_etree_generate         | 53.2 ms                                                         | 55.8 ms: 1.05x slower                                       |
| spectral_norm              | 63.7 ms                                                         | 66.9 ms: 1.05x slower                                       |
| 2to3                       | 207 ms                                                          | 218 ms: 1.05x slower                                        |
| sqlglot_optimize           | 32.7 ms                                                         | 34.5 ms: 1.06x slower                                       |
| pyflate                    | 279 ms                                                          | 295 ms: 1.06x slower                                        |
| django_template            | 21.7 ms                                                         | 22.9 ms: 1.06x slower                                       |
| sympy_integrate            | 12.2 ms                                                         | 13.0 ms: 1.06x slower                                       |
| pathlib                    | 75.9 ms                                                         | 80.5 ms: 1.06x slower                                       |
| richards                   | 26.7 ms                                                         | 28.4 ms: 1.06x slower                                       |
| regex_dna                  | 119 ms                                                          | 126 ms: 1.06x slower                                        |
| nbody                      | 67.6 ms                                                         | 71.9 ms: 1.06x slower                                       |
| richards_super             | 30.2 ms                                                         | 32.1 ms: 1.06x slower                                       |
| crypto_pyaes               | 45.5 ms                                                         | 48.5 ms: 1.07x slower                                       |
| meteor_contest             | 69.9 ms                                                         | 74.6 ms: 1.07x slower                                       |
| bench_mp_pool              | 64.8 ms                                                         | 69.2 ms: 1.07x slower                                       |
| sqlglot_transpile          | 955 us                                                          | 1.02 ms: 1.07x slower                                       |
| async_generators           | 223 ms                                                          | 239 ms: 1.07x slower                                        |
| deepcopy_memo              | 22.1 us                                                         | 23.7 us: 1.07x slower                                       |
| sqlglot_parse              | 748 us                                                          | 804 us: 1.07x slower                                        |
| scimark_fft                | 171 ms                                                          | 184 ms: 1.08x slower                                        |
| logging_format             | 6.22 us                                                         | 6.72 us: 1.08x slower                                       |
| sqlglot_normalize          | 173 ms                                                          | 187 ms: 1.08x slower                                        |
| pprint_pformat             | 966 ms                                                          | 1.05 sec: 1.08x slower                                      |
| pprint_safe_repr           | 474 ms                                                          | 513 ms: 1.08x slower                                        |
| deepcopy                   | 220 us                                                          | 238 us: 1.08x slower                                        |
| sympy_sum                  | 84.4 ms                                                         | 91.5 ms: 1.08x slower                                       |
| logging_simple             | 5.78 us                                                         | 6.28 us: 1.09x slower                                       |
| unpickle_pure_python       | 122 us                                                          | 133 us: 1.09x slower                                        |
| tornado_http               | 81.8 ms                                                         | 89.5 ms: 1.09x slower                                       |
| sympy_str                  | 159 ms                                                          | 175 ms: 1.10x slower                                        |
| hexiom                     | 3.72 ms                                                         | 4.10 ms: 1.10x slower                                       |
| sqlite_synth               | 1.60 us                                                         | 1.76 us: 1.10x slower                                       |
| nqueens                    | 56.7 ms                                                         | 62.8 ms: 1.11x slower                                       |
| pickle_pure_python         | 175 us                                                          | 195 us: 1.11x slower                                        |
| mako                       | 6.36 ms                                                         | 7.09 ms: 1.11x slower                                       |
| bench_thread_pool          | 768 us                                                          | 857 us: 1.12x slower                                        |
| go                         | 82.1 ms                                                         | 91.6 ms: 1.12x slower                                       |
| scimark_monte_carlo        | 39.1 ms                                                         | 43.7 ms: 1.12x slower                                       |
| coroutines                 | 12.8 ms                                                         | 14.3 ms: 1.12x slower                                       |
| regex_compile              | 78.0 ms                                                         | 87.5 ms: 1.12x slower                                       |
| chaos                      | 38.4 ms                                                         | 43.3 ms: 1.13x slower                                       |
| float                      | 49.7 ms                                                         | 56.8 ms: 1.14x slower                                       |
| logging_silent             | 52.9 ns                                                         | 60.5 ns: 1.14x slower                                       |
| deltablue                  | 1.88 ms                                                         | 2.16 ms: 1.15x slower                                       |
| generators                 | 19.6 ms                                                         | 22.5 ms: 1.15x slower                                       |
| dulwich_log                | 38.0 ms                                                         | 44.3 ms: 1.16x slower                                       |
| raytrace                   | 162 ms                                                          | 192 ms: 1.19x slower                                        |
| mypy2                      | 418 ms                                                          | 509 ms: 1.22x slower                                        |
| async_tree_io              | 588 ms                                                          | 731 ms: 1.24x slower                                        |
| async_tree_cpu_io_mixed    | 389 ms                                                          | 489 ms: 1.26x slower                                        |
| async_tree_io_tg           | 605 ms                                                          | 771 ms: 1.27x slower                                        |
| async_tree_memoization     | 264 ms                                                          | 339 ms: 1.28x slower                                        |
| async_tree_cpu_io_mixed_tg | 382 ms                                                          | 502 ms: 1.31x slower                                        |
| async_tree_none            | 218 ms                                                          | 291 ms: 1.34x slower                                        |
| comprehensions             | 10.4 us                                                         | 14.1 us: 1.36x slower                                       |
| async_tree_none_tg         | 202 ms                                                          | 285 ms: 1.41x slower                                        |
| asyncio_tcp_ssl            | 1.48 sec                                                        | 2.10 sec: 1.41x slower                                      |
| async_tree_memoization_tg  | 258 ms                                                          | 367 ms: 1.42x slower                                        |
| Geometric mean             | (ref)                                                           | 1.08x slower                                                |

Benchmark hidden because not significant (2): aiohttp, python_startup_no_site
Ignored benchmarks (6) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17.json: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
Ignored benchmarks (4) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: dask, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.06x
- 95% likely to have a slowdown of 1.06x
- 99% likely to have a slowdown of 1.05x

# Memory
- memory change: unknown