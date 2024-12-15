# Results vs. 3.12.0

- fork: python
- ref: 0ac40acec045c4ce780c
- machine: windows-x86
- commit hash: 0ac40ac
- commit date: 2024-12-14
- overall geometric mean: 1.076x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241214-pythonperf1_win32-x86-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 260 ms: 1.08x faster                                                            |
| docutils       | 1.98 sec                                                        | 1.92 sec: 1.04x faster                                                          |
| Geometric mean | (ref)                                                           | 1.06x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241214-pythonperf1_win32-x86-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_io_tg           | 677 ms                                                          | 460 ms: 1.47x faster                                                            |
| async_tree_io              | 693 ms                                                          | 483 ms: 1.44x faster                                                            |
| async_tree_memoization_tg  | 350 ms                                                          | 247 ms: 1.42x faster                                                            |
| async_tree_none_tg         | 278 ms                                                          | 198 ms: 1.40x faster                                                            |
| async_tree_none            | 298 ms                                                          | 227 ms: 1.31x faster                                                            |
| async_tree_memoization     | 364 ms                                                          | 279 ms: 1.31x faster                                                            |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 441 ms: 1.24x faster                                                            |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 473 ms: 1.19x faster                                                            |
| Geometric mean             | (ref)                                                           | 1.34x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241214-pythonperf1_win32-x86-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 76.7 ms                                                         | 56.2 ms: 1.36x faster                                                           |
| nbody          | 127 ms                                                          | 104 ms: 1.22x faster                                                            |
| pidigits       | 199 ms                                                          | 200 ms: 1.00x slower                                                            |
| Geometric mean | (ref)                                                           | 1.18x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241214-pythonperf1_win32-x86-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_effbot   | 2.04 ms                                                         | 1.57 ms: 1.30x faster                                                           |
| regex_dna      | 127 ms                                                          | 111 ms: 1.14x faster                                                            |
| regex_compile  | 129 ms                                                          | 114 ms: 1.14x faster                                                            |
| regex_v8       | 15.0 ms                                                         | 15.4 ms: 1.02x slower                                                           |
| Geometric mean | (ref)                                                           | 1.13x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241214-pythonperf1_win32-x86-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 2.20 sec                                                        | 1.75 sec: 1.26x faster                                                          |
| xml_etree_iterparse  | 77.6 ms                                                         | 66.4 ms: 1.17x faster                                                           |
| xml_etree_parse      | 113 ms                                                          | 108 ms: 1.05x faster                                                            |
| xml_etree_generate   | 72.1 ms                                                         | 71.0 ms: 1.02x faster                                                           |
| unpickle_pure_python | 210 us                                                          | 207 us: 1.01x faster                                                            |
| json_loads           | 20.4 us                                                         | 20.6 us: 1.01x slower                                                           |
| pickle_pure_python   | 286 us                                                          | 296 us: 1.03x slower                                                            |
| json_dumps           | 7.40 ms                                                         | 9.05 ms: 1.22x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.02x faster                                                                    |

Benchmark hidden because not significant (1): xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241214-pythonperf1_win32-x86-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 19.5 ms: 1.02x slower                                                           |
| python_startup         | 22.4 ms                                                         | 25.9 ms: 1.16x slower                                                           |
| Geometric mean         | (ref)                                                           | 1.09x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241214-pythonperf1_win32-x86-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 7.36 ms: 1.35x faster                                                           |
| django_template | 36.9 ms                                                         | 37.3 ms: 1.01x slower                                                           |
| Geometric mean  | (ref)                                                           | 1.16x faster                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241214-pythonperf1_win32-x86-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| deepcopy_memo              | 38.4 us                                                         | 23.4 us: 1.64x faster                                                           |
| async_tree_io_tg           | 677 ms                                                          | 460 ms: 1.47x faster                                                            |
| async_tree_io              | 693 ms                                                          | 483 ms: 1.44x faster                                                            |
| async_tree_memoization_tg  | 350 ms                                                          | 247 ms: 1.42x faster                                                            |
| async_tree_none_tg         | 278 ms                                                          | 198 ms: 1.40x faster                                                            |
| spectral_norm              | 104 ms                                                          | 75.4 ms: 1.38x faster                                                           |
| float                      | 76.7 ms                                                         | 56.2 ms: 1.36x faster                                                           |
| mako                       | 9.96 ms                                                         | 7.36 ms: 1.35x faster                                                           |
| scimark_sor                | 130 ms                                                          | 96.6 ms: 1.34x faster                                                           |
| deepcopy                   | 360 us                                                          | 271 us: 1.33x faster                                                            |
| async_tree_none            | 298 ms                                                          | 227 ms: 1.31x faster                                                            |
| async_tree_memoization     | 364 ms                                                          | 279 ms: 1.31x faster                                                            |
| regex_effbot               | 2.04 ms                                                         | 1.57 ms: 1.30x faster                                                           |
| logging_silent             | 101 ns                                                          | 78.4 ns: 1.29x faster                                                           |
| tomli_loads                | 2.20 sec                                                        | 1.75 sec: 1.26x faster                                                          |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 441 ms: 1.24x faster                                                            |
| coroutines                 | 20.9 ms                                                         | 17.2 ms: 1.22x faster                                                           |
| nbody                      | 127 ms                                                          | 104 ms: 1.22x faster                                                            |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 3.22 ms: 1.20x faster                                                           |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 473 ms: 1.19x faster                                                            |
| scimark_lu                 | 93.2 ms                                                         | 78.8 ms: 1.18x faster                                                           |
| xml_etree_iterparse        | 77.6 ms                                                         | 66.4 ms: 1.17x faster                                                           |
| logging_simple             | 9.75 us                                                         | 8.40 us: 1.16x faster                                                           |
| deepcopy_reduce            | 3.23 us                                                         | 2.79 us: 1.15x faster                                                           |
| dulwich_log                | 58.5 ms                                                         | 50.8 ms: 1.15x faster                                                           |
| logging_format             | 10.4 us                                                         | 9.07 us: 1.15x faster                                                           |
| regex_dna                  | 127 ms                                                          | 111 ms: 1.14x faster                                                            |
| regex_compile              | 129 ms                                                          | 114 ms: 1.14x faster                                                            |
| go                         | 137 ms                                                          | 121 ms: 1.13x faster                                                            |
| deltablue                  | 3.58 ms                                                         | 3.16 ms: 1.13x faster                                                           |
| scimark_fft                | 271 ms                                                          | 244 ms: 1.11x faster                                                            |
| pyflate                    | 424 ms                                                          | 384 ms: 1.10x faster                                                            |
| pathlib                    | 91.4 ms                                                         | 83.2 ms: 1.10x faster                                                           |
| chaos                      | 69.4 ms                                                         | 63.6 ms: 1.09x faster                                                           |
| sqlglot_parse              | 1.25 ms                                                         | 1.15 ms: 1.08x faster                                                           |
| 2to3                       | 280 ms                                                          | 260 ms: 1.08x faster                                                            |
| sympy_sum                  | 123 ms                                                          | 114 ms: 1.08x faster                                                            |
| sqlglot_transpile          | 1.53 ms                                                         | 1.43 ms: 1.07x faster                                                           |
| pycparser                  | 978 ms                                                          | 912 ms: 1.07x faster                                                            |
| sqlite_synth               | 2.07 us                                                         | 1.93 us: 1.07x faster                                                           |
| generators                 | 38.5 ms                                                         | 36.1 ms: 1.07x faster                                                           |
| bench_thread_pool          | 1.10 ms                                                         | 1.04 ms: 1.06x faster                                                           |
| xml_etree_parse            | 113 ms                                                          | 108 ms: 1.05x faster                                                            |
| fannkuch                   | 354 ms                                                          | 338 ms: 1.05x faster                                                            |
| comprehensions             | 19.2 us                                                         | 18.3 us: 1.05x faster                                                           |
| mdp                        | 1.91 sec                                                        | 1.84 sec: 1.04x faster                                                          |
| scimark_monte_carlo        | 66.4 ms                                                         | 64.1 ms: 1.04x faster                                                           |
| raytrace                   | 308 ms                                                          | 297 ms: 1.04x faster                                                            |
| docutils                   | 1.98 sec                                                        | 1.92 sec: 1.04x faster                                                          |
| sympy_str                  | 240 ms                                                          | 233 ms: 1.03x faster                                                            |
| crypto_pyaes               | 69.2 ms                                                         | 67.6 ms: 1.02x faster                                                           |
| async_generators           | 313 ms                                                          | 307 ms: 1.02x faster                                                            |
| xml_etree_generate         | 72.1 ms                                                         | 71.0 ms: 1.02x faster                                                           |
| unpickle_pure_python       | 210 us                                                          | 207 us: 1.01x faster                                                            |
| sympy_integrate            | 17.5 ms                                                         | 17.4 ms: 1.01x faster                                                           |
| pidigits                   | 199 ms                                                          | 200 ms: 1.00x slower                                                            |
| django_template            | 36.9 ms                                                         | 37.3 ms: 1.01x slower                                                           |
| pprint_pformat             | 1.50 sec                                                        | 1.51 sec: 1.01x slower                                                          |
| json_loads                 | 20.4 us                                                         | 20.6 us: 1.01x slower                                                           |
| sympy_expand               | 398 ms                                                          | 404 ms: 1.01x slower                                                            |
| richards                   | 41.3 ms                                                         | 42.0 ms: 1.02x slower                                                           |
| regex_v8                   | 15.0 ms                                                         | 15.4 ms: 1.02x slower                                                           |
| python_startup_no_site     | 19.1 ms                                                         | 19.5 ms: 1.02x slower                                                           |
| richards_super             | 46.5 ms                                                         | 47.6 ms: 1.02x slower                                                           |
| pprint_safe_repr           | 721 ms                                                          | 740 ms: 1.03x slower                                                            |
| meteor_contest             | 86.9 ms                                                         | 89.3 ms: 1.03x slower                                                           |
| pickle_pure_python         | 286 us                                                          | 296 us: 1.03x slower                                                            |
| nqueens                    | 93.7 ms                                                         | 97.4 ms: 1.04x slower                                                           |
| hexiom                     | 6.82 ms                                                         | 7.14 ms: 1.05x slower                                                           |
| sqlglot_optimize           | 48.5 ms                                                         | 51.0 ms: 1.05x slower                                                           |
| sqlglot_normalize          | 100 ms                                                          | 106 ms: 1.06x slower                                                            |
| json                       | 4.15 ms                                                         | 4.44 ms: 1.07x slower                                                           |
| coverage                   | 48.4 ms                                                         | 53.8 ms: 1.11x slower                                                           |
| bench_mp_pool              | 75.4 ms                                                         | 87.3 ms: 1.16x slower                                                           |
| python_startup             | 22.4 ms                                                         | 25.9 ms: 1.16x slower                                                           |
| json_dumps                 | 7.40 ms                                                         | 9.05 ms: 1.22x slower                                                           |
| mypy2                      | 584 ms                                                          | 726 ms: 1.24x slower                                                            |
| gc_traversal               | 1.44 ms                                                         | 1.81 ms: 1.26x slower                                                           |
| typing_runtime_protocols   | 126 us                                                          | 160 us: 1.27x slower                                                            |
| telco                      | 5.51 ms                                                         | 7.24 ms: 1.31x slower                                                           |
| create_gc_cycles           | 652 us                                                          | 1.05 ms: 1.61x slower                                                           |
| Geometric mean             | (ref)                                                           | 1.07x faster                                                                    |

Benchmark hidden because not significant (1): xml_etree_process
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20241214-3.14.0a2+-0ac40ac-JIT/bm-20241214-pythonperf1_win32-x86-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.076x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: unknown