# Results vs. 3.12.0

- fork: python
- ref: bc26f95e8ff60ccca981
- machine: windows-x86
- commit hash: bc26f95
- commit date: 2025-03-22
- overall geometric mean: 1.136x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250322-pythonperf1_win32-x86-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 268 ms: 1.04x faster                                                            |
| docutils       | 1.98 sec                                                        | 1.91 sec: 1.04x faster                                                          |
| Geometric mean | (ref)                                                           | 1.04x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250322-pythonperf1_win32-x86-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_io_tg           | 677 ms                                                          | 447 ms: 1.51x faster                                                            |
| async_tree_io              | 693 ms                                                          | 464 ms: 1.49x faster                                                            |
| async_tree_memoization_tg  | 350 ms                                                          | 238 ms: 1.47x faster                                                            |
| async_tree_memoization     | 364 ms                                                          | 255 ms: 1.43x faster                                                            |
| async_tree_none_tg         | 278 ms                                                          | 195 ms: 1.43x faster                                                            |
| async_tree_none            | 298 ms                                                          | 219 ms: 1.36x faster                                                            |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 466 ms: 1.17x faster                                                            |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 486 ms: 1.16x faster                                                            |
| Geometric mean             | (ref)                                                           | 1.37x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250322-pythonperf1_win32-x86-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 86.0 ms: 1.48x faster                                                           |
| float          | 76.7 ms                                                         | 54.1 ms: 1.42x faster                                                           |
| pidigits       | 199 ms                                                          | 201 ms: 1.01x slower                                                            |
| Geometric mean | (ref)                                                           | 1.28x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250322-pythonperf1_win32-x86-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_effbot   | 2.04 ms                                                         | 1.57 ms: 1.29x faster                                                           |
| regex_compile  | 129 ms                                                          | 108 ms: 1.20x faster                                                            |
| regex_dna      | 127 ms                                                          | 119 ms: 1.07x faster                                                            |
| Geometric mean | (ref)                                                           | 1.13x faster                                                                    |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250322-pythonperf1_win32-x86-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 2.20 sec                                                        | 1.77 sec: 1.24x faster                                                          |
| xml_etree_iterparse  | 77.6 ms                                                         | 68.0 ms: 1.14x faster                                                           |
| unpickle_pure_python | 210 us                                                          | 187 us: 1.12x faster                                                            |
| pickle_pure_python   | 286 us                                                          | 272 us: 1.05x faster                                                            |
| xml_etree_parse      | 113 ms                                                          | 110 ms: 1.03x faster                                                            |
| xml_etree_generate   | 72.1 ms                                                         | 72.6 ms: 1.01x slower                                                           |
| pickle_dict          | 19.9 us                                                         | 21.0 us: 1.06x slower                                                           |
| json_loads           | 20.4 us                                                         | 21.6 us: 1.06x slower                                                           |
| unpickle_list        | 2.95 us                                                         | 3.18 us: 1.08x slower                                                           |
| json_dumps           | 7.40 ms                                                         | 8.33 ms: 1.13x slower                                                           |
| pickle_list          | 3.37 us                                                         | 3.85 us: 1.14x slower                                                           |
| unpickle             | 9.71 us                                                         | 11.2 us: 1.15x slower                                                           |
| pickle               | 7.79 us                                                         | 9.19 us: 1.18x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.02x slower                                                                    |

Benchmark hidden because not significant (1): xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250322-pythonperf1_win32-x86-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 22.9 ms: 1.20x slower                                                           |
| python_startup         | 22.4 ms                                                         | 29.0 ms: 1.30x slower                                                           |
| Geometric mean         | (ref)                                                           | 1.25x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250322-pythonperf1_win32-x86-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 8.37 ms: 1.19x faster                                                           |
| django_template | 36.9 ms                                                         | 35.6 ms: 1.04x faster                                                           |
| Geometric mean  | (ref)                                                           | 1.11x faster                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250322-pythonperf1_win32-x86-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pathlib                    | 91.4 ms                                                         | 37.3 ms: 2.45x faster                                                           |
| deepcopy_memo              | 38.4 us                                                         | 21.6 us: 1.78x faster                                                           |
| unpack_sequence            | 62.5 ns                                                         | 39.4 ns: 1.59x faster                                                           |
| generators                 | 38.5 ms                                                         | 25.2 ms: 1.53x faster                                                           |
| async_tree_io_tg           | 677 ms                                                          | 447 ms: 1.51x faster                                                            |
| logging_silent             | 101 ns                                                          | 67.2 ns: 1.50x faster                                                           |
| async_tree_io              | 693 ms                                                          | 464 ms: 1.49x faster                                                            |
| nbody                      | 127 ms                                                          | 86.0 ms: 1.48x faster                                                           |
| async_tree_memoization_tg  | 350 ms                                                          | 238 ms: 1.47x faster                                                            |
| async_tree_memoization     | 364 ms                                                          | 255 ms: 1.43x faster                                                            |
| async_tree_none_tg         | 278 ms                                                          | 195 ms: 1.43x faster                                                            |
| float                      | 76.7 ms                                                         | 54.1 ms: 1.42x faster                                                           |
| spectral_norm              | 104 ms                                                          | 74.3 ms: 1.40x faster                                                           |
| deepcopy                   | 360 us                                                          | 259 us: 1.39x faster                                                            |
| scimark_lu                 | 93.2 ms                                                         | 67.7 ms: 1.38x faster                                                           |
| async_tree_none            | 298 ms                                                          | 219 ms: 1.36x faster                                                            |
| scimark_sor                | 130 ms                                                          | 96.7 ms: 1.34x faster                                                           |
| hexiom                     | 6.82 ms                                                         | 5.08 ms: 1.34x faster                                                           |
| comprehensions             | 19.2 us                                                         | 14.5 us: 1.33x faster                                                           |
| deltablue                  | 3.58 ms                                                         | 2.73 ms: 1.31x faster                                                           |
| regex_effbot               | 2.04 ms                                                         | 1.57 ms: 1.29x faster                                                           |
| coroutines                 | 20.9 ms                                                         | 16.5 ms: 1.26x faster                                                           |
| tomli_loads                | 2.20 sec                                                        | 1.77 sec: 1.24x faster                                                          |
| go                         | 137 ms                                                          | 111 ms: 1.24x faster                                                            |
| scimark_monte_carlo        | 66.4 ms                                                         | 54.3 ms: 1.22x faster                                                           |
| raytrace                   | 308 ms                                                          | 253 ms: 1.22x faster                                                            |
| regex_compile              | 129 ms                                                          | 108 ms: 1.20x faster                                                            |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 3.24 ms: 1.19x faster                                                           |
| mako                       | 9.96 ms                                                         | 8.37 ms: 1.19x faster                                                           |
| pyflate                    | 424 ms                                                          | 358 ms: 1.18x faster                                                            |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 466 ms: 1.17x faster                                                            |
| deepcopy_reduce            | 3.23 us                                                         | 2.75 us: 1.17x faster                                                           |
| chaos                      | 69.4 ms                                                         | 59.7 ms: 1.16x faster                                                           |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 486 ms: 1.16x faster                                                            |
| scimark_fft                | 271 ms                                                          | 235 ms: 1.15x faster                                                            |
| xml_etree_iterparse        | 77.6 ms                                                         | 68.0 ms: 1.14x faster                                                           |
| unpickle_pure_python       | 210 us                                                          | 187 us: 1.12x faster                                                            |
| dulwich_log                | 58.5 ms                                                         | 52.2 ms: 1.12x faster                                                           |
| sympy_integrate            | 17.5 ms                                                         | 15.9 ms: 1.10x faster                                                           |
| pprint_pformat             | 1.50 sec                                                        | 1.36 sec: 1.10x faster                                                          |
| logging_simple             | 9.75 us                                                         | 8.88 us: 1.10x faster                                                           |
| sympy_sum                  | 123 ms                                                          | 113 ms: 1.09x faster                                                            |
| pprint_safe_repr           | 721 ms                                                          | 670 ms: 1.08x faster                                                            |
| nqueens                    | 93.7 ms                                                         | 87.2 ms: 1.07x faster                                                           |
| richards                   | 41.3 ms                                                         | 38.5 ms: 1.07x faster                                                           |
| richards_super             | 46.5 ms                                                         | 43.3 ms: 1.07x faster                                                           |
| sqlite_synth               | 2.07 us                                                         | 1.93 us: 1.07x faster                                                           |
| regex_dna                  | 127 ms                                                          | 119 ms: 1.07x faster                                                            |
| logging_format             | 10.4 us                                                         | 9.75 us: 1.07x faster                                                           |
| sympy_str                  | 240 ms                                                          | 228 ms: 1.05x faster                                                            |
| pickle_pure_python         | 286 us                                                          | 272 us: 1.05x faster                                                            |
| 2to3                       | 280 ms                                                          | 268 ms: 1.04x faster                                                            |
| docutils                   | 1.98 sec                                                        | 1.91 sec: 1.04x faster                                                          |
| django_template            | 36.9 ms                                                         | 35.6 ms: 1.04x faster                                                           |
| pycparser                  | 978 ms                                                          | 947 ms: 1.03x faster                                                            |
| xml_etree_parse            | 113 ms                                                          | 110 ms: 1.03x faster                                                            |
| meteor_contest             | 86.9 ms                                                         | 84.9 ms: 1.02x faster                                                           |
| asyncio_tcp_ssl            | 17.7 sec                                                        | 17.3 sec: 1.02x faster                                                          |
| fannkuch                   | 354 ms                                                          | 347 ms: 1.02x faster                                                            |
| mdp                        | 1.91 sec                                                        | 1.88 sec: 1.01x faster                                                          |
| crypto_pyaes               | 69.2 ms                                                         | 68.8 ms: 1.01x faster                                                           |
| xml_etree_generate         | 72.1 ms                                                         | 72.6 ms: 1.01x slower                                                           |
| pidigits                   | 199 ms                                                          | 201 ms: 1.01x slower                                                            |
| async_generators           | 313 ms                                                          | 317 ms: 1.01x slower                                                            |
| sympy_expand               | 398 ms                                                          | 406 ms: 1.02x slower                                                            |
| pickle_dict                | 19.9 us                                                         | 21.0 us: 1.06x slower                                                           |
| json_loads                 | 20.4 us                                                         | 21.6 us: 1.06x slower                                                           |
| unpickle_list              | 2.95 us                                                         | 3.18 us: 1.08x slower                                                           |
| coverage                   | 48.4 ms                                                         | 53.2 ms: 1.10x slower                                                           |
| json                       | 4.15 ms                                                         | 4.63 ms: 1.12x slower                                                           |
| json_dumps                 | 7.40 ms                                                         | 8.33 ms: 1.13x slower                                                           |
| pickle_list                | 3.37 us                                                         | 3.85 us: 1.14x slower                                                           |
| unpickle                   | 9.71 us                                                         | 11.2 us: 1.15x slower                                                           |
| pickle                     | 7.79 us                                                         | 9.19 us: 1.18x slower                                                           |
| bench_thread_pool          | 1.10 ms                                                         | 1.30 ms: 1.18x slower                                                           |
| python_startup_no_site     | 19.1 ms                                                         | 22.9 ms: 1.20x slower                                                           |
| typing_runtime_protocols   | 126 us                                                          | 153 us: 1.21x slower                                                            |
| telco                      | 5.51 ms                                                         | 6.82 ms: 1.24x slower                                                           |
| gc_traversal               | 1.44 ms                                                         | 1.82 ms: 1.26x slower                                                           |
| bench_mp_pool              | 75.4 ms                                                         | 95.7 ms: 1.27x slower                                                           |
| python_startup             | 22.4 ms                                                         | 29.0 ms: 1.30x slower                                                           |
| create_gc_cycles           | 652 us                                                          | 1.07 ms: 1.63x slower                                                           |
| Geometric mean             | (ref)                                                           | 1.11x faster                                                                    |

Benchmark hidden because not significant (3): asyncio_tcp, xml_etree_process, regex_v8
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (17) of results/bm-20250322-3.14.0a6+-bc26f95/bm-20250322-pythonperf1_win32-x86-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.136x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.09x
- 95% likely to have a speedup of 1.07x
- 99% likely to have a speedup of 1.06x

# Memory
- memory change: unknown