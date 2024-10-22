# Results vs. 3.12.0

- fork: python
- ref: c8db0e817e7e0db50153
- machine: windows-x86
- commit hash: c8db0e8
- commit date: 2024-10-03
- overall geometric mean: 1.11x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.08x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241003-pythonperf1_win32-x86-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 250 ms: 1.12x faster                                                           |
| docutils       | 1.98 sec                                                        | 1.87 sec: 1.06x faster                                                         |
| Geometric mean | (ref)                                                           | 1.06x faster                                                                   |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241003-pythonperf1_win32-x86-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_none_tg         | 278 ms                                                          | 202 ms: 1.37x faster                                                           |
| async_tree_memoization_tg  | 350 ms                                                          | 257 ms: 1.37x faster                                                           |
| async_tree_none            | 298 ms                                                          | 220 ms: 1.35x faster                                                           |
| async_tree_memoization     | 364 ms                                                          | 276 ms: 1.32x faster                                                           |
| async_tree_io_tg           | 677 ms                                                          | 527 ms: 1.29x faster                                                           |
| async_tree_io              | 693 ms                                                          | 545 ms: 1.27x faster                                                           |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 475 ms: 1.15x faster                                                           |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 491 ms: 1.15x faster                                                           |
| Geometric mean             | (ref)                                                           | 1.28x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241003-pythonperf1_win32-x86-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 91.6 ms: 1.39x faster                                                          |
| float          | 76.7 ms                                                         | 61.7 ms: 1.24x faster                                                          |
| Geometric mean | (ref)                                                           | 1.20x faster                                                                   |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241003-pythonperf1_win32-x86-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 110 ms: 1.17x faster                                                           |
| regex_effbot   | 2.04 ms                                                         | 1.92 ms: 1.06x faster                                                          |
| regex_dna      | 127 ms                                                          | 120 ms: 1.05x faster                                                           |
| regex_v8       | 15.0 ms                                                         | 16.2 ms: 1.08x slower                                                          |
| Geometric mean | (ref)                                                           | 1.05x faster                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241003-pythonperf1_win32-x86-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| unpickle_pure_python | 210 us                                                          | 183 us: 1.15x faster                                                           |
| tomli_loads          | 2.20 sec                                                        | 1.92 sec: 1.15x faster                                                         |
| xml_etree_iterparse  | 77.6 ms                                                         | 68.0 ms: 1.14x faster                                                          |
| pickle_pure_python   | 286 us                                                          | 268 us: 1.07x faster                                                           |
| xml_etree_parse      | 113 ms                                                          | 108 ms: 1.05x faster                                                           |
| xml_etree_process    | 53.2 ms                                                         | 50.7 ms: 1.05x faster                                                          |
| xml_etree_generate   | 72.1 ms                                                         | 69.1 ms: 1.04x faster                                                          |
| pickle_list          | 3.37 us                                                         | 3.41 us: 1.01x slower                                                          |
| json_dumps           | 7.40 ms                                                         | 7.54 ms: 1.02x slower                                                          |
| unpickle_list        | 2.95 us                                                         | 3.00 us: 1.02x slower                                                          |
| pickle_dict          | 19.9 us                                                         | 20.7 us: 1.04x slower                                                          |
| json_loads           | 20.4 us                                                         | 21.3 us: 1.04x slower                                                          |
| pickle               | 7.79 us                                                         | 8.18 us: 1.05x slower                                                          |
| unpickle             | 9.71 us                                                         | 10.4 us: 1.08x slower                                                          |
| Geometric mean       | (ref)                                                           | 1.03x faster                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241003-pythonperf1_win32-x86-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 19.7 ms: 1.03x slower                                                          |
| python_startup         | 22.4 ms                                                         | 24.1 ms: 1.08x slower                                                          |
| Geometric mean         | (ref)                                                           | 1.05x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241003-pythonperf1_win32-x86-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 8.12 ms: 1.23x faster                                                          |
| django_template | 36.9 ms                                                         | 34.3 ms: 1.07x faster                                                          |
| Geometric mean  | (ref)                                                           | 1.15x faster                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241003-pythonperf1_win32-x86-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| deepcopy_memo              | 38.4 us                                                         | 22.9 us: 1.68x faster                                                          |
| deepcopy                   | 360 us                                                          | 247 us: 1.46x faster                                                           |
| generators                 | 38.5 ms                                                         | 26.7 ms: 1.44x faster                                                          |
| nbody                      | 127 ms                                                          | 91.6 ms: 1.39x faster                                                          |
| async_tree_none_tg         | 278 ms                                                          | 202 ms: 1.37x faster                                                           |
| comprehensions             | 19.2 us                                                         | 14.0 us: 1.37x faster                                                          |
| async_tree_memoization_tg  | 350 ms                                                          | 257 ms: 1.37x faster                                                           |
| async_tree_none            | 298 ms                                                          | 220 ms: 1.35x faster                                                           |
| logging_silent             | 101 ns                                                          | 74.7 ns: 1.35x faster                                                          |
| scimark_lu                 | 93.2 ms                                                         | 69.2 ms: 1.35x faster                                                          |
| unpack_sequence            | 62.5 ns                                                         | 46.7 ns: 1.34x faster                                                          |
| spectral_norm              | 104 ms                                                          | 78.5 ms: 1.32x faster                                                          |
| async_tree_memoization     | 364 ms                                                          | 276 ms: 1.32x faster                                                           |
| scimark_sor                | 130 ms                                                          | 99.0 ms: 1.31x faster                                                          |
| hexiom                     | 6.82 ms                                                         | 5.23 ms: 1.30x faster                                                          |
| async_tree_io_tg           | 677 ms                                                          | 527 ms: 1.29x faster                                                           |
| deltablue                  | 3.58 ms                                                         | 2.82 ms: 1.27x faster                                                          |
| async_tree_io              | 693 ms                                                          | 545 ms: 1.27x faster                                                           |
| go                         | 137 ms                                                          | 110 ms: 1.25x faster                                                           |
| deepcopy_reduce            | 3.23 us                                                         | 2.58 us: 1.25x faster                                                          |
| nqueens                    | 93.7 ms                                                         | 75.1 ms: 1.25x faster                                                          |
| float                      | 76.7 ms                                                         | 61.7 ms: 1.24x faster                                                          |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 3.11 ms: 1.24x faster                                                          |
| chaos                      | 69.4 ms                                                         | 56.2 ms: 1.23x faster                                                          |
| mako                       | 9.96 ms                                                         | 8.12 ms: 1.23x faster                                                          |
| scimark_monte_carlo        | 66.4 ms                                                         | 55.3 ms: 1.20x faster                                                          |
| crypto_pyaes               | 69.2 ms                                                         | 57.8 ms: 1.20x faster                                                          |
| logging_simple             | 9.75 us                                                         | 8.18 us: 1.19x faster                                                          |
| raytrace                   | 308 ms                                                          | 260 ms: 1.18x faster                                                           |
| regex_compile              | 129 ms                                                          | 110 ms: 1.17x faster                                                           |
| logging_format             | 10.4 us                                                         | 8.92 us: 1.17x faster                                                          |
| sqlglot_parse              | 1.25 ms                                                         | 1.07 ms: 1.16x faster                                                          |
| scimark_fft                | 271 ms                                                          | 233 ms: 1.16x faster                                                           |
| sqlglot_transpile          | 1.53 ms                                                         | 1.32 ms: 1.16x faster                                                          |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 475 ms: 1.15x faster                                                           |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 491 ms: 1.15x faster                                                           |
| pyflate                    | 424 ms                                                          | 370 ms: 1.15x faster                                                           |
| unpickle_pure_python       | 210 us                                                          | 183 us: 1.15x faster                                                           |
| tomli_loads                | 2.20 sec                                                        | 1.92 sec: 1.15x faster                                                         |
| xml_etree_iterparse        | 77.6 ms                                                         | 68.0 ms: 1.14x faster                                                          |
| sympy_sum                  | 123 ms                                                          | 108 ms: 1.14x faster                                                           |
| pycparser                  | 978 ms                                                          | 861 ms: 1.14x faster                                                           |
| fannkuch                   | 354 ms                                                          | 313 ms: 1.13x faster                                                           |
| coroutines                 | 20.9 ms                                                         | 18.5 ms: 1.13x faster                                                          |
| 2to3                       | 280 ms                                                          | 250 ms: 1.12x faster                                                           |
| sympy_integrate            | 17.5 ms                                                         | 15.7 ms: 1.12x faster                                                          |
| dulwich_log                | 58.5 ms                                                         | 52.5 ms: 1.11x faster                                                          |
| sympy_str                  | 240 ms                                                          | 218 ms: 1.10x faster                                                           |
| meteor_contest             | 86.9 ms                                                         | 79.8 ms: 1.09x faster                                                          |
| bench_thread_pool          | 1.10 ms                                                         | 1.01 ms: 1.09x faster                                                          |
| mdp                        | 1.91 sec                                                        | 1.77 sec: 1.08x faster                                                         |
| django_template            | 36.9 ms                                                         | 34.3 ms: 1.07x faster                                                          |
| pprint_pformat             | 1.50 sec                                                        | 1.40 sec: 1.07x faster                                                         |
| pickle_pure_python         | 286 us                                                          | 268 us: 1.07x faster                                                           |
| sqlglot_optimize           | 48.5 ms                                                         | 45.5 ms: 1.07x faster                                                          |
| docutils                   | 1.98 sec                                                        | 1.87 sec: 1.06x faster                                                         |
| regex_effbot               | 2.04 ms                                                         | 1.92 ms: 1.06x faster                                                          |
| pprint_safe_repr           | 721 ms                                                          | 680 ms: 1.06x faster                                                           |
| pathlib                    | 91.4 ms                                                         | 86.5 ms: 1.06x faster                                                          |
| regex_dna                  | 127 ms                                                          | 120 ms: 1.05x faster                                                           |
| xml_etree_parse            | 113 ms                                                          | 108 ms: 1.05x faster                                                           |
| xml_etree_process          | 53.2 ms                                                         | 50.7 ms: 1.05x faster                                                          |
| sqlite_synth               | 2.07 us                                                         | 1.98 us: 1.05x faster                                                          |
| xml_etree_generate         | 72.1 ms                                                         | 69.1 ms: 1.04x faster                                                          |
| async_generators           | 313 ms                                                          | 302 ms: 1.04x faster                                                           |
| bench_mp_pool              | 75.4 ms                                                         | 72.9 ms: 1.03x faster                                                          |
| asyncio_tcp_ssl            | 17.7 sec                                                        | 17.1 sec: 1.03x faster                                                         |
| sympy_expand               | 398 ms                                                          | 385 ms: 1.03x faster                                                           |
| gc_traversal               | 1.44 ms                                                         | 1.43 ms: 1.01x faster                                                          |
| richards_super             | 46.5 ms                                                         | 46.2 ms: 1.01x faster                                                          |
| pickle_list                | 3.37 us                                                         | 3.41 us: 1.01x slower                                                          |
| json_dumps                 | 7.40 ms                                                         | 7.54 ms: 1.02x slower                                                          |
| unpickle_list              | 2.95 us                                                         | 3.00 us: 1.02x slower                                                          |
| json                       | 4.15 ms                                                         | 4.28 ms: 1.03x slower                                                          |
| python_startup_no_site     | 19.1 ms                                                         | 19.7 ms: 1.03x slower                                                          |
| pickle_dict                | 19.9 us                                                         | 20.7 us: 1.04x slower                                                          |
| json_loads                 | 20.4 us                                                         | 21.3 us: 1.04x slower                                                          |
| pickle                     | 7.79 us                                                         | 8.18 us: 1.05x slower                                                          |
| unpickle                   | 9.71 us                                                         | 10.4 us: 1.08x slower                                                          |
| python_startup             | 22.4 ms                                                         | 24.1 ms: 1.08x slower                                                          |
| regex_v8                   | 15.0 ms                                                         | 16.2 ms: 1.08x slower                                                          |
| coverage                   | 48.4 ms                                                         | 53.6 ms: 1.11x slower                                                          |
| create_gc_cycles           | 652 us                                                          | 732 us: 1.12x slower                                                           |
| typing_runtime_protocols   | 126 us                                                          | 148 us: 1.17x slower                                                           |
| telco                      | 5.51 ms                                                         | 6.48 ms: 1.18x slower                                                          |
| sqlglot_normalize          | 100 ms                                                          | 236 ms: 2.36x slower                                                           |
| Geometric mean             | (ref)                                                           | 1.11x faster                                                                   |

Benchmark hidden because not significant (4): tornado_http, richards, pidigits, asyncio_tcp
Ignored benchmarks (6) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20241003-3.14.0a0-c8db0e8/bm-20241003-pythonperf1_win32-x86-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8.json: genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.11x
- 95% likely to have a speedup of 1.10x
- 99% likely to have a speedup of 1.08x

# Memory
- memory change: unknown