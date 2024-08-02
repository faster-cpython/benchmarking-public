# Results vs. 3.12.0

- fork: python
- ref: v3.13.0b1
- machine: windows-amd64
- commit hash: 2268289
- commit date: 2024-05-08
- overall geometric mean: 1.07x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240508-pythonperf1-amd64-python-v3.13.0b1-3.13.0b1-2268289 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 212 ms: 1.03x faster                                            |
| chameleon      | 4.98 ms                                                     | 4.75 ms: 1.05x faster                                           |
| docutils       | 1.66 sec                                                    | 1.64 sec: 1.02x faster                                          |
| tornado_http   | 89.5 ms                                                     | 82.5 ms: 1.09x faster                                           |
| Geometric mean | (ref)                                                       | 1.04x faster                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240508-pythonperf1-amd64-python-v3.13.0b1-3.13.0b1-2268289 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| async_tree_memoization_tg  | 367 ms                                                      | 267 ms: 1.37x faster                                            |
| async_tree_none_tg         | 285 ms                                                      | 213 ms: 1.34x faster                                            |
| async_tree_none            | 291 ms                                                      | 219 ms: 1.33x faster                                            |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 383 ms: 1.31x faster                                            |
| async_tree_io_tg           | 771 ms                                                      | 604 ms: 1.28x faster                                            |
| async_tree_memoization     | 339 ms                                                      | 266 ms: 1.28x faster                                            |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 385 ms: 1.27x faster                                            |
| async_tree_io              | 731 ms                                                      | 582 ms: 1.26x faster                                            |
| Geometric mean             | (ref)                                                       | 1.30x faster                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240508-pythonperf1-amd64-python-v3.13.0b1-3.13.0b1-2268289 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 48.5 ms: 1.17x faster                                           |
| nbody          | 71.9 ms                                                     | 67.1 ms: 1.07x faster                                           |
| pidigits       | 152 ms                                                      | 147 ms: 1.04x faster                                            |
| Geometric mean | (ref)                                                       | 1.09x faster                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240508-pythonperf1-amd64-python-v3.13.0b1-3.13.0b1-2268289 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_compile  | 87.5 ms                                                     | 78.5 ms: 1.12x faster                                           |
| regex_dna      | 126 ms                                                      | 118 ms: 1.08x faster                                            |
| regex_effbot   | 1.62 ms                                                     | 1.58 ms: 1.03x faster                                           |
| regex_v8       | 14.2 ms                                                     | 14.3 ms: 1.01x slower                                           |
| Geometric mean | (ref)                                                       | 1.05x faster                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240508-pythonperf1-amd64-python-v3.13.0b1-3.13.0b1-2268289 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| pickle_pure_python   | 195 us                                                      | 177 us: 1.11x faster                                            |
| xml_etree_iterparse  | 65.2 ms                                                     | 61.9 ms: 1.05x faster                                           |
| unpickle_pure_python | 133 us                                                      | 127 us: 1.05x faster                                            |
| xml_etree_generate   | 55.8 ms                                                     | 53.7 ms: 1.04x faster                                           |
| pickle               | 7.43 us                                                     | 7.17 us: 1.04x faster                                           |
| xml_etree_parse      | 93.0 ms                                                     | 90.0 ms: 1.03x faster                                           |
| xml_etree_process    | 37.7 ms                                                     | 36.8 ms: 1.02x faster                                           |
| json_dumps           | 5.70 ms                                                     | 5.59 ms: 1.02x faster                                           |
| json_loads           | 13.9 us                                                     | 13.7 us: 1.01x faster                                           |
| unpickle_list        | 2.75 us                                                     | 2.77 us: 1.01x slower                                           |
| unpickle             | 8.18 us                                                     | 8.44 us: 1.03x slower                                           |
| pickle_list          | 2.83 us                                                     | 3.02 us: 1.07x slower                                           |
| Geometric mean       | (ref)                                                       | 1.02x faster                                                    |

Benchmark hidden because not significant (2): pickle_dict, tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240508-pythonperf1-amd64-python-v3.13.0b1-3.13.0b1-2268289 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 16.5 ms: 1.01x slower                                           |
| python_startup         | 19.5 ms                                                     | 20.4 ms: 1.05x slower                                           |
| Geometric mean         | (ref)                                                       | 1.03x slower                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240508-pythonperf1-amd64-python-v3.13.0b1-3.13.0b1-2268289 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 6.28 ms: 1.13x faster                                           |
| django_template | 22.9 ms                                                     | 21.5 ms: 1.07x faster                                           |
| Geometric mean  | (ref)                                                       | 1.10x faster                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240508-pythonperf1-amd64-python-v3.13.0b1-3.13.0b1-2268289 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.51 sec: 1.39x faster                                          |
| comprehensions             | 14.1 us                                                     | 10.2 us: 1.38x faster                                           |
| async_tree_memoization_tg  | 367 ms                                                      | 267 ms: 1.37x faster                                            |
| async_tree_none_tg         | 285 ms                                                      | 213 ms: 1.34x faster                                            |
| async_tree_none            | 291 ms                                                      | 219 ms: 1.33x faster                                            |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 383 ms: 1.31x faster                                            |
| async_tree_io_tg           | 771 ms                                                      | 604 ms: 1.28x faster                                            |
| async_tree_memoization     | 339 ms                                                      | 266 ms: 1.28x faster                                            |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 385 ms: 1.27x faster                                            |
| async_tree_io              | 731 ms                                                      | 582 ms: 1.26x faster                                            |
| raytrace                   | 192 ms                                                      | 154 ms: 1.25x faster                                            |
| generators                 | 22.5 ms                                                     | 18.6 ms: 1.21x faster                                           |
| mypy2                      | 509 ms                                                      | 427 ms: 1.19x faster                                            |
| float                      | 56.8 ms                                                     | 48.5 ms: 1.17x faster                                           |
| logging_silent             | 60.5 ns                                                     | 51.7 ns: 1.17x faster                                           |
| deltablue                  | 2.16 ms                                                     | 1.90 ms: 1.14x faster                                           |
| chaos                      | 43.3 ms                                                     | 38.3 ms: 1.13x faster                                           |
| mako                       | 7.09 ms                                                     | 6.28 ms: 1.13x faster                                           |
| coroutines                 | 14.3 ms                                                     | 12.6 ms: 1.13x faster                                           |
| nqueens                    | 62.8 ms                                                     | 56.2 ms: 1.12x faster                                           |
| dulwich_log                | 44.3 ms                                                     | 39.6 ms: 1.12x faster                                           |
| regex_compile              | 87.5 ms                                                     | 78.5 ms: 1.12x faster                                           |
| pickle_pure_python         | 195 us                                                      | 177 us: 1.11x faster                                            |
| hexiom                     | 4.10 ms                                                     | 3.76 ms: 1.09x faster                                           |
| go                         | 91.6 ms                                                     | 84.3 ms: 1.09x faster                                           |
| sqlglot_normalize          | 187 ms                                                      | 172 ms: 1.09x faster                                            |
| tornado_http               | 89.5 ms                                                     | 82.5 ms: 1.09x faster                                           |
| sqlite_synth               | 1.76 us                                                     | 1.62 us: 1.08x faster                                           |
| logging_simple             | 6.28 us                                                     | 5.80 us: 1.08x faster                                           |
| spectral_norm              | 66.9 ms                                                     | 61.9 ms: 1.08x faster                                           |
| bench_thread_pool          | 857 us                                                      | 793 us: 1.08x faster                                            |
| logging_format             | 6.72 us                                                     | 6.22 us: 1.08x faster                                           |
| sympy_str                  | 175 ms                                                      | 162 ms: 1.08x faster                                            |
| scimark_monte_carlo        | 43.7 ms                                                     | 40.5 ms: 1.08x faster                                           |
| regex_dna                  | 126 ms                                                      | 118 ms: 1.08x faster                                            |
| sympy_sum                  | 91.5 ms                                                     | 85.2 ms: 1.07x faster                                           |
| richards_super             | 32.1 ms                                                     | 29.9 ms: 1.07x faster                                           |
| nbody                      | 71.9 ms                                                     | 67.1 ms: 1.07x faster                                           |
| richards                   | 28.4 ms                                                     | 26.6 ms: 1.07x faster                                           |
| django_template            | 22.9 ms                                                     | 21.5 ms: 1.07x faster                                           |
| pprint_safe_repr           | 513 ms                                                      | 481 ms: 1.07x faster                                            |
| deepcopy                   | 238 us                                                      | 223 us: 1.07x faster                                            |
| async_generators           | 239 ms                                                      | 225 ms: 1.07x faster                                            |
| sqlglot_parse              | 804 us                                                      | 754 us: 1.07x faster                                            |
| pprint_pformat             | 1.05 sec                                                    | 982 ms: 1.06x faster                                            |
| sqlglot_transpile          | 1.02 ms                                                     | 962 us: 1.06x faster                                            |
| bench_mp_pool              | 69.2 ms                                                     | 65.3 ms: 1.06x faster                                           |
| deepcopy_reduce            | 2.09 us                                                     | 1.98 us: 1.06x faster                                           |
| scimark_fft                | 184 ms                                                      | 175 ms: 1.06x faster                                            |
| xml_etree_iterparse        | 65.2 ms                                                     | 61.9 ms: 1.05x faster                                           |
| unpickle_pure_python       | 133 us                                                      | 127 us: 1.05x faster                                            |
| pyflate                    | 295 ms                                                      | 280 ms: 1.05x faster                                            |
| sqlglot_optimize           | 34.5 ms                                                     | 32.9 ms: 1.05x faster                                           |
| chameleon                  | 4.98 ms                                                     | 4.75 ms: 1.05x faster                                           |
| meteor_contest             | 74.6 ms                                                     | 71.3 ms: 1.05x faster                                           |
| mdp                        | 1.37 sec                                                    | 1.31 sec: 1.05x faster                                          |
| pycparser                  | 699 ms                                                      | 669 ms: 1.04x faster                                            |
| json                       | 3.05 ms                                                     | 2.93 ms: 1.04x faster                                           |
| xml_etree_generate         | 55.8 ms                                                     | 53.7 ms: 1.04x faster                                           |
| pidigits                   | 152 ms                                                      | 147 ms: 1.04x faster                                            |
| sympy_integrate            | 13.0 ms                                                     | 12.5 ms: 1.04x faster                                           |
| scimark_sor                | 78.8 ms                                                     | 75.9 ms: 1.04x faster                                           |
| scimark_lu                 | 58.9 ms                                                     | 56.8 ms: 1.04x faster                                           |
| pickle                     | 7.43 us                                                     | 7.17 us: 1.04x faster                                           |
| crypto_pyaes               | 48.5 ms                                                     | 46.9 ms: 1.03x faster                                           |
| xml_etree_parse            | 93.0 ms                                                     | 90.0 ms: 1.03x faster                                           |
| sympy_expand               | 284 ms                                                      | 275 ms: 1.03x faster                                            |
| 2to3                       | 218 ms                                                      | 212 ms: 1.03x faster                                            |
| regex_effbot               | 1.62 ms                                                     | 1.58 ms: 1.03x faster                                           |
| deepcopy_memo              | 23.7 us                                                     | 23.1 us: 1.03x faster                                           |
| xml_etree_process          | 37.7 ms                                                     | 36.8 ms: 1.02x faster                                           |
| json_dumps                 | 5.70 ms                                                     | 5.59 ms: 1.02x faster                                           |
| docutils                   | 1.66 sec                                                    | 1.64 sec: 1.02x faster                                          |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.53 ms: 1.01x faster                                           |
| json_loads                 | 13.9 us                                                     | 13.7 us: 1.01x faster                                           |
| fannkuch                   | 247 ms                                                      | 244 ms: 1.01x faster                                            |
| regex_v8                   | 14.2 ms                                                     | 14.3 ms: 1.01x slower                                           |
| unpickle_list              | 2.75 us                                                     | 2.77 us: 1.01x slower                                           |
| python_startup_no_site     | 16.2 ms                                                     | 16.5 ms: 1.01x slower                                           |
| gc_traversal               | 1.52 ms                                                     | 1.55 ms: 1.02x slower                                           |
| aiohttp                    | 884 us                                                      | 908 us: 1.03x slower                                            |
| unpickle                   | 8.18 us                                                     | 8.44 us: 1.03x slower                                           |
| python_startup             | 19.5 ms                                                     | 20.4 ms: 1.05x slower                                           |
| pickle_list                | 2.83 us                                                     | 3.02 us: 1.07x slower                                           |
| typing_runtime_protocols   | 95.1 us                                                     | 103 us: 1.08x slower                                            |
| coverage                   | 40.8 ms                                                     | 45.3 ms: 1.11x slower                                           |
| telco                      | 4.13 ms                                                     | 4.72 ms: 1.14x slower                                           |
| create_gc_cycles           | 752 us                                                      | 893 us: 1.19x slower                                            |
| dask                       | 263 ms                                                      | 316 ms: 1.20x slower                                            |
| Geometric mean             | (ref)                                                       | 1.07x faster                                                    |

Benchmark hidden because not significant (4): asyncio_tcp, pathlib, pickle_dict, tomli_loads
Ignored benchmarks (3) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (6) of results/bm-20240508-3.13.0b1-2268289/bm-20240508-pythonperf1-amd64-python-v3.13.0b1-3.13.0b1-2268289.json: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: unknown