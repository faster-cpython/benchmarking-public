# Results vs. 3.12.0

- fork: python
- ref: 5ec4bf86b7f4455432ae
- machine: windows-x86
- commit hash: 5ec4bf8
- commit date: 2025-02-22
- overall geometric mean: 1.292x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.25x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250222-pythonperf1_win32-x86-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 235 ms: 1.19x faster                                                            |
| docutils       | 1.98 sec                                                        | 1.72 sec: 1.15x faster                                                          |
| Geometric mean | (ref)                                                           | 1.17x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250222-pythonperf1_win32-x86-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_io_tg           | 677 ms                                                          | 366 ms: 1.85x faster                                                            |
| async_tree_io              | 693 ms                                                          | 376 ms: 1.84x faster                                                            |
| async_tree_none_tg         | 278 ms                                                          | 159 ms: 1.74x faster                                                            |
| async_tree_none            | 298 ms                                                          | 174 ms: 1.71x faster                                                            |
| async_tree_memoization     | 364 ms                                                          | 213 ms: 1.71x faster                                                            |
| async_tree_memoization_tg  | 350 ms                                                          | 210 ms: 1.67x faster                                                            |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 441 ms: 1.28x faster                                                            |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 429 ms: 1.27x faster                                                            |
| Geometric mean             | (ref)                                                           | 1.62x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250222-pythonperf1_win32-x86-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 69.2 ms: 1.83x faster                                                           |
| float          | 76.7 ms                                                         | 46.3 ms: 1.65x faster                                                           |
| pidigits       | 199 ms                                                          | 217 ms: 1.09x slower                                                            |
| Geometric mean | (ref)                                                           | 1.41x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250222-pythonperf1_win32-x86-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 88.8 ms: 1.45x faster                                                           |
| regex_effbot   | 2.04 ms                                                         | 1.93 ms: 1.06x faster                                                           |
| regex_dna      | 127 ms                                                          | 132 ms: 1.04x slower                                                            |
| regex_v8       | 15.0 ms                                                         | 17.4 ms: 1.16x slower                                                           |
| Geometric mean | (ref)                                                           | 1.06x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250222-pythonperf1_win32-x86-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 2.20 sec                                                        | 1.39 sec: 1.58x faster                                                          |
| unpickle_pure_python | 210 us                                                          | 154 us: 1.36x faster                                                            |
| pickle_pure_python   | 286 us                                                          | 224 us: 1.27x faster                                                            |
| pickle_list          | 3.37 us                                                         | 2.70 us: 1.25x faster                                                           |
| pickle_dict          | 19.9 us                                                         | 17.0 us: 1.17x faster                                                           |
| unpickle_list        | 2.95 us                                                         | 2.57 us: 1.15x faster                                                           |
| xml_etree_process    | 53.2 ms                                                         | 46.8 ms: 1.14x faster                                                           |
| xml_etree_generate   | 72.1 ms                                                         | 67.3 ms: 1.07x faster                                                           |
| xml_etree_iterparse  | 77.6 ms                                                         | 72.6 ms: 1.07x faster                                                           |
| json_dumps           | 7.40 ms                                                         | 7.49 ms: 1.01x slower                                                           |
| json_loads           | 20.4 us                                                         | 21.4 us: 1.05x slower                                                           |
| pickle               | 7.79 us                                                         | 8.31 us: 1.07x slower                                                           |
| unpickle             | 9.71 us                                                         | 10.4 us: 1.07x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.12x faster                                                                    |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250222-pythonperf1_win32-x86-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 22.1 ms: 1.16x slower                                                           |
| python_startup         | 22.4 ms                                                         | 28.7 ms: 1.28x slower                                                           |
| Geometric mean         | (ref)                                                           | 1.22x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250222-pythonperf1_win32-x86-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| django_template | 36.9 ms                                                         | 27.0 ms: 1.36x faster                                                           |
| mako            | 9.96 ms                                                         | 7.79 ms: 1.28x faster                                                           |
| Geometric mean  | (ref)                                                           | 1.32x faster                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250222-pythonperf1_win32-x86-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pathlib                    | 91.4 ms                                                         | 32.7 ms: 2.80x faster                                                           |
| generators                 | 38.5 ms                                                         | 17.0 ms: 2.26x faster                                                           |
| unpack_sequence            | 62.5 ns                                                         | 27.7 ns: 2.25x faster                                                           |
| deepcopy_memo              | 38.4 us                                                         | 18.2 us: 2.11x faster                                                           |
| deepcopy                   | 360 us                                                          | 187 us: 1.92x faster                                                            |
| async_tree_io_tg           | 677 ms                                                          | 366 ms: 1.85x faster                                                            |
| async_tree_io              | 693 ms                                                          | 376 ms: 1.84x faster                                                            |
| nbody                      | 127 ms                                                          | 69.2 ms: 1.83x faster                                                           |
| deltablue                  | 3.58 ms                                                         | 2.01 ms: 1.79x faster                                                           |
| async_tree_none_tg         | 278 ms                                                          | 159 ms: 1.74x faster                                                            |
| go                         | 137 ms                                                          | 79.1 ms: 1.74x faster                                                           |
| scimark_sor                | 130 ms                                                          | 75.5 ms: 1.72x faster                                                           |
| async_tree_none            | 298 ms                                                          | 174 ms: 1.71x faster                                                            |
| spectral_norm              | 104 ms                                                          | 60.6 ms: 1.71x faster                                                           |
| async_tree_memoization     | 364 ms                                                          | 213 ms: 1.71x faster                                                            |
| async_tree_memoization_tg  | 350 ms                                                          | 210 ms: 1.67x faster                                                            |
| deepcopy_reduce            | 3.23 us                                                         | 1.94 us: 1.66x faster                                                           |
| float                      | 76.7 ms                                                         | 46.3 ms: 1.65x faster                                                           |
| raytrace                   | 308 ms                                                          | 192 ms: 1.60x faster                                                            |
| logging_silent             | 101 ns                                                          | 63.4 ns: 1.59x faster                                                           |
| tomli_loads                | 2.20 sec                                                        | 1.39 sec: 1.58x faster                                                          |
| comprehensions             | 19.2 us                                                         | 12.3 us: 1.56x faster                                                           |
| hexiom                     | 6.82 ms                                                         | 4.38 ms: 1.56x faster                                                           |
| coroutines                 | 20.9 ms                                                         | 13.5 ms: 1.55x faster                                                           |
| chaos                      | 69.4 ms                                                         | 44.9 ms: 1.55x faster                                                           |
| scimark_monte_carlo        | 66.4 ms                                                         | 43.8 ms: 1.52x faster                                                           |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 2.57 ms: 1.50x faster                                                           |
| regex_compile              | 129 ms                                                          | 88.8 ms: 1.45x faster                                                           |
| sqlglot_parse              | 1.25 ms                                                         | 873 us: 1.43x faster                                                            |
| pyflate                    | 424 ms                                                          | 300 ms: 1.41x faster                                                            |
| sqlglot_transpile          | 1.53 ms                                                         | 1.10 ms: 1.39x faster                                                           |
| pprint_pformat             | 1.50 sec                                                        | 1.08 sec: 1.39x faster                                                          |
| scimark_fft                | 271 ms                                                          | 197 ms: 1.37x faster                                                            |
| logging_simple             | 9.75 us                                                         | 7.10 us: 1.37x faster                                                           |
| django_template            | 36.9 ms                                                         | 27.0 ms: 1.36x faster                                                           |
| unpickle_pure_python       | 210 us                                                          | 154 us: 1.36x faster                                                            |
| logging_format             | 10.4 us                                                         | 7.65 us: 1.36x faster                                                           |
| pprint_safe_repr           | 721 ms                                                          | 532 ms: 1.35x faster                                                            |
| nqueens                    | 93.7 ms                                                         | 69.5 ms: 1.35x faster                                                           |
| async_generators           | 313 ms                                                          | 233 ms: 1.34x faster                                                            |
| pycparser                  | 978 ms                                                          | 757 ms: 1.29x faster                                                            |
| richards                   | 41.3 ms                                                         | 32.0 ms: 1.29x faster                                                           |
| richards_super             | 46.5 ms                                                         | 36.0 ms: 1.29x faster                                                           |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 441 ms: 1.28x faster                                                            |
| mako                       | 9.96 ms                                                         | 7.79 ms: 1.28x faster                                                           |
| dulwich_log                | 58.5 ms                                                         | 45.8 ms: 1.28x faster                                                           |
| pickle_pure_python         | 286 us                                                          | 224 us: 1.27x faster                                                            |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 429 ms: 1.27x faster                                                            |
| fannkuch                   | 354 ms                                                          | 280 ms: 1.26x faster                                                            |
| sqlglot_optimize           | 48.5 ms                                                         | 38.4 ms: 1.26x faster                                                           |
| scimark_lu                 | 93.2 ms                                                         | 74.1 ms: 1.26x faster                                                           |
| sympy_str                  | 240 ms                                                          | 190 ms: 1.26x faster                                                            |
| sympy_sum                  | 123 ms                                                          | 98.1 ms: 1.25x faster                                                           |
| pickle_list                | 3.37 us                                                         | 2.70 us: 1.25x faster                                                           |
| sympy_integrate            | 17.5 ms                                                         | 14.2 ms: 1.24x faster                                                           |
| sympy_expand               | 398 ms                                                          | 328 ms: 1.21x faster                                                            |
| asyncio_tcp                | 662 ms                                                          | 551 ms: 1.20x faster                                                            |
| 2to3                       | 280 ms                                                          | 235 ms: 1.19x faster                                                            |
| crypto_pyaes               | 69.2 ms                                                         | 58.4 ms: 1.19x faster                                                           |
| pickle_dict                | 19.9 us                                                         | 17.0 us: 1.17x faster                                                           |
| docutils                   | 1.98 sec                                                        | 1.72 sec: 1.15x faster                                                          |
| unpickle_list              | 2.95 us                                                         | 2.57 us: 1.15x faster                                                           |
| xml_etree_process          | 53.2 ms                                                         | 46.8 ms: 1.14x faster                                                           |
| meteor_contest             | 86.9 ms                                                         | 76.8 ms: 1.13x faster                                                           |
| sqlite_synth               | 2.07 us                                                         | 1.85 us: 1.12x faster                                                           |
| xml_etree_generate         | 72.1 ms                                                         | 67.3 ms: 1.07x faster                                                           |
| mdp                        | 1.91 sec                                                        | 1.79 sec: 1.07x faster                                                          |
| xml_etree_iterparse        | 77.6 ms                                                         | 72.6 ms: 1.07x faster                                                           |
| regex_effbot               | 2.04 ms                                                         | 1.93 ms: 1.06x faster                                                           |
| asyncio_tcp_ssl            | 17.7 sec                                                        | 17.1 sec: 1.03x faster                                                          |
| typing_runtime_protocols   | 126 us                                                          | 124 us: 1.02x faster                                                            |
| json_dumps                 | 7.40 ms                                                         | 7.49 ms: 1.01x slower                                                           |
| json                       | 4.15 ms                                                         | 4.26 ms: 1.02x slower                                                           |
| regex_dna                  | 127 ms                                                          | 132 ms: 1.04x slower                                                            |
| json_loads                 | 20.4 us                                                         | 21.4 us: 1.05x slower                                                           |
| pickle                     | 7.79 us                                                         | 8.31 us: 1.07x slower                                                           |
| unpickle                   | 9.71 us                                                         | 10.4 us: 1.07x slower                                                           |
| telco                      | 5.51 ms                                                         | 5.98 ms: 1.08x slower                                                           |
| pidigits                   | 199 ms                                                          | 217 ms: 1.09x slower                                                            |
| coverage                   | 48.4 ms                                                         | 55.0 ms: 1.14x slower                                                           |
| regex_v8                   | 15.0 ms                                                         | 17.4 ms: 1.16x slower                                                           |
| python_startup_no_site     | 19.1 ms                                                         | 22.1 ms: 1.16x slower                                                           |
| bench_thread_pool          | 1.10 ms                                                         | 1.32 ms: 1.20x slower                                                           |
| bench_mp_pool              | 75.4 ms                                                         | 92.4 ms: 1.23x slower                                                           |
| python_startup             | 22.4 ms                                                         | 28.7 ms: 1.28x slower                                                           |
| gc_traversal               | 1.44 ms                                                         | 2.45 ms: 1.70x slower                                                           |
| create_gc_cycles           | 652 us                                                          | 1.17 ms: 1.79x slower                                                           |
| sqlglot_normalize          | 100 ms                                                          | 195 ms: 1.95x slower                                                            |
| Geometric mean             | (ref)                                                           | 1.27x faster                                                                    |

Benchmark hidden because not significant (1): xml_etree_parse
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (13) of results/bm-20250222-3.14.0a5+-5ec4bf8-CLANG/bm-20250222-pythonperf1_win32-x86-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.292x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.27x
- 95% likely to have a speedup of 1.26x
- 99% likely to have a speedup of 1.25x

# Memory
- memory change: unknown