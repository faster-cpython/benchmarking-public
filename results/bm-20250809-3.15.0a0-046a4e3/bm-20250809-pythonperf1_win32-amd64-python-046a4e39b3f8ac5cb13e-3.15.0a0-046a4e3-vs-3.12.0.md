# Results vs. 3.12.0

- fork: python
- ref: 046a4e39b3f8ac5cb13e
- machine: windows-amd64
- commit hash: 046a4e3
- commit date: 2025-08-09
- overall geometric mean: 1.455x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.41x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250809-pythonperf1_win32-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 219 ms: 1.28x faster                                                             |
| docutils       | 1.98 sec                                                        | 1.59 sec: 1.25x faster                                                           |
| Geometric mean | (ref)                                                           | 1.26x faster                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250809-pythonperf1_win32-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_io              | 693 ms                                                          | 389 ms: 1.78x faster                                                             |
| async_tree_memoization     | 364 ms                                                          | 204 ms: 1.78x faster                                                             |
| async_tree_io_tg           | 677 ms                                                          | 390 ms: 1.74x faster                                                             |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 328 ms: 1.72x faster                                                             |
| async_tree_none            | 298 ms                                                          | 177 ms: 1.69x faster                                                             |
| async_tree_memoization_tg  | 350 ms                                                          | 210 ms: 1.67x faster                                                             |
| async_tree_none_tg         | 278 ms                                                          | 168 ms: 1.65x faster                                                             |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 337 ms: 1.62x faster                                                             |
| Geometric mean             | (ref)                                                           | 1.70x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250809-pythonperf1_win32-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 65.8 ms: 1.93x faster                                                            |
| float          | 76.7 ms                                                         | 44.0 ms: 1.74x faster                                                            |
| pidigits       | 199 ms                                                          | 145 ms: 1.37x faster                                                             |
| Geometric mean | (ref)                                                           | 1.67x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250809-pythonperf1_win32-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 81.3 ms: 1.59x faster                                                            |
| regex_effbot   | 2.04 ms                                                         | 1.48 ms: 1.37x faster                                                            |
| regex_v8       | 15.0 ms                                                         | 13.3 ms: 1.13x faster                                                            |
| regex_dna      | 127 ms                                                          | 119 ms: 1.07x faster                                                             |
| Geometric mean | (ref)                                                           | 1.27x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250809-pythonperf1_win32-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| unpickle_pure_python | 210 us                                                          | 135 us: 1.55x faster                                                             |
| tomli_loads          | 2.20 sec                                                        | 1.44 sec: 1.53x faster                                                           |
| json_loads           | 20.4 us                                                         | 14.1 us: 1.45x faster                                                            |
| json_dumps           | 7.40 ms                                                         | 5.36 ms: 1.38x faster                                                            |
| pickle_pure_python   | 286 us                                                          | 214 us: 1.34x faster                                                             |
| xml_etree_process    | 53.2 ms                                                         | 40.2 ms: 1.32x faster                                                            |
| xml_etree_parse      | 113 ms                                                          | 88.9 ms: 1.27x faster                                                            |
| xml_etree_generate   | 72.1 ms                                                         | 57.9 ms: 1.25x faster                                                            |
| xml_etree_iterparse  | 77.6 ms                                                         | 64.4 ms: 1.21x faster                                                            |
| unpickle             | 9.71 us                                                         | 8.52 us: 1.14x faster                                                            |
| unpickle_list        | 2.95 us                                                         | 2.85 us: 1.03x faster                                                            |
| pickle_dict          | 19.9 us                                                         | 19.8 us: 1.01x faster                                                            |
| pickle_list          | 3.37 us                                                         | 3.46 us: 1.03x slower                                                            |
| pickle               | 7.79 us                                                         | 8.05 us: 1.03x slower                                                            |
| Geometric mean       | (ref)                                                           | 1.23x faster                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250809-pythonperf1_win32-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 19.8 ms: 1.04x slower                                                            |
| python_startup         | 22.4 ms                                                         | 26.6 ms: 1.19x slower                                                            |
| Geometric mean         | (ref)                                                           | 1.11x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250809-pythonperf1_win32-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| django_template | 36.9 ms                                                         | 24.3 ms: 1.52x faster                                                            |
| mako            | 9.96 ms                                                         | 6.66 ms: 1.50x faster                                                            |
| Geometric mean  | (ref)                                                           | 1.51x faster                                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250809-pythonperf1_win32-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| asyncio_tcp_ssl            | 17.7 sec                                                        | 1.40 sec: 12.60x faster                                                          |
| pathlib                    | 91.4 ms                                                         | 31.9 ms: 2.87x faster                                                            |
| mdp                        | 1.91 sec                                                        | 794 ms: 2.41x faster                                                             |
| deepcopy                   | 360 us                                                          | 168 us: 2.15x faster                                                             |
| deepcopy_memo              | 38.4 us                                                         | 18.2 us: 2.11x faster                                                            |
| generators                 | 38.5 ms                                                         | 19.1 ms: 2.01x faster                                                            |
| nbody                      | 127 ms                                                          | 65.8 ms: 1.93x faster                                                            |
| go                         | 137 ms                                                          | 76.7 ms: 1.79x faster                                                            |
| deepcopy_reduce            | 3.23 us                                                         | 1.80 us: 1.79x faster                                                            |
| async_tree_io              | 693 ms                                                          | 389 ms: 1.78x faster                                                             |
| async_tree_memoization     | 364 ms                                                          | 204 ms: 1.78x faster                                                             |
| comprehensions             | 19.2 us                                                         | 11.0 us: 1.75x faster                                                            |
| unpack_sequence            | 62.5 ns                                                         | 35.8 ns: 1.74x faster                                                            |
| float                      | 76.7 ms                                                         | 44.0 ms: 1.74x faster                                                            |
| logging_silent             | 101 ns                                                          | 58.0 ns: 1.74x faster                                                            |
| async_tree_io_tg           | 677 ms                                                          | 390 ms: 1.74x faster                                                             |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 328 ms: 1.72x faster                                                             |
| chaos                      | 69.4 ms                                                         | 40.6 ms: 1.71x faster                                                            |
| async_tree_none            | 298 ms                                                          | 177 ms: 1.69x faster                                                             |
| raytrace                   | 308 ms                                                          | 184 ms: 1.67x faster                                                             |
| async_tree_memoization_tg  | 350 ms                                                          | 210 ms: 1.67x faster                                                             |
| hexiom                     | 6.82 ms                                                         | 4.11 ms: 1.66x faster                                                            |
| async_tree_none_tg         | 278 ms                                                          | 168 ms: 1.65x faster                                                             |
| scimark_sor                | 130 ms                                                          | 78.9 ms: 1.65x faster                                                            |
| spectral_norm              | 104 ms                                                          | 63.9 ms: 1.62x faster                                                            |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 337 ms: 1.62x faster                                                             |
| deltablue                  | 3.58 ms                                                         | 2.21 ms: 1.62x faster                                                            |
| logging_simple             | 9.75 us                                                         | 6.03 us: 1.62x faster                                                            |
| logging_format             | 10.4 us                                                         | 6.52 us: 1.60x faster                                                            |
| regex_compile              | 129 ms                                                          | 81.3 ms: 1.59x faster                                                            |
| scimark_lu                 | 93.2 ms                                                         | 59.3 ms: 1.57x faster                                                            |
| scimark_monte_carlo        | 66.4 ms                                                         | 42.4 ms: 1.57x faster                                                            |
| unpickle_pure_python       | 210 us                                                          | 135 us: 1.55x faster                                                             |
| tomli_loads                | 2.20 sec                                                        | 1.44 sec: 1.53x faster                                                           |
| richards                   | 41.3 ms                                                         | 27.2 ms: 1.52x faster                                                            |
| django_template            | 36.9 ms                                                         | 24.3 ms: 1.52x faster                                                            |
| mako                       | 9.96 ms                                                         | 6.66 ms: 1.50x faster                                                            |
| richards_super             | 46.5 ms                                                         | 31.1 ms: 1.49x faster                                                            |
| nqueens                    | 93.7 ms                                                         | 63.1 ms: 1.48x faster                                                            |
| dulwich_log                | 58.5 ms                                                         | 39.4 ms: 1.48x faster                                                            |
| crypto_pyaes               | 69.2 ms                                                         | 46.9 ms: 1.48x faster                                                            |
| pprint_pformat             | 1.50 sec                                                        | 1.02 sec: 1.46x faster                                                           |
| scimark_fft                | 271 ms                                                          | 187 ms: 1.45x faster                                                             |
| pprint_safe_repr           | 721 ms                                                          | 497 ms: 1.45x faster                                                             |
| pyflate                    | 424 ms                                                          | 293 ms: 1.45x faster                                                             |
| json_loads                 | 20.4 us                                                         | 14.1 us: 1.45x faster                                                            |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 2.69 ms: 1.43x faster                                                            |
| coroutines                 | 20.9 ms                                                         | 14.7 ms: 1.42x faster                                                            |
| sympy_str                  | 240 ms                                                          | 170 ms: 1.41x faster                                                             |
| sympy_sum                  | 123 ms                                                          | 87.3 ms: 1.41x faster                                                            |
| async_generators           | 313 ms                                                          | 224 ms: 1.40x faster                                                             |
| json                       | 4.15 ms                                                         | 2.97 ms: 1.40x faster                                                            |
| pycparser                  | 978 ms                                                          | 702 ms: 1.39x faster                                                             |
| sympy_integrate            | 17.5 ms                                                         | 12.6 ms: 1.39x faster                                                            |
| sympy_expand               | 398 ms                                                          | 287 ms: 1.39x faster                                                             |
| json_dumps                 | 7.40 ms                                                         | 5.36 ms: 1.38x faster                                                            |
| pidigits                   | 199 ms                                                          | 145 ms: 1.37x faster                                                             |
| regex_effbot               | 2.04 ms                                                         | 1.48 ms: 1.37x faster                                                            |
| fannkuch                   | 354 ms                                                          | 262 ms: 1.35x faster                                                             |
| pickle_pure_python         | 286 us                                                          | 214 us: 1.34x faster                                                             |
| xml_etree_process          | 53.2 ms                                                         | 40.2 ms: 1.32x faster                                                            |
| asyncio_tcp                | 662 ms                                                          | 506 ms: 1.31x faster                                                             |
| bench_thread_pool          | 1.10 ms                                                         | 848 us: 1.30x faster                                                             |
| sqlite_synth               | 2.07 us                                                         | 1.61 us: 1.28x faster                                                            |
| 2to3                       | 280 ms                                                          | 219 ms: 1.28x faster                                                             |
| xml_etree_parse            | 113 ms                                                          | 88.9 ms: 1.27x faster                                                            |
| docutils                   | 1.98 sec                                                        | 1.59 sec: 1.25x faster                                                           |
| xml_etree_generate         | 72.1 ms                                                         | 57.9 ms: 1.25x faster                                                            |
| typing_runtime_protocols   | 126 us                                                          | 104 us: 1.21x faster                                                             |
| xml_etree_iterparse        | 77.6 ms                                                         | 64.4 ms: 1.21x faster                                                            |
| meteor_contest             | 86.9 ms                                                         | 72.6 ms: 1.20x faster                                                            |
| telco                      | 5.51 ms                                                         | 4.72 ms: 1.17x faster                                                            |
| unpickle                   | 9.71 us                                                         | 8.52 us: 1.14x faster                                                            |
| regex_v8                   | 15.0 ms                                                         | 13.3 ms: 1.13x faster                                                            |
| regex_dna                  | 127 ms                                                          | 119 ms: 1.07x faster                                                             |
| unpickle_list              | 2.95 us                                                         | 2.85 us: 1.03x faster                                                            |
| pickle_dict                | 19.9 us                                                         | 19.8 us: 1.01x faster                                                            |
| coverage                   | 48.4 ms                                                         | 49.6 ms: 1.02x slower                                                            |
| pickle_list                | 3.37 us                                                         | 3.46 us: 1.03x slower                                                            |
| pickle                     | 7.79 us                                                         | 8.05 us: 1.03x slower                                                            |
| python_startup_no_site     | 19.1 ms                                                         | 19.8 ms: 1.04x slower                                                            |
| python_startup             | 22.4 ms                                                         | 26.6 ms: 1.19x slower                                                            |
| bench_mp_pool              | 75.4 ms                                                         | 94.5 ms: 1.25x slower                                                            |
| gc_traversal               | 1.44 ms                                                         | 2.15 ms: 1.49x slower                                                            |
| create_gc_cycles           | 652 us                                                          | 1.31 ms: 2.00x slower                                                            |
| Geometric mean             | (ref)                                                           | 1.46x faster                                                                     |
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (17) of results/bm-20250809-3.15.0a0-046a4e3/bm-20250809-pythonperf1_win32-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.455x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.45x
- 95% likely to have a speedup of 1.43x
- 99% likely to have a speedup of 1.41x

# Memory
- memory change: unknown