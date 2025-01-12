# Results vs. 3.12.0

- fork: python
- ref: 22a442181d5f1ac496da
- machine: windows-x86
- commit hash: 22a4421
- commit date: 2025-01-11
- overall geometric mean: 1.074x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.01x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250111-pythonperf1_win32-x86-python-22a442181d5f1ac496da-3.14.0a3+-22a4421 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 264 ms: 1.06x faster                                                            |
| Geometric mean | (ref)                                                           | 1.03x faster                                                                    |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250111-pythonperf1_win32-x86-python-22a442181d5f1ac496da-3.14.0a3+-22a4421 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_io_tg           | 677 ms                                                          | 457 ms: 1.48x faster                                                            |
| async_tree_io              | 693 ms                                                          | 485 ms: 1.43x faster                                                            |
| async_tree_memoization_tg  | 350 ms                                                          | 249 ms: 1.41x faster                                                            |
| async_tree_none_tg         | 278 ms                                                          | 197 ms: 1.41x faster                                                            |
| async_tree_memoization     | 364 ms                                                          | 285 ms: 1.28x faster                                                            |
| async_tree_none            | 298 ms                                                          | 233 ms: 1.27x faster                                                            |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 445 ms: 1.23x faster                                                            |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 473 ms: 1.19x faster                                                            |
| Geometric mean             | (ref)                                                           | 1.33x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250111-pythonperf1_win32-x86-python-22a442181d5f1ac496da-3.14.0a3+-22a4421 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 76.7 ms                                                         | 52.1 ms: 1.47x faster                                                           |
| nbody          | 127 ms                                                          | 100 ms: 1.27x faster                                                            |
| pidigits       | 199 ms                                                          | 201 ms: 1.01x slower                                                            |
| Geometric mean | (ref)                                                           | 1.23x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250111-pythonperf1_win32-x86-python-22a442181d5f1ac496da-3.14.0a3+-22a4421 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_effbot   | 2.04 ms                                                         | 1.54 ms: 1.33x faster                                                           |
| regex_compile  | 129 ms                                                          | 114 ms: 1.13x faster                                                            |
| regex_dna      | 127 ms                                                          | 116 ms: 1.09x faster                                                            |
| regex_v8       | 15.0 ms                                                         | 15.6 ms: 1.04x slower                                                           |
| Geometric mean | (ref)                                                           | 1.12x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250111-pythonperf1_win32-x86-python-22a442181d5f1ac496da-3.14.0a3+-22a4421 |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 2.20 sec                                                        | 1.77 sec: 1.24x faster                                                          |
| xml_etree_iterparse  | 77.6 ms                                                         | 66.4 ms: 1.17x faster                                                           |
| unpickle_pure_python | 210 us                                                          | 202 us: 1.04x faster                                                            |
| xml_etree_parse      | 113 ms                                                          | 109 ms: 1.03x faster                                                            |
| json_loads           | 20.4 us                                                         | 20.7 us: 1.02x slower                                                           |
| xml_etree_process    | 53.2 ms                                                         | 54.4 ms: 1.02x slower                                                           |
| pickle_pure_python   | 286 us                                                          | 298 us: 1.04x slower                                                            |
| xml_etree_generate   | 72.1 ms                                                         | 76.1 ms: 1.05x slower                                                           |
| pickle_dict          | 19.9 us                                                         | 21.3 us: 1.07x slower                                                           |
| unpickle             | 9.71 us                                                         | 10.7 us: 1.11x slower                                                           |
| pickle_list          | 3.37 us                                                         | 3.80 us: 1.13x slower                                                           |
| unpickle_list        | 2.95 us                                                         | 3.32 us: 1.13x slower                                                           |
| json_dumps           | 7.40 ms                                                         | 8.98 ms: 1.21x slower                                                           |
| pickle               | 7.79 us                                                         | 10.2 us: 1.31x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.04x slower                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250111-pythonperf1_win32-x86-python-22a442181d5f1ac496da-3.14.0a3+-22a4421 |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 19.4 ms: 1.02x slower                                                           |
| python_startup         | 22.4 ms                                                         | 25.8 ms: 1.16x slower                                                           |
| Geometric mean         | (ref)                                                           | 1.08x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250111-pythonperf1_win32-x86-python-22a442181d5f1ac496da-3.14.0a3+-22a4421 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako           | 9.96 ms                                                         | 7.42 ms: 1.34x faster                                                           |
| Geometric mean | (ref)                                                           | 1.16x faster                                                                    |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250111-pythonperf1_win32-x86-python-22a442181d5f1ac496da-3.14.0a3+-22a4421 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| deepcopy_memo              | 38.4 us                                                         | 23.8 us: 1.62x faster                                                           |
| async_tree_io_tg           | 677 ms                                                          | 457 ms: 1.48x faster                                                            |
| float                      | 76.7 ms                                                         | 52.1 ms: 1.47x faster                                                           |
| spectral_norm              | 104 ms                                                          | 72.6 ms: 1.43x faster                                                           |
| async_tree_io              | 693 ms                                                          | 485 ms: 1.43x faster                                                            |
| unpack_sequence            | 62.5 ns                                                         | 44.1 ns: 1.42x faster                                                           |
| async_tree_memoization_tg  | 350 ms                                                          | 249 ms: 1.41x faster                                                            |
| async_tree_none_tg         | 278 ms                                                          | 197 ms: 1.41x faster                                                            |
| mako                       | 9.96 ms                                                         | 7.42 ms: 1.34x faster                                                           |
| regex_effbot               | 2.04 ms                                                         | 1.54 ms: 1.33x faster                                                           |
| scimark_sor                | 130 ms                                                          | 98.3 ms: 1.32x faster                                                           |
| deepcopy                   | 360 us                                                          | 280 us: 1.29x faster                                                            |
| logging_silent             | 101 ns                                                          | 79.0 ns: 1.28x faster                                                           |
| scimark_lu                 | 93.2 ms                                                         | 73.0 ms: 1.28x faster                                                           |
| async_tree_memoization     | 364 ms                                                          | 285 ms: 1.28x faster                                                            |
| async_tree_none            | 298 ms                                                          | 233 ms: 1.27x faster                                                            |
| coroutines                 | 20.9 ms                                                         | 16.4 ms: 1.27x faster                                                           |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 3.03 ms: 1.27x faster                                                           |
| nbody                      | 127 ms                                                          | 100 ms: 1.27x faster                                                            |
| tomli_loads                | 2.20 sec                                                        | 1.77 sec: 1.24x faster                                                          |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 445 ms: 1.23x faster                                                            |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 473 ms: 1.19x faster                                                            |
| xml_etree_iterparse        | 77.6 ms                                                         | 66.4 ms: 1.17x faster                                                           |
| logging_simple             | 9.75 us                                                         | 8.57 us: 1.14x faster                                                           |
| scimark_fft                | 271 ms                                                          | 239 ms: 1.14x faster                                                            |
| dulwich_log                | 58.5 ms                                                         | 51.5 ms: 1.13x faster                                                           |
| regex_compile              | 129 ms                                                          | 114 ms: 1.13x faster                                                            |
| deltablue                  | 3.58 ms                                                         | 3.18 ms: 1.13x faster                                                           |
| logging_format             | 10.4 us                                                         | 9.23 us: 1.13x faster                                                           |
| deepcopy_reduce            | 3.23 us                                                         | 2.87 us: 1.12x faster                                                           |
| regex_dna                  | 127 ms                                                          | 116 ms: 1.09x faster                                                            |
| go                         | 137 ms                                                          | 126 ms: 1.09x faster                                                            |
| sqlglot_parse              | 1.25 ms                                                         | 1.15 ms: 1.09x faster                                                           |
| sqlglot_transpile          | 1.53 ms                                                         | 1.42 ms: 1.08x faster                                                           |
| sympy_sum                  | 123 ms                                                          | 115 ms: 1.07x faster                                                            |
| sqlite_synth               | 2.07 us                                                         | 1.94 us: 1.07x faster                                                           |
| chaos                      | 69.4 ms                                                         | 65.0 ms: 1.07x faster                                                           |
| scimark_monte_carlo        | 66.4 ms                                                         | 62.2 ms: 1.07x faster                                                           |
| pyflate                    | 424 ms                                                          | 400 ms: 1.06x faster                                                            |
| 2to3                       | 280 ms                                                          | 264 ms: 1.06x faster                                                            |
| comprehensions             | 19.2 us                                                         | 18.2 us: 1.06x faster                                                           |
| pathlib                    | 91.4 ms                                                         | 87.1 ms: 1.05x faster                                                           |
| bench_thread_pool          | 1.10 ms                                                         | 1.06 ms: 1.04x faster                                                           |
| unpickle_pure_python       | 210 us                                                          | 202 us: 1.04x faster                                                            |
| fannkuch                   | 354 ms                                                          | 342 ms: 1.03x faster                                                            |
| xml_etree_parse            | 113 ms                                                          | 109 ms: 1.03x faster                                                            |
| mdp                        | 1.91 sec                                                        | 1.85 sec: 1.03x faster                                                          |
| asyncio_tcp_ssl            | 17.7 sec                                                        | 17.1 sec: 1.03x faster                                                          |
| pycparser                  | 978 ms                                                          | 950 ms: 1.03x faster                                                            |
| sympy_str                  | 240 ms                                                          | 235 ms: 1.02x faster                                                            |
| generators                 | 38.5 ms                                                         | 38.0 ms: 1.01x faster                                                           |
| raytrace                   | 308 ms                                                          | 305 ms: 1.01x faster                                                            |
| sympy_integrate            | 17.5 ms                                                         | 17.4 ms: 1.01x faster                                                           |
| crypto_pyaes               | 69.2 ms                                                         | 69.8 ms: 1.01x slower                                                           |
| pidigits                   | 199 ms                                                          | 201 ms: 1.01x slower                                                            |
| python_startup_no_site     | 19.1 ms                                                         | 19.4 ms: 1.02x slower                                                           |
| json_loads                 | 20.4 us                                                         | 20.7 us: 1.02x slower                                                           |
| pprint_safe_repr           | 721 ms                                                          | 735 ms: 1.02x slower                                                            |
| nqueens                    | 93.7 ms                                                         | 95.6 ms: 1.02x slower                                                           |
| xml_etree_process          | 53.2 ms                                                         | 54.4 ms: 1.02x slower                                                           |
| meteor_contest             | 86.9 ms                                                         | 89.1 ms: 1.03x slower                                                           |
| regex_v8                   | 15.0 ms                                                         | 15.6 ms: 1.04x slower                                                           |
| sympy_expand               | 398 ms                                                          | 413 ms: 1.04x slower                                                            |
| richards_super             | 46.5 ms                                                         | 48.4 ms: 1.04x slower                                                           |
| pickle_pure_python         | 286 us                                                          | 298 us: 1.04x slower                                                            |
| richards                   | 41.3 ms                                                         | 43.1 ms: 1.04x slower                                                           |
| hexiom                     | 6.82 ms                                                         | 7.11 ms: 1.04x slower                                                           |
| sqlglot_optimize           | 48.5 ms                                                         | 50.6 ms: 1.04x slower                                                           |
| json                       | 4.15 ms                                                         | 4.36 ms: 1.05x slower                                                           |
| xml_etree_generate         | 72.1 ms                                                         | 76.1 ms: 1.05x slower                                                           |
| sqlglot_normalize          | 100 ms                                                          | 107 ms: 1.07x slower                                                            |
| pickle_dict                | 19.9 us                                                         | 21.3 us: 1.07x slower                                                           |
| async_generators           | 313 ms                                                          | 338 ms: 1.08x slower                                                            |
| coverage                   | 48.4 ms                                                         | 53.0 ms: 1.09x slower                                                           |
| unpickle                   | 9.71 us                                                         | 10.7 us: 1.11x slower                                                           |
| pickle_list                | 3.37 us                                                         | 3.80 us: 1.13x slower                                                           |
| unpickle_list              | 2.95 us                                                         | 3.32 us: 1.13x slower                                                           |
| python_startup             | 22.4 ms                                                         | 25.8 ms: 1.16x slower                                                           |
| bench_mp_pool              | 75.4 ms                                                         | 88.7 ms: 1.18x slower                                                           |
| json_dumps                 | 7.40 ms                                                         | 8.98 ms: 1.21x slower                                                           |
| gc_traversal               | 1.44 ms                                                         | 1.83 ms: 1.27x slower                                                           |
| pickle                     | 7.79 us                                                         | 10.2 us: 1.31x slower                                                           |
| typing_runtime_protocols   | 126 us                                                          | 167 us: 1.32x slower                                                            |
| telco                      | 5.51 ms                                                         | 7.31 ms: 1.33x slower                                                           |
| create_gc_cycles           | 652 us                                                          | 1.07 ms: 1.64x slower                                                           |
| Geometric mean             | (ref)                                                           | 1.06x faster                                                                    |

Benchmark hidden because not significant (4): django_template, docutils, pprint_pformat, asyncio_tcp
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (13) of results/bm-20250111-3.14.0a3+-22a4421-JIT/bm-20250111-pythonperf1_win32-x86-python-22a442181d5f1ac496da-3.14.0a3+-22a4421.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.074x faster

# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: unknown