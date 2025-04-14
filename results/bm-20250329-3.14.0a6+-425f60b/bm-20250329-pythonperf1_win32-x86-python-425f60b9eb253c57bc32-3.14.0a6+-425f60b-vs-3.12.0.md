# Results vs. 3.12.0

- fork: python
- ref: 425f60b9eb253c57bc32
- machine: windows-x86
- commit hash: 425f60b
- commit date: 2025-03-29
- overall geometric mean: 1.156x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.09x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250329-pythonperf1_win32-x86-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 264 ms: 1.06x faster                                                            |
| docutils       | 1.98 sec                                                        | 1.88 sec: 1.05x faster                                                          |
| Geometric mean | (ref)                                                           | 1.06x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250329-pythonperf1_win32-x86-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_io_tg           | 677 ms                                                          | 459 ms: 1.48x faster                                                            |
| async_tree_io              | 693 ms                                                          | 470 ms: 1.47x faster                                                            |
| async_tree_memoization_tg  | 350 ms                                                          | 249 ms: 1.41x faster                                                            |
| async_tree_memoization     | 364 ms                                                          | 258 ms: 1.41x faster                                                            |
| async_tree_none_tg         | 278 ms                                                          | 204 ms: 1.36x faster                                                            |
| async_tree_none            | 298 ms                                                          | 221 ms: 1.35x faster                                                            |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 451 ms: 1.21x faster                                                            |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 466 ms: 1.21x faster                                                            |
| Geometric mean             | (ref)                                                           | 1.36x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250329-pythonperf1_win32-x86-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 85.9 ms: 1.48x faster                                                           |
| float          | 76.7 ms                                                         | 54.2 ms: 1.41x faster                                                           |
| pidigits       | 199 ms                                                          | 200 ms: 1.00x slower                                                            |
| Geometric mean | (ref)                                                           | 1.28x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250329-pythonperf1_win32-x86-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_effbot   | 2.04 ms                                                         | 1.57 ms: 1.30x faster                                                           |
| regex_compile  | 129 ms                                                          | 108 ms: 1.20x faster                                                            |
| regex_dna      | 127 ms                                                          | 119 ms: 1.07x faster                                                            |
| Geometric mean | (ref)                                                           | 1.13x faster                                                                    |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250329-pythonperf1_win32-x86-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 2.20 sec                                                        | 1.79 sec: 1.23x faster                                                          |
| xml_etree_iterparse  | 77.6 ms                                                         | 67.4 ms: 1.15x faster                                                           |
| unpickle_pure_python | 210 us                                                          | 186 us: 1.13x faster                                                            |
| pickle_pure_python   | 286 us                                                          | 271 us: 1.05x faster                                                            |
| xml_etree_generate   | 72.1 ms                                                         | 69.4 ms: 1.04x faster                                                           |
| xml_etree_process    | 53.2 ms                                                         | 52.0 ms: 1.02x faster                                                           |
| xml_etree_parse      | 113 ms                                                          | 112 ms: 1.01x faster                                                            |
| unpickle_list        | 2.95 us                                                         | 3.08 us: 1.04x slower                                                           |
| pickle_dict          | 19.9 us                                                         | 21.2 us: 1.07x slower                                                           |
| json_loads           | 20.4 us                                                         | 21.8 us: 1.07x slower                                                           |
| json_dumps           | 7.40 ms                                                         | 8.18 ms: 1.11x slower                                                           |
| pickle_list          | 3.37 us                                                         | 3.82 us: 1.13x slower                                                           |
| unpickle             | 9.71 us                                                         | 11.2 us: 1.15x slower                                                           |
| pickle               | 7.79 us                                                         | 9.35 us: 1.20x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.01x slower                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250329-pythonperf1_win32-x86-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 22.7 ms: 1.19x slower                                                           |
| python_startup         | 22.4 ms                                                         | 28.8 ms: 1.29x slower                                                           |
| Geometric mean         | (ref)                                                           | 1.24x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250329-pythonperf1_win32-x86-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 8.37 ms: 1.19x faster                                                           |
| django_template | 36.9 ms                                                         | 36.1 ms: 1.02x faster                                                           |
| Geometric mean  | (ref)                                                           | 1.10x faster                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250329-pythonperf1_win32-x86-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pathlib                    | 91.4 ms                                                         | 37.7 ms: 2.42x faster                                                           |
| deepcopy_memo              | 38.4 us                                                         | 20.4 us: 1.88x faster                                                           |
| mdp                        | 1.91 sec                                                        | 1.03 sec: 1.85x faster                                                          |
| unpack_sequence            | 62.5 ns                                                         | 39.2 ns: 1.59x faster                                                           |
| logging_silent             | 101 ns                                                          | 67.0 ns: 1.51x faster                                                           |
| generators                 | 38.5 ms                                                         | 25.6 ms: 1.51x faster                                                           |
| nbody                      | 127 ms                                                          | 85.9 ms: 1.48x faster                                                           |
| async_tree_io_tg           | 677 ms                                                          | 459 ms: 1.48x faster                                                            |
| async_tree_io              | 693 ms                                                          | 470 ms: 1.47x faster                                                            |
| deepcopy                   | 360 us                                                          | 248 us: 1.45x faster                                                            |
| spectral_norm              | 104 ms                                                          | 71.9 ms: 1.44x faster                                                           |
| float                      | 76.7 ms                                                         | 54.2 ms: 1.41x faster                                                           |
| async_tree_memoization_tg  | 350 ms                                                          | 249 ms: 1.41x faster                                                            |
| async_tree_memoization     | 364 ms                                                          | 258 ms: 1.41x faster                                                            |
| scimark_lu                 | 93.2 ms                                                         | 68.2 ms: 1.37x faster                                                           |
| async_tree_none_tg         | 278 ms                                                          | 204 ms: 1.36x faster                                                            |
| deltablue                  | 3.58 ms                                                         | 2.65 ms: 1.35x faster                                                           |
| async_tree_none            | 298 ms                                                          | 221 ms: 1.35x faster                                                            |
| scimark_sor                | 130 ms                                                          | 96.8 ms: 1.34x faster                                                           |
| comprehensions             | 19.2 us                                                         | 14.4 us: 1.34x faster                                                           |
| hexiom                     | 6.82 ms                                                         | 5.19 ms: 1.31x faster                                                           |
| regex_effbot               | 2.04 ms                                                         | 1.57 ms: 1.30x faster                                                           |
| raytrace                   | 308 ms                                                          | 240 ms: 1.28x faster                                                            |
| coroutines                 | 20.9 ms                                                         | 16.3 ms: 1.28x faster                                                           |
| scimark_monte_carlo        | 66.4 ms                                                         | 52.7 ms: 1.26x faster                                                           |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 3.11 ms: 1.24x faster                                                           |
| chaos                      | 69.4 ms                                                         | 56.2 ms: 1.23x faster                                                           |
| go                         | 137 ms                                                          | 111 ms: 1.23x faster                                                            |
| tomli_loads                | 2.20 sec                                                        | 1.79 sec: 1.23x faster                                                          |
| deepcopy_reduce            | 3.23 us                                                         | 2.65 us: 1.22x faster                                                           |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 451 ms: 1.21x faster                                                            |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 466 ms: 1.21x faster                                                            |
| regex_compile              | 129 ms                                                          | 108 ms: 1.20x faster                                                            |
| mako                       | 9.96 ms                                                         | 8.37 ms: 1.19x faster                                                           |
| scimark_fft                | 271 ms                                                          | 230 ms: 1.18x faster                                                            |
| pyflate                    | 424 ms                                                          | 365 ms: 1.16x faster                                                            |
| xml_etree_iterparse        | 77.6 ms                                                         | 67.4 ms: 1.15x faster                                                           |
| unpickle_pure_python       | 210 us                                                          | 186 us: 1.13x faster                                                            |
| nqueens                    | 93.7 ms                                                         | 83.1 ms: 1.13x faster                                                           |
| dulwich_log                | 58.5 ms                                                         | 52.4 ms: 1.12x faster                                                           |
| fannkuch                   | 354 ms                                                          | 317 ms: 1.12x faster                                                            |
| sympy_integrate            | 17.5 ms                                                         | 15.7 ms: 1.11x faster                                                           |
| pprint_pformat             | 1.50 sec                                                        | 1.36 sec: 1.10x faster                                                          |
| logging_simple             | 9.75 us                                                         | 8.85 us: 1.10x faster                                                           |
| sympy_sum                  | 123 ms                                                          | 112 ms: 1.10x faster                                                            |
| pprint_safe_repr           | 721 ms                                                          | 659 ms: 1.09x faster                                                            |
| logging_format             | 10.4 us                                                         | 9.58 us: 1.09x faster                                                           |
| sqlite_synth               | 2.07 us                                                         | 1.92 us: 1.08x faster                                                           |
| crypto_pyaes               | 69.2 ms                                                         | 64.4 ms: 1.08x faster                                                           |
| richards                   | 41.3 ms                                                         | 38.7 ms: 1.07x faster                                                           |
| pycparser                  | 978 ms                                                          | 917 ms: 1.07x faster                                                            |
| regex_dna                  | 127 ms                                                          | 119 ms: 1.07x faster                                                            |
| richards_super             | 46.5 ms                                                         | 43.8 ms: 1.06x faster                                                           |
| 2to3                       | 280 ms                                                          | 264 ms: 1.06x faster                                                            |
| sympy_str                  | 240 ms                                                          | 226 ms: 1.06x faster                                                            |
| docutils                   | 1.98 sec                                                        | 1.88 sec: 1.05x faster                                                          |
| pickle_pure_python         | 286 us                                                          | 271 us: 1.05x faster                                                            |
| asyncio_tcp                | 662 ms                                                          | 631 ms: 1.05x faster                                                            |
| async_generators           | 313 ms                                                          | 299 ms: 1.05x faster                                                            |
| meteor_contest             | 86.9 ms                                                         | 83.4 ms: 1.04x faster                                                           |
| xml_etree_generate         | 72.1 ms                                                         | 69.4 ms: 1.04x faster                                                           |
| django_template            | 36.9 ms                                                         | 36.1 ms: 1.02x faster                                                           |
| xml_etree_process          | 53.2 ms                                                         | 52.0 ms: 1.02x faster                                                           |
| xml_etree_parse            | 113 ms                                                          | 112 ms: 1.01x faster                                                            |
| pidigits                   | 199 ms                                                          | 200 ms: 1.00x slower                                                            |
| sympy_expand               | 398 ms                                                          | 401 ms: 1.01x slower                                                            |
| asyncio_tcp_ssl            | 17.7 sec                                                        | 17.8 sec: 1.01x slower                                                          |
| unpickle_list              | 2.95 us                                                         | 3.08 us: 1.04x slower                                                           |
| pickle_dict                | 19.9 us                                                         | 21.2 us: 1.07x slower                                                           |
| json_loads                 | 20.4 us                                                         | 21.8 us: 1.07x slower                                                           |
| coverage                   | 48.4 ms                                                         | 53.3 ms: 1.10x slower                                                           |
| json                       | 4.15 ms                                                         | 4.59 ms: 1.10x slower                                                           |
| json_dumps                 | 7.40 ms                                                         | 8.18 ms: 1.11x slower                                                           |
| pickle_list                | 3.37 us                                                         | 3.82 us: 1.13x slower                                                           |
| unpickle                   | 9.71 us                                                         | 11.2 us: 1.15x slower                                                           |
| bench_thread_pool          | 1.10 ms                                                         | 1.30 ms: 1.18x slower                                                           |
| python_startup_no_site     | 19.1 ms                                                         | 22.7 ms: 1.19x slower                                                           |
| pickle                     | 7.79 us                                                         | 9.35 us: 1.20x slower                                                           |
| typing_runtime_protocols   | 126 us                                                          | 157 us: 1.24x slower                                                            |
| gc_traversal               | 1.44 ms                                                         | 1.82 ms: 1.26x slower                                                           |
| bench_mp_pool              | 75.4 ms                                                         | 95.2 ms: 1.26x slower                                                           |
| telco                      | 5.51 ms                                                         | 7.07 ms: 1.28x slower                                                           |
| python_startup             | 22.4 ms                                                         | 28.8 ms: 1.29x slower                                                           |
| create_gc_cycles           | 652 us                                                          | 1.06 ms: 1.63x slower                                                           |
| Geometric mean             | (ref)                                                           | 1.13x faster                                                                    |

Benchmark hidden because not significant (1): regex_v8
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250329-3.14.0a6+-425f60b/bm-20250329-pythonperf1_win32-x86-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.156x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.11x
- 95% likely to have a speedup of 1.10x
- 99% likely to have a speedup of 1.09x

# Memory
- memory change: unknown