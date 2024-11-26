# Results vs. 3.12.0

- fork: brandtbucher
- ref: justin_no_externs
- machine: windows-amd64
- commit hash: 9698931
- commit date: 2024-10-24
- overall geometric mean: 1.041x slower
- HPT reliability: 97.27%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241024-pythonperf1-amd64-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 258 ms: 1.18x slower                                                           |
| docutils       | 1.66 sec                                                    | 1.94 sec: 1.17x slower                                                         |
| tornado_http   | 89.5 ms                                                     | 100 ms: 1.12x slower                                                           |
| Geometric mean | (ref)                                                       | 1.16x slower                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241024-pythonperf1-amd64-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|----------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 367 ms                                                      | 262 ms: 1.40x faster                                                           |
| async_tree_none_tg         | 285 ms                                                      | 214 ms: 1.33x faster                                                           |
| async_tree_none            | 291 ms                                                      | 224 ms: 1.30x faster                                                           |
| async_tree_io              | 731 ms                                                      | 564 ms: 1.30x faster                                                           |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 388 ms: 1.26x faster                                                           |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 402 ms: 1.25x faster                                                           |
| async_tree_io_tg           | 771 ms                                                      | 646 ms: 1.19x faster                                                           |
| async_tree_memoization     | 339 ms                                                      | 284 ms: 1.19x faster                                                           |
| Geometric mean             | (ref)                                                       | 1.28x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241024-pythonperf1-amd64-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| nbody          | 71.9 ms                                                     | 57.3 ms: 1.25x faster                                                          |
| float          | 56.8 ms                                                     | 46.8 ms: 1.21x faster                                                          |
| pidigits       | 152 ms                                                      | 149 ms: 1.02x faster                                                           |
| Geometric mean | (ref)                                                       | 1.16x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241024-pythonperf1-amd64-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_dna      | 126 ms                                                      | 118 ms: 1.07x faster                                                           |
| regex_effbot   | 1.62 ms                                                     | 1.58 ms: 1.02x faster                                                          |
| regex_v8       | 14.2 ms                                                     | 15.0 ms: 1.05x slower                                                          |
| regex_compile  | 87.5 ms                                                     | 98.9 ms: 1.13x slower                                                          |
| Geometric mean | (ref)                                                       | 1.02x slower                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241024-pythonperf1-amd64-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|----------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| xml_etree_iterparse  | 65.2 ms                                                     | 63.9 ms: 1.02x faster                                                          |
| xml_etree_parse      | 93.0 ms                                                     | 95.0 ms: 1.02x slower                                                          |
| tomli_loads          | 1.37 sec                                                    | 1.41 sec: 1.03x slower                                                         |
| json_loads           | 13.9 us                                                     | 14.4 us: 1.04x slower                                                          |
| xml_etree_process    | 37.7 ms                                                     | 40.7 ms: 1.08x slower                                                          |
| pickle_pure_python   | 195 us                                                      | 219 us: 1.12x slower                                                           |
| unpickle_pure_python | 133 us                                                      | 151 us: 1.13x slower                                                           |
| json_dumps           | 5.70 ms                                                     | 6.71 ms: 1.18x slower                                                          |
| Geometric mean       | (ref)                                                       | 1.06x slower                                                                   |

Benchmark hidden because not significant (1): xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241024-pythonperf1-amd64-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 18.9 ms: 1.16x slower                                                          |
| python_startup         | 19.5 ms                                                     | 24.8 ms: 1.27x slower                                                          |
| Geometric mean         | (ref)                                                       | 1.22x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241024-pythonperf1-amd64-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|-----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 5.60 ms: 1.26x faster                                                          |
| django_template | 22.9 ms                                                     | 28.8 ms: 1.25x slower                                                          |
| Geometric mean  | (ref)                                                       | 1.00x faster                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241024-pythonperf1-amd64-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|----------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 367 ms                                                      | 262 ms: 1.40x faster                                                           |
| deepcopy_memo              | 23.7 us                                                     | 17.6 us: 1.34x faster                                                          |
| async_tree_none_tg         | 285 ms                                                      | 214 ms: 1.33x faster                                                           |
| async_tree_none            | 291 ms                                                      | 224 ms: 1.30x faster                                                           |
| async_tree_io              | 731 ms                                                      | 564 ms: 1.30x faster                                                           |
| mako                       | 7.09 ms                                                     | 5.60 ms: 1.26x faster                                                          |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 388 ms: 1.26x faster                                                           |
| nbody                      | 71.9 ms                                                     | 57.3 ms: 1.25x faster                                                          |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 402 ms: 1.25x faster                                                           |
| float                      | 56.8 ms                                                     | 46.8 ms: 1.21x faster                                                          |
| async_tree_io_tg           | 771 ms                                                      | 646 ms: 1.19x faster                                                           |
| async_tree_memoization     | 339 ms                                                      | 284 ms: 1.19x faster                                                           |
| spectral_norm              | 66.9 ms                                                     | 56.3 ms: 1.19x faster                                                          |
| deepcopy                   | 238 us                                                      | 210 us: 1.13x faster                                                           |
| dulwich_log                | 44.3 ms                                                     | 39.4 ms: 1.13x faster                                                          |
| scimark_sor                | 78.8 ms                                                     | 71.8 ms: 1.10x faster                                                          |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.38 ms: 1.07x faster                                                          |
| regex_dna                  | 126 ms                                                      | 118 ms: 1.07x faster                                                           |
| scimark_fft                | 184 ms                                                      | 175 ms: 1.05x faster                                                           |
| comprehensions             | 14.1 us                                                     | 13.5 us: 1.05x faster                                                          |
| deepcopy_reduce            | 2.09 us                                                     | 2.03 us: 1.03x faster                                                          |
| crypto_pyaes               | 48.5 ms                                                     | 47.2 ms: 1.03x faster                                                          |
| pidigits                   | 152 ms                                                      | 149 ms: 1.02x faster                                                           |
| regex_effbot               | 1.62 ms                                                     | 1.58 ms: 1.02x faster                                                          |
| xml_etree_iterparse        | 65.2 ms                                                     | 63.9 ms: 1.02x faster                                                          |
| coroutines                 | 14.3 ms                                                     | 14.1 ms: 1.01x faster                                                          |
| scimark_lu                 | 58.9 ms                                                     | 58.4 ms: 1.01x faster                                                          |
| logging_format             | 6.72 us                                                     | 6.68 us: 1.01x faster                                                          |
| xml_etree_parse            | 93.0 ms                                                     | 95.0 ms: 1.02x slower                                                          |
| fannkuch                   | 247 ms                                                      | 253 ms: 1.03x slower                                                           |
| tomli_loads                | 1.37 sec                                                    | 1.41 sec: 1.03x slower                                                         |
| scimark_monte_carlo        | 43.7 ms                                                     | 45.0 ms: 1.03x slower                                                          |
| json_loads                 | 13.9 us                                                     | 14.4 us: 1.04x slower                                                          |
| pprint_safe_repr           | 513 ms                                                      | 539 ms: 1.05x slower                                                           |
| regex_v8                   | 14.2 ms                                                     | 15.0 ms: 1.05x slower                                                          |
| generators                 | 22.5 ms                                                     | 23.7 ms: 1.05x slower                                                          |
| pprint_pformat             | 1.05 sec                                                    | 1.10 sec: 1.06x slower                                                         |
| xml_etree_process          | 37.7 ms                                                     | 40.7 ms: 1.08x slower                                                          |
| pycparser                  | 699 ms                                                      | 758 ms: 1.09x slower                                                           |
| meteor_contest             | 74.6 ms                                                     | 81.9 ms: 1.10x slower                                                          |
| pyflate                    | 295 ms                                                      | 324 ms: 1.10x slower                                                           |
| chaos                      | 43.3 ms                                                     | 47.8 ms: 1.10x slower                                                          |
| async_generators           | 239 ms                                                      | 265 ms: 1.11x slower                                                           |
| go                         | 91.6 ms                                                     | 102 ms: 1.11x slower                                                           |
| tornado_http               | 89.5 ms                                                     | 100 ms: 1.12x slower                                                           |
| pickle_pure_python         | 195 us                                                      | 219 us: 1.12x slower                                                           |
| deltablue                  | 2.16 ms                                                     | 2.43 ms: 1.13x slower                                                          |
| regex_compile              | 87.5 ms                                                     | 98.9 ms: 1.13x slower                                                          |
| unpickle_pure_python       | 133 us                                                      | 151 us: 1.13x slower                                                           |
| sympy_str                  | 175 ms                                                      | 199 ms: 1.14x slower                                                           |
| logging_silent             | 60.5 ns                                                     | 69.4 ns: 1.15x slower                                                          |
| raytrace                   | 192 ms                                                      | 221 ms: 1.15x slower                                                           |
| nqueens                    | 62.8 ms                                                     | 72.8 ms: 1.16x slower                                                          |
| mdp                        | 1.37 sec                                                    | 1.59 sec: 1.16x slower                                                         |
| python_startup_no_site     | 16.2 ms                                                     | 18.9 ms: 1.16x slower                                                          |
| sympy_sum                  | 91.5 ms                                                     | 107 ms: 1.16x slower                                                           |
| sqlglot_parse              | 804 us                                                      | 940 us: 1.17x slower                                                           |
| docutils                   | 1.66 sec                                                    | 1.94 sec: 1.17x slower                                                         |
| json_dumps                 | 5.70 ms                                                     | 6.71 ms: 1.18x slower                                                          |
| 2to3                       | 218 ms                                                      | 258 ms: 1.18x slower                                                           |
| telco                      | 4.13 ms                                                     | 4.90 ms: 1.19x slower                                                          |
| sympy_expand               | 284 ms                                                      | 337 ms: 1.19x slower                                                           |
| coverage                   | 40.8 ms                                                     | 49.6 ms: 1.21x slower                                                          |
| sqlglot_transpile          | 1.02 ms                                                     | 1.25 ms: 1.22x slower                                                          |
| sqlglot_normalize          | 187 ms                                                      | 228 ms: 1.22x slower                                                           |
| django_template            | 22.9 ms                                                     | 28.8 ms: 1.25x slower                                                          |
| sympy_integrate            | 13.0 ms                                                     | 16.5 ms: 1.27x slower                                                          |
| python_startup             | 19.5 ms                                                     | 24.8 ms: 1.27x slower                                                          |
| gc_traversal               | 1.52 ms                                                     | 1.96 ms: 1.29x slower                                                          |
| typing_runtime_protocols   | 95.1 us                                                     | 123 us: 1.30x slower                                                           |
| bench_mp_pool              | 69.2 ms                                                     | 89.7 ms: 1.30x slower                                                          |
| richards_super             | 32.1 ms                                                     | 42.5 ms: 1.33x slower                                                          |
| sqlglot_optimize           | 34.5 ms                                                     | 46.1 ms: 1.34x slower                                                          |
| richards                   | 28.4 ms                                                     | 38.6 ms: 1.36x slower                                                          |
| hexiom                     | 4.10 ms                                                     | 5.95 ms: 1.45x slower                                                          |
| create_gc_cycles           | 752 us                                                      | 1.39 ms: 1.85x slower                                                          |
| Geometric mean             | (ref)                                                       | 1.05x slower                                                                   |

Benchmark hidden because not significant (5): bench_thread_pool, pathlib, xml_etree_generate, logging_simple, json
Ignored benchmarks (15) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20241024-3.14.0a1+-9698931-JIT/bm-20241024-pythonperf1-amd64-brandtbucher-justin_no_externs-3.14.0a1+-9698931.json: genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift

- Geometric mean (including insignificant results): 1.041x slower
# HPT report

- Reliability score: 97.27% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown