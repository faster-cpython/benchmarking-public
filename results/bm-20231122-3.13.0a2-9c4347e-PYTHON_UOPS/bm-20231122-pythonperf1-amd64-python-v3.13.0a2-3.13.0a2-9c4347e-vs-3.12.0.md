
# Results vs. 3.12.0

- fork: python
- ref: v3.13.0a2
- machine: windows-amd64
- commit hash: 9c4347e
- commit date: 2023-11-22
- overall geometric mean: 1.00x slower
- HPT reliability: 91.72%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20231122-pythonperf1-amd64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| chameleon      | 4.98 ms                                                     | 4.84 ms: 1.03x faster                                           |
| docutils       | 1.66 sec                                                    | 1.55 sec: 1.07x faster                                          |
| Geometric mean | (ref)                                                       | 1.03x faster                                                    |

Benchmark hidden because not significant (2): 2to3, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20231122-pythonperf1-amd64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| async_tree_none            | 291 ms                                                      | 267 ms: 1.09x faster                                            |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 454 ms: 1.08x faster                                            |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 481 ms: 1.04x faster                                            |
| async_tree_none_tg         | 285 ms                                                      | 281 ms: 1.01x faster                                            |
| async_tree_memoization     | 339 ms                                                      | 346 ms: 1.02x slower                                            |
| Geometric mean             | (ref)                                                       | 1.03x faster                                                    |

Benchmark hidden because not significant (3): async_tree_memoization_tg, async_tree_io_tg, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20231122-pythonperf1-amd64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| pidigits       | 152 ms                                                      | 148 ms: 1.03x faster                                            |
| nbody          | 71.9 ms                                                     | 81.4 ms: 1.13x slower                                           |
| Geometric mean | (ref)                                                       | 1.03x slower                                                    |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20231122-pythonperf1-amd64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_dna      | 126 ms                                                      | 120 ms: 1.06x faster                                            |
| regex_effbot   | 1.62 ms                                                     | 1.58 ms: 1.03x faster                                           |
| regex_compile  | 87.5 ms                                                     | 88.1 ms: 1.01x slower                                           |
| regex_v8       | 14.2 ms                                                     | 17.9 ms: 1.25x slower                                           |
| Geometric mean | (ref)                                                       | 1.04x slower                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20231122-pythonperf1-amd64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| pickle_pure_python   | 195 us                                                      | 175 us: 1.12x faster                                            |
| pickle               | 7.43 us                                                     | 6.96 us: 1.07x faster                                           |
| unpickle_list        | 2.75 us                                                     | 2.62 us: 1.05x faster                                           |
| json_dumps           | 5.70 ms                                                     | 5.46 ms: 1.04x faster                                           |
| json_loads           | 13.9 us                                                     | 13.4 us: 1.04x faster                                           |
| xml_etree_generate   | 55.8 ms                                                     | 55.1 ms: 1.01x faster                                           |
| unpickle             | 8.18 us                                                     | 8.09 us: 1.01x faster                                           |
| pickle_dict          | 18.4 us                                                     | 18.6 us: 1.01x slower                                           |
| unpickle_pure_python | 133 us                                                      | 136 us: 1.02x slower                                            |
| xml_etree_iterparse  | 65.2 ms                                                     | 67.5 ms: 1.04x slower                                           |
| tomli_loads          | 1.37 sec                                                    | 1.43 sec: 1.04x slower                                          |
| pickle_list          | 2.83 us                                                     | 3.32 us: 1.18x slower                                           |
| Geometric mean       | (ref)                                                       | 1.00x faster                                                    |

Benchmark hidden because not significant (2): xml_etree_process, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20231122-pythonperf1-amd64-python-v3.13.0a2-3.13.0a2-9c4347e |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup         | 19.5 ms                                                     | 20.7 ms: 1.07x slower                                           |
| python_startup_no_site | 16.2 ms                                                     | 19.6 ms: 1.21x slower                                           |
| Geometric mean         | (ref)                                                       | 1.13x slower                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20231122-pythonperf1-amd64-python-v3.13.0a2-3.13.0a2-9c4347e |
|-----------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| mako      | 7.09 ms                                                     | 7.38 ms: 1.04x slower                                           |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20231122-pythonperf1-amd64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.66 sec: 1.26x faster                                          |
| typing_runtime_protocols   | 95.1 us                                                     | 77.0 us: 1.24x faster                                           |
| sqlite_synth               | 1.76 us                                                     | 1.57 us: 1.12x faster                                           |
| pickle_pure_python         | 195 us                                                      | 175 us: 1.12x faster                                            |
| generators                 | 22.5 ms                                                     | 20.3 ms: 1.11x faster                                           |
| deepcopy                   | 238 us                                                      | 216 us: 1.10x faster                                            |
| comprehensions             | 14.1 us                                                     | 12.9 us: 1.09x faster                                           |
| async_tree_none            | 291 ms                                                      | 267 ms: 1.09x faster                                            |
| logging_silent             | 60.5 ns                                                     | 55.5 ns: 1.09x faster                                           |
| raytrace                   | 192 ms                                                      | 177 ms: 1.08x faster                                            |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 454 ms: 1.08x faster                                            |
| deepcopy_reduce            | 2.09 us                                                     | 1.94 us: 1.08x faster                                           |
| docutils                   | 1.66 sec                                                    | 1.55 sec: 1.07x faster                                          |
| coroutines                 | 14.3 ms                                                     | 13.3 ms: 1.07x faster                                           |
| pickle                     | 7.43 us                                                     | 6.96 us: 1.07x faster                                           |
| bench_mp_pool              | 69.2 ms                                                     | 64.9 ms: 1.07x faster                                           |
| richards_super             | 32.1 ms                                                     | 30.1 ms: 1.07x faster                                           |
| regex_dna                  | 126 ms                                                      | 120 ms: 1.06x faster                                            |
| unpickle_list              | 2.75 us                                                     | 2.62 us: 1.05x faster                                           |
| richards                   | 28.4 ms                                                     | 27.0 ms: 1.05x faster                                           |
| async_generators           | 239 ms                                                      | 228 ms: 1.05x faster                                            |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 481 ms: 1.04x faster                                            |
| json_dumps                 | 5.70 ms                                                     | 5.46 ms: 1.04x faster                                           |
| sympy_str                  | 175 ms                                                      | 168 ms: 1.04x faster                                            |
| deepcopy_memo              | 23.7 us                                                     | 22.9 us: 1.04x faster                                           |
| json_loads                 | 13.9 us                                                     | 13.4 us: 1.04x faster                                           |
| pycparser                  | 699 ms                                                      | 675 ms: 1.04x faster                                            |
| dulwich_log                | 44.3 ms                                                     | 42.8 ms: 1.03x faster                                           |
| dask                       | 263 ms                                                      | 254 ms: 1.03x faster                                            |
| sqlglot_parse              | 804 us                                                      | 779 us: 1.03x faster                                            |
| chameleon                  | 4.98 ms                                                     | 4.84 ms: 1.03x faster                                           |
| pidigits                   | 152 ms                                                      | 148 ms: 1.03x faster                                            |
| sympy_sum                  | 91.5 ms                                                     | 89.1 ms: 1.03x faster                                           |
| create_gc_cycles           | 752 us                                                      | 732 us: 1.03x faster                                            |
| regex_effbot               | 1.62 ms                                                     | 1.58 ms: 1.03x faster                                           |
| pathlib                    | 80.5 ms                                                     | 78.5 ms: 1.02x faster                                           |
| asyncio_tcp                | 487 ms                                                      | 477 ms: 1.02x faster                                            |
| scimark_lu                 | 58.9 ms                                                     | 57.6 ms: 1.02x faster                                           |
| gc_traversal               | 1.52 ms                                                     | 1.49 ms: 1.02x faster                                           |
| sqlglot_normalize          | 187 ms                                                      | 183 ms: 1.02x faster                                            |
| sqlglot_transpile          | 1.02 ms                                                     | 1.01 ms: 1.01x faster                                           |
| async_tree_none_tg         | 285 ms                                                      | 281 ms: 1.01x faster                                            |
| xml_etree_generate         | 55.8 ms                                                     | 55.1 ms: 1.01x faster                                           |
| unpickle                   | 8.18 us                                                     | 8.09 us: 1.01x faster                                           |
| sympy_expand               | 284 ms                                                      | 281 ms: 1.01x faster                                            |
| logging_simple             | 6.28 us                                                     | 6.24 us: 1.01x faster                                           |
| go                         | 91.6 ms                                                     | 92.1 ms: 1.01x slower                                           |
| logging_format             | 6.72 us                                                     | 6.76 us: 1.01x slower                                           |
| regex_compile              | 87.5 ms                                                     | 88.1 ms: 1.01x slower                                           |
| sqlglot_optimize           | 34.5 ms                                                     | 34.8 ms: 1.01x slower                                           |
| pickle_dict                | 18.4 us                                                     | 18.6 us: 1.01x slower                                           |
| pprint_safe_repr           | 513 ms                                                      | 519 ms: 1.01x slower                                            |
| crypto_pyaes               | 48.5 ms                                                     | 49.2 ms: 1.01x slower                                           |
| async_tree_memoization     | 339 ms                                                      | 346 ms: 1.02x slower                                            |
| unpickle_pure_python       | 133 us                                                      | 136 us: 1.02x slower                                            |
| sympy_integrate            | 13.0 ms                                                     | 13.3 ms: 1.02x slower                                           |
| chaos                      | 43.3 ms                                                     | 44.4 ms: 1.03x slower                                           |
| pprint_pformat             | 1.05 sec                                                    | 1.07 sec: 1.03x slower                                          |
| xml_etree_iterparse        | 65.2 ms                                                     | 67.5 ms: 1.04x slower                                           |
| meteor_contest             | 74.6 ms                                                     | 77.5 ms: 1.04x slower                                           |
| nqueens                    | 62.8 ms                                                     | 65.3 ms: 1.04x slower                                           |
| mako                       | 7.09 ms                                                     | 7.38 ms: 1.04x slower                                           |
| tomli_loads                | 1.37 sec                                                    | 1.43 sec: 1.04x slower                                          |
| mdp                        | 1.37 sec                                                    | 1.44 sec: 1.05x slower                                          |
| python_startup             | 19.5 ms                                                     | 20.7 ms: 1.07x slower                                           |
| unpack_sequence            | 37.5 ns                                                     | 40.1 ns: 1.07x slower                                           |
| pyflate                    | 295 ms                                                      | 324 ms: 1.10x slower                                            |
| coverage                   | 40.8 ms                                                     | 45.2 ms: 1.11x slower                                           |
| fannkuch                   | 247 ms                                                      | 277 ms: 1.12x slower                                            |
| telco                      | 4.13 ms                                                     | 4.64 ms: 1.12x slower                                           |
| scimark_monte_carlo        | 43.7 ms                                                     | 49.4 ms: 1.13x slower                                           |
| nbody                      | 71.9 ms                                                     | 81.4 ms: 1.13x slower                                           |
| mypy2                      | 509 ms                                                      | 589 ms: 1.16x slower                                            |
| scimark_fft                | 184 ms                                                      | 213 ms: 1.16x slower                                            |
| pickle_list                | 2.83 us                                                     | 3.32 us: 1.18x slower                                           |
| python_startup_no_site     | 16.2 ms                                                     | 19.6 ms: 1.21x slower                                           |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 3.09 ms: 1.21x slower                                           |
| hexiom                     | 4.10 ms                                                     | 5.03 ms: 1.23x slower                                           |
| regex_v8                   | 14.2 ms                                                     | 17.9 ms: 1.25x slower                                           |
| spectral_norm              | 66.9 ms                                                     | 84.1 ms: 1.26x slower                                           |
| deltablue                  | 2.16 ms                                                     | 2.72 ms: 1.26x slower                                           |
| Geometric mean             | (ref)                                                       | 1.00x slower                                                    |

Benchmark hidden because not significant (11): async_tree_memoization_tg, async_tree_io_tg, async_tree_io, xml_etree_process, 2to3, scimark_sor, tornado_http, xml_etree_parse, bench_thread_pool, float, json
Ignored benchmarks (4) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, django_template, sqlalchemy_declarative, sqlalchemy_imperative


# HPT report

- Reliability score: 91.72% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x


# Memory

- memory change: unknown