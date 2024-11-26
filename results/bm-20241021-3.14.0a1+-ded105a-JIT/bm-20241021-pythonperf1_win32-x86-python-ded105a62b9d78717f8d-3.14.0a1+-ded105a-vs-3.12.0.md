# Results vs. 3.12.0

- fork: python
- ref: ded105a62b9d78717f8d
- machine: windows-x86
- commit hash: ded105a
- commit date: 2024-10-21
- overall geometric mean: 1.184x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.11x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241021-pythonperf1_win32-x86-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 263 ms: 1.06x faster                                                            |
| docutils       | 1.98 sec                                                        | 2.06 sec: 1.04x slower                                                          |
| tornado_http   | 105 ms                                                          | 110 ms: 1.05x slower                                                            |
| Geometric mean | (ref)                                                           | 1.01x slower                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241021-pythonperf1_win32-x86-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 350 ms                                                          | 254 ms: 1.38x faster                                                            |
| async_tree_none_tg         | 278 ms                                                          | 204 ms: 1.36x faster                                                            |
| async_tree_none            | 298 ms                                                          | 220 ms: 1.35x faster                                                            |
| async_tree_io              | 693 ms                                                          | 523 ms: 1.32x faster                                                            |
| async_tree_memoization     | 364 ms                                                          | 280 ms: 1.30x faster                                                            |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 467 ms: 1.21x faster                                                            |
| async_tree_io_tg           | 677 ms                                                          | 562 ms: 1.21x faster                                                            |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 466 ms: 1.17x faster                                                            |
| Geometric mean             | (ref)                                                           | 1.29x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241021-pythonperf1_win32-x86-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 65.9 ms: 1.93x faster                                                           |
| float          | 76.7 ms                                                         | 46.7 ms: 1.64x faster                                                           |
| pidigits       | 199 ms                                                          | 205 ms: 1.03x slower                                                            |
| Geometric mean | (ref)                                                           | 1.45x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241021-pythonperf1_win32-x86-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 104 ms: 1.24x faster                                                            |
| regex_effbot   | 2.04 ms                                                         | 1.90 ms: 1.07x faster                                                           |
| regex_dna      | 127 ms                                                          | 123 ms: 1.03x faster                                                            |
| regex_v8       | 15.0 ms                                                         | 15.6 ms: 1.04x slower                                                           |
| Geometric mean | (ref)                                                           | 1.07x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241021-pythonperf1_win32-x86-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 2.20 sec                                                        | 1.49 sec: 1.47x faster                                                          |
| unpickle_pure_python | 210 us                                                          | 159 us: 1.32x faster                                                            |
| xml_etree_generate   | 72.1 ms                                                         | 55.6 ms: 1.30x faster                                                           |
| xml_etree_process    | 53.2 ms                                                         | 41.4 ms: 1.29x faster                                                           |
| pickle_pure_python   | 286 us                                                          | 239 us: 1.20x faster                                                            |
| xml_etree_iterparse  | 77.6 ms                                                         | 65.2 ms: 1.19x faster                                                           |
| xml_etree_parse      | 113 ms                                                          | 111 ms: 1.02x faster                                                            |
| json_loads           | 20.4 us                                                         | 21.3 us: 1.05x slower                                                           |
| json_dumps           | 7.40 ms                                                         | 8.14 ms: 1.10x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.17x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241021-pythonperf1_win32-x86-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 20.2 ms: 1.06x slower                                                           |
| python_startup         | 22.4 ms                                                         | 27.0 ms: 1.21x slower                                                           |
| Geometric mean         | (ref)                                                           | 1.13x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241021-pythonperf1_win32-x86-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 5.68 ms: 1.75x faster                                                           |
| django_template | 36.9 ms                                                         | 33.4 ms: 1.11x faster                                                           |
| Geometric mean  | (ref)                                                           | 1.39x faster                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241021-pythonperf1_win32-x86-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| deepcopy_memo              | 38.4 us                                                         | 16.2 us: 2.37x faster                                                           |
| scimark_sor                | 130 ms                                                          | 66.5 ms: 1.95x faster                                                           |
| nbody                      | 127 ms                                                          | 65.9 ms: 1.93x faster                                                           |
| logging_silent             | 101 ns                                                          | 53.8 ns: 1.88x faster                                                           |
| spectral_norm              | 104 ms                                                          | 58.3 ms: 1.78x faster                                                           |
| mako                       | 9.96 ms                                                         | 5.68 ms: 1.75x faster                                                           |
| scimark_monte_carlo        | 66.4 ms                                                         | 39.0 ms: 1.70x faster                                                           |
| float                      | 76.7 ms                                                         | 46.7 ms: 1.64x faster                                                           |
| scimark_lu                 | 93.2 ms                                                         | 59.5 ms: 1.57x faster                                                           |
| deepcopy                   | 360 us                                                          | 231 us: 1.56x faster                                                            |
| generators                 | 38.5 ms                                                         | 24.7 ms: 1.56x faster                                                           |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 2.50 ms: 1.55x faster                                                           |
| scimark_fft                | 271 ms                                                          | 182 ms: 1.49x faster                                                            |
| tomli_loads                | 2.20 sec                                                        | 1.49 sec: 1.47x faster                                                          |
| comprehensions             | 19.2 us                                                         | 13.2 us: 1.46x faster                                                           |
| fannkuch                   | 354 ms                                                          | 248 ms: 1.42x faster                                                            |
| go                         | 137 ms                                                          | 96.7 ms: 1.42x faster                                                           |
| deltablue                  | 3.58 ms                                                         | 2.55 ms: 1.41x faster                                                           |
| crypto_pyaes               | 69.2 ms                                                         | 49.6 ms: 1.40x faster                                                           |
| async_tree_memoization_tg  | 350 ms                                                          | 254 ms: 1.38x faster                                                            |
| async_tree_none_tg         | 278 ms                                                          | 204 ms: 1.36x faster                                                            |
| async_tree_none            | 298 ms                                                          | 220 ms: 1.35x faster                                                            |
| deepcopy_reduce            | 3.23 us                                                         | 2.40 us: 1.34x faster                                                           |
| pyflate                    | 424 ms                                                          | 319 ms: 1.33x faster                                                            |
| async_tree_io              | 693 ms                                                          | 523 ms: 1.32x faster                                                            |
| unpickle_pure_python       | 210 us                                                          | 159 us: 1.32x faster                                                            |
| chaos                      | 69.4 ms                                                         | 52.8 ms: 1.31x faster                                                           |
| pprint_pformat             | 1.50 sec                                                        | 1.14 sec: 1.31x faster                                                          |
| async_tree_memoization     | 364 ms                                                          | 280 ms: 1.30x faster                                                            |
| xml_etree_generate         | 72.1 ms                                                         | 55.6 ms: 1.30x faster                                                           |
| hexiom                     | 6.82 ms                                                         | 5.27 ms: 1.29x faster                                                           |
| pprint_safe_repr           | 721 ms                                                          | 560 ms: 1.29x faster                                                            |
| xml_etree_process          | 53.2 ms                                                         | 41.4 ms: 1.29x faster                                                           |
| logging_simple             | 9.75 us                                                         | 7.63 us: 1.28x faster                                                           |
| nqueens                    | 93.7 ms                                                         | 73.9 ms: 1.27x faster                                                           |
| logging_format             | 10.4 us                                                         | 8.28 us: 1.26x faster                                                           |
| regex_compile              | 129 ms                                                          | 104 ms: 1.24x faster                                                            |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 467 ms: 1.21x faster                                                            |
| async_tree_io_tg           | 677 ms                                                          | 562 ms: 1.21x faster                                                            |
| pickle_pure_python         | 286 us                                                          | 239 us: 1.20x faster                                                            |
| xml_etree_iterparse        | 77.6 ms                                                         | 65.2 ms: 1.19x faster                                                           |
| meteor_contest             | 86.9 ms                                                         | 73.1 ms: 1.19x faster                                                           |
| pycparser                  | 978 ms                                                          | 824 ms: 1.19x faster                                                            |
| dulwich_log                | 58.5 ms                                                         | 49.3 ms: 1.19x faster                                                           |
| coroutines                 | 20.9 ms                                                         | 17.7 ms: 1.18x faster                                                           |
| sqlglot_parse              | 1.25 ms                                                         | 1.06 ms: 1.17x faster                                                           |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 466 ms: 1.17x faster                                                            |
| raytrace                   | 308 ms                                                          | 271 ms: 1.14x faster                                                            |
| sqlglot_transpile          | 1.53 ms                                                         | 1.37 ms: 1.12x faster                                                           |
| bench_thread_pool          | 1.10 ms                                                         | 991 us: 1.11x faster                                                            |
| django_template            | 36.9 ms                                                         | 33.4 ms: 1.11x faster                                                           |
| regex_effbot               | 2.04 ms                                                         | 1.90 ms: 1.07x faster                                                           |
| 2to3                       | 280 ms                                                          | 263 ms: 1.06x faster                                                            |
| richards                   | 41.3 ms                                                         | 39.3 ms: 1.05x faster                                                           |
| sympy_sum                  | 123 ms                                                          | 117 ms: 1.05x faster                                                            |
| sympy_str                  | 240 ms                                                          | 229 ms: 1.04x faster                                                            |
| richards_super             | 46.5 ms                                                         | 44.5 ms: 1.04x faster                                                           |
| mdp                        | 1.91 sec                                                        | 1.84 sec: 1.04x faster                                                          |
| pathlib                    | 91.4 ms                                                         | 88.1 ms: 1.04x faster                                                           |
| regex_dna                  | 127 ms                                                          | 123 ms: 1.03x faster                                                            |
| xml_etree_parse            | 113 ms                                                          | 111 ms: 1.02x faster                                                            |
| sympy_integrate            | 17.5 ms                                                         | 17.3 ms: 1.02x faster                                                           |
| async_generators           | 313 ms                                                          | 315 ms: 1.01x slower                                                            |
| sympy_expand               | 398 ms                                                          | 400 ms: 1.01x slower                                                            |
| sqlglot_optimize           | 48.5 ms                                                         | 49.8 ms: 1.03x slower                                                           |
| pidigits                   | 199 ms                                                          | 205 ms: 1.03x slower                                                            |
| regex_v8                   | 15.0 ms                                                         | 15.6 ms: 1.04x slower                                                           |
| docutils                   | 1.98 sec                                                        | 2.06 sec: 1.04x slower                                                          |
| tornado_http               | 105 ms                                                          | 110 ms: 1.05x slower                                                            |
| json_loads                 | 20.4 us                                                         | 21.3 us: 1.05x slower                                                           |
| python_startup_no_site     | 19.1 ms                                                         | 20.2 ms: 1.06x slower                                                           |
| telco                      | 5.51 ms                                                         | 6.06 ms: 1.10x slower                                                           |
| json_dumps                 | 7.40 ms                                                         | 8.14 ms: 1.10x slower                                                           |
| coverage                   | 48.4 ms                                                         | 54.1 ms: 1.12x slower                                                           |
| typing_runtime_protocols   | 126 us                                                          | 147 us: 1.16x slower                                                            |
| json                       | 4.15 ms                                                         | 5.01 ms: 1.21x slower                                                           |
| python_startup             | 22.4 ms                                                         | 27.0 ms: 1.21x slower                                                           |
| bench_mp_pool              | 75.4 ms                                                         | 94.1 ms: 1.25x slower                                                           |
| gc_traversal               | 1.44 ms                                                         | 1.82 ms: 1.27x slower                                                           |
| create_gc_cycles           | 652 us                                                          | 1.20 ms: 1.84x slower                                                           |
| sqlglot_normalize          | 100 ms                                                          | 240 ms: 2.40x slower                                                            |
| Geometric mean             | (ref)                                                           | 1.18x faster                                                                    |
Ignored benchmarks (15) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20241021-3.14.0a1+-ded105a-JIT/bm-20241021-pythonperf1_win32-x86-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a.json: genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift

- Geometric mean (including insignificant results): 1.184x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.16x
- 95% likely to have a speedup of 1.15x
- 99% likely to have a speedup of 1.11x

# Memory
- memory change: unknown