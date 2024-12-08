# Results vs. 3.12.0

- fork: python
- ref: 79b7cab50a3292a1c014
- machine: windows-x86
- commit hash: 79b7cab
- commit date: 2024-12-07
- overall geometric mean: 1.072x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241207-pythonperf1_win32-x86-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 259 ms: 1.08x faster                                                            |
| docutils       | 1.98 sec                                                        | 1.95 sec: 1.02x faster                                                          |
| Geometric mean | (ref)                                                           | 1.05x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241207-pythonperf1_win32-x86-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_io_tg           | 677 ms                                                          | 451 ms: 1.50x faster                                                            |
| async_tree_io              | 693 ms                                                          | 480 ms: 1.44x faster                                                            |
| async_tree_none_tg         | 278 ms                                                          | 200 ms: 1.39x faster                                                            |
| async_tree_memoization_tg  | 350 ms                                                          | 252 ms: 1.39x faster                                                            |
| async_tree_none            | 298 ms                                                          | 228 ms: 1.31x faster                                                            |
| async_tree_memoization     | 364 ms                                                          | 282 ms: 1.29x faster                                                            |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 456 ms: 1.20x faster                                                            |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 480 ms: 1.17x faster                                                            |
| Geometric mean             | (ref)                                                           | 1.33x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241207-pythonperf1_win32-x86-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 76.7 ms                                                         | 57.5 ms: 1.33x faster                                                           |
| nbody          | 127 ms                                                          | 99.4 ms: 1.28x faster                                                           |
| pidigits       | 199 ms                                                          | 200 ms: 1.01x slower                                                            |
| Geometric mean | (ref)                                                           | 1.19x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241207-pythonperf1_win32-x86-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_effbot   | 2.04 ms                                                         | 1.59 ms: 1.28x faster                                                           |
| regex_compile  | 129 ms                                                          | 115 ms: 1.13x faster                                                            |
| regex_dna      | 127 ms                                                          | 115 ms: 1.10x faster                                                            |
| regex_v8       | 15.0 ms                                                         | 15.7 ms: 1.05x slower                                                           |
| Geometric mean | (ref)                                                           | 1.11x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241207-pythonperf1_win32-x86-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| xml_etree_iterparse  | 77.6 ms                                                         | 63.4 ms: 1.22x faster                                                           |
| tomli_loads          | 2.20 sec                                                        | 1.85 sec: 1.19x faster                                                          |
| xml_etree_parse      | 113 ms                                                          | 104 ms: 1.08x faster                                                            |
| unpickle_pure_python | 210 us                                                          | 203 us: 1.03x faster                                                            |
| xml_etree_generate   | 72.1 ms                                                         | 71.5 ms: 1.01x faster                                                           |
| json_loads           | 20.4 us                                                         | 20.5 us: 1.01x slower                                                           |
| pickle_pure_python   | 286 us                                                          | 304 us: 1.06x slower                                                            |
| json_dumps           | 7.40 ms                                                         | 9.01 ms: 1.22x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.03x faster                                                                    |

Benchmark hidden because not significant (1): xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241207-pythonperf1_win32-x86-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 19.6 ms: 1.03x slower                                                           |
| python_startup         | 22.4 ms                                                         | 26.3 ms: 1.18x slower                                                           |
| Geometric mean         | (ref)                                                           | 1.10x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241207-pythonperf1_win32-x86-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako           | 9.96 ms                                                         | 7.31 ms: 1.36x faster                                                           |
| Geometric mean | (ref)                                                           | 1.17x faster                                                                    |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241207-pythonperf1_win32-x86-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| deepcopy_memo              | 38.4 us                                                         | 24.3 us: 1.58x faster                                                           |
| async_tree_io_tg           | 677 ms                                                          | 451 ms: 1.50x faster                                                            |
| async_tree_io              | 693 ms                                                          | 480 ms: 1.44x faster                                                            |
| async_tree_none_tg         | 278 ms                                                          | 200 ms: 1.39x faster                                                            |
| async_tree_memoization_tg  | 350 ms                                                          | 252 ms: 1.39x faster                                                            |
| mako                       | 9.96 ms                                                         | 7.31 ms: 1.36x faster                                                           |
| float                      | 76.7 ms                                                         | 57.5 ms: 1.33x faster                                                           |
| async_tree_none            | 298 ms                                                          | 228 ms: 1.31x faster                                                            |
| spectral_norm              | 104 ms                                                          | 79.9 ms: 1.30x faster                                                           |
| scimark_lu                 | 93.2 ms                                                         | 72.2 ms: 1.29x faster                                                           |
| async_tree_memoization     | 364 ms                                                          | 282 ms: 1.29x faster                                                            |
| deepcopy                   | 360 us                                                          | 281 us: 1.28x faster                                                            |
| regex_effbot               | 2.04 ms                                                         | 1.59 ms: 1.28x faster                                                           |
| nbody                      | 127 ms                                                          | 99.4 ms: 1.28x faster                                                           |
| scimark_sor                | 130 ms                                                          | 102 ms: 1.28x faster                                                            |
| coroutines                 | 20.9 ms                                                         | 16.6 ms: 1.26x faster                                                           |
| xml_etree_iterparse        | 77.6 ms                                                         | 63.4 ms: 1.22x faster                                                           |
| logging_silent             | 101 ns                                                          | 83.1 ns: 1.22x faster                                                           |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 3.21 ms: 1.20x faster                                                           |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 456 ms: 1.20x faster                                                            |
| tomli_loads                | 2.20 sec                                                        | 1.85 sec: 1.19x faster                                                          |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 480 ms: 1.17x faster                                                            |
| logging_simple             | 9.75 us                                                         | 8.42 us: 1.16x faster                                                           |
| logging_format             | 10.4 us                                                         | 9.07 us: 1.15x faster                                                           |
| go                         | 137 ms                                                          | 121 ms: 1.13x faster                                                            |
| deepcopy_reduce            | 3.23 us                                                         | 2.85 us: 1.13x faster                                                           |
| regex_compile              | 129 ms                                                          | 115 ms: 1.13x faster                                                            |
| dulwich_log                | 58.5 ms                                                         | 52.0 ms: 1.12x faster                                                           |
| pathlib                    | 91.4 ms                                                         | 81.4 ms: 1.12x faster                                                           |
| deltablue                  | 3.58 ms                                                         | 3.19 ms: 1.12x faster                                                           |
| regex_dna                  | 127 ms                                                          | 115 ms: 1.10x faster                                                            |
| scimark_fft                | 271 ms                                                          | 246 ms: 1.10x faster                                                            |
| xml_etree_parse            | 113 ms                                                          | 104 ms: 1.08x faster                                                            |
| pyflate                    | 424 ms                                                          | 391 ms: 1.08x faster                                                            |
| 2to3                       | 280 ms                                                          | 259 ms: 1.08x faster                                                            |
| scimark_monte_carlo        | 66.4 ms                                                         | 61.9 ms: 1.07x faster                                                           |
| pycparser                  | 978 ms                                                          | 913 ms: 1.07x faster                                                            |
| bench_thread_pool          | 1.10 ms                                                         | 1.03 ms: 1.07x faster                                                           |
| chaos                      | 69.4 ms                                                         | 65.1 ms: 1.07x faster                                                           |
| sympy_sum                  | 123 ms                                                          | 115 ms: 1.06x faster                                                            |
| fannkuch                   | 354 ms                                                          | 335 ms: 1.06x faster                                                            |
| sqlglot_parse              | 1.25 ms                                                         | 1.19 ms: 1.05x faster                                                           |
| sqlglot_transpile          | 1.53 ms                                                         | 1.47 ms: 1.04x faster                                                           |
| crypto_pyaes               | 69.2 ms                                                         | 66.6 ms: 1.04x faster                                                           |
| sqlite_synth               | 2.07 us                                                         | 1.99 us: 1.04x faster                                                           |
| unpickle_pure_python       | 210 us                                                          | 203 us: 1.03x faster                                                            |
| mdp                        | 1.91 sec                                                        | 1.85 sec: 1.03x faster                                                          |
| comprehensions             | 19.2 us                                                         | 18.7 us: 1.03x faster                                                           |
| raytrace                   | 308 ms                                                          | 301 ms: 1.02x faster                                                            |
| sympy_str                  | 240 ms                                                          | 235 ms: 1.02x faster                                                            |
| generators                 | 38.5 ms                                                         | 37.8 ms: 1.02x faster                                                           |
| docutils                   | 1.98 sec                                                        | 1.95 sec: 1.02x faster                                                          |
| xml_etree_generate         | 72.1 ms                                                         | 71.5 ms: 1.01x faster                                                           |
| pprint_pformat             | 1.50 sec                                                        | 1.51 sec: 1.00x slower                                                          |
| pidigits                   | 199 ms                                                          | 200 ms: 1.01x slower                                                            |
| json_loads                 | 20.4 us                                                         | 20.5 us: 1.01x slower                                                           |
| pprint_safe_repr           | 721 ms                                                          | 732 ms: 1.02x slower                                                            |
| sympy_expand               | 398 ms                                                          | 408 ms: 1.03x slower                                                            |
| python_startup_no_site     | 19.1 ms                                                         | 19.6 ms: 1.03x slower                                                           |
| hexiom                     | 6.82 ms                                                         | 7.02 ms: 1.03x slower                                                           |
| meteor_contest             | 86.9 ms                                                         | 89.8 ms: 1.03x slower                                                           |
| async_generators           | 313 ms                                                          | 326 ms: 1.04x slower                                                            |
| regex_v8                   | 15.0 ms                                                         | 15.7 ms: 1.05x slower                                                           |
| richards_super             | 46.5 ms                                                         | 49.3 ms: 1.06x slower                                                           |
| nqueens                    | 93.7 ms                                                         | 99.5 ms: 1.06x slower                                                           |
| pickle_pure_python         | 286 us                                                          | 304 us: 1.06x slower                                                            |
| json                       | 4.15 ms                                                         | 4.43 ms: 1.07x slower                                                           |
| sqlglot_optimize           | 48.5 ms                                                         | 51.7 ms: 1.07x slower                                                           |
| richards                   | 41.3 ms                                                         | 44.4 ms: 1.08x slower                                                           |
| sqlglot_normalize          | 100 ms                                                          | 110 ms: 1.09x slower                                                            |
| coverage                   | 48.4 ms                                                         | 54.7 ms: 1.13x slower                                                           |
| bench_mp_pool              | 75.4 ms                                                         | 87.0 ms: 1.15x slower                                                           |
| python_startup             | 22.4 ms                                                         | 26.3 ms: 1.18x slower                                                           |
| json_dumps                 | 7.40 ms                                                         | 9.01 ms: 1.22x slower                                                           |
| gc_traversal               | 1.44 ms                                                         | 1.76 ms: 1.22x slower                                                           |
| telco                      | 5.51 ms                                                         | 7.19 ms: 1.30x slower                                                           |
| typing_runtime_protocols   | 126 us                                                          | 166 us: 1.32x slower                                                            |
| create_gc_cycles           | 652 us                                                          | 981 us: 1.50x slower                                                            |
| Geometric mean             | (ref)                                                           | 1.07x faster                                                                    |

Benchmark hidden because not significant (3): django_template, xml_etree_process, sympy_integrate
Ignored benchmarks (15) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20241207-3.14.0a2+-79b7cab-JIT/bm-20241207-pythonperf1_win32-x86-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.072x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: unknown