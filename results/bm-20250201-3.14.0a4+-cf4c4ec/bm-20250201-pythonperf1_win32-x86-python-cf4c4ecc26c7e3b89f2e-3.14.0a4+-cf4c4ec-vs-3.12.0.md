# Results vs. 3.12.0

- fork: python
- ref: cf4c4ecc26c7e3b89f2e
- machine: windows-x86
- commit hash: cf4c4ec
- commit date: 2025-02-01
- overall geometric mean: 1.133x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.11x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250201-pythonperf1_win32-x86-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 251 ms: 1.12x faster                                                            |
| docutils       | 1.98 sec                                                        | 1.83 sec: 1.08x faster                                                          |
| Geometric mean | (ref)                                                           | 1.10x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250201-pythonperf1_win32-x86-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_io              | 693 ms                                                          | 461 ms: 1.50x faster                                                            |
| async_tree_io_tg           | 677 ms                                                          | 461 ms: 1.47x faster                                                            |
| async_tree_none_tg         | 278 ms                                                          | 197 ms: 1.41x faster                                                            |
| async_tree_memoization_tg  | 350 ms                                                          | 250 ms: 1.40x faster                                                            |
| async_tree_none            | 298 ms                                                          | 216 ms: 1.38x faster                                                            |
| async_tree_memoization     | 364 ms                                                          | 264 ms: 1.38x faster                                                            |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 435 ms: 1.26x faster                                                            |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 451 ms: 1.25x faster                                                            |
| Geometric mean             | (ref)                                                           | 1.38x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250201-pythonperf1_win32-x86-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 89.4 ms: 1.42x faster                                                           |
| float          | 76.7 ms                                                         | 56.5 ms: 1.36x faster                                                           |
| pidigits       | 199 ms                                                          | 201 ms: 1.01x slower                                                            |
| Geometric mean | (ref)                                                           | 1.24x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250201-pythonperf1_win32-x86-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_effbot   | 2.04 ms                                                         | 1.55 ms: 1.32x faster                                                           |
| regex_compile  | 129 ms                                                          | 105 ms: 1.23x faster                                                            |
| regex_dna      | 127 ms                                                          | 116 ms: 1.09x faster                                                            |
| regex_v8       | 15.0 ms                                                         | 15.7 ms: 1.04x slower                                                           |
| Geometric mean | (ref)                                                           | 1.14x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250201-pythonperf1_win32-x86-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 2.20 sec                                                        | 1.69 sec: 1.30x faster                                                          |
| unpickle_pure_python | 210 us                                                          | 179 us: 1.17x faster                                                            |
| xml_etree_iterparse  | 77.6 ms                                                         | 66.9 ms: 1.16x faster                                                           |
| xml_etree_process    | 53.2 ms                                                         | 49.6 ms: 1.07x faster                                                           |
| xml_etree_generate   | 72.1 ms                                                         | 68.0 ms: 1.06x faster                                                           |
| pickle_pure_python   | 286 us                                                          | 274 us: 1.04x faster                                                            |
| xml_etree_parse      | 113 ms                                                          | 109 ms: 1.04x faster                                                            |
| pickle_dict          | 19.9 us                                                         | 21.1 us: 1.06x slower                                                           |
| pickle_list          | 3.37 us                                                         | 3.68 us: 1.09x slower                                                           |
| json_loads           | 20.4 us                                                         | 22.4 us: 1.10x slower                                                           |
| unpickle             | 9.71 us                                                         | 11.0 us: 1.13x slower                                                           |
| pickle               | 7.79 us                                                         | 9.30 us: 1.19x slower                                                           |
| json_dumps           | 7.40 ms                                                         | 9.08 ms: 1.23x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.00x faster                                                                    |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250201-pythonperf1_win32-x86-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 20.1 ms: 1.06x slower                                                           |
| python_startup         | 22.4 ms                                                         | 26.8 ms: 1.20x slower                                                           |
| Geometric mean         | (ref)                                                           | 1.13x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250201-pythonperf1_win32-x86-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 7.88 ms: 1.26x faster                                                           |
| django_template | 36.9 ms                                                         | 33.7 ms: 1.09x faster                                                           |
| Geometric mean  | (ref)                                                           | 1.18x faster                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250201-pythonperf1_win32-x86-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| deepcopy_memo              | 38.4 us                                                         | 21.8 us: 1.76x faster                                                           |
| async_tree_io              | 693 ms                                                          | 461 ms: 1.50x faster                                                            |
| deepcopy                   | 360 us                                                          | 243 us: 1.48x faster                                                            |
| unpack_sequence            | 62.5 ns                                                         | 42.4 ns: 1.47x faster                                                           |
| async_tree_io_tg           | 677 ms                                                          | 461 ms: 1.47x faster                                                            |
| spectral_norm              | 104 ms                                                          | 72.5 ms: 1.43x faster                                                           |
| generators                 | 38.5 ms                                                         | 27.1 ms: 1.42x faster                                                           |
| nbody                      | 127 ms                                                          | 89.4 ms: 1.42x faster                                                           |
| comprehensions             | 19.2 us                                                         | 13.6 us: 1.41x faster                                                           |
| async_tree_none_tg         | 278 ms                                                          | 197 ms: 1.41x faster                                                            |
| async_tree_memoization_tg  | 350 ms                                                          | 250 ms: 1.40x faster                                                            |
| async_tree_none            | 298 ms                                                          | 216 ms: 1.38x faster                                                            |
| async_tree_memoization     | 364 ms                                                          | 264 ms: 1.38x faster                                                            |
| float                      | 76.7 ms                                                         | 56.5 ms: 1.36x faster                                                           |
| regex_effbot               | 2.04 ms                                                         | 1.55 ms: 1.32x faster                                                           |
| scimark_lu                 | 93.2 ms                                                         | 71.2 ms: 1.31x faster                                                           |
| go                         | 137 ms                                                          | 105 ms: 1.31x faster                                                            |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 2.97 ms: 1.30x faster                                                           |
| tomli_loads                | 2.20 sec                                                        | 1.69 sec: 1.30x faster                                                          |
| hexiom                     | 6.82 ms                                                         | 5.31 ms: 1.29x faster                                                           |
| logging_silent             | 101 ns                                                          | 78.7 ns: 1.28x faster                                                           |
| chaos                      | 69.4 ms                                                         | 54.2 ms: 1.28x faster                                                           |
| mako                       | 9.96 ms                                                         | 7.88 ms: 1.26x faster                                                           |
| deepcopy_reduce            | 3.23 us                                                         | 2.55 us: 1.26x faster                                                           |
| deltablue                  | 3.58 ms                                                         | 2.84 ms: 1.26x faster                                                           |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 435 ms: 1.26x faster                                                            |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 451 ms: 1.25x faster                                                            |
| scimark_sor                | 130 ms                                                          | 105 ms: 1.24x faster                                                            |
| pyflate                    | 424 ms                                                          | 344 ms: 1.23x faster                                                            |
| regex_compile              | 129 ms                                                          | 105 ms: 1.23x faster                                                            |
| coroutines                 | 20.9 ms                                                         | 17.2 ms: 1.21x faster                                                           |
| scimark_fft                | 271 ms                                                          | 226 ms: 1.20x faster                                                            |
| logging_simple             | 9.75 us                                                         | 8.25 us: 1.18x faster                                                           |
| logging_format             | 10.4 us                                                         | 8.87 us: 1.17x faster                                                           |
| unpickle_pure_python       | 210 us                                                          | 179 us: 1.17x faster                                                            |
| scimark_monte_carlo        | 66.4 ms                                                         | 56.8 ms: 1.17x faster                                                           |
| crypto_pyaes               | 69.2 ms                                                         | 59.5 ms: 1.16x faster                                                           |
| xml_etree_iterparse        | 77.6 ms                                                         | 66.9 ms: 1.16x faster                                                           |
| fannkuch                   | 354 ms                                                          | 306 ms: 1.15x faster                                                            |
| raytrace                   | 308 ms                                                          | 267 ms: 1.15x faster                                                            |
| nqueens                    | 93.7 ms                                                         | 81.3 ms: 1.15x faster                                                           |
| dulwich_log                | 58.5 ms                                                         | 51.1 ms: 1.15x faster                                                           |
| sqlglot_transpile          | 1.53 ms                                                         | 1.34 ms: 1.14x faster                                                           |
| sqlglot_parse              | 1.25 ms                                                         | 1.10 ms: 1.14x faster                                                           |
| sympy_sum                  | 123 ms                                                          | 108 ms: 1.14x faster                                                            |
| pprint_safe_repr           | 721 ms                                                          | 641 ms: 1.12x faster                                                            |
| sqlglot_optimize           | 48.5 ms                                                         | 43.1 ms: 1.12x faster                                                           |
| pycparser                  | 978 ms                                                          | 871 ms: 1.12x faster                                                            |
| pprint_pformat             | 1.50 sec                                                        | 1.34 sec: 1.12x faster                                                          |
| mdp                        | 1.91 sec                                                        | 1.71 sec: 1.12x faster                                                          |
| 2to3                       | 280 ms                                                          | 251 ms: 1.12x faster                                                            |
| sympy_str                  | 240 ms                                                          | 216 ms: 1.11x faster                                                            |
| sympy_integrate            | 17.5 ms                                                         | 15.9 ms: 1.11x faster                                                           |
| regex_dna                  | 127 ms                                                          | 116 ms: 1.09x faster                                                            |
| django_template            | 36.9 ms                                                         | 33.7 ms: 1.09x faster                                                           |
| meteor_contest             | 86.9 ms                                                         | 80.1 ms: 1.08x faster                                                           |
| docutils                   | 1.98 sec                                                        | 1.83 sec: 1.08x faster                                                          |
| sqlite_synth               | 2.07 us                                                         | 1.92 us: 1.08x faster                                                           |
| pathlib                    | 91.4 ms                                                         | 85.1 ms: 1.07x faster                                                           |
| xml_etree_process          | 53.2 ms                                                         | 49.6 ms: 1.07x faster                                                           |
| bench_thread_pool          | 1.10 ms                                                         | 1.03 ms: 1.07x faster                                                           |
| xml_etree_generate         | 72.1 ms                                                         | 68.0 ms: 1.06x faster                                                           |
| pickle_pure_python         | 286 us                                                          | 274 us: 1.04x faster                                                            |
| sympy_expand               | 398 ms                                                          | 381 ms: 1.04x faster                                                            |
| async_generators           | 313 ms                                                          | 302 ms: 1.04x faster                                                            |
| xml_etree_parse            | 113 ms                                                          | 109 ms: 1.04x faster                                                            |
| richards_super             | 46.5 ms                                                         | 44.9 ms: 1.04x faster                                                           |
| asyncio_tcp_ssl            | 17.7 sec                                                        | 17.1 sec: 1.03x faster                                                          |
| richards                   | 41.3 ms                                                         | 40.1 ms: 1.03x faster                                                           |
| pidigits                   | 199 ms                                                          | 201 ms: 1.01x slower                                                            |
| regex_v8                   | 15.0 ms                                                         | 15.7 ms: 1.04x slower                                                           |
| python_startup_no_site     | 19.1 ms                                                         | 20.1 ms: 1.06x slower                                                           |
| pickle_dict                | 19.9 us                                                         | 21.1 us: 1.06x slower                                                           |
| coverage                   | 48.4 ms                                                         | 52.5 ms: 1.08x slower                                                           |
| pickle_list                | 3.37 us                                                         | 3.68 us: 1.09x slower                                                           |
| json_loads                 | 20.4 us                                                         | 22.4 us: 1.10x slower                                                           |
| json                       | 4.15 ms                                                         | 4.58 ms: 1.10x slower                                                           |
| typing_runtime_protocols   | 126 us                                                          | 143 us: 1.13x slower                                                            |
| unpickle                   | 9.71 us                                                         | 11.0 us: 1.13x slower                                                           |
| asyncio_tcp                | 662 ms                                                          | 757 ms: 1.14x slower                                                            |
| pickle                     | 7.79 us                                                         | 9.30 us: 1.19x slower                                                           |
| python_startup             | 22.4 ms                                                         | 26.8 ms: 1.20x slower                                                           |
| json_dumps                 | 7.40 ms                                                         | 9.08 ms: 1.23x slower                                                           |
| bench_mp_pool              | 75.4 ms                                                         | 93.0 ms: 1.23x slower                                                           |
| gc_traversal               | 1.44 ms                                                         | 1.81 ms: 1.26x slower                                                           |
| telco                      | 5.51 ms                                                         | 7.15 ms: 1.30x slower                                                           |
| create_gc_cycles           | 652 us                                                          | 1.05 ms: 1.60x slower                                                           |
| sqlglot_normalize          | 100 ms                                                          | 224 ms: 2.23x slower                                                            |
| Geometric mean             | (ref)                                                           | 1.11x faster                                                                    |

Benchmark hidden because not significant (1): unpickle_list
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (13) of results/bm-20250201-3.14.0a4+-cf4c4ec/bm-20250201-pythonperf1_win32-x86-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.133x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.12x
- 95% likely to have a speedup of 1.12x
- 99% likely to have a speedup of 1.11x

# Memory
- memory change: unknown