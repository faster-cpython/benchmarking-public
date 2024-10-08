# Results vs. 3.12.0

- fork: python
- ref: 04eb5c8db1e24cabd0cb
- machine: windows-x86
- commit hash: 04eb5c8
- commit date: 2024-07-27
- overall geometric mean: 1.16x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.12x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240727-pythonperf1_win32-x86-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 249 ms: 1.12x faster                                                           |
| docutils       | 1.98 sec                                                        | 1.89 sec: 1.05x faster                                                         |
| tornado_http   | 105 ms                                                          | 104 ms: 1.01x faster                                                           |
| Geometric mean | (ref)                                                           | 1.06x faster                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240727-pythonperf1_win32-x86-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_none_tg         | 278 ms                                                          | 193 ms: 1.44x faster                                                           |
| async_tree_memoization_tg  | 350 ms                                                          | 244 ms: 1.44x faster                                                           |
| async_tree_io_tg           | 677 ms                                                          | 500 ms: 1.35x faster                                                           |
| async_tree_none            | 298 ms                                                          | 223 ms: 1.33x faster                                                           |
| async_tree_memoization     | 364 ms                                                          | 274 ms: 1.33x faster                                                           |
| async_tree_io              | 693 ms                                                          | 541 ms: 1.28x faster                                                           |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 481 ms: 1.17x faster                                                           |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 469 ms: 1.16x faster                                                           |
| Geometric mean             | (ref)                                                           | 1.31x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240727-pythonperf1_win32-x86-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 90.9 ms: 1.40x faster                                                          |
| float          | 76.7 ms                                                         | 58.2 ms: 1.32x faster                                                          |
| pidigits       | 199 ms                                                          | 197 ms: 1.01x faster                                                           |
| Geometric mean | (ref)                                                           | 1.23x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240727-pythonperf1_win32-x86-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 104 ms: 1.24x faster                                                           |
| regex_effbot   | 2.04 ms                                                         | 1.92 ms: 1.06x faster                                                          |
| regex_dna      | 127 ms                                                          | 122 ms: 1.04x faster                                                           |
| regex_v8       | 15.0 ms                                                         | 16.3 ms: 1.08x slower                                                          |
| Geometric mean | (ref)                                                           | 1.06x faster                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240727-pythonperf1_win32-x86-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| tomli_loads          | 2.20 sec                                                        | 1.77 sec: 1.24x faster                                                         |
| unpickle_pure_python | 210 us                                                          | 170 us: 1.23x faster                                                           |
| pickle_pure_python   | 286 us                                                          | 239 us: 1.20x faster                                                           |
| xml_etree_iterparse  | 77.6 ms                                                         | 67.5 ms: 1.15x faster                                                          |
| xml_etree_process    | 53.2 ms                                                         | 46.9 ms: 1.14x faster                                                          |
| xml_etree_generate   | 72.1 ms                                                         | 65.5 ms: 1.10x faster                                                          |
| xml_etree_parse      | 113 ms                                                          | 106 ms: 1.07x faster                                                           |
| json_loads           | 20.4 us                                                         | 20.2 us: 1.01x faster                                                          |
| json_dumps           | 7.40 ms                                                         | 7.46 ms: 1.01x slower                                                          |
| Geometric mean       | (ref)                                                           | 1.12x faster                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240727-pythonperf1_win32-x86-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 19.4 ms: 1.02x slower                                                          |
| python_startup         | 22.4 ms                                                         | 23.8 ms: 1.07x slower                                                          |
| Geometric mean         | (ref)                                                           | 1.04x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240727-pythonperf1_win32-x86-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 8.06 ms: 1.24x faster                                                          |
| django_template | 36.9 ms                                                         | 33.3 ms: 1.11x faster                                                          |
| Geometric mean  | (ref)                                                           | 1.17x faster                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240727-pythonperf1_win32-x86-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| deepcopy_memo              | 38.4 us                                                         | 20.9 us: 1.84x faster                                                          |
| generators                 | 38.5 ms                                                         | 25.7 ms: 1.50x faster                                                          |
| deepcopy                   | 360 us                                                          | 242 us: 1.49x faster                                                           |
| comprehensions             | 19.2 us                                                         | 13.3 us: 1.44x faster                                                          |
| async_tree_none_tg         | 278 ms                                                          | 193 ms: 1.44x faster                                                           |
| async_tree_memoization_tg  | 350 ms                                                          | 244 ms: 1.44x faster                                                           |
| nbody                      | 127 ms                                                          | 90.9 ms: 1.40x faster                                                          |
| logging_silent             | 101 ns                                                          | 72.6 ns: 1.39x faster                                                          |
| raytrace                   | 308 ms                                                          | 222 ms: 1.39x faster                                                           |
| deltablue                  | 3.58 ms                                                         | 2.58 ms: 1.39x faster                                                          |
| hexiom                     | 6.82 ms                                                         | 4.95 ms: 1.38x faster                                                          |
| scimark_lu                 | 93.2 ms                                                         | 68.4 ms: 1.36x faster                                                          |
| async_tree_io_tg           | 677 ms                                                          | 500 ms: 1.35x faster                                                           |
| async_tree_none            | 298 ms                                                          | 223 ms: 1.33x faster                                                           |
| async_tree_memoization     | 364 ms                                                          | 274 ms: 1.33x faster                                                           |
| spectral_norm              | 104 ms                                                          | 78.1 ms: 1.33x faster                                                          |
| scimark_sor                | 130 ms                                                          | 98.4 ms: 1.32x faster                                                          |
| float                      | 76.7 ms                                                         | 58.2 ms: 1.32x faster                                                          |
| scimark_monte_carlo        | 66.4 ms                                                         | 50.6 ms: 1.31x faster                                                          |
| nqueens                    | 93.7 ms                                                         | 71.9 ms: 1.30x faster                                                          |
| chaos                      | 69.4 ms                                                         | 53.6 ms: 1.29x faster                                                          |
| deepcopy_reduce            | 3.23 us                                                         | 2.51 us: 1.29x faster                                                          |
| async_tree_io              | 693 ms                                                          | 541 ms: 1.28x faster                                                           |
| logging_simple             | 9.75 us                                                         | 7.78 us: 1.25x faster                                                          |
| go                         | 137 ms                                                          | 110 ms: 1.25x faster                                                           |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 3.10 ms: 1.25x faster                                                          |
| tomli_loads                | 2.20 sec                                                        | 1.77 sec: 1.24x faster                                                         |
| pyflate                    | 424 ms                                                          | 341 ms: 1.24x faster                                                           |
| regex_compile              | 129 ms                                                          | 104 ms: 1.24x faster                                                           |
| mako                       | 9.96 ms                                                         | 8.06 ms: 1.24x faster                                                          |
| unpickle_pure_python       | 210 us                                                          | 170 us: 1.23x faster                                                           |
| scimark_fft                | 271 ms                                                          | 221 ms: 1.23x faster                                                           |
| sqlglot_parse              | 1.25 ms                                                         | 1.02 ms: 1.22x faster                                                          |
| crypto_pyaes               | 69.2 ms                                                         | 56.8 ms: 1.22x faster                                                          |
| logging_format             | 10.4 us                                                         | 8.58 us: 1.21x faster                                                          |
| coroutines                 | 20.9 ms                                                         | 17.3 ms: 1.21x faster                                                          |
| sqlglot_transpile          | 1.53 ms                                                         | 1.28 ms: 1.20x faster                                                          |
| pickle_pure_python         | 286 us                                                          | 239 us: 1.20x faster                                                           |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 481 ms: 1.17x faster                                                           |
| dulwich_log                | 58.5 ms                                                         | 50.1 ms: 1.17x faster                                                          |
| richards_super             | 46.5 ms                                                         | 39.9 ms: 1.16x faster                                                          |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 469 ms: 1.16x faster                                                           |
| sympy_integrate            | 17.5 ms                                                         | 15.2 ms: 1.15x faster                                                          |
| xml_etree_iterparse        | 77.6 ms                                                         | 67.5 ms: 1.15x faster                                                          |
| mdp                        | 1.91 sec                                                        | 1.67 sec: 1.14x faster                                                         |
| pycparser                  | 978 ms                                                          | 858 ms: 1.14x faster                                                           |
| fannkuch                   | 354 ms                                                          | 311 ms: 1.14x faster                                                           |
| xml_etree_process          | 53.2 ms                                                         | 46.9 ms: 1.14x faster                                                          |
| sympy_sum                  | 123 ms                                                          | 109 ms: 1.13x faster                                                           |
| pprint_pformat             | 1.50 sec                                                        | 1.33 sec: 1.13x faster                                                         |
| richards                   | 41.3 ms                                                         | 36.7 ms: 1.13x faster                                                          |
| 2to3                       | 280 ms                                                          | 249 ms: 1.12x faster                                                           |
| async_generators           | 313 ms                                                          | 281 ms: 1.12x faster                                                           |
| pprint_safe_repr           | 721 ms                                                          | 646 ms: 1.12x faster                                                           |
| sqlglot_optimize           | 48.5 ms                                                         | 43.5 ms: 1.11x faster                                                          |
| bench_thread_pool          | 1.10 ms                                                         | 992 us: 1.11x faster                                                           |
| meteor_contest             | 86.9 ms                                                         | 78.3 ms: 1.11x faster                                                          |
| django_template            | 36.9 ms                                                         | 33.3 ms: 1.11x faster                                                          |
| sympy_str                  | 240 ms                                                          | 217 ms: 1.10x faster                                                           |
| xml_etree_generate         | 72.1 ms                                                         | 65.5 ms: 1.10x faster                                                          |
| xml_etree_parse            | 113 ms                                                          | 106 ms: 1.07x faster                                                           |
| regex_effbot               | 2.04 ms                                                         | 1.92 ms: 1.06x faster                                                          |
| docutils                   | 1.98 sec                                                        | 1.89 sec: 1.05x faster                                                         |
| regex_dna                  | 127 ms                                                          | 122 ms: 1.04x faster                                                           |
| pathlib                    | 91.4 ms                                                         | 88.1 ms: 1.04x faster                                                          |
| asyncio_tcp_ssl            | 17.7 sec                                                        | 17.1 sec: 1.04x faster                                                         |
| sympy_expand               | 398 ms                                                          | 385 ms: 1.03x faster                                                           |
| bench_mp_pool              | 75.4 ms                                                         | 73.4 ms: 1.03x faster                                                          |
| pidigits                   | 199 ms                                                          | 197 ms: 1.01x faster                                                           |
| tornado_http               | 105 ms                                                          | 104 ms: 1.01x faster                                                           |
| json_loads                 | 20.4 us                                                         | 20.2 us: 1.01x faster                                                          |
| json_dumps                 | 7.40 ms                                                         | 7.46 ms: 1.01x slower                                                          |
| python_startup_no_site     | 19.1 ms                                                         | 19.4 ms: 1.02x slower                                                          |
| python_startup             | 22.4 ms                                                         | 23.8 ms: 1.07x slower                                                          |
| coverage                   | 48.4 ms                                                         | 52.0 ms: 1.07x slower                                                          |
| regex_v8                   | 15.0 ms                                                         | 16.3 ms: 1.08x slower                                                          |
| asyncio_tcp                | 662 ms                                                          | 722 ms: 1.09x slower                                                           |
| telco                      | 5.51 ms                                                         | 6.24 ms: 1.13x slower                                                          |
| create_gc_cycles           | 652 us                                                          | 748 us: 1.15x slower                                                           |
| typing_runtime_protocols   | 126 us                                                          | 148 us: 1.17x slower                                                           |
| sqlglot_normalize          | 100 ms                                                          | 225 ms: 2.25x slower                                                           |
| Geometric mean             | (ref)                                                           | 1.16x faster                                                                   |

Benchmark hidden because not significant (2): gc_traversal, json
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240727-3.14.0a0-04eb5c8/bm-20240727-pythonperf1_win32-x86-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8.json: genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.13x
- 95% likely to have a speedup of 1.13x
- 99% likely to have a speedup of 1.12x

# Memory
- memory change: unknown