# Results vs. 3.12.0

- fork: python
- ref: 2f60b8f02fe7cb83dd58
- machine: windows-amd64
- commit hash: 2f60b8f
- commit date: 2025-11-01
- overall geometric mean: 1.556x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.50x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20251101-pythonperf1_win32-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 213 ms: 1.31x faster                                                              |
| docutils       | 1.98 sec                                                        | 1.60 sec: 1.24x faster                                                            |
| Geometric mean | (ref)                                                           | 1.28x faster                                                                      |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20251101-pythonperf1_win32-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|----------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| async_tree_io              | 693 ms                                                          | 358 ms: 1.94x faster                                                              |
| async_tree_memoization     | 364 ms                                                          | 190 ms: 1.92x faster                                                              |
| async_tree_io_tg           | 677 ms                                                          | 361 ms: 1.87x faster                                                              |
| async_tree_none_tg         | 278 ms                                                          | 152 ms: 1.83x faster                                                              |
| async_tree_memoization_tg  | 350 ms                                                          | 192 ms: 1.82x faster                                                              |
| async_tree_none            | 298 ms                                                          | 164 ms: 1.81x faster                                                              |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 321 ms: 1.76x faster                                                              |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 333 ms: 1.64x faster                                                              |
| Geometric mean             | (ref)                                                           | 1.82x faster                                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20251101-pythonperf1_win32-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 53.4 ms: 2.38x faster                                                             |
| float          | 76.7 ms                                                         | 38.8 ms: 1.97x faster                                                             |
| pidigits       | 199 ms                                                          | 143 ms: 1.39x faster                                                              |
| Geometric mean | (ref)                                                           | 1.87x faster                                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20251101-pythonperf1_win32-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 77.0 ms: 1.68x faster                                                             |
| regex_effbot   | 2.04 ms                                                         | 1.54 ms: 1.32x faster                                                             |
| regex_dna      | 127 ms                                                          | 117 ms: 1.08x faster                                                              |
| regex_v8       | 15.0 ms                                                         | 14.0 ms: 1.08x faster                                                             |
| Geometric mean | (ref)                                                           | 1.27x faster                                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20251101-pythonperf1_win32-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|----------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| tomli_loads          | 2.20 sec                                                        | 1.09 sec: 2.02x faster                                                            |
| unpickle_pure_python | 210 us                                                          | 105 us: 1.99x faster                                                              |
| xml_etree_process    | 53.2 ms                                                         | 35.0 ms: 1.52x faster                                                             |
| xml_etree_generate   | 72.1 ms                                                         | 48.6 ms: 1.48x faster                                                             |
| pickle_pure_python   | 286 us                                                          | 196 us: 1.46x faster                                                              |
| json_loads           | 20.4 us                                                         | 13.9 us: 1.46x faster                                                             |
| xml_etree_iterparse  | 77.6 ms                                                         | 56.5 ms: 1.38x faster                                                             |
| json_dumps           | 7.40 ms                                                         | 5.47 ms: 1.35x faster                                                             |
| xml_etree_parse      | 113 ms                                                          | 85.6 ms: 1.32x faster                                                             |
| unpickle             | 9.71 us                                                         | 8.47 us: 1.15x faster                                                             |
| unpickle_list        | 2.95 us                                                         | 2.77 us: 1.06x faster                                                             |
| pickle_list          | 3.37 us                                                         | 3.18 us: 1.06x faster                                                             |
| pickle               | 7.79 us                                                         | 7.48 us: 1.04x faster                                                             |
| pickle_dict          | 19.9 us                                                         | 19.8 us: 1.01x faster                                                             |
| Geometric mean       | (ref)                                                           | 1.35x faster                                                                      |

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20251101-pythonperf1_win32-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup | 22.4 ms                                                         | 25.2 ms: 1.13x slower                                                             |
| Geometric mean | (ref)                                                           | 1.06x slower                                                                      |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20251101-pythonperf1_win32-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|-----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 5.23 ms: 1.90x faster                                                             |
| django_template | 36.9 ms                                                         | 23.4 ms: 1.57x faster                                                             |
| Geometric mean  | (ref)                                                           | 1.73x faster                                                                      |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20251101-pythonperf1_win32-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|----------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| asyncio_tcp_ssl            | 17.7 sec                                                        | 1.34 sec: 13.20x faster                                                           |
| pathlib                    | 91.4 ms                                                         | 28.7 ms: 3.18x faster                                                             |
| mdp                        | 1.91 sec                                                        | 779 ms: 2.45x faster                                                              |
| nbody                      | 127 ms                                                          | 53.4 ms: 2.38x faster                                                             |
| deepcopy_memo              | 38.4 us                                                         | 17.1 us: 2.24x faster                                                             |
| deepcopy                   | 360 us                                                          | 161 us: 2.24x faster                                                              |
| scimark_fft                | 271 ms                                                          | 133 ms: 2.04x faster                                                              |
| tomli_loads                | 2.20 sec                                                        | 1.09 sec: 2.02x faster                                                            |
| generators                 | 38.5 ms                                                         | 19.1 ms: 2.01x faster                                                             |
| unpickle_pure_python       | 210 us                                                          | 105 us: 1.99x faster                                                              |
| float                      | 76.7 ms                                                         | 38.8 ms: 1.97x faster                                                             |
| async_tree_io              | 693 ms                                                          | 358 ms: 1.94x faster                                                              |
| async_tree_memoization     | 364 ms                                                          | 190 ms: 1.92x faster                                                              |
| mako                       | 9.96 ms                                                         | 5.23 ms: 1.90x faster                                                             |
| unpack_sequence            | 62.5 ns                                                         | 33.0 ns: 1.89x faster                                                             |
| deepcopy_reduce            | 3.23 us                                                         | 1.71 us: 1.88x faster                                                             |
| comprehensions             | 19.2 us                                                         | 10.2 us: 1.88x faster                                                             |
| async_tree_io_tg           | 677 ms                                                          | 361 ms: 1.87x faster                                                              |
| logging_silent             | 101 ns                                                          | 54.4 ns: 1.86x faster                                                             |
| go                         | 137 ms                                                          | 74.3 ms: 1.85x faster                                                             |
| async_tree_none_tg         | 278 ms                                                          | 152 ms: 1.83x faster                                                              |
| async_tree_memoization_tg  | 350 ms                                                          | 192 ms: 1.82x faster                                                              |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 2.12 ms: 1.82x faster                                                             |
| raytrace                   | 308 ms                                                          | 169 ms: 1.82x faster                                                              |
| async_tree_none            | 298 ms                                                          | 164 ms: 1.81x faster                                                              |
| chaos                      | 69.4 ms                                                         | 38.5 ms: 1.80x faster                                                             |
| scimark_sor                | 130 ms                                                          | 73.0 ms: 1.78x faster                                                             |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 321 ms: 1.76x faster                                                              |
| pprint_pformat             | 1.50 sec                                                        | 852 ms: 1.76x faster                                                              |
| hexiom                     | 6.82 ms                                                         | 3.91 ms: 1.74x faster                                                             |
| fannkuch                   | 354 ms                                                          | 204 ms: 1.73x faster                                                              |
| pprint_safe_repr           | 721 ms                                                          | 418 ms: 1.72x faster                                                              |
| pyflate                    | 424 ms                                                          | 248 ms: 1.71x faster                                                              |
| regex_compile              | 129 ms                                                          | 77.0 ms: 1.68x faster                                                             |
| logging_simple             | 9.75 us                                                         | 5.91 us: 1.65x faster                                                             |
| deltablue                  | 3.58 ms                                                         | 2.17 ms: 1.65x faster                                                             |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 333 ms: 1.64x faster                                                              |
| logging_format             | 10.4 us                                                         | 6.42 us: 1.62x faster                                                             |
| scimark_lu                 | 93.2 ms                                                         | 57.8 ms: 1.61x faster                                                             |
| spectral_norm              | 104 ms                                                          | 64.8 ms: 1.60x faster                                                             |
| richards                   | 41.3 ms                                                         | 26.1 ms: 1.58x faster                                                             |
| django_template            | 36.9 ms                                                         | 23.4 ms: 1.57x faster                                                             |
| scimark_monte_carlo        | 66.4 ms                                                         | 42.2 ms: 1.57x faster                                                             |
| richards_super             | 46.5 ms                                                         | 29.7 ms: 1.56x faster                                                             |
| nqueens                    | 93.7 ms                                                         | 60.1 ms: 1.56x faster                                                             |
| crypto_pyaes               | 69.2 ms                                                         | 44.9 ms: 1.54x faster                                                             |
| xml_etree_process          | 53.2 ms                                                         | 35.0 ms: 1.52x faster                                                             |
| dulwich_log                | 58.5 ms                                                         | 38.7 ms: 1.51x faster                                                             |
| pycparser                  | 978 ms                                                          | 653 ms: 1.50x faster                                                              |
| xml_etree_generate         | 72.1 ms                                                         | 48.6 ms: 1.48x faster                                                             |
| pickle_pure_python         | 286 us                                                          | 196 us: 1.46x faster                                                              |
| json_loads                 | 20.4 us                                                         | 13.9 us: 1.46x faster                                                             |
| asyncio_tcp                | 662 ms                                                          | 458 ms: 1.45x faster                                                              |
| sympy_sum                  | 123 ms                                                          | 85.0 ms: 1.44x faster                                                             |
| coroutines                 | 20.9 ms                                                         | 14.5 ms: 1.44x faster                                                             |
| sympy_str                  | 240 ms                                                          | 167 ms: 1.43x faster                                                              |
| json                       | 4.15 ms                                                         | 2.91 ms: 1.43x faster                                                             |
| telco                      | 5.51 ms                                                         | 3.90 ms: 1.41x faster                                                             |
| sympy_integrate            | 17.5 ms                                                         | 12.5 ms: 1.40x faster                                                             |
| pidigits                   | 199 ms                                                          | 143 ms: 1.39x faster                                                              |
| sympy_expand               | 398 ms                                                          | 287 ms: 1.39x faster                                                              |
| xml_etree_iterparse        | 77.6 ms                                                         | 56.5 ms: 1.38x faster                                                             |
| json_dumps                 | 7.40 ms                                                         | 5.47 ms: 1.35x faster                                                             |
| sqlite_synth               | 2.07 us                                                         | 1.55 us: 1.34x faster                                                             |
| regex_effbot               | 2.04 ms                                                         | 1.54 ms: 1.32x faster                                                             |
| bench_thread_pool          | 1.10 ms                                                         | 834 us: 1.32x faster                                                              |
| xml_etree_parse            | 113 ms                                                          | 85.6 ms: 1.32x faster                                                             |
| 2to3                       | 280 ms                                                          | 213 ms: 1.31x faster                                                              |
| async_generators           | 313 ms                                                          | 241 ms: 1.30x faster                                                              |
| meteor_contest             | 86.9 ms                                                         | 69.8 ms: 1.25x faster                                                             |
| docutils                   | 1.98 sec                                                        | 1.60 sec: 1.24x faster                                                            |
| typing_runtime_protocols   | 126 us                                                          | 104 us: 1.21x faster                                                              |
| unpickle                   | 9.71 us                                                         | 8.47 us: 1.15x faster                                                             |
| regex_dna                  | 127 ms                                                          | 117 ms: 1.08x faster                                                              |
| regex_v8                   | 15.0 ms                                                         | 14.0 ms: 1.08x faster                                                             |
| unpickle_list              | 2.95 us                                                         | 2.77 us: 1.06x faster                                                             |
| pickle_list                | 3.37 us                                                         | 3.18 us: 1.06x faster                                                             |
| pickle                     | 7.79 us                                                         | 7.48 us: 1.04x faster                                                             |
| pickle_dict                | 19.9 us                                                         | 19.8 us: 1.01x faster                                                             |
| coverage                   | 48.4 ms                                                         | 48.8 ms: 1.01x slower                                                             |
| python_startup             | 22.4 ms                                                         | 25.2 ms: 1.13x slower                                                             |
| bench_mp_pool              | 75.4 ms                                                         | 88.6 ms: 1.18x slower                                                             |
| gc_traversal               | 1.44 ms                                                         | 2.05 ms: 1.42x slower                                                             |
| create_gc_cycles           | 652 us                                                          | 1.30 ms: 2.00x slower                                                             |
| Geometric mean             | (ref)                                                           | 1.55x faster                                                                      |

Benchmark hidden because not significant (1): python_startup_no_site
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (17) of results/bm-20251101-3.15.0a1+-2f60b8f-JIT/bm-20251101-pythonperf1_win32-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.556x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.56x
- 95% likely to have a speedup of 1.54x
- 99% likely to have a speedup of 1.50x

# Memory
- memory change: unknown