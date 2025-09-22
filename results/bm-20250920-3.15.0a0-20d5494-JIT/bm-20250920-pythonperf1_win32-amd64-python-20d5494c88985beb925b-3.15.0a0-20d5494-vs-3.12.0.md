# Results vs. 3.12.0

- fork: python
- ref: 20d5494c88985beb925b
- machine: windows-amd64
- commit hash: 20d5494
- commit date: 2025-09-20
- overall geometric mean: 1.511x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.45x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250920-pythonperf1_win32-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 222 ms: 1.26x faster                                                             |
| docutils       | 1.98 sec                                                        | 1.66 sec: 1.20x faster                                                           |
| Geometric mean | (ref)                                                           | 1.23x faster                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250920-pythonperf1_win32-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494 |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_io              | 693 ms                                                          | 386 ms: 1.80x faster                                                             |
| async_tree_memoization     | 364 ms                                                          | 206 ms: 1.77x faster                                                             |
| async_tree_io_tg           | 677 ms                                                          | 385 ms: 1.76x faster                                                             |
| async_tree_none            | 298 ms                                                          | 173 ms: 1.72x faster                                                             |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 331 ms: 1.70x faster                                                             |
| async_tree_none_tg         | 278 ms                                                          | 165 ms: 1.69x faster                                                             |
| async_tree_memoization_tg  | 350 ms                                                          | 210 ms: 1.67x faster                                                             |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 339 ms: 1.61x faster                                                             |
| Geometric mean             | (ref)                                                           | 1.71x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250920-pythonperf1_win32-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 55.0 ms: 2.31x faster                                                            |
| float          | 76.7 ms                                                         | 39.7 ms: 1.93x faster                                                            |
| pidigits       | 199 ms                                                          | 148 ms: 1.35x faster                                                             |
| Geometric mean | (ref)                                                           | 1.82x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250920-pythonperf1_win32-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 77.8 ms: 1.66x faster                                                            |
| regex_effbot   | 2.04 ms                                                         | 1.54 ms: 1.32x faster                                                            |
| regex_v8       | 15.0 ms                                                         | 14.2 ms: 1.06x faster                                                            |
| regex_dna      | 127 ms                                                          | 121 ms: 1.05x faster                                                             |
| Geometric mean | (ref)                                                           | 1.25x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250920-pythonperf1_win32-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494 |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| tomli_loads          | 2.20 sec                                                        | 1.10 sec: 2.00x faster                                                           |
| unpickle_pure_python | 210 us                                                          | 107 us: 1.97x faster                                                             |
| xml_etree_process    | 53.2 ms                                                         | 35.2 ms: 1.51x faster                                                            |
| json_loads           | 20.4 us                                                         | 14.0 us: 1.45x faster                                                            |
| xml_etree_generate   | 72.1 ms                                                         | 49.8 ms: 1.45x faster                                                            |
| pickle_pure_python   | 286 us                                                          | 199 us: 1.43x faster                                                             |
| json_dumps           | 7.40 ms                                                         | 5.38 ms: 1.37x faster                                                            |
| xml_etree_parse      | 113 ms                                                          | 86.2 ms: 1.31x faster                                                            |
| xml_etree_iterparse  | 77.6 ms                                                         | 61.7 ms: 1.26x faster                                                            |
| unpickle             | 9.71 us                                                         | 8.47 us: 1.15x faster                                                            |
| unpickle_list        | 2.95 us                                                         | 2.72 us: 1.08x faster                                                            |
| pickle               | 7.79 us                                                         | 7.98 us: 1.02x slower                                                            |
| Geometric mean       | (ref)                                                           | 1.32x faster                                                                     |

Benchmark hidden because not significant (2): pickle_dict, pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250920-pythonperf1_win32-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494 |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 19.3 ms: 1.01x slower                                                            |
| python_startup         | 22.4 ms                                                         | 25.5 ms: 1.14x slower                                                            |
| Geometric mean         | (ref)                                                           | 1.07x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250920-pythonperf1_win32-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494 |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 5.26 ms: 1.89x faster                                                            |
| django_template | 36.9 ms                                                         | 24.1 ms: 1.53x faster                                                            |
| Geometric mean  | (ref)                                                           | 1.70x faster                                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250920-pythonperf1_win32-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494 |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| asyncio_tcp_ssl            | 17.7 sec                                                        | 1.38 sec: 12.77x faster                                                          |
| pathlib                    | 91.4 ms                                                         | 29.6 ms: 3.09x faster                                                            |
| mdp                        | 1.91 sec                                                        | 820 ms: 2.33x faster                                                             |
| nbody                      | 127 ms                                                          | 55.0 ms: 2.31x faster                                                            |
| deepcopy_memo              | 38.4 us                                                         | 16.9 us: 2.26x faster                                                            |
| deepcopy                   | 360 us                                                          | 167 us: 2.15x faster                                                             |
| tomli_loads                | 2.20 sec                                                        | 1.10 sec: 2.00x faster                                                           |
| generators                 | 38.5 ms                                                         | 19.5 ms: 1.97x faster                                                            |
| unpickle_pure_python       | 210 us                                                          | 107 us: 1.97x faster                                                             |
| float                      | 76.7 ms                                                         | 39.7 ms: 1.93x faster                                                            |
| unpack_sequence            | 62.5 ns                                                         | 32.4 ns: 1.93x faster                                                            |
| mako                       | 9.96 ms                                                         | 5.26 ms: 1.89x faster                                                            |
| logging_silent             | 101 ns                                                          | 54.2 ns: 1.87x faster                                                            |
| scimark_fft                | 271 ms                                                          | 149 ms: 1.82x faster                                                             |
| go                         | 137 ms                                                          | 76.4 ms: 1.80x faster                                                            |
| async_tree_io              | 693 ms                                                          | 386 ms: 1.80x faster                                                             |
| comprehensions             | 19.2 us                                                         | 10.7 us: 1.79x faster                                                            |
| deepcopy_reduce            | 3.23 us                                                         | 1.81 us: 1.78x faster                                                            |
| async_tree_memoization     | 364 ms                                                          | 206 ms: 1.77x faster                                                             |
| async_tree_io_tg           | 677 ms                                                          | 385 ms: 1.76x faster                                                             |
| raytrace                   | 308 ms                                                          | 177 ms: 1.74x faster                                                             |
| async_tree_none            | 298 ms                                                          | 173 ms: 1.72x faster                                                             |
| pprint_pformat             | 1.50 sec                                                        | 873 ms: 1.72x faster                                                             |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 331 ms: 1.70x faster                                                             |
| chaos                      | 69.4 ms                                                         | 41.1 ms: 1.69x faster                                                            |
| async_tree_none_tg         | 278 ms                                                          | 165 ms: 1.69x faster                                                             |
| pprint_safe_repr           | 721 ms                                                          | 430 ms: 1.68x faster                                                             |
| pyflate                    | 424 ms                                                          | 253 ms: 1.67x faster                                                             |
| async_tree_memoization_tg  | 350 ms                                                          | 210 ms: 1.67x faster                                                             |
| fannkuch                   | 354 ms                                                          | 212 ms: 1.67x faster                                                             |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 2.32 ms: 1.67x faster                                                            |
| regex_compile              | 129 ms                                                          | 77.8 ms: 1.66x faster                                                            |
| hexiom                     | 6.82 ms                                                         | 4.12 ms: 1.65x faster                                                            |
| scimark_sor                | 130 ms                                                          | 78.5 ms: 1.65x faster                                                            |
| scimark_monte_carlo        | 66.4 ms                                                         | 40.5 ms: 1.64x faster                                                            |
| logging_simple             | 9.75 us                                                         | 6.03 us: 1.62x faster                                                            |
| deltablue                  | 3.58 ms                                                         | 2.22 ms: 1.61x faster                                                            |
| scimark_lu                 | 93.2 ms                                                         | 57.8 ms: 1.61x faster                                                            |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 339 ms: 1.61x faster                                                             |
| logging_format             | 10.4 us                                                         | 6.47 us: 1.61x faster                                                            |
| spectral_norm              | 104 ms                                                          | 67.2 ms: 1.54x faster                                                            |
| django_template            | 36.9 ms                                                         | 24.1 ms: 1.53x faster                                                            |
| nqueens                    | 93.7 ms                                                         | 61.3 ms: 1.53x faster                                                            |
| xml_etree_process          | 53.2 ms                                                         | 35.2 ms: 1.51x faster                                                            |
| crypto_pyaes               | 69.2 ms                                                         | 46.0 ms: 1.50x faster                                                            |
| richards                   | 41.3 ms                                                         | 27.5 ms: 1.50x faster                                                            |
| richards_super             | 46.5 ms                                                         | 31.0 ms: 1.50x faster                                                            |
| json_loads                 | 20.4 us                                                         | 14.0 us: 1.45x faster                                                            |
| xml_etree_generate         | 72.1 ms                                                         | 49.8 ms: 1.45x faster                                                            |
| coroutines                 | 20.9 ms                                                         | 14.4 ms: 1.45x faster                                                            |
| dulwich_log                | 58.5 ms                                                         | 40.8 ms: 1.43x faster                                                            |
| pickle_pure_python         | 286 us                                                          | 199 us: 1.43x faster                                                             |
| json                       | 4.15 ms                                                         | 2.91 ms: 1.43x faster                                                            |
| sympy_sum                  | 123 ms                                                          | 87.4 ms: 1.41x faster                                                            |
| asyncio_tcp                | 662 ms                                                          | 472 ms: 1.40x faster                                                             |
| sympy_str                  | 240 ms                                                          | 171 ms: 1.40x faster                                                             |
| pycparser                  | 978 ms                                                          | 701 ms: 1.39x faster                                                             |
| telco                      | 5.51 ms                                                         | 3.98 ms: 1.38x faster                                                            |
| sympy_integrate            | 17.5 ms                                                         | 12.7 ms: 1.38x faster                                                            |
| json_dumps                 | 7.40 ms                                                         | 5.38 ms: 1.37x faster                                                            |
| pidigits                   | 199 ms                                                          | 148 ms: 1.35x faster                                                             |
| sympy_expand               | 398 ms                                                          | 296 ms: 1.34x faster                                                             |
| sqlite_synth               | 2.07 us                                                         | 1.55 us: 1.34x faster                                                            |
| regex_effbot               | 2.04 ms                                                         | 1.54 ms: 1.32x faster                                                            |
| xml_etree_parse            | 113 ms                                                          | 86.2 ms: 1.31x faster                                                            |
| bench_thread_pool          | 1.10 ms                                                         | 851 us: 1.30x faster                                                             |
| async_generators           | 313 ms                                                          | 246 ms: 1.27x faster                                                             |
| 2to3                       | 280 ms                                                          | 222 ms: 1.26x faster                                                             |
| xml_etree_iterparse        | 77.6 ms                                                         | 61.7 ms: 1.26x faster                                                            |
| typing_runtime_protocols   | 126 us                                                          | 102 us: 1.24x faster                                                             |
| docutils                   | 1.98 sec                                                        | 1.66 sec: 1.20x faster                                                           |
| meteor_contest             | 86.9 ms                                                         | 72.7 ms: 1.19x faster                                                            |
| unpickle                   | 9.71 us                                                         | 8.47 us: 1.15x faster                                                            |
| unpickle_list              | 2.95 us                                                         | 2.72 us: 1.08x faster                                                            |
| regex_v8                   | 15.0 ms                                                         | 14.2 ms: 1.06x faster                                                            |
| regex_dna                  | 127 ms                                                          | 121 ms: 1.05x faster                                                             |
| python_startup_no_site     | 19.1 ms                                                         | 19.3 ms: 1.01x slower                                                            |
| coverage                   | 48.4 ms                                                         | 49.1 ms: 1.01x slower                                                            |
| pickle                     | 7.79 us                                                         | 7.98 us: 1.02x slower                                                            |
| python_startup             | 22.4 ms                                                         | 25.5 ms: 1.14x slower                                                            |
| bench_mp_pool              | 75.4 ms                                                         | 91.1 ms: 1.21x slower                                                            |
| gc_traversal               | 1.44 ms                                                         | 2.14 ms: 1.48x slower                                                            |
| create_gc_cycles           | 652 us                                                          | 1.29 ms: 1.98x slower                                                            |
| Geometric mean             | (ref)                                                           | 1.51x faster                                                                     |

Benchmark hidden because not significant (2): pickle_dict, pickle_list
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (17) of results/bm-20250920-3.15.0a0-20d5494-JIT/bm-20250920-pythonperf1_win32-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.511x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.51x
- 95% likely to have a speedup of 1.50x
- 99% likely to have a speedup of 1.45x

# Memory
- memory change: unknown