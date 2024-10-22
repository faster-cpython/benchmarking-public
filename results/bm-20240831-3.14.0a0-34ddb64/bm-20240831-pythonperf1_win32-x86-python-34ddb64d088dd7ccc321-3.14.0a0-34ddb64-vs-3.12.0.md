# Results vs. 3.12.0

- fork: python
- ref: 34ddb64d088dd7ccc321
- machine: windows-x86
- commit hash: 34ddb64
- commit date: 2024-08-31
- overall geometric mean: 1.13x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.11x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240831-pythonperf1_win32-x86-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 250 ms: 1.12x faster                                                           |
| docutils       | 1.98 sec                                                        | 1.85 sec: 1.07x faster                                                         |
| Geometric mean | (ref)                                                           | 1.06x faster                                                                   |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240831-pythonperf1_win32-x86-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 350 ms                                                          | 253 ms: 1.39x faster                                                           |
| async_tree_none_tg         | 278 ms                                                          | 201 ms: 1.38x faster                                                           |
| async_tree_none            | 298 ms                                                          | 221 ms: 1.34x faster                                                           |
| async_tree_memoization     | 364 ms                                                          | 278 ms: 1.31x faster                                                           |
| async_tree_io_tg           | 677 ms                                                          | 518 ms: 1.31x faster                                                           |
| async_tree_io              | 693 ms                                                          | 539 ms: 1.29x faster                                                           |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 471 ms: 1.20x faster                                                           |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 464 ms: 1.18x faster                                                           |
| Geometric mean             | (ref)                                                           | 1.30x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240831-pythonperf1_win32-x86-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 96.5 ms: 1.32x faster                                                          |
| float          | 76.7 ms                                                         | 60.6 ms: 1.27x faster                                                          |
| pidigits       | 199 ms                                                          | 200 ms: 1.00x slower                                                           |
| Geometric mean | (ref)                                                           | 1.18x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240831-pythonperf1_win32-x86-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 107 ms: 1.21x faster                                                           |
| regex_v8       | 15.0 ms                                                         | 16.2 ms: 1.08x slower                                                          |
| Geometric mean | (ref)                                                           | 1.03x faster                                                                   |

Benchmark hidden because not significant (2): regex_effbot, regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240831-pythonperf1_win32-x86-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| unpickle_pure_python | 210 us                                                          | 176 us: 1.19x faster                                                           |
| tomli_loads          | 2.20 sec                                                        | 1.90 sec: 1.15x faster                                                         |
| xml_etree_iterparse  | 77.6 ms                                                         | 68.5 ms: 1.13x faster                                                          |
| pickle_pure_python   | 286 us                                                          | 254 us: 1.13x faster                                                           |
| xml_etree_process    | 53.2 ms                                                         | 50.8 ms: 1.05x faster                                                          |
| xml_etree_generate   | 72.1 ms                                                         | 69.1 ms: 1.04x faster                                                          |
| xml_etree_parse      | 113 ms                                                          | 109 ms: 1.04x faster                                                           |
| json_dumps           | 7.40 ms                                                         | 7.21 ms: 1.03x faster                                                          |
| Geometric mean       | (ref)                                                           | 1.08x faster                                                                   |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240831-pythonperf1_win32-x86-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 19.9 ms: 1.04x slower                                                          |
| python_startup         | 22.4 ms                                                         | 24.1 ms: 1.08x slower                                                          |
| Geometric mean         | (ref)                                                           | 1.06x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240831-pythonperf1_win32-x86-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 8.10 ms: 1.23x faster                                                          |
| django_template | 36.9 ms                                                         | 33.3 ms: 1.11x faster                                                          |
| Geometric mean  | (ref)                                                           | 1.17x faster                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240831-pythonperf1_win32-x86-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| deepcopy_memo              | 38.4 us                                                         | 21.6 us: 1.77x faster                                                          |
| deepcopy                   | 360 us                                                          | 243 us: 1.48x faster                                                           |
| generators                 | 38.5 ms                                                         | 26.7 ms: 1.44x faster                                                          |
| comprehensions             | 19.2 us                                                         | 13.6 us: 1.41x faster                                                          |
| logging_silent             | 101 ns                                                          | 72.8 ns: 1.39x faster                                                          |
| async_tree_memoization_tg  | 350 ms                                                          | 253 ms: 1.39x faster                                                           |
| async_tree_none_tg         | 278 ms                                                          | 201 ms: 1.38x faster                                                           |
| spectral_norm              | 104 ms                                                          | 75.5 ms: 1.38x faster                                                          |
| raytrace                   | 308 ms                                                          | 227 ms: 1.36x faster                                                           |
| async_tree_none            | 298 ms                                                          | 221 ms: 1.34x faster                                                           |
| go                         | 137 ms                                                          | 103 ms: 1.33x faster                                                           |
| scimark_lu                 | 93.2 ms                                                         | 70.3 ms: 1.33x faster                                                          |
| deltablue                  | 3.58 ms                                                         | 2.70 ms: 1.32x faster                                                          |
| scimark_sor                | 130 ms                                                          | 98.2 ms: 1.32x faster                                                          |
| nbody                      | 127 ms                                                          | 96.5 ms: 1.32x faster                                                          |
| async_tree_memoization     | 364 ms                                                          | 278 ms: 1.31x faster                                                           |
| async_tree_io_tg           | 677 ms                                                          | 518 ms: 1.31x faster                                                           |
| deepcopy_reduce            | 3.23 us                                                         | 2.50 us: 1.29x faster                                                          |
| hexiom                     | 6.82 ms                                                         | 5.29 ms: 1.29x faster                                                          |
| async_tree_io              | 693 ms                                                          | 539 ms: 1.29x faster                                                           |
| chaos                      | 69.4 ms                                                         | 54.6 ms: 1.27x faster                                                          |
| float                      | 76.7 ms                                                         | 60.6 ms: 1.27x faster                                                          |
| mako                       | 9.96 ms                                                         | 8.10 ms: 1.23x faster                                                          |
| logging_simple             | 9.75 us                                                         | 7.94 us: 1.23x faster                                                          |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 3.17 ms: 1.22x faster                                                          |
| logging_format             | 10.4 us                                                         | 8.58 us: 1.21x faster                                                          |
| regex_compile              | 129 ms                                                          | 107 ms: 1.21x faster                                                           |
| coroutines                 | 20.9 ms                                                         | 17.4 ms: 1.20x faster                                                          |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 471 ms: 1.20x faster                                                           |
| crypto_pyaes               | 69.2 ms                                                         | 57.8 ms: 1.20x faster                                                          |
| unpickle_pure_python       | 210 us                                                          | 176 us: 1.19x faster                                                           |
| scimark_monte_carlo        | 66.4 ms                                                         | 55.8 ms: 1.19x faster                                                          |
| nqueens                    | 93.7 ms                                                         | 79.0 ms: 1.19x faster                                                          |
| pyflate                    | 424 ms                                                          | 358 ms: 1.18x faster                                                           |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 464 ms: 1.18x faster                                                           |
| scimark_fft                | 271 ms                                                          | 231 ms: 1.17x faster                                                           |
| dulwich_log                | 58.5 ms                                                         | 50.3 ms: 1.16x faster                                                          |
| sqlglot_parse              | 1.25 ms                                                         | 1.08 ms: 1.16x faster                                                          |
| sqlglot_transpile          | 1.53 ms                                                         | 1.32 ms: 1.16x faster                                                          |
| tomli_loads                | 2.20 sec                                                        | 1.90 sec: 1.15x faster                                                         |
| sympy_sum                  | 123 ms                                                          | 107 ms: 1.15x faster                                                           |
| sympy_integrate            | 17.5 ms                                                         | 15.3 ms: 1.15x faster                                                          |
| xml_etree_iterparse        | 77.6 ms                                                         | 68.5 ms: 1.13x faster                                                          |
| pycparser                  | 978 ms                                                          | 864 ms: 1.13x faster                                                           |
| pprint_pformat             | 1.50 sec                                                        | 1.33 sec: 1.13x faster                                                         |
| pickle_pure_python         | 286 us                                                          | 254 us: 1.13x faster                                                           |
| 2to3                       | 280 ms                                                          | 250 ms: 1.12x faster                                                           |
| sympy_str                  | 240 ms                                                          | 214 ms: 1.12x faster                                                           |
| pprint_safe_repr           | 721 ms                                                          | 645 ms: 1.12x faster                                                           |
| mdp                        | 1.91 sec                                                        | 1.72 sec: 1.11x faster                                                         |
| django_template            | 36.9 ms                                                         | 33.3 ms: 1.11x faster                                                          |
| sqlglot_optimize           | 48.5 ms                                                         | 44.2 ms: 1.10x faster                                                          |
| docutils                   | 1.98 sec                                                        | 1.85 sec: 1.07x faster                                                         |
| meteor_contest             | 86.9 ms                                                         | 81.3 ms: 1.07x faster                                                          |
| fannkuch                   | 354 ms                                                          | 332 ms: 1.07x faster                                                           |
| sympy_expand               | 398 ms                                                          | 375 ms: 1.06x faster                                                           |
| pathlib                    | 91.4 ms                                                         | 87.2 ms: 1.05x faster                                                          |
| xml_etree_process          | 53.2 ms                                                         | 50.8 ms: 1.05x faster                                                          |
| richards_super             | 46.5 ms                                                         | 44.3 ms: 1.05x faster                                                          |
| async_generators           | 313 ms                                                          | 300 ms: 1.05x faster                                                           |
| xml_etree_generate         | 72.1 ms                                                         | 69.1 ms: 1.04x faster                                                          |
| xml_etree_parse            | 113 ms                                                          | 109 ms: 1.04x faster                                                           |
| richards                   | 41.3 ms                                                         | 39.8 ms: 1.04x faster                                                          |
| asyncio_tcp_ssl            | 17.7 sec                                                        | 17.2 sec: 1.03x faster                                                         |
| bench_mp_pool              | 75.4 ms                                                         | 73.5 ms: 1.03x faster                                                          |
| json_dumps                 | 7.40 ms                                                         | 7.21 ms: 1.03x faster                                                          |
| gc_traversal               | 1.44 ms                                                         | 1.42 ms: 1.01x faster                                                          |
| pidigits                   | 199 ms                                                          | 200 ms: 1.00x slower                                                           |
| json                       | 4.15 ms                                                         | 4.18 ms: 1.01x slower                                                          |
| python_startup_no_site     | 19.1 ms                                                         | 19.9 ms: 1.04x slower                                                          |
| python_startup             | 22.4 ms                                                         | 24.1 ms: 1.08x slower                                                          |
| regex_v8                   | 15.0 ms                                                         | 16.2 ms: 1.08x slower                                                          |
| coverage                   | 48.4 ms                                                         | 52.5 ms: 1.08x slower                                                          |
| asyncio_tcp                | 662 ms                                                          | 731 ms: 1.10x slower                                                           |
| create_gc_cycles           | 652 us                                                          | 741 us: 1.14x slower                                                           |
| typing_runtime_protocols   | 126 us                                                          | 144 us: 1.14x slower                                                           |
| telco                      | 5.51 ms                                                         | 6.78 ms: 1.23x slower                                                          |
| sqlglot_normalize          | 100 ms                                                          | 229 ms: 2.29x slower                                                           |
| Geometric mean             | (ref)                                                           | 1.13x faster                                                                   |

Benchmark hidden because not significant (5): regex_effbot, bench_thread_pool, regex_dna, tornado_http, json_loads
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240831-3.14.0a0-34ddb64/bm-20240831-pythonperf1_win32-x86-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64.json: genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.12x
- 95% likely to have a speedup of 1.11x
- 99% likely to have a speedup of 1.11x

# Memory
- memory change: unknown