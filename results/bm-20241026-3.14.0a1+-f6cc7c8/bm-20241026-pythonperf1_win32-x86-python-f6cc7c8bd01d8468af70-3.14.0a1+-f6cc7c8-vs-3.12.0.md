# Results vs. 3.12.0

- fork: python
- ref: f6cc7c8bd01d8468af70
- machine: windows-x86
- commit hash: f6cc7c8
- commit date: 2024-10-26
- overall geometric mean: 1.111x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.10x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241026-pythonperf1_win32-x86-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 248 ms: 1.13x faster                                                            |
| docutils       | 1.98 sec                                                        | 1.87 sec: 1.06x faster                                                          |
| Geometric mean | (ref)                                                           | 1.07x faster                                                                    |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241026-pythonperf1_win32-x86-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 350 ms                                                          | 262 ms: 1.34x faster                                                            |
| async_tree_none_tg         | 278 ms                                                          | 208 ms: 1.33x faster                                                            |
| async_tree_none            | 298 ms                                                          | 226 ms: 1.32x faster                                                            |
| async_tree_io              | 693 ms                                                          | 534 ms: 1.30x faster                                                            |
| async_tree_memoization     | 364 ms                                                          | 281 ms: 1.30x faster                                                            |
| async_tree_io_tg           | 677 ms                                                          | 562 ms: 1.21x faster                                                            |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 477 ms: 1.18x faster                                                            |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 471 ms: 1.16x faster                                                            |
| Geometric mean             | (ref)                                                           | 1.26x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241026-pythonperf1_win32-x86-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 88.2 ms: 1.44x faster                                                           |
| float          | 76.7 ms                                                         | 61.5 ms: 1.25x faster                                                           |
| pidigits       | 199 ms                                                          | 204 ms: 1.02x slower                                                            |
| Geometric mean | (ref)                                                           | 1.21x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241026-pythonperf1_win32-x86-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 108 ms: 1.19x faster                                                            |
| regex_effbot   | 2.04 ms                                                         | 1.81 ms: 1.13x faster                                                           |
| regex_dna      | 127 ms                                                          | 113 ms: 1.12x faster                                                            |
| regex_v8       | 15.0 ms                                                         | 15.8 ms: 1.05x slower                                                           |
| Geometric mean | (ref)                                                           | 1.09x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241026-pythonperf1_win32-x86-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 2.20 sec                                                        | 1.82 sec: 1.20x faster                                                          |
| unpickle_pure_python | 210 us                                                          | 179 us: 1.17x faster                                                            |
| xml_etree_iterparse  | 77.6 ms                                                         | 68.7 ms: 1.13x faster                                                           |
| xml_etree_process    | 53.2 ms                                                         | 47.6 ms: 1.12x faster                                                           |
| xml_etree_generate   | 72.1 ms                                                         | 65.8 ms: 1.10x faster                                                           |
| pickle_pure_python   | 286 us                                                          | 266 us: 1.08x faster                                                            |
| xml_etree_parse      | 113 ms                                                          | 112 ms: 1.01x faster                                                            |
| json_loads           | 20.4 us                                                         | 21.0 us: 1.03x slower                                                           |
| json_dumps           | 7.40 ms                                                         | 9.04 ms: 1.22x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.06x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241026-pythonperf1_win32-x86-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 20.1 ms: 1.05x slower                                                           |
| python_startup         | 22.4 ms                                                         | 26.8 ms: 1.20x slower                                                           |
| Geometric mean         | (ref)                                                           | 1.13x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241026-pythonperf1_win32-x86-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 7.78 ms: 1.28x faster                                                           |
| django_template | 36.9 ms                                                         | 34.0 ms: 1.09x faster                                                           |
| Geometric mean  | (ref)                                                           | 1.18x faster                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241026-pythonperf1_win32-x86-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| deepcopy_memo              | 38.4 us                                                         | 21.9 us: 1.75x faster                                                           |
| generators                 | 38.5 ms                                                         | 24.1 ms: 1.60x faster                                                           |
| deepcopy                   | 360 us                                                          | 238 us: 1.51x faster                                                            |
| logging_silent             | 101 ns                                                          | 69.7 ns: 1.45x faster                                                           |
| nbody                      | 127 ms                                                          | 88.2 ms: 1.44x faster                                                           |
| go                         | 137 ms                                                          | 100 ms: 1.37x faster                                                            |
| comprehensions             | 19.2 us                                                         | 14.0 us: 1.37x faster                                                           |
| deltablue                  | 3.58 ms                                                         | 2.65 ms: 1.35x faster                                                           |
| scimark_lu                 | 93.2 ms                                                         | 69.2 ms: 1.35x faster                                                           |
| spectral_norm              | 104 ms                                                          | 77.4 ms: 1.34x faster                                                           |
| async_tree_memoization_tg  | 350 ms                                                          | 262 ms: 1.34x faster                                                            |
| async_tree_none_tg         | 278 ms                                                          | 208 ms: 1.33x faster                                                            |
| hexiom                     | 6.82 ms                                                         | 5.16 ms: 1.32x faster                                                           |
| async_tree_none            | 298 ms                                                          | 226 ms: 1.32x faster                                                            |
| deepcopy_reduce            | 3.23 us                                                         | 2.46 us: 1.31x faster                                                           |
| async_tree_io              | 693 ms                                                          | 534 ms: 1.30x faster                                                            |
| async_tree_memoization     | 364 ms                                                          | 281 ms: 1.30x faster                                                            |
| mako                       | 9.96 ms                                                         | 7.78 ms: 1.28x faster                                                           |
| float                      | 76.7 ms                                                         | 61.5 ms: 1.25x faster                                                           |
| raytrace                   | 308 ms                                                          | 250 ms: 1.23x faster                                                            |
| logging_simple             | 9.75 us                                                         | 7.98 us: 1.22x faster                                                           |
| scimark_sor                | 130 ms                                                          | 106 ms: 1.22x faster                                                            |
| logging_format             | 10.4 us                                                         | 8.58 us: 1.21x faster                                                           |
| async_tree_io_tg           | 677 ms                                                          | 562 ms: 1.21x faster                                                            |
| tomli_loads                | 2.20 sec                                                        | 1.82 sec: 1.20x faster                                                          |
| chaos                      | 69.4 ms                                                         | 57.7 ms: 1.20x faster                                                           |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 3.21 ms: 1.20x faster                                                           |
| regex_compile              | 129 ms                                                          | 108 ms: 1.19x faster                                                            |
| coroutines                 | 20.9 ms                                                         | 17.6 ms: 1.19x faster                                                           |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 477 ms: 1.18x faster                                                            |
| nqueens                    | 93.7 ms                                                         | 79.6 ms: 1.18x faster                                                           |
| unpickle_pure_python       | 210 us                                                          | 179 us: 1.17x faster                                                            |
| scimark_monte_carlo        | 66.4 ms                                                         | 57.0 ms: 1.17x faster                                                           |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 471 ms: 1.16x faster                                                            |
| crypto_pyaes               | 69.2 ms                                                         | 59.8 ms: 1.16x faster                                                           |
| pyflate                    | 424 ms                                                          | 368 ms: 1.15x faster                                                            |
| pycparser                  | 978 ms                                                          | 850 ms: 1.15x faster                                                            |
| sympy_sum                  | 123 ms                                                          | 107 ms: 1.15x faster                                                            |
| sqlglot_parse              | 1.25 ms                                                         | 1.10 ms: 1.14x faster                                                           |
| sqlglot_transpile          | 1.53 ms                                                         | 1.35 ms: 1.13x faster                                                           |
| xml_etree_iterparse        | 77.6 ms                                                         | 68.7 ms: 1.13x faster                                                           |
| 2to3                       | 280 ms                                                          | 248 ms: 1.13x faster                                                            |
| regex_effbot               | 2.04 ms                                                         | 1.81 ms: 1.13x faster                                                           |
| fannkuch                   | 354 ms                                                          | 314 ms: 1.13x faster                                                            |
| regex_dna                  | 127 ms                                                          | 113 ms: 1.12x faster                                                            |
| dulwich_log                | 58.5 ms                                                         | 52.1 ms: 1.12x faster                                                           |
| xml_etree_process          | 53.2 ms                                                         | 47.6 ms: 1.12x faster                                                           |
| sympy_integrate            | 17.5 ms                                                         | 15.7 ms: 1.11x faster                                                           |
| pprint_safe_repr           | 721 ms                                                          | 651 ms: 1.11x faster                                                            |
| pprint_pformat             | 1.50 sec                                                        | 1.36 sec: 1.10x faster                                                          |
| scimark_fft                | 271 ms                                                          | 246 ms: 1.10x faster                                                            |
| bench_thread_pool          | 1.10 ms                                                         | 1.00 ms: 1.10x faster                                                           |
| sqlglot_optimize           | 48.5 ms                                                         | 44.1 ms: 1.10x faster                                                           |
| sympy_str                  | 240 ms                                                          | 218 ms: 1.10x faster                                                            |
| xml_etree_generate         | 72.1 ms                                                         | 65.8 ms: 1.10x faster                                                           |
| django_template            | 36.9 ms                                                         | 34.0 ms: 1.09x faster                                                           |
| meteor_contest             | 86.9 ms                                                         | 80.4 ms: 1.08x faster                                                           |
| pickle_pure_python         | 286 us                                                          | 266 us: 1.08x faster                                                            |
| async_generators           | 313 ms                                                          | 295 ms: 1.06x faster                                                            |
| docutils                   | 1.98 sec                                                        | 1.87 sec: 1.06x faster                                                          |
| richards                   | 41.3 ms                                                         | 39.2 ms: 1.06x faster                                                           |
| richards_super             | 46.5 ms                                                         | 44.1 ms: 1.05x faster                                                           |
| mdp                        | 1.91 sec                                                        | 1.81 sec: 1.05x faster                                                          |
| sympy_expand               | 398 ms                                                          | 383 ms: 1.04x faster                                                            |
| pathlib                    | 91.4 ms                                                         | 89.6 ms: 1.02x faster                                                           |
| xml_etree_parse            | 113 ms                                                          | 112 ms: 1.01x faster                                                            |
| pidigits                   | 199 ms                                                          | 204 ms: 1.02x slower                                                            |
| json_loads                 | 20.4 us                                                         | 21.0 us: 1.03x slower                                                           |
| regex_v8                   | 15.0 ms                                                         | 15.8 ms: 1.05x slower                                                           |
| python_startup_no_site     | 19.1 ms                                                         | 20.1 ms: 1.05x slower                                                           |
| typing_runtime_protocols   | 126 us                                                          | 143 us: 1.13x slower                                                            |
| coverage                   | 48.4 ms                                                         | 56.4 ms: 1.16x slower                                                           |
| bench_mp_pool              | 75.4 ms                                                         | 88.8 ms: 1.18x slower                                                           |
| python_startup             | 22.4 ms                                                         | 26.8 ms: 1.20x slower                                                           |
| json_dumps                 | 7.40 ms                                                         | 9.04 ms: 1.22x slower                                                           |
| gc_traversal               | 1.44 ms                                                         | 1.80 ms: 1.25x slower                                                           |
| telco                      | 5.51 ms                                                         | 7.00 ms: 1.27x slower                                                           |
| json                       | 4.15 ms                                                         | 5.89 ms: 1.42x slower                                                           |
| create_gc_cycles           | 652 us                                                          | 1.18 ms: 1.82x slower                                                           |
| sqlglot_normalize          | 100 ms                                                          | 234 ms: 2.34x slower                                                            |
| Geometric mean             | (ref)                                                           | 1.11x faster                                                                    |

Benchmark hidden because not significant (1): tornado_http
Ignored benchmarks (15) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20241026-3.14.0a1+-f6cc7c8/bm-20241026-pythonperf1_win32-x86-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8.json: genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift

- Geometric mean (including insignificant results): 1.111x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.11x
- 95% likely to have a speedup of 1.11x
- 99% likely to have a speedup of 1.10x

# Memory
- memory change: unknown