# Results vs. 3.12.0

- fork: brandtbucher
- ref: nojit
- machine: windows-x86
- commit hash: f098037
- commit date: 2025-01-07
- overall geometric mean: 1.077x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.02x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250107-pythonperf1_win32-x86-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 263 ms: 1.06x faster                                                   |
| docutils       | 1.98 sec                                                        | 1.95 sec: 1.02x faster                                                 |
| Geometric mean | (ref)                                                           | 1.04x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250107-pythonperf1_win32-x86-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io_tg           | 677 ms                                                          | 444 ms: 1.52x faster                                                   |
| async_tree_io              | 693 ms                                                          | 470 ms: 1.47x faster                                                   |
| async_tree_none_tg         | 278 ms                                                          | 189 ms: 1.47x faster                                                   |
| async_tree_memoization_tg  | 350 ms                                                          | 241 ms: 1.46x faster                                                   |
| async_tree_none            | 298 ms                                                          | 223 ms: 1.33x faster                                                   |
| async_tree_memoization     | 364 ms                                                          | 273 ms: 1.33x faster                                                   |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 453 ms: 1.21x faster                                                   |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 473 ms: 1.19x faster                                                   |
| Geometric mean             | (ref)                                                           | 1.37x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250107-pythonperf1_win32-x86-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 76.7 ms                                                         | 52.2 ms: 1.47x faster                                                  |
| nbody          | 127 ms                                                          | 102 ms: 1.25x faster                                                   |
| pidigits       | 199 ms                                                          | 201 ms: 1.01x slower                                                   |
| Geometric mean | (ref)                                                           | 1.22x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250107-pythonperf1_win32-x86-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_effbot   | 2.04 ms                                                         | 1.65 ms: 1.24x faster                                                  |
| regex_compile  | 129 ms                                                          | 112 ms: 1.15x faster                                                   |
| regex_dna      | 127 ms                                                          | 124 ms: 1.03x faster                                                   |
| regex_v8       | 15.0 ms                                                         | 15.7 ms: 1.04x slower                                                  |
| Geometric mean | (ref)                                                           | 1.09x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250107-pythonperf1_win32-x86-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 2.20 sec                                                        | 1.76 sec: 1.25x faster                                                 |
| xml_etree_iterparse  | 77.6 ms                                                         | 66.6 ms: 1.17x faster                                                  |
| xml_etree_parse      | 113 ms                                                          | 107 ms: 1.05x faster                                                   |
| unpickle_pure_python | 210 us                                                          | 203 us: 1.03x faster                                                   |
| xml_etree_generate   | 72.1 ms                                                         | 72.8 ms: 1.01x slower                                                  |
| json_loads           | 20.4 us                                                         | 20.6 us: 1.01x slower                                                  |
| pickle_pure_python   | 286 us                                                          | 294 us: 1.03x slower                                                   |
| json_dumps           | 7.40 ms                                                         | 9.18 ms: 1.24x slower                                                  |
| Geometric mean       | (ref)                                                           | 1.02x faster                                                           |

Benchmark hidden because not significant (1): xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250107-pythonperf1_win32-x86-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup | 22.4 ms                                                         | 25.7 ms: 1.15x slower                                                  |
| Geometric mean | (ref)                                                           | 1.07x slower                                                           |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250107-pythonperf1_win32-x86-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako           | 9.96 ms                                                         | 7.59 ms: 1.31x faster                                                  |
| Geometric mean | (ref)                                                           | 1.15x faster                                                           |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250107-pythonperf1_win32-x86-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------:|
| deepcopy_memo              | 38.4 us                                                         | 22.8 us: 1.69x faster                                                  |
| async_tree_io_tg           | 677 ms                                                          | 444 ms: 1.52x faster                                                   |
| async_tree_io              | 693 ms                                                          | 470 ms: 1.47x faster                                                   |
| async_tree_none_tg         | 278 ms                                                          | 189 ms: 1.47x faster                                                   |
| float                      | 76.7 ms                                                         | 52.2 ms: 1.47x faster                                                  |
| async_tree_memoization_tg  | 350 ms                                                          | 241 ms: 1.46x faster                                                   |
| scimark_sor                | 130 ms                                                          | 92.7 ms: 1.40x faster                                                  |
| spectral_norm              | 104 ms                                                          | 74.7 ms: 1.39x faster                                                  |
| async_tree_none            | 298 ms                                                          | 223 ms: 1.33x faster                                                   |
| async_tree_memoization     | 364 ms                                                          | 273 ms: 1.33x faster                                                   |
| deepcopy                   | 360 us                                                          | 273 us: 1.32x faster                                                   |
| mako                       | 9.96 ms                                                         | 7.59 ms: 1.31x faster                                                  |
| scimark_lu                 | 93.2 ms                                                         | 72.5 ms: 1.29x faster                                                  |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 3.08 ms: 1.25x faster                                                  |
| tomli_loads                | 2.20 sec                                                        | 1.76 sec: 1.25x faster                                                 |
| nbody                      | 127 ms                                                          | 102 ms: 1.25x faster                                                   |
| coroutines                 | 20.9 ms                                                         | 16.8 ms: 1.25x faster                                                  |
| regex_effbot               | 2.04 ms                                                         | 1.65 ms: 1.24x faster                                                  |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 453 ms: 1.21x faster                                                   |
| logging_silent             | 101 ns                                                          | 84.3 ns: 1.20x faster                                                  |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 473 ms: 1.19x faster                                                   |
| xml_etree_iterparse        | 77.6 ms                                                         | 66.6 ms: 1.17x faster                                                  |
| deepcopy_reduce            | 3.23 us                                                         | 2.79 us: 1.16x faster                                                  |
| dulwich_log                | 58.5 ms                                                         | 50.5 ms: 1.16x faster                                                  |
| regex_compile              | 129 ms                                                          | 112 ms: 1.15x faster                                                   |
| logging_simple             | 9.75 us                                                         | 8.54 us: 1.14x faster                                                  |
| logging_format             | 10.4 us                                                         | 9.18 us: 1.13x faster                                                  |
| deltablue                  | 3.58 ms                                                         | 3.17 ms: 1.13x faster                                                  |
| scimark_fft                | 271 ms                                                          | 240 ms: 1.13x faster                                                   |
| go                         | 137 ms                                                          | 124 ms: 1.11x faster                                                   |
| pathlib                    | 91.4 ms                                                         | 82.9 ms: 1.10x faster                                                  |
| sqlglot_parse              | 1.25 ms                                                         | 1.15 ms: 1.09x faster                                                  |
| sympy_sum                  | 123 ms                                                          | 114 ms: 1.08x faster                                                   |
| sqlite_synth               | 2.07 us                                                         | 1.92 us: 1.08x faster                                                  |
| scimark_monte_carlo        | 66.4 ms                                                         | 61.7 ms: 1.08x faster                                                  |
| sqlglot_transpile          | 1.53 ms                                                         | 1.42 ms: 1.08x faster                                                  |
| chaos                      | 69.4 ms                                                         | 64.7 ms: 1.07x faster                                                  |
| 2to3                       | 280 ms                                                          | 263 ms: 1.06x faster                                                   |
| pyflate                    | 424 ms                                                          | 399 ms: 1.06x faster                                                   |
| fannkuch                   | 354 ms                                                          | 334 ms: 1.06x faster                                                   |
| bench_thread_pool          | 1.10 ms                                                         | 1.04 ms: 1.06x faster                                                  |
| xml_etree_parse            | 113 ms                                                          | 107 ms: 1.05x faster                                                   |
| mdp                        | 1.91 sec                                                        | 1.84 sec: 1.04x faster                                                 |
| pycparser                  | 978 ms                                                          | 943 ms: 1.04x faster                                                   |
| comprehensions             | 19.2 us                                                         | 18.5 us: 1.04x faster                                                  |
| unpickle_pure_python       | 210 us                                                          | 203 us: 1.03x faster                                                   |
| regex_dna                  | 127 ms                                                          | 124 ms: 1.03x faster                                                   |
| sympy_str                  | 240 ms                                                          | 233 ms: 1.03x faster                                                   |
| generators                 | 38.5 ms                                                         | 37.6 ms: 1.02x faster                                                  |
| docutils                   | 1.98 sec                                                        | 1.95 sec: 1.02x faster                                                 |
| sympy_integrate            | 17.5 ms                                                         | 17.3 ms: 1.02x faster                                                  |
| pprint_pformat             | 1.50 sec                                                        | 1.49 sec: 1.01x faster                                                 |
| crypto_pyaes               | 69.2 ms                                                         | 68.9 ms: 1.00x faster                                                  |
| pidigits                   | 199 ms                                                          | 201 ms: 1.01x slower                                                   |
| xml_etree_generate         | 72.1 ms                                                         | 72.8 ms: 1.01x slower                                                  |
| json_loads                 | 20.4 us                                                         | 20.6 us: 1.01x slower                                                  |
| meteor_contest             | 86.9 ms                                                         | 88.3 ms: 1.02x slower                                                  |
| pprint_safe_repr           | 721 ms                                                          | 733 ms: 1.02x slower                                                   |
| sympy_expand               | 398 ms                                                          | 406 ms: 1.02x slower                                                   |
| pickle_pure_python         | 286 us                                                          | 294 us: 1.03x slower                                                   |
| nqueens                    | 93.7 ms                                                         | 96.5 ms: 1.03x slower                                                  |
| sqlglot_optimize           | 48.5 ms                                                         | 50.1 ms: 1.03x slower                                                  |
| richards_super             | 46.5 ms                                                         | 48.1 ms: 1.04x slower                                                  |
| async_generators           | 313 ms                                                          | 326 ms: 1.04x slower                                                   |
| hexiom                     | 6.82 ms                                                         | 7.10 ms: 1.04x slower                                                  |
| regex_v8                   | 15.0 ms                                                         | 15.7 ms: 1.04x slower                                                  |
| json                       | 4.15 ms                                                         | 4.34 ms: 1.04x slower                                                  |
| sqlglot_normalize          | 100 ms                                                          | 105 ms: 1.05x slower                                                   |
| richards                   | 41.3 ms                                                         | 43.5 ms: 1.05x slower                                                  |
| coverage                   | 48.4 ms                                                         | 51.9 ms: 1.07x slower                                                  |
| python_startup             | 22.4 ms                                                         | 25.7 ms: 1.15x slower                                                  |
| bench_mp_pool              | 75.4 ms                                                         | 87.4 ms: 1.16x slower                                                  |
| json_dumps                 | 7.40 ms                                                         | 9.18 ms: 1.24x slower                                                  |
| mypy2                      | 584 ms                                                          | 727 ms: 1.25x slower                                                   |
| typing_runtime_protocols   | 126 us                                                          | 159 us: 1.26x slower                                                   |
| gc_traversal               | 1.44 ms                                                         | 1.82 ms: 1.26x slower                                                  |
| telco                      | 5.51 ms                                                         | 7.18 ms: 1.30x slower                                                  |
| create_gc_cycles           | 652 us                                                          | 1.06 ms: 1.63x slower                                                  |
| Geometric mean             | (ref)                                                           | 1.08x faster                                                           |

Benchmark hidden because not significant (4): django_template, raytrace, xml_etree_process, python_startup_no_site
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20250107-3.14.0a3+-f098037-JIT/bm-20250107-pythonperf1_win32-x86-brandtbucher-nojit-3.14.0a3+-f098037.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.077x faster

# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: unknown