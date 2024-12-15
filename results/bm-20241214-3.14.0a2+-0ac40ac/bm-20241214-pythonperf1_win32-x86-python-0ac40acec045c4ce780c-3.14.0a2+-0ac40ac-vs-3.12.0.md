# Results vs. 3.12.0

- fork: python
- ref: 0ac40acec045c4ce780c
- machine: windows-x86
- commit hash: 0ac40ac
- commit date: 2024-12-14
- overall geometric mean: 1.170x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.12x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241214-pythonperf1_win32-x86-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 240 ms: 1.17x faster                                                            |
| docutils       | 1.98 sec                                                        | 1.80 sec: 1.10x faster                                                          |
| Geometric mean | (ref)                                                           | 1.14x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241214-pythonperf1_win32-x86-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_io_tg           | 677 ms                                                          | 415 ms: 1.63x faster                                                            |
| async_tree_io              | 693 ms                                                          | 433 ms: 1.60x faster                                                            |
| async_tree_memoization_tg  | 350 ms                                                          | 227 ms: 1.55x faster                                                            |
| async_tree_none_tg         | 278 ms                                                          | 182 ms: 1.52x faster                                                            |
| async_tree_none            | 298 ms                                                          | 199 ms: 1.49x faster                                                            |
| async_tree_memoization     | 364 ms                                                          | 246 ms: 1.48x faster                                                            |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 442 ms: 1.28x faster                                                            |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 437 ms: 1.25x faster                                                            |
| Geometric mean             | (ref)                                                           | 1.47x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241214-pythonperf1_win32-x86-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 86.0 ms: 1.48x faster                                                           |
| float          | 76.7 ms                                                         | 58.2 ms: 1.32x faster                                                           |
| pidigits       | 199 ms                                                          | 202 ms: 1.01x slower                                                            |
| Geometric mean | (ref)                                                           | 1.24x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241214-pythonperf1_win32-x86-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 103 ms: 1.25x faster                                                            |
| regex_effbot   | 2.04 ms                                                         | 1.65 ms: 1.23x faster                                                           |
| regex_dna      | 127 ms                                                          | 126 ms: 1.01x faster                                                            |
| regex_v8       | 15.0 ms                                                         | 15.8 ms: 1.05x slower                                                           |
| Geometric mean | (ref)                                                           | 1.10x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241214-pythonperf1_win32-x86-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 2.20 sec                                                        | 1.68 sec: 1.30x faster                                                          |
| unpickle_pure_python | 210 us                                                          | 167 us: 1.26x faster                                                            |
| xml_etree_iterparse  | 77.6 ms                                                         | 66.6 ms: 1.17x faster                                                           |
| xml_etree_process    | 53.2 ms                                                         | 47.6 ms: 1.12x faster                                                           |
| xml_etree_generate   | 72.1 ms                                                         | 67.1 ms: 1.07x faster                                                           |
| pickle_pure_python   | 286 us                                                          | 274 us: 1.04x faster                                                            |
| xml_etree_parse      | 113 ms                                                          | 109 ms: 1.04x faster                                                            |
| json_dumps           | 7.40 ms                                                         | 8.69 ms: 1.17x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.09x faster                                                                    |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241214-pythonperf1_win32-x86-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 20.2 ms: 1.06x slower                                                           |
| python_startup         | 22.4 ms                                                         | 27.0 ms: 1.21x slower                                                           |
| Geometric mean         | (ref)                                                           | 1.13x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241214-pythonperf1_win32-x86-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 7.61 ms: 1.31x faster                                                           |
| django_template | 36.9 ms                                                         | 31.6 ms: 1.17x faster                                                           |
| Geometric mean  | (ref)                                                           | 1.23x faster                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241214-pythonperf1_win32-x86-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| deepcopy_memo              | 38.4 us                                                         | 20.7 us: 1.85x faster                                                           |
| async_tree_io_tg           | 677 ms                                                          | 415 ms: 1.63x faster                                                            |
| generators                 | 38.5 ms                                                         | 23.7 ms: 1.62x faster                                                           |
| async_tree_io              | 693 ms                                                          | 433 ms: 1.60x faster                                                            |
| deepcopy                   | 360 us                                                          | 229 us: 1.57x faster                                                            |
| async_tree_memoization_tg  | 350 ms                                                          | 227 ms: 1.55x faster                                                            |
| async_tree_none_tg         | 278 ms                                                          | 182 ms: 1.52x faster                                                            |
| spectral_norm              | 104 ms                                                          | 68.4 ms: 1.52x faster                                                           |
| async_tree_none            | 298 ms                                                          | 199 ms: 1.49x faster                                                            |
| nbody                      | 127 ms                                                          | 86.0 ms: 1.48x faster                                                           |
| async_tree_memoization     | 364 ms                                                          | 246 ms: 1.48x faster                                                            |
| go                         | 137 ms                                                          | 94.8 ms: 1.45x faster                                                           |
| logging_silent             | 101 ns                                                          | 70.2 ns: 1.44x faster                                                           |
| hexiom                     | 6.82 ms                                                         | 4.74 ms: 1.44x faster                                                           |
| comprehensions             | 19.2 us                                                         | 13.4 us: 1.43x faster                                                           |
| deltablue                  | 3.58 ms                                                         | 2.57 ms: 1.39x faster                                                           |
| scimark_lu                 | 93.2 ms                                                         | 67.6 ms: 1.38x faster                                                           |
| scimark_sor                | 130 ms                                                          | 95.1 ms: 1.37x faster                                                           |
| deepcopy_reduce            | 3.23 us                                                         | 2.40 us: 1.34x faster                                                           |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 2.90 ms: 1.33x faster                                                           |
| float                      | 76.7 ms                                                         | 58.2 ms: 1.32x faster                                                           |
| mako                       | 9.96 ms                                                         | 7.61 ms: 1.31x faster                                                           |
| tomli_loads                | 2.20 sec                                                        | 1.68 sec: 1.30x faster                                                          |
| chaos                      | 69.4 ms                                                         | 54.1 ms: 1.28x faster                                                           |
| raytrace                   | 308 ms                                                          | 241 ms: 1.28x faster                                                            |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 442 ms: 1.28x faster                                                            |
| scimark_monte_carlo        | 66.4 ms                                                         | 52.1 ms: 1.28x faster                                                           |
| coroutines                 | 20.9 ms                                                         | 16.5 ms: 1.27x faster                                                           |
| logging_simple             | 9.75 us                                                         | 7.71 us: 1.27x faster                                                           |
| unpickle_pure_python       | 210 us                                                          | 167 us: 1.26x faster                                                            |
| nqueens                    | 93.7 ms                                                         | 74.9 ms: 1.25x faster                                                           |
| regex_compile              | 129 ms                                                          | 103 ms: 1.25x faster                                                            |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 437 ms: 1.25x faster                                                            |
| regex_effbot               | 2.04 ms                                                         | 1.65 ms: 1.23x faster                                                           |
| logging_format             | 10.4 us                                                         | 8.46 us: 1.23x faster                                                           |
| pyflate                    | 424 ms                                                          | 345 ms: 1.23x faster                                                            |
| sqlglot_parse              | 1.25 ms                                                         | 1.04 ms: 1.21x faster                                                           |
| fannkuch                   | 354 ms                                                          | 295 ms: 1.20x faster                                                            |
| sqlglot_transpile          | 1.53 ms                                                         | 1.28 ms: 1.20x faster                                                           |
| scimark_fft                | 271 ms                                                          | 227 ms: 1.20x faster                                                            |
| crypto_pyaes               | 69.2 ms                                                         | 58.8 ms: 1.18x faster                                                           |
| sqlglot_optimize           | 48.5 ms                                                         | 41.3 ms: 1.17x faster                                                           |
| dulwich_log                | 58.5 ms                                                         | 50.0 ms: 1.17x faster                                                           |
| 2to3                       | 280 ms                                                          | 240 ms: 1.17x faster                                                            |
| django_template            | 36.9 ms                                                         | 31.6 ms: 1.17x faster                                                           |
| xml_etree_iterparse        | 77.6 ms                                                         | 66.6 ms: 1.17x faster                                                           |
| pycparser                  | 978 ms                                                          | 840 ms: 1.16x faster                                                            |
| sympy_sum                  | 123 ms                                                          | 106 ms: 1.16x faster                                                            |
| sympy_integrate            | 17.5 ms                                                         | 15.1 ms: 1.16x faster                                                           |
| pprint_safe_repr           | 721 ms                                                          | 636 ms: 1.13x faster                                                            |
| sympy_str                  | 240 ms                                                          | 212 ms: 1.13x faster                                                            |
| pprint_pformat             | 1.50 sec                                                        | 1.33 sec: 1.13x faster                                                          |
| xml_etree_process          | 53.2 ms                                                         | 47.6 ms: 1.12x faster                                                           |
| mdp                        | 1.91 sec                                                        | 1.71 sec: 1.12x faster                                                          |
| bench_thread_pool          | 1.10 ms                                                         | 995 us: 1.11x faster                                                            |
| pathlib                    | 91.4 ms                                                         | 82.6 ms: 1.11x faster                                                           |
| docutils                   | 1.98 sec                                                        | 1.80 sec: 1.10x faster                                                          |
| async_generators           | 313 ms                                                          | 287 ms: 1.09x faster                                                            |
| meteor_contest             | 86.9 ms                                                         | 79.6 ms: 1.09x faster                                                           |
| xml_etree_generate         | 72.1 ms                                                         | 67.1 ms: 1.07x faster                                                           |
| sqlite_synth               | 2.07 us                                                         | 1.94 us: 1.07x faster                                                           |
| richards                   | 41.3 ms                                                         | 38.8 ms: 1.06x faster                                                           |
| sympy_expand               | 398 ms                                                          | 374 ms: 1.06x faster                                                            |
| richards_super             | 46.5 ms                                                         | 43.9 ms: 1.06x faster                                                           |
| pickle_pure_python         | 286 us                                                          | 274 us: 1.04x faster                                                            |
| xml_etree_parse            | 113 ms                                                          | 109 ms: 1.04x faster                                                            |
| regex_dna                  | 127 ms                                                          | 126 ms: 1.01x faster                                                            |
| pidigits                   | 199 ms                                                          | 202 ms: 1.01x slower                                                            |
| regex_v8                   | 15.0 ms                                                         | 15.8 ms: 1.05x slower                                                           |
| python_startup_no_site     | 19.1 ms                                                         | 20.2 ms: 1.06x slower                                                           |
| coverage                   | 48.4 ms                                                         | 52.5 ms: 1.08x slower                                                           |
| typing_runtime_protocols   | 126 us                                                          | 139 us: 1.10x slower                                                            |
| mypy2                      | 584 ms                                                          | 681 ms: 1.17x slower                                                            |
| json_dumps                 | 7.40 ms                                                         | 8.69 ms: 1.17x slower                                                           |
| telco                      | 5.51 ms                                                         | 6.51 ms: 1.18x slower                                                           |
| python_startup             | 22.4 ms                                                         | 27.0 ms: 1.21x slower                                                           |
| gc_traversal               | 1.44 ms                                                         | 1.78 ms: 1.23x slower                                                           |
| bench_mp_pool              | 75.4 ms                                                         | 93.0 ms: 1.23x slower                                                           |
| create_gc_cycles           | 652 us                                                          | 1.06 ms: 1.62x slower                                                           |
| sqlglot_normalize          | 100 ms                                                          | 216 ms: 2.15x slower                                                            |
| Geometric mean             | (ref)                                                           | 1.17x faster                                                                    |

Benchmark hidden because not significant (2): json, json_loads
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20241214-3.14.0a2+-0ac40ac/bm-20241214-pythonperf1_win32-x86-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.170x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.15x
- 95% likely to have a speedup of 1.14x
- 99% likely to have a speedup of 1.12x

# Memory
- memory change: unknown