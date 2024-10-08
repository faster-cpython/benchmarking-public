# Results vs. 3.12.0

- fork: python
- ref: v3.13.0a4
- machine: windows-amd64
- commit hash: 9d34f60
- commit date: 2024-02-15
- overall geometric mean: 1.04x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240215-pythonperf1-amd64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 214 ms: 1.02x faster                                            |
| docutils       | 1.66 sec                                                    | 1.55 sec: 1.07x faster                                          |
| tornado_http   | 89.5 ms                                                     | 84.3 ms: 1.06x faster                                           |
| Geometric mean | (ref)                                                       | 1.04x faster                                                    |

Benchmark hidden because not significant (1): chameleon

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240215-pythonperf1-amd64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| async_tree_none            | 291 ms                                                      | 266 ms: 1.10x faster                                            |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 453 ms: 1.08x faster                                            |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 472 ms: 1.06x faster                                            |
| async_tree_memoization_tg  | 367 ms                                                      | 349 ms: 1.05x faster                                            |
| async_tree_none_tg         | 285 ms                                                      | 274 ms: 1.04x faster                                            |
| async_tree_io_tg           | 771 ms                                                      | 758 ms: 1.02x faster                                            |
| Geometric mean             | (ref)                                                       | 1.04x faster                                                    |

Benchmark hidden because not significant (2): async_tree_io, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240215-pythonperf1-amd64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 51.0 ms: 1.11x faster                                           |
| pidigits       | 152 ms                                                      | 148 ms: 1.03x faster                                            |
| nbody          | 71.9 ms                                                     | 73.2 ms: 1.02x slower                                           |
| Geometric mean | (ref)                                                       | 1.04x faster                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240215-pythonperf1-amd64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_compile  | 87.5 ms                                                     | 77.8 ms: 1.12x faster                                           |
| regex_dna      | 126 ms                                                      | 115 ms: 1.10x faster                                            |
| regex_effbot   | 1.62 ms                                                     | 1.56 ms: 1.03x faster                                           |
| regex_v8       | 14.2 ms                                                     | 14.4 ms: 1.01x slower                                           |
| Geometric mean | (ref)                                                       | 1.06x faster                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240215-pythonperf1-amd64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| pickle_pure_python   | 195 us                                                      | 186 us: 1.05x faster                                            |
| unpickle_pure_python | 133 us                                                      | 129 us: 1.03x faster                                            |
| unpickle_list        | 2.75 us                                                     | 2.68 us: 1.03x faster                                           |
| xml_etree_generate   | 55.8 ms                                                     | 54.5 ms: 1.02x faster                                           |
| json_dumps           | 5.70 ms                                                     | 5.58 ms: 1.02x faster                                           |
| xml_etree_process    | 37.7 ms                                                     | 37.1 ms: 1.02x faster                                           |
| json_loads           | 13.9 us                                                     | 13.7 us: 1.02x faster                                           |
| pickle               | 7.43 us                                                     | 7.32 us: 1.02x faster                                           |
| xml_etree_parse      | 93.0 ms                                                     | 92.2 ms: 1.01x faster                                           |
| tomli_loads          | 1.37 sec                                                    | 1.43 sec: 1.04x slower                                          |
| pickle_list          | 2.83 us                                                     | 2.96 us: 1.05x slower                                           |
| unpickle             | 8.18 us                                                     | 8.66 us: 1.06x slower                                           |
| Geometric mean       | (ref)                                                       | 1.00x faster                                                    |

Benchmark hidden because not significant (2): pickle_dict, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240215-pythonperf1-amd64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup         | 19.5 ms                                                     | 20.2 ms: 1.04x slower                                           |
| python_startup_no_site | 16.2 ms                                                     | 17.8 ms: 1.09x slower                                           |
| Geometric mean         | (ref)                                                       | 1.07x slower                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240215-pythonperf1-amd64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 6.29 ms: 1.13x faster                                           |
| django_template | 22.9 ms                                                     | 22.5 ms: 1.02x faster                                           |
| Geometric mean  | (ref)                                                       | 1.07x faster                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240215-pythonperf1-amd64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| typing_runtime_protocols   | 95.1 us                                                     | 71.0 us: 1.34x faster                                           |
| comprehensions             | 14.1 us                                                     | 10.8 us: 1.31x faster                                           |
| mypy2                      | 509 ms                                                      | 416 ms: 1.22x faster                                            |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.77 sec: 1.18x faster                                          |
| raytrace                   | 192 ms                                                      | 165 ms: 1.17x faster                                            |
| sqlite_synth               | 1.76 us                                                     | 1.53 us: 1.15x faster                                           |
| spectral_norm              | 66.9 ms                                                     | 59.0 ms: 1.13x faster                                           |
| crypto_pyaes               | 48.5 ms                                                     | 42.8 ms: 1.13x faster                                           |
| mako                       | 7.09 ms                                                     | 6.29 ms: 1.13x faster                                           |
| regex_compile              | 87.5 ms                                                     | 77.8 ms: 1.12x faster                                           |
| float                      | 56.8 ms                                                     | 51.0 ms: 1.11x faster                                           |
| regex_dna                  | 126 ms                                                      | 115 ms: 1.10x faster                                            |
| chaos                      | 43.3 ms                                                     | 39.5 ms: 1.10x faster                                           |
| sympy_str                  | 175 ms                                                      | 160 ms: 1.10x faster                                            |
| async_tree_none            | 291 ms                                                      | 266 ms: 1.10x faster                                            |
| sympy_sum                  | 91.5 ms                                                     | 83.5 ms: 1.10x faster                                           |
| deltablue                  | 2.16 ms                                                     | 1.98 ms: 1.09x faster                                           |
| go                         | 91.6 ms                                                     | 84.4 ms: 1.08x faster                                           |
| generators                 | 22.5 ms                                                     | 20.8 ms: 1.08x faster                                           |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 453 ms: 1.08x faster                                            |
| nqueens                    | 62.8 ms                                                     | 58.2 ms: 1.08x faster                                           |
| coroutines                 | 14.3 ms                                                     | 13.2 ms: 1.08x faster                                           |
| docutils                   | 1.66 sec                                                    | 1.55 sec: 1.07x faster                                          |
| hexiom                     | 4.10 ms                                                     | 3.82 ms: 1.07x faster                                           |
| scimark_monte_carlo        | 43.7 ms                                                     | 40.7 ms: 1.07x faster                                           |
| dulwich_log                | 44.3 ms                                                     | 41.3 ms: 1.07x faster                                           |
| scimark_lu                 | 58.9 ms                                                     | 55.0 ms: 1.07x faster                                           |
| sqlglot_normalize          | 187 ms                                                      | 176 ms: 1.06x faster                                            |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 472 ms: 1.06x faster                                            |
| tornado_http               | 89.5 ms                                                     | 84.3 ms: 1.06x faster                                           |
| logging_silent             | 60.5 ns                                                     | 57.3 ns: 1.06x faster                                           |
| pickle_pure_python         | 195 us                                                      | 186 us: 1.05x faster                                            |
| async_tree_memoization_tg  | 367 ms                                                      | 349 ms: 1.05x faster                                            |
| json                       | 3.05 ms                                                     | 2.91 ms: 1.05x faster                                           |
| sqlglot_parse              | 804 us                                                      | 768 us: 1.05x faster                                            |
| sympy_integrate            | 13.0 ms                                                     | 12.4 ms: 1.05x faster                                           |
| bench_mp_pool              | 69.2 ms                                                     | 66.4 ms: 1.04x faster                                           |
| async_generators           | 239 ms                                                      | 230 ms: 1.04x faster                                            |
| async_tree_none_tg         | 285 ms                                                      | 274 ms: 1.04x faster                                            |
| sqlglot_transpile          | 1.02 ms                                                     | 983 us: 1.04x faster                                            |
| bench_thread_pool          | 857 us                                                      | 824 us: 1.04x faster                                            |
| sympy_expand               | 284 ms                                                      | 274 ms: 1.04x faster                                            |
| regex_effbot               | 1.62 ms                                                     | 1.56 ms: 1.03x faster                                           |
| sqlglot_optimize           | 34.5 ms                                                     | 33.4 ms: 1.03x faster                                           |
| meteor_contest             | 74.6 ms                                                     | 72.2 ms: 1.03x faster                                           |
| pyflate                    | 295 ms                                                      | 285 ms: 1.03x faster                                            |
| deepcopy_memo              | 23.7 us                                                     | 23.0 us: 1.03x faster                                           |
| pidigits                   | 152 ms                                                      | 148 ms: 1.03x faster                                            |
| unpickle_pure_python       | 133 us                                                      | 129 us: 1.03x faster                                            |
| scimark_fft                | 184 ms                                                      | 179 ms: 1.03x faster                                            |
| pprint_safe_repr           | 513 ms                                                      | 500 ms: 1.03x faster                                            |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.49 ms: 1.03x faster                                           |
| unpickle_list              | 2.75 us                                                     | 2.68 us: 1.03x faster                                           |
| mdp                        | 1.37 sec                                                    | 1.34 sec: 1.02x faster                                          |
| xml_etree_generate         | 55.8 ms                                                     | 54.5 ms: 1.02x faster                                           |
| deepcopy                   | 238 us                                                      | 233 us: 1.02x faster                                            |
| pprint_pformat             | 1.05 sec                                                    | 1.02 sec: 1.02x faster                                          |
| logging_format             | 6.72 us                                                     | 6.57 us: 1.02x faster                                           |
| deepcopy_reduce            | 2.09 us                                                     | 2.05 us: 1.02x faster                                           |
| json_dumps                 | 5.70 ms                                                     | 5.58 ms: 1.02x faster                                           |
| logging_simple             | 6.28 us                                                     | 6.15 us: 1.02x faster                                           |
| django_template            | 22.9 ms                                                     | 22.5 ms: 1.02x faster                                           |
| 2to3                       | 218 ms                                                      | 214 ms: 1.02x faster                                            |
| async_tree_io_tg           | 771 ms                                                      | 758 ms: 1.02x faster                                            |
| xml_etree_process          | 37.7 ms                                                     | 37.1 ms: 1.02x faster                                           |
| json_loads                 | 13.9 us                                                     | 13.7 us: 1.02x faster                                           |
| pickle                     | 7.43 us                                                     | 7.32 us: 1.02x faster                                           |
| gc_traversal               | 1.52 ms                                                     | 1.50 ms: 1.02x faster                                           |
| richards_super             | 32.1 ms                                                     | 31.6 ms: 1.01x faster                                           |
| richards                   | 28.4 ms                                                     | 28.0 ms: 1.01x faster                                           |
| create_gc_cycles           | 752 us                                                      | 743 us: 1.01x faster                                            |
| scimark_sor                | 78.8 ms                                                     | 77.9 ms: 1.01x faster                                           |
| xml_etree_parse            | 93.0 ms                                                     | 92.2 ms: 1.01x faster                                           |
| regex_v8                   | 14.2 ms                                                     | 14.4 ms: 1.01x slower                                           |
| fannkuch                   | 247 ms                                                      | 250 ms: 1.01x slower                                            |
| nbody                      | 71.9 ms                                                     | 73.2 ms: 1.02x slower                                           |
| python_startup             | 19.5 ms                                                     | 20.2 ms: 1.04x slower                                           |
| tomli_loads                | 1.37 sec                                                    | 1.43 sec: 1.04x slower                                          |
| pickle_list                | 2.83 us                                                     | 2.96 us: 1.05x slower                                           |
| unpickle                   | 8.18 us                                                     | 8.66 us: 1.06x slower                                           |
| pycparser                  | 699 ms                                                      | 754 ms: 1.08x slower                                            |
| python_startup_no_site     | 16.2 ms                                                     | 17.8 ms: 1.09x slower                                           |
| telco                      | 4.13 ms                                                     | 4.73 ms: 1.15x slower                                           |
| coverage                   | 40.8 ms                                                     | 47.3 ms: 1.16x slower                                           |
| Geometric mean             | (ref)                                                       | 1.04x faster                                                    |

Benchmark hidden because not significant (8): asyncio_tcp, pickle_dict, xml_etree_iterparse, aiohttp, async_tree_io, async_tree_memoization, pathlib, chameleon
Ignored benchmarks (4) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: dask, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (6) of results/bm-20240215-3.13.0a4-9d34f60/bm-20240215-pythonperf1-amd64-python-v3.13.0a4-3.13.0a4-9d34f60.json: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: unknown