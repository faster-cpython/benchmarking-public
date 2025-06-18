# Results vs. 3.12.0

- fork: python
- ref: fba5dded6df3c2b19435
- machine: windows-amd64
- commit hash: fba5dde
- commit date: 2025-06-17
- overall geometric mean: 1.212x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.19x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250617-pythonperf1_win32-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 338 ms: 1.21x slower                                                             |
| docutils       | 1.98 sec                                                        | 4.22 sec: 2.13x slower                                                           |
| Geometric mean | (ref)                                                           | 1.60x slower                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250617-pythonperf1_win32-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_io_tg           | 677 ms                                                          | 555 ms: 1.22x faster                                                             |
| async_tree_io              | 693 ms                                                          | 580 ms: 1.19x faster                                                             |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 460 ms: 1.19x faster                                                             |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 484 ms: 1.16x faster                                                             |
| async_tree_none_tg         | 278 ms                                                          | 248 ms: 1.12x faster                                                             |
| async_tree_memoization_tg  | 350 ms                                                          | 313 ms: 1.12x faster                                                             |
| async_tree_none            | 298 ms                                                          | 275 ms: 1.08x faster                                                             |
| async_tree_memoization     | 364 ms                                                          | 336 ms: 1.08x faster                                                             |
| Geometric mean             | (ref)                                                           | 1.15x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250617-pythonperf1_win32-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pidigits       | 199 ms                                                          | 140 ms: 1.42x faster                                                             |
| float          | 76.7 ms                                                         | 97.7 ms: 1.27x slower                                                            |
| nbody          | 127 ms                                                          | 184 ms: 1.45x slower                                                             |
| Geometric mean | (ref)                                                           | 1.09x slower                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250617-pythonperf1_win32-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_dna      | 127 ms                                                          | 113 ms: 1.12x faster                                                             |
| regex_effbot   | 2.04 ms                                                         | 1.83 ms: 1.12x faster                                                            |
| regex_v8       | 15.0 ms                                                         | 16.9 ms: 1.12x slower                                                            |
| regex_compile  | 129 ms                                                          | 161 ms: 1.24x slower                                                             |
| Geometric mean | (ref)                                                           | 1.03x slower                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250617-pythonperf1_win32-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pickle_dict          | 19.9 us                                                         | 22.0 us: 1.10x slower                                                            |
| pickle_list          | 3.37 us                                                         | 3.81 us: 1.13x slower                                                            |
| json_loads           | 20.4 us                                                         | 23.1 us: 1.13x slower                                                            |
| xml_etree_iterparse  | 77.6 ms                                                         | 92.3 ms: 1.19x slower                                                            |
| unpickle_list        | 2.95 us                                                         | 3.55 us: 1.20x slower                                                            |
| unpickle             | 9.71 us                                                         | 12.0 us: 1.23x slower                                                            |
| pickle               | 7.79 us                                                         | 9.85 us: 1.26x slower                                                            |
| json_dumps           | 7.40 ms                                                         | 9.52 ms: 1.29x slower                                                            |
| xml_etree_generate   | 72.1 ms                                                         | 107 ms: 1.49x slower                                                             |
| xml_etree_process    | 53.2 ms                                                         | 79.9 ms: 1.50x slower                                                            |
| pickle_pure_python   | 286 us                                                          | 451 us: 1.58x slower                                                             |
| unpickle_pure_python | 210 us                                                          | 356 us: 1.70x slower                                                             |
| tomli_loads          | 2.20 sec                                                        | 5.05 sec: 2.30x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.33x slower                                                                     |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250617-pythonperf1_win32-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 20.4 ms: 1.07x slower                                                            |
| python_startup         | 22.4 ms                                                         | 27.7 ms: 1.24x slower                                                            |
| Geometric mean         | (ref)                                                           | 1.15x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250617-pythonperf1_win32-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| django_template | 36.9 ms                                                         | 45.9 ms: 1.24x slower                                                            |
| mako            | 9.96 ms                                                         | 16.4 ms: 1.65x slower                                                            |
| Geometric mean  | (ref)                                                           | 1.43x slower                                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250617-pythonperf1_win32-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| asyncio_tcp_ssl            | 17.7 sec                                                        | 2.71 sec: 6.51x faster                                                           |
| pathlib                    | 91.4 ms                                                         | 35.5 ms: 2.57x faster                                                            |
| pidigits                   | 199 ms                                                          | 140 ms: 1.42x faster                                                             |
| async_tree_io_tg           | 677 ms                                                          | 555 ms: 1.22x faster                                                             |
| sqlite_synth               | 2.07 us                                                         | 1.71 us: 1.21x faster                                                            |
| async_tree_io              | 693 ms                                                          | 580 ms: 1.19x faster                                                             |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 460 ms: 1.19x faster                                                             |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 484 ms: 1.16x faster                                                             |
| async_tree_none_tg         | 278 ms                                                          | 248 ms: 1.12x faster                                                             |
| regex_dna                  | 127 ms                                                          | 113 ms: 1.12x faster                                                             |
| async_tree_memoization_tg  | 350 ms                                                          | 313 ms: 1.12x faster                                                             |
| regex_effbot               | 2.04 ms                                                         | 1.83 ms: 1.12x faster                                                            |
| asyncio_tcp                | 662 ms                                                          | 608 ms: 1.09x faster                                                             |
| async_tree_none            | 298 ms                                                          | 275 ms: 1.08x faster                                                             |
| async_tree_memoization     | 364 ms                                                          | 336 ms: 1.08x faster                                                             |
| deepcopy                   | 360 us                                                          | 336 us: 1.07x faster                                                             |
| dulwich_log                | 58.5 ms                                                         | 56.3 ms: 1.04x faster                                                            |
| json                       | 4.15 ms                                                         | 4.23 ms: 1.02x slower                                                            |
| python_startup_no_site     | 19.1 ms                                                         | 20.4 ms: 1.07x slower                                                            |
| deepcopy_reduce            | 3.23 us                                                         | 3.48 us: 1.08x slower                                                            |
| pickle_dict                | 19.9 us                                                         | 22.0 us: 1.10x slower                                                            |
| bench_thread_pool          | 1.10 ms                                                         | 1.23 ms: 1.12x slower                                                            |
| logging_format             | 10.4 us                                                         | 11.7 us: 1.12x slower                                                            |
| regex_v8                   | 15.0 ms                                                         | 16.9 ms: 1.12x slower                                                            |
| pickle_list                | 3.37 us                                                         | 3.81 us: 1.13x slower                                                            |
| json_loads                 | 20.4 us                                                         | 23.1 us: 1.13x slower                                                            |
| logging_simple             | 9.75 us                                                         | 11.1 us: 1.14x slower                                                            |
| deepcopy_memo              | 38.4 us                                                         | 43.7 us: 1.14x slower                                                            |
| mdp                        | 1.91 sec                                                        | 2.22 sec: 1.16x slower                                                           |
| generators                 | 38.5 ms                                                         | 44.8 ms: 1.16x slower                                                            |
| sympy_sum                  | 123 ms                                                          | 144 ms: 1.17x slower                                                             |
| bench_mp_pool              | 75.4 ms                                                         | 89.4 ms: 1.19x slower                                                            |
| sympy_integrate            | 17.5 ms                                                         | 20.8 ms: 1.19x slower                                                            |
| xml_etree_iterparse        | 77.6 ms                                                         | 92.3 ms: 1.19x slower                                                            |
| gc_traversal               | 1.44 ms                                                         | 1.72 ms: 1.19x slower                                                            |
| unpickle_list              | 2.95 us                                                         | 3.55 us: 1.20x slower                                                            |
| 2to3                       | 280 ms                                                          | 338 ms: 1.21x slower                                                             |
| sympy_str                  | 240 ms                                                          | 292 ms: 1.22x slower                                                             |
| unpickle                   | 9.71 us                                                         | 12.0 us: 1.23x slower                                                            |
| python_startup             | 22.4 ms                                                         | 27.7 ms: 1.24x slower                                                            |
| django_template            | 36.9 ms                                                         | 45.9 ms: 1.24x slower                                                            |
| regex_compile              | 129 ms                                                          | 161 ms: 1.24x slower                                                             |
| sympy_expand               | 398 ms                                                          | 496 ms: 1.25x slower                                                             |
| pickle                     | 7.79 us                                                         | 9.85 us: 1.26x slower                                                            |
| float                      | 76.7 ms                                                         | 97.7 ms: 1.27x slower                                                            |
| json_dumps                 | 7.40 ms                                                         | 9.52 ms: 1.29x slower                                                            |
| unpack_sequence            | 62.5 ns                                                         | 81.1 ns: 1.30x slower                                                            |
| comprehensions             | 19.2 us                                                         | 25.5 us: 1.33x slower                                                            |
| nqueens                    | 93.7 ms                                                         | 125 ms: 1.33x slower                                                             |
| async_generators           | 313 ms                                                          | 418 ms: 1.33x slower                                                             |
| meteor_contest             | 86.9 ms                                                         | 117 ms: 1.35x slower                                                             |
| raytrace                   | 308 ms                                                          | 419 ms: 1.36x slower                                                             |
| chaos                      | 69.4 ms                                                         | 96.3 ms: 1.39x slower                                                            |
| go                         | 137 ms                                                          | 191 ms: 1.39x slower                                                             |
| nbody                      | 127 ms                                                          | 184 ms: 1.45x slower                                                             |
| pyflate                    | 424 ms                                                          | 614 ms: 1.45x slower                                                             |
| scimark_sor                | 130 ms                                                          | 189 ms: 1.46x slower                                                             |
| telco                      | 5.51 ms                                                         | 8.06 ms: 1.46x slower                                                            |
| xml_etree_generate         | 72.1 ms                                                         | 107 ms: 1.49x slower                                                             |
| xml_etree_process          | 53.2 ms                                                         | 79.9 ms: 1.50x slower                                                            |
| hexiom                     | 6.82 ms                                                         | 10.5 ms: 1.54x slower                                                            |
| typing_runtime_protocols   | 126 us                                                          | 198 us: 1.56x slower                                                             |
| scimark_fft                | 271 ms                                                          | 425 ms: 1.57x slower                                                             |
| pickle_pure_python         | 286 us                                                          | 451 us: 1.58x slower                                                             |
| spectral_norm              | 104 ms                                                          | 165 ms: 1.59x slower                                                             |
| fannkuch                   | 354 ms                                                          | 573 ms: 1.62x slower                                                             |
| scimark_monte_carlo        | 66.4 ms                                                         | 108 ms: 1.63x slower                                                             |
| coroutines                 | 20.9 ms                                                         | 34.0 ms: 1.63x slower                                                            |
| deltablue                  | 3.58 ms                                                         | 5.91 ms: 1.65x slower                                                            |
| mako                       | 9.96 ms                                                         | 16.4 ms: 1.65x slower                                                            |
| create_gc_cycles           | 652 us                                                          | 1.10 ms: 1.69x slower                                                            |
| crypto_pyaes               | 69.2 ms                                                         | 117 ms: 1.70x slower                                                             |
| richards                   | 41.3 ms                                                         | 70.2 ms: 1.70x slower                                                            |
| unpickle_pure_python       | 210 us                                                          | 356 us: 1.70x slower                                                             |
| richards_super             | 46.5 ms                                                         | 79.3 ms: 1.71x slower                                                            |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 6.61 ms: 1.71x slower                                                            |
| coverage                   | 48.4 ms                                                         | 84.1 ms: 1.74x slower                                                            |
| scimark_lu                 | 93.2 ms                                                         | 165 ms: 1.77x slower                                                             |
| pycparser                  | 978 ms                                                          | 1.74 sec: 1.78x slower                                                           |
| pprint_safe_repr           | 721 ms                                                          | 1.48 sec: 2.05x slower                                                           |
| docutils                   | 1.98 sec                                                        | 4.22 sec: 2.13x slower                                                           |
| tomli_loads                | 2.20 sec                                                        | 5.05 sec: 2.30x slower                                                           |
| pprint_pformat             | 1.50 sec                                                        | 4.25 sec: 2.84x slower                                                           |
| logging_silent             | 101 ns                                                          | 586 ns: 5.80x slower                                                             |
| Geometric mean             | (ref)                                                           | 1.25x slower                                                                     |

Benchmark hidden because not significant (1): xml_etree_parse
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (17) of results/bm-20250617-3.15.0a0-fba5dde-NOGIL/bm-20250617-pythonperf1_win32-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.212x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.24x
- 95% likely to have a slowdown of 1.22x
- 99% likely to have a slowdown of 1.19x

# Memory
- memory change: unknown