# Results vs. 3.12.0

- fork: savannahostrowski
- ref: jit_llvm_19
- machine: windows-x86
- commit hash: 7f9fe5a
- commit date: 2024-09-26
- overall geometric mean: 1.20x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.15x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240926-pythonperf1_win32-x86-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 260 ms: 1.08x faster                                                             |
| docutils       | 1.98 sec                                                        | 2.00 sec: 1.01x slower                                                           |
| tornado_http   | 105 ms                                                          | 110 ms: 1.05x slower                                                             |
| Geometric mean | (ref)                                                           | 1.01x faster                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240926-pythonperf1_win32-x86-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_none_tg         | 278 ms                                                          | 204 ms: 1.36x faster                                                             |
| async_tree_memoization_tg  | 350 ms                                                          | 260 ms: 1.35x faster                                                             |
| async_tree_none            | 298 ms                                                          | 221 ms: 1.34x faster                                                             |
| async_tree_memoization     | 364 ms                                                          | 280 ms: 1.30x faster                                                             |
| async_tree_io_tg           | 677 ms                                                          | 530 ms: 1.28x faster                                                             |
| async_tree_io              | 693 ms                                                          | 548 ms: 1.26x faster                                                             |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 474 ms: 1.19x faster                                                             |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 467 ms: 1.17x faster                                                             |
| Geometric mean             | (ref)                                                           | 1.28x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240926-pythonperf1_win32-x86-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 48.6 ms: 2.61x faster                                                            |
| float          | 76.7 ms                                                         | 43.3 ms: 1.77x faster                                                            |
| pidigits       | 199 ms                                                          | 195 ms: 1.02x faster                                                             |
| Geometric mean | (ref)                                                           | 1.68x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240926-pythonperf1_win32-x86-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 103 ms: 1.25x faster                                                             |
| regex_dna      | 127 ms                                                          | 119 ms: 1.07x faster                                                             |
| regex_effbot   | 2.04 ms                                                         | 1.96 ms: 1.04x faster                                                            |
| regex_v8       | 15.0 ms                                                         | 16.1 ms: 1.07x slower                                                            |
| Geometric mean | (ref)                                                           | 1.07x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240926-pythonperf1_win32-x86-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| tomli_loads          | 2.20 sec                                                        | 1.56 sec: 1.41x faster                                                           |
| xml_etree_generate   | 72.1 ms                                                         | 54.0 ms: 1.34x faster                                                            |
| xml_etree_process    | 53.2 ms                                                         | 40.6 ms: 1.31x faster                                                            |
| xml_etree_iterparse  | 77.6 ms                                                         | 61.8 ms: 1.26x faster                                                            |
| unpickle_pure_python | 210 us                                                          | 168 us: 1.25x faster                                                             |
| pickle_pure_python   | 286 us                                                          | 255 us: 1.12x faster                                                             |
| xml_etree_parse      | 113 ms                                                          | 104 ms: 1.09x faster                                                             |
| json_dumps           | 7.40 ms                                                         | 6.85 ms: 1.08x faster                                                            |
| unpickle_list        | 2.95 us                                                         | 2.75 us: 1.07x faster                                                            |
| pickle_dict          | 19.9 us                                                         | 20.0 us: 1.00x slower                                                            |
| pickle               | 7.79 us                                                         | 8.02 us: 1.03x slower                                                            |
| json_loads           | 20.4 us                                                         | 21.2 us: 1.04x slower                                                            |
| unpickle             | 9.71 us                                                         | 10.5 us: 1.08x slower                                                            |
| Geometric mean       | (ref)                                                           | 1.12x faster                                                                     |

Benchmark hidden because not significant (1): pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240926-pythonperf1_win32-x86-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 20.2 ms: 1.06x slower                                                            |
| python_startup         | 22.4 ms                                                         | 24.5 ms: 1.09x slower                                                            |
| Geometric mean         | (ref)                                                           | 1.08x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240926-pythonperf1_win32-x86-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 5.48 ms: 1.82x faster                                                            |
| django_template | 36.9 ms                                                         | 34.7 ms: 1.06x faster                                                            |
| Geometric mean  | (ref)                                                           | 1.39x faster                                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240926-pythonperf1_win32-x86-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| nbody                      | 127 ms                                                          | 48.6 ms: 2.61x faster                                                            |
| deepcopy_memo              | 38.4 us                                                         | 15.5 us: 2.47x faster                                                            |
| spectral_norm              | 104 ms                                                          | 47.0 ms: 2.21x faster                                                            |
| scimark_sor                | 130 ms                                                          | 68.2 ms: 1.90x faster                                                            |
| mako                       | 9.96 ms                                                         | 5.48 ms: 1.82x faster                                                            |
| float                      | 76.7 ms                                                         | 43.3 ms: 1.77x faster                                                            |
| generators                 | 38.5 ms                                                         | 22.7 ms: 1.70x faster                                                            |
| deltablue                  | 3.58 ms                                                         | 2.12 ms: 1.69x faster                                                            |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 2.36 ms: 1.63x faster                                                            |
| logging_silent             | 101 ns                                                          | 62.2 ns: 1.62x faster                                                            |
| comprehensions             | 19.2 us                                                         | 11.9 us: 1.62x faster                                                            |
| scimark_fft                | 271 ms                                                          | 173 ms: 1.56x faster                                                             |
| scimark_lu                 | 93.2 ms                                                         | 59.8 ms: 1.56x faster                                                            |
| deepcopy                   | 360 us                                                          | 239 us: 1.51x faster                                                             |
| fannkuch                   | 354 ms                                                          | 235 ms: 1.50x faster                                                             |
| crypto_pyaes               | 69.2 ms                                                         | 47.6 ms: 1.45x faster                                                            |
| pyflate                    | 424 ms                                                          | 297 ms: 1.43x faster                                                             |
| tomli_loads                | 2.20 sec                                                        | 1.56 sec: 1.41x faster                                                           |
| scimark_monte_carlo        | 66.4 ms                                                         | 48.2 ms: 1.38x faster                                                            |
| hexiom                     | 6.82 ms                                                         | 4.96 ms: 1.37x faster                                                            |
| unpack_sequence            | 62.5 ns                                                         | 45.6 ns: 1.37x faster                                                            |
| async_tree_none_tg         | 278 ms                                                          | 204 ms: 1.36x faster                                                             |
| async_tree_memoization_tg  | 350 ms                                                          | 260 ms: 1.35x faster                                                             |
| async_tree_none            | 298 ms                                                          | 221 ms: 1.34x faster                                                             |
| xml_etree_generate         | 72.1 ms                                                         | 54.0 ms: 1.34x faster                                                            |
| go                         | 137 ms                                                          | 104 ms: 1.32x faster                                                             |
| xml_etree_process          | 53.2 ms                                                         | 40.6 ms: 1.31x faster                                                            |
| async_tree_memoization     | 364 ms                                                          | 280 ms: 1.30x faster                                                             |
| richards_super             | 46.5 ms                                                         | 35.9 ms: 1.29x faster                                                            |
| chaos                      | 69.4 ms                                                         | 53.9 ms: 1.29x faster                                                            |
| async_tree_io_tg           | 677 ms                                                          | 530 ms: 1.28x faster                                                             |
| async_tree_io              | 693 ms                                                          | 548 ms: 1.26x faster                                                             |
| deepcopy_reduce            | 3.23 us                                                         | 2.56 us: 1.26x faster                                                            |
| nqueens                    | 93.7 ms                                                         | 74.5 ms: 1.26x faster                                                            |
| xml_etree_iterparse        | 77.6 ms                                                         | 61.8 ms: 1.26x faster                                                            |
| richards                   | 41.3 ms                                                         | 33.0 ms: 1.25x faster                                                            |
| unpickle_pure_python       | 210 us                                                          | 168 us: 1.25x faster                                                             |
| regex_compile              | 129 ms                                                          | 103 ms: 1.25x faster                                                             |
| raytrace                   | 308 ms                                                          | 249 ms: 1.24x faster                                                             |
| logging_simple             | 9.75 us                                                         | 8.05 us: 1.21x faster                                                            |
| meteor_contest             | 86.9 ms                                                         | 72.2 ms: 1.20x faster                                                            |
| pprint_safe_repr           | 721 ms                                                          | 599 ms: 1.20x faster                                                             |
| logging_format             | 10.4 us                                                         | 8.65 us: 1.20x faster                                                            |
| pycparser                  | 978 ms                                                          | 818 ms: 1.20x faster                                                             |
| pprint_pformat             | 1.50 sec                                                        | 1.26 sec: 1.19x faster                                                           |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 474 ms: 1.19x faster                                                             |
| sqlglot_parse              | 1.25 ms                                                         | 1.06 ms: 1.18x faster                                                            |
| dulwich_log                | 58.5 ms                                                         | 49.7 ms: 1.18x faster                                                            |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 467 ms: 1.17x faster                                                             |
| coroutines                 | 20.9 ms                                                         | 18.2 ms: 1.15x faster                                                            |
| sqlglot_transpile          | 1.53 ms                                                         | 1.36 ms: 1.12x faster                                                            |
| pickle_pure_python         | 286 us                                                          | 255 us: 1.12x faster                                                             |
| mdp                        | 1.91 sec                                                        | 1.72 sec: 1.11x faster                                                           |
| bench_thread_pool          | 1.10 ms                                                         | 995 us: 1.11x faster                                                             |
| xml_etree_parse            | 113 ms                                                          | 104 ms: 1.09x faster                                                             |
| sqlite_synth               | 2.07 us                                                         | 1.91 us: 1.08x faster                                                            |
| sympy_sum                  | 123 ms                                                          | 114 ms: 1.08x faster                                                             |
| json_dumps                 | 7.40 ms                                                         | 6.85 ms: 1.08x faster                                                            |
| sympy_str                  | 240 ms                                                          | 222 ms: 1.08x faster                                                             |
| 2to3                       | 280 ms                                                          | 260 ms: 1.08x faster                                                             |
| unpickle_list              | 2.95 us                                                         | 2.75 us: 1.07x faster                                                            |
| regex_dna                  | 127 ms                                                          | 119 ms: 1.07x faster                                                             |
| django_template            | 36.9 ms                                                         | 34.7 ms: 1.06x faster                                                            |
| sympy_integrate            | 17.5 ms                                                         | 16.8 ms: 1.05x faster                                                            |
| pathlib                    | 91.4 ms                                                         | 87.5 ms: 1.05x faster                                                            |
| regex_effbot               | 2.04 ms                                                         | 1.96 ms: 1.04x faster                                                            |
| asyncio_tcp_ssl            | 17.7 sec                                                        | 17.0 sec: 1.04x faster                                                           |
| sqlglot_optimize           | 48.5 ms                                                         | 46.9 ms: 1.03x faster                                                            |
| pidigits                   | 199 ms                                                          | 195 ms: 1.02x faster                                                             |
| json                       | 4.15 ms                                                         | 4.11 ms: 1.01x faster                                                            |
| pickle_dict                | 19.9 us                                                         | 20.0 us: 1.00x slower                                                            |
| sympy_expand               | 398 ms                                                          | 400 ms: 1.01x slower                                                             |
| docutils                   | 1.98 sec                                                        | 2.00 sec: 1.01x slower                                                           |
| bench_mp_pool              | 75.4 ms                                                         | 77.5 ms: 1.03x slower                                                            |
| async_generators           | 313 ms                                                          | 322 ms: 1.03x slower                                                             |
| pickle                     | 7.79 us                                                         | 8.02 us: 1.03x slower                                                            |
| json_loads                 | 20.4 us                                                         | 21.2 us: 1.04x slower                                                            |
| tornado_http               | 105 ms                                                          | 110 ms: 1.05x slower                                                             |
| python_startup_no_site     | 19.1 ms                                                         | 20.2 ms: 1.06x slower                                                            |
| regex_v8                   | 15.0 ms                                                         | 16.1 ms: 1.07x slower                                                            |
| unpickle                   | 9.71 us                                                         | 10.5 us: 1.08x slower                                                            |
| python_startup             | 22.4 ms                                                         | 24.5 ms: 1.09x slower                                                            |
| telco                      | 5.51 ms                                                         | 6.08 ms: 1.10x slower                                                            |
| coverage                   | 48.4 ms                                                         | 54.9 ms: 1.13x slower                                                            |
| create_gc_cycles           | 652 us                                                          | 754 us: 1.16x slower                                                             |
| typing_runtime_protocols   | 126 us                                                          | 148 us: 1.17x slower                                                             |
| sqlglot_normalize          | 100 ms                                                          | 230 ms: 2.29x slower                                                             |
| Geometric mean             | (ref)                                                           | 1.20x faster                                                                     |

Benchmark hidden because not significant (3): gc_traversal, pickle_list, asyncio_tcp
Ignored benchmarks (6) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20240926-3.14.0a0-7f9fe5a-JIT/bm-20240926-pythonperf1_win32-x86-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a.json: genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.18x
- 95% likely to have a speedup of 1.17x
- 99% likely to have a speedup of 1.15x

# Memory
- memory change: unknown