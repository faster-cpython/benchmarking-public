# Results vs. 3.12.0

- fork: python
- ref: 29f8a67ae00081a36fdc
- machine: windows-x86
- commit hash: 29f8a67
- commit date: 2025-02-08
- overall geometric mean: 1.289x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.25x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250208-pythonperf1_win32-x86-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 240 ms: 1.17x faster                                                            |
| docutils       | 1.98 sec                                                        | 1.73 sec: 1.15x faster                                                          |
| Geometric mean | (ref)                                                           | 1.16x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250208-pythonperf1_win32-x86-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_io_tg           | 677 ms                                                          | 373 ms: 1.82x faster                                                            |
| async_tree_io              | 693 ms                                                          | 385 ms: 1.80x faster                                                            |
| async_tree_none_tg         | 278 ms                                                          | 162 ms: 1.71x faster                                                            |
| async_tree_memoization     | 364 ms                                                          | 215 ms: 1.69x faster                                                            |
| async_tree_none            | 298 ms                                                          | 176 ms: 1.69x faster                                                            |
| async_tree_memoization_tg  | 350 ms                                                          | 213 ms: 1.65x faster                                                            |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 438 ms: 1.29x faster                                                            |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 429 ms: 1.27x faster                                                            |
| Geometric mean             | (ref)                                                           | 1.60x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250208-pythonperf1_win32-x86-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 64.5 ms: 1.97x faster                                                           |
| float          | 76.7 ms                                                         | 44.0 ms: 1.74x faster                                                           |
| pidigits       | 199 ms                                                          | 217 ms: 1.09x slower                                                            |
| Geometric mean | (ref)                                                           | 1.47x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250208-pythonperf1_win32-x86-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 90.0 ms: 1.43x faster                                                           |
| regex_effbot   | 2.04 ms                                                         | 1.97 ms: 1.03x faster                                                           |
| regex_dna      | 127 ms                                                          | 132 ms: 1.04x slower                                                            |
| regex_v8       | 15.0 ms                                                         | 17.4 ms: 1.16x slower                                                           |
| Geometric mean | (ref)                                                           | 1.05x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250208-pythonperf1_win32-x86-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 2.20 sec                                                        | 1.39 sec: 1.58x faster                                                          |
| unpickle_pure_python | 210 us                                                          | 151 us: 1.39x faster                                                            |
| pickle_pure_python   | 286 us                                                          | 220 us: 1.30x faster                                                            |
| xml_etree_process    | 53.2 ms                                                         | 46.6 ms: 1.14x faster                                                           |
| xml_etree_generate   | 72.1 ms                                                         | 66.3 ms: 1.09x faster                                                           |
| xml_etree_iterparse  | 77.6 ms                                                         | 71.8 ms: 1.08x faster                                                           |
| xml_etree_parse      | 113 ms                                                          | 114 ms: 1.01x slower                                                            |
| json_dumps           | 7.40 ms                                                         | 7.71 ms: 1.04x slower                                                           |
| json_loads           | 20.4 us                                                         | 21.5 us: 1.06x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.15x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250208-pythonperf1_win32-x86-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 22.6 ms: 1.19x slower                                                           |
| python_startup         | 22.4 ms                                                         | 29.6 ms: 1.33x slower                                                           |
| Geometric mean         | (ref)                                                           | 1.25x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250208-pythonperf1_win32-x86-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 7.59 ms: 1.31x faster                                                           |
| django_template | 36.9 ms                                                         | 28.6 ms: 1.29x faster                                                           |
| Geometric mean  | (ref)                                                           | 1.30x faster                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250208-pythonperf1_win32-x86-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| generators                 | 38.5 ms                                                         | 17.5 ms: 2.20x faster                                                           |
| deepcopy_memo              | 38.4 us                                                         | 17.7 us: 2.17x faster                                                           |
| nbody                      | 127 ms                                                          | 64.5 ms: 1.97x faster                                                           |
| deepcopy                   | 360 us                                                          | 189 us: 1.90x faster                                                            |
| deltablue                  | 3.58 ms                                                         | 1.97 ms: 1.82x faster                                                           |
| async_tree_io_tg           | 677 ms                                                          | 373 ms: 1.82x faster                                                            |
| async_tree_io              | 693 ms                                                          | 385 ms: 1.80x faster                                                            |
| scimark_sor                | 130 ms                                                          | 72.7 ms: 1.79x faster                                                           |
| go                         | 137 ms                                                          | 77.5 ms: 1.77x faster                                                           |
| spectral_norm              | 104 ms                                                          | 58.6 ms: 1.77x faster                                                           |
| float                      | 76.7 ms                                                         | 44.0 ms: 1.74x faster                                                           |
| async_tree_none_tg         | 278 ms                                                          | 162 ms: 1.71x faster                                                            |
| async_tree_memoization     | 364 ms                                                          | 215 ms: 1.69x faster                                                            |
| async_tree_none            | 298 ms                                                          | 176 ms: 1.69x faster                                                            |
| raytrace                   | 308 ms                                                          | 186 ms: 1.66x faster                                                            |
| async_tree_memoization_tg  | 350 ms                                                          | 213 ms: 1.65x faster                                                            |
| hexiom                     | 6.82 ms                                                         | 4.22 ms: 1.62x faster                                                           |
| deepcopy_reduce            | 3.23 us                                                         | 2.01 us: 1.60x faster                                                           |
| scimark_monte_carlo        | 66.4 ms                                                         | 41.6 ms: 1.60x faster                                                           |
| comprehensions             | 19.2 us                                                         | 12.1 us: 1.59x faster                                                           |
| chaos                      | 69.4 ms                                                         | 43.8 ms: 1.59x faster                                                           |
| coroutines                 | 20.9 ms                                                         | 13.2 ms: 1.58x faster                                                           |
| tomli_loads                | 2.20 sec                                                        | 1.39 sec: 1.58x faster                                                          |
| logging_silent             | 101 ns                                                          | 66.4 ns: 1.52x faster                                                           |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 2.58 ms: 1.50x faster                                                           |
| sqlglot_parse              | 1.25 ms                                                         | 858 us: 1.45x faster                                                            |
| pyflate                    | 424 ms                                                          | 293 ms: 1.45x faster                                                            |
| regex_compile              | 129 ms                                                          | 90.0 ms: 1.43x faster                                                           |
| sqlglot_transpile          | 1.53 ms                                                         | 1.08 ms: 1.42x faster                                                           |
| scimark_fft                | 271 ms                                                          | 193 ms: 1.40x faster                                                            |
| pprint_pformat             | 1.50 sec                                                        | 1.07 sec: 1.40x faster                                                          |
| unpickle_pure_python       | 210 us                                                          | 151 us: 1.39x faster                                                            |
| pathlib                    | 91.4 ms                                                         | 66.0 ms: 1.39x faster                                                           |
| pprint_safe_repr           | 721 ms                                                          | 524 ms: 1.37x faster                                                            |
| nqueens                    | 93.7 ms                                                         | 68.4 ms: 1.37x faster                                                           |
| scimark_lu                 | 93.2 ms                                                         | 68.5 ms: 1.36x faster                                                           |
| logging_simple             | 9.75 us                                                         | 7.17 us: 1.36x faster                                                           |
| logging_format             | 10.4 us                                                         | 7.65 us: 1.36x faster                                                           |
| async_generators           | 313 ms                                                          | 231 ms: 1.35x faster                                                            |
| richards                   | 41.3 ms                                                         | 30.6 ms: 1.35x faster                                                           |
| richards_super             | 46.5 ms                                                         | 34.8 ms: 1.33x faster                                                           |
| mako                       | 9.96 ms                                                         | 7.59 ms: 1.31x faster                                                           |
| pickle_pure_python         | 286 us                                                          | 220 us: 1.30x faster                                                            |
| fannkuch                   | 354 ms                                                          | 273 ms: 1.30x faster                                                            |
| django_template            | 36.9 ms                                                         | 28.6 ms: 1.29x faster                                                           |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 438 ms: 1.29x faster                                                            |
| pycparser                  | 978 ms                                                          | 765 ms: 1.28x faster                                                            |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 429 ms: 1.27x faster                                                            |
| sqlglot_optimize           | 48.5 ms                                                         | 38.3 ms: 1.27x faster                                                           |
| crypto_pyaes               | 69.2 ms                                                         | 54.9 ms: 1.26x faster                                                           |
| sympy_str                  | 240 ms                                                          | 190 ms: 1.26x faster                                                            |
| sympy_sum                  | 123 ms                                                          | 98.1 ms: 1.25x faster                                                           |
| sympy_integrate            | 17.5 ms                                                         | 14.0 ms: 1.25x faster                                                           |
| dulwich_log                | 58.5 ms                                                         | 46.8 ms: 1.25x faster                                                           |
| sympy_expand               | 398 ms                                                          | 328 ms: 1.21x faster                                                            |
| 2to3                       | 280 ms                                                          | 240 ms: 1.17x faster                                                            |
| meteor_contest             | 86.9 ms                                                         | 74.9 ms: 1.16x faster                                                           |
| docutils                   | 1.98 sec                                                        | 1.73 sec: 1.15x faster                                                          |
| xml_etree_process          | 53.2 ms                                                         | 46.6 ms: 1.14x faster                                                           |
| sqlite_synth               | 2.07 us                                                         | 1.85 us: 1.12x faster                                                           |
| xml_etree_generate         | 72.1 ms                                                         | 66.3 ms: 1.09x faster                                                           |
| xml_etree_iterparse        | 77.6 ms                                                         | 71.8 ms: 1.08x faster                                                           |
| mdp                        | 1.91 sec                                                        | 1.77 sec: 1.08x faster                                                          |
| regex_effbot               | 2.04 ms                                                         | 1.97 ms: 1.03x faster                                                           |
| xml_etree_parse            | 113 ms                                                          | 114 ms: 1.01x slower                                                            |
| json                       | 4.15 ms                                                         | 4.21 ms: 1.01x slower                                                           |
| regex_dna                  | 127 ms                                                          | 132 ms: 1.04x slower                                                            |
| json_dumps                 | 7.40 ms                                                         | 7.71 ms: 1.04x slower                                                           |
| json_loads                 | 20.4 us                                                         | 21.5 us: 1.06x slower                                                           |
| telco                      | 5.51 ms                                                         | 5.91 ms: 1.07x slower                                                           |
| pidigits                   | 199 ms                                                          | 217 ms: 1.09x slower                                                            |
| coverage                   | 48.4 ms                                                         | 55.7 ms: 1.15x slower                                                           |
| regex_v8                   | 15.0 ms                                                         | 17.4 ms: 1.16x slower                                                           |
| python_startup_no_site     | 19.1 ms                                                         | 22.6 ms: 1.19x slower                                                           |
| bench_thread_pool          | 1.10 ms                                                         | 1.31 ms: 1.19x slower                                                           |
| bench_mp_pool              | 75.4 ms                                                         | 98.1 ms: 1.30x slower                                                           |
| python_startup             | 22.4 ms                                                         | 29.6 ms: 1.33x slower                                                           |
| gc_traversal               | 1.44 ms                                                         | 2.43 ms: 1.69x slower                                                           |
| create_gc_cycles           | 652 us                                                          | 1.19 ms: 1.83x slower                                                           |
| sqlglot_normalize          | 100 ms                                                          | 192 ms: 1.92x slower                                                            |
| Geometric mean             | (ref)                                                           | 1.28x faster                                                                    |

Benchmark hidden because not significant (1): typing_runtime_protocols
Ignored benchmarks (15) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20250208-3.14.0a4+-29f8a67-CLANG/bm-20250208-pythonperf1_win32-x86-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.289x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.27x
- 95% likely to have a speedup of 1.27x
- 99% likely to have a speedup of 1.25x

# Memory
- memory change: unknown