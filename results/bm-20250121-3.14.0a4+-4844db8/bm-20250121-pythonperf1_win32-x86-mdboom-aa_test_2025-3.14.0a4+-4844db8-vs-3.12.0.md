# Results vs. 3.12.0

- fork: mdboom
- ref: aa_test_2025
- machine: windows-x86
- commit hash: 4844db8
- commit date: 2025-01-21
- overall geometric mean: 1.128x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.10x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250121-pythonperf1_win32-x86-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|----------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 256 ms: 1.09x faster                                                    |
| docutils       | 1.98 sec                                                        | 1.86 sec: 1.07x faster                                                  |
| Geometric mean | (ref)                                                           | 1.08x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250121-pythonperf1_win32-x86-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|----------------------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_io_tg           | 677 ms                                                          | 452 ms: 1.50x faster                                                    |
| async_tree_io              | 693 ms                                                          | 463 ms: 1.50x faster                                                    |
| async_tree_memoization_tg  | 350 ms                                                          | 249 ms: 1.41x faster                                                    |
| async_tree_none_tg         | 278 ms                                                          | 197 ms: 1.41x faster                                                    |
| async_tree_none            | 298 ms                                                          | 216 ms: 1.37x faster                                                    |
| async_tree_memoization     | 364 ms                                                          | 267 ms: 1.36x faster                                                    |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 440 ms: 1.24x faster                                                    |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 456 ms: 1.24x faster                                                    |
| Geometric mean             | (ref)                                                           | 1.37x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250121-pythonperf1_win32-x86-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|----------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 90.0 ms: 1.41x faster                                                   |
| float          | 76.7 ms                                                         | 56.5 ms: 1.36x faster                                                   |
| pidigits       | 199 ms                                                          | 202 ms: 1.01x slower                                                    |
| Geometric mean | (ref)                                                           | 1.24x faster                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250121-pythonperf1_win32-x86-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|----------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 2.04 ms                                                         | 1.58 ms: 1.29x faster                                                   |
| regex_compile  | 129 ms                                                          | 107 ms: 1.21x faster                                                    |
| regex_dna      | 127 ms                                                          | 117 ms: 1.09x faster                                                    |
| regex_v8       | 15.0 ms                                                         | 15.5 ms: 1.03x slower                                                   |
| Geometric mean | (ref)                                                           | 1.13x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250121-pythonperf1_win32-x86-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|----------------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| tomli_loads          | 2.20 sec                                                        | 1.71 sec: 1.28x faster                                                  |
| xml_etree_iterparse  | 77.6 ms                                                         | 66.8 ms: 1.16x faster                                                   |
| unpickle_pure_python | 210 us                                                          | 185 us: 1.13x faster                                                    |
| xml_etree_generate   | 72.1 ms                                                         | 67.9 ms: 1.06x faster                                                   |
| xml_etree_process    | 53.2 ms                                                         | 50.9 ms: 1.05x faster                                                   |
| xml_etree_parse      | 113 ms                                                          | 109 ms: 1.04x faster                                                    |
| json_loads           | 20.4 us                                                         | 21.4 us: 1.05x slower                                                   |
| json_dumps           | 7.40 ms                                                         | 9.40 ms: 1.27x slower                                                   |
| Geometric mean       | (ref)                                                           | 1.04x faster                                                            |

Benchmark hidden because not significant (1): pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250121-pythonperf1_win32-x86-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|------------------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 20.1 ms: 1.05x slower                                                   |
| python_startup         | 22.4 ms                                                         | 27.0 ms: 1.21x slower                                                   |
| Geometric mean         | (ref)                                                           | 1.13x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250121-pythonperf1_win32-x86-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|-----------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 7.69 ms: 1.29x faster                                                   |
| django_template | 36.9 ms                                                         | 33.4 ms: 1.11x faster                                                   |
| Geometric mean  | (ref)                                                           | 1.20x faster                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250121-pythonperf1_win32-x86-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|----------------------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| deepcopy_memo              | 38.4 us                                                         | 21.5 us: 1.78x faster                                                   |
| deepcopy                   | 360 us                                                          | 235 us: 1.53x faster                                                    |
| async_tree_io_tg           | 677 ms                                                          | 452 ms: 1.50x faster                                                    |
| async_tree_io              | 693 ms                                                          | 463 ms: 1.50x faster                                                    |
| generators                 | 38.5 ms                                                         | 25.7 ms: 1.50x faster                                                   |
| spectral_norm              | 104 ms                                                          | 72.0 ms: 1.44x faster                                                   |
| nbody                      | 127 ms                                                          | 90.0 ms: 1.41x faster                                                   |
| async_tree_memoization_tg  | 350 ms                                                          | 249 ms: 1.41x faster                                                    |
| async_tree_none_tg         | 278 ms                                                          | 197 ms: 1.41x faster                                                    |
| go                         | 137 ms                                                          | 98.5 ms: 1.39x faster                                                   |
| async_tree_none            | 298 ms                                                          | 216 ms: 1.37x faster                                                    |
| async_tree_memoization     | 364 ms                                                          | 267 ms: 1.36x faster                                                    |
| float                      | 76.7 ms                                                         | 56.5 ms: 1.36x faster                                                   |
| logging_silent             | 101 ns                                                          | 74.6 ns: 1.35x faster                                                   |
| deltablue                  | 3.58 ms                                                         | 2.70 ms: 1.33x faster                                                   |
| comprehensions             | 19.2 us                                                         | 14.6 us: 1.32x faster                                                   |
| hexiom                     | 6.82 ms                                                         | 5.21 ms: 1.31x faster                                                   |
| scimark_sor                | 130 ms                                                          | 99.7 ms: 1.30x faster                                                   |
| mako                       | 9.96 ms                                                         | 7.69 ms: 1.29x faster                                                   |
| regex_effbot               | 2.04 ms                                                         | 1.58 ms: 1.29x faster                                                   |
| tomli_loads                | 2.20 sec                                                        | 1.71 sec: 1.28x faster                                                  |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 3.06 ms: 1.26x faster                                                   |
| deepcopy_reduce            | 3.23 us                                                         | 2.57 us: 1.26x faster                                                   |
| pyflate                    | 424 ms                                                          | 340 ms: 1.25x faster                                                    |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 440 ms: 1.24x faster                                                    |
| scimark_lu                 | 93.2 ms                                                         | 75.2 ms: 1.24x faster                                                   |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 456 ms: 1.24x faster                                                    |
| scimark_monte_carlo        | 66.4 ms                                                         | 54.1 ms: 1.23x faster                                                   |
| chaos                      | 69.4 ms                                                         | 56.6 ms: 1.23x faster                                                   |
| coroutines                 | 20.9 ms                                                         | 17.3 ms: 1.21x faster                                                   |
| regex_compile              | 129 ms                                                          | 107 ms: 1.21x faster                                                    |
| nqueens                    | 93.7 ms                                                         | 78.6 ms: 1.19x faster                                                   |
| scimark_fft                | 271 ms                                                          | 228 ms: 1.19x faster                                                    |
| logging_simple             | 9.75 us                                                         | 8.23 us: 1.18x faster                                                   |
| fannkuch                   | 354 ms                                                          | 300 ms: 1.18x faster                                                    |
| logging_format             | 10.4 us                                                         | 8.85 us: 1.18x faster                                                   |
| xml_etree_iterparse        | 77.6 ms                                                         | 66.8 ms: 1.16x faster                                                   |
| sqlglot_transpile          | 1.53 ms                                                         | 1.33 ms: 1.15x faster                                                   |
| sqlglot_parse              | 1.25 ms                                                         | 1.08 ms: 1.15x faster                                                   |
| unpickle_pure_python       | 210 us                                                          | 185 us: 1.13x faster                                                    |
| pycparser                  | 978 ms                                                          | 867 ms: 1.13x faster                                                    |
| mdp                        | 1.91 sec                                                        | 1.71 sec: 1.12x faster                                                  |
| sqlglot_optimize           | 48.5 ms                                                         | 43.5 ms: 1.11x faster                                                   |
| dulwich_log                | 58.5 ms                                                         | 52.6 ms: 1.11x faster                                                   |
| pprint_safe_repr           | 721 ms                                                          | 650 ms: 1.11x faster                                                    |
| django_template            | 36.9 ms                                                         | 33.4 ms: 1.11x faster                                                   |
| sympy_integrate            | 17.5 ms                                                         | 15.9 ms: 1.10x faster                                                   |
| sympy_sum                  | 123 ms                                                          | 112 ms: 1.10x faster                                                    |
| pprint_pformat             | 1.50 sec                                                        | 1.36 sec: 1.10x faster                                                  |
| raytrace                   | 308 ms                                                          | 280 ms: 1.10x faster                                                    |
| crypto_pyaes               | 69.2 ms                                                         | 63.0 ms: 1.10x faster                                                   |
| 2to3                       | 280 ms                                                          | 256 ms: 1.09x faster                                                    |
| richards                   | 41.3 ms                                                         | 38.0 ms: 1.09x faster                                                   |
| regex_dna                  | 127 ms                                                          | 117 ms: 1.09x faster                                                    |
| sqlite_synth               | 2.07 us                                                         | 1.94 us: 1.07x faster                                                   |
| sympy_str                  | 240 ms                                                          | 224 ms: 1.07x faster                                                    |
| docutils                   | 1.98 sec                                                        | 1.86 sec: 1.07x faster                                                  |
| richards_super             | 46.5 ms                                                         | 43.6 ms: 1.06x faster                                                   |
| meteor_contest             | 86.9 ms                                                         | 81.7 ms: 1.06x faster                                                   |
| xml_etree_generate         | 72.1 ms                                                         | 67.9 ms: 1.06x faster                                                   |
| bench_thread_pool          | 1.10 ms                                                         | 1.04 ms: 1.06x faster                                                   |
| xml_etree_process          | 53.2 ms                                                         | 50.9 ms: 1.05x faster                                                   |
| async_generators           | 313 ms                                                          | 300 ms: 1.04x faster                                                    |
| pathlib                    | 91.4 ms                                                         | 87.8 ms: 1.04x faster                                                   |
| xml_etree_parse            | 113 ms                                                          | 109 ms: 1.04x faster                                                    |
| pidigits                   | 199 ms                                                          | 202 ms: 1.01x slower                                                    |
| regex_v8                   | 15.0 ms                                                         | 15.5 ms: 1.03x slower                                                   |
| json_loads                 | 20.4 us                                                         | 21.4 us: 1.05x slower                                                   |
| python_startup_no_site     | 19.1 ms                                                         | 20.1 ms: 1.05x slower                                                   |
| json                       | 4.15 ms                                                         | 4.65 ms: 1.12x slower                                                   |
| coverage                   | 48.4 ms                                                         | 54.4 ms: 1.12x slower                                                   |
| python_startup             | 22.4 ms                                                         | 27.0 ms: 1.21x slower                                                   |
| gc_traversal               | 1.44 ms                                                         | 1.78 ms: 1.24x slower                                                   |
| typing_runtime_protocols   | 126 us                                                          | 157 us: 1.24x slower                                                    |
| telco                      | 5.51 ms                                                         | 6.84 ms: 1.24x slower                                                   |
| bench_mp_pool              | 75.4 ms                                                         | 94.7 ms: 1.26x slower                                                   |
| json_dumps                 | 7.40 ms                                                         | 9.40 ms: 1.27x slower                                                   |
| create_gc_cycles           | 652 us                                                          | 1.06 ms: 1.63x slower                                                   |
| sqlglot_normalize          | 100 ms                                                          | 225 ms: 2.25x slower                                                    |
| Geometric mean             | (ref)                                                           | 1.13x faster                                                            |

Benchmark hidden because not significant (2): sympy_expand, pickle_pure_python
Ignored benchmarks (15) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20250121-3.14.0a4+-4844db8/bm-20250121-pythonperf1_win32-x86-mdboom-aa_test_2025-3.14.0a4+-4844db8.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.128x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.11x
- 95% likely to have a speedup of 1.10x
- 99% likely to have a speedup of 1.10x

# Memory
- memory change: unknown