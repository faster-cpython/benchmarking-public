# Results vs. 3.12.0

- fork: python
- ref: 425f60b9eb253c57bc32
- machine: windows-x86
- commit hash: 425f60b
- commit date: 2025-03-29
- overall geometric mean: 1.038x faster
- HPT reliability: 88.08%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250329-pythonperf1_win32-x86-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| docutils       | 1.98 sec                                                        | 3.16 sec: 1.59x slower                                                          |
| Geometric mean | (ref)                                                           | 1.26x slower                                                                    |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250329-pythonperf1_win32-x86-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_io_tg           | 677 ms                                                          | 416 ms: 1.63x faster                                                            |
| async_tree_io              | 693 ms                                                          | 445 ms: 1.56x faster                                                            |
| async_tree_memoization_tg  | 350 ms                                                          | 236 ms: 1.49x faster                                                            |
| async_tree_none            | 298 ms                                                          | 215 ms: 1.39x faster                                                            |
| async_tree_memoization     | 364 ms                                                          | 265 ms: 1.37x faster                                                            |
| async_tree_none_tg         | 278 ms                                                          | 204 ms: 1.36x faster                                                            |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 428 ms: 1.28x faster                                                            |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 459 ms: 1.23x faster                                                            |
| Geometric mean             | (ref)                                                           | 1.41x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250329-pythonperf1_win32-x86-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 76.7 ms                                                         | 62.5 ms: 1.23x faster                                                           |
| pidigits       | 199 ms                                                          | 187 ms: 1.06x faster                                                            |
| nbody          | 127 ms                                                          | 133 ms: 1.05x slower                                                            |
| Geometric mean | (ref)                                                           | 1.08x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250329-pythonperf1_win32-x86-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_effbot   | 2.04 ms                                                         | 1.54 ms: 1.32x faster                                                           |
| regex_dna      | 127 ms                                                          | 107 ms: 1.18x faster                                                            |
| regex_v8       | 15.0 ms                                                         | 13.5 ms: 1.12x faster                                                           |
| regex_compile  | 129 ms                                                          | 127 ms: 1.02x faster                                                            |
| Geometric mean | (ref)                                                           | 1.16x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250329-pythonperf1_win32-x86-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|---------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| xml_etree_iterparse | 77.6 ms                                                         | 67.0 ms: 1.16x faster                                                           |
| xml_etree_parse     | 113 ms                                                          | 107 ms: 1.06x faster                                                            |
| xml_etree_generate  | 72.1 ms                                                         | 73.3 ms: 1.02x slower                                                           |
| xml_etree_process   | 53.2 ms                                                         | 54.8 ms: 1.03x slower                                                           |
| pickle_pure_python  | 286 us                                                          | 301 us: 1.05x slower                                                            |
| pickle_list         | 3.37 us                                                         | 3.87 us: 1.15x slower                                                           |
| json_dumps          | 7.40 ms                                                         | 8.81 ms: 1.19x slower                                                           |
| pickle_dict         | 19.9 us                                                         | 24.3 us: 1.22x slower                                                           |
| unpickle_list       | 2.95 us                                                         | 3.64 us: 1.24x slower                                                           |
| json_loads          | 20.4 us                                                         | 25.6 us: 1.26x slower                                                           |
| unpickle            | 9.71 us                                                         | 12.3 us: 1.27x slower                                                           |
| pickle              | 7.79 us                                                         | 10.3 us: 1.33x slower                                                           |
| tomli_loads         | 2.20 sec                                                        | 3.64 sec: 1.66x slower                                                          |
| Geometric mean      | (ref)                                                           | 1.14x slower                                                                    |

Benchmark hidden because not significant (1): unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250329-pythonperf1_win32-x86-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 23.8 ms: 1.25x slower                                                           |
| python_startup         | 22.4 ms                                                         | 29.8 ms: 1.33x slower                                                           |
| Geometric mean         | (ref)                                                           | 1.29x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250329-pythonperf1_win32-x86-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| django_template | 36.9 ms                                                         | 38.8 ms: 1.05x slower                                                           |
| mako            | 9.96 ms                                                         | 11.7 ms: 1.17x slower                                                           |
| Geometric mean  | (ref)                                                           | 1.11x slower                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250329-pythonperf1_win32-x86-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pathlib                    | 91.4 ms                                                         | 37.8 ms: 2.42x faster                                                           |
| async_tree_io_tg           | 677 ms                                                          | 416 ms: 1.63x faster                                                            |
| async_tree_io              | 693 ms                                                          | 445 ms: 1.56x faster                                                            |
| generators                 | 38.5 ms                                                         | 25.9 ms: 1.49x faster                                                           |
| async_tree_memoization_tg  | 350 ms                                                          | 236 ms: 1.49x faster                                                            |
| deepcopy_memo              | 38.4 us                                                         | 27.0 us: 1.42x faster                                                           |
| async_tree_none            | 298 ms                                                          | 215 ms: 1.39x faster                                                            |
| async_tree_memoization     | 364 ms                                                          | 265 ms: 1.37x faster                                                            |
| async_tree_none_tg         | 278 ms                                                          | 204 ms: 1.36x faster                                                            |
| gc_traversal               | 1.44 ms                                                         | 1.07 ms: 1.34x faster                                                           |
| regex_effbot               | 2.04 ms                                                         | 1.54 ms: 1.32x faster                                                           |
| deepcopy                   | 360 us                                                          | 280 us: 1.29x faster                                                            |
| sqlite_synth               | 2.07 us                                                         | 1.61 us: 1.28x faster                                                           |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 428 ms: 1.28x faster                                                            |
| mdp                        | 1.91 sec                                                        | 1.52 sec: 1.26x faster                                                          |
| logging_silent             | 101 ns                                                          | 80.9 ns: 1.25x faster                                                           |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 459 ms: 1.23x faster                                                            |
| float                      | 76.7 ms                                                         | 62.5 ms: 1.23x faster                                                           |
| coroutines                 | 20.9 ms                                                         | 17.1 ms: 1.22x faster                                                           |
| unpack_sequence            | 62.5 ns                                                         | 52.1 ns: 1.20x faster                                                           |
| scimark_sor                | 130 ms                                                          | 108 ms: 1.20x faster                                                            |
| spectral_norm              | 104 ms                                                          | 86.9 ms: 1.19x faster                                                           |
| regex_dna                  | 127 ms                                                          | 107 ms: 1.18x faster                                                            |
| xml_etree_iterparse        | 77.6 ms                                                         | 67.0 ms: 1.16x faster                                                           |
| deltablue                  | 3.58 ms                                                         | 3.11 ms: 1.15x faster                                                           |
| comprehensions             | 19.2 us                                                         | 16.8 us: 1.14x faster                                                           |
| hexiom                     | 6.82 ms                                                         | 6.07 ms: 1.12x faster                                                           |
| scimark_lu                 | 93.2 ms                                                         | 83.4 ms: 1.12x faster                                                           |
| regex_v8                   | 15.0 ms                                                         | 13.5 ms: 1.12x faster                                                           |
| raytrace                   | 308 ms                                                          | 280 ms: 1.10x faster                                                            |
| asyncio_tcp                | 662 ms                                                          | 610 ms: 1.09x faster                                                            |
| dulwich_log                | 58.5 ms                                                         | 54.3 ms: 1.08x faster                                                           |
| deepcopy_reduce            | 3.23 us                                                         | 3.02 us: 1.07x faster                                                           |
| pidigits                   | 199 ms                                                          | 187 ms: 1.06x faster                                                            |
| xml_etree_parse            | 113 ms                                                          | 107 ms: 1.06x faster                                                            |
| logging_simple             | 9.75 us                                                         | 9.31 us: 1.05x faster                                                           |
| chaos                      | 69.4 ms                                                         | 66.4 ms: 1.04x faster                                                           |
| nqueens                    | 93.7 ms                                                         | 90.0 ms: 1.04x faster                                                           |
| logging_format             | 10.4 us                                                         | 10.0 us: 1.04x faster                                                           |
| go                         | 137 ms                                                          | 133 ms: 1.03x faster                                                            |
| regex_compile              | 129 ms                                                          | 127 ms: 1.02x faster                                                            |
| pyflate                    | 424 ms                                                          | 417 ms: 1.02x faster                                                            |
| sympy_sum                  | 123 ms                                                          | 125 ms: 1.02x slower                                                            |
| xml_etree_generate         | 72.1 ms                                                         | 73.3 ms: 1.02x slower                                                           |
| xml_etree_process          | 53.2 ms                                                         | 54.8 ms: 1.03x slower                                                           |
| sympy_integrate            | 17.5 ms                                                         | 18.1 ms: 1.03x slower                                                           |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 3.98 ms: 1.03x slower                                                           |
| scimark_monte_carlo        | 66.4 ms                                                         | 69.1 ms: 1.04x slower                                                           |
| sympy_str                  | 240 ms                                                          | 250 ms: 1.04x slower                                                            |
| nbody                      | 127 ms                                                          | 133 ms: 1.05x slower                                                            |
| pickle_pure_python         | 286 us                                                          | 301 us: 1.05x slower                                                            |
| django_template            | 36.9 ms                                                         | 38.8 ms: 1.05x slower                                                           |
| scimark_fft                | 271 ms                                                          | 288 ms: 1.06x slower                                                            |
| crypto_pyaes               | 69.2 ms                                                         | 74.7 ms: 1.08x slower                                                           |
| sympy_expand               | 398 ms                                                          | 431 ms: 1.08x slower                                                            |
| bench_mp_pool              | 75.4 ms                                                         | 82.2 ms: 1.09x slower                                                           |
| fannkuch                   | 354 ms                                                          | 389 ms: 1.10x slower                                                            |
| meteor_contest             | 86.9 ms                                                         | 96.3 ms: 1.11x slower                                                           |
| richards_super             | 46.5 ms                                                         | 52.7 ms: 1.13x slower                                                           |
| pickle_list                | 3.37 us                                                         | 3.87 us: 1.15x slower                                                           |
| richards                   | 41.3 ms                                                         | 47.9 ms: 1.16x slower                                                           |
| bench_thread_pool          | 1.10 ms                                                         | 1.29 ms: 1.17x slower                                                           |
| json                       | 4.15 ms                                                         | 4.85 ms: 1.17x slower                                                           |
| mako                       | 9.96 ms                                                         | 11.7 ms: 1.17x slower                                                           |
| pprint_safe_repr           | 721 ms                                                          | 857 ms: 1.19x slower                                                            |
| json_dumps                 | 7.40 ms                                                         | 8.81 ms: 1.19x slower                                                           |
| pycparser                  | 978 ms                                                          | 1.18 sec: 1.21x slower                                                          |
| pickle_dict                | 19.9 us                                                         | 24.3 us: 1.22x slower                                                           |
| unpickle_list              | 2.95 us                                                         | 3.64 us: 1.24x slower                                                           |
| python_startup_no_site     | 19.1 ms                                                         | 23.8 ms: 1.25x slower                                                           |
| json_loads                 | 20.4 us                                                         | 25.6 us: 1.26x slower                                                           |
| unpickle                   | 9.71 us                                                         | 12.3 us: 1.27x slower                                                           |
| asyncio_tcp_ssl            | 17.7 sec                                                        | 22.6 sec: 1.28x slower                                                          |
| pickle                     | 7.79 us                                                         | 10.3 us: 1.33x slower                                                           |
| python_startup             | 22.4 ms                                                         | 29.8 ms: 1.33x slower                                                           |
| create_gc_cycles           | 652 us                                                          | 872 us: 1.34x slower                                                            |
| telco                      | 5.51 ms                                                         | 7.44 ms: 1.35x slower                                                           |
| typing_runtime_protocols   | 126 us                                                          | 180 us: 1.43x slower                                                            |
| coverage                   | 48.4 ms                                                         | 74.0 ms: 1.53x slower                                                           |
| docutils                   | 1.98 sec                                                        | 3.16 sec: 1.59x slower                                                          |
| tomli_loads                | 2.20 sec                                                        | 3.64 sec: 1.66x slower                                                          |
| pprint_pformat             | 1.50 sec                                                        | 2.49 sec: 1.66x slower                                                          |
| Geometric mean             | (ref)                                                           | 1.02x faster                                                                    |

Benchmark hidden because not significant (3): 2to3, async_generators, unpickle_pure_python
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (17) of results/bm-20250329-3.14.0a6+-425f60b-NOGIL/bm-20250329-pythonperf1_win32-x86-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.038x faster

# HPT report

- Reliability score: 88.08% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown