# Results vs. 3.12.0

- fork: python
- ref: fba5dded6df3c2b19435
- machine: windows-amd64
- commit hash: fba5dde
- commit date: 2025-06-17
- overall geometric mean: 1.010x slower
- HPT reliability: 66.56%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250617-pythonperf1_win32-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 291 ms: 1.04x slower                                                             |
| docutils       | 1.98 sec                                                        | 2.08 sec: 1.05x slower                                                           |
| Geometric mean | (ref)                                                           | 1.04x slower                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250617-pythonperf1_win32-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed    | 564 ms                                                          | 442 ms: 1.28x faster                                                             |
| async_tree_io              | 693 ms                                                          | 548 ms: 1.26x faster                                                             |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 439 ms: 1.24x faster                                                             |
| async_tree_memoization     | 364 ms                                                          | 295 ms: 1.23x faster                                                             |
| async_tree_none            | 298 ms                                                          | 243 ms: 1.23x faster                                                             |
| async_tree_memoization_tg  | 350 ms                                                          | 291 ms: 1.20x faster                                                             |
| async_tree_io_tg           | 677 ms                                                          | 564 ms: 1.20x faster                                                             |
| async_tree_none_tg         | 278 ms                                                          | 233 ms: 1.19x faster                                                             |
| Geometric mean             | (ref)                                                           | 1.23x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250617-pythonperf1_win32-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pidigits       | 199 ms                                                          | 147 ms: 1.36x faster                                                             |
| nbody          | 127 ms                                                          | 99.3 ms: 1.28x faster                                                            |
| float          | 76.7 ms                                                         | 75.5 ms: 1.02x faster                                                            |
| Geometric mean | (ref)                                                           | 1.21x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250617-pythonperf1_win32-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_effbot   | 2.04 ms                                                         | 1.72 ms: 1.18x faster                                                            |
| regex_dna      | 127 ms                                                          | 117 ms: 1.09x faster                                                             |
| regex_compile  | 129 ms                                                          | 122 ms: 1.06x faster                                                             |
| regex_v8       | 15.0 ms                                                         | 17.1 ms: 1.13x slower                                                            |
| Geometric mean | (ref)                                                           | 1.05x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250617-pythonperf1_win32-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| tomli_loads          | 2.20 sec                                                        | 2.02 sec: 1.09x faster                                                           |
| xml_etree_parse      | 113 ms                                                          | 109 ms: 1.04x faster                                                             |
| json_loads           | 20.4 us                                                         | 20.8 us: 1.02x slower                                                            |
| unpickle_list        | 2.95 us                                                         | 3.06 us: 1.04x slower                                                            |
| pickle_list          | 3.37 us                                                         | 3.79 us: 1.13x slower                                                            |
| pickle_dict          | 19.9 us                                                         | 22.7 us: 1.14x slower                                                            |
| json_dumps           | 7.40 ms                                                         | 8.53 ms: 1.15x slower                                                            |
| unpickle             | 9.71 us                                                         | 11.5 us: 1.18x slower                                                            |
| xml_etree_iterparse  | 77.6 ms                                                         | 92.2 ms: 1.19x slower                                                            |
| xml_etree_process    | 53.2 ms                                                         | 64.0 ms: 1.20x slower                                                            |
| pickle               | 7.79 us                                                         | 9.57 us: 1.23x slower                                                            |
| xml_etree_generate   | 72.1 ms                                                         | 89.1 ms: 1.23x slower                                                            |
| pickle_pure_python   | 286 us                                                          | 358 us: 1.25x slower                                                             |
| unpickle_pure_python | 210 us                                                          | 275 us: 1.31x slower                                                             |
| Geometric mean       | (ref)                                                           | 1.13x slower                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250617-pythonperf1_win32-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 20.2 ms: 1.06x slower                                                            |
| python_startup         | 22.4 ms                                                         | 27.4 ms: 1.22x slower                                                            |
| Geometric mean         | (ref)                                                           | 1.14x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250617-pythonperf1_win32-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| django_template | 36.9 ms                                                         | 36.3 ms: 1.02x faster                                                            |
| mako            | 9.96 ms                                                         | 12.4 ms: 1.24x slower                                                            |
| Geometric mean  | (ref)                                                           | 1.10x slower                                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250617-pythonperf1_win32-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| asyncio_tcp_ssl            | 17.7 sec                                                        | 1.48 sec: 11.93x faster                                                          |
| pathlib                    | 91.4 ms                                                         | 34.2 ms: 2.68x faster                                                            |
| mdp                        | 1.91 sec                                                        | 1.15 sec: 1.67x faster                                                           |
| deepcopy                   | 360 us                                                          | 262 us: 1.37x faster                                                             |
| pidigits                   | 199 ms                                                          | 147 ms: 1.36x faster                                                             |
| nbody                      | 127 ms                                                          | 99.3 ms: 1.28x faster                                                            |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 442 ms: 1.28x faster                                                             |
| async_tree_io              | 693 ms                                                          | 548 ms: 1.26x faster                                                             |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 439 ms: 1.24x faster                                                             |
| async_tree_memoization     | 364 ms                                                          | 295 ms: 1.23x faster                                                             |
| async_tree_none            | 298 ms                                                          | 243 ms: 1.23x faster                                                             |
| async_tree_memoization_tg  | 350 ms                                                          | 291 ms: 1.20x faster                                                             |
| async_tree_io_tg           | 677 ms                                                          | 564 ms: 1.20x faster                                                             |
| deepcopy_reduce            | 3.23 us                                                         | 2.69 us: 1.20x faster                                                            |
| async_tree_none_tg         | 278 ms                                                          | 233 ms: 1.19x faster                                                             |
| asyncio_tcp                | 662 ms                                                          | 560 ms: 1.18x faster                                                             |
| regex_effbot               | 2.04 ms                                                         | 1.72 ms: 1.18x faster                                                            |
| deepcopy_memo              | 38.4 us                                                         | 33.1 us: 1.16x faster                                                            |
| dulwich_log                | 58.5 ms                                                         | 50.9 ms: 1.15x faster                                                            |
| sqlite_synth               | 2.07 us                                                         | 1.86 us: 1.12x faster                                                            |
| bench_thread_pool          | 1.10 ms                                                         | 993 us: 1.11x faster                                                             |
| regex_dna                  | 127 ms                                                          | 117 ms: 1.09x faster                                                             |
| tomli_loads                | 2.20 sec                                                        | 2.02 sec: 1.09x faster                                                           |
| chaos                      | 69.4 ms                                                         | 63.9 ms: 1.09x faster                                                            |
| sympy_sum                  | 123 ms                                                          | 115 ms: 1.07x faster                                                             |
| logging_format             | 10.4 us                                                         | 9.72 us: 1.07x faster                                                            |
| sympy_integrate            | 17.5 ms                                                         | 16.4 ms: 1.07x faster                                                            |
| regex_compile              | 129 ms                                                          | 122 ms: 1.06x faster                                                             |
| logging_simple             | 9.75 us                                                         | 9.21 us: 1.06x faster                                                            |
| generators                 | 38.5 ms                                                         | 36.5 ms: 1.05x faster                                                            |
| go                         | 137 ms                                                          | 132 ms: 1.04x faster                                                             |
| xml_etree_parse            | 113 ms                                                          | 109 ms: 1.04x faster                                                             |
| sympy_str                  | 240 ms                                                          | 232 ms: 1.03x faster                                                             |
| json                       | 4.15 ms                                                         | 4.05 ms: 1.03x faster                                                            |
| raytrace                   | 308 ms                                                          | 301 ms: 1.02x faster                                                             |
| nqueens                    | 93.7 ms                                                         | 91.5 ms: 1.02x faster                                                            |
| scimark_fft                | 271 ms                                                          | 266 ms: 1.02x faster                                                             |
| django_template            | 36.9 ms                                                         | 36.3 ms: 1.02x faster                                                            |
| float                      | 76.7 ms                                                         | 75.5 ms: 1.02x faster                                                            |
| scimark_sor                | 130 ms                                                          | 129 ms: 1.01x faster                                                             |
| sympy_expand               | 398 ms                                                          | 395 ms: 1.01x faster                                                             |
| comprehensions             | 19.2 us                                                         | 19.3 us: 1.01x slower                                                            |
| json_loads                 | 20.4 us                                                         | 20.8 us: 1.02x slower                                                            |
| unpickle_list              | 2.95 us                                                         | 3.06 us: 1.04x slower                                                            |
| 2to3                       | 280 ms                                                          | 291 ms: 1.04x slower                                                             |
| docutils                   | 1.98 sec                                                        | 2.08 sec: 1.05x slower                                                           |
| async_generators           | 313 ms                                                          | 332 ms: 1.06x slower                                                             |
| meteor_contest             | 86.9 ms                                                         | 92.2 ms: 1.06x slower                                                            |
| python_startup_no_site     | 19.1 ms                                                         | 20.2 ms: 1.06x slower                                                            |
| pyflate                    | 424 ms                                                          | 451 ms: 1.06x slower                                                             |
| spectral_norm              | 104 ms                                                          | 111 ms: 1.07x slower                                                             |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 4.15 ms: 1.08x slower                                                            |
| scimark_monte_carlo        | 66.4 ms                                                         | 71.7 ms: 1.08x slower                                                            |
| hexiom                     | 6.82 ms                                                         | 7.40 ms: 1.09x slower                                                            |
| pickle_list                | 3.37 us                                                         | 3.79 us: 1.13x slower                                                            |
| telco                      | 5.51 ms                                                         | 6.25 ms: 1.13x slower                                                            |
| regex_v8                   | 15.0 ms                                                         | 17.1 ms: 1.13x slower                                                            |
| pickle_dict                | 19.9 us                                                         | 22.7 us: 1.14x slower                                                            |
| crypto_pyaes               | 69.2 ms                                                         | 79.5 ms: 1.15x slower                                                            |
| fannkuch                   | 354 ms                                                          | 406 ms: 1.15x slower                                                             |
| json_dumps                 | 7.40 ms                                                         | 8.53 ms: 1.15x slower                                                            |
| pprint_pformat             | 1.50 sec                                                        | 1.74 sec: 1.16x slower                                                           |
| unpickle                   | 9.71 us                                                         | 11.5 us: 1.18x slower                                                            |
| coroutines                 | 20.9 ms                                                         | 24.7 ms: 1.18x slower                                                            |
| xml_etree_iterparse        | 77.6 ms                                                         | 92.2 ms: 1.19x slower                                                            |
| pprint_safe_repr           | 721 ms                                                          | 856 ms: 1.19x slower                                                             |
| deltablue                  | 3.58 ms                                                         | 4.29 ms: 1.20x slower                                                            |
| xml_etree_process          | 53.2 ms                                                         | 64.0 ms: 1.20x slower                                                            |
| typing_runtime_protocols   | 126 us                                                          | 154 us: 1.22x slower                                                             |
| richards                   | 41.3 ms                                                         | 50.6 ms: 1.22x slower                                                            |
| python_startup             | 22.4 ms                                                         | 27.4 ms: 1.22x slower                                                            |
| pickle                     | 7.79 us                                                         | 9.57 us: 1.23x slower                                                            |
| richards_super             | 46.5 ms                                                         | 57.3 ms: 1.23x slower                                                            |
| xml_etree_generate         | 72.1 ms                                                         | 89.1 ms: 1.23x slower                                                            |
| mako                       | 9.96 ms                                                         | 12.4 ms: 1.24x slower                                                            |
| unpack_sequence            | 62.5 ns                                                         | 77.6 ns: 1.24x slower                                                            |
| pickle_pure_python         | 286 us                                                          | 358 us: 1.25x slower                                                             |
| scimark_lu                 | 93.2 ms                                                         | 119 ms: 1.28x slower                                                             |
| coverage                   | 48.4 ms                                                         | 62.2 ms: 1.29x slower                                                            |
| unpickle_pure_python       | 210 us                                                          | 275 us: 1.31x slower                                                             |
| bench_mp_pool              | 75.4 ms                                                         | 105 ms: 1.39x slower                                                             |
| gc_traversal               | 1.44 ms                                                         | 2.99 ms: 2.08x slower                                                            |
| create_gc_cycles           | 652 us                                                          | 1.47 ms: 2.26x slower                                                            |
| logging_silent             | 101 ns                                                          | 495 ns: 4.90x slower                                                             |
| Geometric mean             | (ref)                                                           | 1.01x slower                                                                     |

Benchmark hidden because not significant (1): pycparser
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (17) of results/bm-20250617-3.15.0a0-fba5dde/bm-20250617-pythonperf1_win32-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.010x slower

# HPT report

- Reliability score: 66.56% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown