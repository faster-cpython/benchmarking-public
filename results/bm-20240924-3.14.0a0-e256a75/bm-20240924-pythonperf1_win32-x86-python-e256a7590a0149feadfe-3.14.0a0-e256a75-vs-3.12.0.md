# Results vs. 3.12.0

- fork: python
- ref: e256a7590a0149feadfe
- machine: windows-x86
- commit hash: e256a75
- commit date: 2024-09-24
- overall geometric mean: 1.13x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.09x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240924-pythonperf1_win32-x86-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 249 ms: 1.12x faster                                                           |
| docutils       | 1.98 sec                                                        | 1.87 sec: 1.06x faster                                                         |
| tornado_http   | 105 ms                                                          | 94.9 ms: 1.11x faster                                                          |
| Geometric mean | (ref)                                                           | 1.10x faster                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240924-pythonperf1_win32-x86-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 350 ms                                                          | 253 ms: 1.39x faster                                                           |
| async_tree_none_tg         | 278 ms                                                          | 201 ms: 1.38x faster                                                           |
| async_tree_none            | 298 ms                                                          | 218 ms: 1.36x faster                                                           |
| async_tree_memoization     | 364 ms                                                          | 273 ms: 1.33x faster                                                           |
| async_tree_io_tg           | 677 ms                                                          | 518 ms: 1.31x faster                                                           |
| async_tree_io              | 693 ms                                                          | 534 ms: 1.30x faster                                                           |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 464 ms: 1.21x faster                                                           |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 455 ms: 1.20x faster                                                           |
| Geometric mean             | (ref)                                                           | 1.31x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240924-pythonperf1_win32-x86-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 93.0 ms: 1.37x faster                                                          |
| float          | 76.7 ms                                                         | 62.8 ms: 1.22x faster                                                          |
| pidigits       | 199 ms                                                          | 197 ms: 1.01x faster                                                           |
| Geometric mean | (ref)                                                           | 1.19x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240924-pythonperf1_win32-x86-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 109 ms: 1.18x faster                                                           |
| regex_effbot   | 2.04 ms                                                         | 1.90 ms: 1.07x faster                                                          |
| regex_dna      | 127 ms                                                          | 121 ms: 1.05x faster                                                           |
| regex_v8       | 15.0 ms                                                         | 16.2 ms: 1.08x slower                                                          |
| Geometric mean | (ref)                                                           | 1.06x faster                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240924-pythonperf1_win32-x86-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| tomli_loads          | 2.20 sec                                                        | 1.85 sec: 1.19x faster                                                         |
| unpickle_pure_python | 210 us                                                          | 180 us: 1.16x faster                                                           |
| xml_etree_iterparse  | 77.6 ms                                                         | 67.5 ms: 1.15x faster                                                          |
| pickle_pure_python   | 286 us                                                          | 262 us: 1.09x faster                                                           |
| xml_etree_process    | 53.2 ms                                                         | 49.4 ms: 1.08x faster                                                          |
| xml_etree_generate   | 72.1 ms                                                         | 67.5 ms: 1.07x faster                                                          |
| xml_etree_parse      | 113 ms                                                          | 107 ms: 1.05x faster                                                           |
| unpickle_list        | 2.95 us                                                         | 3.00 us: 1.02x slower                                                          |
| pickle               | 7.79 us                                                         | 7.94 us: 1.02x slower                                                          |
| json_loads           | 20.4 us                                                         | 21.0 us: 1.03x slower                                                          |
| pickle_dict          | 19.9 us                                                         | 20.6 us: 1.03x slower                                                          |
| json_dumps           | 7.40 ms                                                         | 7.68 ms: 1.04x slower                                                          |
| unpickle             | 9.71 us                                                         | 10.3 us: 1.06x slower                                                          |
| Geometric mean       | (ref)                                                           | 1.04x faster                                                                   |

Benchmark hidden because not significant (1): pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240924-pythonperf1_win32-x86-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 19.4 ms: 1.02x slower                                                          |
| python_startup         | 22.4 ms                                                         | 23.5 ms: 1.05x slower                                                          |
| Geometric mean         | (ref)                                                           | 1.04x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240924-pythonperf1_win32-x86-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 8.16 ms: 1.22x faster                                                          |
| django_template | 36.9 ms                                                         | 33.6 ms: 1.10x faster                                                          |
| Geometric mean  | (ref)                                                           | 1.16x faster                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240924-pythonperf1_win32-x86-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| deepcopy_memo              | 38.4 us                                                         | 22.6 us: 1.70x faster                                                          |
| generators                 | 38.5 ms                                                         | 26.0 ms: 1.48x faster                                                          |
| deepcopy                   | 360 us                                                          | 250 us: 1.44x faster                                                           |
| async_tree_memoization_tg  | 350 ms                                                          | 253 ms: 1.39x faster                                                           |
| async_tree_none_tg         | 278 ms                                                          | 201 ms: 1.38x faster                                                           |
| unpack_sequence            | 62.5 ns                                                         | 45.3 ns: 1.38x faster                                                          |
| spectral_norm              | 104 ms                                                          | 75.9 ms: 1.37x faster                                                          |
| nbody                      | 127 ms                                                          | 93.0 ms: 1.37x faster                                                          |
| async_tree_none            | 298 ms                                                          | 218 ms: 1.36x faster                                                           |
| comprehensions             | 19.2 us                                                         | 14.1 us: 1.36x faster                                                          |
| scimark_lu                 | 93.2 ms                                                         | 68.7 ms: 1.36x faster                                                          |
| logging_silent             | 101 ns                                                          | 74.6 ns: 1.35x faster                                                          |
| deltablue                  | 3.58 ms                                                         | 2.67 ms: 1.34x faster                                                          |
| async_tree_memoization     | 364 ms                                                          | 273 ms: 1.33x faster                                                           |
| raytrace                   | 308 ms                                                          | 233 ms: 1.32x faster                                                           |
| hexiom                     | 6.82 ms                                                         | 5.17 ms: 1.32x faster                                                          |
| async_tree_io_tg           | 677 ms                                                          | 518 ms: 1.31x faster                                                           |
| async_tree_io              | 693 ms                                                          | 534 ms: 1.30x faster                                                           |
| deepcopy_reduce            | 3.23 us                                                         | 2.50 us: 1.29x faster                                                          |
| go                         | 137 ms                                                          | 107 ms: 1.28x faster                                                           |
| chaos                      | 69.4 ms                                                         | 54.3 ms: 1.28x faster                                                          |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 3.06 ms: 1.26x faster                                                          |
| scimark_sor                | 130 ms                                                          | 105 ms: 1.24x faster                                                           |
| logging_simple             | 9.75 us                                                         | 7.93 us: 1.23x faster                                                          |
| float                      | 76.7 ms                                                         | 62.8 ms: 1.22x faster                                                          |
| mako                       | 9.96 ms                                                         | 8.16 ms: 1.22x faster                                                          |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 464 ms: 1.21x faster                                                           |
| nqueens                    | 93.7 ms                                                         | 77.3 ms: 1.21x faster                                                          |
| crypto_pyaes               | 69.2 ms                                                         | 57.2 ms: 1.21x faster                                                          |
| logging_format             | 10.4 us                                                         | 8.66 us: 1.20x faster                                                          |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 455 ms: 1.20x faster                                                           |
| tomli_loads                | 2.20 sec                                                        | 1.85 sec: 1.19x faster                                                         |
| regex_compile              | 129 ms                                                          | 109 ms: 1.18x faster                                                           |
| pyflate                    | 424 ms                                                          | 362 ms: 1.17x faster                                                           |
| scimark_monte_carlo        | 66.4 ms                                                         | 56.9 ms: 1.17x faster                                                          |
| unpickle_pure_python       | 210 us                                                          | 180 us: 1.16x faster                                                           |
| coroutines                 | 20.9 ms                                                         | 18.0 ms: 1.16x faster                                                          |
| mdp                        | 1.91 sec                                                        | 1.66 sec: 1.15x faster                                                         |
| xml_etree_iterparse        | 77.6 ms                                                         | 67.5 ms: 1.15x faster                                                          |
| sympy_integrate            | 17.5 ms                                                         | 15.3 ms: 1.15x faster                                                          |
| sympy_sum                  | 123 ms                                                          | 107 ms: 1.14x faster                                                           |
| dulwich_log                | 58.5 ms                                                         | 51.2 ms: 1.14x faster                                                          |
| sqlglot_parse              | 1.25 ms                                                         | 1.10 ms: 1.14x faster                                                          |
| sqlglot_transpile          | 1.53 ms                                                         | 1.35 ms: 1.14x faster                                                          |
| scimark_fft                | 271 ms                                                          | 239 ms: 1.13x faster                                                           |
| 2to3                       | 280 ms                                                          | 249 ms: 1.12x faster                                                           |
| pycparser                  | 978 ms                                                          | 877 ms: 1.11x faster                                                           |
| sympy_str                  | 240 ms                                                          | 216 ms: 1.11x faster                                                           |
| tornado_http               | 105 ms                                                          | 94.9 ms: 1.11x faster                                                          |
| bench_thread_pool          | 1.10 ms                                                         | 998 us: 1.10x faster                                                           |
| django_template            | 36.9 ms                                                         | 33.6 ms: 1.10x faster                                                          |
| pathlib                    | 91.4 ms                                                         | 83.5 ms: 1.09x faster                                                          |
| pickle_pure_python         | 286 us                                                          | 262 us: 1.09x faster                                                           |
| sqlglot_optimize           | 48.5 ms                                                         | 44.6 ms: 1.09x faster                                                          |
| bench_mp_pool              | 75.4 ms                                                         | 69.9 ms: 1.08x faster                                                          |
| xml_etree_process          | 53.2 ms                                                         | 49.4 ms: 1.08x faster                                                          |
| regex_effbot               | 2.04 ms                                                         | 1.90 ms: 1.07x faster                                                          |
| pprint_pformat             | 1.50 sec                                                        | 1.40 sec: 1.07x faster                                                         |
| xml_etree_generate         | 72.1 ms                                                         | 67.5 ms: 1.07x faster                                                          |
| meteor_contest             | 86.9 ms                                                         | 81.4 ms: 1.07x faster                                                          |
| docutils                   | 1.98 sec                                                        | 1.87 sec: 1.06x faster                                                         |
| xml_etree_parse            | 113 ms                                                          | 107 ms: 1.05x faster                                                           |
| fannkuch                   | 354 ms                                                          | 336 ms: 1.05x faster                                                           |
| pprint_safe_repr           | 721 ms                                                          | 684 ms: 1.05x faster                                                           |
| regex_dna                  | 127 ms                                                          | 121 ms: 1.05x faster                                                           |
| richards                   | 41.3 ms                                                         | 39.4 ms: 1.05x faster                                                          |
| richards_super             | 46.5 ms                                                         | 44.3 ms: 1.05x faster                                                          |
| sqlite_synth               | 2.07 us                                                         | 1.98 us: 1.05x faster                                                          |
| sympy_expand               | 398 ms                                                          | 381 ms: 1.04x faster                                                           |
| async_generators           | 313 ms                                                          | 301 ms: 1.04x faster                                                           |
| asyncio_tcp_ssl            | 17.7 sec                                                        | 17.0 sec: 1.04x faster                                                         |
| gc_traversal               | 1.44 ms                                                         | 1.42 ms: 1.02x faster                                                          |
| pidigits                   | 199 ms                                                          | 197 ms: 1.01x faster                                                           |
| unpickle_list              | 2.95 us                                                         | 3.00 us: 1.02x slower                                                          |
| pickle                     | 7.79 us                                                         | 7.94 us: 1.02x slower                                                          |
| python_startup_no_site     | 19.1 ms                                                         | 19.4 ms: 1.02x slower                                                          |
| json_loads                 | 20.4 us                                                         | 21.0 us: 1.03x slower                                                          |
| pickle_dict                | 19.9 us                                                         | 20.6 us: 1.03x slower                                                          |
| json_dumps                 | 7.40 ms                                                         | 7.68 ms: 1.04x slower                                                          |
| json                       | 4.15 ms                                                         | 4.32 ms: 1.04x slower                                                          |
| python_startup             | 22.4 ms                                                         | 23.5 ms: 1.05x slower                                                          |
| unpickle                   | 9.71 us                                                         | 10.3 us: 1.06x slower                                                          |
| regex_v8                   | 15.0 ms                                                         | 16.2 ms: 1.08x slower                                                          |
| coverage                   | 48.4 ms                                                         | 53.2 ms: 1.10x slower                                                          |
| create_gc_cycles           | 652 us                                                          | 727 us: 1.11x slower                                                           |
| typing_runtime_protocols   | 126 us                                                          | 143 us: 1.13x slower                                                           |
| telco                      | 5.51 ms                                                         | 6.61 ms: 1.20x slower                                                          |
| sqlglot_normalize          | 100 ms                                                          | 233 ms: 2.32x slower                                                           |
| Geometric mean             | (ref)                                                           | 1.13x faster                                                                   |

Benchmark hidden because not significant (2): pickle_list, asyncio_tcp
Ignored benchmarks (6) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20240924-3.14.0a0-e256a75/bm-20240924-pythonperf1_win32-x86-python-e256a7590a0149feadfe-3.14.0a0-e256a75.json: genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.11x
- 95% likely to have a speedup of 1.10x
- 99% likely to have a speedup of 1.09x

# Memory
- memory change: unknown