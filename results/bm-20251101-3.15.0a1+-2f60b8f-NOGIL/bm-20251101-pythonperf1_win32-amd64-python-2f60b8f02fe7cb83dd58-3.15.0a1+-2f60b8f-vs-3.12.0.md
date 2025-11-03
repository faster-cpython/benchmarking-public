# Results vs. 3.12.0

- fork: python
- ref: 2f60b8f02fe7cb83dd58
- machine: windows-amd64
- commit hash: 2f60b8f
- commit date: 2025-11-01
- overall geometric mean: 1.387x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.30x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20251101-pythonperf1_win32-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 213 ms: 1.31x faster                                                              |
| docutils       | 1.98 sec                                                        | 2.70 sec: 1.36x slower                                                            |
| Geometric mean | (ref)                                                           | 1.02x slower                                                                      |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20251101-pythonperf1_win32-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|----------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| async_tree_io_tg           | 677 ms                                                          | 313 ms: 2.17x faster                                                              |
| async_tree_io              | 693 ms                                                          | 332 ms: 2.08x faster                                                              |
| async_tree_none_tg         | 278 ms                                                          | 140 ms: 1.99x faster                                                              |
| async_tree_memoization_tg  | 350 ms                                                          | 181 ms: 1.94x faster                                                              |
| async_tree_memoization     | 364 ms                                                          | 199 ms: 1.83x faster                                                              |
| async_tree_none            | 298 ms                                                          | 165 ms: 1.80x faster                                                              |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 305 ms: 1.79x faster                                                              |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 331 ms: 1.70x faster                                                              |
| Geometric mean             | (ref)                                                           | 1.91x faster                                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20251101-pythonperf1_win32-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| float          | 76.7 ms                                                         | 44.1 ms: 1.74x faster                                                             |
| nbody          | 127 ms                                                          | 76.7 ms: 1.66x faster                                                             |
| pidigits       | 199 ms                                                          | 135 ms: 1.48x faster                                                              |
| Geometric mean | (ref)                                                           | 1.62x faster                                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20251101-pythonperf1_win32-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 88.1 ms: 1.47x faster                                                             |
| regex_effbot   | 2.04 ms                                                         | 1.53 ms: 1.33x faster                                                             |
| regex_v8       | 15.0 ms                                                         | 13.2 ms: 1.14x faster                                                             |
| regex_dna      | 127 ms                                                          | 114 ms: 1.12x faster                                                              |
| Geometric mean | (ref)                                                           | 1.25x faster                                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20251101-pythonperf1_win32-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|----------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| unpickle_pure_python | 210 us                                                          | 148 us: 1.41x faster                                                              |
| json_loads           | 20.4 us                                                         | 15.6 us: 1.30x faster                                                             |
| xml_etree_iterparse  | 77.6 ms                                                         | 60.4 ms: 1.29x faster                                                             |
| pickle_pure_python   | 286 us                                                          | 224 us: 1.28x faster                                                              |
| xml_etree_parse      | 113 ms                                                          | 89.0 ms: 1.27x faster                                                             |
| json_dumps           | 7.40 ms                                                         | 5.95 ms: 1.24x faster                                                             |
| xml_etree_process    | 53.2 ms                                                         | 43.1 ms: 1.24x faster                                                             |
| xml_etree_generate   | 72.1 ms                                                         | 60.4 ms: 1.19x faster                                                             |
| pickle_list          | 3.37 us                                                         | 3.02 us: 1.12x faster                                                             |
| unpickle_list        | 2.95 us                                                         | 2.99 us: 1.02x slower                                                             |
| unpickle             | 9.71 us                                                         | 9.87 us: 1.02x slower                                                             |
| Geometric mean       | (ref)                                                           | 1.15x faster                                                                      |

Benchmark hidden because not significant (3): pickle_dict, pickle, tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20251101-pythonperf1_win32-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup | 22.4 ms                                                         | 25.2 ms: 1.13x slower                                                             |
| Geometric mean | (ref)                                                           | 1.06x slower                                                                      |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20251101-pythonperf1_win32-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|-----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| django_template | 36.9 ms                                                         | 25.8 ms: 1.43x faster                                                             |
| mako            | 9.96 ms                                                         | 9.61 ms: 1.04x faster                                                             |
| Geometric mean  | (ref)                                                           | 1.22x faster                                                                      |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20251101-pythonperf1_win32-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|----------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| asyncio_tcp_ssl            | 17.7 sec                                                        | 2.28 sec: 7.75x faster                                                            |
| pathlib                    | 91.4 ms                                                         | 28.8 ms: 3.17x faster                                                             |
| async_tree_io_tg           | 677 ms                                                          | 313 ms: 2.17x faster                                                              |
| async_tree_io              | 693 ms                                                          | 332 ms: 2.08x faster                                                              |
| deepcopy_memo              | 38.4 us                                                         | 18.9 us: 2.03x faster                                                             |
| async_tree_none_tg         | 278 ms                                                          | 140 ms: 1.99x faster                                                              |
| deepcopy                   | 360 us                                                          | 182 us: 1.98x faster                                                              |
| mdp                        | 1.91 sec                                                        | 973 ms: 1.96x faster                                                              |
| async_tree_memoization_tg  | 350 ms                                                          | 181 ms: 1.94x faster                                                              |
| generators                 | 38.5 ms                                                         | 21.1 ms: 1.83x faster                                                             |
| async_tree_memoization     | 364 ms                                                          | 199 ms: 1.83x faster                                                              |
| async_tree_none            | 298 ms                                                          | 165 ms: 1.80x faster                                                              |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 305 ms: 1.79x faster                                                              |
| unpack_sequence            | 62.5 ns                                                         | 35.0 ns: 1.79x faster                                                             |
| float                      | 76.7 ms                                                         | 44.1 ms: 1.74x faster                                                             |
| logging_silent             | 101 ns                                                          | 58.3 ns: 1.73x faster                                                             |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 331 ms: 1.70x faster                                                              |
| comprehensions             | 19.2 us                                                         | 11.5 us: 1.67x faster                                                             |
| nbody                      | 127 ms                                                          | 76.7 ms: 1.66x faster                                                             |
| deepcopy_reduce            | 3.23 us                                                         | 2.00 us: 1.62x faster                                                             |
| go                         | 137 ms                                                          | 85.6 ms: 1.61x faster                                                             |
| chaos                      | 69.4 ms                                                         | 44.7 ms: 1.55x faster                                                             |
| deltablue                  | 3.58 ms                                                         | 2.31 ms: 1.55x faster                                                             |
| hexiom                     | 6.82 ms                                                         | 4.44 ms: 1.54x faster                                                             |
| scimark_sor                | 130 ms                                                          | 84.8 ms: 1.53x faster                                                             |
| logging_simple             | 9.75 us                                                         | 6.40 us: 1.52x faster                                                             |
| raytrace                   | 308 ms                                                          | 203 ms: 1.52x faster                                                              |
| spectral_norm              | 104 ms                                                          | 69.1 ms: 1.50x faster                                                             |
| logging_format             | 10.4 us                                                         | 6.92 us: 1.50x faster                                                             |
| sqlite_synth               | 2.07 us                                                         | 1.40 us: 1.48x faster                                                             |
| pidigits                   | 199 ms                                                          | 135 ms: 1.48x faster                                                              |
| scimark_lu                 | 93.2 ms                                                         | 63.2 ms: 1.47x faster                                                             |
| dulwich_log                | 58.5 ms                                                         | 39.8 ms: 1.47x faster                                                             |
| regex_compile              | 129 ms                                                          | 88.1 ms: 1.47x faster                                                             |
| django_template            | 36.9 ms                                                         | 25.8 ms: 1.43x faster                                                             |
| pyflate                    | 424 ms                                                          | 297 ms: 1.43x faster                                                              |
| pycparser                  | 978 ms                                                          | 686 ms: 1.43x faster                                                              |
| unpickle_pure_python       | 210 us                                                          | 148 us: 1.41x faster                                                              |
| scimark_fft                | 271 ms                                                          | 192 ms: 1.41x faster                                                              |
| coroutines                 | 20.9 ms                                                         | 14.9 ms: 1.41x faster                                                             |
| json                       | 4.15 ms                                                         | 3.03 ms: 1.37x faster                                                             |
| scimark_monte_carlo        | 66.4 ms                                                         | 49.3 ms: 1.35x faster                                                             |
| sympy_str                  | 240 ms                                                          | 178 ms: 1.35x faster                                                              |
| pprint_safe_repr           | 721 ms                                                          | 535 ms: 1.35x faster                                                              |
| sympy_sum                  | 123 ms                                                          | 91.5 ms: 1.34x faster                                                             |
| regex_effbot               | 2.04 ms                                                         | 1.53 ms: 1.33x faster                                                             |
| richards                   | 41.3 ms                                                         | 31.3 ms: 1.32x faster                                                             |
| 2to3                       | 280 ms                                                          | 213 ms: 1.31x faster                                                              |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 2.94 ms: 1.31x faster                                                             |
| sympy_expand               | 398 ms                                                          | 303 ms: 1.31x faster                                                              |
| json_loads                 | 20.4 us                                                         | 15.6 us: 1.30x faster                                                             |
| nqueens                    | 93.7 ms                                                         | 72.1 ms: 1.30x faster                                                             |
| xml_etree_iterparse        | 77.6 ms                                                         | 60.4 ms: 1.29x faster                                                             |
| sympy_integrate            | 17.5 ms                                                         | 13.7 ms: 1.28x faster                                                             |
| pickle_pure_python         | 286 us                                                          | 224 us: 1.28x faster                                                              |
| xml_etree_parse            | 113 ms                                                          | 89.0 ms: 1.27x faster                                                             |
| richards_super             | 46.5 ms                                                         | 36.6 ms: 1.27x faster                                                             |
| asyncio_tcp                | 662 ms                                                          | 528 ms: 1.25x faster                                                              |
| gc_traversal               | 1.44 ms                                                         | 1.15 ms: 1.25x faster                                                             |
| json_dumps                 | 7.40 ms                                                         | 5.95 ms: 1.24x faster                                                             |
| xml_etree_process          | 53.2 ms                                                         | 43.1 ms: 1.24x faster                                                             |
| crypto_pyaes               | 69.2 ms                                                         | 56.5 ms: 1.23x faster                                                             |
| async_generators           | 313 ms                                                          | 256 ms: 1.22x faster                                                              |
| xml_etree_generate         | 72.1 ms                                                         | 60.4 ms: 1.19x faster                                                             |
| fannkuch                   | 354 ms                                                          | 299 ms: 1.18x faster                                                              |
| regex_v8                   | 15.0 ms                                                         | 13.2 ms: 1.14x faster                                                             |
| telco                      | 5.51 ms                                                         | 4.85 ms: 1.14x faster                                                             |
| pickle_list                | 3.37 us                                                         | 3.02 us: 1.12x faster                                                             |
| regex_dna                  | 127 ms                                                          | 114 ms: 1.12x faster                                                              |
| bench_thread_pool          | 1.10 ms                                                         | 1.01 ms: 1.09x faster                                                             |
| typing_runtime_protocols   | 126 us                                                          | 121 us: 1.04x faster                                                              |
| bench_mp_pool              | 75.4 ms                                                         | 72.3 ms: 1.04x faster                                                             |
| mako                       | 9.96 ms                                                         | 9.61 ms: 1.04x faster                                                             |
| meteor_contest             | 86.9 ms                                                         | 85.1 ms: 1.02x faster                                                             |
| unpickle_list              | 2.95 us                                                         | 2.99 us: 1.02x slower                                                             |
| unpickle                   | 9.71 us                                                         | 9.87 us: 1.02x slower                                                             |
| python_startup             | 22.4 ms                                                         | 25.2 ms: 1.13x slower                                                             |
| docutils                   | 1.98 sec                                                        | 2.70 sec: 1.36x slower                                                            |
| coverage                   | 48.4 ms                                                         | 66.3 ms: 1.37x slower                                                             |
| create_gc_cycles           | 652 us                                                          | 1.01 ms: 1.55x slower                                                             |
| Geometric mean             | (ref)                                                           | 1.39x faster                                                                      |

Benchmark hidden because not significant (5): python_startup_no_site, pickle_dict, pickle, tomli_loads, pprint_pformat
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (17) of results/bm-20251101-3.15.0a1+-2f60b8f-NOGIL/bm-20251101-pythonperf1_win32-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.387x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.34x
- 95% likely to have a speedup of 1.32x
- 99% likely to have a speedup of 1.30x

# Memory
- memory change: unknown