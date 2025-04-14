# Results vs. 3.12.0

- fork: python
- ref: 425f60b9eb253c57bc32
- machine: windows-x86
- commit hash: 425f60b
- commit date: 2025-03-29
- overall geometric mean: 1.079x faster
- HPT reliability: 99.75%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250329-pythonperf1_win32-x86-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 283 ms: 1.01x slower                                                            |
| docutils       | 1.98 sec                                                        | 1.99 sec: 1.00x slower                                                          |
| Geometric mean | (ref)                                                           | 1.01x slower                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250329-pythonperf1_win32-x86-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_io_tg           | 677 ms                                                          | 473 ms: 1.43x faster                                                            |
| async_tree_io              | 693 ms                                                          | 494 ms: 1.40x faster                                                            |
| async_tree_memoization_tg  | 350 ms                                                          | 257 ms: 1.36x faster                                                            |
| async_tree_memoization     | 364 ms                                                          | 271 ms: 1.34x faster                                                            |
| async_tree_none_tg         | 278 ms                                                          | 211 ms: 1.31x faster                                                            |
| async_tree_none            | 298 ms                                                          | 232 ms: 1.28x faster                                                            |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 515 ms: 1.10x faster                                                            |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 501 ms: 1.09x faster                                                            |
| Geometric mean             | (ref)                                                           | 1.28x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250329-pythonperf1_win32-x86-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 76.7 ms                                                         | 57.5 ms: 1.33x faster                                                           |
| nbody          | 127 ms                                                          | 112 ms: 1.13x faster                                                            |
| pidigits       | 199 ms                                                          | 202 ms: 1.01x slower                                                            |
| Geometric mean | (ref)                                                           | 1.14x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250329-pythonperf1_win32-x86-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_effbot   | 2.04 ms                                                         | 1.58 ms: 1.29x faster                                                           |
| regex_compile  | 129 ms                                                          | 114 ms: 1.13x faster                                                            |
| regex_dna      | 127 ms                                                          | 114 ms: 1.11x faster                                                            |
| regex_v8       | 15.0 ms                                                         | 14.5 ms: 1.04x faster                                                           |
| Geometric mean | (ref)                                                           | 1.14x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250329-pythonperf1_win32-x86-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 2.20 sec                                                        | 1.87 sec: 1.18x faster                                                          |
| xml_etree_iterparse  | 77.6 ms                                                         | 68.1 ms: 1.14x faster                                                           |
| xml_etree_parse      | 113 ms                                                          | 110 ms: 1.02x faster                                                            |
| xml_etree_generate   | 72.1 ms                                                         | 72.6 ms: 1.01x slower                                                           |
| unpickle             | 9.71 us                                                         | 10.2 us: 1.06x slower                                                           |
| xml_etree_process    | 53.2 ms                                                         | 56.3 ms: 1.06x slower                                                           |
| json_loads           | 20.4 us                                                         | 21.7 us: 1.07x slower                                                           |
| pickle_dict          | 19.9 us                                                         | 21.4 us: 1.08x slower                                                           |
| pickle_list          | 3.37 us                                                         | 3.75 us: 1.11x slower                                                           |
| json_dumps           | 7.40 ms                                                         | 8.35 ms: 1.13x slower                                                           |
| unpickle_pure_python | 210 us                                                          | 239 us: 1.14x slower                                                            |
| pickle_pure_python   | 286 us                                                          | 326 us: 1.14x slower                                                            |
| pickle               | 7.79 us                                                         | 9.49 us: 1.22x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.05x slower                                                                    |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250329-pythonperf1_win32-x86-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 22.9 ms: 1.20x slower                                                           |
| python_startup         | 22.4 ms                                                         | 29.0 ms: 1.30x slower                                                           |
| Geometric mean         | (ref)                                                           | 1.25x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250329-pythonperf1_win32-x86-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 8.18 ms: 1.22x faster                                                           |
| django_template | 36.9 ms                                                         | 35.7 ms: 1.03x faster                                                           |
| Geometric mean  | (ref)                                                           | 1.12x faster                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250329-pythonperf1_win32-x86-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pathlib                    | 91.4 ms                                                         | 37.5 ms: 2.44x faster                                                           |
| mdp                        | 1.91 sec                                                        | 1.13 sec: 1.69x faster                                                          |
| deepcopy_memo              | 38.4 us                                                         | 23.3 us: 1.64x faster                                                           |
| async_tree_io_tg           | 677 ms                                                          | 473 ms: 1.43x faster                                                            |
| generators                 | 38.5 ms                                                         | 27.0 ms: 1.43x faster                                                           |
| deepcopy                   | 360 us                                                          | 254 us: 1.42x faster                                                            |
| async_tree_io              | 693 ms                                                          | 494 ms: 1.40x faster                                                            |
| async_tree_memoization_tg  | 350 ms                                                          | 257 ms: 1.36x faster                                                            |
| logging_silent             | 101 ns                                                          | 75.3 ns: 1.34x faster                                                           |
| async_tree_memoization     | 364 ms                                                          | 271 ms: 1.34x faster                                                            |
| float                      | 76.7 ms                                                         | 57.5 ms: 1.33x faster                                                           |
| spectral_norm              | 104 ms                                                          | 78.6 ms: 1.32x faster                                                           |
| async_tree_none_tg         | 278 ms                                                          | 211 ms: 1.31x faster                                                            |
| scimark_sor                | 130 ms                                                          | 101 ms: 1.29x faster                                                            |
| regex_effbot               | 2.04 ms                                                         | 1.58 ms: 1.29x faster                                                           |
| async_tree_none            | 298 ms                                                          | 232 ms: 1.28x faster                                                            |
| deepcopy_reduce            | 3.23 us                                                         | 2.62 us: 1.23x faster                                                           |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 3.14 ms: 1.23x faster                                                           |
| mako                       | 9.96 ms                                                         | 8.18 ms: 1.22x faster                                                           |
| scimark_lu                 | 93.2 ms                                                         | 76.8 ms: 1.21x faster                                                           |
| scimark_monte_carlo        | 66.4 ms                                                         | 54.7 ms: 1.21x faster                                                           |
| unpack_sequence            | 62.5 ns                                                         | 51.7 ns: 1.21x faster                                                           |
| raytrace                   | 308 ms                                                          | 255 ms: 1.21x faster                                                            |
| go                         | 137 ms                                                          | 114 ms: 1.20x faster                                                            |
| tomli_loads                | 2.20 sec                                                        | 1.87 sec: 1.18x faster                                                          |
| coroutines                 | 20.9 ms                                                         | 17.8 ms: 1.17x faster                                                           |
| chaos                      | 69.4 ms                                                         | 59.5 ms: 1.17x faster                                                           |
| deltablue                  | 3.58 ms                                                         | 3.10 ms: 1.16x faster                                                           |
| xml_etree_iterparse        | 77.6 ms                                                         | 68.1 ms: 1.14x faster                                                           |
| nbody                      | 127 ms                                                          | 112 ms: 1.13x faster                                                            |
| regex_compile              | 129 ms                                                          | 114 ms: 1.13x faster                                                            |
| pyflate                    | 424 ms                                                          | 377 ms: 1.12x faster                                                            |
| logging_simple             | 9.75 us                                                         | 8.76 us: 1.11x faster                                                           |
| regex_dna                  | 127 ms                                                          | 114 ms: 1.11x faster                                                            |
| dulwich_log                | 58.5 ms                                                         | 53.0 ms: 1.10x faster                                                           |
| logging_format             | 10.4 us                                                         | 9.45 us: 1.10x faster                                                           |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 515 ms: 1.10x faster                                                            |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 501 ms: 1.09x faster                                                            |
| sqlite_synth               | 2.07 us                                                         | 1.91 us: 1.09x faster                                                           |
| sympy_sum                  | 123 ms                                                          | 114 ms: 1.08x faster                                                            |
| sympy_integrate            | 17.5 ms                                                         | 16.7 ms: 1.05x faster                                                           |
| asyncio_tcp                | 662 ms                                                          | 634 ms: 1.04x faster                                                            |
| regex_v8                   | 15.0 ms                                                         | 14.5 ms: 1.04x faster                                                           |
| django_template            | 36.9 ms                                                         | 35.7 ms: 1.03x faster                                                           |
| comprehensions             | 19.2 us                                                         | 18.6 us: 1.03x faster                                                           |
| xml_etree_parse            | 113 ms                                                          | 110 ms: 1.02x faster                                                            |
| scimark_fft                | 271 ms                                                          | 265 ms: 1.02x faster                                                            |
| sympy_str                  | 240 ms                                                          | 236 ms: 1.01x faster                                                            |
| hexiom                     | 6.82 ms                                                         | 6.75 ms: 1.01x faster                                                           |
| docutils                   | 1.98 sec                                                        | 1.99 sec: 1.00x slower                                                          |
| xml_etree_generate         | 72.1 ms                                                         | 72.6 ms: 1.01x slower                                                           |
| asyncio_tcp_ssl            | 17.7 sec                                                        | 17.8 sec: 1.01x slower                                                          |
| 2to3                       | 280 ms                                                          | 283 ms: 1.01x slower                                                            |
| pidigits                   | 199 ms                                                          | 202 ms: 1.01x slower                                                            |
| richards_super             | 46.5 ms                                                         | 47.5 ms: 1.02x slower                                                           |
| richards                   | 41.3 ms                                                         | 42.3 ms: 1.02x slower                                                           |
| pycparser                  | 978 ms                                                          | 1.01 sec: 1.03x slower                                                          |
| unpickle                   | 9.71 us                                                         | 10.2 us: 1.06x slower                                                           |
| xml_etree_process          | 53.2 ms                                                         | 56.3 ms: 1.06x slower                                                           |
| sympy_expand               | 398 ms                                                          | 421 ms: 1.06x slower                                                            |
| meteor_contest             | 86.9 ms                                                         | 92.2 ms: 1.06x slower                                                           |
| fannkuch                   | 354 ms                                                          | 376 ms: 1.06x slower                                                            |
| json_loads                 | 20.4 us                                                         | 21.7 us: 1.07x slower                                                           |
| pprint_pformat             | 1.50 sec                                                        | 1.61 sec: 1.07x slower                                                          |
| pickle_dict                | 19.9 us                                                         | 21.4 us: 1.08x slower                                                           |
| async_generators           | 313 ms                                                          | 338 ms: 1.08x slower                                                            |
| pprint_safe_repr           | 721 ms                                                          | 786 ms: 1.09x slower                                                            |
| pickle_list                | 3.37 us                                                         | 3.75 us: 1.11x slower                                                           |
| json                       | 4.15 ms                                                         | 4.66 ms: 1.12x slower                                                           |
| json_dumps                 | 7.40 ms                                                         | 8.35 ms: 1.13x slower                                                           |
| coverage                   | 48.4 ms                                                         | 55.0 ms: 1.14x slower                                                           |
| unpickle_pure_python       | 210 us                                                          | 239 us: 1.14x slower                                                            |
| pickle_pure_python         | 286 us                                                          | 326 us: 1.14x slower                                                            |
| python_startup_no_site     | 19.1 ms                                                         | 22.9 ms: 1.20x slower                                                           |
| crypto_pyaes               | 69.2 ms                                                         | 83.3 ms: 1.20x slower                                                           |
| pickle                     | 7.79 us                                                         | 9.49 us: 1.22x slower                                                           |
| bench_thread_pool          | 1.10 ms                                                         | 1.34 ms: 1.22x slower                                                           |
| bench_mp_pool              | 75.4 ms                                                         | 95.6 ms: 1.27x slower                                                           |
| gc_traversal               | 1.44 ms                                                         | 1.87 ms: 1.30x slower                                                           |
| python_startup             | 22.4 ms                                                         | 29.0 ms: 1.30x slower                                                           |
| telco                      | 5.51 ms                                                         | 7.75 ms: 1.41x slower                                                           |
| typing_runtime_protocols   | 126 us                                                          | 180 us: 1.43x slower                                                            |
| create_gc_cycles           | 652 us                                                          | 1.07 ms: 1.63x slower                                                           |
| Geometric mean             | (ref)                                                           | 1.06x faster                                                                    |

Benchmark hidden because not significant (2): unpickle_list, nqueens
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250329-3.14.0a6+-425f60b-JIT/bm-20250329-pythonperf1_win32-x86-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.079x faster

# HPT report

- Reliability score: 99.75% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown