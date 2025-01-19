# Results vs. 3.12.0

- fork: python
- ref: 61b35f74aa4a6ac60663
- machine: windows-x86
- commit hash: 61b35f7
- commit date: 2025-01-18
- overall geometric mean: 1.008x faster
- HPT reliability: 75.59%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250118-pythonperf1_win32-x86-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 291 ms: 1.04x slower                                                            |
| docutils       | 1.98 sec                                                        | 2.15 sec: 1.08x slower                                                          |
| Geometric mean | (ref)                                                           | 1.06x slower                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250118-pythonperf1_win32-x86-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_io_tg           | 677 ms                                                          | 480 ms: 1.41x faster                                                            |
| async_tree_io              | 693 ms                                                          | 508 ms: 1.36x faster                                                            |
| async_tree_memoization_tg  | 350 ms                                                          | 261 ms: 1.34x faster                                                            |
| async_tree_none_tg         | 278 ms                                                          | 208 ms: 1.34x faster                                                            |
| async_tree_none            | 298 ms                                                          | 238 ms: 1.25x faster                                                            |
| async_tree_memoization     | 364 ms                                                          | 291 ms: 1.25x faster                                                            |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 461 ms: 1.19x faster                                                            |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 490 ms: 1.15x faster                                                            |
| Geometric mean             | (ref)                                                           | 1.28x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250118-pythonperf1_win32-x86-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 76.7 ms                                                         | 56.8 ms: 1.35x faster                                                           |
| nbody          | 127 ms                                                          | 112 ms: 1.13x faster                                                            |
| pidigits       | 199 ms                                                          | 200 ms: 1.01x slower                                                            |
| Geometric mean | (ref)                                                           | 1.15x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250118-pythonperf1_win32-x86-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_effbot   | 2.04 ms                                                         | 1.56 ms: 1.31x faster                                                           |
| regex_dna      | 127 ms                                                          | 115 ms: 1.10x faster                                                            |
| regex_compile  | 129 ms                                                          | 132 ms: 1.02x slower                                                            |
| regex_v8       | 15.0 ms                                                         | 16.4 ms: 1.09x slower                                                           |
| Geometric mean | (ref)                                                           | 1.07x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250118-pythonperf1_win32-x86-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7 |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 2.20 sec                                                        | 1.89 sec: 1.16x faster                                                          |
| xml_etree_iterparse  | 77.6 ms                                                         | 69.7 ms: 1.11x faster                                                           |
| xml_etree_parse      | 113 ms                                                          | 110 ms: 1.03x faster                                                            |
| unpickle_list        | 2.95 us                                                         | 2.98 us: 1.01x slower                                                           |
| unpickle_pure_python | 210 us                                                          | 213 us: 1.01x slower                                                            |
| pickle_dict          | 19.9 us                                                         | 20.8 us: 1.04x slower                                                           |
| xml_etree_process    | 53.2 ms                                                         | 56.6 ms: 1.06x slower                                                           |
| xml_etree_generate   | 72.1 ms                                                         | 77.0 ms: 1.07x slower                                                           |
| pickle_list          | 3.37 us                                                         | 3.72 us: 1.10x slower                                                           |
| unpickle             | 9.71 us                                                         | 10.9 us: 1.12x slower                                                           |
| json_loads           | 20.4 us                                                         | 23.0 us: 1.13x slower                                                           |
| pickle_pure_python   | 286 us                                                          | 335 us: 1.17x slower                                                            |
| pickle               | 7.79 us                                                         | 9.42 us: 1.21x slower                                                           |
| json_dumps           | 7.40 ms                                                         | 9.55 ms: 1.29x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.06x slower                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250118-pythonperf1_win32-x86-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7 |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 20.4 ms: 1.07x slower                                                           |
| python_startup         | 22.4 ms                                                         | 27.2 ms: 1.22x slower                                                           |
| Geometric mean         | (ref)                                                           | 1.14x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250118-pythonperf1_win32-x86-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7 |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 7.39 ms: 1.35x faster                                                           |
| django_template | 36.9 ms                                                         | 40.2 ms: 1.09x slower                                                           |
| Geometric mean  | (ref)                                                           | 1.11x faster                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250118-pythonperf1_win32-x86-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| deepcopy_memo              | 38.4 us                                                         | 25.5 us: 1.50x faster                                                           |
| async_tree_io_tg           | 677 ms                                                          | 480 ms: 1.41x faster                                                            |
| async_tree_io              | 693 ms                                                          | 508 ms: 1.36x faster                                                            |
| float                      | 76.7 ms                                                         | 56.8 ms: 1.35x faster                                                           |
| mako                       | 9.96 ms                                                         | 7.39 ms: 1.35x faster                                                           |
| async_tree_memoization_tg  | 350 ms                                                          | 261 ms: 1.34x faster                                                            |
| async_tree_none_tg         | 278 ms                                                          | 208 ms: 1.34x faster                                                            |
| spectral_norm              | 104 ms                                                          | 78.3 ms: 1.33x faster                                                           |
| regex_effbot               | 2.04 ms                                                         | 1.56 ms: 1.31x faster                                                           |
| async_tree_none            | 298 ms                                                          | 238 ms: 1.25x faster                                                            |
| async_tree_memoization     | 364 ms                                                          | 291 ms: 1.25x faster                                                            |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 3.13 ms: 1.23x faster                                                           |
| deepcopy                   | 360 us                                                          | 299 us: 1.20x faster                                                            |
| scimark_sor                | 130 ms                                                          | 109 ms: 1.19x faster                                                            |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 461 ms: 1.19x faster                                                            |
| tomli_loads                | 2.20 sec                                                        | 1.89 sec: 1.16x faster                                                          |
| scimark_lu                 | 93.2 ms                                                         | 80.7 ms: 1.15x faster                                                           |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 490 ms: 1.15x faster                                                            |
| logging_silent             | 101 ns                                                          | 88.0 ns: 1.15x faster                                                           |
| nbody                      | 127 ms                                                          | 112 ms: 1.13x faster                                                            |
| xml_etree_iterparse        | 77.6 ms                                                         | 69.7 ms: 1.11x faster                                                           |
| regex_dna                  | 127 ms                                                          | 115 ms: 1.10x faster                                                            |
| scimark_fft                | 271 ms                                                          | 247 ms: 1.10x faster                                                            |
| unpack_sequence            | 62.5 ns                                                         | 57.5 ns: 1.09x faster                                                           |
| sqlite_synth               | 2.07 us                                                         | 1.92 us: 1.08x faster                                                           |
| pyflate                    | 424 ms                                                          | 399 ms: 1.06x faster                                                            |
| deepcopy_reduce            | 3.23 us                                                         | 3.05 us: 1.06x faster                                                           |
| pathlib                    | 91.4 ms                                                         | 86.5 ms: 1.06x faster                                                           |
| deltablue                  | 3.58 ms                                                         | 3.41 ms: 1.05x faster                                                           |
| asyncio_tcp_ssl            | 17.7 sec                                                        | 17.1 sec: 1.03x faster                                                          |
| xml_etree_parse            | 113 ms                                                          | 110 ms: 1.03x faster                                                            |
| dulwich_log                | 58.5 ms                                                         | 57.0 ms: 1.03x faster                                                           |
| comprehensions             | 19.2 us                                                         | 19.1 us: 1.00x faster                                                           |
| pidigits                   | 199 ms                                                          | 200 ms: 1.01x slower                                                            |
| scimark_monte_carlo        | 66.4 ms                                                         | 66.9 ms: 1.01x slower                                                           |
| chaos                      | 69.4 ms                                                         | 70.0 ms: 1.01x slower                                                           |
| go                         | 137 ms                                                          | 139 ms: 1.01x slower                                                            |
| unpickle_list              | 2.95 us                                                         | 2.98 us: 1.01x slower                                                           |
| crypto_pyaes               | 69.2 ms                                                         | 70.1 ms: 1.01x slower                                                           |
| unpickle_pure_python       | 210 us                                                          | 213 us: 1.01x slower                                                            |
| fannkuch                   | 354 ms                                                          | 359 ms: 1.01x slower                                                            |
| bench_thread_pool          | 1.10 ms                                                         | 1.12 ms: 1.02x slower                                                           |
| pprint_pformat             | 1.50 sec                                                        | 1.53 sec: 1.02x slower                                                          |
| sqlglot_parse              | 1.25 ms                                                         | 1.27 ms: 1.02x slower                                                           |
| regex_compile              | 129 ms                                                          | 132 ms: 1.02x slower                                                            |
| pycparser                  | 978 ms                                                          | 1.00 sec: 1.02x slower                                                          |
| sqlglot_transpile          | 1.53 ms                                                         | 1.58 ms: 1.03x slower                                                           |
| 2to3                       | 280 ms                                                          | 291 ms: 1.04x slower                                                            |
| mdp                        | 1.91 sec                                                        | 1.99 sec: 1.04x slower                                                          |
| pickle_dict                | 19.9 us                                                         | 20.8 us: 1.04x slower                                                           |
| coroutines                 | 20.9 ms                                                         | 21.8 ms: 1.04x slower                                                           |
| pprint_safe_repr           | 721 ms                                                          | 759 ms: 1.05x slower                                                            |
| meteor_contest             | 86.9 ms                                                         | 91.7 ms: 1.06x slower                                                           |
| xml_etree_process          | 53.2 ms                                                         | 56.6 ms: 1.06x slower                                                           |
| xml_etree_generate         | 72.1 ms                                                         | 77.0 ms: 1.07x slower                                                           |
| python_startup_no_site     | 19.1 ms                                                         | 20.4 ms: 1.07x slower                                                           |
| sympy_sum                  | 123 ms                                                          | 132 ms: 1.08x slower                                                            |
| docutils                   | 1.98 sec                                                        | 2.15 sec: 1.08x slower                                                          |
| regex_v8                   | 15.0 ms                                                         | 16.4 ms: 1.09x slower                                                           |
| django_template            | 36.9 ms                                                         | 40.2 ms: 1.09x slower                                                           |
| generators                 | 38.5 ms                                                         | 42.0 ms: 1.09x slower                                                           |
| raytrace                   | 308 ms                                                          | 337 ms: 1.09x slower                                                            |
| sympy_str                  | 240 ms                                                          | 263 ms: 1.10x slower                                                            |
| async_generators           | 313 ms                                                          | 345 ms: 1.10x slower                                                            |
| json                       | 4.15 ms                                                         | 4.58 ms: 1.10x slower                                                           |
| sympy_integrate            | 17.5 ms                                                         | 19.4 ms: 1.10x slower                                                           |
| pickle_list                | 3.37 us                                                         | 3.72 us: 1.10x slower                                                           |
| hexiom                     | 6.82 ms                                                         | 7.57 ms: 1.11x slower                                                           |
| coverage                   | 48.4 ms                                                         | 54.3 ms: 1.12x slower                                                           |
| unpickle                   | 9.71 us                                                         | 10.9 us: 1.12x slower                                                           |
| asyncio_tcp                | 662 ms                                                          | 747 ms: 1.13x slower                                                            |
| json_loads                 | 20.4 us                                                         | 23.0 us: 1.13x slower                                                           |
| nqueens                    | 93.7 ms                                                         | 106 ms: 1.14x slower                                                            |
| sympy_expand               | 398 ms                                                          | 452 ms: 1.14x slower                                                            |
| richards_super             | 46.5 ms                                                         | 52.9 ms: 1.14x slower                                                           |
| richards                   | 41.3 ms                                                         | 47.2 ms: 1.14x slower                                                           |
| sqlglot_optimize           | 48.5 ms                                                         | 55.6 ms: 1.15x slower                                                           |
| sqlglot_normalize          | 100 ms                                                          | 115 ms: 1.15x slower                                                            |
| pickle_pure_python         | 286 us                                                          | 335 us: 1.17x slower                                                            |
| pickle                     | 7.79 us                                                         | 9.42 us: 1.21x slower                                                           |
| python_startup             | 22.4 ms                                                         | 27.2 ms: 1.22x slower                                                           |
| gc_traversal               | 1.44 ms                                                         | 1.82 ms: 1.26x slower                                                           |
| json_dumps                 | 7.40 ms                                                         | 9.55 ms: 1.29x slower                                                           |
| bench_mp_pool              | 75.4 ms                                                         | 97.5 ms: 1.29x slower                                                           |
| telco                      | 5.51 ms                                                         | 7.57 ms: 1.37x slower                                                           |
| typing_runtime_protocols   | 126 us                                                          | 174 us: 1.38x slower                                                            |
| create_gc_cycles           | 652 us                                                          | 1.04 ms: 1.60x slower                                                           |
| Geometric mean             | (ref)                                                           | 1.00x faster                                                                    |

Benchmark hidden because not significant (2): logging_format, logging_simple
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (13) of results/bm-20250118-3.14.0a4+-61b35f7-JIT/bm-20250118-pythonperf1_win32-x86-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.008x faster

# HPT report

- Reliability score: 75.59% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown