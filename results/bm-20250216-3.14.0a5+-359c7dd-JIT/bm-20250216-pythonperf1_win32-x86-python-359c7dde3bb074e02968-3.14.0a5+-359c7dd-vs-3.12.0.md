# Results vs. 3.12.0

- fork: python
- ref: 359c7dde3bb074e02968
- machine: windows-x86
- commit hash: 359c7dd
- commit date: 2025-02-16
- overall geometric mean: 1.069x faster
- HPT reliability: 99.08%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250216-pythonperf1_win32-x86-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 276 ms: 1.02x faster                                                            |
| docutils       | 1.98 sec                                                        | 2.06 sec: 1.04x slower                                                          |
| Geometric mean | (ref)                                                           | 1.01x slower                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250216-pythonperf1_win32-x86-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_io              | 693 ms                                                          | 506 ms: 1.37x faster                                                            |
| async_tree_io_tg           | 677 ms                                                          | 500 ms: 1.35x faster                                                            |
| async_tree_memoization_tg  | 350 ms                                                          | 275 ms: 1.28x faster                                                            |
| async_tree_none_tg         | 278 ms                                                          | 220 ms: 1.26x faster                                                            |
| async_tree_memoization     | 364 ms                                                          | 295 ms: 1.23x faster                                                            |
| async_tree_none            | 298 ms                                                          | 245 ms: 1.22x faster                                                            |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 482 ms: 1.13x faster                                                            |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 500 ms: 1.13x faster                                                            |
| Geometric mean             | (ref)                                                           | 1.24x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250216-pythonperf1_win32-x86-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 76.7 ms                                                         | 54.5 ms: 1.41x faster                                                           |
| nbody          | 127 ms                                                          | 113 ms: 1.12x faster                                                            |
| pidigits       | 199 ms                                                          | 203 ms: 1.02x slower                                                            |
| Geometric mean | (ref)                                                           | 1.16x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250216-pythonperf1_win32-x86-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_effbot   | 2.04 ms                                                         | 1.55 ms: 1.32x faster                                                           |
| regex_compile  | 129 ms                                                          | 122 ms: 1.06x faster                                                            |
| regex_dna      | 127 ms                                                          | 121 ms: 1.05x faster                                                            |
| regex_v8       | 15.0 ms                                                         | 16.0 ms: 1.06x slower                                                           |
| Geometric mean | (ref)                                                           | 1.08x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250216-pythonperf1_win32-x86-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| xml_etree_iterparse  | 77.6 ms                                                         | 65.6 ms: 1.18x faster                                                           |
| tomli_loads          | 2.20 sec                                                        | 1.89 sec: 1.16x faster                                                          |
| xml_etree_parse      | 113 ms                                                          | 108 ms: 1.05x faster                                                            |
| xml_etree_generate   | 72.1 ms                                                         | 73.1 ms: 1.01x slower                                                           |
| unpickle_list        | 2.95 us                                                         | 3.04 us: 1.03x slower                                                           |
| pickle_dict          | 19.9 us                                                         | 20.8 us: 1.04x slower                                                           |
| xml_etree_process    | 53.2 ms                                                         | 56.0 ms: 1.05x slower                                                           |
| unpickle             | 9.71 us                                                         | 10.5 us: 1.08x slower                                                           |
| json_loads           | 20.4 us                                                         | 22.7 us: 1.11x slower                                                           |
| pickle_list          | 3.37 us                                                         | 3.80 us: 1.13x slower                                                           |
| unpickle_pure_python | 210 us                                                          | 244 us: 1.16x slower                                                            |
| pickle_pure_python   | 286 us                                                          | 334 us: 1.17x slower                                                            |
| pickle               | 7.79 us                                                         | 9.37 us: 1.20x slower                                                           |
| json_dumps           | 7.40 ms                                                         | 9.21 ms: 1.24x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.06x slower                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250216-pythonperf1_win32-x86-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 21.3 ms: 1.12x slower                                                           |
| python_startup         | 22.4 ms                                                         | 27.8 ms: 1.24x slower                                                           |
| Geometric mean         | (ref)                                                           | 1.18x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250216-pythonperf1_win32-x86-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 7.78 ms: 1.28x faster                                                           |
| django_template | 36.9 ms                                                         | 38.8 ms: 1.05x slower                                                           |
| Geometric mean  | (ref)                                                           | 1.10x faster                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250216-pythonperf1_win32-x86-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pathlib                    | 91.4 ms                                                         | 34.8 ms: 2.63x faster                                                           |
| deepcopy_memo              | 38.4 us                                                         | 22.2 us: 1.73x faster                                                           |
| generators                 | 38.5 ms                                                         | 24.1 ms: 1.60x faster                                                           |
| spectral_norm              | 104 ms                                                          | 72.5 ms: 1.43x faster                                                           |
| logging_silent             | 101 ns                                                          | 71.1 ns: 1.42x faster                                                           |
| float                      | 76.7 ms                                                         | 54.5 ms: 1.41x faster                                                           |
| scimark_lu                 | 93.2 ms                                                         | 67.5 ms: 1.38x faster                                                           |
| async_tree_io              | 693 ms                                                          | 506 ms: 1.37x faster                                                            |
| async_tree_io_tg           | 677 ms                                                          | 500 ms: 1.35x faster                                                            |
| deepcopy                   | 360 us                                                          | 272 us: 1.32x faster                                                            |
| scimark_sor                | 130 ms                                                          | 98.4 ms: 1.32x faster                                                           |
| regex_effbot               | 2.04 ms                                                         | 1.55 ms: 1.32x faster                                                           |
| mako                       | 9.96 ms                                                         | 7.78 ms: 1.28x faster                                                           |
| async_tree_memoization_tg  | 350 ms                                                          | 275 ms: 1.28x faster                                                            |
| coroutines                 | 20.9 ms                                                         | 16.5 ms: 1.26x faster                                                           |
| async_tree_none_tg         | 278 ms                                                          | 220 ms: 1.26x faster                                                            |
| unpack_sequence            | 62.5 ns                                                         | 49.9 ns: 1.25x faster                                                           |
| async_tree_memoization     | 364 ms                                                          | 295 ms: 1.23x faster                                                            |
| scimark_monte_carlo        | 66.4 ms                                                         | 54.4 ms: 1.22x faster                                                           |
| hexiom                     | 6.82 ms                                                         | 5.59 ms: 1.22x faster                                                           |
| async_tree_none            | 298 ms                                                          | 245 ms: 1.22x faster                                                            |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 3.19 ms: 1.21x faster                                                           |
| deltablue                  | 3.58 ms                                                         | 2.99 ms: 1.20x faster                                                           |
| pyflate                    | 424 ms                                                          | 358 ms: 1.19x faster                                                            |
| xml_etree_iterparse        | 77.6 ms                                                         | 65.6 ms: 1.18x faster                                                           |
| go                         | 137 ms                                                          | 116 ms: 1.18x faster                                                            |
| tomli_loads                | 2.20 sec                                                        | 1.89 sec: 1.16x faster                                                          |
| raytrace                   | 308 ms                                                          | 266 ms: 1.16x faster                                                            |
| chaos                      | 69.4 ms                                                         | 60.0 ms: 1.16x faster                                                           |
| deepcopy_reduce            | 3.23 us                                                         | 2.84 us: 1.13x faster                                                           |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 482 ms: 1.13x faster                                                            |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 500 ms: 1.13x faster                                                            |
| nbody                      | 127 ms                                                          | 113 ms: 1.12x faster                                                            |
| mdp                        | 1.91 sec                                                        | 1.71 sec: 1.12x faster                                                          |
| comprehensions             | 19.2 us                                                         | 17.2 us: 1.11x faster                                                           |
| logging_simple             | 9.75 us                                                         | 8.83 us: 1.10x faster                                                           |
| dulwich_log                | 58.5 ms                                                         | 53.0 ms: 1.10x faster                                                           |
| logging_format             | 10.4 us                                                         | 9.60 us: 1.08x faster                                                           |
| sqlite_synth               | 2.07 us                                                         | 1.91 us: 1.08x faster                                                           |
| sympy_sum                  | 123 ms                                                          | 116 ms: 1.06x faster                                                            |
| regex_compile              | 129 ms                                                          | 122 ms: 1.06x faster                                                            |
| xml_etree_parse            | 113 ms                                                          | 108 ms: 1.05x faster                                                            |
| regex_dna                  | 127 ms                                                          | 121 ms: 1.05x faster                                                            |
| bench_thread_pool          | 1.10 ms                                                         | 1.05 ms: 1.05x faster                                                           |
| asyncio_tcp_ssl            | 17.7 sec                                                        | 17.0 sec: 1.04x faster                                                          |
| richards_super             | 46.5 ms                                                         | 45.0 ms: 1.03x faster                                                           |
| richards                   | 41.3 ms                                                         | 40.1 ms: 1.03x faster                                                           |
| sympy_integrate            | 17.5 ms                                                         | 17.1 ms: 1.02x faster                                                           |
| 2to3                       | 280 ms                                                          | 276 ms: 1.02x faster                                                            |
| sympy_str                  | 240 ms                                                          | 238 ms: 1.00x faster                                                            |
| pycparser                  | 978 ms                                                          | 982 ms: 1.00x slower                                                            |
| xml_etree_generate         | 72.1 ms                                                         | 73.1 ms: 1.01x slower                                                           |
| pidigits                   | 199 ms                                                          | 203 ms: 1.02x slower                                                            |
| scimark_fft                | 271 ms                                                          | 279 ms: 1.03x slower                                                            |
| unpickle_list              | 2.95 us                                                         | 3.04 us: 1.03x slower                                                           |
| docutils                   | 1.98 sec                                                        | 2.06 sec: 1.04x slower                                                          |
| sqlglot_transpile          | 1.53 ms                                                         | 1.59 ms: 1.04x slower                                                           |
| pickle_dict                | 19.9 us                                                         | 20.8 us: 1.04x slower                                                           |
| sqlglot_parse              | 1.25 ms                                                         | 1.31 ms: 1.05x slower                                                           |
| xml_etree_process          | 53.2 ms                                                         | 56.0 ms: 1.05x slower                                                           |
| django_template            | 36.9 ms                                                         | 38.8 ms: 1.05x slower                                                           |
| meteor_contest             | 86.9 ms                                                         | 91.5 ms: 1.05x slower                                                           |
| sqlglot_optimize           | 48.5 ms                                                         | 51.2 ms: 1.06x slower                                                           |
| sympy_expand               | 398 ms                                                          | 423 ms: 1.06x slower                                                            |
| regex_v8                   | 15.0 ms                                                         | 16.0 ms: 1.06x slower                                                           |
| fannkuch                   | 354 ms                                                          | 379 ms: 1.07x slower                                                            |
| sqlglot_normalize          | 100 ms                                                          | 108 ms: 1.08x slower                                                            |
| async_generators           | 313 ms                                                          | 338 ms: 1.08x slower                                                            |
| unpickle                   | 9.71 us                                                         | 10.5 us: 1.08x slower                                                           |
| pprint_pformat             | 1.50 sec                                                        | 1.65 sec: 1.10x slower                                                          |
| json                       | 4.15 ms                                                         | 4.61 ms: 1.11x slower                                                           |
| pprint_safe_repr           | 721 ms                                                          | 801 ms: 1.11x slower                                                            |
| json_loads                 | 20.4 us                                                         | 22.7 us: 1.11x slower                                                           |
| python_startup_no_site     | 19.1 ms                                                         | 21.3 ms: 1.12x slower                                                           |
| coverage                   | 48.4 ms                                                         | 54.2 ms: 1.12x slower                                                           |
| pickle_list                | 3.37 us                                                         | 3.80 us: 1.13x slower                                                           |
| unpickle_pure_python       | 210 us                                                          | 244 us: 1.16x slower                                                            |
| pickle_pure_python         | 286 us                                                          | 334 us: 1.17x slower                                                            |
| crypto_pyaes               | 69.2 ms                                                         | 81.4 ms: 1.18x slower                                                           |
| bench_mp_pool              | 75.4 ms                                                         | 89.6 ms: 1.19x slower                                                           |
| pickle                     | 7.79 us                                                         | 9.37 us: 1.20x slower                                                           |
| python_startup             | 22.4 ms                                                         | 27.8 ms: 1.24x slower                                                           |
| json_dumps                 | 7.40 ms                                                         | 9.21 ms: 1.24x slower                                                           |
| gc_traversal               | 1.44 ms                                                         | 1.83 ms: 1.27x slower                                                           |
| telco                      | 5.51 ms                                                         | 7.81 ms: 1.42x slower                                                           |
| typing_runtime_protocols   | 126 us                                                          | 181 us: 1.43x slower                                                            |
| create_gc_cycles           | 652 us                                                          | 1.04 ms: 1.59x slower                                                           |
| Geometric mean             | (ref)                                                           | 1.06x faster                                                                    |

Benchmark hidden because not significant (2): nqueens, asyncio_tcp
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (13) of results/bm-20250216-3.14.0a5+-359c7dd-JIT/bm-20250216-pythonperf1_win32-x86-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.069x faster

# HPT report

- Reliability score: 99.08% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown