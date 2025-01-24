# Results vs. 3.12.0

- fork: mdboom
- ref: test_without_pgo_wor
- machine: windows-x86
- commit hash: 71a13ea
- commit date: 2025-01-23
- overall geometric mean: 1.123x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.09x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250123-pythonperf1_win32-x86-mdboom-test_without_pgo_wor-3.14.0a4+-71a13ea |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 256 ms: 1.09x faster                                                            |
| docutils       | 1.98 sec                                                        | 1.85 sec: 1.07x faster                                                          |
| Geometric mean | (ref)                                                           | 1.08x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250123-pythonperf1_win32-x86-mdboom-test_without_pgo_wor-3.14.0a4+-71a13ea |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_io              | 693 ms                                                          | 459 ms: 1.51x faster                                                            |
| async_tree_io_tg           | 677 ms                                                          | 453 ms: 1.50x faster                                                            |
| async_tree_none_tg         | 278 ms                                                          | 192 ms: 1.44x faster                                                            |
| async_tree_memoization_tg  | 350 ms                                                          | 244 ms: 1.43x faster                                                            |
| async_tree_none            | 298 ms                                                          | 212 ms: 1.40x faster                                                            |
| async_tree_memoization     | 364 ms                                                          | 261 ms: 1.39x faster                                                            |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 461 ms: 1.22x faster                                                            |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 450 ms: 1.21x faster                                                            |
| Geometric mean             | (ref)                                                           | 1.39x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250123-pythonperf1_win32-x86-mdboom-test_without_pgo_wor-3.14.0a4+-71a13ea |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 89.4 ms: 1.42x faster                                                           |
| float          | 76.7 ms                                                         | 57.8 ms: 1.33x faster                                                           |
| Geometric mean | (ref)                                                           | 1.23x faster                                                                    |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250123-pythonperf1_win32-x86-mdboom-test_without_pgo_wor-3.14.0a4+-71a13ea |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_effbot   | 2.04 ms                                                         | 1.55 ms: 1.31x faster                                                           |
| regex_compile  | 129 ms                                                          | 106 ms: 1.22x faster                                                            |
| regex_dna      | 127 ms                                                          | 113 ms: 1.12x faster                                                            |
| regex_v8       | 15.0 ms                                                         | 16.2 ms: 1.08x slower                                                           |
| Geometric mean | (ref)                                                           | 1.14x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250123-pythonperf1_win32-x86-mdboom-test_without_pgo_wor-3.14.0a4+-71a13ea |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 2.20 sec                                                        | 1.69 sec: 1.30x faster                                                          |
| xml_etree_iterparse  | 77.6 ms                                                         | 66.9 ms: 1.16x faster                                                           |
| unpickle_pure_python | 210 us                                                          | 185 us: 1.14x faster                                                            |
| xml_etree_generate   | 72.1 ms                                                         | 67.1 ms: 1.07x faster                                                           |
| xml_etree_parse      | 113 ms                                                          | 109 ms: 1.04x faster                                                            |
| pickle_pure_python   | 286 us                                                          | 281 us: 1.02x faster                                                            |
| xml_etree_process    | 53.2 ms                                                         | 52.4 ms: 1.02x faster                                                           |
| json_loads           | 20.4 us                                                         | 21.5 us: 1.06x slower                                                           |
| json_dumps           | 7.40 ms                                                         | 9.25 ms: 1.25x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.05x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250123-pythonperf1_win32-x86-mdboom-test_without_pgo_wor-3.14.0a4+-71a13ea |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 20.3 ms: 1.06x slower                                                           |
| python_startup         | 22.4 ms                                                         | 26.7 ms: 1.19x slower                                                           |
| Geometric mean         | (ref)                                                           | 1.13x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250123-pythonperf1_win32-x86-mdboom-test_without_pgo_wor-3.14.0a4+-71a13ea |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 7.68 ms: 1.30x faster                                                           |
| django_template | 36.9 ms                                                         | 33.7 ms: 1.09x faster                                                           |
| Geometric mean  | (ref)                                                           | 1.19x faster                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250123-pythonperf1_win32-x86-mdboom-test_without_pgo_wor-3.14.0a4+-71a13ea |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| deepcopy_memo              | 38.4 us                                                         | 21.9 us: 1.75x faster                                                           |
| async_tree_io              | 693 ms                                                          | 459 ms: 1.51x faster                                                            |
| async_tree_io_tg           | 677 ms                                                          | 453 ms: 1.50x faster                                                            |
| generators                 | 38.5 ms                                                         | 26.1 ms: 1.47x faster                                                           |
| deepcopy                   | 360 us                                                          | 250 us: 1.44x faster                                                            |
| async_tree_none_tg         | 278 ms                                                          | 192 ms: 1.44x faster                                                            |
| spectral_norm              | 104 ms                                                          | 72.0 ms: 1.44x faster                                                           |
| async_tree_memoization_tg  | 350 ms                                                          | 244 ms: 1.43x faster                                                            |
| nbody                      | 127 ms                                                          | 89.4 ms: 1.42x faster                                                           |
| async_tree_none            | 298 ms                                                          | 212 ms: 1.40x faster                                                            |
| async_tree_memoization     | 364 ms                                                          | 261 ms: 1.39x faster                                                            |
| go                         | 137 ms                                                          | 101 ms: 1.36x faster                                                            |
| float                      | 76.7 ms                                                         | 57.8 ms: 1.33x faster                                                           |
| logging_silent             | 101 ns                                                          | 76.4 ns: 1.32x faster                                                           |
| hexiom                     | 6.82 ms                                                         | 5.18 ms: 1.32x faster                                                           |
| regex_effbot               | 2.04 ms                                                         | 1.55 ms: 1.31x faster                                                           |
| deltablue                  | 3.58 ms                                                         | 2.75 ms: 1.30x faster                                                           |
| tomli_loads                | 2.20 sec                                                        | 1.69 sec: 1.30x faster                                                          |
| mako                       | 9.96 ms                                                         | 7.68 ms: 1.30x faster                                                           |
| comprehensions             | 19.2 us                                                         | 14.9 us: 1.29x faster                                                           |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 3.01 ms: 1.28x faster                                                           |
| scimark_lu                 | 93.2 ms                                                         | 74.6 ms: 1.25x faster                                                           |
| scimark_sor                | 130 ms                                                          | 104 ms: 1.25x faster                                                            |
| pyflate                    | 424 ms                                                          | 341 ms: 1.24x faster                                                            |
| scimark_fft                | 271 ms                                                          | 219 ms: 1.24x faster                                                            |
| deepcopy_reduce            | 3.23 us                                                         | 2.61 us: 1.23x faster                                                           |
| chaos                      | 69.4 ms                                                         | 56.4 ms: 1.23x faster                                                           |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 461 ms: 1.22x faster                                                            |
| regex_compile              | 129 ms                                                          | 106 ms: 1.22x faster                                                            |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 450 ms: 1.21x faster                                                            |
| coroutines                 | 20.9 ms                                                         | 17.6 ms: 1.19x faster                                                           |
| scimark_monte_carlo        | 66.4 ms                                                         | 56.2 ms: 1.18x faster                                                           |
| nqueens                    | 93.7 ms                                                         | 79.5 ms: 1.18x faster                                                           |
| logging_simple             | 9.75 us                                                         | 8.37 us: 1.16x faster                                                           |
| xml_etree_iterparse        | 77.6 ms                                                         | 66.9 ms: 1.16x faster                                                           |
| sqlglot_parse              | 1.25 ms                                                         | 1.08 ms: 1.16x faster                                                           |
| fannkuch                   | 354 ms                                                          | 305 ms: 1.16x faster                                                            |
| sqlglot_transpile          | 1.53 ms                                                         | 1.32 ms: 1.16x faster                                                           |
| logging_format             | 10.4 us                                                         | 9.05 us: 1.15x faster                                                           |
| unpickle_pure_python       | 210 us                                                          | 185 us: 1.14x faster                                                            |
| pycparser                  | 978 ms                                                          | 864 ms: 1.13x faster                                                            |
| regex_dna                  | 127 ms                                                          | 113 ms: 1.12x faster                                                            |
| dulwich_log                | 58.5 ms                                                         | 52.2 ms: 1.12x faster                                                           |
| crypto_pyaes               | 69.2 ms                                                         | 62.0 ms: 1.12x faster                                                           |
| mdp                        | 1.91 sec                                                        | 1.71 sec: 1.12x faster                                                          |
| sympy_sum                  | 123 ms                                                          | 111 ms: 1.11x faster                                                            |
| sympy_integrate            | 17.5 ms                                                         | 15.9 ms: 1.10x faster                                                           |
| raytrace                   | 308 ms                                                          | 281 ms: 1.10x faster                                                            |
| 2to3                       | 280 ms                                                          | 256 ms: 1.09x faster                                                            |
| django_template            | 36.9 ms                                                         | 33.7 ms: 1.09x faster                                                           |
| pprint_pformat             | 1.50 sec                                                        | 1.38 sec: 1.08x faster                                                          |
| sqlite_synth               | 2.07 us                                                         | 1.91 us: 1.08x faster                                                           |
| sqlglot_optimize           | 48.5 ms                                                         | 44.9 ms: 1.08x faster                                                           |
| xml_etree_generate         | 72.1 ms                                                         | 67.1 ms: 1.07x faster                                                           |
| pprint_safe_repr           | 721 ms                                                          | 672 ms: 1.07x faster                                                            |
| docutils                   | 1.98 sec                                                        | 1.85 sec: 1.07x faster                                                          |
| bench_thread_pool          | 1.10 ms                                                         | 1.03 ms: 1.07x faster                                                           |
| sympy_str                  | 240 ms                                                          | 226 ms: 1.06x faster                                                            |
| meteor_contest             | 86.9 ms                                                         | 82.0 ms: 1.06x faster                                                           |
| pathlib                    | 91.4 ms                                                         | 86.7 ms: 1.06x faster                                                           |
| xml_etree_parse            | 113 ms                                                          | 109 ms: 1.04x faster                                                            |
| richards                   | 41.3 ms                                                         | 39.9 ms: 1.04x faster                                                           |
| richards_super             | 46.5 ms                                                         | 45.5 ms: 1.02x faster                                                           |
| pickle_pure_python         | 286 us                                                          | 281 us: 1.02x faster                                                            |
| xml_etree_process          | 53.2 ms                                                         | 52.4 ms: 1.02x faster                                                           |
| async_generators           | 313 ms                                                          | 311 ms: 1.01x faster                                                            |
| sympy_expand               | 398 ms                                                          | 402 ms: 1.01x slower                                                            |
| json_loads                 | 20.4 us                                                         | 21.5 us: 1.06x slower                                                           |
| python_startup_no_site     | 19.1 ms                                                         | 20.3 ms: 1.06x slower                                                           |
| regex_v8                   | 15.0 ms                                                         | 16.2 ms: 1.08x slower                                                           |
| coverage                   | 48.4 ms                                                         | 53.1 ms: 1.10x slower                                                           |
| json                       | 4.15 ms                                                         | 4.86 ms: 1.17x slower                                                           |
| python_startup             | 22.4 ms                                                         | 26.7 ms: 1.19x slower                                                           |
| gc_traversal               | 1.44 ms                                                         | 1.78 ms: 1.24x slower                                                           |
| json_dumps                 | 7.40 ms                                                         | 9.25 ms: 1.25x slower                                                           |
| bench_mp_pool              | 75.4 ms                                                         | 95.1 ms: 1.26x slower                                                           |
| typing_runtime_protocols   | 126 us                                                          | 160 us: 1.26x slower                                                            |
| telco                      | 5.51 ms                                                         | 7.13 ms: 1.29x slower                                                           |
| create_gc_cycles           | 652 us                                                          | 1.05 ms: 1.61x slower                                                           |
| sqlglot_normalize          | 100 ms                                                          | 235 ms: 2.34x slower                                                            |
| Geometric mean             | (ref)                                                           | 1.12x faster                                                                    |

Benchmark hidden because not significant (1): pidigits
Ignored benchmarks (15) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20250123-3.14.0a4+-71a13ea/bm-20250123-pythonperf1_win32-x86-mdboom-test_without_pgo_wor-3.14.0a4+-71a13ea.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.123x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.11x
- 95% likely to have a speedup of 1.10x
- 99% likely to have a speedup of 1.09x

# Memory
- memory change: unknown