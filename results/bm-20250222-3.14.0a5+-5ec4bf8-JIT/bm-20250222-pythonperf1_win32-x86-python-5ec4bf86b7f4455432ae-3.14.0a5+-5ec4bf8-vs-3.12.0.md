# Results vs. 3.12.0

- fork: python
- ref: 5ec4bf86b7f4455432ae
- machine: windows-x86
- commit hash: 5ec4bf8
- commit date: 2025-02-22
- overall geometric mean: 1.071x faster
- HPT reliability: 99.46%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250222-pythonperf1_win32-x86-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 278 ms: 1.01x faster                                                            |
| docutils       | 1.98 sec                                                        | 2.00 sec: 1.01x slower                                                          |
| Geometric mean | (ref)                                                           | 1.00x slower                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250222-pythonperf1_win32-x86-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_io_tg           | 677 ms                                                          | 473 ms: 1.43x faster                                                            |
| async_tree_io              | 693 ms                                                          | 491 ms: 1.41x faster                                                            |
| async_tree_memoization_tg  | 350 ms                                                          | 269 ms: 1.30x faster                                                            |
| async_tree_none_tg         | 278 ms                                                          | 216 ms: 1.28x faster                                                            |
| async_tree_memoization     | 364 ms                                                          | 284 ms: 1.28x faster                                                            |
| async_tree_none            | 298 ms                                                          | 236 ms: 1.26x faster                                                            |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 487 ms: 1.12x faster                                                            |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 503 ms: 1.12x faster                                                            |
| Geometric mean             | (ref)                                                           | 1.27x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250222-pythonperf1_win32-x86-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 76.7 ms                                                         | 57.0 ms: 1.35x faster                                                           |
| nbody          | 127 ms                                                          | 115 ms: 1.10x faster                                                            |
| pidigits       | 199 ms                                                          | 203 ms: 1.02x slower                                                            |
| Geometric mean | (ref)                                                           | 1.13x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250222-pythonperf1_win32-x86-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_effbot   | 2.04 ms                                                         | 1.61 ms: 1.26x faster                                                           |
| regex_dna      | 127 ms                                                          | 118 ms: 1.07x faster                                                            |
| regex_compile  | 129 ms                                                          | 123 ms: 1.05x faster                                                            |
| regex_v8       | 15.0 ms                                                         | 15.8 ms: 1.05x slower                                                           |
| Geometric mean | (ref)                                                           | 1.08x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250222-pythonperf1_win32-x86-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| xml_etree_iterparse  | 77.6 ms                                                         | 64.9 ms: 1.20x faster                                                           |
| tomli_loads          | 2.20 sec                                                        | 1.87 sec: 1.17x faster                                                          |
| xml_etree_parse      | 113 ms                                                          | 107 ms: 1.05x faster                                                            |
| xml_etree_generate   | 72.1 ms                                                         | 73.2 ms: 1.01x slower                                                           |
| unpickle_list        | 2.95 us                                                         | 3.06 us: 1.04x slower                                                           |
| xml_etree_process    | 53.2 ms                                                         | 56.1 ms: 1.05x slower                                                           |
| pickle_dict          | 19.9 us                                                         | 21.1 us: 1.06x slower                                                           |
| json_loads           | 20.4 us                                                         | 21.8 us: 1.07x slower                                                           |
| unpickle             | 9.71 us                                                         | 10.8 us: 1.11x slower                                                           |
| pickle_list          | 3.37 us                                                         | 3.78 us: 1.12x slower                                                           |
| json_dumps           | 7.40 ms                                                         | 8.40 ms: 1.14x slower                                                           |
| unpickle_pure_python | 210 us                                                          | 240 us: 1.14x slower                                                            |
| pickle               | 7.79 us                                                         | 9.22 us: 1.18x slower                                                           |
| pickle_pure_python   | 286 us                                                          | 346 us: 1.21x slower                                                            |
| Geometric mean       | (ref)                                                           | 1.05x slower                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250222-pythonperf1_win32-x86-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 21.4 ms: 1.12x slower                                                           |
| python_startup         | 22.4 ms                                                         | 27.8 ms: 1.24x slower                                                           |
| Geometric mean         | (ref)                                                           | 1.18x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250222-pythonperf1_win32-x86-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 7.50 ms: 1.33x faster                                                           |
| django_template | 36.9 ms                                                         | 38.9 ms: 1.05x slower                                                           |
| Geometric mean  | (ref)                                                           | 1.12x faster                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250222-pythonperf1_win32-x86-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pathlib                    | 91.4 ms                                                         | 35.2 ms: 2.59x faster                                                           |
| deepcopy_memo              | 38.4 us                                                         | 21.4 us: 1.79x faster                                                           |
| generators                 | 38.5 ms                                                         | 24.8 ms: 1.55x faster                                                           |
| spectral_norm              | 104 ms                                                          | 71.4 ms: 1.45x faster                                                           |
| async_tree_io_tg           | 677 ms                                                          | 473 ms: 1.43x faster                                                            |
| deepcopy                   | 360 us                                                          | 255 us: 1.41x faster                                                            |
| async_tree_io              | 693 ms                                                          | 491 ms: 1.41x faster                                                            |
| scimark_lu                 | 93.2 ms                                                         | 68.8 ms: 1.36x faster                                                           |
| logging_silent             | 101 ns                                                          | 75.0 ns: 1.35x faster                                                           |
| float                      | 76.7 ms                                                         | 57.0 ms: 1.35x faster                                                           |
| mako                       | 9.96 ms                                                         | 7.50 ms: 1.33x faster                                                           |
| async_tree_memoization_tg  | 350 ms                                                          | 269 ms: 1.30x faster                                                            |
| async_tree_none_tg         | 278 ms                                                          | 216 ms: 1.28x faster                                                            |
| async_tree_memoization     | 364 ms                                                          | 284 ms: 1.28x faster                                                            |
| scimark_sor                | 130 ms                                                          | 102 ms: 1.28x faster                                                            |
| regex_effbot               | 2.04 ms                                                         | 1.61 ms: 1.26x faster                                                           |
| async_tree_none            | 298 ms                                                          | 236 ms: 1.26x faster                                                            |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 3.09 ms: 1.25x faster                                                           |
| deepcopy_reduce            | 3.23 us                                                         | 2.63 us: 1.23x faster                                                           |
| unpack_sequence            | 62.5 ns                                                         | 51.9 ns: 1.20x faster                                                           |
| xml_etree_iterparse        | 77.6 ms                                                         | 64.9 ms: 1.20x faster                                                           |
| coroutines                 | 20.9 ms                                                         | 17.5 ms: 1.19x faster                                                           |
| tomli_loads                | 2.20 sec                                                        | 1.87 sec: 1.17x faster                                                          |
| scimark_monte_carlo        | 66.4 ms                                                         | 56.6 ms: 1.17x faster                                                           |
| chaos                      | 69.4 ms                                                         | 59.2 ms: 1.17x faster                                                           |
| hexiom                     | 6.82 ms                                                         | 5.92 ms: 1.15x faster                                                           |
| comprehensions             | 19.2 us                                                         | 16.8 us: 1.14x faster                                                           |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 487 ms: 1.12x faster                                                            |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 503 ms: 1.12x faster                                                            |
| sqlite_synth               | 2.07 us                                                         | 1.87 us: 1.11x faster                                                           |
| mdp                        | 1.91 sec                                                        | 1.73 sec: 1.11x faster                                                          |
| nbody                      | 127 ms                                                          | 115 ms: 1.10x faster                                                            |
| pyflate                    | 424 ms                                                          | 385 ms: 1.10x faster                                                            |
| deltablue                  | 3.58 ms                                                         | 3.26 ms: 1.10x faster                                                           |
| dulwich_log                | 58.5 ms                                                         | 53.4 ms: 1.10x faster                                                           |
| regex_dna                  | 127 ms                                                          | 118 ms: 1.07x faster                                                            |
| logging_simple             | 9.75 us                                                         | 9.14 us: 1.07x faster                                                           |
| nqueens                    | 93.7 ms                                                         | 87.9 ms: 1.07x faster                                                           |
| sympy_sum                  | 123 ms                                                          | 115 ms: 1.06x faster                                                            |
| logging_format             | 10.4 us                                                         | 9.78 us: 1.06x faster                                                           |
| go                         | 137 ms                                                          | 129 ms: 1.06x faster                                                            |
| raytrace                   | 308 ms                                                          | 290 ms: 1.06x faster                                                            |
| xml_etree_parse            | 113 ms                                                          | 107 ms: 1.05x faster                                                            |
| regex_compile              | 129 ms                                                          | 123 ms: 1.05x faster                                                            |
| asyncio_tcp_ssl            | 17.7 sec                                                        | 17.2 sec: 1.03x faster                                                          |
| sympy_integrate            | 17.5 ms                                                         | 17.1 ms: 1.02x faster                                                           |
| sympy_str                  | 240 ms                                                          | 236 ms: 1.02x faster                                                            |
| 2to3                       | 280 ms                                                          | 278 ms: 1.01x faster                                                            |
| docutils                   | 1.98 sec                                                        | 2.00 sec: 1.01x slower                                                          |
| xml_etree_generate         | 72.1 ms                                                         | 73.2 ms: 1.01x slower                                                           |
| pidigits                   | 199 ms                                                          | 203 ms: 1.02x slower                                                            |
| sqlglot_transpile          | 1.53 ms                                                         | 1.58 ms: 1.03x slower                                                           |
| pycparser                  | 978 ms                                                          | 1.01 sec: 1.03x slower                                                          |
| sqlglot_optimize           | 48.5 ms                                                         | 50.2 ms: 1.04x slower                                                           |
| unpickle_list              | 2.95 us                                                         | 3.06 us: 1.04x slower                                                           |
| sqlglot_parse              | 1.25 ms                                                         | 1.30 ms: 1.04x slower                                                           |
| sympy_expand               | 398 ms                                                          | 416 ms: 1.05x slower                                                            |
| fannkuch                   | 354 ms                                                          | 370 ms: 1.05x slower                                                            |
| regex_v8                   | 15.0 ms                                                         | 15.8 ms: 1.05x slower                                                           |
| sqlglot_normalize          | 100 ms                                                          | 105 ms: 1.05x slower                                                            |
| richards                   | 41.3 ms                                                         | 43.6 ms: 1.05x slower                                                           |
| meteor_contest             | 86.9 ms                                                         | 91.6 ms: 1.05x slower                                                           |
| xml_etree_process          | 53.2 ms                                                         | 56.1 ms: 1.05x slower                                                           |
| django_template            | 36.9 ms                                                         | 38.9 ms: 1.05x slower                                                           |
| json                       | 4.15 ms                                                         | 4.40 ms: 1.06x slower                                                           |
| pickle_dict                | 19.9 us                                                         | 21.1 us: 1.06x slower                                                           |
| pprint_pformat             | 1.50 sec                                                        | 1.59 sec: 1.06x slower                                                          |
| json_loads                 | 20.4 us                                                         | 21.8 us: 1.07x slower                                                           |
| pprint_safe_repr           | 721 ms                                                          | 776 ms: 1.08x slower                                                            |
| asyncio_tcp                | 662 ms                                                          | 717 ms: 1.08x slower                                                            |
| richards_super             | 46.5 ms                                                         | 51.3 ms: 1.10x slower                                                           |
| coverage                   | 48.4 ms                                                         | 53.6 ms: 1.11x slower                                                           |
| unpickle                   | 9.71 us                                                         | 10.8 us: 1.11x slower                                                           |
| python_startup_no_site     | 19.1 ms                                                         | 21.4 ms: 1.12x slower                                                           |
| pickle_list                | 3.37 us                                                         | 3.78 us: 1.12x slower                                                           |
| json_dumps                 | 7.40 ms                                                         | 8.40 ms: 1.14x slower                                                           |
| unpickle_pure_python       | 210 us                                                          | 240 us: 1.14x slower                                                            |
| crypto_pyaes               | 69.2 ms                                                         | 80.3 ms: 1.16x slower                                                           |
| pickle                     | 7.79 us                                                         | 9.22 us: 1.18x slower                                                           |
| bench_mp_pool              | 75.4 ms                                                         | 90.8 ms: 1.20x slower                                                           |
| pickle_pure_python         | 286 us                                                          | 346 us: 1.21x slower                                                            |
| bench_thread_pool          | 1.10 ms                                                         | 1.34 ms: 1.21x slower                                                           |
| python_startup             | 22.4 ms                                                         | 27.8 ms: 1.24x slower                                                           |
| gc_traversal               | 1.44 ms                                                         | 1.81 ms: 1.26x slower                                                           |
| typing_runtime_protocols   | 126 us                                                          | 172 us: 1.36x slower                                                            |
| telco                      | 5.51 ms                                                         | 7.58 ms: 1.37x slower                                                           |
| create_gc_cycles           | 652 us                                                          | 1.03 ms: 1.58x slower                                                           |
| Geometric mean             | (ref)                                                           | 1.06x faster                                                                    |

Benchmark hidden because not significant (2): scimark_fft, async_generators
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (13) of results/bm-20250222-3.14.0a5+-5ec4bf8-JIT/bm-20250222-pythonperf1_win32-x86-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.071x faster

# HPT report

- Reliability score: 99.46% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown