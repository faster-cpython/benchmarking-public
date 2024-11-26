# Results vs. 3.12.0

- fork: python
- ref: 5436d8b9c397c48d9b0d
- machine: windows-x86
- commit hash: 5436d8b
- commit date: 2024-09-11
- overall geometric mean: 1.137x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.10x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240911-pythonperf1_win32-x86-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 249 ms: 1.13x faster                                                           |
| docutils       | 1.98 sec                                                        | 1.86 sec: 1.07x faster                                                         |
| tornado_http   | 105 ms                                                          | 94.8 ms: 1.11x faster                                                          |
| Geometric mean | (ref)                                                           | 1.10x faster                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240911-pythonperf1_win32-x86-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_none_tg         | 278 ms                                                          | 198 ms: 1.40x faster                                                           |
| async_tree_memoization_tg  | 350 ms                                                          | 250 ms: 1.40x faster                                                           |
| async_tree_none            | 298 ms                                                          | 218 ms: 1.37x faster                                                           |
| async_tree_memoization     | 364 ms                                                          | 271 ms: 1.34x faster                                                           |
| async_tree_io_tg           | 677 ms                                                          | 510 ms: 1.33x faster                                                           |
| async_tree_io              | 693 ms                                                          | 529 ms: 1.31x faster                                                           |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 464 ms: 1.22x faster                                                           |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 457 ms: 1.19x faster                                                           |
| Geometric mean             | (ref)                                                           | 1.32x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240911-pythonperf1_win32-x86-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 91.9 ms: 1.38x faster                                                          |
| float          | 76.7 ms                                                         | 62.2 ms: 1.23x faster                                                          |
| pidigits       | 199 ms                                                          | 196 ms: 1.02x faster                                                           |
| Geometric mean | (ref)                                                           | 1.20x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240911-pythonperf1_win32-x86-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 108 ms: 1.20x faster                                                           |
| regex_dna      | 127 ms                                                          | 119 ms: 1.06x faster                                                           |
| regex_effbot   | 2.04 ms                                                         | 1.92 ms: 1.06x faster                                                          |
| regex_v8       | 15.0 ms                                                         | 16.3 ms: 1.08x slower                                                          |
| Geometric mean | (ref)                                                           | 1.06x faster                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240911-pythonperf1_win32-x86-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| tomli_loads          | 2.20 sec                                                        | 1.89 sec: 1.17x faster                                                         |
| xml_etree_iterparse  | 77.6 ms                                                         | 66.9 ms: 1.16x faster                                                          |
| unpickle_pure_python | 210 us                                                          | 181 us: 1.16x faster                                                           |
| pickle_pure_python   | 286 us                                                          | 262 us: 1.09x faster                                                           |
| xml_etree_process    | 53.2 ms                                                         | 49.8 ms: 1.07x faster                                                          |
| xml_etree_generate   | 72.1 ms                                                         | 68.2 ms: 1.06x faster                                                          |
| xml_etree_parse      | 113 ms                                                          | 108 ms: 1.04x faster                                                           |
| json_loads           | 20.4 us                                                         | 20.6 us: 1.01x slower                                                          |
| pickle               | 7.79 us                                                         | 7.99 us: 1.03x slower                                                          |
| json_dumps           | 7.40 ms                                                         | 7.62 ms: 1.03x slower                                                          |
| unpickle_list        | 2.95 us                                                         | 3.10 us: 1.05x slower                                                          |
| pickle_dict          | 19.9 us                                                         | 21.0 us: 1.05x slower                                                          |
| unpickle             | 9.71 us                                                         | 10.3 us: 1.06x slower                                                          |
| pickle_list          | 3.37 us                                                         | 3.65 us: 1.08x slower                                                          |
| Geometric mean       | (ref)                                                           | 1.03x faster                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240911-pythonperf1_win32-x86-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 19.8 ms: 1.04x slower                                                          |
| python_startup         | 22.4 ms                                                         | 24.0 ms: 1.07x slower                                                          |
| Geometric mean         | (ref)                                                           | 1.06x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240911-pythonperf1_win32-x86-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 8.18 ms: 1.22x faster                                                          |
| django_template | 36.9 ms                                                         | 32.6 ms: 1.13x faster                                                          |
| Geometric mean  | (ref)                                                           | 1.17x faster                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240911-pythonperf1_win32-x86-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| deepcopy_memo              | 38.4 us                                                         | 22.3 us: 1.72x faster                                                          |
| generators                 | 38.5 ms                                                         | 26.2 ms: 1.47x faster                                                          |
| deepcopy                   | 360 us                                                          | 246 us: 1.47x faster                                                           |
| async_tree_none_tg         | 278 ms                                                          | 198 ms: 1.40x faster                                                           |
| async_tree_memoization_tg  | 350 ms                                                          | 250 ms: 1.40x faster                                                           |
| nbody                      | 127 ms                                                          | 91.9 ms: 1.38x faster                                                          |
| comprehensions             | 19.2 us                                                         | 14.0 us: 1.37x faster                                                          |
| scimark_lu                 | 93.2 ms                                                         | 68.1 ms: 1.37x faster                                                          |
| async_tree_none            | 298 ms                                                          | 218 ms: 1.37x faster                                                           |
| spectral_norm              | 104 ms                                                          | 76.1 ms: 1.36x faster                                                          |
| logging_silent             | 101 ns                                                          | 75.0 ns: 1.35x faster                                                          |
| async_tree_memoization     | 364 ms                                                          | 271 ms: 1.34x faster                                                           |
| async_tree_io_tg           | 677 ms                                                          | 510 ms: 1.33x faster                                                           |
| hexiom                     | 6.82 ms                                                         | 5.15 ms: 1.32x faster                                                          |
| go                         | 137 ms                                                          | 104 ms: 1.32x faster                                                           |
| deltablue                  | 3.58 ms                                                         | 2.72 ms: 1.32x faster                                                          |
| raytrace                   | 308 ms                                                          | 235 ms: 1.31x faster                                                           |
| async_tree_io              | 693 ms                                                          | 529 ms: 1.31x faster                                                           |
| chaos                      | 69.4 ms                                                         | 53.7 ms: 1.29x faster                                                          |
| deepcopy_reduce            | 3.23 us                                                         | 2.54 us: 1.27x faster                                                          |
| unpack_sequence            | 62.5 ns                                                         | 49.3 ns: 1.27x faster                                                          |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 3.08 ms: 1.25x faster                                                          |
| nqueens                    | 93.7 ms                                                         | 74.9 ms: 1.25x faster                                                          |
| scimark_sor                | 130 ms                                                          | 104 ms: 1.25x faster                                                           |
| float                      | 76.7 ms                                                         | 62.2 ms: 1.23x faster                                                          |
| mako                       | 9.96 ms                                                         | 8.18 ms: 1.22x faster                                                          |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 464 ms: 1.22x faster                                                           |
| logging_simple             | 9.75 us                                                         | 8.04 us: 1.21x faster                                                          |
| regex_compile              | 129 ms                                                          | 108 ms: 1.20x faster                                                           |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 457 ms: 1.19x faster                                                           |
| crypto_pyaes               | 69.2 ms                                                         | 58.1 ms: 1.19x faster                                                          |
| logging_format             | 10.4 us                                                         | 8.77 us: 1.19x faster                                                          |
| pyflate                    | 424 ms                                                          | 360 ms: 1.18x faster                                                           |
| tomli_loads                | 2.20 sec                                                        | 1.89 sec: 1.17x faster                                                         |
| xml_etree_iterparse        | 77.6 ms                                                         | 66.9 ms: 1.16x faster                                                          |
| unpickle_pure_python       | 210 us                                                          | 181 us: 1.16x faster                                                           |
| scimark_monte_carlo        | 66.4 ms                                                         | 57.5 ms: 1.16x faster                                                          |
| sqlglot_parse              | 1.25 ms                                                         | 1.08 ms: 1.15x faster                                                          |
| dulwich_log                | 58.5 ms                                                         | 50.8 ms: 1.15x faster                                                          |
| scimark_fft                | 271 ms                                                          | 236 ms: 1.15x faster                                                           |
| sympy_sum                  | 123 ms                                                          | 108 ms: 1.14x faster                                                           |
| sqlglot_transpile          | 1.53 ms                                                         | 1.35 ms: 1.14x faster                                                          |
| sympy_integrate            | 17.5 ms                                                         | 15.4 ms: 1.14x faster                                                          |
| django_template            | 36.9 ms                                                         | 32.6 ms: 1.13x faster                                                          |
| pycparser                  | 978 ms                                                          | 864 ms: 1.13x faster                                                           |
| 2to3                       | 280 ms                                                          | 249 ms: 1.13x faster                                                           |
| mdp                        | 1.91 sec                                                        | 1.70 sec: 1.13x faster                                                         |
| sqlglot_optimize           | 48.5 ms                                                         | 43.2 ms: 1.12x faster                                                          |
| pathlib                    | 91.4 ms                                                         | 81.8 ms: 1.12x faster                                                          |
| coroutines                 | 20.9 ms                                                         | 18.7 ms: 1.11x faster                                                          |
| pprint_pformat             | 1.50 sec                                                        | 1.35 sec: 1.11x faster                                                         |
| tornado_http               | 105 ms                                                          | 94.8 ms: 1.11x faster                                                          |
| sympy_str                  | 240 ms                                                          | 218 ms: 1.10x faster                                                           |
| pprint_safe_repr           | 721 ms                                                          | 659 ms: 1.09x faster                                                           |
| pickle_pure_python         | 286 us                                                          | 262 us: 1.09x faster                                                           |
| bench_thread_pool          | 1.10 ms                                                         | 1.02 ms: 1.08x faster                                                          |
| bench_mp_pool              | 75.4 ms                                                         | 69.9 ms: 1.08x faster                                                          |
| xml_etree_process          | 53.2 ms                                                         | 49.8 ms: 1.07x faster                                                          |
| docutils                   | 1.98 sec                                                        | 1.86 sec: 1.07x faster                                                         |
| regex_dna                  | 127 ms                                                          | 119 ms: 1.06x faster                                                           |
| meteor_contest             | 86.9 ms                                                         | 81.9 ms: 1.06x faster                                                          |
| regex_effbot               | 2.04 ms                                                         | 1.92 ms: 1.06x faster                                                          |
| xml_etree_generate         | 72.1 ms                                                         | 68.2 ms: 1.06x faster                                                          |
| sqlite_synth               | 2.07 us                                                         | 1.97 us: 1.05x faster                                                          |
| fannkuch                   | 354 ms                                                          | 338 ms: 1.05x faster                                                           |
| xml_etree_parse            | 113 ms                                                          | 108 ms: 1.04x faster                                                           |
| asyncio_tcp_ssl            | 17.7 sec                                                        | 17.0 sec: 1.04x faster                                                         |
| richards                   | 41.3 ms                                                         | 39.8 ms: 1.04x faster                                                          |
| gc_traversal               | 1.44 ms                                                         | 1.39 ms: 1.03x faster                                                          |
| richards_super             | 46.5 ms                                                         | 45.0 ms: 1.03x faster                                                          |
| async_generators           | 313 ms                                                          | 305 ms: 1.03x faster                                                           |
| sympy_expand               | 398 ms                                                          | 388 ms: 1.03x faster                                                           |
| pidigits                   | 199 ms                                                          | 196 ms: 1.02x faster                                                           |
| json_loads                 | 20.4 us                                                         | 20.6 us: 1.01x slower                                                          |
| json                       | 4.15 ms                                                         | 4.25 ms: 1.02x slower                                                          |
| pickle                     | 7.79 us                                                         | 7.99 us: 1.03x slower                                                          |
| json_dumps                 | 7.40 ms                                                         | 7.62 ms: 1.03x slower                                                          |
| python_startup_no_site     | 19.1 ms                                                         | 19.8 ms: 1.04x slower                                                          |
| unpickle_list              | 2.95 us                                                         | 3.10 us: 1.05x slower                                                          |
| pickle_dict                | 19.9 us                                                         | 21.0 us: 1.05x slower                                                          |
| unpickle                   | 9.71 us                                                         | 10.3 us: 1.06x slower                                                          |
| python_startup             | 22.4 ms                                                         | 24.0 ms: 1.07x slower                                                          |
| regex_v8                   | 15.0 ms                                                         | 16.3 ms: 1.08x slower                                                          |
| pickle_list                | 3.37 us                                                         | 3.65 us: 1.08x slower                                                          |
| create_gc_cycles           | 652 us                                                          | 731 us: 1.12x slower                                                           |
| coverage                   | 48.4 ms                                                         | 54.7 ms: 1.13x slower                                                          |
| typing_runtime_protocols   | 126 us                                                          | 145 us: 1.14x slower                                                           |
| telco                      | 5.51 ms                                                         | 6.37 ms: 1.16x slower                                                          |
| sqlglot_normalize          | 100 ms                                                          | 226 ms: 2.25x slower                                                           |
| Geometric mean             | (ref)                                                           | 1.12x faster                                                                   |

Benchmark hidden because not significant (1): asyncio_tcp
Ignored benchmarks (6) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20240911-3.14.0a0-5436d8b/bm-20240911-pythonperf1_win32-x86-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b.json: genshi_text, genshi_xml, html5lib, pylint, thrift

- Geometric mean (including insignificant results): 1.137x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.12x
- 95% likely to have a speedup of 1.12x
- 99% likely to have a speedup of 1.10x

# Memory
- memory change: unknown