
# Results vs. 3.12.0

- fork: python
- ref: v3.13.0a1
- machine: windows-amd64
- commit hash: ad056f0
- commit date: 2023-10-13
- overall geometric mean: 1.01x faster \*
- HPT reliability: 99.92%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20231013-pythonperf1-amd64-python-v3.13.0a1-3.13.0a1-ad056f0 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 216 ms: 1.01x faster                                            |
| docutils       | 1.66 sec                                                    | 1.61 sec: 1.03x faster                                          |
| Geometric mean | (ref)                                                       | 1.01x faster                                                    |

Benchmark hidden because not significant (2): chameleon, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20231013-pythonperf1-amd64-python-v3.13.0a1-3.13.0a1-ad056f0 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| async_tree_none            | 291 ms                                                      | 267 ms: 1.09x faster                                            |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 455 ms: 1.07x faster                                            |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 486 ms: 1.03x faster                                            |
| async_tree_memoization_tg  | 367 ms                                                      | 359 ms: 1.02x faster                                            |
| Geometric mean             | (ref)                                                       | 1.03x faster                                                    |

Benchmark hidden because not significant (4): async_tree_io, async_tree_none_tg, async_tree_io_tg, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20231013-pythonperf1-amd64-python-v3.13.0a1-3.13.0a1-ad056f0 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 53.6 ms: 1.06x faster                                           |
| pidigits       | 152 ms                                                      | 150 ms: 1.01x faster                                            |
| Geometric mean | (ref)                                                       | 1.02x faster                                                    |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20231013-pythonperf1-amd64-python-v3.13.0a1-3.13.0a1-ad056f0 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_dna      | 126 ms                                                      | 119 ms: 1.06x faster                                            |
| regex_effbot   | 1.62 ms                                                     | 1.60 ms: 1.01x faster                                           |
| regex_compile  | 87.5 ms                                                     | 90.8 ms: 1.04x slower                                           |
| regex_v8       | 14.2 ms                                                     | 14.8 ms: 1.04x slower                                           |
| Geometric mean | (ref)                                                       | 1.00x slower                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20231013-pythonperf1-amd64-python-v3.13.0a1-3.13.0a1-ad056f0 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| pickle               | 7.43 us                                                     | 6.98 us: 1.06x faster                                           |
| pickle_pure_python   | 195 us                                                      | 190 us: 1.03x faster                                            |
| json_loads           | 13.9 us                                                     | 13.5 us: 1.03x faster                                           |
| xml_etree_iterparse  | 65.2 ms                                                     | 64.0 ms: 1.02x faster                                           |
| json_dumps           | 5.70 ms                                                     | 5.60 ms: 1.02x faster                                           |
| xml_etree_parse      | 93.0 ms                                                     | 91.6 ms: 1.02x faster                                           |
| unpickle             | 8.18 us                                                     | 8.12 us: 1.01x faster                                           |
| xml_etree_generate   | 55.8 ms                                                     | 55.4 ms: 1.01x faster                                           |
| unpickle_list        | 2.75 us                                                     | 2.74 us: 1.01x faster                                           |
| xml_etree_process    | 37.7 ms                                                     | 38.2 ms: 1.01x slower                                           |
| unpickle_pure_python | 133 us                                                      | 137 us: 1.03x slower                                            |
| pickle_list          | 2.83 us                                                     | 2.94 us: 1.04x slower                                           |
| tomli_loads          | 1.37 sec                                                    | 1.48 sec: 1.08x slower                                          |
| Geometric mean       | (ref)                                                       | 1.00x faster                                                    |

Benchmark hidden because not significant (1): pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20231013-pythonperf1-amd64-python-v3.13.0a1-3.13.0a1-ad056f0 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup | 19.5 ms                                                     | 19.7 ms: 1.01x slower                                           |
| Geometric mean | (ref)                                                       | 1.00x slower                                                    |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20231013-pythonperf1-amd64-python-v3.13.0a1-3.13.0a1-ad056f0 |
|-----------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| mako      | 7.09 ms                                                     | 7.20 ms: 1.02x slower                                           |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20231013-pythonperf1-amd64-python-v3.13.0a1-3.13.0a1-ad056f0 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| crypto_pyaes               | 48.5 ms                                                     | 43.3 ms: 1.12x faster                                           |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.89 sec: 1.11x faster                                          |
| raytrace                   | 192 ms                                                      | 174 ms: 1.10x faster                                            |
| async_tree_none            | 291 ms                                                      | 267 ms: 1.09x faster                                            |
| bench_mp_pool              | 69.2 ms                                                     | 64.0 ms: 1.08x faster                                           |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 455 ms: 1.07x faster                                            |
| chaos                      | 43.3 ms                                                     | 40.4 ms: 1.07x faster                                           |
| scimark_monte_carlo        | 43.7 ms                                                     | 41.0 ms: 1.07x faster                                           |
| sqlite_synth               | 1.76 us                                                     | 1.65 us: 1.07x faster                                           |
| pickle                     | 7.43 us                                                     | 6.98 us: 1.06x faster                                           |
| regex_dna                  | 126 ms                                                      | 119 ms: 1.06x faster                                            |
| spectral_norm              | 66.9 ms                                                     | 63.0 ms: 1.06x faster                                           |
| nqueens                    | 62.8 ms                                                     | 59.1 ms: 1.06x faster                                           |
| float                      | 56.8 ms                                                     | 53.6 ms: 1.06x faster                                           |
| scimark_fft                | 184 ms                                                      | 176 ms: 1.05x faster                                            |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.45 ms: 1.05x faster                                           |
| asyncio_tcp                | 487 ms                                                      | 470 ms: 1.04x faster                                            |
| deepcopy                   | 238 us                                                      | 230 us: 1.04x faster                                            |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 486 ms: 1.03x faster                                            |
| create_gc_cycles           | 752 us                                                      | 728 us: 1.03x faster                                            |
| pickle_pure_python         | 195 us                                                      | 190 us: 1.03x faster                                            |
| docutils                   | 1.66 sec                                                    | 1.61 sec: 1.03x faster                                          |
| json_loads                 | 13.9 us                                                     | 13.5 us: 1.03x faster                                           |
| gc_traversal               | 1.52 ms                                                     | 1.49 ms: 1.02x faster                                           |
| pathlib                    | 80.5 ms                                                     | 78.5 ms: 1.02x faster                                           |
| bench_thread_pool          | 857 us                                                      | 836 us: 1.02x faster                                            |
| scimark_sor                | 78.8 ms                                                     | 77.0 ms: 1.02x faster                                           |
| async_tree_memoization_tg  | 367 ms                                                      | 359 ms: 1.02x faster                                            |
| sqlglot_normalize          | 187 ms                                                      | 184 ms: 1.02x faster                                            |
| xml_etree_iterparse        | 65.2 ms                                                     | 64.0 ms: 1.02x faster                                           |
| go                         | 91.6 ms                                                     | 90.0 ms: 1.02x faster                                           |
| json_dumps                 | 5.70 ms                                                     | 5.60 ms: 1.02x faster                                           |
| xml_etree_parse            | 93.0 ms                                                     | 91.6 ms: 1.02x faster                                           |
| async_generators           | 239 ms                                                      | 236 ms: 1.02x faster                                            |
| pidigits                   | 152 ms                                                      | 150 ms: 1.01x faster                                            |
| pprint_pformat             | 1.05 sec                                                    | 1.03 sec: 1.01x faster                                          |
| pprint_safe_repr           | 513 ms                                                      | 507 ms: 1.01x faster                                            |
| regex_effbot               | 1.62 ms                                                     | 1.60 ms: 1.01x faster                                           |
| 2to3                       | 218 ms                                                      | 216 ms: 1.01x faster                                            |
| deepcopy_reduce            | 2.09 us                                                     | 2.07 us: 1.01x faster                                           |
| generators                 | 22.5 ms                                                     | 22.3 ms: 1.01x faster                                           |
| unpickle                   | 8.18 us                                                     | 8.12 us: 1.01x faster                                           |
| xml_etree_generate         | 55.8 ms                                                     | 55.4 ms: 1.01x faster                                           |
| unpickle_list              | 2.75 us                                                     | 2.74 us: 1.01x faster                                           |
| sqlglot_transpile          | 1.02 ms                                                     | 1.03 ms: 1.01x slower                                           |
| sqlglot_optimize           | 34.5 ms                                                     | 34.8 ms: 1.01x slower                                           |
| sqlglot_parse              | 804 us                                                      | 811 us: 1.01x slower                                            |
| sympy_expand               | 284 ms                                                      | 287 ms: 1.01x slower                                            |
| python_startup             | 19.5 ms                                                     | 19.7 ms: 1.01x slower                                           |
| fannkuch                   | 247 ms                                                      | 249 ms: 1.01x slower                                            |
| pyflate                    | 295 ms                                                      | 298 ms: 1.01x slower                                            |
| typing_runtime_protocols   | 95.1 us                                                     | 96.3 us: 1.01x slower                                           |
| deltablue                  | 2.16 ms                                                     | 2.19 ms: 1.01x slower                                           |
| xml_etree_process          | 37.7 ms                                                     | 38.2 ms: 1.01x slower                                           |
| logging_format             | 6.72 us                                                     | 6.81 us: 1.01x slower                                           |
| sympy_integrate            | 13.0 ms                                                     | 13.1 ms: 1.01x slower                                           |
| mako                       | 7.09 ms                                                     | 7.20 ms: 1.02x slower                                           |
| richards                   | 28.4 ms                                                     | 28.8 ms: 1.02x slower                                           |
| dulwich_log                | 44.3 ms                                                     | 45.2 ms: 1.02x slower                                           |
| logging_simple             | 6.28 us                                                     | 6.40 us: 1.02x slower                                           |
| unpack_sequence            | 37.5 ns                                                     | 38.5 ns: 1.03x slower                                           |
| coroutines                 | 14.3 ms                                                     | 14.7 ms: 1.03x slower                                           |
| unpickle_pure_python       | 133 us                                                      | 137 us: 1.03x slower                                            |
| regex_compile              | 87.5 ms                                                     | 90.8 ms: 1.04x slower                                           |
| pickle_list                | 2.83 us                                                     | 2.94 us: 1.04x slower                                           |
| regex_v8                   | 14.2 ms                                                     | 14.8 ms: 1.04x slower                                           |
| deepcopy_memo              | 23.7 us                                                     | 24.8 us: 1.04x slower                                           |
| logging_silent             | 60.5 ns                                                     | 63.2 ns: 1.05x slower                                           |
| tomli_loads                | 1.37 sec                                                    | 1.48 sec: 1.08x slower                                          |
| mdp                        | 1.37 sec                                                    | 1.49 sec: 1.09x slower                                          |
| coverage                   | 40.8 ms                                                     | 45.4 ms: 1.11x slower                                           |
| telco                      | 4.13 ms                                                     | 4.73 ms: 1.14x slower                                           |
| pycparser                  | 699 ms                                                      | 861 ms: 1.23x slower                                            |
| Geometric mean             | (ref)                                                       | 1.01x faster                                                    |

Benchmark hidden because not significant (17): json, async_tree_io, tornado_http, sympy_sum, scimark_lu, hexiom, sympy_str, pickle_dict, meteor_contest, async_tree_none_tg, richards_super, python_startup_no_site, chameleon, async_tree_io_tg, comprehensions, async_tree_memoization, nbody
Ignored benchmarks (6) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, dask, django_template, mypy2, sqlalchemy_declarative, sqlalchemy_imperative


# HPT report

- Reliability score: 99.92% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x


# Memory

- memory change: unknown