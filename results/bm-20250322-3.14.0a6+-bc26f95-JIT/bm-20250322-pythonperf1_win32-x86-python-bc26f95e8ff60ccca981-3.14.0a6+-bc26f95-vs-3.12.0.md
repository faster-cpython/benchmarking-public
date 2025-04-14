# Results vs. 3.12.0

- fork: python
- ref: bc26f95e8ff60ccca981
- machine: windows-x86
- commit hash: bc26f95
- commit date: 2025-03-22
- overall geometric mean: 1.042x faster
- HPT reliability: 96.37%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250322-pythonperf1_win32-x86-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 287 ms: 1.03x slower                                                            |
| docutils       | 1.98 sec                                                        | 2.03 sec: 1.02x slower                                                          |
| Geometric mean | (ref)                                                           | 1.02x slower                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250322-pythonperf1_win32-x86-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_io_tg           | 677 ms                                                          | 501 ms: 1.35x faster                                                            |
| async_tree_io              | 693 ms                                                          | 513 ms: 1.35x faster                                                            |
| async_tree_memoization_tg  | 350 ms                                                          | 262 ms: 1.34x faster                                                            |
| async_tree_memoization     | 364 ms                                                          | 281 ms: 1.30x faster                                                            |
| async_tree_none_tg         | 278 ms                                                          | 215 ms: 1.29x faster                                                            |
| async_tree_none            | 298 ms                                                          | 241 ms: 1.23x faster                                                            |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 485 ms: 1.13x faster                                                            |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 506 ms: 1.11x faster                                                            |
| Geometric mean             | (ref)                                                           | 1.26x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250322-pythonperf1_win32-x86-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 76.7 ms                                                         | 59.0 ms: 1.30x faster                                                           |
| pidigits       | 199 ms                                                          | 201 ms: 1.01x slower                                                            |
| nbody          | 127 ms                                                          | 130 ms: 1.02x slower                                                            |
| Geometric mean | (ref)                                                           | 1.08x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250322-pythonperf1_win32-x86-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_effbot   | 2.04 ms                                                         | 1.59 ms: 1.28x faster                                                           |
| regex_dna      | 127 ms                                                          | 115 ms: 1.11x faster                                                            |
| regex_compile  | 129 ms                                                          | 120 ms: 1.08x faster                                                            |
| Geometric mean | (ref)                                                           | 1.11x faster                                                                    |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250322-pythonperf1_win32-x86-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 2.20 sec                                                        | 1.96 sec: 1.12x faster                                                          |
| xml_etree_iterparse  | 77.6 ms                                                         | 71.2 ms: 1.09x faster                                                           |
| xml_etree_parse      | 113 ms                                                          | 112 ms: 1.01x faster                                                            |
| pickle_dict          | 19.9 us                                                         | 21.4 us: 1.07x slower                                                           |
| json_loads           | 20.4 us                                                         | 22.0 us: 1.08x slower                                                           |
| xml_etree_generate   | 72.1 ms                                                         | 78.0 ms: 1.08x slower                                                           |
| unpickle_list        | 2.95 us                                                         | 3.19 us: 1.08x slower                                                           |
| unpickle             | 9.71 us                                                         | 10.5 us: 1.08x slower                                                           |
| xml_etree_process    | 53.2 ms                                                         | 58.9 ms: 1.11x slower                                                           |
| pickle_list          | 3.37 us                                                         | 3.85 us: 1.14x slower                                                           |
| json_dumps           | 7.40 ms                                                         | 8.55 ms: 1.16x slower                                                           |
| unpickle_pure_python | 210 us                                                          | 254 us: 1.21x slower                                                            |
| pickle               | 7.79 us                                                         | 9.50 us: 1.22x slower                                                           |
| pickle_pure_python   | 286 us                                                          | 350 us: 1.22x slower                                                            |
| Geometric mean       | (ref)                                                           | 1.08x slower                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250322-pythonperf1_win32-x86-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 22.8 ms: 1.19x slower                                                           |
| python_startup         | 22.4 ms                                                         | 28.7 ms: 1.28x slower                                                           |
| Geometric mean         | (ref)                                                           | 1.24x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250322-pythonperf1_win32-x86-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 8.05 ms: 1.24x faster                                                           |
| django_template | 36.9 ms                                                         | 37.2 ms: 1.01x slower                                                           |
| Geometric mean  | (ref)                                                           | 1.11x faster                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250322-pythonperf1_win32-x86-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pathlib                    | 91.4 ms                                                         | 38.1 ms: 2.40x faster                                                           |
| deepcopy_memo              | 38.4 us                                                         | 23.8 us: 1.61x faster                                                           |
| async_tree_io_tg           | 677 ms                                                          | 501 ms: 1.35x faster                                                            |
| async_tree_io              | 693 ms                                                          | 513 ms: 1.35x faster                                                            |
| async_tree_memoization_tg  | 350 ms                                                          | 262 ms: 1.34x faster                                                            |
| deepcopy                   | 360 us                                                          | 275 us: 1.31x faster                                                            |
| float                      | 76.7 ms                                                         | 59.0 ms: 1.30x faster                                                           |
| async_tree_memoization     | 364 ms                                                          | 281 ms: 1.30x faster                                                            |
| async_tree_none_tg         | 278 ms                                                          | 215 ms: 1.29x faster                                                            |
| regex_effbot               | 2.04 ms                                                         | 1.59 ms: 1.28x faster                                                           |
| generators                 | 38.5 ms                                                         | 30.0 ms: 1.28x faster                                                           |
| spectral_norm              | 104 ms                                                          | 82.8 ms: 1.25x faster                                                           |
| mako                       | 9.96 ms                                                         | 8.05 ms: 1.24x faster                                                           |
| async_tree_none            | 298 ms                                                          | 241 ms: 1.23x faster                                                            |
| logging_silent             | 101 ns                                                          | 82.6 ns: 1.22x faster                                                           |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 3.19 ms: 1.21x faster                                                           |
| scimark_sor                | 130 ms                                                          | 108 ms: 1.20x faster                                                            |
| scimark_lu                 | 93.2 ms                                                         | 78.1 ms: 1.19x faster                                                           |
| coroutines                 | 20.9 ms                                                         | 17.8 ms: 1.17x faster                                                           |
| raytrace                   | 308 ms                                                          | 266 ms: 1.16x faster                                                            |
| deepcopy_reduce            | 3.23 us                                                         | 2.80 us: 1.15x faster                                                           |
| scimark_monte_carlo        | 66.4 ms                                                         | 58.8 ms: 1.13x faster                                                           |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 485 ms: 1.13x faster                                                            |
| tomli_loads                | 2.20 sec                                                        | 1.96 sec: 1.12x faster                                                          |
| go                         | 137 ms                                                          | 123 ms: 1.12x faster                                                            |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 506 ms: 1.11x faster                                                            |
| unpack_sequence            | 62.5 ns                                                         | 56.0 ns: 1.11x faster                                                           |
| deltablue                  | 3.58 ms                                                         | 3.23 ms: 1.11x faster                                                           |
| regex_dna                  | 127 ms                                                          | 115 ms: 1.11x faster                                                            |
| chaos                      | 69.4 ms                                                         | 63.2 ms: 1.10x faster                                                           |
| sqlite_synth               | 2.07 us                                                         | 1.90 us: 1.09x faster                                                           |
| xml_etree_iterparse        | 77.6 ms                                                         | 71.2 ms: 1.09x faster                                                           |
| dulwich_log                | 58.5 ms                                                         | 53.9 ms: 1.09x faster                                                           |
| regex_compile              | 129 ms                                                          | 120 ms: 1.08x faster                                                            |
| pyflate                    | 424 ms                                                          | 399 ms: 1.06x faster                                                            |
| logging_simple             | 9.75 us                                                         | 9.20 us: 1.06x faster                                                           |
| logging_format             | 10.4 us                                                         | 9.92 us: 1.05x faster                                                           |
| sympy_sum                  | 123 ms                                                          | 117 ms: 1.05x faster                                                            |
| mdp                        | 1.91 sec                                                        | 1.83 sec: 1.05x faster                                                          |
| sympy_integrate            | 17.5 ms                                                         | 17.1 ms: 1.03x faster                                                           |
| asyncio_tcp_ssl            | 17.7 sec                                                        | 17.2 sec: 1.02x faster                                                          |
| scimark_fft                | 271 ms                                                          | 268 ms: 1.01x faster                                                            |
| xml_etree_parse            | 113 ms                                                          | 112 ms: 1.01x faster                                                            |
| comprehensions             | 19.2 us                                                         | 19.3 us: 1.00x slower                                                           |
| django_template            | 36.9 ms                                                         | 37.2 ms: 1.01x slower                                                           |
| richards                   | 41.3 ms                                                         | 41.6 ms: 1.01x slower                                                           |
| pidigits                   | 199 ms                                                          | 201 ms: 1.01x slower                                                            |
| richards_super             | 46.5 ms                                                         | 47.1 ms: 1.01x slower                                                           |
| hexiom                     | 6.82 ms                                                         | 6.92 ms: 1.02x slower                                                           |
| docutils                   | 1.98 sec                                                        | 2.03 sec: 1.02x slower                                                          |
| nbody                      | 127 ms                                                          | 130 ms: 1.02x slower                                                            |
| 2to3                       | 280 ms                                                          | 287 ms: 1.03x slower                                                            |
| asyncio_tcp                | 662 ms                                                          | 691 ms: 1.04x slower                                                            |
| pycparser                  | 978 ms                                                          | 1.03 sec: 1.05x slower                                                          |
| sympy_expand               | 398 ms                                                          | 421 ms: 1.06x slower                                                            |
| pickle_dict                | 19.9 us                                                         | 21.4 us: 1.07x slower                                                           |
| pprint_pformat             | 1.50 sec                                                        | 1.61 sec: 1.08x slower                                                          |
| json_loads                 | 20.4 us                                                         | 22.0 us: 1.08x slower                                                           |
| xml_etree_generate         | 72.1 ms                                                         | 78.0 ms: 1.08x slower                                                           |
| unpickle_list              | 2.95 us                                                         | 3.19 us: 1.08x slower                                                           |
| unpickle                   | 9.71 us                                                         | 10.5 us: 1.08x slower                                                           |
| async_generators           | 313 ms                                                          | 340 ms: 1.09x slower                                                            |
| nqueens                    | 93.7 ms                                                         | 102 ms: 1.09x slower                                                            |
| pprint_safe_repr           | 721 ms                                                          | 793 ms: 1.10x slower                                                            |
| meteor_contest             | 86.9 ms                                                         | 96.1 ms: 1.11x slower                                                           |
| xml_etree_process          | 53.2 ms                                                         | 58.9 ms: 1.11x slower                                                           |
| fannkuch                   | 354 ms                                                          | 391 ms: 1.11x slower                                                            |
| json                       | 4.15 ms                                                         | 4.61 ms: 1.11x slower                                                           |
| pickle_list                | 3.37 us                                                         | 3.85 us: 1.14x slower                                                           |
| coverage                   | 48.4 ms                                                         | 55.9 ms: 1.15x slower                                                           |
| json_dumps                 | 7.40 ms                                                         | 8.55 ms: 1.16x slower                                                           |
| python_startup_no_site     | 19.1 ms                                                         | 22.8 ms: 1.19x slower                                                           |
| unpickle_pure_python       | 210 us                                                          | 254 us: 1.21x slower                                                            |
| pickle                     | 7.79 us                                                         | 9.50 us: 1.22x slower                                                           |
| bench_thread_pool          | 1.10 ms                                                         | 1.35 ms: 1.22x slower                                                           |
| pickle_pure_python         | 286 us                                                          | 350 us: 1.22x slower                                                            |
| bench_mp_pool              | 75.4 ms                                                         | 96.2 ms: 1.28x slower                                                           |
| crypto_pyaes               | 69.2 ms                                                         | 88.6 ms: 1.28x slower                                                           |
| python_startup             | 22.4 ms                                                         | 28.7 ms: 1.28x slower                                                           |
| gc_traversal               | 1.44 ms                                                         | 1.85 ms: 1.29x slower                                                           |
| telco                      | 5.51 ms                                                         | 7.56 ms: 1.37x slower                                                           |
| typing_runtime_protocols   | 126 us                                                          | 186 us: 1.47x slower                                                            |
| create_gc_cycles           | 652 us                                                          | 1.06 ms: 1.63x slower                                                           |
| Geometric mean             | (ref)                                                           | 1.03x faster                                                                    |

Benchmark hidden because not significant (2): regex_v8, sympy_str
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (17) of results/bm-20250322-3.14.0a6+-bc26f95-JIT/bm-20250322-pythonperf1_win32-x86-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.042x faster

# HPT report

- Reliability score: 96.37% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown