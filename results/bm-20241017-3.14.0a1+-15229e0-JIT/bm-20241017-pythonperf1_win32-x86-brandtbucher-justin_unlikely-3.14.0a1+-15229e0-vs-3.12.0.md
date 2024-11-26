# Results vs. 3.12.0

- fork: brandtbucher
- ref: justin_unlikely
- machine: windows-x86
- commit hash: 15229e0
- commit date: 2024-10-17
- overall geometric mean: 1.201x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.12x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241017-pythonperf1_win32-x86-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 264 ms: 1.06x faster                                                             |
| docutils       | 1.98 sec                                                        | 2.05 sec: 1.03x slower                                                           |
| tornado_http   | 105 ms                                                          | 110 ms: 1.05x slower                                                             |
| Geometric mean | (ref)                                                           | 1.01x slower                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241017-pythonperf1_win32-x86-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 350 ms                                                          | 255 ms: 1.37x faster                                                             |
| async_tree_none            | 298 ms                                                          | 218 ms: 1.36x faster                                                             |
| async_tree_none_tg         | 278 ms                                                          | 204 ms: 1.36x faster                                                             |
| async_tree_io              | 693 ms                                                          | 527 ms: 1.31x faster                                                             |
| async_tree_memoization     | 364 ms                                                          | 278 ms: 1.31x faster                                                             |
| async_tree_io_tg           | 677 ms                                                          | 555 ms: 1.22x faster                                                             |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 462 ms: 1.22x faster                                                             |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 462 ms: 1.18x faster                                                             |
| Geometric mean             | (ref)                                                           | 1.29x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241017-pythonperf1_win32-x86-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 57.1 ms: 2.22x faster                                                            |
| float          | 76.7 ms                                                         | 46.5 ms: 1.65x faster                                                            |
| Geometric mean | (ref)                                                           | 1.54x faster                                                                     |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241017-pythonperf1_win32-x86-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 105 ms: 1.23x faster                                                             |
| regex_effbot   | 2.04 ms                                                         | 1.80 ms: 1.13x faster                                                            |
| regex_dna      | 127 ms                                                          | 113 ms: 1.12x faster                                                             |
| Geometric mean | (ref)                                                           | 1.12x faster                                                                     |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241017-pythonperf1_win32-x86-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| tomli_loads          | 2.20 sec                                                        | 1.49 sec: 1.48x faster                                                           |
| unpickle_pure_python | 210 us                                                          | 156 us: 1.35x faster                                                             |
| xml_etree_generate   | 72.1 ms                                                         | 55.0 ms: 1.31x faster                                                            |
| xml_etree_process    | 53.2 ms                                                         | 41.5 ms: 1.28x faster                                                            |
| xml_etree_iterparse  | 77.6 ms                                                         | 63.0 ms: 1.23x faster                                                            |
| pickle_pure_python   | 286 us                                                          | 244 us: 1.17x faster                                                             |
| xml_etree_parse      | 113 ms                                                          | 109 ms: 1.04x faster                                                             |
| pickle_list          | 3.37 us                                                         | 3.40 us: 1.01x slower                                                            |
| json_loads           | 20.4 us                                                         | 20.5 us: 1.01x slower                                                            |
| unpickle_list        | 2.95 us                                                         | 2.98 us: 1.01x slower                                                            |
| pickle_dict          | 19.9 us                                                         | 21.2 us: 1.06x slower                                                            |
| json_dumps           | 7.40 ms                                                         | 7.95 ms: 1.07x slower                                                            |
| unpickle             | 9.71 us                                                         | 10.4 us: 1.08x slower                                                            |
| pickle               | 7.79 us                                                         | 8.55 us: 1.10x slower                                                            |
| Geometric mean       | (ref)                                                           | 1.10x faster                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241017-pythonperf1_win32-x86-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 20.3 ms: 1.06x slower                                                            |
| python_startup         | 22.4 ms                                                         | 26.8 ms: 1.20x slower                                                            |
| Geometric mean         | (ref)                                                           | 1.13x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241017-pythonperf1_win32-x86-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 5.82 ms: 1.71x faster                                                            |
| django_template | 36.9 ms                                                         | 33.3 ms: 1.11x faster                                                            |
| Geometric mean  | (ref)                                                           | 1.38x faster                                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241017-pythonperf1_win32-x86-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| deepcopy_memo              | 38.4 us                                                         | 15.9 us: 2.41x faster                                                            |
| nbody                      | 127 ms                                                          | 57.1 ms: 2.22x faster                                                            |
| scimark_sor                | 130 ms                                                          | 68.1 ms: 1.91x faster                                                            |
| logging_silent             | 101 ns                                                          | 54.6 ns: 1.85x faster                                                            |
| spectral_norm              | 104 ms                                                          | 58.3 ms: 1.78x faster                                                            |
| mako                       | 9.96 ms                                                         | 5.82 ms: 1.71x faster                                                            |
| scimark_monte_carlo        | 66.4 ms                                                         | 39.6 ms: 1.68x faster                                                            |
| float                      | 76.7 ms                                                         | 46.5 ms: 1.65x faster                                                            |
| deepcopy                   | 360 us                                                          | 225 us: 1.60x faster                                                             |
| generators                 | 38.5 ms                                                         | 24.3 ms: 1.59x faster                                                            |
| unpack_sequence            | 62.5 ns                                                         | 39.5 ns: 1.58x faster                                                            |
| scimark_lu                 | 93.2 ms                                                         | 60.6 ms: 1.54x faster                                                            |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 2.55 ms: 1.51x faster                                                            |
| scimark_fft                | 271 ms                                                          | 183 ms: 1.48x faster                                                             |
| tomli_loads                | 2.20 sec                                                        | 1.49 sec: 1.48x faster                                                           |
| comprehensions             | 19.2 us                                                         | 13.2 us: 1.46x faster                                                            |
| go                         | 137 ms                                                          | 94.8 ms: 1.45x faster                                                            |
| fannkuch                   | 354 ms                                                          | 244 ms: 1.45x faster                                                             |
| deepcopy_reduce            | 3.23 us                                                         | 2.28 us: 1.41x faster                                                            |
| deltablue                  | 3.58 ms                                                         | 2.57 ms: 1.39x faster                                                            |
| crypto_pyaes               | 69.2 ms                                                         | 50.0 ms: 1.39x faster                                                            |
| async_tree_memoization_tg  | 350 ms                                                          | 255 ms: 1.37x faster                                                             |
| async_tree_none            | 298 ms                                                          | 218 ms: 1.36x faster                                                             |
| pyflate                    | 424 ms                                                          | 311 ms: 1.36x faster                                                             |
| async_tree_none_tg         | 278 ms                                                          | 204 ms: 1.36x faster                                                             |
| unpickle_pure_python       | 210 us                                                          | 156 us: 1.35x faster                                                             |
| async_tree_io              | 693 ms                                                          | 527 ms: 1.31x faster                                                             |
| xml_etree_generate         | 72.1 ms                                                         | 55.0 ms: 1.31x faster                                                            |
| async_tree_memoization     | 364 ms                                                          | 278 ms: 1.31x faster                                                             |
| pprint_pformat             | 1.50 sec                                                        | 1.17 sec: 1.28x faster                                                           |
| xml_etree_process          | 53.2 ms                                                         | 41.5 ms: 1.28x faster                                                            |
| pprint_safe_repr           | 721 ms                                                          | 564 ms: 1.28x faster                                                             |
| logging_simple             | 9.75 us                                                         | 7.65 us: 1.28x faster                                                            |
| hexiom                     | 6.82 ms                                                         | 5.39 ms: 1.27x faster                                                            |
| chaos                      | 69.4 ms                                                         | 55.2 ms: 1.26x faster                                                            |
| logging_format             | 10.4 us                                                         | 8.37 us: 1.24x faster                                                            |
| xml_etree_iterparse        | 77.6 ms                                                         | 63.0 ms: 1.23x faster                                                            |
| regex_compile              | 129 ms                                                          | 105 ms: 1.23x faster                                                             |
| async_tree_io_tg           | 677 ms                                                          | 555 ms: 1.22x faster                                                             |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 462 ms: 1.22x faster                                                             |
| nqueens                    | 93.7 ms                                                         | 77.4 ms: 1.21x faster                                                            |
| coroutines                 | 20.9 ms                                                         | 17.4 ms: 1.20x faster                                                            |
| meteor_contest             | 86.9 ms                                                         | 73.1 ms: 1.19x faster                                                            |
| sqlglot_parse              | 1.25 ms                                                         | 1.05 ms: 1.18x faster                                                            |
| dulwich_log                | 58.5 ms                                                         | 49.5 ms: 1.18x faster                                                            |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 462 ms: 1.18x faster                                                             |
| pycparser                  | 978 ms                                                          | 833 ms: 1.17x faster                                                             |
| pickle_pure_python         | 286 us                                                          | 244 us: 1.17x faster                                                             |
| regex_effbot               | 2.04 ms                                                         | 1.80 ms: 1.13x faster                                                            |
| raytrace                   | 308 ms                                                          | 273 ms: 1.13x faster                                                             |
| sqlglot_transpile          | 1.53 ms                                                         | 1.37 ms: 1.12x faster                                                            |
| regex_dna                  | 127 ms                                                          | 113 ms: 1.12x faster                                                             |
| django_template            | 36.9 ms                                                         | 33.3 ms: 1.11x faster                                                            |
| bench_thread_pool          | 1.10 ms                                                         | 1.01 ms: 1.09x faster                                                            |
| 2to3                       | 280 ms                                                          | 264 ms: 1.06x faster                                                             |
| mdp                        | 1.91 sec                                                        | 1.80 sec: 1.06x faster                                                           |
| sqlite_synth               | 2.07 us                                                         | 1.97 us: 1.05x faster                                                            |
| richards                   | 41.3 ms                                                         | 39.3 ms: 1.05x faster                                                            |
| pathlib                    | 91.4 ms                                                         | 87.7 ms: 1.04x faster                                                            |
| sympy_str                  | 240 ms                                                          | 231 ms: 1.04x faster                                                             |
| xml_etree_parse            | 113 ms                                                          | 109 ms: 1.04x faster                                                             |
| sympy_sum                  | 123 ms                                                          | 119 ms: 1.04x faster                                                             |
| asyncio_tcp_ssl            | 17.7 sec                                                        | 17.5 sec: 1.01x faster                                                           |
| sympy_integrate            | 17.5 ms                                                         | 17.4 ms: 1.01x faster                                                            |
| pickle_list                | 3.37 us                                                         | 3.40 us: 1.01x slower                                                            |
| json_loads                 | 20.4 us                                                         | 20.5 us: 1.01x slower                                                            |
| unpickle_list              | 2.95 us                                                         | 2.98 us: 1.01x slower                                                            |
| sqlglot_normalize          | 100 ms                                                          | 103 ms: 1.03x slower                                                             |
| docutils                   | 1.98 sec                                                        | 2.05 sec: 1.03x slower                                                           |
| sqlglot_optimize           | 48.5 ms                                                         | 50.3 ms: 1.04x slower                                                            |
| tornado_http               | 105 ms                                                          | 110 ms: 1.05x slower                                                             |
| python_startup_no_site     | 19.1 ms                                                         | 20.3 ms: 1.06x slower                                                            |
| pickle_dict                | 19.9 us                                                         | 21.2 us: 1.06x slower                                                            |
| json_dumps                 | 7.40 ms                                                         | 7.95 ms: 1.07x slower                                                            |
| unpickle                   | 9.71 us                                                         | 10.4 us: 1.08x slower                                                            |
| telco                      | 5.51 ms                                                         | 5.95 ms: 1.08x slower                                                            |
| pickle                     | 7.79 us                                                         | 8.55 us: 1.10x slower                                                            |
| typing_runtime_protocols   | 126 us                                                          | 139 us: 1.10x slower                                                             |
| coverage                   | 48.4 ms                                                         | 53.8 ms: 1.11x slower                                                            |
| python_startup             | 22.4 ms                                                         | 26.8 ms: 1.20x slower                                                            |
| json                       | 4.15 ms                                                         | 5.06 ms: 1.22x slower                                                            |
| asyncio_tcp                | 662 ms                                                          | 832 ms: 1.26x slower                                                             |
| bench_mp_pool              | 75.4 ms                                                         | 95.5 ms: 1.27x slower                                                            |
| gc_traversal               | 1.44 ms                                                         | 1.83 ms: 1.27x slower                                                            |
| create_gc_cycles           | 652 us                                                          | 1.19 ms: 1.82x slower                                                            |
| Geometric mean             | (ref)                                                           | 1.18x faster                                                                     |

Benchmark hidden because not significant (5): richards_super, sympy_expand, regex_v8, async_generators, pidigits
Ignored benchmarks (6) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (6) of results/bm-20241017-3.14.0a1+-15229e0-JIT/bm-20241017-pythonperf1_win32-x86-brandtbucher-justin_unlikely-3.14.0a1+-15229e0.json: genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift

- Geometric mean (including insignificant results): 1.201x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.17x
- 95% likely to have a speedup of 1.15x
- 99% likely to have a speedup of 1.12x

# Memory
- memory change: unknown