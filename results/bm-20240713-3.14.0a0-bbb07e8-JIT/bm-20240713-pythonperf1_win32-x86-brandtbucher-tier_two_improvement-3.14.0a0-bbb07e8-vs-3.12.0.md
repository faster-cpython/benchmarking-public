# Results vs. 3.12.0

- fork: brandtbucher
- ref: tier_two_improvement
- machine: windows-x86
- commit hash: bbb07e8
- commit date: 2024-07-13
- overall geometric mean: 1.24x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.15x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240713-pythonperf1_win32-x86-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 251 ms: 1.11x faster                                                                 |
| docutils       | 1.98 sec                                                        | 1.91 sec: 1.04x faster                                                               |
| tornado_http   | 105 ms                                                          | 97.0 ms: 1.08x faster                                                                |
| Geometric mean | (ref)                                                           | 1.08x faster                                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240713-pythonperf1_win32-x86-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| async_tree_none_tg         | 278 ms                                                          | 194 ms: 1.43x faster                                                                 |
| async_tree_memoization_tg  | 350 ms                                                          | 249 ms: 1.41x faster                                                                 |
| async_tree_io_tg           | 677 ms                                                          | 498 ms: 1.36x faster                                                                 |
| async_tree_none            | 298 ms                                                          | 220 ms: 1.35x faster                                                                 |
| async_tree_memoization     | 364 ms                                                          | 272 ms: 1.34x faster                                                                 |
| async_tree_io              | 693 ms                                                          | 531 ms: 1.30x faster                                                                 |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 482 ms: 1.17x faster                                                                 |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 470 ms: 1.16x faster                                                                 |
| Geometric mean             | (ref)                                                           | 1.31x faster                                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240713-pythonperf1_win32-x86-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 61.2 ms: 2.07x faster                                                                |
| float          | 76.7 ms                                                         | 43.0 ms: 1.78x faster                                                                |
| pidigits       | 199 ms                                                          | 196 ms: 1.02x faster                                                                 |
| Geometric mean | (ref)                                                           | 1.56x faster                                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240713-pythonperf1_win32-x86-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 94.4 ms: 1.37x faster                                                                |
| regex_dna      | 127 ms                                                          | 118 ms: 1.08x faster                                                                 |
| regex_effbot   | 2.04 ms                                                         | 1.89 ms: 1.08x faster                                                                |
| regex_v8       | 15.0 ms                                                         | 15.7 ms: 1.04x slower                                                                |
| Geometric mean | (ref)                                                           | 1.11x faster                                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240713-pythonperf1_win32-x86-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| tomli_loads          | 2.20 sec                                                        | 1.49 sec: 1.47x faster                                                               |
| unpickle_pure_python | 210 us                                                          | 146 us: 1.44x faster                                                                 |
| pickle_pure_python   | 286 us                                                          | 212 us: 1.35x faster                                                                 |
| xml_etree_iterparse  | 77.6 ms                                                         | 62.0 ms: 1.25x faster                                                                |
| xml_etree_generate   | 72.1 ms                                                         | 58.1 ms: 1.24x faster                                                                |
| xml_etree_process    | 53.2 ms                                                         | 43.4 ms: 1.23x faster                                                                |
| xml_etree_parse      | 113 ms                                                          | 105 ms: 1.08x faster                                                                 |
| json_dumps           | 7.40 ms                                                         | 7.17 ms: 1.03x faster                                                                |
| json_loads           | 20.4 us                                                         | 21.7 us: 1.07x slower                                                                |
| Geometric mean       | (ref)                                                           | 1.21x faster                                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240713-pythonperf1_win32-x86-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 19.3 ms: 1.01x slower                                                                |
| python_startup         | 22.4 ms                                                         | 23.1 ms: 1.03x slower                                                                |
| Geometric mean         | (ref)                                                           | 1.02x slower                                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240713-pythonperf1_win32-x86-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 5.39 ms: 1.85x faster                                                                |
| django_template | 36.9 ms                                                         | 33.6 ms: 1.10x faster                                                                |
| Geometric mean  | (ref)                                                           | 1.42x faster                                                                         |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240713-pythonperf1_win32-x86-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| deepcopy_memo              | 38.4 us                                                         | 15.8 us: 2.43x faster                                                                |
| spectral_norm              | 104 ms                                                          | 48.7 ms: 2.13x faster                                                                |
| nbody                      | 127 ms                                                          | 61.2 ms: 2.07x faster                                                                |
| mako                       | 9.96 ms                                                         | 5.39 ms: 1.85x faster                                                                |
| float                      | 76.7 ms                                                         | 43.0 ms: 1.78x faster                                                                |
| logging_silent             | 101 ns                                                          | 57.4 ns: 1.76x faster                                                                |
| comprehensions             | 19.2 us                                                         | 11.2 us: 1.71x faster                                                                |
| scimark_fft                | 271 ms                                                          | 166 ms: 1.63x faster                                                                 |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 2.37 ms: 1.63x faster                                                                |
| pyflate                    | 424 ms                                                          | 263 ms: 1.61x faster                                                                 |
| fannkuch                   | 354 ms                                                          | 225 ms: 1.57x faster                                                                 |
| scimark_monte_carlo        | 66.4 ms                                                         | 42.8 ms: 1.55x faster                                                                |
| generators                 | 38.5 ms                                                         | 25.5 ms: 1.51x faster                                                                |
| deepcopy                   | 360 us                                                          | 240 us: 1.50x faster                                                                 |
| crypto_pyaes               | 69.2 ms                                                         | 46.8 ms: 1.48x faster                                                                |
| tomli_loads                | 2.20 sec                                                        | 1.49 sec: 1.47x faster                                                               |
| hexiom                     | 6.82 ms                                                         | 4.68 ms: 1.46x faster                                                                |
| unpickle_pure_python       | 210 us                                                          | 146 us: 1.44x faster                                                                 |
| async_tree_none_tg         | 278 ms                                                          | 194 ms: 1.43x faster                                                                 |
| async_tree_memoization_tg  | 350 ms                                                          | 249 ms: 1.41x faster                                                                 |
| regex_compile              | 129 ms                                                          | 94.4 ms: 1.37x faster                                                                |
| async_tree_io_tg           | 677 ms                                                          | 498 ms: 1.36x faster                                                                 |
| async_tree_none            | 298 ms                                                          | 220 ms: 1.35x faster                                                                 |
| pickle_pure_python         | 286 us                                                          | 212 us: 1.35x faster                                                                 |
| deltablue                  | 3.58 ms                                                         | 2.67 ms: 1.34x faster                                                                |
| raytrace                   | 308 ms                                                          | 229 ms: 1.34x faster                                                                 |
| async_tree_memoization     | 364 ms                                                          | 272 ms: 1.34x faster                                                                 |
| deepcopy_reduce            | 3.23 us                                                         | 2.42 us: 1.33x faster                                                                |
| sqlglot_parse              | 1.25 ms                                                         | 942 us: 1.32x faster                                                                 |
| logging_simple             | 9.75 us                                                         | 7.44 us: 1.31x faster                                                                |
| async_tree_io              | 693 ms                                                          | 531 ms: 1.30x faster                                                                 |
| chaos                      | 69.4 ms                                                         | 53.3 ms: 1.30x faster                                                                |
| scimark_sor                | 130 ms                                                          | 99.9 ms: 1.30x faster                                                                |
| pprint_pformat             | 1.50 sec                                                        | 1.16 sec: 1.29x faster                                                               |
| logging_format             | 10.4 us                                                         | 8.06 us: 1.29x faster                                                                |
| pprint_safe_repr           | 721 ms                                                          | 563 ms: 1.28x faster                                                                 |
| nqueens                    | 93.7 ms                                                         | 73.7 ms: 1.27x faster                                                                |
| sqlglot_transpile          | 1.53 ms                                                         | 1.21 ms: 1.26x faster                                                                |
| xml_etree_iterparse        | 77.6 ms                                                         | 62.0 ms: 1.25x faster                                                                |
| xml_etree_generate         | 72.1 ms                                                         | 58.1 ms: 1.24x faster                                                                |
| meteor_contest             | 86.9 ms                                                         | 70.1 ms: 1.24x faster                                                                |
| richards                   | 41.3 ms                                                         | 33.7 ms: 1.23x faster                                                                |
| xml_etree_process          | 53.2 ms                                                         | 43.4 ms: 1.23x faster                                                                |
| coroutines                 | 20.9 ms                                                         | 17.1 ms: 1.22x faster                                                                |
| richards_super             | 46.5 ms                                                         | 38.2 ms: 1.22x faster                                                                |
| go                         | 137 ms                                                          | 113 ms: 1.22x faster                                                                 |
| pycparser                  | 978 ms                                                          | 826 ms: 1.18x faster                                                                 |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 482 ms: 1.17x faster                                                                 |
| mdp                        | 1.91 sec                                                        | 1.64 sec: 1.17x faster                                                               |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 470 ms: 1.16x faster                                                                 |
| scimark_lu                 | 93.2 ms                                                         | 80.4 ms: 1.16x faster                                                                |
| sympy_sum                  | 123 ms                                                          | 108 ms: 1.14x faster                                                                 |
| bench_thread_pool          | 1.10 ms                                                         | 980 us: 1.12x faster                                                                 |
| sqlglot_optimize           | 48.5 ms                                                         | 43.1 ms: 1.12x faster                                                                |
| sympy_str                  | 240 ms                                                          | 214 ms: 1.12x faster                                                                 |
| 2to3                       | 280 ms                                                          | 251 ms: 1.11x faster                                                                 |
| sympy_integrate            | 17.5 ms                                                         | 15.9 ms: 1.10x faster                                                                |
| django_template            | 36.9 ms                                                         | 33.6 ms: 1.10x faster                                                                |
| pathlib                    | 91.4 ms                                                         | 83.2 ms: 1.10x faster                                                                |
| tornado_http               | 105 ms                                                          | 97.0 ms: 1.08x faster                                                                |
| xml_etree_parse            | 113 ms                                                          | 105 ms: 1.08x faster                                                                 |
| regex_dna                  | 127 ms                                                          | 118 ms: 1.08x faster                                                                 |
| regex_effbot               | 2.04 ms                                                         | 1.89 ms: 1.08x faster                                                                |
| asyncio_tcp                | 662 ms                                                          | 623 ms: 1.06x faster                                                                 |
| sympy_expand               | 398 ms                                                          | 379 ms: 1.05x faster                                                                 |
| asyncio_tcp_ssl            | 17.7 sec                                                        | 16.8 sec: 1.05x faster                                                               |
| docutils                   | 1.98 sec                                                        | 1.91 sec: 1.04x faster                                                               |
| json_dumps                 | 7.40 ms                                                         | 7.17 ms: 1.03x faster                                                                |
| bench_mp_pool              | 75.4 ms                                                         | 73.4 ms: 1.03x faster                                                                |
| pidigits                   | 199 ms                                                          | 196 ms: 1.02x faster                                                                 |
| python_startup_no_site     | 19.1 ms                                                         | 19.3 ms: 1.01x slower                                                                |
| gc_traversal               | 1.44 ms                                                         | 1.46 ms: 1.01x slower                                                                |
| telco                      | 5.51 ms                                                         | 5.60 ms: 1.02x slower                                                                |
| async_generators           | 313 ms                                                          | 321 ms: 1.02x slower                                                                 |
| json                       | 4.15 ms                                                         | 4.27 ms: 1.03x slower                                                                |
| python_startup             | 22.4 ms                                                         | 23.1 ms: 1.03x slower                                                                |
| regex_v8                   | 15.0 ms                                                         | 15.7 ms: 1.04x slower                                                                |
| json_loads                 | 20.4 us                                                         | 21.7 us: 1.07x slower                                                                |
| coverage                   | 48.4 ms                                                         | 51.9 ms: 1.07x slower                                                                |
| typing_runtime_protocols   | 126 us                                                          | 144 us: 1.14x slower                                                                 |
| create_gc_cycles           | 652 us                                                          | 755 us: 1.16x slower                                                                 |
| sqlglot_normalize          | 100 ms                                                          | 232 ms: 2.32x slower                                                                 |
| Geometric mean             | (ref)                                                           | 1.24x faster                                                                         |
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, dulwich_log, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240713-3.14.0a0-bbb07e8-JIT/bm-20240713-pythonperf1_win32-x86-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8.json: genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.17x
- 95% likely to have a speedup of 1.16x
- 99% likely to have a speedup of 1.15x

# Memory
- memory change: unknown