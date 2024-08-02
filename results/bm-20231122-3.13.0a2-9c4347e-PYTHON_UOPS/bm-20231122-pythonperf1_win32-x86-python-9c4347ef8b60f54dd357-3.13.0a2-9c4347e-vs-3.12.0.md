
# Results vs. 3.12.0

- fork: python
- ref: 9c4347ef8b60f54dd357
- machine: windows-x86
- commit hash: 9c4347e
- commit date: 2023-11-22
- overall geometric mean: 1.05x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20231122-pythonperf1_win32-x86-python-9c4347ef8b60f54dd357-3.13.0a2-9c4347e |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 268 ms: 1.04x faster                                                           |
| chameleon      | 7.75 ms                                                         | 6.15 ms: 1.26x faster                                                          |
| docutils       | 1.98 sec                                                        | 1.94 sec: 1.02x faster                                                         |
| tornado_http   | 105 ms                                                          | 112 ms: 1.06x slower                                                           |
| Geometric mean | (ref)                                                           | 1.06x faster                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20231122-pythonperf1_win32-x86-python-9c4347ef8b60f54dd357-3.13.0a2-9c4347e |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_memoization     | 364 ms                                                          | 329 ms: 1.11x faster                                                           |
| async_tree_none            | 298 ms                                                          | 270 ms: 1.10x faster                                                           |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 523 ms: 1.08x faster                                                           |
| async_tree_memoization_tg  | 350 ms                                                          | 327 ms: 1.07x faster                                                           |
| async_tree_io_tg           | 677 ms                                                          | 634 ms: 1.07x faster                                                           |
| async_tree_io              | 693 ms                                                          | 651 ms: 1.06x faster                                                           |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 518 ms: 1.05x faster                                                           |
| async_tree_none_tg         | 278 ms                                                          | 264 ms: 1.05x faster                                                           |
| Geometric mean             | (ref)                                                           | 1.07x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20231122-pythonperf1_win32-x86-python-9c4347ef8b60f54dd357-3.13.0a2-9c4347e |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 91.9 ms: 1.38x faster                                                          |
| float          | 76.7 ms                                                         | 62.3 ms: 1.23x faster                                                          |
| pidigits       | 199 ms                                                          | 198 ms: 1.00x faster                                                           |
| Geometric mean | (ref)                                                           | 1.20x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20231122-pythonperf1_win32-x86-python-9c4347ef8b60f54dd357-3.13.0a2-9c4347e |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 131 ms: 1.02x slower                                                           |
| regex_dna      | 127 ms                                                          | 132 ms: 1.04x slower                                                           |
| regex_v8       | 15.0 ms                                                         | 16.3 ms: 1.08x slower                                                          |
| Geometric mean | (ref)                                                           | 1.03x slower                                                                   |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20231122-pythonperf1_win32-x86-python-9c4347ef8b60f54dd357-3.13.0a2-9c4347e |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| tomli_loads          | 2.20 sec                                                        | 1.79 sec: 1.22x faster                                                         |
| pickle_pure_python   | 286 us                                                          | 235 us: 1.22x faster                                                           |
| unpickle_pure_python | 210 us                                                          | 173 us: 1.21x faster                                                           |
| xml_etree_process    | 53.2 ms                                                         | 47.9 ms: 1.11x faster                                                          |
| unpickle_list        | 2.95 us                                                         | 2.69 us: 1.09x faster                                                          |
| xml_etree_iterparse  | 77.6 ms                                                         | 71.7 ms: 1.08x faster                                                          |
| xml_etree_generate   | 72.1 ms                                                         | 67.3 ms: 1.07x faster                                                          |
| pickle_list          | 3.37 us                                                         | 3.20 us: 1.05x faster                                                          |
| json_dumps           | 7.40 ms                                                         | 7.11 ms: 1.04x faster                                                          |
| xml_etree_parse      | 113 ms                                                          | 111 ms: 1.02x faster                                                           |
| json_loads           | 20.4 us                                                         | 19.9 us: 1.02x faster                                                          |
| pickle               | 7.79 us                                                         | 7.66 us: 1.02x faster                                                          |
| pickle_dict          | 19.9 us                                                         | 19.7 us: 1.01x faster                                                          |
| unpickle             | 9.71 us                                                         | 9.65 us: 1.01x faster                                                          |
| Geometric mean       | (ref)                                                           | 1.08x faster                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20231122-pythonperf1_win32-x86-python-9c4347ef8b60f54dd357-3.13.0a2-9c4347e |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 22.4 ms                                                         | 23.3 ms: 1.04x slower                                                          |
| python_startup_no_site | 19.1 ms                                                         | 21.2 ms: 1.11x slower                                                          |
| Geometric mean         | (ref)                                                           | 1.08x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20231122-pythonperf1_win32-x86-python-9c4347ef8b60f54dd357-3.13.0a2-9c4347e |
|-----------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako      | 9.96 ms                                                         | 8.20 ms: 1.21x faster                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20231122-pythonperf1_win32-x86-python-9c4347ef8b60f54dd357-3.13.0a2-9c4347e |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| unpack_sequence            | 62.5 ns                                                         | 42.6 ns: 1.47x faster                                                          |
| deepcopy_memo              | 38.4 us                                                         | 27.8 us: 1.38x faster                                                          |
| nbody                      | 127 ms                                                          | 91.9 ms: 1.38x faster                                                          |
| logging_silent             | 101 ns                                                          | 76.8 ns: 1.31x faster                                                          |
| generators                 | 38.5 ms                                                         | 29.6 ms: 1.30x faster                                                          |
| scimark_sor                | 130 ms                                                          | 102 ms: 1.27x faster                                                           |
| chameleon                  | 7.75 ms                                                         | 6.15 ms: 1.26x faster                                                          |
| float                      | 76.7 ms                                                         | 62.3 ms: 1.23x faster                                                          |
| tomli_loads                | 2.20 sec                                                        | 1.79 sec: 1.22x faster                                                         |
| deepcopy_reduce            | 3.23 us                                                         | 2.64 us: 1.22x faster                                                          |
| comprehensions             | 19.2 us                                                         | 15.7 us: 1.22x faster                                                          |
| pickle_pure_python         | 286 us                                                          | 235 us: 1.22x faster                                                           |
| mako                       | 9.96 ms                                                         | 8.20 ms: 1.21x faster                                                          |
| chaos                      | 69.4 ms                                                         | 57.2 ms: 1.21x faster                                                          |
| unpickle_pure_python       | 210 us                                                          | 173 us: 1.21x faster                                                           |
| typing_runtime_protocols   | 126 us                                                          | 105 us: 1.20x faster                                                           |
| raytrace                   | 308 ms                                                          | 257 ms: 1.20x faster                                                           |
| crypto_pyaes               | 69.2 ms                                                         | 58.8 ms: 1.18x faster                                                          |
| scimark_lu                 | 93.2 ms                                                         | 79.2 ms: 1.18x faster                                                          |
| sqlglot_parse              | 1.25 ms                                                         | 1.06 ms: 1.18x faster                                                          |
| deepcopy                   | 360 us                                                          | 310 us: 1.16x faster                                                           |
| deltablue                  | 3.58 ms                                                         | 3.08 ms: 1.16x faster                                                          |
| richards                   | 41.3 ms                                                         | 35.6 ms: 1.16x faster                                                          |
| pyflate                    | 424 ms                                                          | 367 ms: 1.16x faster                                                           |
| scimark_monte_carlo        | 66.4 ms                                                         | 57.8 ms: 1.15x faster                                                          |
| sqlglot_transpile          | 1.53 ms                                                         | 1.33 ms: 1.15x faster                                                          |
| richards_super             | 46.5 ms                                                         | 40.6 ms: 1.15x faster                                                          |
| coroutines                 | 20.9 ms                                                         | 18.3 ms: 1.14x faster                                                          |
| logging_format             | 10.4 us                                                         | 9.15 us: 1.14x faster                                                          |
| logging_simple             | 9.75 us                                                         | 8.58 us: 1.14x faster                                                          |
| go                         | 137 ms                                                          | 121 ms: 1.14x faster                                                           |
| pprint_pformat             | 1.50 sec                                                        | 1.33 sec: 1.13x faster                                                         |
| scimark_fft                | 271 ms                                                          | 243 ms: 1.12x faster                                                           |
| xml_etree_process          | 53.2 ms                                                         | 47.9 ms: 1.11x faster                                                          |
| pprint_safe_repr           | 721 ms                                                          | 649 ms: 1.11x faster                                                           |
| sqlite_synth               | 2.07 us                                                         | 1.87 us: 1.11x faster                                                          |
| async_tree_memoization     | 364 ms                                                          | 329 ms: 1.11x faster                                                           |
| fannkuch                   | 354 ms                                                          | 321 ms: 1.10x faster                                                           |
| async_tree_none            | 298 ms                                                          | 270 ms: 1.10x faster                                                           |
| unpickle_list              | 2.95 us                                                         | 2.69 us: 1.09x faster                                                          |
| hexiom                     | 6.82 ms                                                         | 6.24 ms: 1.09x faster                                                          |
| xml_etree_iterparse        | 77.6 ms                                                         | 71.7 ms: 1.08x faster                                                          |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 523 ms: 1.08x faster                                                           |
| async_tree_memoization_tg  | 350 ms                                                          | 327 ms: 1.07x faster                                                           |
| xml_etree_generate         | 72.1 ms                                                         | 67.3 ms: 1.07x faster                                                          |
| spectral_norm              | 104 ms                                                          | 96.9 ms: 1.07x faster                                                          |
| async_tree_io_tg           | 677 ms                                                          | 634 ms: 1.07x faster                                                           |
| async_tree_io              | 693 ms                                                          | 651 ms: 1.06x faster                                                           |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 3.63 ms: 1.06x faster                                                          |
| mdp                        | 1.91 sec                                                        | 1.81 sec: 1.06x faster                                                         |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 518 ms: 1.05x faster                                                           |
| pickle_list                | 3.37 us                                                         | 3.20 us: 1.05x faster                                                          |
| async_tree_none_tg         | 278 ms                                                          | 264 ms: 1.05x faster                                                           |
| meteor_contest             | 86.9 ms                                                         | 83.2 ms: 1.04x faster                                                          |
| 2to3                       | 280 ms                                                          | 268 ms: 1.04x faster                                                           |
| json_dumps                 | 7.40 ms                                                         | 7.11 ms: 1.04x faster                                                          |
| sqlglot_optimize           | 48.5 ms                                                         | 46.8 ms: 1.04x faster                                                          |
| async_generators           | 313 ms                                                          | 304 ms: 1.03x faster                                                           |
| gc_traversal               | 1.44 ms                                                         | 1.40 ms: 1.03x faster                                                          |
| nqueens                    | 93.7 ms                                                         | 91.2 ms: 1.03x faster                                                          |
| pathlib                    | 91.4 ms                                                         | 89.1 ms: 1.03x faster                                                          |
| pycparser                  | 978 ms                                                          | 955 ms: 1.02x faster                                                           |
| xml_etree_parse            | 113 ms                                                          | 111 ms: 1.02x faster                                                           |
| docutils                   | 1.98 sec                                                        | 1.94 sec: 1.02x faster                                                         |
| json_loads                 | 20.4 us                                                         | 19.9 us: 1.02x faster                                                          |
| pickle                     | 7.79 us                                                         | 7.66 us: 1.02x faster                                                          |
| asyncio_tcp_ssl            | 17.7 sec                                                        | 17.4 sec: 1.02x faster                                                         |
| pickle_dict                | 19.9 us                                                         | 19.7 us: 1.01x faster                                                          |
| json                       | 4.15 ms                                                         | 4.12 ms: 1.01x faster                                                          |
| sympy_integrate            | 17.5 ms                                                         | 17.4 ms: 1.01x faster                                                          |
| unpickle                   | 9.71 us                                                         | 9.65 us: 1.01x faster                                                          |
| pidigits                   | 199 ms                                                          | 198 ms: 1.00x faster                                                           |
| sympy_str                  | 240 ms                                                          | 241 ms: 1.01x slower                                                           |
| dask                       | 323 ms                                                          | 328 ms: 1.01x slower                                                           |
| regex_compile              | 129 ms                                                          | 131 ms: 1.02x slower                                                           |
| sympy_expand               | 398 ms                                                          | 408 ms: 1.03x slower                                                           |
| regex_dna                  | 127 ms                                                          | 132 ms: 1.04x slower                                                           |
| python_startup             | 22.4 ms                                                         | 23.3 ms: 1.04x slower                                                          |
| tornado_http               | 105 ms                                                          | 112 ms: 1.06x slower                                                           |
| regex_v8                   | 15.0 ms                                                         | 16.3 ms: 1.08x slower                                                          |
| python_startup_no_site     | 19.1 ms                                                         | 21.2 ms: 1.11x slower                                                          |
| telco                      | 5.51 ms                                                         | 6.40 ms: 1.16x slower                                                          |
| sqlglot_normalize          | 100 ms                                                          | 237 ms: 2.36x slower                                                           |
| coverage                   | 48.4 ms                                                         | 510 ms: 10.53x slower                                                          |
| Geometric mean             | (ref)                                                           | 1.05x faster                                                                   |

Benchmark hidden because not significant (6): regex_effbot, bench_thread_pool, asyncio_tcp, create_gc_cycles, bench_mp_pool, sympy_sum
Ignored benchmarks (6) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, django_template, dulwich_log, mypy2, sqlalchemy_declarative, sqlalchemy_imperative


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x


# Memory

- memory change: unknown