# Results vs. 3.12.0

- fork: mdboom
- ref: simplify_richcompare
- machine: windows-x86
- commit hash: 15b187e
- commit date: 2024-08-29
- overall geometric mean: 1.133x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.11x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240829-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 251 ms: 1.12x faster                                                           |
| docutils       | 1.98 sec                                                        | 1.86 sec: 1.07x faster                                                         |
| Geometric mean | (ref)                                                           | 1.06x faster                                                                   |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240829-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_none_tg         | 278 ms                                                          | 199 ms: 1.39x faster                                                           |
| async_tree_none            | 298 ms                                                          | 215 ms: 1.39x faster                                                           |
| async_tree_memoization_tg  | 350 ms                                                          | 253 ms: 1.38x faster                                                           |
| async_tree_memoization     | 364 ms                                                          | 276 ms: 1.32x faster                                                           |
| async_tree_io_tg           | 677 ms                                                          | 518 ms: 1.31x faster                                                           |
| async_tree_io              | 693 ms                                                          | 539 ms: 1.28x faster                                                           |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 465 ms: 1.21x faster                                                           |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 465 ms: 1.18x faster                                                           |
| Geometric mean             | (ref)                                                           | 1.31x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240829-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 95.8 ms: 1.33x faster                                                          |
| float          | 76.7 ms                                                         | 62.0 ms: 1.24x faster                                                          |
| pidigits       | 199 ms                                                          | 202 ms: 1.01x slower                                                           |
| Geometric mean | (ref)                                                           | 1.17x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240829-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 107 ms: 1.21x faster                                                           |
| regex_effbot   | 2.04 ms                                                         | 1.94 ms: 1.05x faster                                                          |
| regex_dna      | 127 ms                                                          | 122 ms: 1.04x faster                                                           |
| regex_v8       | 15.0 ms                                                         | 16.2 ms: 1.08x slower                                                          |
| Geometric mean | (ref)                                                           | 1.05x faster                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240829-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| tomli_loads          | 2.20 sec                                                        | 1.86 sec: 1.18x faster                                                         |
| unpickle_pure_python | 210 us                                                          | 179 us: 1.17x faster                                                           |
| xml_etree_iterparse  | 77.6 ms                                                         | 67.9 ms: 1.14x faster                                                          |
| pickle_pure_python   | 286 us                                                          | 254 us: 1.12x faster                                                           |
| xml_etree_generate   | 72.1 ms                                                         | 68.4 ms: 1.05x faster                                                          |
| xml_etree_parse      | 113 ms                                                          | 107 ms: 1.05x faster                                                           |
| xml_etree_process    | 53.2 ms                                                         | 51.0 ms: 1.04x faster                                                          |
| json_dumps           | 7.40 ms                                                         | 7.74 ms: 1.05x slower                                                          |
| Geometric mean       | (ref)                                                           | 1.08x faster                                                                   |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240829-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 19.7 ms: 1.04x slower                                                          |
| python_startup         | 22.4 ms                                                         | 24.1 ms: 1.08x slower                                                          |
| Geometric mean         | (ref)                                                           | 1.06x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240829-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 8.41 ms: 1.18x faster                                                          |
| django_template | 36.9 ms                                                         | 32.8 ms: 1.13x faster                                                          |
| Geometric mean  | (ref)                                                           | 1.15x faster                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240829-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| deepcopy_memo              | 38.4 us                                                         | 22.0 us: 1.74x faster                                                          |
| deepcopy                   | 360 us                                                          | 246 us: 1.46x faster                                                           |
| comprehensions             | 19.2 us                                                         | 13.5 us: 1.42x faster                                                          |
| async_tree_none_tg         | 278 ms                                                          | 199 ms: 1.39x faster                                                           |
| async_tree_none            | 298 ms                                                          | 215 ms: 1.39x faster                                                           |
| async_tree_memoization_tg  | 350 ms                                                          | 253 ms: 1.38x faster                                                           |
| generators                 | 38.5 ms                                                         | 27.9 ms: 1.38x faster                                                          |
| spectral_norm              | 104 ms                                                          | 75.6 ms: 1.37x faster                                                          |
| logging_silent             | 101 ns                                                          | 74.5 ns: 1.36x faster                                                          |
| go                         | 137 ms                                                          | 103 ms: 1.34x faster                                                           |
| nbody                      | 127 ms                                                          | 95.8 ms: 1.33x faster                                                          |
| scimark_lu                 | 93.2 ms                                                         | 70.6 ms: 1.32x faster                                                          |
| async_tree_memoization     | 364 ms                                                          | 276 ms: 1.32x faster                                                           |
| deltablue                  | 3.58 ms                                                         | 2.72 ms: 1.32x faster                                                          |
| async_tree_io_tg           | 677 ms                                                          | 518 ms: 1.31x faster                                                           |
| raytrace                   | 308 ms                                                          | 236 ms: 1.31x faster                                                           |
| chaos                      | 69.4 ms                                                         | 53.5 ms: 1.30x faster                                                          |
| hexiom                     | 6.82 ms                                                         | 5.29 ms: 1.29x faster                                                          |
| async_tree_io              | 693 ms                                                          | 539 ms: 1.28x faster                                                           |
| deepcopy_reduce            | 3.23 us                                                         | 2.51 us: 1.28x faster                                                          |
| scimark_sor                | 130 ms                                                          | 102 ms: 1.27x faster                                                           |
| float                      | 76.7 ms                                                         | 62.0 ms: 1.24x faster                                                          |
| nqueens                    | 93.7 ms                                                         | 75.9 ms: 1.23x faster                                                          |
| logging_simple             | 9.75 us                                                         | 8.02 us: 1.22x faster                                                          |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 465 ms: 1.21x faster                                                           |
| regex_compile              | 129 ms                                                          | 107 ms: 1.21x faster                                                           |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 3.19 ms: 1.21x faster                                                          |
| coroutines                 | 20.9 ms                                                         | 17.5 ms: 1.19x faster                                                          |
| crypto_pyaes               | 69.2 ms                                                         | 58.2 ms: 1.19x faster                                                          |
| pyflate                    | 424 ms                                                          | 358 ms: 1.19x faster                                                           |
| logging_format             | 10.4 us                                                         | 8.78 us: 1.19x faster                                                          |
| mako                       | 9.96 ms                                                         | 8.41 ms: 1.18x faster                                                          |
| tomli_loads                | 2.20 sec                                                        | 1.86 sec: 1.18x faster                                                         |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 465 ms: 1.18x faster                                                           |
| unpickle_pure_python       | 210 us                                                          | 179 us: 1.17x faster                                                           |
| scimark_monte_carlo        | 66.4 ms                                                         | 56.6 ms: 1.17x faster                                                          |
| dulwich_log                | 58.5 ms                                                         | 50.0 ms: 1.17x faster                                                          |
| sqlglot_parse              | 1.25 ms                                                         | 1.07 ms: 1.16x faster                                                          |
| sqlglot_transpile          | 1.53 ms                                                         | 1.32 ms: 1.16x faster                                                          |
| sympy_sum                  | 123 ms                                                          | 107 ms: 1.15x faster                                                           |
| scimark_fft                | 271 ms                                                          | 237 ms: 1.14x faster                                                           |
| xml_etree_iterparse        | 77.6 ms                                                         | 67.9 ms: 1.14x faster                                                          |
| sympy_integrate            | 17.5 ms                                                         | 15.3 ms: 1.14x faster                                                          |
| pycparser                  | 978 ms                                                          | 857 ms: 1.14x faster                                                           |
| django_template            | 36.9 ms                                                         | 32.8 ms: 1.13x faster                                                          |
| mdp                        | 1.91 sec                                                        | 1.70 sec: 1.12x faster                                                         |
| pprint_pformat             | 1.50 sec                                                        | 1.33 sec: 1.12x faster                                                         |
| pickle_pure_python         | 286 us                                                          | 254 us: 1.12x faster                                                           |
| 2to3                       | 280 ms                                                          | 251 ms: 1.12x faster                                                           |
| sqlglot_optimize           | 48.5 ms                                                         | 43.5 ms: 1.12x faster                                                          |
| sympy_str                  | 240 ms                                                          | 216 ms: 1.11x faster                                                           |
| pprint_safe_repr           | 721 ms                                                          | 654 ms: 1.10x faster                                                           |
| bench_thread_pool          | 1.10 ms                                                         | 1.01 ms: 1.09x faster                                                          |
| meteor_contest             | 86.9 ms                                                         | 79.9 ms: 1.09x faster                                                          |
| docutils                   | 1.98 sec                                                        | 1.86 sec: 1.07x faster                                                         |
| fannkuch                   | 354 ms                                                          | 332 ms: 1.07x faster                                                           |
| richards                   | 41.3 ms                                                         | 39.0 ms: 1.06x faster                                                          |
| xml_etree_generate         | 72.1 ms                                                         | 68.4 ms: 1.05x faster                                                          |
| xml_etree_parse            | 113 ms                                                          | 107 ms: 1.05x faster                                                           |
| pathlib                    | 91.4 ms                                                         | 86.9 ms: 1.05x faster                                                          |
| regex_effbot               | 2.04 ms                                                         | 1.94 ms: 1.05x faster                                                          |
| xml_etree_process          | 53.2 ms                                                         | 51.0 ms: 1.04x faster                                                          |
| sympy_expand               | 398 ms                                                          | 381 ms: 1.04x faster                                                           |
| regex_dna                  | 127 ms                                                          | 122 ms: 1.04x faster                                                           |
| richards_super             | 46.5 ms                                                         | 44.8 ms: 1.04x faster                                                          |
| asyncio_tcp_ssl            | 17.7 sec                                                        | 17.0 sec: 1.04x faster                                                         |
| bench_mp_pool              | 75.4 ms                                                         | 72.8 ms: 1.04x faster                                                          |
| async_generators           | 313 ms                                                          | 307 ms: 1.02x faster                                                           |
| pidigits                   | 199 ms                                                          | 202 ms: 1.01x slower                                                           |
| json                       | 4.15 ms                                                         | 4.27 ms: 1.03x slower                                                          |
| python_startup_no_site     | 19.1 ms                                                         | 19.7 ms: 1.04x slower                                                          |
| json_dumps                 | 7.40 ms                                                         | 7.74 ms: 1.05x slower                                                          |
| python_startup             | 22.4 ms                                                         | 24.1 ms: 1.08x slower                                                          |
| regex_v8                   | 15.0 ms                                                         | 16.2 ms: 1.08x slower                                                          |
| coverage                   | 48.4 ms                                                         | 54.0 ms: 1.11x slower                                                          |
| asyncio_tcp                | 662 ms                                                          | 751 ms: 1.13x slower                                                           |
| create_gc_cycles           | 652 us                                                          | 751 us: 1.15x slower                                                           |
| typing_runtime_protocols   | 126 us                                                          | 148 us: 1.17x slower                                                           |
| telco                      | 5.51 ms                                                         | 7.08 ms: 1.28x slower                                                          |
| sqlglot_normalize          | 100 ms                                                          | 223 ms: 2.23x slower                                                           |
| Geometric mean             | (ref)                                                           | 1.13x faster                                                                   |

Benchmark hidden because not significant (3): gc_traversal, tornado_http, json_loads
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240829-3.14.0a0-15b187e/bm-20240829-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-15b187e.json: genshi_text, genshi_xml, html5lib, pylint, thrift

- Geometric mean (including insignificant results): 1.133x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.12x
- 95% likely to have a speedup of 1.12x
- 99% likely to have a speedup of 1.11x

# Memory
- memory change: unknown