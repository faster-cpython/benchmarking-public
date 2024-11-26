# Results vs. 3.12.0

- fork: brandtbucher
- ref: justin_no_externs
- machine: windows-amd64
- commit hash: 64b198a
- commit date: 2024-10-25
- overall geometric mean: 1.001x faster
- HPT reliability: 59.33%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241025-pythonperf1-amd64-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 248 ms: 1.14x slower                                                           |
| docutils       | 1.66 sec                                                    | 1.93 sec: 1.16x slower                                                         |
| tornado_http   | 89.5 ms                                                     | 99.0 ms: 1.11x slower                                                          |
| Geometric mean | (ref)                                                       | 1.13x slower                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241025-pythonperf1-amd64-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|----------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 367 ms                                                      | 260 ms: 1.41x faster                                                           |
| async_tree_none_tg         | 285 ms                                                      | 210 ms: 1.36x faster                                                           |
| async_tree_none            | 291 ms                                                      | 216 ms: 1.35x faster                                                           |
| async_tree_io              | 731 ms                                                      | 553 ms: 1.32x faster                                                           |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 383 ms: 1.28x faster                                                           |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 399 ms: 1.26x faster                                                           |
| async_tree_memoization     | 339 ms                                                      | 281 ms: 1.21x faster                                                           |
| async_tree_io_tg           | 771 ms                                                      | 640 ms: 1.20x faster                                                           |
| Geometric mean             | (ref)                                                       | 1.30x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241025-pythonperf1-amd64-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| nbody          | 71.9 ms                                                     | 56.2 ms: 1.28x faster                                                          |
| float          | 56.8 ms                                                     | 48.3 ms: 1.17x faster                                                          |
| pidigits       | 152 ms                                                      | 148 ms: 1.03x faster                                                           |
| Geometric mean | (ref)                                                       | 1.16x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241025-pythonperf1-amd64-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_dna      | 126 ms                                                      | 115 ms: 1.10x faster                                                           |
| regex_effbot   | 1.62 ms                                                     | 1.56 ms: 1.03x faster                                                          |
| regex_v8       | 14.2 ms                                                     | 14.7 ms: 1.03x slower                                                          |
| regex_compile  | 87.5 ms                                                     | 92.5 ms: 1.06x slower                                                          |
| Geometric mean | (ref)                                                       | 1.01x faster                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241025-pythonperf1-amd64-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|----------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| xml_etree_generate   | 55.8 ms                                                     | 51.7 ms: 1.08x faster                                                          |
| tomli_loads          | 1.37 sec                                                    | 1.30 sec: 1.05x faster                                                         |
| xml_etree_process    | 37.7 ms                                                     | 36.7 ms: 1.03x faster                                                          |
| xml_etree_iterparse  | 65.2 ms                                                     | 63.8 ms: 1.02x faster                                                          |
| xml_etree_parse      | 93.0 ms                                                     | 95.8 ms: 1.03x slower                                                          |
| pickle_pure_python   | 195 us                                                      | 204 us: 1.05x slower                                                           |
| json_loads           | 13.9 us                                                     | 14.6 us: 1.05x slower                                                          |
| unpickle_pure_python | 133 us                                                      | 147 us: 1.11x slower                                                           |
| json_dumps           | 5.70 ms                                                     | 6.62 ms: 1.16x slower                                                          |
| Geometric mean       | (ref)                                                       | 1.02x slower                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241025-pythonperf1-amd64-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 18.4 ms: 1.13x slower                                                          |
| python_startup         | 19.5 ms                                                     | 24.4 ms: 1.25x slower                                                          |
| Geometric mean         | (ref)                                                       | 1.19x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241025-pythonperf1-amd64-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|-----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 5.14 ms: 1.38x faster                                                          |
| django_template | 22.9 ms                                                     | 27.0 ms: 1.18x slower                                                          |
| Geometric mean  | (ref)                                                       | 1.08x faster                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241025-pythonperf1-amd64-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|----------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 367 ms                                                      | 260 ms: 1.41x faster                                                           |
| deepcopy_memo              | 23.7 us                                                     | 17.0 us: 1.40x faster                                                          |
| mako                       | 7.09 ms                                                     | 5.14 ms: 1.38x faster                                                          |
| async_tree_none_tg         | 285 ms                                                      | 210 ms: 1.36x faster                                                           |
| async_tree_none            | 291 ms                                                      | 216 ms: 1.35x faster                                                           |
| async_tree_io              | 731 ms                                                      | 553 ms: 1.32x faster                                                           |
| nbody                      | 71.9 ms                                                     | 56.2 ms: 1.28x faster                                                          |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 383 ms: 1.28x faster                                                           |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 399 ms: 1.26x faster                                                           |
| spectral_norm              | 66.9 ms                                                     | 53.6 ms: 1.25x faster                                                          |
| deepcopy                   | 238 us                                                      | 196 us: 1.21x faster                                                           |
| async_tree_memoization     | 339 ms                                                      | 281 ms: 1.21x faster                                                           |
| async_tree_io_tg           | 771 ms                                                      | 640 ms: 1.20x faster                                                           |
| comprehensions             | 14.1 us                                                     | 11.8 us: 1.20x faster                                                          |
| float                      | 56.8 ms                                                     | 48.3 ms: 1.17x faster                                                          |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.20 ms: 1.16x faster                                                          |
| scimark_sor                | 78.8 ms                                                     | 67.9 ms: 1.16x faster                                                          |
| crypto_pyaes               | 48.5 ms                                                     | 42.8 ms: 1.13x faster                                                          |
| pprint_safe_repr           | 513 ms                                                      | 453 ms: 1.13x faster                                                           |
| scimark_fft                | 184 ms                                                      | 163 ms: 1.13x faster                                                           |
| scimark_monte_carlo        | 43.7 ms                                                     | 39.4 ms: 1.11x faster                                                          |
| pprint_pformat             | 1.05 sec                                                    | 945 ms: 1.11x faster                                                           |
| regex_dna                  | 126 ms                                                      | 115 ms: 1.10x faster                                                           |
| dulwich_log                | 44.3 ms                                                     | 40.6 ms: 1.09x faster                                                          |
| deepcopy_reduce            | 2.09 us                                                     | 1.92 us: 1.09x faster                                                          |
| xml_etree_generate         | 55.8 ms                                                     | 51.7 ms: 1.08x faster                                                          |
| fannkuch                   | 247 ms                                                      | 234 ms: 1.06x faster                                                           |
| logging_silent             | 60.5 ns                                                     | 57.6 ns: 1.05x faster                                                          |
| tomli_loads                | 1.37 sec                                                    | 1.30 sec: 1.05x faster                                                         |
| regex_effbot               | 1.62 ms                                                     | 1.56 ms: 1.03x faster                                                          |
| pidigits                   | 152 ms                                                      | 148 ms: 1.03x faster                                                           |
| xml_etree_process          | 37.7 ms                                                     | 36.7 ms: 1.03x faster                                                          |
| xml_etree_iterparse        | 65.2 ms                                                     | 63.8 ms: 1.02x faster                                                          |
| coroutines                 | 14.3 ms                                                     | 14.0 ms: 1.02x faster                                                          |
| json                       | 3.05 ms                                                     | 3.01 ms: 1.01x faster                                                          |
| logging_simple             | 6.28 us                                                     | 6.22 us: 1.01x faster                                                          |
| scimark_lu                 | 58.9 ms                                                     | 58.4 ms: 1.01x faster                                                          |
| nqueens                    | 62.8 ms                                                     | 63.7 ms: 1.01x slower                                                          |
| meteor_contest             | 74.6 ms                                                     | 75.7 ms: 1.01x slower                                                          |
| pyflate                    | 295 ms                                                      | 300 ms: 1.02x slower                                                           |
| generators                 | 22.5 ms                                                     | 23.0 ms: 1.02x slower                                                          |
| go                         | 91.6 ms                                                     | 94.0 ms: 1.03x slower                                                          |
| xml_etree_parse            | 93.0 ms                                                     | 95.8 ms: 1.03x slower                                                          |
| regex_v8                   | 14.2 ms                                                     | 14.7 ms: 1.03x slower                                                          |
| pycparser                  | 699 ms                                                      | 722 ms: 1.03x slower                                                           |
| pickle_pure_python         | 195 us                                                      | 204 us: 1.05x slower                                                           |
| json_loads                 | 13.9 us                                                     | 14.6 us: 1.05x slower                                                          |
| regex_compile              | 87.5 ms                                                     | 92.5 ms: 1.06x slower                                                          |
| raytrace                   | 192 ms                                                      | 207 ms: 1.07x slower                                                           |
| deltablue                  | 2.16 ms                                                     | 2.35 ms: 1.09x slower                                                          |
| unpickle_pure_python       | 133 us                                                      | 147 us: 1.11x slower                                                           |
| tornado_http               | 89.5 ms                                                     | 99.0 ms: 1.11x slower                                                          |
| sympy_str                  | 175 ms                                                      | 194 ms: 1.11x slower                                                           |
| sqlglot_normalize          | 187 ms                                                      | 211 ms: 1.13x slower                                                           |
| async_generators           | 239 ms                                                      | 270 ms: 1.13x slower                                                           |
| sqlglot_parse              | 804 us                                                      | 908 us: 1.13x slower                                                           |
| python_startup_no_site     | 16.2 ms                                                     | 18.4 ms: 1.13x slower                                                          |
| sympy_sum                  | 91.5 ms                                                     | 104 ms: 1.13x slower                                                           |
| 2to3                       | 218 ms                                                      | 248 ms: 1.14x slower                                                           |
| sympy_expand               | 284 ms                                                      | 325 ms: 1.15x slower                                                           |
| telco                      | 4.13 ms                                                     | 4.77 ms: 1.16x slower                                                          |
| coverage                   | 40.8 ms                                                     | 47.2 ms: 1.16x slower                                                          |
| docutils                   | 1.66 sec                                                    | 1.93 sec: 1.16x slower                                                         |
| json_dumps                 | 5.70 ms                                                     | 6.62 ms: 1.16x slower                                                          |
| sqlglot_transpile          | 1.02 ms                                                     | 1.20 ms: 1.17x slower                                                          |
| django_template            | 22.9 ms                                                     | 27.0 ms: 1.18x slower                                                          |
| mdp                        | 1.37 sec                                                    | 1.62 sec: 1.18x slower                                                         |
| richards_super             | 32.1 ms                                                     | 38.3 ms: 1.19x slower                                                          |
| richards                   | 28.4 ms                                                     | 34.2 ms: 1.21x slower                                                          |
| sympy_integrate            | 13.0 ms                                                     | 15.7 ms: 1.21x slower                                                          |
| typing_runtime_protocols   | 95.1 us                                                     | 119 us: 1.25x slower                                                           |
| python_startup             | 19.5 ms                                                     | 24.4 ms: 1.25x slower                                                          |
| sqlglot_optimize           | 34.5 ms                                                     | 43.7 ms: 1.27x slower                                                          |
| gc_traversal               | 1.52 ms                                                     | 1.97 ms: 1.29x slower                                                          |
| bench_mp_pool              | 69.2 ms                                                     | 89.6 ms: 1.30x slower                                                          |
| hexiom                     | 4.10 ms                                                     | 5.33 ms: 1.30x slower                                                          |
| create_gc_cycles           | 752 us                                                      | 1.39 ms: 1.84x slower                                                          |
| Geometric mean             | (ref)                                                       | 1.00x slower                                                                   |

Benchmark hidden because not significant (4): bench_thread_pool, chaos, logging_format, pathlib
Ignored benchmarks (15) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20241025-3.14.0a1+-64b198a-JIT/bm-20241025-pythonperf1-amd64-brandtbucher-justin_no_externs-3.14.0a1+-64b198a.json: genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift

- Geometric mean (including insignificant results): 1.001x faster
# HPT report

- Reliability score: 59.33% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown