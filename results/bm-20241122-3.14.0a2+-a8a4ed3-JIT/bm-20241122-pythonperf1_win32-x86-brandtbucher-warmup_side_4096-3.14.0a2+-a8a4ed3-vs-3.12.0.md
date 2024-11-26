# Results vs. 3.12.0

- fork: brandtbucher
- ref: warmup_side_4096
- machine: windows-x86
- commit hash: a8a4ed3
- commit date: 2024-11-22
- overall geometric mean: 1.062x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.02x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241122-pythonperf1_win32-x86-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 260 ms: 1.08x faster                                                              |
| docutils       | 1.98 sec                                                        | 1.95 sec: 1.02x faster                                                            |
| Geometric mean | (ref)                                                           | 1.05x faster                                                                      |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241122-pythonperf1_win32-x86-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|----------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 350 ms                                                          | 264 ms: 1.33x faster                                                              |
| async_tree_none_tg         | 278 ms                                                          | 215 ms: 1.29x faster                                                              |
| async_tree_io_tg           | 677 ms                                                          | 542 ms: 1.25x faster                                                              |
| async_tree_none            | 298 ms                                                          | 240 ms: 1.24x faster                                                              |
| async_tree_io              | 693 ms                                                          | 567 ms: 1.22x faster                                                              |
| async_tree_memoization     | 364 ms                                                          | 301 ms: 1.21x faster                                                              |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 474 ms: 1.15x faster                                                              |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 500 ms: 1.13x faster                                                              |
| Geometric mean             | (ref)                                                           | 1.23x faster                                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241122-pythonperf1_win32-x86-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| float          | 76.7 ms                                                         | 56.3 ms: 1.36x faster                                                             |
| nbody          | 127 ms                                                          | 94.9 ms: 1.34x faster                                                             |
| pidigits       | 199 ms                                                          | 203 ms: 1.02x slower                                                              |
| Geometric mean | (ref)                                                           | 1.21x faster                                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241122-pythonperf1_win32-x86-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_effbot   | 2.04 ms                                                         | 1.55 ms: 1.31x faster                                                             |
| regex_compile  | 129 ms                                                          | 113 ms: 1.14x faster                                                              |
| regex_dna      | 127 ms                                                          | 113 ms: 1.13x faster                                                              |
| regex_v8       | 15.0 ms                                                         | 15.6 ms: 1.03x slower                                                             |
| Geometric mean | (ref)                                                           | 1.13x faster                                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241122-pythonperf1_win32-x86-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|----------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| tomli_loads          | 2.20 sec                                                        | 1.84 sec: 1.19x faster                                                            |
| xml_etree_iterparse  | 77.6 ms                                                         | 68.3 ms: 1.14x faster                                                             |
| unpickle_pure_python | 210 us                                                          | 207 us: 1.01x faster                                                              |
| xml_etree_generate   | 72.1 ms                                                         | 72.7 ms: 1.01x slower                                                             |
| xml_etree_process    | 53.2 ms                                                         | 53.7 ms: 1.01x slower                                                             |
| pickle_pure_python   | 286 us                                                          | 296 us: 1.04x slower                                                              |
| json_loads           | 20.4 us                                                         | 21.3 us: 1.04x slower                                                             |
| json_dumps           | 7.40 ms                                                         | 9.01 ms: 1.22x slower                                                             |
| Geometric mean       | (ref)                                                           | 1.00x faster                                                                      |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241122-pythonperf1_win32-x86-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 19.5 ms: 1.02x slower                                                             |
| python_startup         | 22.4 ms                                                         | 25.7 ms: 1.15x slower                                                             |
| Geometric mean         | (ref)                                                           | 1.09x slower                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241122-pythonperf1_win32-x86-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| mako           | 9.96 ms                                                         | 7.39 ms: 1.35x faster                                                             |
| Geometric mean | (ref)                                                           | 1.16x faster                                                                      |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241122-pythonperf1_win32-x86-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|----------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| deepcopy_memo              | 38.4 us                                                         | 24.0 us: 1.60x faster                                                             |
| float                      | 76.7 ms                                                         | 56.3 ms: 1.36x faster                                                             |
| mako                       | 9.96 ms                                                         | 7.39 ms: 1.35x faster                                                             |
| nbody                      | 127 ms                                                          | 94.9 ms: 1.34x faster                                                             |
| async_tree_memoization_tg  | 350 ms                                                          | 264 ms: 1.33x faster                                                              |
| regex_effbot               | 2.04 ms                                                         | 1.55 ms: 1.31x faster                                                             |
| deepcopy                   | 360 us                                                          | 278 us: 1.29x faster                                                              |
| async_tree_none_tg         | 278 ms                                                          | 215 ms: 1.29x faster                                                              |
| coroutines                 | 20.9 ms                                                         | 16.5 ms: 1.26x faster                                                             |
| scimark_lu                 | 93.2 ms                                                         | 74.0 ms: 1.26x faster                                                             |
| async_tree_io_tg           | 677 ms                                                          | 542 ms: 1.25x faster                                                              |
| spectral_norm              | 104 ms                                                          | 83.5 ms: 1.24x faster                                                             |
| async_tree_none            | 298 ms                                                          | 240 ms: 1.24x faster                                                              |
| async_tree_io              | 693 ms                                                          | 567 ms: 1.22x faster                                                              |
| scimark_sor                | 130 ms                                                          | 106 ms: 1.22x faster                                                              |
| async_tree_memoization     | 364 ms                                                          | 301 ms: 1.21x faster                                                              |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 3.21 ms: 1.20x faster                                                             |
| tomli_loads                | 2.20 sec                                                        | 1.84 sec: 1.19x faster                                                            |
| dulwich_log                | 58.5 ms                                                         | 49.8 ms: 1.17x faster                                                             |
| logging_simple             | 9.75 us                                                         | 8.40 us: 1.16x faster                                                             |
| logging_format             | 10.4 us                                                         | 9.01 us: 1.15x faster                                                             |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 474 ms: 1.15x faster                                                              |
| logging_silent             | 101 ns                                                          | 87.9 ns: 1.15x faster                                                             |
| regex_compile              | 129 ms                                                          | 113 ms: 1.14x faster                                                              |
| go                         | 137 ms                                                          | 121 ms: 1.14x faster                                                              |
| xml_etree_iterparse        | 77.6 ms                                                         | 68.3 ms: 1.14x faster                                                             |
| regex_dna                  | 127 ms                                                          | 113 ms: 1.13x faster                                                              |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 500 ms: 1.13x faster                                                              |
| deepcopy_reduce            | 3.23 us                                                         | 2.86 us: 1.13x faster                                                             |
| deltablue                  | 3.58 ms                                                         | 3.21 ms: 1.12x faster                                                             |
| pathlib                    | 91.4 ms                                                         | 83.4 ms: 1.10x faster                                                             |
| sqlglot_parse              | 1.25 ms                                                         | 1.15 ms: 1.09x faster                                                             |
| scimark_fft                | 271 ms                                                          | 250 ms: 1.08x faster                                                              |
| sqlglot_transpile          | 1.53 ms                                                         | 1.42 ms: 1.08x faster                                                             |
| 2to3                       | 280 ms                                                          | 260 ms: 1.08x faster                                                              |
| fannkuch                   | 354 ms                                                          | 330 ms: 1.07x faster                                                              |
| sqlite_synth               | 2.07 us                                                         | 1.94 us: 1.07x faster                                                             |
| bench_thread_pool          | 1.10 ms                                                         | 1.03 ms: 1.07x faster                                                             |
| sympy_sum                  | 123 ms                                                          | 115 ms: 1.06x faster                                                              |
| chaos                      | 69.4 ms                                                         | 65.7 ms: 1.06x faster                                                             |
| pycparser                  | 978 ms                                                          | 931 ms: 1.05x faster                                                              |
| generators                 | 38.5 ms                                                         | 36.7 ms: 1.05x faster                                                             |
| comprehensions             | 19.2 us                                                         | 18.4 us: 1.04x faster                                                             |
| pyflate                    | 424 ms                                                          | 408 ms: 1.04x faster                                                              |
| crypto_pyaes               | 69.2 ms                                                         | 66.7 ms: 1.04x faster                                                             |
| scimark_monte_carlo        | 66.4 ms                                                         | 64.1 ms: 1.04x faster                                                             |
| mdp                        | 1.91 sec                                                        | 1.85 sec: 1.03x faster                                                            |
| sympy_str                  | 240 ms                                                          | 233 ms: 1.03x faster                                                              |
| docutils                   | 1.98 sec                                                        | 1.95 sec: 1.02x faster                                                            |
| raytrace                   | 308 ms                                                          | 303 ms: 1.02x faster                                                              |
| unpickle_pure_python       | 210 us                                                          | 207 us: 1.01x faster                                                              |
| pprint_pformat             | 1.50 sec                                                        | 1.51 sec: 1.00x slower                                                            |
| richards                   | 41.3 ms                                                         | 41.6 ms: 1.01x slower                                                             |
| xml_etree_generate         | 72.1 ms                                                         | 72.7 ms: 1.01x slower                                                             |
| xml_etree_process          | 53.2 ms                                                         | 53.7 ms: 1.01x slower                                                             |
| sympy_expand               | 398 ms                                                          | 403 ms: 1.01x slower                                                              |
| pprint_safe_repr           | 721 ms                                                          | 731 ms: 1.01x slower                                                              |
| pidigits                   | 199 ms                                                          | 203 ms: 1.02x slower                                                              |
| meteor_contest             | 86.9 ms                                                         | 88.3 ms: 1.02x slower                                                             |
| async_generators           | 313 ms                                                          | 319 ms: 1.02x slower                                                              |
| richards_super             | 46.5 ms                                                         | 47.4 ms: 1.02x slower                                                             |
| python_startup_no_site     | 19.1 ms                                                         | 19.5 ms: 1.02x slower                                                             |
| hexiom                     | 6.82 ms                                                         | 7.00 ms: 1.03x slower                                                             |
| regex_v8                   | 15.0 ms                                                         | 15.6 ms: 1.03x slower                                                             |
| pickle_pure_python         | 286 us                                                          | 296 us: 1.04x slower                                                              |
| json_loads                 | 20.4 us                                                         | 21.3 us: 1.04x slower                                                             |
| sqlglot_optimize           | 48.5 ms                                                         | 50.8 ms: 1.05x slower                                                             |
| nqueens                    | 93.7 ms                                                         | 98.9 ms: 1.06x slower                                                             |
| sqlglot_normalize          | 100 ms                                                          | 108 ms: 1.08x slower                                                              |
| json                       | 4.15 ms                                                         | 4.63 ms: 1.11x slower                                                             |
| coverage                   | 48.4 ms                                                         | 55.0 ms: 1.14x slower                                                             |
| python_startup             | 22.4 ms                                                         | 25.7 ms: 1.15x slower                                                             |
| bench_mp_pool              | 75.4 ms                                                         | 87.2 ms: 1.16x slower                                                             |
| gc_traversal               | 1.44 ms                                                         | 1.70 ms: 1.18x slower                                                             |
| json_dumps                 | 7.40 ms                                                         | 9.01 ms: 1.22x slower                                                             |
| telco                      | 5.51 ms                                                         | 7.17 ms: 1.30x slower                                                             |
| typing_runtime_protocols   | 126 us                                                          | 169 us: 1.33x slower                                                              |
| create_gc_cycles           | 652 us                                                          | 1.15 ms: 1.76x slower                                                             |
| Geometric mean             | (ref)                                                           | 1.06x faster                                                                      |

Benchmark hidden because not significant (3): xml_etree_parse, sympy_integrate, django_template
Ignored benchmarks (15) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20241122-3.14.0a2+-a8a4ed3-JIT/bm-20241122-pythonperf1_win32-x86-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.062x faster
# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: unknown