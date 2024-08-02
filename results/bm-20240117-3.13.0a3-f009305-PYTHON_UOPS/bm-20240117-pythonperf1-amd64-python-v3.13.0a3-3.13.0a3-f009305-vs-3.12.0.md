
# Results vs. 3.12.0

- fork: python
- ref: v3.13.0a3
- machine: windows-amd64
- commit hash: f009305
- commit date: 2024-01-17
- overall geometric mean: 1.00x faster
- HPT reliability: 98.39%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240117-pythonperf1-amd64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| chameleon      | 4.98 ms                                                     | 5.10 ms: 1.02x slower                                           |
| docutils       | 1.66 sec                                                    | 1.59 sec: 1.05x faster                                          |
| tornado_http   | 89.5 ms                                                     | 88.2 ms: 1.02x faster                                           |
| Geometric mean | (ref)                                                       | 1.01x faster                                                    |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240117-pythonperf1-amd64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| async_tree_none            | 291 ms                                                      | 266 ms: 1.10x faster                                            |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 450 ms: 1.09x faster                                            |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 469 ms: 1.07x faster                                            |
| async_tree_none_tg         | 285 ms                                                      | 275 ms: 1.04x faster                                            |
| async_tree_memoization_tg  | 367 ms                                                      | 354 ms: 1.04x faster                                            |
| async_tree_io_tg           | 771 ms                                                      | 748 ms: 1.03x faster                                            |
| Geometric mean             | (ref)                                                       | 1.05x faster                                                    |

Benchmark hidden because not significant (2): async_tree_io, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240117-pythonperf1-amd64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| pidigits       | 152 ms                                                      | 148 ms: 1.03x faster                                            |
| float          | 56.8 ms                                                     | 55.5 ms: 1.02x faster                                           |
| nbody          | 71.9 ms                                                     | 79.2 ms: 1.10x slower                                           |
| Geometric mean | (ref)                                                       | 1.01x slower                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240117-pythonperf1-amd64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_compile  | 87.5 ms                                                     | 84.2 ms: 1.04x faster                                           |
| regex_dna      | 126 ms                                                      | 122 ms: 1.04x faster                                            |
| regex_effbot   | 1.62 ms                                                     | 1.60 ms: 1.01x faster                                           |
| regex_v8       | 14.2 ms                                                     | 15.5 ms: 1.09x slower                                           |
| Geometric mean | (ref)                                                       | 1.00x faster                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240117-pythonperf1-amd64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| pickle_pure_python   | 195 us                                                      | 182 us: 1.08x faster                                            |
| json_loads           | 13.9 us                                                     | 13.6 us: 1.02x faster                                           |
| json_dumps           | 5.70 ms                                                     | 5.59 ms: 1.02x faster                                           |
| xml_etree_generate   | 55.8 ms                                                     | 55.2 ms: 1.01x faster                                           |
| xml_etree_process    | 37.7 ms                                                     | 37.3 ms: 1.01x faster                                           |
| pickle               | 7.43 us                                                     | 7.37 us: 1.01x faster                                           |
| xml_etree_parse      | 93.0 ms                                                     | 94.0 ms: 1.01x slower                                           |
| tomli_loads          | 1.37 sec                                                    | 1.38 sec: 1.01x slower                                          |
| pickle_dict          | 18.4 us                                                     | 18.8 us: 1.02x slower                                           |
| unpickle_pure_python | 133 us                                                      | 137 us: 1.03x slower                                            |
| xml_etree_iterparse  | 65.2 ms                                                     | 67.5 ms: 1.04x slower                                           |
| pickle_list          | 2.83 us                                                     | 3.08 us: 1.09x slower                                           |
| Geometric mean       | (ref)                                                       | 1.00x slower                                                    |

Benchmark hidden because not significant (2): unpickle_list, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240117-pythonperf1-amd64-python-v3.13.0a3-3.13.0a3-f009305 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup         | 19.5 ms                                                     | 20.7 ms: 1.06x slower                                           |
| python_startup_no_site | 16.2 ms                                                     | 18.5 ms: 1.14x slower                                           |
| Geometric mean         | (ref)                                                       | 1.10x slower                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240117-pythonperf1-amd64-python-v3.13.0a3-3.13.0a3-f009305 |
|-----------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| mako      | 7.09 ms                                                     | 7.29 ms: 1.03x slower                                           |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240117-pythonperf1-amd64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.62 sec: 1.29x faster                                          |
| typing_runtime_protocols   | 95.1 us                                                     | 74.9 us: 1.27x faster                                           |
| mypy2                      | 509 ms                                                      | 424 ms: 1.20x faster                                            |
| sqlite_synth               | 1.76 us                                                     | 1.57 us: 1.12x faster                                           |
| comprehensions             | 14.1 us                                                     | 12.7 us: 1.11x faster                                           |
| raytrace                   | 192 ms                                                      | 174 ms: 1.11x faster                                            |
| coroutines                 | 14.3 ms                                                     | 12.9 ms: 1.10x faster                                           |
| async_tree_none            | 291 ms                                                      | 266 ms: 1.10x faster                                            |
| generators                 | 22.5 ms                                                     | 20.6 ms: 1.10x faster                                           |
| logging_silent             | 60.5 ns                                                     | 55.3 ns: 1.09x faster                                           |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 450 ms: 1.09x faster                                            |
| pickle_pure_python         | 195 us                                                      | 182 us: 1.08x faster                                            |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 469 ms: 1.07x faster                                            |
| sympy_sum                  | 91.5 ms                                                     | 86.6 ms: 1.06x faster                                           |
| sympy_str                  | 175 ms                                                      | 166 ms: 1.05x faster                                            |
| async_generators           | 239 ms                                                      | 227 ms: 1.05x faster                                            |
| richards_super             | 32.1 ms                                                     | 30.5 ms: 1.05x faster                                           |
| richards                   | 28.4 ms                                                     | 27.0 ms: 1.05x faster                                           |
| docutils                   | 1.66 sec                                                    | 1.59 sec: 1.05x faster                                          |
| asyncio_tcp                | 487 ms                                                      | 468 ms: 1.04x faster                                            |
| regex_compile              | 87.5 ms                                                     | 84.2 ms: 1.04x faster                                           |
| dulwich_log                | 44.3 ms                                                     | 42.6 ms: 1.04x faster                                           |
| async_tree_none_tg         | 285 ms                                                      | 275 ms: 1.04x faster                                            |
| regex_dna                  | 126 ms                                                      | 122 ms: 1.04x faster                                            |
| sqlglot_normalize          | 187 ms                                                      | 180 ms: 1.04x faster                                            |
| async_tree_memoization_tg  | 367 ms                                                      | 354 ms: 1.04x faster                                            |
| pycparser                  | 699 ms                                                      | 675 ms: 1.04x faster                                            |
| deepcopy_reduce            | 2.09 us                                                     | 2.02 us: 1.04x faster                                           |
| deepcopy                   | 238 us                                                      | 230 us: 1.03x faster                                            |
| sqlglot_parse              | 804 us                                                      | 778 us: 1.03x faster                                            |
| scimark_lu                 | 58.9 ms                                                     | 56.9 ms: 1.03x faster                                           |
| bench_mp_pool              | 69.2 ms                                                     | 67.1 ms: 1.03x faster                                           |
| pidigits                   | 152 ms                                                      | 148 ms: 1.03x faster                                            |
| async_tree_io_tg           | 771 ms                                                      | 748 ms: 1.03x faster                                            |
| pathlib                    | 80.5 ms                                                     | 78.3 ms: 1.03x faster                                           |
| json_loads                 | 13.9 us                                                     | 13.6 us: 1.02x faster                                           |
| float                      | 56.8 ms                                                     | 55.5 ms: 1.02x faster                                           |
| sqlglot_transpile          | 1.02 ms                                                     | 1000 us: 1.02x faster                                           |
| gc_traversal               | 1.52 ms                                                     | 1.49 ms: 1.02x faster                                           |
| dask                       | 263 ms                                                      | 257 ms: 1.02x faster                                            |
| create_gc_cycles           | 752 us                                                      | 738 us: 1.02x faster                                            |
| json_dumps                 | 5.70 ms                                                     | 5.59 ms: 1.02x faster                                           |
| sympy_expand               | 284 ms                                                      | 279 ms: 1.02x faster                                            |
| crypto_pyaes               | 48.5 ms                                                     | 47.7 ms: 1.02x faster                                           |
| tornado_http               | 89.5 ms                                                     | 88.2 ms: 1.02x faster                                           |
| xml_etree_generate         | 55.8 ms                                                     | 55.2 ms: 1.01x faster                                           |
| regex_effbot               | 1.62 ms                                                     | 1.60 ms: 1.01x faster                                           |
| xml_etree_process          | 37.7 ms                                                     | 37.3 ms: 1.01x faster                                           |
| go                         | 91.6 ms                                                     | 90.8 ms: 1.01x faster                                           |
| pickle                     | 7.43 us                                                     | 7.37 us: 1.01x faster                                           |
| logging_simple             | 6.28 us                                                     | 6.23 us: 1.01x faster                                           |
| sympy_integrate            | 13.0 ms                                                     | 13.1 ms: 1.01x slower                                           |
| xml_etree_parse            | 93.0 ms                                                     | 94.0 ms: 1.01x slower                                           |
| tomli_loads                | 1.37 sec                                                    | 1.38 sec: 1.01x slower                                          |
| scimark_sor                | 78.8 ms                                                     | 79.9 ms: 1.01x slower                                           |
| chaos                      | 43.3 ms                                                     | 44.0 ms: 1.02x slower                                           |
| meteor_contest             | 74.6 ms                                                     | 76.2 ms: 1.02x slower                                           |
| pickle_dict                | 18.4 us                                                     | 18.8 us: 1.02x slower                                           |
| chameleon                  | 4.98 ms                                                     | 5.10 ms: 1.02x slower                                           |
| unpickle_pure_python       | 133 us                                                      | 137 us: 1.03x slower                                            |
| mako                       | 7.09 ms                                                     | 7.29 ms: 1.03x slower                                           |
| pprint_safe_repr           | 513 ms                                                      | 528 ms: 1.03x slower                                            |
| xml_etree_iterparse        | 65.2 ms                                                     | 67.5 ms: 1.04x slower                                           |
| unpack_sequence            | 37.5 ns                                                     | 39.1 ns: 1.04x slower                                           |
| pprint_pformat             | 1.05 sec                                                    | 1.09 sec: 1.04x slower                                          |
| python_startup             | 19.5 ms                                                     | 20.7 ms: 1.06x slower                                           |
| fannkuch                   | 247 ms                                                      | 264 ms: 1.07x slower                                            |
| mdp                        | 1.37 sec                                                    | 1.47 sec: 1.07x slower                                          |
| scimark_monte_carlo        | 43.7 ms                                                     | 47.5 ms: 1.09x slower                                           |
| pickle_list                | 2.83 us                                                     | 3.08 us: 1.09x slower                                           |
| regex_v8                   | 14.2 ms                                                     | 15.5 ms: 1.09x slower                                           |
| pyflate                    | 295 ms                                                      | 323 ms: 1.10x slower                                            |
| scimark_fft                | 184 ms                                                      | 203 ms: 1.10x slower                                            |
| nbody                      | 71.9 ms                                                     | 79.2 ms: 1.10x slower                                           |
| coverage                   | 40.8 ms                                                     | 46.0 ms: 1.13x slower                                           |
| telco                      | 4.13 ms                                                     | 4.66 ms: 1.13x slower                                           |
| python_startup_no_site     | 16.2 ms                                                     | 18.5 ms: 1.14x slower                                           |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.95 ms: 1.15x slower                                           |
| json                       | 3.05 ms                                                     | 3.52 ms: 1.16x slower                                           |
| hexiom                     | 4.10 ms                                                     | 4.82 ms: 1.18x slower                                           |
| spectral_norm              | 66.9 ms                                                     | 79.9 ms: 1.19x slower                                           |
| deltablue                  | 2.16 ms                                                     | 2.60 ms: 1.20x slower                                           |
| Geometric mean             | (ref)                                                       | 1.00x faster                                                    |

Benchmark hidden because not significant (10): async_tree_io, unpickle_list, 2to3, logging_format, deepcopy_memo, sqlglot_optimize, nqueens, unpickle, async_tree_memoization, bench_thread_pool
Ignored benchmarks (4) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, django_template, sqlalchemy_declarative, sqlalchemy_imperative


# HPT report

- Reliability score: 98.39% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x


# Memory

- memory change: unknown