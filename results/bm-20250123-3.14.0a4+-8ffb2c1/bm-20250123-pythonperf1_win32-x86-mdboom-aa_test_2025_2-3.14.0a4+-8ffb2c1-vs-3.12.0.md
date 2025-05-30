# Results vs. 3.12.0

- fork: mdboom
- ref: aa_test_2025_2
- machine: windows-x86
- commit hash: 8ffb2c1
- commit date: 2025-01-23
- overall geometric mean: 1.124x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.09x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250123-pythonperf1_win32-x86-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 254 ms: 1.10x faster                                                      |
| docutils       | 1.98 sec                                                        | 1.86 sec: 1.07x faster                                                    |
| Geometric mean | (ref)                                                           | 1.09x faster                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250123-pythonperf1_win32-x86-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_io              | 693 ms                                                          | 462 ms: 1.50x faster                                                      |
| async_tree_io_tg           | 677 ms                                                          | 451 ms: 1.50x faster                                                      |
| async_tree_memoization_tg  | 350 ms                                                          | 245 ms: 1.43x faster                                                      |
| async_tree_none_tg         | 278 ms                                                          | 194 ms: 1.43x faster                                                      |
| async_tree_none            | 298 ms                                                          | 212 ms: 1.40x faster                                                      |
| async_tree_memoization     | 364 ms                                                          | 261 ms: 1.40x faster                                                      |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 455 ms: 1.24x faster                                                      |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 444 ms: 1.23x faster                                                      |
| Geometric mean             | (ref)                                                           | 1.39x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250123-pythonperf1_win32-x86-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 87.3 ms: 1.45x faster                                                     |
| float          | 76.7 ms                                                         | 57.8 ms: 1.33x faster                                                     |
| pidigits       | 199 ms                                                          | 202 ms: 1.01x slower                                                      |
| Geometric mean | (ref)                                                           | 1.24x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250123-pythonperf1_win32-x86-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_effbot   | 2.04 ms                                                         | 1.59 ms: 1.28x faster                                                     |
| regex_compile  | 129 ms                                                          | 107 ms: 1.21x faster                                                      |
| regex_dna      | 127 ms                                                          | 123 ms: 1.03x faster                                                      |
| regex_v8       | 15.0 ms                                                         | 16.6 ms: 1.10x slower                                                     |
| Geometric mean | (ref)                                                           | 1.10x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250123-pythonperf1_win32-x86-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| tomli_loads          | 2.20 sec                                                        | 1.66 sec: 1.33x faster                                                    |
| xml_etree_iterparse  | 77.6 ms                                                         | 67.4 ms: 1.15x faster                                                     |
| unpickle_pure_python | 210 us                                                          | 186 us: 1.13x faster                                                      |
| xml_etree_parse      | 113 ms                                                          | 108 ms: 1.04x faster                                                      |
| xml_etree_generate   | 72.1 ms                                                         | 69.3 ms: 1.04x faster                                                     |
| xml_etree_process    | 53.2 ms                                                         | 52.4 ms: 1.02x faster                                                     |
| json_loads           | 20.4 us                                                         | 21.3 us: 1.04x slower                                                     |
| json_dumps           | 7.40 ms                                                         | 9.41 ms: 1.27x slower                                                     |
| Geometric mean       | (ref)                                                           | 1.04x faster                                                              |

Benchmark hidden because not significant (1): pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250123-pythonperf1_win32-x86-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 20.0 ms: 1.05x slower                                                     |
| python_startup         | 22.4 ms                                                         | 26.8 ms: 1.20x slower                                                     |
| Geometric mean         | (ref)                                                           | 1.12x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250123-pythonperf1_win32-x86-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 7.81 ms: 1.27x faster                                                     |
| django_template | 36.9 ms                                                         | 34.2 ms: 1.08x faster                                                     |
| Geometric mean  | (ref)                                                           | 1.17x faster                                                              |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250123-pythonperf1_win32-x86-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| deepcopy_memo              | 38.4 us                                                         | 21.6 us: 1.78x faster                                                     |
| async_tree_io              | 693 ms                                                          | 462 ms: 1.50x faster                                                      |
| async_tree_io_tg           | 677 ms                                                          | 451 ms: 1.50x faster                                                      |
| generators                 | 38.5 ms                                                         | 26.0 ms: 1.48x faster                                                     |
| deepcopy                   | 360 us                                                          | 245 us: 1.47x faster                                                      |
| nbody                      | 127 ms                                                          | 87.3 ms: 1.45x faster                                                     |
| spectral_norm              | 104 ms                                                          | 72.5 ms: 1.43x faster                                                     |
| async_tree_memoization_tg  | 350 ms                                                          | 245 ms: 1.43x faster                                                      |
| async_tree_none_tg         | 278 ms                                                          | 194 ms: 1.43x faster                                                      |
| async_tree_none            | 298 ms                                                          | 212 ms: 1.40x faster                                                      |
| async_tree_memoization     | 364 ms                                                          | 261 ms: 1.40x faster                                                      |
| go                         | 137 ms                                                          | 101 ms: 1.36x faster                                                      |
| logging_silent             | 101 ns                                                          | 74.5 ns: 1.36x faster                                                     |
| comprehensions             | 19.2 us                                                         | 14.4 us: 1.33x faster                                                     |
| float                      | 76.7 ms                                                         | 57.8 ms: 1.33x faster                                                     |
| tomli_loads                | 2.20 sec                                                        | 1.66 sec: 1.33x faster                                                    |
| deltablue                  | 3.58 ms                                                         | 2.71 ms: 1.32x faster                                                     |
| hexiom                     | 6.82 ms                                                         | 5.25 ms: 1.30x faster                                                     |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 3.01 ms: 1.28x faster                                                     |
| regex_effbot               | 2.04 ms                                                         | 1.59 ms: 1.28x faster                                                     |
| mako                       | 9.96 ms                                                         | 7.81 ms: 1.27x faster                                                     |
| scimark_sor                | 130 ms                                                          | 103 ms: 1.26x faster                                                      |
| deepcopy_reduce            | 3.23 us                                                         | 2.57 us: 1.25x faster                                                     |
| scimark_lu                 | 93.2 ms                                                         | 74.9 ms: 1.25x faster                                                     |
| pyflate                    | 424 ms                                                          | 341 ms: 1.24x faster                                                      |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 455 ms: 1.24x faster                                                      |
| coroutines                 | 20.9 ms                                                         | 16.9 ms: 1.24x faster                                                     |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 444 ms: 1.23x faster                                                      |
| regex_compile              | 129 ms                                                          | 107 ms: 1.21x faster                                                      |
| scimark_monte_carlo        | 66.4 ms                                                         | 55.3 ms: 1.20x faster                                                     |
| scimark_fft                | 271 ms                                                          | 228 ms: 1.19x faster                                                      |
| fannkuch                   | 354 ms                                                          | 299 ms: 1.18x faster                                                      |
| nqueens                    | 93.7 ms                                                         | 79.4 ms: 1.18x faster                                                     |
| chaos                      | 69.4 ms                                                         | 59.3 ms: 1.17x faster                                                     |
| sqlglot_parse              | 1.25 ms                                                         | 1.07 ms: 1.16x faster                                                     |
| sqlglot_transpile          | 1.53 ms                                                         | 1.32 ms: 1.16x faster                                                     |
| logging_simple             | 9.75 us                                                         | 8.42 us: 1.16x faster                                                     |
| xml_etree_iterparse        | 77.6 ms                                                         | 67.4 ms: 1.15x faster                                                     |
| logging_format             | 10.4 us                                                         | 9.05 us: 1.15x faster                                                     |
| unpickle_pure_python       | 210 us                                                          | 186 us: 1.13x faster                                                      |
| pycparser                  | 978 ms                                                          | 869 ms: 1.12x faster                                                      |
| dulwich_log                | 58.5 ms                                                         | 52.3 ms: 1.12x faster                                                     |
| sympy_sum                  | 123 ms                                                          | 110 ms: 1.12x faster                                                      |
| pprint_pformat             | 1.50 sec                                                        | 1.35 sec: 1.11x faster                                                    |
| mdp                        | 1.91 sec                                                        | 1.72 sec: 1.11x faster                                                    |
| crypto_pyaes               | 69.2 ms                                                         | 62.4 ms: 1.11x faster                                                     |
| pprint_safe_repr           | 721 ms                                                          | 650 ms: 1.11x faster                                                      |
| 2to3                       | 280 ms                                                          | 254 ms: 1.10x faster                                                      |
| sympy_integrate            | 17.5 ms                                                         | 16.0 ms: 1.10x faster                                                     |
| sqlglot_optimize           | 48.5 ms                                                         | 44.5 ms: 1.09x faster                                                     |
| django_template            | 36.9 ms                                                         | 34.2 ms: 1.08x faster                                                     |
| sympy_str                  | 240 ms                                                          | 222 ms: 1.08x faster                                                      |
| bench_thread_pool          | 1.10 ms                                                         | 1.02 ms: 1.08x faster                                                     |
| sqlite_synth               | 2.07 us                                                         | 1.94 us: 1.07x faster                                                     |
| richards                   | 41.3 ms                                                         | 38.7 ms: 1.07x faster                                                     |
| richards_super             | 46.5 ms                                                         | 43.5 ms: 1.07x faster                                                     |
| docutils                   | 1.98 sec                                                        | 1.86 sec: 1.07x faster                                                    |
| pathlib                    | 91.4 ms                                                         | 86.1 ms: 1.06x faster                                                     |
| meteor_contest             | 86.9 ms                                                         | 82.3 ms: 1.06x faster                                                     |
| raytrace                   | 308 ms                                                          | 293 ms: 1.05x faster                                                      |
| xml_etree_parse            | 113 ms                                                          | 108 ms: 1.04x faster                                                      |
| xml_etree_generate         | 72.1 ms                                                         | 69.3 ms: 1.04x faster                                                     |
| async_generators           | 313 ms                                                          | 303 ms: 1.03x faster                                                      |
| regex_dna                  | 127 ms                                                          | 123 ms: 1.03x faster                                                      |
| xml_etree_process          | 53.2 ms                                                         | 52.4 ms: 1.02x faster                                                     |
| sympy_expand               | 398 ms                                                          | 392 ms: 1.01x faster                                                      |
| pidigits                   | 199 ms                                                          | 202 ms: 1.01x slower                                                      |
| json_loads                 | 20.4 us                                                         | 21.3 us: 1.04x slower                                                     |
| python_startup_no_site     | 19.1 ms                                                         | 20.0 ms: 1.05x slower                                                     |
| json                       | 4.15 ms                                                         | 4.50 ms: 1.08x slower                                                     |
| regex_v8                   | 15.0 ms                                                         | 16.6 ms: 1.10x slower                                                     |
| coverage                   | 48.4 ms                                                         | 53.8 ms: 1.11x slower                                                     |
| python_startup             | 22.4 ms                                                         | 26.8 ms: 1.20x slower                                                     |
| gc_traversal               | 1.44 ms                                                         | 1.79 ms: 1.24x slower                                                     |
| bench_mp_pool              | 75.4 ms                                                         | 94.8 ms: 1.26x slower                                                     |
| typing_runtime_protocols   | 126 us                                                          | 159 us: 1.26x slower                                                      |
| json_dumps                 | 7.40 ms                                                         | 9.41 ms: 1.27x slower                                                     |
| telco                      | 5.51 ms                                                         | 7.09 ms: 1.29x slower                                                     |
| create_gc_cycles           | 652 us                                                          | 1.05 ms: 1.61x slower                                                     |
| sqlglot_normalize          | 100 ms                                                          | 233 ms: 2.32x slower                                                      |
| Geometric mean             | (ref)                                                           | 1.12x faster                                                              |

Benchmark hidden because not significant (1): pickle_pure_python
Ignored benchmarks (15) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20250123-3.14.0a4+-8ffb2c1/bm-20250123-pythonperf1_win32-x86-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.124x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.11x
- 95% likely to have a speedup of 1.10x
- 99% likely to have a speedup of 1.09x

# Memory
- memory change: unknown