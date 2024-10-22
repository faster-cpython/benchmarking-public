# Results vs. 3.12.0

- fork: python
- ref: 7aca84e557d0a6d242f3
- machine: windows-x86
- commit hash: 7aca84e
- commit date: 2024-08-02
- overall geometric mean: 1.10x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.07x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240802-pythonperf1_win32-x86-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 264 ms: 1.06x faster                                                           |
| docutils       | 1.98 sec                                                        | 1.96 sec: 1.01x faster                                                         |
| tornado_http   | 105 ms                                                          | 107 ms: 1.02x slower                                                           |
| Geometric mean | (ref)                                                           | 1.02x faster                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240802-pythonperf1_win32-x86-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 350 ms                                                          | 256 ms: 1.37x faster                                                           |
| async_tree_none_tg         | 278 ms                                                          | 204 ms: 1.36x faster                                                           |
| async_tree_io_tg           | 677 ms                                                          | 528 ms: 1.28x faster                                                           |
| async_tree_none            | 298 ms                                                          | 232 ms: 1.28x faster                                                           |
| async_tree_memoization     | 364 ms                                                          | 287 ms: 1.27x faster                                                           |
| async_tree_io              | 693 ms                                                          | 570 ms: 1.21x faster                                                           |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 484 ms: 1.16x faster                                                           |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 472 ms: 1.16x faster                                                           |
| Geometric mean             | (ref)                                                           | 1.26x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240802-pythonperf1_win32-x86-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 102 ms: 1.25x faster                                                           |
| float          | 76.7 ms                                                         | 61.5 ms: 1.25x faster                                                          |
| Geometric mean | (ref)                                                           | 1.16x faster                                                                   |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240802-pythonperf1_win32-x86-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 111 ms: 1.16x faster                                                           |
| regex_dna      | 127 ms                                                          | 129 ms: 1.01x slower                                                           |
| regex_v8       | 15.0 ms                                                         | 16.4 ms: 1.09x slower                                                          |
| Geometric mean | (ref)                                                           | 1.01x faster                                                                   |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240802-pythonperf1_win32-x86-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| unpickle_pure_python | 210 us                                                          | 174 us: 1.21x faster                                                           |
| tomli_loads          | 2.20 sec                                                        | 1.91 sec: 1.15x faster                                                         |
| xml_etree_iterparse  | 77.6 ms                                                         | 67.7 ms: 1.15x faster                                                          |
| xml_etree_generate   | 72.1 ms                                                         | 65.8 ms: 1.10x faster                                                          |
| xml_etree_process    | 53.2 ms                                                         | 49.1 ms: 1.08x faster                                                          |
| pickle_pure_python   | 286 us                                                          | 266 us: 1.08x faster                                                           |
| xml_etree_parse      | 113 ms                                                          | 105 ms: 1.07x faster                                                           |
| json_loads           | 20.4 us                                                         | 20.8 us: 1.02x slower                                                          |
| json_dumps           | 7.40 ms                                                         | 7.71 ms: 1.04x slower                                                          |
| Geometric mean       | (ref)                                                           | 1.08x faster                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240802-pythonperf1_win32-x86-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 19.6 ms: 1.03x slower                                                          |
| python_startup         | 22.4 ms                                                         | 23.7 ms: 1.06x slower                                                          |
| Geometric mean         | (ref)                                                           | 1.05x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240802-pythonperf1_win32-x86-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 8.31 ms: 1.20x faster                                                          |
| django_template | 36.9 ms                                                         | 34.9 ms: 1.06x faster                                                          |
| Geometric mean  | (ref)                                                           | 1.13x faster                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240802-pythonperf1_win32-x86-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| deepcopy_memo              | 38.4 us                                                         | 23.0 us: 1.67x faster                                                          |
| generators                 | 38.5 ms                                                         | 27.9 ms: 1.38x faster                                                          |
| async_tree_memoization_tg  | 350 ms                                                          | 256 ms: 1.37x faster                                                           |
| comprehensions             | 19.2 us                                                         | 14.1 us: 1.36x faster                                                          |
| deepcopy                   | 360 us                                                          | 264 us: 1.36x faster                                                           |
| async_tree_none_tg         | 278 ms                                                          | 204 ms: 1.36x faster                                                           |
| logging_silent             | 101 ns                                                          | 75.3 ns: 1.34x faster                                                          |
| spectral_norm              | 104 ms                                                          | 78.0 ms: 1.33x faster                                                          |
| scimark_sor                | 130 ms                                                          | 101 ms: 1.29x faster                                                           |
| scimark_lu                 | 93.2 ms                                                         | 72.4 ms: 1.29x faster                                                          |
| async_tree_io_tg           | 677 ms                                                          | 528 ms: 1.28x faster                                                           |
| async_tree_none            | 298 ms                                                          | 232 ms: 1.28x faster                                                           |
| raytrace                   | 308 ms                                                          | 241 ms: 1.28x faster                                                           |
| chaos                      | 69.4 ms                                                         | 54.7 ms: 1.27x faster                                                          |
| async_tree_memoization     | 364 ms                                                          | 287 ms: 1.27x faster                                                           |
| hexiom                     | 6.82 ms                                                         | 5.40 ms: 1.26x faster                                                          |
| deltablue                  | 3.58 ms                                                         | 2.84 ms: 1.26x faster                                                          |
| nbody                      | 127 ms                                                          | 102 ms: 1.25x faster                                                           |
| float                      | 76.7 ms                                                         | 61.5 ms: 1.25x faster                                                          |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 3.17 ms: 1.22x faster                                                          |
| async_tree_io              | 693 ms                                                          | 570 ms: 1.21x faster                                                           |
| deepcopy_reduce            | 3.23 us                                                         | 2.66 us: 1.21x faster                                                          |
| unpickle_pure_python       | 210 us                                                          | 174 us: 1.21x faster                                                           |
| mako                       | 9.96 ms                                                         | 8.31 ms: 1.20x faster                                                          |
| nqueens                    | 93.7 ms                                                         | 79.0 ms: 1.19x faster                                                          |
| logging_simple             | 9.75 us                                                         | 8.27 us: 1.18x faster                                                          |
| coroutines                 | 20.9 ms                                                         | 17.7 ms: 1.18x faster                                                          |
| pyflate                    | 424 ms                                                          | 360 ms: 1.18x faster                                                           |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 484 ms: 1.16x faster                                                           |
| regex_compile              | 129 ms                                                          | 111 ms: 1.16x faster                                                           |
| logging_format             | 10.4 us                                                         | 8.98 us: 1.16x faster                                                          |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 472 ms: 1.16x faster                                                           |
| crypto_pyaes               | 69.2 ms                                                         | 59.8 ms: 1.16x faster                                                          |
| scimark_fft                | 271 ms                                                          | 235 ms: 1.15x faster                                                           |
| tomli_loads                | 2.20 sec                                                        | 1.91 sec: 1.15x faster                                                         |
| xml_etree_iterparse        | 77.6 ms                                                         | 67.7 ms: 1.15x faster                                                          |
| scimark_monte_carlo        | 66.4 ms                                                         | 58.2 ms: 1.14x faster                                                          |
| dulwich_log                | 58.5 ms                                                         | 51.6 ms: 1.13x faster                                                          |
| sqlglot_parse              | 1.25 ms                                                         | 1.12 ms: 1.11x faster                                                          |
| sqlglot_transpile          | 1.53 ms                                                         | 1.38 ms: 1.11x faster                                                          |
| go                         | 137 ms                                                          | 124 ms: 1.11x faster                                                           |
| xml_etree_generate         | 72.1 ms                                                         | 65.8 ms: 1.10x faster                                                          |
| bench_thread_pool          | 1.10 ms                                                         | 1.01 ms: 1.10x faster                                                          |
| sympy_sum                  | 123 ms                                                          | 112 ms: 1.09x faster                                                           |
| sympy_integrate            | 17.5 ms                                                         | 16.1 ms: 1.09x faster                                                          |
| fannkuch                   | 354 ms                                                          | 325 ms: 1.09x faster                                                           |
| sqlglot_optimize           | 48.5 ms                                                         | 44.6 ms: 1.09x faster                                                          |
| mdp                        | 1.91 sec                                                        | 1.76 sec: 1.08x faster                                                         |
| xml_etree_process          | 53.2 ms                                                         | 49.1 ms: 1.08x faster                                                          |
| pprint_pformat             | 1.50 sec                                                        | 1.39 sec: 1.08x faster                                                         |
| pickle_pure_python         | 286 us                                                          | 266 us: 1.08x faster                                                           |
| xml_etree_parse            | 113 ms                                                          | 105 ms: 1.07x faster                                                           |
| pycparser                  | 978 ms                                                          | 918 ms: 1.07x faster                                                           |
| sympy_str                  | 240 ms                                                          | 225 ms: 1.06x faster                                                           |
| 2to3                       | 280 ms                                                          | 264 ms: 1.06x faster                                                           |
| django_template            | 36.9 ms                                                         | 34.9 ms: 1.06x faster                                                          |
| pprint_safe_repr           | 721 ms                                                          | 685 ms: 1.05x faster                                                           |
| meteor_contest             | 86.9 ms                                                         | 83.9 ms: 1.04x faster                                                          |
| asyncio_tcp_ssl            | 17.7 sec                                                        | 17.2 sec: 1.03x faster                                                         |
| pathlib                    | 91.4 ms                                                         | 89.3 ms: 1.02x faster                                                          |
| async_generators           | 313 ms                                                          | 306 ms: 1.02x faster                                                           |
| bench_mp_pool              | 75.4 ms                                                         | 74.2 ms: 1.02x faster                                                          |
| sympy_expand               | 398 ms                                                          | 392 ms: 1.01x faster                                                           |
| docutils                   | 1.98 sec                                                        | 1.96 sec: 1.01x faster                                                         |
| regex_dna                  | 127 ms                                                          | 129 ms: 1.01x slower                                                           |
| tornado_http               | 105 ms                                                          | 107 ms: 1.02x slower                                                           |
| richards_super             | 46.5 ms                                                         | 47.4 ms: 1.02x slower                                                          |
| json_loads                 | 20.4 us                                                         | 20.8 us: 1.02x slower                                                          |
| python_startup_no_site     | 19.1 ms                                                         | 19.6 ms: 1.03x slower                                                          |
| json_dumps                 | 7.40 ms                                                         | 7.71 ms: 1.04x slower                                                          |
| json                       | 4.15 ms                                                         | 4.34 ms: 1.04x slower                                                          |
| richards                   | 41.3 ms                                                         | 43.7 ms: 1.06x slower                                                          |
| python_startup             | 22.4 ms                                                         | 23.7 ms: 1.06x slower                                                          |
| coverage                   | 48.4 ms                                                         | 52.2 ms: 1.08x slower                                                          |
| regex_v8                   | 15.0 ms                                                         | 16.4 ms: 1.09x slower                                                          |
| create_gc_cycles           | 652 us                                                          | 753 us: 1.16x slower                                                           |
| asyncio_tcp                | 662 ms                                                          | 785 ms: 1.19x slower                                                           |
| telco                      | 5.51 ms                                                         | 6.60 ms: 1.20x slower                                                          |
| typing_runtime_protocols   | 126 us                                                          | 152 us: 1.20x slower                                                           |
| sqlglot_normalize          | 100 ms                                                          | 229 ms: 2.28x slower                                                           |
| Geometric mean             | (ref)                                                           | 1.10x faster                                                                   |

Benchmark hidden because not significant (3): gc_traversal, pidigits, regex_effbot
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240802-3.14.0a0-7aca84e/bm-20240802-pythonperf1_win32-x86-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e.json: genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.08x
- 95% likely to have a speedup of 1.08x
- 99% likely to have a speedup of 1.07x

# Memory
- memory change: unknown