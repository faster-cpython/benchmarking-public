# Results vs. 3.12.0

- fork: python
- ref: 79b7cab50a3292a1c014
- machine: windows-x86
- commit hash: 79b7cab
- commit date: 2024-12-07
- overall geometric mean: 1.163x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.13x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241207-pythonperf1_win32-x86-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 247 ms: 1.13x faster                                                            |
| docutils       | 1.98 sec                                                        | 1.79 sec: 1.11x faster                                                          |
| Geometric mean | (ref)                                                           | 1.12x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241207-pythonperf1_win32-x86-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_io_tg           | 677 ms                                                          | 421 ms: 1.61x faster                                                            |
| async_tree_io              | 693 ms                                                          | 432 ms: 1.61x faster                                                            |
| async_tree_none            | 298 ms                                                          | 201 ms: 1.48x faster                                                            |
| async_tree_none_tg         | 278 ms                                                          | 187 ms: 1.48x faster                                                            |
| async_tree_memoization_tg  | 350 ms                                                          | 237 ms: 1.48x faster                                                            |
| async_tree_memoization     | 364 ms                                                          | 250 ms: 1.45x faster                                                            |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 449 ms: 1.26x faster                                                            |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 443 ms: 1.23x faster                                                            |
| Geometric mean             | (ref)                                                           | 1.44x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241207-pythonperf1_win32-x86-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 86.7 ms: 1.46x faster                                                           |
| float          | 76.7 ms                                                         | 60.8 ms: 1.26x faster                                                           |
| pidigits       | 199 ms                                                          | 202 ms: 1.01x slower                                                            |
| Geometric mean | (ref)                                                           | 1.22x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241207-pythonperf1_win32-x86-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_effbot   | 2.04 ms                                                         | 1.56 ms: 1.31x faster                                                           |
| regex_compile  | 129 ms                                                          | 105 ms: 1.23x faster                                                            |
| regex_dna      | 127 ms                                                          | 115 ms: 1.11x faster                                                            |
| regex_v8       | 15.0 ms                                                         | 15.3 ms: 1.02x slower                                                           |
| Geometric mean | (ref)                                                           | 1.15x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241207-pythonperf1_win32-x86-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| unpickle_pure_python | 210 us                                                          | 170 us: 1.23x faster                                                            |
| tomli_loads          | 2.20 sec                                                        | 1.80 sec: 1.22x faster                                                          |
| xml_etree_iterparse  | 77.6 ms                                                         | 64.9 ms: 1.20x faster                                                           |
| xml_etree_process    | 53.2 ms                                                         | 48.3 ms: 1.10x faster                                                           |
| xml_etree_parse      | 113 ms                                                          | 104 ms: 1.08x faster                                                            |
| xml_etree_generate   | 72.1 ms                                                         | 67.3 ms: 1.07x faster                                                           |
| pickle_pure_python   | 286 us                                                          | 274 us: 1.04x faster                                                            |
| json_loads           | 20.4 us                                                         | 20.3 us: 1.00x faster                                                           |
| json_dumps           | 7.40 ms                                                         | 8.57 ms: 1.16x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.09x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241207-pythonperf1_win32-x86-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 20.0 ms: 1.05x slower                                                           |
| python_startup         | 22.4 ms                                                         | 26.8 ms: 1.20x slower                                                           |
| Geometric mean         | (ref)                                                           | 1.12x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241207-pythonperf1_win32-x86-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 7.50 ms: 1.33x faster                                                           |
| django_template | 36.9 ms                                                         | 32.5 ms: 1.14x faster                                                           |
| Geometric mean  | (ref)                                                           | 1.23x faster                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241207-pythonperf1_win32-x86-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| deepcopy_memo              | 38.4 us                                                         | 21.4 us: 1.80x faster                                                           |
| async_tree_io_tg           | 677 ms                                                          | 421 ms: 1.61x faster                                                            |
| generators                 | 38.5 ms                                                         | 23.9 ms: 1.61x faster                                                           |
| async_tree_io              | 693 ms                                                          | 432 ms: 1.61x faster                                                            |
| deepcopy                   | 360 us                                                          | 230 us: 1.56x faster                                                            |
| async_tree_none            | 298 ms                                                          | 201 ms: 1.48x faster                                                            |
| async_tree_none_tg         | 278 ms                                                          | 187 ms: 1.48x faster                                                            |
| async_tree_memoization_tg  | 350 ms                                                          | 237 ms: 1.48x faster                                                            |
| nbody                      | 127 ms                                                          | 86.7 ms: 1.46x faster                                                           |
| async_tree_memoization     | 364 ms                                                          | 250 ms: 1.45x faster                                                            |
| spectral_norm              | 104 ms                                                          | 72.9 ms: 1.42x faster                                                           |
| scimark_lu                 | 93.2 ms                                                         | 65.7 ms: 1.42x faster                                                           |
| go                         | 137 ms                                                          | 98.3 ms: 1.40x faster                                                           |
| comprehensions             | 19.2 us                                                         | 13.9 us: 1.38x faster                                                           |
| logging_silent             | 101 ns                                                          | 73.1 ns: 1.38x faster                                                           |
| hexiom                     | 6.82 ms                                                         | 5.01 ms: 1.36x faster                                                           |
| deltablue                  | 3.58 ms                                                         | 2.65 ms: 1.35x faster                                                           |
| mako                       | 9.96 ms                                                         | 7.50 ms: 1.33x faster                                                           |
| deepcopy_reduce            | 3.23 us                                                         | 2.45 us: 1.32x faster                                                           |
| regex_effbot               | 2.04 ms                                                         | 1.56 ms: 1.31x faster                                                           |
| raytrace                   | 308 ms                                                          | 239 ms: 1.29x faster                                                            |
| scimark_sor                | 130 ms                                                          | 102 ms: 1.27x faster                                                            |
| float                      | 76.7 ms                                                         | 60.8 ms: 1.26x faster                                                           |
| chaos                      | 69.4 ms                                                         | 55.2 ms: 1.26x faster                                                           |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 449 ms: 1.26x faster                                                            |
| logging_simple             | 9.75 us                                                         | 7.78 us: 1.25x faster                                                           |
| unpickle_pure_python       | 210 us                                                          | 170 us: 1.23x faster                                                            |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 443 ms: 1.23x faster                                                            |
| logging_format             | 10.4 us                                                         | 8.44 us: 1.23x faster                                                           |
| coroutines                 | 20.9 ms                                                         | 17.0 ms: 1.23x faster                                                           |
| regex_compile              | 129 ms                                                          | 105 ms: 1.23x faster                                                            |
| tomli_loads                | 2.20 sec                                                        | 1.80 sec: 1.22x faster                                                          |
| pyflate                    | 424 ms                                                          | 349 ms: 1.21x faster                                                            |
| pycparser                  | 978 ms                                                          | 816 ms: 1.20x faster                                                            |
| xml_etree_iterparse        | 77.6 ms                                                         | 64.9 ms: 1.20x faster                                                           |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 3.23 ms: 1.19x faster                                                           |
| scimark_monte_carlo        | 66.4 ms                                                         | 55.7 ms: 1.19x faster                                                           |
| scimark_fft                | 271 ms                                                          | 229 ms: 1.18x faster                                                            |
| sqlglot_parse              | 1.25 ms                                                         | 1.06 ms: 1.18x faster                                                           |
| nqueens                    | 93.7 ms                                                         | 79.4 ms: 1.18x faster                                                           |
| sqlglot_transpile          | 1.53 ms                                                         | 1.30 ms: 1.18x faster                                                           |
| crypto_pyaes               | 69.2 ms                                                         | 59.2 ms: 1.17x faster                                                           |
| fannkuch                   | 354 ms                                                          | 305 ms: 1.16x faster                                                            |
| dulwich_log                | 58.5 ms                                                         | 50.5 ms: 1.16x faster                                                           |
| sympy_sum                  | 123 ms                                                          | 107 ms: 1.15x faster                                                            |
| sqlglot_optimize           | 48.5 ms                                                         | 42.3 ms: 1.15x faster                                                           |
| sympy_integrate            | 17.5 ms                                                         | 15.4 ms: 1.14x faster                                                           |
| pprint_safe_repr           | 721 ms                                                          | 634 ms: 1.14x faster                                                            |
| django_template            | 36.9 ms                                                         | 32.5 ms: 1.14x faster                                                           |
| 2to3                       | 280 ms                                                          | 247 ms: 1.13x faster                                                            |
| mdp                        | 1.91 sec                                                        | 1.69 sec: 1.13x faster                                                          |
| pprint_pformat             | 1.50 sec                                                        | 1.33 sec: 1.13x faster                                                          |
| bench_thread_pool          | 1.10 ms                                                         | 983 us: 1.12x faster                                                            |
| pathlib                    | 91.4 ms                                                         | 81.6 ms: 1.12x faster                                                           |
| sympy_str                  | 240 ms                                                          | 215 ms: 1.12x faster                                                            |
| docutils                   | 1.98 sec                                                        | 1.79 sec: 1.11x faster                                                          |
| regex_dna                  | 127 ms                                                          | 115 ms: 1.11x faster                                                            |
| xml_etree_process          | 53.2 ms                                                         | 48.3 ms: 1.10x faster                                                           |
| richards                   | 41.3 ms                                                         | 37.9 ms: 1.09x faster                                                           |
| xml_etree_parse            | 113 ms                                                          | 104 ms: 1.08x faster                                                            |
| meteor_contest             | 86.9 ms                                                         | 80.6 ms: 1.08x faster                                                           |
| xml_etree_generate         | 72.1 ms                                                         | 67.3 ms: 1.07x faster                                                           |
| richards_super             | 46.5 ms                                                         | 43.4 ms: 1.07x faster                                                           |
| sqlite_synth               | 2.07 us                                                         | 1.95 us: 1.06x faster                                                           |
| async_generators           | 313 ms                                                          | 296 ms: 1.06x faster                                                            |
| sympy_expand               | 398 ms                                                          | 377 ms: 1.05x faster                                                            |
| pickle_pure_python         | 286 us                                                          | 274 us: 1.04x faster                                                            |
| json_loads                 | 20.4 us                                                         | 20.3 us: 1.00x faster                                                           |
| json                       | 4.15 ms                                                         | 4.18 ms: 1.01x slower                                                           |
| pidigits                   | 199 ms                                                          | 202 ms: 1.01x slower                                                            |
| regex_v8                   | 15.0 ms                                                         | 15.3 ms: 1.02x slower                                                           |
| python_startup_no_site     | 19.1 ms                                                         | 20.0 ms: 1.05x slower                                                           |
| coverage                   | 48.4 ms                                                         | 52.9 ms: 1.09x slower                                                           |
| typing_runtime_protocols   | 126 us                                                          | 139 us: 1.10x slower                                                            |
| json_dumps                 | 7.40 ms                                                         | 8.57 ms: 1.16x slower                                                           |
| telco                      | 5.51 ms                                                         | 6.51 ms: 1.18x slower                                                           |
| python_startup             | 22.4 ms                                                         | 26.8 ms: 1.20x slower                                                           |
| bench_mp_pool              | 75.4 ms                                                         | 92.1 ms: 1.22x slower                                                           |
| gc_traversal               | 1.44 ms                                                         | 1.78 ms: 1.23x slower                                                           |
| create_gc_cycles           | 652 us                                                          | 972 us: 1.49x slower                                                            |
| sqlglot_normalize          | 100 ms                                                          | 218 ms: 2.17x slower                                                            |
| Geometric mean             | (ref)                                                           | 1.16x faster                                                                    |
Ignored benchmarks (15) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20241207-3.14.0a2+-79b7cab/bm-20241207-pythonperf1_win32-x86-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.163x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.14x
- 95% likely to have a speedup of 1.14x
- 99% likely to have a speedup of 1.13x

# Memory
- memory change: unknown