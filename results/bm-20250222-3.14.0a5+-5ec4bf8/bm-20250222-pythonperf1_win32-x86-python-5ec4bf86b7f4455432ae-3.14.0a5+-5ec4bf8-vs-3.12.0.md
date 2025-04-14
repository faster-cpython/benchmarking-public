# Results vs. 3.12.0

- fork: python
- ref: 5ec4bf86b7f4455432ae
- machine: windows-x86
- commit hash: 5ec4bf8
- commit date: 2025-02-22
- overall geometric mean: 1.144x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.09x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250222-pythonperf1_win32-x86-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 253 ms: 1.11x faster                                                            |
| docutils       | 1.98 sec                                                        | 1.85 sec: 1.07x faster                                                          |
| Geometric mean | (ref)                                                           | 1.09x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250222-pythonperf1_win32-x86-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_io              | 693 ms                                                          | 463 ms: 1.50x faster                                                            |
| async_tree_io_tg           | 677 ms                                                          | 453 ms: 1.49x faster                                                            |
| async_tree_memoization_tg  | 350 ms                                                          | 245 ms: 1.43x faster                                                            |
| async_tree_none_tg         | 278 ms                                                          | 197 ms: 1.41x faster                                                            |
| async_tree_memoization     | 364 ms                                                          | 259 ms: 1.41x faster                                                            |
| async_tree_none            | 298 ms                                                          | 216 ms: 1.38x faster                                                            |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 468 ms: 1.20x faster                                                            |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 454 ms: 1.20x faster                                                            |
| Geometric mean             | (ref)                                                           | 1.37x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250222-pythonperf1_win32-x86-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 89.3 ms: 1.42x faster                                                           |
| float          | 76.7 ms                                                         | 57.5 ms: 1.33x faster                                                           |
| Geometric mean | (ref)                                                           | 1.24x faster                                                                    |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250222-pythonperf1_win32-x86-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_effbot   | 2.04 ms                                                         | 1.54 ms: 1.32x faster                                                           |
| regex_compile  | 129 ms                                                          | 108 ms: 1.19x faster                                                            |
| regex_dna      | 127 ms                                                          | 112 ms: 1.14x faster                                                            |
| regex_v8       | 15.0 ms                                                         | 15.2 ms: 1.01x slower                                                           |
| Geometric mean | (ref)                                                           | 1.15x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250222-pythonperf1_win32-x86-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 2.20 sec                                                        | 1.73 sec: 1.27x faster                                                          |
| xml_etree_iterparse  | 77.6 ms                                                         | 65.6 ms: 1.18x faster                                                           |
| unpickle_pure_python | 210 us                                                          | 187 us: 1.12x faster                                                            |
| xml_etree_process    | 53.2 ms                                                         | 48.7 ms: 1.09x faster                                                           |
| xml_etree_generate   | 72.1 ms                                                         | 67.0 ms: 1.08x faster                                                           |
| xml_etree_parse      | 113 ms                                                          | 109 ms: 1.04x faster                                                            |
| pickle_pure_python   | 286 us                                                          | 277 us: 1.03x faster                                                            |
| unpickle_list        | 2.95 us                                                         | 3.07 us: 1.04x slower                                                           |
| pickle_dict          | 19.9 us                                                         | 20.9 us: 1.05x slower                                                           |
| json_loads           | 20.4 us                                                         | 21.5 us: 1.06x slower                                                           |
| json_dumps           | 7.40 ms                                                         | 8.19 ms: 1.11x slower                                                           |
| pickle_list          | 3.37 us                                                         | 3.79 us: 1.13x slower                                                           |
| unpickle             | 9.71 us                                                         | 11.4 us: 1.17x slower                                                           |
| pickle               | 7.79 us                                                         | 9.18 us: 1.18x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.01x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250222-pythonperf1_win32-x86-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 21.7 ms: 1.14x slower                                                           |
| python_startup         | 22.4 ms                                                         | 28.1 ms: 1.26x slower                                                           |
| Geometric mean         | (ref)                                                           | 1.20x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250222-pythonperf1_win32-x86-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 7.73 ms: 1.29x faster                                                           |
| django_template | 36.9 ms                                                         | 35.4 ms: 1.04x faster                                                           |
| Geometric mean  | (ref)                                                           | 1.16x faster                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250222-pythonperf1_win32-x86-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pathlib                    | 91.4 ms                                                         | 34.3 ms: 2.66x faster                                                           |
| deepcopy_memo              | 38.4 us                                                         | 21.6 us: 1.78x faster                                                           |
| async_tree_io              | 693 ms                                                          | 463 ms: 1.50x faster                                                            |
| async_tree_io_tg           | 677 ms                                                          | 453 ms: 1.49x faster                                                            |
| deepcopy                   | 360 us                                                          | 241 us: 1.49x faster                                                            |
| unpack_sequence            | 62.5 ns                                                         | 43.5 ns: 1.44x faster                                                           |
| generators                 | 38.5 ms                                                         | 26.8 ms: 1.44x faster                                                           |
| async_tree_memoization_tg  | 350 ms                                                          | 245 ms: 1.43x faster                                                            |
| nbody                      | 127 ms                                                          | 89.3 ms: 1.42x faster                                                           |
| spectral_norm              | 104 ms                                                          | 73.2 ms: 1.42x faster                                                           |
| comprehensions             | 19.2 us                                                         | 13.6 us: 1.41x faster                                                           |
| async_tree_none_tg         | 278 ms                                                          | 197 ms: 1.41x faster                                                            |
| async_tree_memoization     | 364 ms                                                          | 259 ms: 1.41x faster                                                            |
| logging_silent             | 101 ns                                                          | 72.4 ns: 1.40x faster                                                           |
| async_tree_none            | 298 ms                                                          | 216 ms: 1.38x faster                                                            |
| scimark_lu                 | 93.2 ms                                                         | 69.5 ms: 1.34x faster                                                           |
| float                      | 76.7 ms                                                         | 57.5 ms: 1.33x faster                                                           |
| regex_effbot               | 2.04 ms                                                         | 1.54 ms: 1.32x faster                                                           |
| hexiom                     | 6.82 ms                                                         | 5.15 ms: 1.32x faster                                                           |
| scimark_sor                | 130 ms                                                          | 99.7 ms: 1.30x faster                                                           |
| deepcopy_reduce            | 3.23 us                                                         | 2.49 us: 1.30x faster                                                           |
| mako                       | 9.96 ms                                                         | 7.73 ms: 1.29x faster                                                           |
| tomli_loads                | 2.20 sec                                                        | 1.73 sec: 1.27x faster                                                          |
| coroutines                 | 20.9 ms                                                         | 16.5 ms: 1.27x faster                                                           |
| deltablue                  | 3.58 ms                                                         | 2.83 ms: 1.27x faster                                                           |
| go                         | 137 ms                                                          | 109 ms: 1.26x faster                                                            |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 3.07 ms: 1.26x faster                                                           |
| chaos                      | 69.4 ms                                                         | 56.5 ms: 1.23x faster                                                           |
| scimark_monte_carlo        | 66.4 ms                                                         | 54.5 ms: 1.22x faster                                                           |
| nqueens                    | 93.7 ms                                                         | 77.6 ms: 1.21x faster                                                           |
| pyflate                    | 424 ms                                                          | 352 ms: 1.20x faster                                                            |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 468 ms: 1.20x faster                                                            |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 454 ms: 1.20x faster                                                            |
| raytrace                   | 308 ms                                                          | 257 ms: 1.20x faster                                                            |
| scimark_fft                | 271 ms                                                          | 226 ms: 1.20x faster                                                            |
| regex_compile              | 129 ms                                                          | 108 ms: 1.19x faster                                                            |
| xml_etree_iterparse        | 77.6 ms                                                         | 65.6 ms: 1.18x faster                                                           |
| logging_simple             | 9.75 us                                                         | 8.36 us: 1.17x faster                                                           |
| sympy_sum                  | 123 ms                                                          | 107 ms: 1.15x faster                                                            |
| fannkuch                   | 354 ms                                                          | 310 ms: 1.14x faster                                                            |
| regex_dna                  | 127 ms                                                          | 112 ms: 1.14x faster                                                            |
| logging_format             | 10.4 us                                                         | 9.16 us: 1.14x faster                                                           |
| dulwich_log                | 58.5 ms                                                         | 51.8 ms: 1.13x faster                                                           |
| sqlite_synth               | 2.07 us                                                         | 1.84 us: 1.13x faster                                                           |
| unpickle_pure_python       | 210 us                                                          | 187 us: 1.12x faster                                                            |
| sympy_integrate            | 17.5 ms                                                         | 15.6 ms: 1.12x faster                                                           |
| sqlglot_optimize           | 48.5 ms                                                         | 43.3 ms: 1.12x faster                                                           |
| 2to3                       | 280 ms                                                          | 253 ms: 1.11x faster                                                            |
| sympy_str                  | 240 ms                                                          | 217 ms: 1.10x faster                                                            |
| asyncio_tcp                | 662 ms                                                          | 601 ms: 1.10x faster                                                            |
| pprint_pformat             | 1.50 sec                                                        | 1.36 sec: 1.10x faster                                                          |
| richards                   | 41.3 ms                                                         | 37.7 ms: 1.10x faster                                                           |
| xml_etree_process          | 53.2 ms                                                         | 48.7 ms: 1.09x faster                                                           |
| pycparser                  | 978 ms                                                          | 897 ms: 1.09x faster                                                            |
| crypto_pyaes               | 69.2 ms                                                         | 63.9 ms: 1.08x faster                                                           |
| pprint_safe_repr           | 721 ms                                                          | 667 ms: 1.08x faster                                                            |
| xml_etree_generate         | 72.1 ms                                                         | 67.0 ms: 1.08x faster                                                           |
| sqlglot_parse              | 1.25 ms                                                         | 1.16 ms: 1.08x faster                                                           |
| docutils                   | 1.98 sec                                                        | 1.85 sec: 1.07x faster                                                          |
| sqlglot_transpile          | 1.53 ms                                                         | 1.43 ms: 1.07x faster                                                           |
| richards_super             | 46.5 ms                                                         | 43.4 ms: 1.07x faster                                                           |
| mdp                        | 1.91 sec                                                        | 1.80 sec: 1.06x faster                                                          |
| meteor_contest             | 86.9 ms                                                         | 82.1 ms: 1.06x faster                                                           |
| sympy_expand               | 398 ms                                                          | 379 ms: 1.05x faster                                                            |
| django_template            | 36.9 ms                                                         | 35.4 ms: 1.04x faster                                                           |
| xml_etree_parse            | 113 ms                                                          | 109 ms: 1.04x faster                                                            |
| pickle_pure_python         | 286 us                                                          | 277 us: 1.03x faster                                                            |
| asyncio_tcp_ssl            | 17.7 sec                                                        | 17.2 sec: 1.03x faster                                                          |
| async_generators           | 313 ms                                                          | 306 ms: 1.02x faster                                                            |
| regex_v8                   | 15.0 ms                                                         | 15.2 ms: 1.01x slower                                                           |
| unpickle_list              | 2.95 us                                                         | 3.07 us: 1.04x slower                                                           |
| pickle_dict                | 19.9 us                                                         | 20.9 us: 1.05x slower                                                           |
| json_loads                 | 20.4 us                                                         | 21.5 us: 1.06x slower                                                           |
| json                       | 4.15 ms                                                         | 4.43 ms: 1.07x slower                                                           |
| coverage                   | 48.4 ms                                                         | 52.1 ms: 1.08x slower                                                           |
| json_dumps                 | 7.40 ms                                                         | 8.19 ms: 1.11x slower                                                           |
| pickle_list                | 3.37 us                                                         | 3.79 us: 1.13x slower                                                           |
| python_startup_no_site     | 19.1 ms                                                         | 21.7 ms: 1.14x slower                                                           |
| unpickle                   | 9.71 us                                                         | 11.4 us: 1.17x slower                                                           |
| pickle                     | 7.79 us                                                         | 9.18 us: 1.18x slower                                                           |
| bench_thread_pool          | 1.10 ms                                                         | 1.31 ms: 1.19x slower                                                           |
| bench_mp_pool              | 75.4 ms                                                         | 90.6 ms: 1.20x slower                                                           |
| typing_runtime_protocols   | 126 us                                                          | 153 us: 1.21x slower                                                            |
| python_startup             | 22.4 ms                                                         | 28.1 ms: 1.26x slower                                                           |
| gc_traversal               | 1.44 ms                                                         | 1.81 ms: 1.26x slower                                                           |
| telco                      | 5.51 ms                                                         | 6.95 ms: 1.26x slower                                                           |
| create_gc_cycles           | 652 us                                                          | 1.03 ms: 1.58x slower                                                           |
| sqlglot_normalize          | 100 ms                                                          | 222 ms: 2.21x slower                                                            |
| Geometric mean             | (ref)                                                           | 1.13x faster                                                                    |

Benchmark hidden because not significant (1): pidigits
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (13) of results/bm-20250222-3.14.0a5+-5ec4bf8/bm-20250222-pythonperf1_win32-x86-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.144x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.12x
- 95% likely to have a speedup of 1.10x
- 99% likely to have a speedup of 1.09x

# Memory
- memory change: unknown