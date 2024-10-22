# Results vs. 3.12.0

- fork: python
- ref: c4c7097e64b0c9cb0081
- machine: windows-x86
- commit hash: c4c7097
- commit date: 2024-07-20
- overall geometric mean: 1.14x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.11x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240720-pythonperf1_win32-x86-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 251 ms: 1.11x faster                                                           |
| docutils       | 1.98 sec                                                        | 1.90 sec: 1.05x faster                                                         |
| tornado_http   | 105 ms                                                          | 103 ms: 1.02x faster                                                           |
| Geometric mean | (ref)                                                           | 1.06x faster                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240720-pythonperf1_win32-x86-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_none_tg         | 278 ms                                                          | 193 ms: 1.44x faster                                                           |
| async_tree_memoization_tg  | 350 ms                                                          | 246 ms: 1.43x faster                                                           |
| async_tree_io_tg           | 677 ms                                                          | 502 ms: 1.35x faster                                                           |
| async_tree_none            | 298 ms                                                          | 224 ms: 1.33x faster                                                           |
| async_tree_memoization     | 364 ms                                                          | 276 ms: 1.32x faster                                                           |
| async_tree_io              | 693 ms                                                          | 541 ms: 1.28x faster                                                           |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 463 ms: 1.18x faster                                                           |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 479 ms: 1.18x faster                                                           |
| Geometric mean             | (ref)                                                           | 1.31x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240720-pythonperf1_win32-x86-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 91.4 ms: 1.39x faster                                                          |
| float          | 76.7 ms                                                         | 60.5 ms: 1.27x faster                                                          |
| pidigits       | 199 ms                                                          | 198 ms: 1.00x faster                                                           |
| Geometric mean | (ref)                                                           | 1.21x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240720-pythonperf1_win32-x86-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 105 ms: 1.23x faster                                                           |
| regex_dna      | 127 ms                                                          | 121 ms: 1.05x faster                                                           |
| regex_effbot   | 2.04 ms                                                         | 1.98 ms: 1.03x faster                                                          |
| regex_v8       | 15.0 ms                                                         | 16.2 ms: 1.08x slower                                                          |
| Geometric mean | (ref)                                                           | 1.05x faster                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240720-pythonperf1_win32-x86-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| unpickle_pure_python | 210 us                                                          | 168 us: 1.25x faster                                                           |
| tomli_loads          | 2.20 sec                                                        | 1.84 sec: 1.19x faster                                                         |
| pickle_pure_python   | 286 us                                                          | 241 us: 1.19x faster                                                           |
| xml_etree_iterparse  | 77.6 ms                                                         | 67.5 ms: 1.15x faster                                                          |
| xml_etree_process    | 53.2 ms                                                         | 48.2 ms: 1.10x faster                                                          |
| xml_etree_generate   | 72.1 ms                                                         | 65.6 ms: 1.10x faster                                                          |
| xml_etree_parse      | 113 ms                                                          | 106 ms: 1.07x faster                                                           |
| json_dumps           | 7.40 ms                                                         | 7.21 ms: 1.03x faster                                                          |
| json_loads           | 20.4 us                                                         | 20.5 us: 1.01x slower                                                          |
| Geometric mean       | (ref)                                                           | 1.12x faster                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240720-pythonperf1_win32-x86-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 20.3 ms: 1.06x slower                                                          |
| python_startup         | 22.4 ms                                                         | 24.2 ms: 1.08x slower                                                          |
| Geometric mean         | (ref)                                                           | 1.07x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240720-pythonperf1_win32-x86-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 7.94 ms: 1.25x faster                                                          |
| django_template | 36.9 ms                                                         | 33.8 ms: 1.09x faster                                                          |
| Geometric mean  | (ref)                                                           | 1.17x faster                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240720-pythonperf1_win32-x86-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| deepcopy_memo              | 38.4 us                                                         | 21.4 us: 1.79x faster                                                          |
| generators                 | 38.5 ms                                                         | 26.1 ms: 1.48x faster                                                          |
| deepcopy                   | 360 us                                                          | 247 us: 1.46x faster                                                           |
| async_tree_none_tg         | 278 ms                                                          | 193 ms: 1.44x faster                                                           |
| async_tree_memoization_tg  | 350 ms                                                          | 246 ms: 1.43x faster                                                           |
| raytrace                   | 308 ms                                                          | 216 ms: 1.42x faster                                                           |
| logging_silent             | 101 ns                                                          | 71.0 ns: 1.42x faster                                                          |
| comprehensions             | 19.2 us                                                         | 13.5 us: 1.42x faster                                                          |
| nbody                      | 127 ms                                                          | 91.4 ms: 1.39x faster                                                          |
| hexiom                     | 6.82 ms                                                         | 4.94 ms: 1.38x faster                                                          |
| deltablue                  | 3.58 ms                                                         | 2.62 ms: 1.37x faster                                                          |
| scimark_lu                 | 93.2 ms                                                         | 68.5 ms: 1.36x faster                                                          |
| async_tree_io_tg           | 677 ms                                                          | 502 ms: 1.35x faster                                                           |
| scimark_sor                | 130 ms                                                          | 97.2 ms: 1.34x faster                                                          |
| async_tree_none            | 298 ms                                                          | 224 ms: 1.33x faster                                                           |
| async_tree_memoization     | 364 ms                                                          | 276 ms: 1.32x faster                                                           |
| spectral_norm              | 104 ms                                                          | 78.8 ms: 1.32x faster                                                          |
| chaos                      | 69.4 ms                                                         | 52.9 ms: 1.31x faster                                                          |
| async_tree_io              | 693 ms                                                          | 541 ms: 1.28x faster                                                           |
| float                      | 76.7 ms                                                         | 60.5 ms: 1.27x faster                                                          |
| deepcopy_reduce            | 3.23 us                                                         | 2.56 us: 1.26x faster                                                          |
| scimark_monte_carlo        | 66.4 ms                                                         | 52.9 ms: 1.26x faster                                                          |
| pyflate                    | 424 ms                                                          | 338 ms: 1.25x faster                                                           |
| mako                       | 9.96 ms                                                         | 7.94 ms: 1.25x faster                                                          |
| unpickle_pure_python       | 210 us                                                          | 168 us: 1.25x faster                                                           |
| logging_simple             | 9.75 us                                                         | 7.86 us: 1.24x faster                                                          |
| regex_compile              | 129 ms                                                          | 105 ms: 1.23x faster                                                           |
| logging_format             | 10.4 us                                                         | 8.53 us: 1.22x faster                                                          |
| coroutines                 | 20.9 ms                                                         | 17.2 ms: 1.21x faster                                                          |
| go                         | 137 ms                                                          | 113 ms: 1.21x faster                                                           |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 3.20 ms: 1.21x faster                                                          |
| tomli_loads                | 2.20 sec                                                        | 1.84 sec: 1.19x faster                                                         |
| scimark_fft                | 271 ms                                                          | 228 ms: 1.19x faster                                                           |
| pickle_pure_python         | 286 us                                                          | 241 us: 1.19x faster                                                           |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 463 ms: 1.18x faster                                                           |
| nqueens                    | 93.7 ms                                                         | 79.5 ms: 1.18x faster                                                          |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 479 ms: 1.18x faster                                                           |
| crypto_pyaes               | 69.2 ms                                                         | 58.9 ms: 1.18x faster                                                          |
| sqlglot_parse              | 1.25 ms                                                         | 1.07 ms: 1.16x faster                                                          |
| xml_etree_iterparse        | 77.6 ms                                                         | 67.5 ms: 1.15x faster                                                          |
| sqlglot_transpile          | 1.53 ms                                                         | 1.33 ms: 1.15x faster                                                          |
| pycparser                  | 978 ms                                                          | 852 ms: 1.15x faster                                                           |
| sympy_integrate            | 17.5 ms                                                         | 15.5 ms: 1.13x faster                                                          |
| pprint_pformat             | 1.50 sec                                                        | 1.33 sec: 1.13x faster                                                         |
| richards                   | 41.3 ms                                                         | 36.9 ms: 1.12x faster                                                          |
| pprint_safe_repr           | 721 ms                                                          | 645 ms: 1.12x faster                                                           |
| meteor_contest             | 86.9 ms                                                         | 77.9 ms: 1.11x faster                                                          |
| sympy_sum                  | 123 ms                                                          | 110 ms: 1.11x faster                                                           |
| 2to3                       | 280 ms                                                          | 251 ms: 1.11x faster                                                           |
| bench_thread_pool          | 1.10 ms                                                         | 996 us: 1.11x faster                                                           |
| richards_super             | 46.5 ms                                                         | 42.0 ms: 1.11x faster                                                          |
| xml_etree_process          | 53.2 ms                                                         | 48.2 ms: 1.10x faster                                                          |
| mdp                        | 1.91 sec                                                        | 1.73 sec: 1.10x faster                                                         |
| xml_etree_generate         | 72.1 ms                                                         | 65.6 ms: 1.10x faster                                                          |
| sqlglot_optimize           | 48.5 ms                                                         | 44.3 ms: 1.09x faster                                                          |
| sympy_str                  | 240 ms                                                          | 219 ms: 1.09x faster                                                           |
| django_template            | 36.9 ms                                                         | 33.8 ms: 1.09x faster                                                          |
| async_generators           | 313 ms                                                          | 290 ms: 1.08x faster                                                           |
| fannkuch                   | 354 ms                                                          | 328 ms: 1.08x faster                                                           |
| xml_etree_parse            | 113 ms                                                          | 106 ms: 1.07x faster                                                           |
| regex_dna                  | 127 ms                                                          | 121 ms: 1.05x faster                                                           |
| docutils                   | 1.98 sec                                                        | 1.90 sec: 1.05x faster                                                         |
| asyncio_tcp_ssl            | 17.7 sec                                                        | 17.0 sec: 1.04x faster                                                         |
| pathlib                    | 91.4 ms                                                         | 88.2 ms: 1.04x faster                                                          |
| regex_effbot               | 2.04 ms                                                         | 1.98 ms: 1.03x faster                                                          |
| json_dumps                 | 7.40 ms                                                         | 7.21 ms: 1.03x faster                                                          |
| sympy_expand               | 398 ms                                                          | 388 ms: 1.02x faster                                                           |
| tornado_http               | 105 ms                                                          | 103 ms: 1.02x faster                                                           |
| pidigits                   | 199 ms                                                          | 198 ms: 1.00x faster                                                           |
| bench_mp_pool              | 75.4 ms                                                         | 75.9 ms: 1.01x slower                                                          |
| json_loads                 | 20.4 us                                                         | 20.5 us: 1.01x slower                                                          |
| json                       | 4.15 ms                                                         | 4.28 ms: 1.03x slower                                                          |
| python_startup_no_site     | 19.1 ms                                                         | 20.3 ms: 1.06x slower                                                          |
| regex_v8                   | 15.0 ms                                                         | 16.2 ms: 1.08x slower                                                          |
| python_startup             | 22.4 ms                                                         | 24.2 ms: 1.08x slower                                                          |
| asyncio_tcp                | 662 ms                                                          | 732 ms: 1.10x slower                                                           |
| telco                      | 5.51 ms                                                         | 6.15 ms: 1.12x slower                                                          |
| coverage                   | 48.4 ms                                                         | 54.3 ms: 1.12x slower                                                          |
| create_gc_cycles           | 652 us                                                          | 748 us: 1.15x slower                                                           |
| typing_runtime_protocols   | 126 us                                                          | 145 us: 1.15x slower                                                           |
| sqlglot_normalize          | 100 ms                                                          | 229 ms: 2.29x slower                                                           |
| Geometric mean             | (ref)                                                           | 1.14x faster                                                                   |

Benchmark hidden because not significant (1): gc_traversal
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, dulwich_log, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240720-3.14.0a0-c4c7097/bm-20240720-pythonperf1_win32-x86-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097.json: genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.12x
- 95% likely to have a speedup of 1.12x
- 99% likely to have a speedup of 1.11x

# Memory
- memory change: unknown