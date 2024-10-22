# Results vs. 3.12.0

- fork: python
- ref: c4c7097e64b0c9cb0081
- machine: windows-x86
- commit hash: c4c7097
- commit date: 2024-07-20
- overall geometric mean: 1.23x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.15x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240720-pythonperf1_win32-x86-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 256 ms: 1.09x faster                                                           |
| docutils       | 1.98 sec                                                        | 1.93 sec: 1.03x faster                                                         |
| Geometric mean | (ref)                                                           | 1.04x faster                                                                   |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240720-pythonperf1_win32-x86-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_none_tg         | 278 ms                                                          | 193 ms: 1.43x faster                                                           |
| async_tree_memoization_tg  | 350 ms                                                          | 249 ms: 1.41x faster                                                           |
| async_tree_none            | 298 ms                                                          | 218 ms: 1.36x faster                                                           |
| async_tree_memoization     | 364 ms                                                          | 269 ms: 1.35x faster                                                           |
| async_tree_io_tg           | 677 ms                                                          | 503 ms: 1.35x faster                                                           |
| async_tree_io              | 693 ms                                                          | 540 ms: 1.28x faster                                                           |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 468 ms: 1.20x faster                                                           |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 454 ms: 1.20x faster                                                           |
| Geometric mean             | (ref)                                                           | 1.32x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240720-pythonperf1_win32-x86-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 56.7 ms: 2.24x faster                                                          |
| float          | 76.7 ms                                                         | 43.5 ms: 1.76x faster                                                          |
| pidigits       | 199 ms                                                          | 198 ms: 1.01x faster                                                           |
| Geometric mean | (ref)                                                           | 1.58x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240720-pythonperf1_win32-x86-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 94.3 ms: 1.37x faster                                                          |
| regex_dna      | 127 ms                                                          | 117 ms: 1.08x faster                                                           |
| regex_effbot   | 2.04 ms                                                         | 1.99 ms: 1.02x faster                                                          |
| regex_v8       | 15.0 ms                                                         | 15.9 ms: 1.05x slower                                                          |
| Geometric mean | (ref)                                                           | 1.09x faster                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240720-pythonperf1_win32-x86-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| tomli_loads          | 2.20 sec                                                        | 1.51 sec: 1.45x faster                                                         |
| unpickle_pure_python | 210 us                                                          | 151 us: 1.39x faster                                                           |
| pickle_pure_python   | 286 us                                                          | 214 us: 1.34x faster                                                           |
| xml_etree_iterparse  | 77.6 ms                                                         | 62.8 ms: 1.24x faster                                                          |
| xml_etree_generate   | 72.1 ms                                                         | 58.6 ms: 1.23x faster                                                          |
| xml_etree_process    | 53.2 ms                                                         | 44.5 ms: 1.20x faster                                                          |
| xml_etree_parse      | 113 ms                                                          | 105 ms: 1.08x faster                                                           |
| json_dumps           | 7.40 ms                                                         | 7.05 ms: 1.05x faster                                                          |
| json_loads           | 20.4 us                                                         | 21.0 us: 1.03x slower                                                          |
| Geometric mean       | (ref)                                                           | 1.21x faster                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240720-pythonperf1_win32-x86-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 19.9 ms: 1.04x slower                                                          |
| python_startup         | 22.4 ms                                                         | 23.8 ms: 1.07x slower                                                          |
| Geometric mean         | (ref)                                                           | 1.05x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240720-pythonperf1_win32-x86-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 5.43 ms: 1.83x faster                                                          |
| django_template | 36.9 ms                                                         | 33.2 ms: 1.11x faster                                                          |
| Geometric mean  | (ref)                                                           | 1.43x faster                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240720-pythonperf1_win32-x86-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| deepcopy_memo              | 38.4 us                                                         | 16.1 us: 2.38x faster                                                          |
| nbody                      | 127 ms                                                          | 56.7 ms: 2.24x faster                                                          |
| spectral_norm              | 104 ms                                                          | 47.9 ms: 2.17x faster                                                          |
| mako                       | 9.96 ms                                                         | 5.43 ms: 1.83x faster                                                          |
| float                      | 76.7 ms                                                         | 43.5 ms: 1.76x faster                                                          |
| logging_silent             | 101 ns                                                          | 58.7 ns: 1.72x faster                                                          |
| comprehensions             | 19.2 us                                                         | 11.7 us: 1.65x faster                                                          |
| scimark_fft                | 271 ms                                                          | 168 ms: 1.62x faster                                                           |
| pyflate                    | 424 ms                                                          | 267 ms: 1.59x faster                                                           |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 2.44 ms: 1.58x faster                                                          |
| scimark_monte_carlo        | 66.4 ms                                                         | 43.1 ms: 1.54x faster                                                          |
| deepcopy                   | 360 us                                                          | 235 us: 1.53x faster                                                           |
| fannkuch                   | 354 ms                                                          | 233 ms: 1.52x faster                                                           |
| crypto_pyaes               | 69.2 ms                                                         | 46.3 ms: 1.50x faster                                                          |
| hexiom                     | 6.82 ms                                                         | 4.62 ms: 1.48x faster                                                          |
| tomli_loads                | 2.20 sec                                                        | 1.51 sec: 1.45x faster                                                         |
| async_tree_none_tg         | 278 ms                                                          | 193 ms: 1.43x faster                                                           |
| async_tree_memoization_tg  | 350 ms                                                          | 249 ms: 1.41x faster                                                           |
| generators                 | 38.5 ms                                                         | 27.5 ms: 1.40x faster                                                          |
| unpickle_pure_python       | 210 us                                                          | 151 us: 1.39x faster                                                           |
| regex_compile              | 129 ms                                                          | 94.3 ms: 1.37x faster                                                          |
| async_tree_none            | 298 ms                                                          | 218 ms: 1.36x faster                                                           |
| async_tree_memoization     | 364 ms                                                          | 269 ms: 1.35x faster                                                           |
| async_tree_io_tg           | 677 ms                                                          | 503 ms: 1.35x faster                                                           |
| raytrace                   | 308 ms                                                          | 229 ms: 1.34x faster                                                           |
| pickle_pure_python         | 286 us                                                          | 214 us: 1.34x faster                                                           |
| chaos                      | 69.4 ms                                                         | 52.3 ms: 1.33x faster                                                          |
| deepcopy_reduce            | 3.23 us                                                         | 2.46 us: 1.31x faster                                                          |
| deltablue                  | 3.58 ms                                                         | 2.74 ms: 1.31x faster                                                          |
| sqlglot_parse              | 1.25 ms                                                         | 959 us: 1.30x faster                                                           |
| async_tree_io              | 693 ms                                                          | 540 ms: 1.28x faster                                                           |
| pprint_pformat             | 1.50 sec                                                        | 1.17 sec: 1.28x faster                                                         |
| scimark_sor                | 130 ms                                                          | 102 ms: 1.28x faster                                                           |
| nqueens                    | 93.7 ms                                                         | 73.5 ms: 1.27x faster                                                          |
| pprint_safe_repr           | 721 ms                                                          | 570 ms: 1.26x faster                                                           |
| logging_simple             | 9.75 us                                                         | 7.74 us: 1.26x faster                                                          |
| sqlglot_transpile          | 1.53 ms                                                         | 1.22 ms: 1.25x faster                                                          |
| logging_format             | 10.4 us                                                         | 8.36 us: 1.24x faster                                                          |
| xml_etree_iterparse        | 77.6 ms                                                         | 62.8 ms: 1.24x faster                                                          |
| xml_etree_generate         | 72.1 ms                                                         | 58.6 ms: 1.23x faster                                                          |
| richards                   | 41.3 ms                                                         | 33.6 ms: 1.23x faster                                                          |
| meteor_contest             | 86.9 ms                                                         | 70.7 ms: 1.23x faster                                                          |
| go                         | 137 ms                                                          | 114 ms: 1.21x faster                                                           |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 468 ms: 1.20x faster                                                           |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 454 ms: 1.20x faster                                                           |
| scimark_lu                 | 93.2 ms                                                         | 77.6 ms: 1.20x faster                                                          |
| richards_super             | 46.5 ms                                                         | 38.7 ms: 1.20x faster                                                          |
| xml_etree_process          | 53.2 ms                                                         | 44.5 ms: 1.20x faster                                                          |
| pycparser                  | 978 ms                                                          | 835 ms: 1.17x faster                                                           |
| mdp                        | 1.91 sec                                                        | 1.68 sec: 1.14x faster                                                         |
| coroutines                 | 20.9 ms                                                         | 18.4 ms: 1.14x faster                                                          |
| sympy_sum                  | 123 ms                                                          | 108 ms: 1.14x faster                                                           |
| bench_thread_pool          | 1.10 ms                                                         | 989 us: 1.12x faster                                                           |
| sympy_str                  | 240 ms                                                          | 215 ms: 1.11x faster                                                           |
| sqlglot_optimize           | 48.5 ms                                                         | 43.6 ms: 1.11x faster                                                          |
| django_template            | 36.9 ms                                                         | 33.2 ms: 1.11x faster                                                          |
| sympy_integrate            | 17.5 ms                                                         | 15.9 ms: 1.10x faster                                                          |
| 2to3                       | 280 ms                                                          | 256 ms: 1.09x faster                                                           |
| xml_etree_parse            | 113 ms                                                          | 105 ms: 1.08x faster                                                           |
| regex_dna                  | 127 ms                                                          | 117 ms: 1.08x faster                                                           |
| json_dumps                 | 7.40 ms                                                         | 7.05 ms: 1.05x faster                                                          |
| asyncio_tcp_ssl            | 17.7 sec                                                        | 16.9 sec: 1.05x faster                                                         |
| pathlib                    | 91.4 ms                                                         | 87.9 ms: 1.04x faster                                                          |
| sympy_expand               | 398 ms                                                          | 383 ms: 1.04x faster                                                           |
| docutils                   | 1.98 sec                                                        | 1.93 sec: 1.03x faster                                                         |
| regex_effbot               | 2.04 ms                                                         | 1.99 ms: 1.02x faster                                                          |
| pidigits                   | 199 ms                                                          | 198 ms: 1.01x faster                                                           |
| json_loads                 | 20.4 us                                                         | 21.0 us: 1.03x slower                                                          |
| json                       | 4.15 ms                                                         | 4.33 ms: 1.04x slower                                                          |
| python_startup_no_site     | 19.1 ms                                                         | 19.9 ms: 1.04x slower                                                          |
| regex_v8                   | 15.0 ms                                                         | 15.9 ms: 1.05x slower                                                          |
| python_startup             | 22.4 ms                                                         | 23.8 ms: 1.07x slower                                                          |
| coverage                   | 48.4 ms                                                         | 52.9 ms: 1.09x slower                                                          |
| typing_runtime_protocols   | 126 us                                                          | 146 us: 1.15x slower                                                           |
| create_gc_cycles           | 652 us                                                          | 766 us: 1.18x slower                                                           |
| sqlglot_normalize          | 100 ms                                                          | 231 ms: 2.30x slower                                                           |
| Geometric mean             | (ref)                                                           | 1.23x faster                                                                   |

Benchmark hidden because not significant (6): gc_traversal, bench_mp_pool, async_generators, telco, tornado_http, asyncio_tcp
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, dulwich_log, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240720-3.14.0a0-c4c7097-JIT/bm-20240720-pythonperf1_win32-x86-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097.json: genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.19x
- 95% likely to have a speedup of 1.18x
- 99% likely to have a speedup of 1.15x

# Memory
- memory change: unknown