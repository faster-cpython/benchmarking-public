# Results vs. 3.12.0

- fork: gvanrossum
- ref: backoff_counter_woes
- machine: windows-amd64
- commit hash: 4c1049b
- commit date: 2024-05-04
- overall geometric mean: 1.07x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240504-pythonperf1-amd64-gvanrossum-backoff_counter_woes-3.13.0a6+-4c1049b |
|----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 207 ms: 1.05x faster                                                            |
| chameleon      | 4.98 ms                                                     | 4.74 ms: 1.05x faster                                                           |
| docutils       | 1.66 sec                                                    | 1.63 sec: 1.02x faster                                                          |
| tornado_http   | 89.5 ms                                                     | 79.8 ms: 1.12x faster                                                           |
| Geometric mean | (ref)                                                       | 1.06x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240504-pythonperf1-amd64-gvanrossum-backoff_counter_woes-3.13.0a6+-4c1049b |
|----------------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 367 ms                                                      | 259 ms: 1.42x faster                                                            |
| async_tree_none_tg         | 285 ms                                                      | 211 ms: 1.35x faster                                                            |
| async_tree_none            | 291 ms                                                      | 218 ms: 1.34x faster                                                            |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 383 ms: 1.31x faster                                                            |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 384 ms: 1.27x faster                                                            |
| async_tree_memoization     | 339 ms                                                      | 267 ms: 1.27x faster                                                            |
| async_tree_io_tg           | 771 ms                                                      | 611 ms: 1.26x faster                                                            |
| async_tree_io              | 731 ms                                                      | 588 ms: 1.24x faster                                                            |
| Geometric mean             | (ref)                                                       | 1.31x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240504-pythonperf1-amd64-gvanrossum-backoff_counter_woes-3.13.0a6+-4c1049b |
|----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 48.7 ms: 1.17x faster                                                           |
| nbody          | 71.9 ms                                                     | 67.0 ms: 1.07x faster                                                           |
| pidigits       | 152 ms                                                      | 147 ms: 1.03x faster                                                            |
| Geometric mean | (ref)                                                       | 1.09x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240504-pythonperf1-amd64-gvanrossum-backoff_counter_woes-3.13.0a6+-4c1049b |
|----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 87.5 ms                                                     | 78.1 ms: 1.12x faster                                                           |
| regex_dna      | 126 ms                                                      | 118 ms: 1.07x faster                                                            |
| regex_effbot   | 1.62 ms                                                     | 1.59 ms: 1.02x faster                                                           |
| Geometric mean | (ref)                                                       | 1.03x faster                                                                    |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240504-pythonperf1-amd64-gvanrossum-backoff_counter_woes-3.13.0a6+-4c1049b |
|----------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pickle_pure_python   | 195 us                                                      | 174 us: 1.13x faster                                                            |
| xml_etree_iterparse  | 65.2 ms                                                     | 60.8 ms: 1.07x faster                                                           |
| unpickle_pure_python | 133 us                                                      | 124 us: 1.07x faster                                                            |
| xml_etree_generate   | 55.8 ms                                                     | 52.9 ms: 1.06x faster                                                           |
| xml_etree_parse      | 93.0 ms                                                     | 88.2 ms: 1.06x faster                                                           |
| xml_etree_process    | 37.7 ms                                                     | 36.2 ms: 1.04x faster                                                           |
| json_dumps           | 5.70 ms                                                     | 5.57 ms: 1.02x faster                                                           |
| pickle               | 7.43 us                                                     | 7.47 us: 1.00x slower                                                           |
| pickle_dict          | 18.4 us                                                     | 18.9 us: 1.03x slower                                                           |
| pickle_list          | 2.83 us                                                     | 3.28 us: 1.16x slower                                                           |
| Geometric mean       | (ref)                                                       | 1.02x faster                                                                    |

Benchmark hidden because not significant (4): unpickle_list, unpickle, tomli_loads, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240504-pythonperf1-amd64-gvanrossum-backoff_counter_woes-3.13.0a6+-4c1049b |
|----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup | 19.5 ms                                                     | 20.0 ms: 1.03x slower                                                           |
| Geometric mean | (ref)                                                       | 1.02x slower                                                                    |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240504-pythonperf1-amd64-gvanrossum-backoff_counter_woes-3.13.0a6+-4c1049b |
|-----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 6.48 ms: 1.09x faster                                                           |
| django_template | 22.9 ms                                                     | 21.7 ms: 1.06x faster                                                           |
| Geometric mean  | (ref)                                                       | 1.08x faster                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240504-pythonperf1-amd64-gvanrossum-backoff_counter_woes-3.13.0a6+-4c1049b |
|----------------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 367 ms                                                      | 259 ms: 1.42x faster                                                            |
| comprehensions             | 14.1 us                                                     | 10.2 us: 1.39x faster                                                           |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.54 sec: 1.36x faster                                                          |
| async_tree_none_tg         | 285 ms                                                      | 211 ms: 1.35x faster                                                            |
| async_tree_none            | 291 ms                                                      | 218 ms: 1.34x faster                                                            |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 383 ms: 1.31x faster                                                            |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 384 ms: 1.27x faster                                                            |
| async_tree_memoization     | 339 ms                                                      | 267 ms: 1.27x faster                                                            |
| async_tree_io_tg           | 771 ms                                                      | 611 ms: 1.26x faster                                                            |
| async_tree_io              | 731 ms                                                      | 588 ms: 1.24x faster                                                            |
| raytrace                   | 192 ms                                                      | 156 ms: 1.23x faster                                                            |
| mypy2                      | 509 ms                                                      | 420 ms: 1.21x faster                                                            |
| logging_silent             | 60.5 ns                                                     | 50.7 ns: 1.19x faster                                                           |
| generators                 | 22.5 ms                                                     | 19.0 ms: 1.19x faster                                                           |
| float                      | 56.8 ms                                                     | 48.7 ms: 1.17x faster                                                           |
| deltablue                  | 2.16 ms                                                     | 1.89 ms: 1.14x faster                                                           |
| chaos                      | 43.3 ms                                                     | 37.9 ms: 1.14x faster                                                           |
| coroutines                 | 14.3 ms                                                     | 12.6 ms: 1.13x faster                                                           |
| spectral_norm              | 66.9 ms                                                     | 59.3 ms: 1.13x faster                                                           |
| pickle_pure_python         | 195 us                                                      | 174 us: 1.13x faster                                                            |
| tornado_http               | 89.5 ms                                                     | 79.8 ms: 1.12x faster                                                           |
| regex_compile              | 87.5 ms                                                     | 78.1 ms: 1.12x faster                                                           |
| nqueens                    | 62.8 ms                                                     | 56.8 ms: 1.11x faster                                                           |
| scimark_monte_carlo        | 43.7 ms                                                     | 39.7 ms: 1.10x faster                                                           |
| dulwich_log                | 44.3 ms                                                     | 40.2 ms: 1.10x faster                                                           |
| deepcopy                   | 238 us                                                      | 217 us: 1.10x faster                                                            |
| mako                       | 7.09 ms                                                     | 6.48 ms: 1.09x faster                                                           |
| sympy_str                  | 175 ms                                                      | 161 ms: 1.09x faster                                                            |
| logging_simple             | 6.28 us                                                     | 5.76 us: 1.09x faster                                                           |
| logging_format             | 6.72 us                                                     | 6.17 us: 1.09x faster                                                           |
| sqlglot_normalize          | 187 ms                                                      | 172 ms: 1.09x faster                                                            |
| go                         | 91.6 ms                                                     | 84.5 ms: 1.08x faster                                                           |
| sqlite_synth               | 1.76 us                                                     | 1.63 us: 1.08x faster                                                           |
| scimark_lu                 | 58.9 ms                                                     | 54.4 ms: 1.08x faster                                                           |
| deepcopy_memo              | 23.7 us                                                     | 21.9 us: 1.08x faster                                                           |
| richards_super             | 32.1 ms                                                     | 29.7 ms: 1.08x faster                                                           |
| sympy_sum                  | 91.5 ms                                                     | 84.9 ms: 1.08x faster                                                           |
| hexiom                     | 4.10 ms                                                     | 3.81 ms: 1.08x faster                                                           |
| richards                   | 28.4 ms                                                     | 26.4 ms: 1.08x faster                                                           |
| pprint_safe_repr           | 513 ms                                                      | 478 ms: 1.07x faster                                                            |
| bench_mp_pool              | 69.2 ms                                                     | 64.5 ms: 1.07x faster                                                           |
| nbody                      | 71.9 ms                                                     | 67.0 ms: 1.07x faster                                                           |
| xml_etree_iterparse        | 65.2 ms                                                     | 60.8 ms: 1.07x faster                                                           |
| pprint_pformat             | 1.05 sec                                                    | 975 ms: 1.07x faster                                                            |
| unpickle_pure_python       | 133 us                                                      | 124 us: 1.07x faster                                                            |
| bench_thread_pool          | 857 us                                                      | 801 us: 1.07x faster                                                            |
| regex_dna                  | 126 ms                                                      | 118 ms: 1.07x faster                                                            |
| deepcopy_reduce            | 2.09 us                                                     | 1.97 us: 1.06x faster                                                           |
| sqlglot_parse              | 804 us                                                      | 757 us: 1.06x faster                                                            |
| sqlglot_transpile          | 1.02 ms                                                     | 963 us: 1.06x faster                                                            |
| sqlglot_optimize           | 34.5 ms                                                     | 32.6 ms: 1.06x faster                                                           |
| django_template            | 22.9 ms                                                     | 21.7 ms: 1.06x faster                                                           |
| xml_etree_generate         | 55.8 ms                                                     | 52.9 ms: 1.06x faster                                                           |
| xml_etree_parse            | 93.0 ms                                                     | 88.2 ms: 1.06x faster                                                           |
| meteor_contest             | 74.6 ms                                                     | 70.9 ms: 1.05x faster                                                           |
| scimark_fft                | 184 ms                                                      | 175 ms: 1.05x faster                                                            |
| 2to3                       | 218 ms                                                      | 207 ms: 1.05x faster                                                            |
| sympy_integrate            | 13.0 ms                                                     | 12.3 ms: 1.05x faster                                                           |
| chameleon                  | 4.98 ms                                                     | 4.74 ms: 1.05x faster                                                           |
| async_generators           | 239 ms                                                      | 228 ms: 1.05x faster                                                            |
| pyflate                    | 295 ms                                                      | 281 ms: 1.05x faster                                                            |
| mdp                        | 1.37 sec                                                    | 1.31 sec: 1.05x faster                                                          |
| xml_etree_process          | 37.7 ms                                                     | 36.2 ms: 1.04x faster                                                           |
| sympy_expand               | 284 ms                                                      | 273 ms: 1.04x faster                                                            |
| scimark_sor                | 78.8 ms                                                     | 76.0 ms: 1.04x faster                                                           |
| asyncio_tcp                | 487 ms                                                      | 471 ms: 1.04x faster                                                            |
| pidigits                   | 152 ms                                                      | 147 ms: 1.03x faster                                                            |
| crypto_pyaes               | 48.5 ms                                                     | 46.9 ms: 1.03x faster                                                           |
| json_dumps                 | 5.70 ms                                                     | 5.57 ms: 1.02x faster                                                           |
| pathlib                    | 80.5 ms                                                     | 78.7 ms: 1.02x faster                                                           |
| regex_effbot               | 1.62 ms                                                     | 1.59 ms: 1.02x faster                                                           |
| docutils                   | 1.66 sec                                                    | 1.63 sec: 1.02x faster                                                          |
| fannkuch                   | 247 ms                                                      | 245 ms: 1.01x faster                                                            |
| pickle                     | 7.43 us                                                     | 7.47 us: 1.00x slower                                                           |
| aiohttp                    | 884 us                                                      | 896 us: 1.01x slower                                                            |
| gc_traversal               | 1.52 ms                                                     | 1.55 ms: 1.02x slower                                                           |
| pickle_dict                | 18.4 us                                                     | 18.9 us: 1.03x slower                                                           |
| python_startup             | 19.5 ms                                                     | 20.0 ms: 1.03x slower                                                           |
| typing_runtime_protocols   | 95.1 us                                                     | 99.5 us: 1.05x slower                                                           |
| pycparser                  | 699 ms                                                      | 749 ms: 1.07x slower                                                            |
| coverage                   | 40.8 ms                                                     | 44.6 ms: 1.09x slower                                                           |
| pickle_list                | 2.83 us                                                     | 3.28 us: 1.16x slower                                                           |
| telco                      | 4.13 ms                                                     | 4.82 ms: 1.17x slower                                                           |
| dask                       | 263 ms                                                      | 309 ms: 1.18x slower                                                            |
| create_gc_cycles           | 752 us                                                      | 898 us: 1.19x slower                                                            |
| Geometric mean             | (ref)                                                       | 1.07x faster                                                                    |

Benchmark hidden because not significant (8): unpickle_list, unpickle, scimark_sparse_mat_mult, tomli_loads, python_startup_no_site, json_loads, json, regex_v8
Ignored benchmarks (3) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (6) of results/bm-20240504-3.13.0a6+-4c1049b/bm-20240504-pythonperf1-amd64-gvanrossum-backoff_counter_woes-3.13.0a6+-4c1049b.json: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.05x

# Memory
- memory change: unknown