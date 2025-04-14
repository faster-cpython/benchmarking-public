# Results vs. 3.12.0

- fork: python
- ref: 61b35f74aa4a6ac60663
- machine: windows-x86
- commit hash: 61b35f7
- commit date: 2025-01-18
- overall geometric mean: 1.037x faster
- HPT reliability: 99.06%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250118-pythonperf1_win32-x86-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 282 ms: 1.01x slower                                                            |
| docutils       | 1.98 sec                                                        | 2.06 sec: 1.04x slower                                                          |
| Geometric mean | (ref)                                                           | 1.02x slower                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250118-pythonperf1_win32-x86-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_io_tg           | 677 ms                                                          | 473 ms: 1.43x faster                                                            |
| async_tree_io              | 693 ms                                                          | 490 ms: 1.41x faster                                                            |
| async_tree_memoization_tg  | 350 ms                                                          | 256 ms: 1.37x faster                                                            |
| async_tree_none_tg         | 278 ms                                                          | 203 ms: 1.37x faster                                                            |
| async_tree_none            | 298 ms                                                          | 228 ms: 1.31x faster                                                            |
| async_tree_memoization     | 364 ms                                                          | 278 ms: 1.31x faster                                                            |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 447 ms: 1.22x faster                                                            |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 468 ms: 1.20x faster                                                            |
| Geometric mean             | (ref)                                                           | 1.33x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250118-pythonperf1_win32-x86-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 76.7 ms                                                         | 66.7 ms: 1.15x faster                                                           |
| nbody          | 127 ms                                                          | 119 ms: 1.07x faster                                                            |
| pidigits       | 199 ms                                                          | 201 ms: 1.01x slower                                                            |
| Geometric mean | (ref)                                                           | 1.07x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250118-pythonperf1_win32-x86-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_effbot   | 2.04 ms                                                         | 1.57 ms: 1.30x faster                                                           |
| regex_dna      | 127 ms                                                          | 123 ms: 1.04x faster                                                            |
| regex_compile  | 129 ms                                                          | 127 ms: 1.02x faster                                                            |
| regex_v8       | 15.0 ms                                                         | 16.6 ms: 1.10x slower                                                           |
| Geometric mean | (ref)                                                           | 1.05x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250118-pythonperf1_win32-x86-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7 |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 2.20 sec                                                        | 2.02 sec: 1.09x faster                                                          |
| xml_etree_iterparse  | 77.6 ms                                                         | 71.4 ms: 1.09x faster                                                           |
| xml_etree_parse      | 113 ms                                                          | 109 ms: 1.04x faster                                                            |
| unpickle_pure_python | 210 us                                                          | 212 us: 1.01x slower                                                            |
| xml_etree_generate   | 72.1 ms                                                         | 73.6 ms: 1.02x slower                                                           |
| unpickle_list        | 2.95 us                                                         | 3.02 us: 1.03x slower                                                           |
| xml_etree_process    | 53.2 ms                                                         | 54.8 ms: 1.03x slower                                                           |
| pickle_dict          | 19.9 us                                                         | 21.0 us: 1.05x slower                                                           |
| pickle_pure_python   | 286 us                                                          | 305 us: 1.07x slower                                                            |
| json_loads           | 20.4 us                                                         | 22.0 us: 1.08x slower                                                           |
| pickle_list          | 3.37 us                                                         | 3.74 us: 1.11x slower                                                           |
| unpickle             | 9.71 us                                                         | 11.2 us: 1.16x slower                                                           |
| pickle               | 7.79 us                                                         | 9.51 us: 1.22x slower                                                           |
| json_dumps           | 7.40 ms                                                         | 9.68 ms: 1.31x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.06x slower                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250118-pythonperf1_win32-x86-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7 |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 20.3 ms: 1.06x slower                                                           |
| python_startup         | 22.4 ms                                                         | 26.9 ms: 1.20x slower                                                           |
| Geometric mean         | (ref)                                                           | 1.13x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250118-pythonperf1_win32-x86-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7 |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 8.96 ms: 1.11x faster                                                           |
| django_template | 36.9 ms                                                         | 37.7 ms: 1.02x slower                                                           |
| Geometric mean  | (ref)                                                           | 1.04x faster                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250118-pythonperf1_win32-x86-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| deepcopy_memo              | 38.4 us                                                         | 26.3 us: 1.46x faster                                                           |
| async_tree_io_tg           | 677 ms                                                          | 473 ms: 1.43x faster                                                            |
| async_tree_io              | 693 ms                                                          | 490 ms: 1.41x faster                                                            |
| async_tree_memoization_tg  | 350 ms                                                          | 256 ms: 1.37x faster                                                            |
| async_tree_none_tg         | 278 ms                                                          | 203 ms: 1.37x faster                                                            |
| async_tree_none            | 298 ms                                                          | 228 ms: 1.31x faster                                                            |
| async_tree_memoization     | 364 ms                                                          | 278 ms: 1.31x faster                                                            |
| deepcopy                   | 360 us                                                          | 276 us: 1.31x faster                                                            |
| regex_effbot               | 2.04 ms                                                         | 1.57 ms: 1.30x faster                                                           |
| spectral_norm              | 104 ms                                                          | 84.5 ms: 1.23x faster                                                           |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 447 ms: 1.22x faster                                                            |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 468 ms: 1.20x faster                                                            |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 3.33 ms: 1.16x faster                                                           |
| comprehensions             | 19.2 us                                                         | 16.5 us: 1.16x faster                                                           |
| float                      | 76.7 ms                                                         | 66.7 ms: 1.15x faster                                                           |
| unpack_sequence            | 62.5 ns                                                         | 54.5 ns: 1.15x faster                                                           |
| generators                 | 38.5 ms                                                         | 33.6 ms: 1.15x faster                                                           |
| go                         | 137 ms                                                          | 122 ms: 1.13x faster                                                            |
| deepcopy_reduce            | 3.23 us                                                         | 2.87 us: 1.13x faster                                                           |
| scimark_lu                 | 93.2 ms                                                         | 83.9 ms: 1.11x faster                                                           |
| mako                       | 9.96 ms                                                         | 8.96 ms: 1.11x faster                                                           |
| deltablue                  | 3.58 ms                                                         | 3.25 ms: 1.10x faster                                                           |
| pyflate                    | 424 ms                                                          | 385 ms: 1.10x faster                                                            |
| tomli_loads                | 2.20 sec                                                        | 2.02 sec: 1.09x faster                                                          |
| xml_etree_iterparse        | 77.6 ms                                                         | 71.4 ms: 1.09x faster                                                           |
| hexiom                     | 6.82 ms                                                         | 6.28 ms: 1.09x faster                                                           |
| scimark_sor                | 130 ms                                                          | 120 ms: 1.08x faster                                                            |
| chaos                      | 69.4 ms                                                         | 64.3 ms: 1.08x faster                                                           |
| logging_simple             | 9.75 us                                                         | 9.09 us: 1.07x faster                                                           |
| nbody                      | 127 ms                                                          | 119 ms: 1.07x faster                                                            |
| logging_format             | 10.4 us                                                         | 9.77 us: 1.07x faster                                                           |
| raytrace                   | 308 ms                                                          | 289 ms: 1.07x faster                                                            |
| pathlib                    | 91.4 ms                                                         | 86.2 ms: 1.06x faster                                                           |
| logging_silent             | 101 ns                                                          | 95.4 ns: 1.06x faster                                                           |
| scimark_monte_carlo        | 66.4 ms                                                         | 63.3 ms: 1.05x faster                                                           |
| mdp                        | 1.91 sec                                                        | 1.83 sec: 1.05x faster                                                          |
| meteor_contest             | 86.9 ms                                                         | 83.2 ms: 1.04x faster                                                           |
| nqueens                    | 93.7 ms                                                         | 89.8 ms: 1.04x faster                                                           |
| xml_etree_parse            | 113 ms                                                          | 109 ms: 1.04x faster                                                            |
| regex_dna                  | 127 ms                                                          | 123 ms: 1.04x faster                                                            |
| asyncio_tcp_ssl            | 17.7 sec                                                        | 17.2 sec: 1.03x faster                                                          |
| dulwich_log                | 58.5 ms                                                         | 57.0 ms: 1.03x faster                                                           |
| scimark_fft                | 271 ms                                                          | 264 ms: 1.02x faster                                                            |
| sqlite_synth               | 2.07 us                                                         | 2.04 us: 1.02x faster                                                           |
| regex_compile              | 129 ms                                                          | 127 ms: 1.02x faster                                                            |
| pprint_pformat             | 1.50 sec                                                        | 1.49 sec: 1.01x faster                                                          |
| crypto_pyaes               | 69.2 ms                                                         | 68.7 ms: 1.01x faster                                                           |
| 2to3                       | 280 ms                                                          | 282 ms: 1.01x slower                                                            |
| pidigits                   | 199 ms                                                          | 201 ms: 1.01x slower                                                            |
| sqlglot_optimize           | 48.5 ms                                                         | 48.9 ms: 1.01x slower                                                           |
| fannkuch                   | 354 ms                                                          | 358 ms: 1.01x slower                                                            |
| unpickle_pure_python       | 210 us                                                          | 212 us: 1.01x slower                                                            |
| coroutines                 | 20.9 ms                                                         | 21.2 ms: 1.01x slower                                                           |
| sympy_sum                  | 123 ms                                                          | 125 ms: 1.02x slower                                                            |
| sympy_integrate            | 17.5 ms                                                         | 17.9 ms: 1.02x slower                                                           |
| xml_etree_generate         | 72.1 ms                                                         | 73.6 ms: 1.02x slower                                                           |
| django_template            | 36.9 ms                                                         | 37.7 ms: 1.02x slower                                                           |
| sqlglot_transpile          | 1.53 ms                                                         | 1.56 ms: 1.02x slower                                                           |
| pycparser                  | 978 ms                                                          | 1.00 sec: 1.03x slower                                                          |
| unpickle_list              | 2.95 us                                                         | 3.02 us: 1.03x slower                                                           |
| sqlglot_normalize          | 100 ms                                                          | 103 ms: 1.03x slower                                                            |
| sqlglot_parse              | 1.25 ms                                                         | 1.28 ms: 1.03x slower                                                           |
| xml_etree_process          | 53.2 ms                                                         | 54.8 ms: 1.03x slower                                                           |
| async_generators           | 313 ms                                                          | 323 ms: 1.03x slower                                                            |
| docutils                   | 1.98 sec                                                        | 2.06 sec: 1.04x slower                                                          |
| sympy_str                  | 240 ms                                                          | 249 ms: 1.04x slower                                                            |
| richards_super             | 46.5 ms                                                         | 48.6 ms: 1.05x slower                                                           |
| richards                   | 41.3 ms                                                         | 43.3 ms: 1.05x slower                                                           |
| pickle_dict                | 19.9 us                                                         | 21.0 us: 1.05x slower                                                           |
| python_startup_no_site     | 19.1 ms                                                         | 20.3 ms: 1.06x slower                                                           |
| pickle_pure_python         | 286 us                                                          | 305 us: 1.07x slower                                                            |
| json_loads                 | 20.4 us                                                         | 22.0 us: 1.08x slower                                                           |
| sympy_expand               | 398 ms                                                          | 434 ms: 1.09x slower                                                            |
| regex_v8                   | 15.0 ms                                                         | 16.6 ms: 1.10x slower                                                           |
| pickle_list                | 3.37 us                                                         | 3.74 us: 1.11x slower                                                           |
| coverage                   | 48.4 ms                                                         | 53.8 ms: 1.11x slower                                                           |
| json                       | 4.15 ms                                                         | 4.67 ms: 1.13x slower                                                           |
| unpickle                   | 9.71 us                                                         | 11.2 us: 1.16x slower                                                           |
| python_startup             | 22.4 ms                                                         | 26.9 ms: 1.20x slower                                                           |
| pickle                     | 7.79 us                                                         | 9.51 us: 1.22x slower                                                           |
| asyncio_tcp                | 662 ms                                                          | 811 ms: 1.22x slower                                                            |
| gc_traversal               | 1.44 ms                                                         | 1.80 ms: 1.25x slower                                                           |
| bench_mp_pool              | 75.4 ms                                                         | 96.8 ms: 1.28x slower                                                           |
| json_dumps                 | 7.40 ms                                                         | 9.68 ms: 1.31x slower                                                           |
| telco                      | 5.51 ms                                                         | 7.21 ms: 1.31x slower                                                           |
| typing_runtime_protocols   | 126 us                                                          | 165 us: 1.31x slower                                                            |
| create_gc_cycles           | 652 us                                                          | 1.06 ms: 1.62x slower                                                           |
| Geometric mean             | (ref)                                                           | 1.02x faster                                                                    |

Benchmark hidden because not significant (2): bench_thread_pool, pprint_safe_repr
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (13) of results/bm-20250118-3.14.0a4+-61b35f7/bm-20250118-pythonperf1_win32-x86-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.037x faster

# HPT report

- Reliability score: 99.06% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown