# Results vs. 3.12.0

- fork: python
- ref: 20d5494c88985beb925b
- machine: windows-amd64
- commit hash: 20d5494
- commit date: 2025-09-20
- overall geometric mean: 1.444x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.44x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250920-pythonperf1_win32-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 215 ms: 1.30x faster                                                             |
| docutils       | 1.98 sec                                                        | 1.59 sec: 1.25x faster                                                           |
| Geometric mean | (ref)                                                           | 1.27x faster                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250920-pythonperf1_win32-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494 |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_memoization     | 364 ms                                                          | 200 ms: 1.82x faster                                                             |
| async_tree_io              | 693 ms                                                          | 381 ms: 1.82x faster                                                             |
| async_tree_io_tg           | 677 ms                                                          | 379 ms: 1.79x faster                                                             |
| async_tree_none            | 298 ms                                                          | 169 ms: 1.76x faster                                                             |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 328 ms: 1.72x faster                                                             |
| async_tree_memoization_tg  | 350 ms                                                          | 205 ms: 1.71x faster                                                             |
| async_tree_none_tg         | 278 ms                                                          | 165 ms: 1.68x faster                                                             |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 332 ms: 1.65x faster                                                             |
| Geometric mean             | (ref)                                                           | 1.74x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250920-pythonperf1_win32-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 63.9 ms: 1.99x faster                                                            |
| float          | 76.7 ms                                                         | 42.0 ms: 1.82x faster                                                            |
| pidigits       | 199 ms                                                          | 148 ms: 1.34x faster                                                             |
| Geometric mean | (ref)                                                           | 1.70x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250920-pythonperf1_win32-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 78.0 ms: 1.65x faster                                                            |
| regex_effbot   | 2.04 ms                                                         | 1.53 ms: 1.33x faster                                                            |
| regex_v8       | 15.0 ms                                                         | 13.9 ms: 1.08x faster                                                            |
| regex_dna      | 127 ms                                                          | 120 ms: 1.06x faster                                                             |
| Geometric mean | (ref)                                                           | 1.26x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250920-pythonperf1_win32-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494 |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| tomli_loads          | 2.20 sec                                                        | 1.33 sec: 1.65x faster                                                           |
| unpickle_pure_python | 210 us                                                          | 132 us: 1.59x faster                                                             |
| json_loads           | 20.4 us                                                         | 14.3 us: 1.42x faster                                                            |
| json_dumps           | 7.40 ms                                                         | 5.31 ms: 1.39x faster                                                            |
| xml_etree_process    | 53.2 ms                                                         | 38.3 ms: 1.39x faster                                                            |
| pickle_pure_python   | 286 us                                                          | 213 us: 1.34x faster                                                             |
| xml_etree_parse      | 113 ms                                                          | 85.3 ms: 1.33x faster                                                            |
| xml_etree_generate   | 72.1 ms                                                         | 55.0 ms: 1.31x faster                                                            |
| xml_etree_iterparse  | 77.6 ms                                                         | 62.4 ms: 1.25x faster                                                            |
| unpickle             | 9.71 us                                                         | 8.31 us: 1.17x faster                                                            |
| unpickle_list        | 2.95 us                                                         | 2.80 us: 1.05x faster                                                            |
| pickle_list          | 3.37 us                                                         | 3.32 us: 1.01x faster                                                            |
| pickle_dict          | 19.9 us                                                         | 19.8 us: 1.01x faster                                                            |
| pickle               | 7.79 us                                                         | 7.93 us: 1.02x slower                                                            |
| Geometric mean       | (ref)                                                           | 1.26x faster                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250920-pythonperf1_win32-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup | 22.4 ms                                                         | 25.3 ms: 1.13x slower                                                            |
| Geometric mean | (ref)                                                           | 1.06x slower                                                                     |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250920-pythonperf1_win32-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494 |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| django_template | 36.9 ms                                                         | 24.1 ms: 1.53x faster                                                            |
| mako            | 9.96 ms                                                         | 6.66 ms: 1.49x faster                                                            |
| Geometric mean  | (ref)                                                           | 1.51x faster                                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250920-pythonperf1_win32-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494 |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| asyncio_tcp_ssl            | 17.7 sec                                                        | 1.37 sec: 12.90x faster                                                          |
| pathlib                    | 91.4 ms                                                         | 29.3 ms: 3.12x faster                                                            |
| mdp                        | 1.91 sec                                                        | 793 ms: 2.41x faster                                                             |
| deepcopy_memo              | 38.4 us                                                         | 16.7 us: 2.30x faster                                                            |
| deepcopy                   | 360 us                                                          | 164 us: 2.19x faster                                                             |
| generators                 | 38.5 ms                                                         | 19.2 ms: 2.01x faster                                                            |
| nbody                      | 127 ms                                                          | 63.9 ms: 1.99x faster                                                            |
| unpack_sequence            | 62.5 ns                                                         | 32.4 ns: 1.93x faster                                                            |
| go                         | 137 ms                                                          | 74.2 ms: 1.85x faster                                                            |
| deepcopy_reduce            | 3.23 us                                                         | 1.76 us: 1.83x faster                                                            |
| float                      | 76.7 ms                                                         | 42.0 ms: 1.82x faster                                                            |
| logging_silent             | 101 ns                                                          | 55.4 ns: 1.82x faster                                                            |
| async_tree_memoization     | 364 ms                                                          | 200 ms: 1.82x faster                                                             |
| async_tree_io              | 693 ms                                                          | 381 ms: 1.82x faster                                                             |
| async_tree_io_tg           | 677 ms                                                          | 379 ms: 1.79x faster                                                             |
| comprehensions             | 19.2 us                                                         | 10.9 us: 1.76x faster                                                            |
| async_tree_none            | 298 ms                                                          | 169 ms: 1.76x faster                                                             |
| raytrace                   | 308 ms                                                          | 176 ms: 1.75x faster                                                             |
| scimark_sor                | 130 ms                                                          | 74.2 ms: 1.75x faster                                                            |
| chaos                      | 69.4 ms                                                         | 40.1 ms: 1.73x faster                                                            |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 328 ms: 1.72x faster                                                             |
| async_tree_memoization_tg  | 350 ms                                                          | 205 ms: 1.71x faster                                                             |
| hexiom                     | 6.82 ms                                                         | 4.00 ms: 1.70x faster                                                            |
| async_tree_none_tg         | 278 ms                                                          | 165 ms: 1.68x faster                                                             |
| spectral_norm              | 104 ms                                                          | 61.9 ms: 1.68x faster                                                            |
| deltablue                  | 3.58 ms                                                         | 2.14 ms: 1.67x faster                                                            |
| logging_simple             | 9.75 us                                                         | 5.86 us: 1.66x faster                                                            |
| regex_compile              | 129 ms                                                          | 78.0 ms: 1.65x faster                                                            |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 332 ms: 1.65x faster                                                             |
| tomli_loads                | 2.20 sec                                                        | 1.33 sec: 1.65x faster                                                           |
| scimark_monte_carlo        | 66.4 ms                                                         | 40.6 ms: 1.64x faster                                                            |
| logging_format             | 10.4 us                                                         | 6.40 us: 1.63x faster                                                            |
| scimark_lu                 | 93.2 ms                                                         | 58.7 ms: 1.59x faster                                                            |
| unpickle_pure_python       | 210 us                                                          | 132 us: 1.59x faster                                                             |
| richards                   | 41.3 ms                                                         | 26.1 ms: 1.58x faster                                                            |
| richards_super             | 46.5 ms                                                         | 29.6 ms: 1.57x faster                                                            |
| django_template            | 36.9 ms                                                         | 24.1 ms: 1.53x faster                                                            |
| nqueens                    | 93.7 ms                                                         | 61.3 ms: 1.53x faster                                                            |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 2.55 ms: 1.51x faster                                                            |
| scimark_fft                | 271 ms                                                          | 179 ms: 1.51x faster                                                             |
| pyflate                    | 424 ms                                                          | 280 ms: 1.51x faster                                                             |
| pprint_pformat             | 1.50 sec                                                        | 995 ms: 1.51x faster                                                             |
| dulwich_log                | 58.5 ms                                                         | 38.9 ms: 1.50x faster                                                            |
| mako                       | 9.96 ms                                                         | 6.66 ms: 1.49x faster                                                            |
| crypto_pyaes               | 69.2 ms                                                         | 47.0 ms: 1.47x faster                                                            |
| pprint_safe_repr           | 721 ms                                                          | 490 ms: 1.47x faster                                                             |
| sympy_sum                  | 123 ms                                                          | 85.0 ms: 1.44x faster                                                            |
| coroutines                 | 20.9 ms                                                         | 14.5 ms: 1.44x faster                                                            |
| sympy_integrate            | 17.5 ms                                                         | 12.2 ms: 1.44x faster                                                            |
| sympy_str                  | 240 ms                                                          | 167 ms: 1.43x faster                                                             |
| json                       | 4.15 ms                                                         | 2.92 ms: 1.42x faster                                                            |
| json_loads                 | 20.4 us                                                         | 14.3 us: 1.42x faster                                                            |
| sympy_expand               | 398 ms                                                          | 283 ms: 1.41x faster                                                             |
| pycparser                  | 978 ms                                                          | 699 ms: 1.40x faster                                                             |
| json_dumps                 | 7.40 ms                                                         | 5.31 ms: 1.39x faster                                                            |
| xml_etree_process          | 53.2 ms                                                         | 38.3 ms: 1.39x faster                                                            |
| async_generators           | 313 ms                                                          | 227 ms: 1.38x faster                                                             |
| fannkuch                   | 354 ms                                                          | 257 ms: 1.37x faster                                                             |
| asyncio_tcp                | 662 ms                                                          | 491 ms: 1.35x faster                                                             |
| pidigits                   | 199 ms                                                          | 148 ms: 1.34x faster                                                             |
| pickle_pure_python         | 286 us                                                          | 213 us: 1.34x faster                                                             |
| sqlite_synth               | 2.07 us                                                         | 1.55 us: 1.34x faster                                                            |
| regex_effbot               | 2.04 ms                                                         | 1.53 ms: 1.33x faster                                                            |
| xml_etree_parse            | 113 ms                                                          | 85.3 ms: 1.33x faster                                                            |
| xml_etree_generate         | 72.1 ms                                                         | 55.0 ms: 1.31x faster                                                            |
| 2to3                       | 280 ms                                                          | 215 ms: 1.30x faster                                                             |
| telco                      | 5.51 ms                                                         | 4.29 ms: 1.29x faster                                                            |
| typing_runtime_protocols   | 126 us                                                          | 101 us: 1.25x faster                                                             |
| docutils                   | 1.98 sec                                                        | 1.59 sec: 1.25x faster                                                           |
| xml_etree_iterparse        | 77.6 ms                                                         | 62.4 ms: 1.25x faster                                                            |
| meteor_contest             | 86.9 ms                                                         | 71.5 ms: 1.21x faster                                                            |
| unpickle                   | 9.71 us                                                         | 8.31 us: 1.17x faster                                                            |
| regex_v8                   | 15.0 ms                                                         | 13.9 ms: 1.08x faster                                                            |
| regex_dna                  | 127 ms                                                          | 120 ms: 1.06x faster                                                             |
| unpickle_list              | 2.95 us                                                         | 2.80 us: 1.05x faster                                                            |
| pickle_list                | 3.37 us                                                         | 3.32 us: 1.01x faster                                                            |
| pickle_dict                | 19.9 us                                                         | 19.8 us: 1.01x faster                                                            |
| pickle                     | 7.79 us                                                         | 7.93 us: 1.02x slower                                                            |
| coverage                   | 48.4 ms                                                         | 50.4 ms: 1.04x slower                                                            |
| python_startup             | 22.4 ms                                                         | 25.3 ms: 1.13x slower                                                            |
| bench_mp_pool              | 75.4 ms                                                         | 90.9 ms: 1.21x slower                                                            |
| gc_traversal               | 1.44 ms                                                         | 2.10 ms: 1.46x slower                                                            |
| create_gc_cycles           | 652 us                                                          | 1.27 ms: 1.95x slower                                                            |
| bench_thread_pool          | 1.10 ms                                                         | 8.12 ms: 7.37x slower                                                            |
| Geometric mean             | (ref)                                                           | 1.45x faster                                                                     |

Benchmark hidden because not significant (1): python_startup_no_site
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (17) of results/bm-20250920-3.15.0a0-20d5494/bm-20250920-pythonperf1_win32-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.444x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.47x
- 95% likely to have a speedup of 1.46x
- 99% likely to have a speedup of 1.44x

# Memory
- memory change: unknown