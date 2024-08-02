# Results vs. 3.12.0

- fork: python
- ref: v3.13.0a4
- machine: windows-amd64
- commit hash: 9d34f60
- commit date: 2024-02-15
- overall geometric mean: 1.04x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240215-pythonperf1-amd64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| chameleon      | 4.98 ms                                                     | 4.74 ms: 1.05x faster                                           |
| docutils       | 1.66 sec                                                    | 1.56 sec: 1.07x faster                                          |
| tornado_http   | 89.5 ms                                                     | 85.5 ms: 1.05x faster                                           |
| Geometric mean | (ref)                                                       | 1.04x faster                                                    |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240215-pythonperf1-amd64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| async_tree_none            | 291 ms                                                      | 266 ms: 1.09x faster                                            |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 455 ms: 1.08x faster                                            |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 472 ms: 1.06x faster                                            |
| async_tree_memoization_tg  | 367 ms                                                      | 350 ms: 1.05x faster                                            |
| async_tree_none_tg         | 285 ms                                                      | 272 ms: 1.05x faster                                            |
| async_tree_io_tg           | 771 ms                                                      | 759 ms: 1.02x faster                                            |
| Geometric mean             | (ref)                                                       | 1.04x faster                                                    |

Benchmark hidden because not significant (2): async_tree_io, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240215-pythonperf1-amd64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| nbody          | 71.9 ms                                                     | 61.0 ms: 1.18x faster                                           |
| float          | 56.8 ms                                                     | 51.4 ms: 1.11x faster                                           |
| pidigits       | 152 ms                                                      | 151 ms: 1.01x faster                                            |
| Geometric mean | (ref)                                                       | 1.09x faster                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240215-pythonperf1-amd64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_compile  | 87.5 ms                                                     | 79.3 ms: 1.10x faster                                           |
| regex_dna      | 126 ms                                                      | 118 ms: 1.07x faster                                            |
| regex_effbot   | 1.62 ms                                                     | 1.56 ms: 1.04x faster                                           |
| Geometric mean | (ref)                                                       | 1.05x faster                                                    |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240215-pythonperf1-amd64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| pickle_pure_python   | 195 us                                                      | 174 us: 1.13x faster                                            |
| xml_etree_generate   | 55.8 ms                                                     | 51.9 ms: 1.08x faster                                           |
| unpickle_pure_python | 133 us                                                      | 126 us: 1.05x faster                                            |
| tomli_loads          | 1.37 sec                                                    | 1.30 sec: 1.05x faster                                          |
| xml_etree_process    | 37.7 ms                                                     | 35.9 ms: 1.05x faster                                           |
| pickle_dict          | 18.4 us                                                     | 17.6 us: 1.05x faster                                           |
| xml_etree_iterparse  | 65.2 ms                                                     | 62.9 ms: 1.04x faster                                           |
| json_dumps           | 5.70 ms                                                     | 5.54 ms: 1.03x faster                                           |
| xml_etree_parse      | 93.0 ms                                                     | 91.2 ms: 1.02x faster                                           |
| pickle_list          | 2.83 us                                                     | 2.78 us: 1.02x faster                                           |
| pickle               | 7.43 us                                                     | 7.32 us: 1.02x faster                                           |
| json_loads           | 13.9 us                                                     | 13.8 us: 1.01x faster                                           |
| unpickle             | 8.18 us                                                     | 8.41 us: 1.03x slower                                           |
| Geometric mean       | (ref)                                                       | 1.04x faster                                                    |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240215-pythonperf1-amd64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup         | 19.5 ms                                                     | 20.5 ms: 1.05x slower                                           |
| python_startup_no_site | 16.2 ms                                                     | 18.5 ms: 1.14x slower                                           |
| Geometric mean         | (ref)                                                       | 1.10x slower                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240215-pythonperf1-amd64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|-----------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| mako      | 7.09 ms                                                     | 6.71 ms: 1.06x faster                                           |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240215-pythonperf1-amd64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| typing_runtime_protocols   | 95.1 us                                                     | 69.7 us: 1.37x faster                                           |
| comprehensions             | 14.1 us                                                     | 10.6 us: 1.33x faster                                           |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.70 sec: 1.23x faster                                          |
| mypy2                      | 509 ms                                                      | 423 ms: 1.20x faster                                            |
| nbody                      | 71.9 ms                                                     | 61.0 ms: 1.18x faster                                           |
| sqlite_synth               | 1.76 us                                                     | 1.51 us: 1.16x faster                                           |
| raytrace                   | 192 ms                                                      | 166 ms: 1.16x faster                                            |
| richards                   | 28.4 ms                                                     | 24.8 ms: 1.14x faster                                           |
| richards_super             | 32.1 ms                                                     | 28.2 ms: 1.14x faster                                           |
| generators                 | 22.5 ms                                                     | 19.9 ms: 1.13x faster                                           |
| pickle_pure_python         | 195 us                                                      | 174 us: 1.13x faster                                            |
| logging_silent             | 60.5 ns                                                     | 54.0 ns: 1.12x faster                                           |
| deepcopy_memo              | 23.7 us                                                     | 21.3 us: 1.11x faster                                           |
| float                      | 56.8 ms                                                     | 51.4 ms: 1.11x faster                                           |
| regex_compile              | 87.5 ms                                                     | 79.3 ms: 1.10x faster                                           |
| dulwich_log                | 44.3 ms                                                     | 40.4 ms: 1.10x faster                                           |
| deepcopy                   | 238 us                                                      | 217 us: 1.10x faster                                            |
| async_tree_none            | 291 ms                                                      | 266 ms: 1.09x faster                                            |
| deepcopy_reduce            | 2.09 us                                                     | 1.92 us: 1.09x faster                                           |
| deltablue                  | 2.16 ms                                                     | 1.99 ms: 1.09x faster                                           |
| coroutines                 | 14.3 ms                                                     | 13.2 ms: 1.08x faster                                           |
| sqlglot_normalize          | 187 ms                                                      | 173 ms: 1.08x faster                                            |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 455 ms: 1.08x faster                                            |
| xml_etree_generate         | 55.8 ms                                                     | 51.9 ms: 1.08x faster                                           |
| sympy_str                  | 175 ms                                                      | 163 ms: 1.07x faster                                            |
| regex_dna                  | 126 ms                                                      | 118 ms: 1.07x faster                                            |
| pprint_safe_repr           | 513 ms                                                      | 480 ms: 1.07x faster                                            |
| pathlib                    | 80.5 ms                                                     | 75.3 ms: 1.07x faster                                           |
| docutils                   | 1.66 sec                                                    | 1.56 sec: 1.07x faster                                          |
| pprint_pformat             | 1.05 sec                                                    | 980 ms: 1.07x faster                                            |
| sqlglot_parse              | 804 us                                                      | 755 us: 1.07x faster                                            |
| scimark_lu                 | 58.9 ms                                                     | 55.3 ms: 1.06x faster                                           |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 472 ms: 1.06x faster                                            |
| crypto_pyaes               | 48.5 ms                                                     | 45.8 ms: 1.06x faster                                           |
| spectral_norm              | 66.9 ms                                                     | 63.3 ms: 1.06x faster                                           |
| mako                       | 7.09 ms                                                     | 6.71 ms: 1.06x faster                                           |
| unpickle_pure_python       | 133 us                                                      | 126 us: 1.05x faster                                            |
| logging_simple             | 6.28 us                                                     | 5.95 us: 1.05x faster                                           |
| sympy_sum                  | 91.5 ms                                                     | 86.8 ms: 1.05x faster                                           |
| tomli_loads                | 1.37 sec                                                    | 1.30 sec: 1.05x faster                                          |
| xml_etree_process          | 37.7 ms                                                     | 35.9 ms: 1.05x faster                                           |
| nqueens                    | 62.8 ms                                                     | 59.7 ms: 1.05x faster                                           |
| logging_format             | 6.72 us                                                     | 6.39 us: 1.05x faster                                           |
| chameleon                  | 4.98 ms                                                     | 4.74 ms: 1.05x faster                                           |
| async_tree_memoization_tg  | 367 ms                                                      | 350 ms: 1.05x faster                                            |
| bench_thread_pool          | 857 us                                                      | 817 us: 1.05x faster                                            |
| tornado_http               | 89.5 ms                                                     | 85.5 ms: 1.05x faster                                           |
| pickle_dict                | 18.4 us                                                     | 17.6 us: 1.05x faster                                           |
| async_tree_none_tg         | 285 ms                                                      | 272 ms: 1.05x faster                                            |
| sqlglot_transpile          | 1.02 ms                                                     | 978 us: 1.04x faster                                            |
| bench_mp_pool              | 69.2 ms                                                     | 66.6 ms: 1.04x faster                                           |
| chaos                      | 43.3 ms                                                     | 41.7 ms: 1.04x faster                                           |
| regex_effbot               | 1.62 ms                                                     | 1.56 ms: 1.04x faster                                           |
| scimark_sor                | 78.8 ms                                                     | 76.0 ms: 1.04x faster                                           |
| xml_etree_iterparse        | 65.2 ms                                                     | 62.9 ms: 1.04x faster                                           |
| sqlglot_optimize           | 34.5 ms                                                     | 33.5 ms: 1.03x faster                                           |
| json_dumps                 | 5.70 ms                                                     | 5.54 ms: 1.03x faster                                           |
| sympy_expand               | 284 ms                                                      | 277 ms: 1.02x faster                                            |
| create_gc_cycles           | 752 us                                                      | 736 us: 1.02x faster                                            |
| xml_etree_parse            | 93.0 ms                                                     | 91.2 ms: 1.02x faster                                           |
| fannkuch                   | 247 ms                                                      | 242 ms: 1.02x faster                                            |
| async_tree_io_tg           | 771 ms                                                      | 759 ms: 1.02x faster                                            |
| pickle_list                | 2.83 us                                                     | 2.78 us: 1.02x faster                                           |
| pickle                     | 7.43 us                                                     | 7.32 us: 1.02x faster                                           |
| gc_traversal               | 1.52 ms                                                     | 1.51 ms: 1.01x faster                                           |
| sympy_integrate            | 13.0 ms                                                     | 12.8 ms: 1.01x faster                                           |
| pidigits                   | 152 ms                                                      | 151 ms: 1.01x faster                                            |
| async_generators           | 239 ms                                                      | 238 ms: 1.01x faster                                            |
| json_loads                 | 13.9 us                                                     | 13.8 us: 1.01x faster                                           |
| scimark_fft                | 184 ms                                                      | 189 ms: 1.02x slower                                            |
| meteor_contest             | 74.6 ms                                                     | 76.7 ms: 1.03x slower                                           |
| unpickle                   | 8.18 us                                                     | 8.41 us: 1.03x slower                                           |
| go                         | 91.6 ms                                                     | 94.8 ms: 1.03x slower                                           |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.65 ms: 1.04x slower                                           |
| pyflate                    | 295 ms                                                      | 308 ms: 1.05x slower                                            |
| python_startup             | 19.5 ms                                                     | 20.5 ms: 1.05x slower                                           |
| unpack_sequence            | 37.5 ns                                                     | 40.0 ns: 1.07x slower                                           |
| pycparser                  | 699 ms                                                      | 748 ms: 1.07x slower                                            |
| mdp                        | 1.37 sec                                                    | 1.49 sec: 1.08x slower                                          |
| telco                      | 4.13 ms                                                     | 4.57 ms: 1.11x slower                                           |
| python_startup_no_site     | 16.2 ms                                                     | 18.5 ms: 1.14x slower                                           |
| coverage                   | 40.8 ms                                                     | 48.4 ms: 1.19x slower                                           |
| hexiom                     | 4.10 ms                                                     | 5.14 ms: 1.25x slower                                           |
| scimark_monte_carlo        | 43.7 ms                                                     | 56.9 ms: 1.30x slower                                           |
| dask                       | 263 ms                                                      | 360 ms: 1.37x slower                                            |
| Geometric mean             | (ref)                                                       | 1.04x faster                                                    |

Benchmark hidden because not significant (7): asyncio_tcp, async_tree_io, json, 2to3, unpickle_list, regex_v8, async_tree_memoization
Ignored benchmarks (4) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, django_template, sqlalchemy_declarative, sqlalchemy_imperative


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x


# Memory

- memory change: unknown