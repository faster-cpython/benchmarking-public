# Results vs. 3.12.0

- fork: brandtbucher
- ref: warmer_side_exits
- machine: windows-x86
- commit hash: 8423e72
- commit date: 2024-07-01
- overall geometric mean: 1.20x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.08x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240701-pythonperf1_win32-x86-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 264 ms: 1.06x faster                                                              |
| docutils       | 1.98 sec                                                        | 2.00 sec: 1.01x slower                                                            |
| tornado_http   | 105 ms                                                          | 101 ms: 1.04x faster                                                              |
| Geometric mean | (ref)                                                           | 1.03x faster                                                                      |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240701-pythonperf1_win32-x86-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|----------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 350 ms                                                          | 267 ms: 1.31x faster                                                              |
| async_tree_none_tg         | 278 ms                                                          | 213 ms: 1.30x faster                                                              |
| async_tree_io_tg           | 677 ms                                                          | 534 ms: 1.27x faster                                                              |
| async_tree_none            | 298 ms                                                          | 240 ms: 1.24x faster                                                              |
| async_tree_memoization     | 364 ms                                                          | 295 ms: 1.23x faster                                                              |
| async_tree_io              | 693 ms                                                          | 575 ms: 1.21x faster                                                              |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 472 ms: 1.16x faster                                                              |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 490 ms: 1.15x faster                                                              |
| Geometric mean             | (ref)                                                           | 1.23x faster                                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240701-pythonperf1_win32-x86-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 51.5 ms: 2.46x faster                                                             |
| float          | 76.7 ms                                                         | 45.6 ms: 1.68x faster                                                             |
| pidigits       | 199 ms                                                          | 197 ms: 1.01x faster                                                              |
| Geometric mean | (ref)                                                           | 1.61x faster                                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240701-pythonperf1_win32-x86-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 101 ms: 1.28x faster                                                              |
| regex_dna      | 127 ms                                                          | 119 ms: 1.07x faster                                                              |
| regex_effbot   | 2.04 ms                                                         | 1.99 ms: 1.02x faster                                                             |
| regex_v8       | 15.0 ms                                                         | 15.9 ms: 1.06x slower                                                             |
| Geometric mean | (ref)                                                           | 1.07x faster                                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240701-pythonperf1_win32-x86-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|----------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| unpickle_pure_python | 210 us                                                          | 130 us: 1.61x faster                                                              |
| tomli_loads          | 2.20 sec                                                        | 1.63 sec: 1.35x faster                                                            |
| pickle_pure_python   | 286 us                                                          | 223 us: 1.28x faster                                                              |
| xml_etree_iterparse  | 77.6 ms                                                         | 63.5 ms: 1.22x faster                                                             |
| xml_etree_generate   | 72.1 ms                                                         | 63.0 ms: 1.14x faster                                                             |
| xml_etree_process    | 53.2 ms                                                         | 48.5 ms: 1.10x faster                                                             |
| xml_etree_parse      | 113 ms                                                          | 106 ms: 1.07x faster                                                              |
| json_loads           | 20.4 us                                                         | 20.9 us: 1.03x slower                                                             |
| Geometric mean       | (ref)                                                           | 1.18x faster                                                                      |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240701-pythonperf1_win32-x86-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 19.2 ms: 1.01x slower                                                             |
| python_startup         | 22.4 ms                                                         | 23.2 ms: 1.04x slower                                                             |
| Geometric mean         | (ref)                                                           | 1.02x slower                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240701-pythonperf1_win32-x86-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|-----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 5.43 ms: 1.83x faster                                                             |
| django_template | 36.9 ms                                                         | 35.9 ms: 1.03x faster                                                             |
| Geometric mean  | (ref)                                                           | 1.37x faster                                                                      |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240701-pythonperf1_win32-x86-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|----------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| nbody                      | 127 ms                                                          | 51.5 ms: 2.46x faster                                                             |
| deepcopy_memo              | 38.4 us                                                         | 16.5 us: 2.33x faster                                                             |
| spectral_norm              | 104 ms                                                          | 49.3 ms: 2.10x faster                                                             |
| mako                       | 9.96 ms                                                         | 5.43 ms: 1.83x faster                                                             |
| comprehensions             | 19.2 us                                                         | 11.1 us: 1.72x faster                                                             |
| logging_silent             | 101 ns                                                          | 59.0 ns: 1.71x faster                                                             |
| float                      | 76.7 ms                                                         | 45.6 ms: 1.68x faster                                                             |
| fannkuch                   | 354 ms                                                          | 216 ms: 1.63x faster                                                              |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 2.37 ms: 1.63x faster                                                             |
| scimark_fft                | 271 ms                                                          | 166 ms: 1.63x faster                                                              |
| unpickle_pure_python       | 210 us                                                          | 130 us: 1.61x faster                                                              |
| scimark_monte_carlo        | 66.4 ms                                                         | 42.9 ms: 1.55x faster                                                             |
| pyflate                    | 424 ms                                                          | 283 ms: 1.50x faster                                                              |
| hexiom                     | 6.82 ms                                                         | 4.68 ms: 1.46x faster                                                             |
| deepcopy                   | 360 us                                                          | 250 us: 1.44x faster                                                              |
| crypto_pyaes               | 69.2 ms                                                         | 48.3 ms: 1.43x faster                                                             |
| tomli_loads                | 2.20 sec                                                        | 1.63 sec: 1.35x faster                                                            |
| async_tree_memoization_tg  | 350 ms                                                          | 267 ms: 1.31x faster                                                              |
| nqueens                    | 93.7 ms                                                         | 71.6 ms: 1.31x faster                                                             |
| async_tree_none_tg         | 278 ms                                                          | 213 ms: 1.30x faster                                                              |
| regex_compile              | 129 ms                                                          | 101 ms: 1.28x faster                                                              |
| pickle_pure_python         | 286 us                                                          | 223 us: 1.28x faster                                                              |
| generators                 | 38.5 ms                                                         | 30.2 ms: 1.27x faster                                                             |
| deltablue                  | 3.58 ms                                                         | 2.82 ms: 1.27x faster                                                             |
| async_tree_io_tg           | 677 ms                                                          | 534 ms: 1.27x faster                                                              |
| chaos                      | 69.4 ms                                                         | 55.7 ms: 1.24x faster                                                             |
| deepcopy_reduce            | 3.23 us                                                         | 2.59 us: 1.24x faster                                                             |
| async_tree_none            | 298 ms                                                          | 240 ms: 1.24x faster                                                              |
| async_tree_memoization     | 364 ms                                                          | 295 ms: 1.23x faster                                                              |
| sqlglot_parse              | 1.25 ms                                                         | 1.02 ms: 1.23x faster                                                             |
| xml_etree_iterparse        | 77.6 ms                                                         | 63.5 ms: 1.22x faster                                                             |
| pprint_pformat             | 1.50 sec                                                        | 1.23 sec: 1.21x faster                                                            |
| logging_simple             | 9.75 us                                                         | 8.05 us: 1.21x faster                                                             |
| async_tree_io              | 693 ms                                                          | 575 ms: 1.21x faster                                                              |
| logging_format             | 10.4 us                                                         | 8.69 us: 1.20x faster                                                             |
| pprint_safe_repr           | 721 ms                                                          | 602 ms: 1.20x faster                                                              |
| sqlglot_transpile          | 1.53 ms                                                         | 1.29 ms: 1.19x faster                                                             |
| scimark_sor                | 130 ms                                                          | 110 ms: 1.18x faster                                                              |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 472 ms: 1.16x faster                                                              |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 490 ms: 1.15x faster                                                              |
| raytrace                   | 308 ms                                                          | 268 ms: 1.15x faster                                                              |
| xml_etree_generate         | 72.1 ms                                                         | 63.0 ms: 1.14x faster                                                             |
| meteor_contest             | 86.9 ms                                                         | 76.5 ms: 1.14x faster                                                             |
| go                         | 137 ms                                                          | 122 ms: 1.12x faster                                                              |
| bench_thread_pool          | 1.10 ms                                                         | 989 us: 1.11x faster                                                              |
| scimark_lu                 | 93.2 ms                                                         | 84.2 ms: 1.11x faster                                                             |
| mdp                        | 1.91 sec                                                        | 1.73 sec: 1.11x faster                                                            |
| richards                   | 41.3 ms                                                         | 37.5 ms: 1.10x faster                                                             |
| xml_etree_process          | 53.2 ms                                                         | 48.5 ms: 1.10x faster                                                             |
| pathlib                    | 91.4 ms                                                         | 83.5 ms: 1.09x faster                                                             |
| richards_super             | 46.5 ms                                                         | 42.9 ms: 1.08x faster                                                             |
| coroutines                 | 20.9 ms                                                         | 19.3 ms: 1.08x faster                                                             |
| xml_etree_parse            | 113 ms                                                          | 106 ms: 1.07x faster                                                              |
| regex_dna                  | 127 ms                                                          | 119 ms: 1.07x faster                                                              |
| pycparser                  | 978 ms                                                          | 917 ms: 1.07x faster                                                              |
| sympy_sum                  | 123 ms                                                          | 115 ms: 1.06x faster                                                              |
| asyncio_tcp                | 662 ms                                                          | 622 ms: 1.06x faster                                                              |
| 2to3                       | 280 ms                                                          | 264 ms: 1.06x faster                                                              |
| sympy_integrate            | 17.5 ms                                                         | 16.6 ms: 1.06x faster                                                             |
| sympy_str                  | 240 ms                                                          | 229 ms: 1.05x faster                                                              |
| asyncio_tcp_ssl            | 17.7 sec                                                        | 16.9 sec: 1.04x faster                                                            |
| sqlglot_optimize           | 48.5 ms                                                         | 46.6 ms: 1.04x faster                                                             |
| tornado_http               | 105 ms                                                          | 101 ms: 1.04x faster                                                              |
| django_template            | 36.9 ms                                                         | 35.9 ms: 1.03x faster                                                             |
| regex_effbot               | 2.04 ms                                                         | 1.99 ms: 1.02x faster                                                             |
| pidigits                   | 199 ms                                                          | 197 ms: 1.01x faster                                                              |
| bench_mp_pool              | 75.4 ms                                                         | 74.9 ms: 1.01x faster                                                             |
| sqlglot_normalize          | 100 ms                                                          | 101 ms: 1.01x slower                                                              |
| docutils                   | 1.98 sec                                                        | 2.00 sec: 1.01x slower                                                            |
| python_startup_no_site     | 19.1 ms                                                         | 19.2 ms: 1.01x slower                                                             |
| telco                      | 5.51 ms                                                         | 5.61 ms: 1.02x slower                                                             |
| json_loads                 | 20.4 us                                                         | 20.9 us: 1.03x slower                                                             |
| python_startup             | 22.4 ms                                                         | 23.2 ms: 1.04x slower                                                             |
| sympy_expand               | 398 ms                                                          | 413 ms: 1.04x slower                                                              |
| regex_v8                   | 15.0 ms                                                         | 15.9 ms: 1.06x slower                                                             |
| async_generators           | 313 ms                                                          | 338 ms: 1.08x slower                                                              |
| coverage                   | 48.4 ms                                                         | 52.4 ms: 1.08x slower                                                             |
| create_gc_cycles           | 652 us                                                          | 761 us: 1.17x slower                                                              |
| typing_runtime_protocols   | 126 us                                                          | 160 us: 1.27x slower                                                              |
| Geometric mean             | (ref)                                                           | 1.20x faster                                                                      |

Benchmark hidden because not significant (3): gc_traversal, json_dumps, json
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, dulwich_log, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240701-3.14.0a0-8423e72-JIT/bm-20240701-pythonperf1_win32-x86-brandtbucher-warmer_side_exits-3.14.0a0-8423e72.json: genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.10x
- 95% likely to have a speedup of 1.10x
- 99% likely to have a speedup of 1.08x

# Memory
- memory change: unknown