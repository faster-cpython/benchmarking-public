# Results vs. 3.12.0

- fork: python
- ref: cebae977a63f32c3c03d
- machine: windows-amd64
- commit hash: cebae97
- commit date: 2025-06-01
- overall geometric mean: 1.044x slower
- HPT reliability: 72.64%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250601-pythonperf1_win32-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 294 ms: 1.05x slower                                                             |
| docutils       | 1.98 sec                                                        | 2.07 sec: 1.04x slower                                                           |
| Geometric mean | (ref)                                                           | 1.05x slower                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250601-pythonperf1_win32-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed    | 564 ms                                                          | 447 ms: 1.26x faster                                                             |
| async_tree_io              | 693 ms                                                          | 550 ms: 1.26x faster                                                             |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 441 ms: 1.24x faster                                                             |
| async_tree_memoization     | 364 ms                                                          | 298 ms: 1.22x faster                                                             |
| async_tree_none            | 298 ms                                                          | 244 ms: 1.22x faster                                                             |
| async_tree_io_tg           | 677 ms                                                          | 560 ms: 1.21x faster                                                             |
| async_tree_memoization_tg  | 350 ms                                                          | 292 ms: 1.20x faster                                                             |
| async_tree_none_tg         | 278 ms                                                          | 239 ms: 1.16x faster                                                             |
| Geometric mean             | (ref)                                                           | 1.22x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250601-pythonperf1_win32-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pidigits       | 199 ms                                                          | 145 ms: 1.37x faster                                                             |
| nbody          | 127 ms                                                          | 106 ms: 1.20x faster                                                             |
| float          | 76.7 ms                                                         | 77.3 ms: 1.01x slower                                                            |
| Geometric mean | (ref)                                                           | 1.18x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250601-pythonperf1_win32-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_effbot   | 2.04 ms                                                         | 1.79 ms: 1.14x faster                                                            |
| regex_dna      | 127 ms                                                          | 117 ms: 1.08x faster                                                             |
| regex_compile  | 129 ms                                                          | 123 ms: 1.05x faster                                                             |
| regex_v8       | 15.0 ms                                                         | 16.6 ms: 1.10x slower                                                            |
| Geometric mean | (ref)                                                           | 1.04x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250601-pythonperf1_win32-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| xml_etree_parse      | 113 ms                                                          | 108 ms: 1.05x faster                                                             |
| tomli_loads          | 2.20 sec                                                        | 2.09 sec: 1.05x faster                                                           |
| json_loads           | 20.4 us                                                         | 20.5 us: 1.01x slower                                                            |
| unpickle_list        | 2.95 us                                                         | 3.15 us: 1.07x slower                                                            |
| pickle_dict          | 19.9 us                                                         | 22.5 us: 1.13x slower                                                            |
| xml_etree_iterparse  | 77.6 ms                                                         | 89.3 ms: 1.15x slower                                                            |
| unpickle             | 9.71 us                                                         | 11.3 us: 1.17x slower                                                            |
| pickle_list          | 3.37 us                                                         | 3.96 us: 1.18x slower                                                            |
| pickle               | 7.79 us                                                         | 9.48 us: 1.22x slower                                                            |
| json_dumps           | 7.40 ms                                                         | 9.00 ms: 1.22x slower                                                            |
| xml_etree_process    | 53.2 ms                                                         | 64.9 ms: 1.22x slower                                                            |
| xml_etree_generate   | 72.1 ms                                                         | 89.7 ms: 1.24x slower                                                            |
| pickle_pure_python   | 286 us                                                          | 358 us: 1.25x slower                                                             |
| unpickle_pure_python | 210 us                                                          | 275 us: 1.31x slower                                                             |
| Geometric mean       | (ref)                                                           | 1.14x slower                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250601-pythonperf1_win32-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 20.1 ms: 1.05x slower                                                            |
| python_startup         | 22.4 ms                                                         | 27.4 ms: 1.22x slower                                                            |
| Geometric mean         | (ref)                                                           | 1.14x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250601-pythonperf1_win32-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| django_template | 36.9 ms                                                         | 37.2 ms: 1.01x slower                                                            |
| mako            | 9.96 ms                                                         | 12.6 ms: 1.26x slower                                                            |
| Geometric mean  | (ref)                                                           | 1.13x slower                                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250601-pythonperf1_win32-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| asyncio_tcp_ssl            | 17.7 sec                                                        | 1.36 sec: 12.98x faster                                                          |
| pathlib                    | 91.4 ms                                                         | 34.1 ms: 2.68x faster                                                            |
| mdp                        | 1.91 sec                                                        | 1.18 sec: 1.61x faster                                                           |
| asyncio_tcp                | 662 ms                                                          | 451 ms: 1.47x faster                                                             |
| pidigits                   | 199 ms                                                          | 145 ms: 1.37x faster                                                             |
| deepcopy                   | 360 us                                                          | 265 us: 1.36x faster                                                             |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 447 ms: 1.26x faster                                                             |
| async_tree_io              | 693 ms                                                          | 550 ms: 1.26x faster                                                             |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 441 ms: 1.24x faster                                                             |
| async_tree_memoization     | 364 ms                                                          | 298 ms: 1.22x faster                                                             |
| async_tree_none            | 298 ms                                                          | 244 ms: 1.22x faster                                                             |
| async_tree_io_tg           | 677 ms                                                          | 560 ms: 1.21x faster                                                             |
| nbody                      | 127 ms                                                          | 106 ms: 1.20x faster                                                             |
| async_tree_memoization_tg  | 350 ms                                                          | 292 ms: 1.20x faster                                                             |
| deepcopy_reduce            | 3.23 us                                                         | 2.74 us: 1.18x faster                                                            |
| async_tree_none_tg         | 278 ms                                                          | 239 ms: 1.16x faster                                                             |
| deepcopy_memo              | 38.4 us                                                         | 33.3 us: 1.15x faster                                                            |
| regex_effbot               | 2.04 ms                                                         | 1.79 ms: 1.14x faster                                                            |
| dulwich_log                | 58.5 ms                                                         | 51.4 ms: 1.14x faster                                                            |
| generators                 | 38.5 ms                                                         | 34.5 ms: 1.12x faster                                                            |
| bench_thread_pool          | 1.10 ms                                                         | 1.00 ms: 1.10x faster                                                            |
| regex_dna                  | 127 ms                                                          | 117 ms: 1.08x faster                                                             |
| sqlite_synth               | 2.07 us                                                         | 1.93 us: 1.07x faster                                                            |
| sympy_sum                  | 123 ms                                                          | 116 ms: 1.06x faster                                                             |
| chaos                      | 69.4 ms                                                         | 65.5 ms: 1.06x faster                                                            |
| logging_format             | 10.4 us                                                         | 9.83 us: 1.06x faster                                                            |
| sympy_integrate            | 17.5 ms                                                         | 16.6 ms: 1.06x faster                                                            |
| json                       | 4.15 ms                                                         | 3.94 ms: 1.05x faster                                                            |
| xml_etree_parse            | 113 ms                                                          | 108 ms: 1.05x faster                                                             |
| tomli_loads                | 2.20 sec                                                        | 2.09 sec: 1.05x faster                                                           |
| regex_compile              | 129 ms                                                          | 123 ms: 1.05x faster                                                             |
| logging_simple             | 9.75 us                                                         | 9.32 us: 1.05x faster                                                            |
| sympy_str                  | 240 ms                                                          | 233 ms: 1.03x faster                                                             |
| go                         | 137 ms                                                          | 134 ms: 1.02x faster                                                             |
| raytrace                   | 308 ms                                                          | 301 ms: 1.02x faster                                                             |
| sympy_expand               | 398 ms                                                          | 400 ms: 1.01x slower                                                             |
| json_loads                 | 20.4 us                                                         | 20.5 us: 1.01x slower                                                            |
| django_template            | 36.9 ms                                                         | 37.2 ms: 1.01x slower                                                            |
| float                      | 76.7 ms                                                         | 77.3 ms: 1.01x slower                                                            |
| scimark_fft                | 271 ms                                                          | 275 ms: 1.01x slower                                                             |
| comprehensions             | 19.2 us                                                         | 19.6 us: 1.02x slower                                                            |
| scimark_sor                | 130 ms                                                          | 133 ms: 1.02x slower                                                             |
| docutils                   | 1.98 sec                                                        | 2.07 sec: 1.04x slower                                                           |
| 2to3                       | 280 ms                                                          | 294 ms: 1.05x slower                                                             |
| python_startup_no_site     | 19.1 ms                                                         | 20.1 ms: 1.05x slower                                                            |
| pyflate                    | 424 ms                                                          | 451 ms: 1.07x slower                                                             |
| unpickle_list              | 2.95 us                                                         | 3.15 us: 1.07x slower                                                            |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 4.15 ms: 1.08x slower                                                            |
| hexiom                     | 6.82 ms                                                         | 7.37 ms: 1.08x slower                                                            |
| meteor_contest             | 86.9 ms                                                         | 94.3 ms: 1.09x slower                                                            |
| async_generators           | 313 ms                                                          | 343 ms: 1.09x slower                                                             |
| scimark_monte_carlo        | 66.4 ms                                                         | 72.7 ms: 1.09x slower                                                            |
| regex_v8                   | 15.0 ms                                                         | 16.6 ms: 1.10x slower                                                            |
| pickle_dict                | 19.9 us                                                         | 22.5 us: 1.13x slower                                                            |
| spectral_norm              | 104 ms                                                          | 117 ms: 1.13x slower                                                             |
| telco                      | 5.51 ms                                                         | 6.26 ms: 1.14x slower                                                            |
| crypto_pyaes               | 69.2 ms                                                         | 79.3 ms: 1.15x slower                                                            |
| xml_etree_iterparse        | 77.6 ms                                                         | 89.3 ms: 1.15x slower                                                            |
| pprint_pformat             | 1.50 sec                                                        | 1.74 sec: 1.16x slower                                                           |
| unpickle                   | 9.71 us                                                         | 11.3 us: 1.17x slower                                                            |
| pickle_list                | 3.37 us                                                         | 3.96 us: 1.18x slower                                                            |
| pprint_safe_repr           | 721 ms                                                          | 849 ms: 1.18x slower                                                             |
| fannkuch                   | 354 ms                                                          | 420 ms: 1.19x slower                                                             |
| deltablue                  | 3.58 ms                                                         | 4.32 ms: 1.21x slower                                                            |
| pickle                     | 7.79 us                                                         | 9.48 us: 1.22x slower                                                            |
| json_dumps                 | 7.40 ms                                                         | 9.00 ms: 1.22x slower                                                            |
| xml_etree_process          | 53.2 ms                                                         | 64.9 ms: 1.22x slower                                                            |
| typing_runtime_protocols   | 126 us                                                          | 155 us: 1.22x slower                                                             |
| python_startup             | 22.4 ms                                                         | 27.4 ms: 1.22x slower                                                            |
| coroutines                 | 20.9 ms                                                         | 25.6 ms: 1.23x slower                                                            |
| richards                   | 41.3 ms                                                         | 50.8 ms: 1.23x slower                                                            |
| richards_super             | 46.5 ms                                                         | 57.3 ms: 1.23x slower                                                            |
| xml_etree_generate         | 72.1 ms                                                         | 89.7 ms: 1.24x slower                                                            |
| pickle_pure_python         | 286 us                                                          | 358 us: 1.25x slower                                                             |
| scimark_lu                 | 93.2 ms                                                         | 118 ms: 1.26x slower                                                             |
| mako                       | 9.96 ms                                                         | 12.6 ms: 1.26x slower                                                            |
| unpack_sequence            | 62.5 ns                                                         | 81.7 ns: 1.31x slower                                                            |
| unpickle_pure_python       | 210 us                                                          | 275 us: 1.31x slower                                                             |
| bench_mp_pool              | 75.4 ms                                                         | 103 ms: 1.37x slower                                                             |
| gc_traversal               | 1.44 ms                                                         | 2.88 ms: 2.00x slower                                                            |
| create_gc_cycles           | 652 us                                                          | 1.47 ms: 2.25x slower                                                            |
| logging_silent             | 101 ns                                                          | 487 ns: 4.82x slower                                                             |
| coverage                   | 48.4 ms                                                         | 475 ms: 9.81x slower                                                             |
| Geometric mean             | (ref)                                                           | 1.04x slower                                                                     |

Benchmark hidden because not significant (2): pycparser, nqueens
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (17) of results/bm-20250601-3.15.0a0-cebae97/bm-20250601-pythonperf1_win32-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.044x slower

# HPT report

- Reliability score: 72.64% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown