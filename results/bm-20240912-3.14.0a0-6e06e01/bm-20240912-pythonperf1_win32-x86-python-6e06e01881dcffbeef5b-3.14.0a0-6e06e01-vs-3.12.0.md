# Results vs. 3.12.0

- fork: python
- ref: 6e06e01881dcffbeef5b
- machine: windows-x86
- commit hash: 6e06e01
- commit date: 2024-09-12
- overall geometric mean: 1.13x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.09x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240912-pythonperf1_win32-x86-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 248 ms: 1.13x faster                                                           |
| docutils       | 1.98 sec                                                        | 1.87 sec: 1.06x faster                                                         |
| tornado_http   | 105 ms                                                          | 95.1 ms: 1.10x faster                                                          |
| Geometric mean | (ref)                                                           | 1.10x faster                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240912-pythonperf1_win32-x86-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 350 ms                                                          | 250 ms: 1.40x faster                                                           |
| async_tree_none_tg         | 278 ms                                                          | 198 ms: 1.40x faster                                                           |
| async_tree_none            | 298 ms                                                          | 217 ms: 1.37x faster                                                           |
| async_tree_memoization     | 364 ms                                                          | 271 ms: 1.34x faster                                                           |
| async_tree_io_tg           | 677 ms                                                          | 515 ms: 1.32x faster                                                           |
| async_tree_io              | 693 ms                                                          | 535 ms: 1.30x faster                                                           |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 466 ms: 1.21x faster                                                           |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 461 ms: 1.18x faster                                                           |
| Geometric mean             | (ref)                                                           | 1.31x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240912-pythonperf1_win32-x86-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 91.3 ms: 1.39x faster                                                          |
| float          | 76.7 ms                                                         | 62.2 ms: 1.23x faster                                                          |
| pidigits       | 199 ms                                                          | 197 ms: 1.01x faster                                                           |
| Geometric mean | (ref)                                                           | 1.20x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240912-pythonperf1_win32-x86-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 108 ms: 1.19x faster                                                           |
| regex_effbot   | 2.04 ms                                                         | 1.88 ms: 1.08x faster                                                          |
| regex_dna      | 127 ms                                                          | 118 ms: 1.08x faster                                                           |
| regex_v8       | 15.0 ms                                                         | 16.1 ms: 1.07x slower                                                          |
| Geometric mean | (ref)                                                           | 1.07x faster                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240912-pythonperf1_win32-x86-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| xml_etree_iterparse  | 77.6 ms                                                         | 66.8 ms: 1.16x faster                                                          |
| unpickle_pure_python | 210 us                                                          | 181 us: 1.16x faster                                                           |
| tomli_loads          | 2.20 sec                                                        | 1.93 sec: 1.14x faster                                                         |
| pickle_pure_python   | 286 us                                                          | 257 us: 1.11x faster                                                           |
| xml_etree_parse      | 113 ms                                                          | 107 ms: 1.06x faster                                                           |
| xml_etree_generate   | 72.1 ms                                                         | 68.3 ms: 1.06x faster                                                          |
| xml_etree_process    | 53.2 ms                                                         | 50.7 ms: 1.05x faster                                                          |
| pickle_dict          | 19.9 us                                                         | 20.3 us: 1.02x slower                                                          |
| json_loads           | 20.4 us                                                         | 20.8 us: 1.02x slower                                                          |
| json_dumps           | 7.40 ms                                                         | 7.69 ms: 1.04x slower                                                          |
| unpickle             | 9.71 us                                                         | 10.3 us: 1.06x slower                                                          |
| Geometric mean       | (ref)                                                           | 1.04x faster                                                                   |

Benchmark hidden because not significant (3): pickle, unpickle_list, pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240912-pythonperf1_win32-x86-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 19.8 ms: 1.04x slower                                                          |
| python_startup         | 22.4 ms                                                         | 23.8 ms: 1.07x slower                                                          |
| Geometric mean         | (ref)                                                           | 1.05x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240912-pythonperf1_win32-x86-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 7.99 ms: 1.25x faster                                                          |
| django_template | 36.9 ms                                                         | 33.7 ms: 1.09x faster                                                          |
| Geometric mean  | (ref)                                                           | 1.17x faster                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240912-pythonperf1_win32-x86-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| deepcopy_memo              | 38.4 us                                                         | 21.9 us: 1.75x faster                                                          |
| generators                 | 38.5 ms                                                         | 26.2 ms: 1.47x faster                                                          |
| deepcopy                   | 360 us                                                          | 250 us: 1.44x faster                                                           |
| async_tree_memoization_tg  | 350 ms                                                          | 250 ms: 1.40x faster                                                           |
| async_tree_none_tg         | 278 ms                                                          | 198 ms: 1.40x faster                                                           |
| comprehensions             | 19.2 us                                                         | 13.8 us: 1.39x faster                                                          |
| nbody                      | 127 ms                                                          | 91.3 ms: 1.39x faster                                                          |
| spectral_norm              | 104 ms                                                          | 75.2 ms: 1.38x faster                                                          |
| async_tree_none            | 298 ms                                                          | 217 ms: 1.37x faster                                                           |
| scimark_lu                 | 93.2 ms                                                         | 68.1 ms: 1.37x faster                                                          |
| logging_silent             | 101 ns                                                          | 74.5 ns: 1.36x faster                                                          |
| async_tree_memoization     | 364 ms                                                          | 271 ms: 1.34x faster                                                           |
| hexiom                     | 6.82 ms                                                         | 5.10 ms: 1.34x faster                                                          |
| deltablue                  | 3.58 ms                                                         | 2.68 ms: 1.34x faster                                                          |
| go                         | 137 ms                                                          | 103 ms: 1.33x faster                                                           |
| unpack_sequence            | 62.5 ns                                                         | 47.1 ns: 1.33x faster                                                          |
| scimark_sor                | 130 ms                                                          | 98.3 ms: 1.32x faster                                                          |
| async_tree_io_tg           | 677 ms                                                          | 515 ms: 1.32x faster                                                           |
| raytrace                   | 308 ms                                                          | 236 ms: 1.31x faster                                                           |
| chaos                      | 69.4 ms                                                         | 53.4 ms: 1.30x faster                                                          |
| async_tree_io              | 693 ms                                                          | 535 ms: 1.30x faster                                                           |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 3.07 ms: 1.26x faster                                                          |
| nqueens                    | 93.7 ms                                                         | 74.9 ms: 1.25x faster                                                          |
| mako                       | 9.96 ms                                                         | 7.99 ms: 1.25x faster                                                          |
| deepcopy_reduce            | 3.23 us                                                         | 2.60 us: 1.24x faster                                                          |
| float                      | 76.7 ms                                                         | 62.2 ms: 1.23x faster                                                          |
| logging_simple             | 9.75 us                                                         | 8.00 us: 1.22x faster                                                          |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 466 ms: 1.21x faster                                                           |
| crypto_pyaes               | 69.2 ms                                                         | 57.3 ms: 1.21x faster                                                          |
| pyflate                    | 424 ms                                                          | 352 ms: 1.20x faster                                                           |
| scimark_monte_carlo        | 66.4 ms                                                         | 55.4 ms: 1.20x faster                                                          |
| logging_format             | 10.4 us                                                         | 8.71 us: 1.20x faster                                                          |
| regex_compile              | 129 ms                                                          | 108 ms: 1.19x faster                                                           |
| sqlglot_parse              | 1.25 ms                                                         | 1.05 ms: 1.18x faster                                                          |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 461 ms: 1.18x faster                                                           |
| sqlglot_transpile          | 1.53 ms                                                         | 1.30 ms: 1.18x faster                                                          |
| dulwich_log                | 58.5 ms                                                         | 49.9 ms: 1.17x faster                                                          |
| coroutines                 | 20.9 ms                                                         | 18.0 ms: 1.16x faster                                                          |
| scimark_fft                | 271 ms                                                          | 233 ms: 1.16x faster                                                           |
| xml_etree_iterparse        | 77.6 ms                                                         | 66.8 ms: 1.16x faster                                                          |
| unpickle_pure_python       | 210 us                                                          | 181 us: 1.16x faster                                                           |
| sympy_sum                  | 123 ms                                                          | 106 ms: 1.16x faster                                                           |
| tomli_loads                | 2.20 sec                                                        | 1.93 sec: 1.14x faster                                                         |
| sympy_integrate            | 17.5 ms                                                         | 15.5 ms: 1.13x faster                                                          |
| 2to3                       | 280 ms                                                          | 248 ms: 1.13x faster                                                           |
| sqlglot_optimize           | 48.5 ms                                                         | 43.0 ms: 1.13x faster                                                          |
| fannkuch                   | 354 ms                                                          | 314 ms: 1.13x faster                                                           |
| mdp                        | 1.91 sec                                                        | 1.70 sec: 1.12x faster                                                         |
| pickle_pure_python         | 286 us                                                          | 257 us: 1.11x faster                                                           |
| sympy_str                  | 240 ms                                                          | 216 ms: 1.11x faster                                                           |
| pycparser                  | 978 ms                                                          | 884 ms: 1.11x faster                                                           |
| tornado_http               | 105 ms                                                          | 95.1 ms: 1.10x faster                                                          |
| pathlib                    | 91.4 ms                                                         | 83.3 ms: 1.10x faster                                                          |
| django_template            | 36.9 ms                                                         | 33.7 ms: 1.09x faster                                                          |
| richards                   | 41.3 ms                                                         | 37.9 ms: 1.09x faster                                                          |
| meteor_contest             | 86.9 ms                                                         | 79.8 ms: 1.09x faster                                                          |
| bench_thread_pool          | 1.10 ms                                                         | 1.02 ms: 1.09x faster                                                          |
| pprint_safe_repr           | 721 ms                                                          | 665 ms: 1.08x faster                                                           |
| regex_effbot               | 2.04 ms                                                         | 1.88 ms: 1.08x faster                                                          |
| pprint_pformat             | 1.50 sec                                                        | 1.39 sec: 1.08x faster                                                         |
| regex_dna                  | 127 ms                                                          | 118 ms: 1.08x faster                                                           |
| sqlite_synth               | 2.07 us                                                         | 1.93 us: 1.07x faster                                                          |
| richards_super             | 46.5 ms                                                         | 43.5 ms: 1.07x faster                                                          |
| docutils                   | 1.98 sec                                                        | 1.87 sec: 1.06x faster                                                         |
| xml_etree_parse            | 113 ms                                                          | 107 ms: 1.06x faster                                                           |
| xml_etree_generate         | 72.1 ms                                                         | 68.3 ms: 1.06x faster                                                          |
| bench_mp_pool              | 75.4 ms                                                         | 71.5 ms: 1.05x faster                                                          |
| xml_etree_process          | 53.2 ms                                                         | 50.7 ms: 1.05x faster                                                          |
| async_generators           | 313 ms                                                          | 300 ms: 1.04x faster                                                           |
| sympy_expand               | 398 ms                                                          | 383 ms: 1.04x faster                                                           |
| asyncio_tcp_ssl            | 17.7 sec                                                        | 17.1 sec: 1.03x faster                                                         |
| gc_traversal               | 1.44 ms                                                         | 1.41 ms: 1.02x faster                                                          |
| pidigits                   | 199 ms                                                          | 197 ms: 1.01x faster                                                           |
| pickle_dict                | 19.9 us                                                         | 20.3 us: 1.02x slower                                                          |
| json_loads                 | 20.4 us                                                         | 20.8 us: 1.02x slower                                                          |
| json                       | 4.15 ms                                                         | 4.28 ms: 1.03x slower                                                          |
| python_startup_no_site     | 19.1 ms                                                         | 19.8 ms: 1.04x slower                                                          |
| json_dumps                 | 7.40 ms                                                         | 7.69 ms: 1.04x slower                                                          |
| unpickle                   | 9.71 us                                                         | 10.3 us: 1.06x slower                                                          |
| python_startup             | 22.4 ms                                                         | 23.8 ms: 1.07x slower                                                          |
| regex_v8                   | 15.0 ms                                                         | 16.1 ms: 1.07x slower                                                          |
| typing_runtime_protocols   | 126 us                                                          | 137 us: 1.09x slower                                                           |
| coverage                   | 48.4 ms                                                         | 52.7 ms: 1.09x slower                                                          |
| create_gc_cycles           | 652 us                                                          | 733 us: 1.12x slower                                                           |
| telco                      | 5.51 ms                                                         | 6.37 ms: 1.16x slower                                                          |
| sqlglot_normalize          | 100 ms                                                          | 223 ms: 2.22x slower                                                           |
| Geometric mean             | (ref)                                                           | 1.13x faster                                                                   |

Benchmark hidden because not significant (4): pickle, unpickle_list, asyncio_tcp, pickle_list
Ignored benchmarks (6) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20240912-3.14.0a0-6e06e01/bm-20240912-pythonperf1_win32-x86-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01.json: genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.11x
- 95% likely to have a speedup of 1.10x
- 99% likely to have a speedup of 1.09x

# Memory
- memory change: unknown