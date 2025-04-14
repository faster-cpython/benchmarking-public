# Results vs. 3.12.0

- fork: python
- ref: 359c7dde3bb074e02968
- machine: windows-x86
- commit hash: 359c7dd
- commit date: 2025-02-16
- overall geometric mean: 1.105x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250216-pythonperf1_win32-x86-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 263 ms: 1.06x faster                                                            |
| docutils       | 1.98 sec                                                        | 1.89 sec: 1.05x faster                                                          |
| Geometric mean | (ref)                                                           | 1.06x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250216-pythonperf1_win32-x86-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_io              | 693 ms                                                          | 502 ms: 1.38x faster                                                            |
| async_tree_io_tg           | 677 ms                                                          | 500 ms: 1.35x faster                                                            |
| async_tree_memoization_tg  | 350 ms                                                          | 269 ms: 1.31x faster                                                            |
| async_tree_none_tg         | 278 ms                                                          | 214 ms: 1.30x faster                                                            |
| async_tree_memoization     | 364 ms                                                          | 284 ms: 1.28x faster                                                            |
| async_tree_none            | 298 ms                                                          | 235 ms: 1.27x faster                                                            |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 484 ms: 1.13x faster                                                            |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 503 ms: 1.12x faster                                                            |
| Geometric mean             | (ref)                                                           | 1.26x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250216-pythonperf1_win32-x86-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 88.2 ms: 1.44x faster                                                           |
| float          | 76.7 ms                                                         | 58.2 ms: 1.32x faster                                                           |
| pidigits       | 199 ms                                                          | 200 ms: 1.00x slower                                                            |
| Geometric mean | (ref)                                                           | 1.24x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250216-pythonperf1_win32-x86-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_effbot   | 2.04 ms                                                         | 1.60 ms: 1.27x faster                                                           |
| regex_compile  | 129 ms                                                          | 113 ms: 1.14x faster                                                            |
| regex_dna      | 127 ms                                                          | 119 ms: 1.06x faster                                                            |
| regex_v8       | 15.0 ms                                                         | 15.8 ms: 1.05x slower                                                           |
| Geometric mean | (ref)                                                           | 1.10x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250216-pythonperf1_win32-x86-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 2.20 sec                                                        | 1.77 sec: 1.24x faster                                                          |
| xml_etree_iterparse  | 77.6 ms                                                         | 67.1 ms: 1.16x faster                                                           |
| unpickle_pure_python | 210 us                                                          | 193 us: 1.09x faster                                                            |
| xml_etree_parse      | 113 ms                                                          | 107 ms: 1.06x faster                                                            |
| xml_etree_generate   | 72.1 ms                                                         | 69.3 ms: 1.04x faster                                                           |
| xml_etree_process    | 53.2 ms                                                         | 51.9 ms: 1.03x faster                                                           |
| unpickle_list        | 2.95 us                                                         | 3.01 us: 1.02x slower                                                           |
| pickle_dict          | 19.9 us                                                         | 20.9 us: 1.05x slower                                                           |
| pickle_pure_python   | 286 us                                                          | 305 us: 1.07x slower                                                            |
| pickle_list          | 3.37 us                                                         | 3.71 us: 1.10x slower                                                           |
| json_loads           | 20.4 us                                                         | 22.8 us: 1.12x slower                                                           |
| unpickle             | 9.71 us                                                         | 11.2 us: 1.15x slower                                                           |
| pickle               | 7.79 us                                                         | 9.27 us: 1.19x slower                                                           |
| json_dumps           | 7.40 ms                                                         | 9.33 ms: 1.26x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.02x slower                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250216-pythonperf1_win32-x86-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 21.4 ms: 1.12x slower                                                           |
| python_startup         | 22.4 ms                                                         | 27.7 ms: 1.24x slower                                                           |
| Geometric mean         | (ref)                                                           | 1.18x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250216-pythonperf1_win32-x86-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 8.48 ms: 1.17x faster                                                           |
| django_template | 36.9 ms                                                         | 37.1 ms: 1.01x slower                                                           |
| Geometric mean  | (ref)                                                           | 1.08x faster                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250216-pythonperf1_win32-x86-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pathlib                    | 91.4 ms                                                         | 34.6 ms: 2.64x faster                                                           |
| deepcopy_memo              | 38.4 us                                                         | 22.8 us: 1.68x faster                                                           |
| unpack_sequence            | 62.5 ns                                                         | 42.4 ns: 1.47x faster                                                           |
| nbody                      | 127 ms                                                          | 88.2 ms: 1.44x faster                                                           |
| async_tree_io              | 693 ms                                                          | 502 ms: 1.38x faster                                                            |
| deepcopy                   | 360 us                                                          | 262 us: 1.37x faster                                                            |
| generators                 | 38.5 ms                                                         | 28.4 ms: 1.36x faster                                                           |
| async_tree_io_tg           | 677 ms                                                          | 500 ms: 1.35x faster                                                            |
| comprehensions             | 19.2 us                                                         | 14.3 us: 1.34x faster                                                           |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 2.92 ms: 1.32x faster                                                           |
| spectral_norm              | 104 ms                                                          | 78.6 ms: 1.32x faster                                                           |
| float                      | 76.7 ms                                                         | 58.2 ms: 1.32x faster                                                           |
| async_tree_memoization_tg  | 350 ms                                                          | 269 ms: 1.31x faster                                                            |
| async_tree_none_tg         | 278 ms                                                          | 214 ms: 1.30x faster                                                            |
| scimark_lu                 | 93.2 ms                                                         | 72.5 ms: 1.29x faster                                                           |
| async_tree_memoization     | 364 ms                                                          | 284 ms: 1.28x faster                                                            |
| regex_effbot               | 2.04 ms                                                         | 1.60 ms: 1.27x faster                                                           |
| async_tree_none            | 298 ms                                                          | 235 ms: 1.27x faster                                                            |
| logging_silent             | 101 ns                                                          | 80.3 ns: 1.26x faster                                                           |
| scimark_sor                | 130 ms                                                          | 104 ms: 1.25x faster                                                            |
| tomli_loads                | 2.20 sec                                                        | 1.77 sec: 1.24x faster                                                          |
| go                         | 137 ms                                                          | 112 ms: 1.23x faster                                                            |
| hexiom                     | 6.82 ms                                                         | 5.58 ms: 1.22x faster                                                           |
| coroutines                 | 20.9 ms                                                         | 17.1 ms: 1.22x faster                                                           |
| scimark_monte_carlo        | 66.4 ms                                                         | 55.4 ms: 1.20x faster                                                           |
| scimark_fft                | 271 ms                                                          | 230 ms: 1.18x faster                                                            |
| deltablue                  | 3.58 ms                                                         | 3.05 ms: 1.18x faster                                                           |
| deepcopy_reduce            | 3.23 us                                                         | 2.74 us: 1.18x faster                                                           |
| mako                       | 9.96 ms                                                         | 8.48 ms: 1.17x faster                                                           |
| pyflate                    | 424 ms                                                          | 366 ms: 1.16x faster                                                            |
| xml_etree_iterparse        | 77.6 ms                                                         | 67.1 ms: 1.16x faster                                                           |
| fannkuch                   | 354 ms                                                          | 308 ms: 1.15x faster                                                            |
| chaos                      | 69.4 ms                                                         | 60.4 ms: 1.15x faster                                                           |
| nqueens                    | 93.7 ms                                                         | 81.9 ms: 1.14x faster                                                           |
| regex_compile              | 129 ms                                                          | 113 ms: 1.14x faster                                                            |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 484 ms: 1.13x faster                                                            |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 503 ms: 1.12x faster                                                            |
| crypto_pyaes               | 69.2 ms                                                         | 61.7 ms: 1.12x faster                                                           |
| mdp                        | 1.91 sec                                                        | 1.74 sec: 1.10x faster                                                          |
| logging_simple             | 9.75 us                                                         | 8.98 us: 1.09x faster                                                           |
| sqlite_synth               | 2.07 us                                                         | 1.91 us: 1.09x faster                                                           |
| unpickle_pure_python       | 210 us                                                          | 193 us: 1.09x faster                                                            |
| dulwich_log                | 58.5 ms                                                         | 54.1 ms: 1.08x faster                                                           |
| sympy_sum                  | 123 ms                                                          | 114 ms: 1.08x faster                                                            |
| meteor_contest             | 86.9 ms                                                         | 80.5 ms: 1.08x faster                                                           |
| logging_format             | 10.4 us                                                         | 9.73 us: 1.07x faster                                                           |
| sqlglot_transpile          | 1.53 ms                                                         | 1.43 ms: 1.07x faster                                                           |
| asyncio_tcp                | 662 ms                                                          | 620 ms: 1.07x faster                                                            |
| raytrace                   | 308 ms                                                          | 288 ms: 1.07x faster                                                            |
| sympy_integrate            | 17.5 ms                                                         | 16.4 ms: 1.07x faster                                                           |
| regex_dna                  | 127 ms                                                          | 119 ms: 1.06x faster                                                            |
| 2to3                       | 280 ms                                                          | 263 ms: 1.06x faster                                                            |
| xml_etree_parse            | 113 ms                                                          | 107 ms: 1.06x faster                                                            |
| sqlglot_parse              | 1.25 ms                                                         | 1.19 ms: 1.05x faster                                                           |
| bench_thread_pool          | 1.10 ms                                                         | 1.05 ms: 1.05x faster                                                           |
| docutils                   | 1.98 sec                                                        | 1.89 sec: 1.05x faster                                                          |
| xml_etree_generate         | 72.1 ms                                                         | 69.3 ms: 1.04x faster                                                           |
| pycparser                  | 978 ms                                                          | 940 ms: 1.04x faster                                                            |
| asyncio_tcp_ssl            | 17.7 sec                                                        | 17.1 sec: 1.03x faster                                                          |
| sympy_str                  | 240 ms                                                          | 232 ms: 1.03x faster                                                            |
| sqlglot_optimize           | 48.5 ms                                                         | 47.1 ms: 1.03x faster                                                           |
| xml_etree_process          | 53.2 ms                                                         | 51.9 ms: 1.03x faster                                                           |
| pidigits                   | 199 ms                                                          | 200 ms: 1.00x slower                                                            |
| pprint_pformat             | 1.50 sec                                                        | 1.51 sec: 1.00x slower                                                          |
| django_template            | 36.9 ms                                                         | 37.1 ms: 1.01x slower                                                           |
| richards                   | 41.3 ms                                                         | 42.1 ms: 1.02x slower                                                           |
| unpickle_list              | 2.95 us                                                         | 3.01 us: 1.02x slower                                                           |
| sqlglot_normalize          | 100 ms                                                          | 103 ms: 1.03x slower                                                            |
| sympy_expand               | 398 ms                                                          | 412 ms: 1.03x slower                                                            |
| async_generators           | 313 ms                                                          | 325 ms: 1.04x slower                                                            |
| pickle_dict                | 19.9 us                                                         | 20.9 us: 1.05x slower                                                           |
| regex_v8                   | 15.0 ms                                                         | 15.8 ms: 1.05x slower                                                           |
| pickle_pure_python         | 286 us                                                          | 305 us: 1.07x slower                                                            |
| pickle_list                | 3.37 us                                                         | 3.71 us: 1.10x slower                                                           |
| coverage                   | 48.4 ms                                                         | 53.6 ms: 1.11x slower                                                           |
| json                       | 4.15 ms                                                         | 4.61 ms: 1.11x slower                                                           |
| json_loads                 | 20.4 us                                                         | 22.8 us: 1.12x slower                                                           |
| python_startup_no_site     | 19.1 ms                                                         | 21.4 ms: 1.12x slower                                                           |
| unpickle                   | 9.71 us                                                         | 11.2 us: 1.15x slower                                                           |
| pickle                     | 7.79 us                                                         | 9.27 us: 1.19x slower                                                           |
| bench_mp_pool              | 75.4 ms                                                         | 89.7 ms: 1.19x slower                                                           |
| python_startup             | 22.4 ms                                                         | 27.7 ms: 1.24x slower                                                           |
| telco                      | 5.51 ms                                                         | 6.90 ms: 1.25x slower                                                           |
| gc_traversal               | 1.44 ms                                                         | 1.80 ms: 1.25x slower                                                           |
| json_dumps                 | 7.40 ms                                                         | 9.33 ms: 1.26x slower                                                           |
| typing_runtime_protocols   | 126 us                                                          | 160 us: 1.27x slower                                                            |
| create_gc_cycles           | 652 us                                                          | 1.06 ms: 1.63x slower                                                           |
| Geometric mean             | (ref)                                                           | 1.09x faster                                                                    |

Benchmark hidden because not significant (2): richards_super, pprint_safe_repr
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (13) of results/bm-20250216-3.14.0a5+-359c7dd/bm-20250216-pythonperf1_win32-x86-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.105x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.08x
- 95% likely to have a speedup of 1.07x
- 99% likely to have a speedup of 1.06x

# Memory
- memory change: unknown