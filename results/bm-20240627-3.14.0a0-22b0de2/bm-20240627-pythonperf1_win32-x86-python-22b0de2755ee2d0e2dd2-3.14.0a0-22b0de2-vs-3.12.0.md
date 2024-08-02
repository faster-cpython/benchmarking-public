# Results vs. 3.12.0

- fork: python
- ref: 22b0de2755ee2d0e2dd2
- machine: windows-x86
- commit hash: 22b0de2
- commit date: 2024-06-27
- overall geometric mean: 1.08x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240627-pythonperf1_win32-x86-python-22b0de2755ee2d0e2dd2-3.14.0a0-22b0de2 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 264 ms: 1.06x faster                                                           |
| docutils       | 1.98 sec                                                        | 1.96 sec: 1.01x faster                                                         |
| tornado_http   | 105 ms                                                          | 97.6 ms: 1.08x faster                                                          |
| Geometric mean | (ref)                                                           | 1.05x faster                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240627-pythonperf1_win32-x86-python-22b0de2755ee2d0e2dd2-3.14.0a0-22b0de2 |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 350 ms                                                          | 262 ms: 1.34x faster                                                           |
| async_tree_none_tg         | 278 ms                                                          | 208 ms: 1.33x faster                                                           |
| async_tree_io_tg           | 677 ms                                                          | 534 ms: 1.27x faster                                                           |
| async_tree_memoization     | 364 ms                                                          | 295 ms: 1.23x faster                                                           |
| async_tree_none            | 298 ms                                                          | 241 ms: 1.23x faster                                                           |
| async_tree_io              | 693 ms                                                          | 579 ms: 1.20x faster                                                           |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 472 ms: 1.16x faster                                                           |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 491 ms: 1.15x faster                                                           |
| Geometric mean             | (ref)                                                           | 1.24x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240627-pythonperf1_win32-x86-python-22b0de2755ee2d0e2dd2-3.14.0a0-22b0de2 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 103 ms: 1.24x faster                                                           |
| float          | 76.7 ms                                                         | 64.8 ms: 1.18x faster                                                          |
| Geometric mean | (ref)                                                           | 1.14x faster                                                                   |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240627-pythonperf1_win32-x86-python-22b0de2755ee2d0e2dd2-3.14.0a0-22b0de2 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 115 ms: 1.12x faster                                                           |
| regex_dna      | 127 ms                                                          | 119 ms: 1.07x faster                                                           |
| regex_effbot   | 2.04 ms                                                         | 1.92 ms: 1.06x faster                                                          |
| regex_v8       | 15.0 ms                                                         | 16.2 ms: 1.08x slower                                                          |
| Geometric mean | (ref)                                                           | 1.04x faster                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240627-pythonperf1_win32-x86-python-22b0de2755ee2d0e2dd2-3.14.0a0-22b0de2 |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| xml_etree_iterparse  | 77.6 ms                                                         | 69.7 ms: 1.11x faster                                                          |
| unpickle_pure_python | 210 us                                                          | 189 us: 1.11x faster                                                           |
| tomli_loads          | 2.20 sec                                                        | 2.01 sec: 1.09x faster                                                         |
| xml_etree_parse      | 113 ms                                                          | 107 ms: 1.06x faster                                                           |
| xml_etree_process    | 53.2 ms                                                         | 51.6 ms: 1.03x faster                                                          |
| pickle_pure_python   | 286 us                                                          | 278 us: 1.03x faster                                                           |
| xml_etree_generate   | 72.1 ms                                                         | 70.2 ms: 1.03x faster                                                          |
| json_loads           | 20.4 us                                                         | 21.1 us: 1.04x slower                                                          |
| json_dumps           | 7.40 ms                                                         | 7.82 ms: 1.06x slower                                                          |
| Geometric mean       | (ref)                                                           | 1.04x faster                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240627-pythonperf1_win32-x86-python-22b0de2755ee2d0e2dd2-3.14.0a0-22b0de2 |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 18.9 ms: 1.01x faster                                                          |
| python_startup         | 22.4 ms                                                         | 22.9 ms: 1.02x slower                                                          |
| Geometric mean         | (ref)                                                           | 1.01x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240627-pythonperf1_win32-x86-python-22b0de2755ee2d0e2dd2-3.14.0a0-22b0de2 |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 8.76 ms: 1.14x faster                                                          |
| django_template | 36.9 ms                                                         | 34.4 ms: 1.07x faster                                                          |
| Geometric mean  | (ref)                                                           | 1.11x faster                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240627-pythonperf1_win32-x86-python-22b0de2755ee2d0e2dd2-3.14.0a0-22b0de2 |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| deepcopy_memo              | 38.4 us                                                         | 25.1 us: 1.53x faster                                                          |
| generators                 | 38.5 ms                                                         | 28.5 ms: 1.35x faster                                                          |
| async_tree_memoization_tg  | 350 ms                                                          | 262 ms: 1.34x faster                                                           |
| async_tree_none_tg         | 278 ms                                                          | 208 ms: 1.33x faster                                                           |
| deepcopy                   | 360 us                                                          | 271 us: 1.33x faster                                                           |
| spectral_norm              | 104 ms                                                          | 79.6 ms: 1.30x faster                                                          |
| logging_silent             | 101 ns                                                          | 77.7 ns: 1.30x faster                                                          |
| comprehensions             | 19.2 us                                                         | 14.8 us: 1.29x faster                                                          |
| async_tree_io_tg           | 677 ms                                                          | 534 ms: 1.27x faster                                                           |
| hexiom                     | 6.82 ms                                                         | 5.43 ms: 1.26x faster                                                          |
| raytrace                   | 308 ms                                                          | 247 ms: 1.25x faster                                                           |
| deltablue                  | 3.58 ms                                                         | 2.88 ms: 1.25x faster                                                          |
| nbody                      | 127 ms                                                          | 103 ms: 1.24x faster                                                           |
| scimark_lu                 | 93.2 ms                                                         | 75.5 ms: 1.24x faster                                                          |
| async_tree_memoization     | 364 ms                                                          | 295 ms: 1.23x faster                                                           |
| async_tree_none            | 298 ms                                                          | 241 ms: 1.23x faster                                                           |
| scimark_sor                | 130 ms                                                          | 106 ms: 1.22x faster                                                           |
| nqueens                    | 93.7 ms                                                         | 77.5 ms: 1.21x faster                                                          |
| async_tree_io              | 693 ms                                                          | 579 ms: 1.20x faster                                                           |
| float                      | 76.7 ms                                                         | 64.8 ms: 1.18x faster                                                          |
| deepcopy_reduce            | 3.23 us                                                         | 2.76 us: 1.17x faster                                                          |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 472 ms: 1.16x faster                                                           |
| coroutines                 | 20.9 ms                                                         | 18.1 ms: 1.16x faster                                                          |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 491 ms: 1.15x faster                                                           |
| chaos                      | 69.4 ms                                                         | 60.7 ms: 1.14x faster                                                          |
| mako                       | 9.96 ms                                                         | 8.76 ms: 1.14x faster                                                          |
| logging_simple             | 9.75 us                                                         | 8.62 us: 1.13x faster                                                          |
| regex_compile              | 129 ms                                                          | 115 ms: 1.12x faster                                                           |
| pyflate                    | 424 ms                                                          | 378 ms: 1.12x faster                                                           |
| logging_format             | 10.4 us                                                         | 9.33 us: 1.11x faster                                                          |
| xml_etree_iterparse        | 77.6 ms                                                         | 69.7 ms: 1.11x faster                                                          |
| bench_thread_pool          | 1.10 ms                                                         | 992 us: 1.11x faster                                                           |
| unpickle_pure_python       | 210 us                                                          | 189 us: 1.11x faster                                                           |
| pycparser                  | 978 ms                                                          | 892 ms: 1.10x faster                                                           |
| tomli_loads                | 2.20 sec                                                        | 2.01 sec: 1.09x faster                                                         |
| scimark_monte_carlo        | 66.4 ms                                                         | 60.9 ms: 1.09x faster                                                          |
| mdp                        | 1.91 sec                                                        | 1.75 sec: 1.09x faster                                                         |
| pathlib                    | 91.4 ms                                                         | 84.0 ms: 1.09x faster                                                          |
| crypto_pyaes               | 69.2 ms                                                         | 63.7 ms: 1.09x faster                                                          |
| go                         | 137 ms                                                          | 127 ms: 1.08x faster                                                           |
| sympy_integrate            | 17.5 ms                                                         | 16.2 ms: 1.08x faster                                                          |
| tornado_http               | 105 ms                                                          | 97.6 ms: 1.08x faster                                                          |
| django_template            | 36.9 ms                                                         | 34.4 ms: 1.07x faster                                                          |
| regex_dna                  | 127 ms                                                          | 119 ms: 1.07x faster                                                           |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 3.61 ms: 1.07x faster                                                          |
| bench_mp_pool              | 75.4 ms                                                         | 71.0 ms: 1.06x faster                                                          |
| sympy_sum                  | 123 ms                                                          | 116 ms: 1.06x faster                                                           |
| 2to3                       | 280 ms                                                          | 264 ms: 1.06x faster                                                           |
| regex_effbot               | 2.04 ms                                                         | 1.92 ms: 1.06x faster                                                          |
| xml_etree_parse            | 113 ms                                                          | 107 ms: 1.06x faster                                                           |
| pprint_pformat             | 1.50 sec                                                        | 1.42 sec: 1.06x faster                                                         |
| scimark_fft                | 271 ms                                                          | 257 ms: 1.05x faster                                                           |
| meteor_contest             | 86.9 ms                                                         | 82.4 ms: 1.05x faster                                                          |
| sqlglot_transpile          | 1.53 ms                                                         | 1.45 ms: 1.05x faster                                                          |
| asyncio_tcp_ssl            | 17.7 sec                                                        | 16.8 sec: 1.05x faster                                                         |
| pprint_safe_repr           | 721 ms                                                          | 694 ms: 1.04x faster                                                           |
| sqlglot_parse              | 1.25 ms                                                         | 1.21 ms: 1.03x faster                                                          |
| xml_etree_process          | 53.2 ms                                                         | 51.6 ms: 1.03x faster                                                          |
| pickle_pure_python         | 286 us                                                          | 278 us: 1.03x faster                                                           |
| sympy_str                  | 240 ms                                                          | 233 ms: 1.03x faster                                                           |
| xml_etree_generate         | 72.1 ms                                                         | 70.2 ms: 1.03x faster                                                          |
| sqlglot_optimize           | 48.5 ms                                                         | 47.3 ms: 1.02x faster                                                          |
| fannkuch                   | 354 ms                                                          | 347 ms: 1.02x faster                                                           |
| richards_super             | 46.5 ms                                                         | 45.8 ms: 1.01x faster                                                          |
| docutils                   | 1.98 sec                                                        | 1.96 sec: 1.01x faster                                                         |
| python_startup_no_site     | 19.1 ms                                                         | 18.9 ms: 1.01x faster                                                          |
| async_generators           | 313 ms                                                          | 314 ms: 1.00x slower                                                           |
| python_startup             | 22.4 ms                                                         | 22.9 ms: 1.02x slower                                                          |
| json_loads                 | 20.4 us                                                         | 21.1 us: 1.04x slower                                                          |
| sympy_expand               | 398 ms                                                          | 413 ms: 1.04x slower                                                           |
| json_dumps                 | 7.40 ms                                                         | 7.82 ms: 1.06x slower                                                          |
| json                       | 4.15 ms                                                         | 4.40 ms: 1.06x slower                                                          |
| coverage                   | 48.4 ms                                                         | 52.1 ms: 1.07x slower                                                          |
| regex_v8                   | 15.0 ms                                                         | 16.2 ms: 1.08x slower                                                          |
| create_gc_cycles           | 652 us                                                          | 739 us: 1.13x slower                                                           |
| typing_runtime_protocols   | 126 us                                                          | 155 us: 1.23x slower                                                           |
| telco                      | 5.51 ms                                                         | 6.79 ms: 1.23x slower                                                          |
| sqlglot_normalize          | 100 ms                                                          | 246 ms: 2.45x slower                                                           |
| Geometric mean             | (ref)                                                           | 1.08x faster                                                                   |

Benchmark hidden because not significant (4): richards, pidigits, gc_traversal, asyncio_tcp
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, dulwich_log, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240627-3.14.0a0-22b0de2/bm-20240627-pythonperf1_win32-x86-python-22b0de2755ee2d0e2dd2-3.14.0a0-22b0de2.json: genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.06x
- 99% likely to have a speedup of 1.05x

# Memory
- memory change: unknown