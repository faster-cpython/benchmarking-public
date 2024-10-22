# Results vs. 3.12.0

- fork: python
- ref: 11fa11987990eb7ed75b
- machine: windows-x86
- commit hash: 11fa119
- commit date: 2024-09-07
- overall geometric mean: 1.22x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.15x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240907-pythonperf1_win32-x86-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 264 ms: 1.06x faster                                                           |
| docutils       | 1.98 sec                                                        | 2.01 sec: 1.02x slower                                                         |
| tornado_http   | 105 ms                                                          | 110 ms: 1.04x slower                                                           |
| Geometric mean | (ref)                                                           | 1.00x faster                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240907-pythonperf1_win32-x86-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_none_tg         | 278 ms                                                          | 201 ms: 1.38x faster                                                           |
| async_tree_memoization_tg  | 350 ms                                                          | 256 ms: 1.37x faster                                                           |
| async_tree_none            | 298 ms                                                          | 220 ms: 1.35x faster                                                           |
| async_tree_memoization     | 364 ms                                                          | 276 ms: 1.32x faster                                                           |
| async_tree_io_tg           | 677 ms                                                          | 524 ms: 1.29x faster                                                           |
| async_tree_io              | 693 ms                                                          | 544 ms: 1.27x faster                                                           |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 470 ms: 1.20x faster                                                           |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 465 ms: 1.17x faster                                                           |
| Geometric mean             | (ref)                                                           | 1.29x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240907-pythonperf1_win32-x86-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 50.1 ms: 2.53x faster                                                          |
| float          | 76.7 ms                                                         | 44.5 ms: 1.72x faster                                                          |
| Geometric mean | (ref)                                                           | 1.64x faster                                                                   |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240907-pythonperf1_win32-x86-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 101 ms: 1.28x faster                                                           |
| regex_dna      | 127 ms                                                          | 129 ms: 1.02x slower                                                           |
| regex_v8       | 15.0 ms                                                         | 15.9 ms: 1.05x slower                                                          |
| Geometric mean | (ref)                                                           | 1.05x faster                                                                   |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240907-pythonperf1_win32-x86-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| tomli_loads          | 2.20 sec                                                        | 1.48 sec: 1.48x faster                                                         |
| xml_etree_generate   | 72.1 ms                                                         | 53.3 ms: 1.35x faster                                                          |
| xml_etree_process    | 53.2 ms                                                         | 40.1 ms: 1.33x faster                                                          |
| unpickle_pure_python | 210 us                                                          | 161 us: 1.30x faster                                                           |
| xml_etree_iterparse  | 77.6 ms                                                         | 62.4 ms: 1.24x faster                                                          |
| pickle_pure_python   | 286 us                                                          | 241 us: 1.19x faster                                                           |
| xml_etree_parse      | 113 ms                                                          | 105 ms: 1.08x faster                                                           |
| json_dumps           | 7.40 ms                                                         | 6.92 ms: 1.07x faster                                                          |
| unpickle_list        | 2.95 us                                                         | 2.79 us: 1.06x faster                                                          |
| pickle               | 7.79 us                                                         | 7.84 us: 1.01x slower                                                          |
| json_loads           | 20.4 us                                                         | 20.6 us: 1.01x slower                                                          |
| pickle_dict          | 19.9 us                                                         | 20.2 us: 1.02x slower                                                          |
| unpickle             | 9.71 us                                                         | 10.6 us: 1.09x slower                                                          |
| Geometric mean       | (ref)                                                           | 1.13x faster                                                                   |

Benchmark hidden because not significant (1): pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240907-pythonperf1_win32-x86-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 20.9 ms: 1.10x slower                                                          |
| python_startup         | 22.4 ms                                                         | 25.0 ms: 1.12x slower                                                          |
| Geometric mean         | (ref)                                                           | 1.11x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240907-pythonperf1_win32-x86-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 5.57 ms: 1.79x faster                                                          |
| django_template | 36.9 ms                                                         | 33.5 ms: 1.10x faster                                                          |
| Geometric mean  | (ref)                                                           | 1.40x faster                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240907-pythonperf1_win32-x86-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| nbody                      | 127 ms                                                          | 50.1 ms: 2.53x faster                                                          |
| deepcopy_memo              | 38.4 us                                                         | 15.7 us: 2.45x faster                                                          |
| spectral_norm              | 104 ms                                                          | 49.2 ms: 2.11x faster                                                          |
| scimark_sor                | 130 ms                                                          | 68.1 ms: 1.91x faster                                                          |
| mako                       | 9.96 ms                                                         | 5.57 ms: 1.79x faster                                                          |
| deltablue                  | 3.58 ms                                                         | 2.04 ms: 1.76x faster                                                          |
| float                      | 76.7 ms                                                         | 44.5 ms: 1.72x faster                                                          |
| logging_silent             | 101 ns                                                          | 61.5 ns: 1.64x faster                                                          |
| generators                 | 38.5 ms                                                         | 23.6 ms: 1.63x faster                                                          |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 2.40 ms: 1.61x faster                                                          |
| comprehensions             | 19.2 us                                                         | 12.0 us: 1.60x faster                                                          |
| scimark_fft                | 271 ms                                                          | 172 ms: 1.58x faster                                                           |
| deepcopy                   | 360 us                                                          | 232 us: 1.55x faster                                                           |
| scimark_lu                 | 93.2 ms                                                         | 60.3 ms: 1.55x faster                                                          |
| pyflate                    | 424 ms                                                          | 275 ms: 1.54x faster                                                           |
| fannkuch                   | 354 ms                                                          | 237 ms: 1.49x faster                                                           |
| tomli_loads                | 2.20 sec                                                        | 1.48 sec: 1.48x faster                                                         |
| crypto_pyaes               | 69.2 ms                                                         | 48.4 ms: 1.43x faster                                                          |
| unpack_sequence            | 62.5 ns                                                         | 44.2 ns: 1.41x faster                                                          |
| go                         | 137 ms                                                          | 98.9 ms: 1.39x faster                                                          |
| async_tree_none_tg         | 278 ms                                                          | 201 ms: 1.38x faster                                                           |
| hexiom                     | 6.82 ms                                                         | 4.96 ms: 1.37x faster                                                          |
| async_tree_memoization_tg  | 350 ms                                                          | 256 ms: 1.37x faster                                                           |
| async_tree_none            | 298 ms                                                          | 220 ms: 1.35x faster                                                           |
| xml_etree_generate         | 72.1 ms                                                         | 53.3 ms: 1.35x faster                                                          |
| scimark_monte_carlo        | 66.4 ms                                                         | 49.6 ms: 1.34x faster                                                          |
| xml_etree_process          | 53.2 ms                                                         | 40.1 ms: 1.33x faster                                                          |
| async_tree_memoization     | 364 ms                                                          | 276 ms: 1.32x faster                                                           |
| unpickle_pure_python       | 210 us                                                          | 161 us: 1.30x faster                                                           |
| async_tree_io_tg           | 677 ms                                                          | 524 ms: 1.29x faster                                                           |
| richards_super             | 46.5 ms                                                         | 36.2 ms: 1.28x faster                                                          |
| regex_compile              | 129 ms                                                          | 101 ms: 1.28x faster                                                           |
| deepcopy_reduce            | 3.23 us                                                         | 2.52 us: 1.28x faster                                                          |
| async_tree_io              | 693 ms                                                          | 544 ms: 1.27x faster                                                           |
| chaos                      | 69.4 ms                                                         | 55.0 ms: 1.26x faster                                                          |
| logging_simple             | 9.75 us                                                         | 7.75 us: 1.26x faster                                                          |
| richards                   | 41.3 ms                                                         | 32.9 ms: 1.26x faster                                                          |
| pprint_safe_repr           | 721 ms                                                          | 574 ms: 1.26x faster                                                           |
| pprint_pformat             | 1.50 sec                                                        | 1.20 sec: 1.25x faster                                                         |
| xml_etree_iterparse        | 77.6 ms                                                         | 62.4 ms: 1.24x faster                                                          |
| raytrace                   | 308 ms                                                          | 248 ms: 1.24x faster                                                           |
| logging_format             | 10.4 us                                                         | 8.46 us: 1.23x faster                                                          |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 470 ms: 1.20x faster                                                           |
| sqlglot_parse              | 1.25 ms                                                         | 1.04 ms: 1.20x faster                                                          |
| pycparser                  | 978 ms                                                          | 821 ms: 1.19x faster                                                           |
| pickle_pure_python         | 286 us                                                          | 241 us: 1.19x faster                                                           |
| nqueens                    | 93.7 ms                                                         | 79.3 ms: 1.18x faster                                                          |
| dulwich_log                | 58.5 ms                                                         | 49.8 ms: 1.17x faster                                                          |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 465 ms: 1.17x faster                                                           |
| meteor_contest             | 86.9 ms                                                         | 74.5 ms: 1.17x faster                                                          |
| mdp                        | 1.91 sec                                                        | 1.68 sec: 1.14x faster                                                         |
| sqlglot_transpile          | 1.53 ms                                                         | 1.35 ms: 1.14x faster                                                          |
| coroutines                 | 20.9 ms                                                         | 18.5 ms: 1.13x faster                                                          |
| sqlite_synth               | 2.07 us                                                         | 1.86 us: 1.11x faster                                                          |
| bench_thread_pool          | 1.10 ms                                                         | 996 us: 1.11x faster                                                           |
| django_template            | 36.9 ms                                                         | 33.5 ms: 1.10x faster                                                          |
| xml_etree_parse            | 113 ms                                                          | 105 ms: 1.08x faster                                                           |
| sympy_str                  | 240 ms                                                          | 224 ms: 1.07x faster                                                           |
| json_dumps                 | 7.40 ms                                                         | 6.92 ms: 1.07x faster                                                          |
| sympy_sum                  | 123 ms                                                          | 115 ms: 1.07x faster                                                           |
| 2to3                       | 280 ms                                                          | 264 ms: 1.06x faster                                                           |
| unpickle_list              | 2.95 us                                                         | 2.79 us: 1.06x faster                                                          |
| pathlib                    | 91.4 ms                                                         | 87.4 ms: 1.05x faster                                                          |
| sympy_integrate            | 17.5 ms                                                         | 16.8 ms: 1.05x faster                                                          |
| sqlglot_optimize           | 48.5 ms                                                         | 46.8 ms: 1.04x faster                                                          |
| asyncio_tcp_ssl            | 17.7 sec                                                        | 17.1 sec: 1.03x faster                                                         |
| json                       | 4.15 ms                                                         | 4.03 ms: 1.03x faster                                                          |
| pickle                     | 7.79 us                                                         | 7.84 us: 1.01x slower                                                          |
| sympy_expand               | 398 ms                                                          | 402 ms: 1.01x slower                                                           |
| json_loads                 | 20.4 us                                                         | 20.6 us: 1.01x slower                                                          |
| docutils                   | 1.98 sec                                                        | 2.01 sec: 1.02x slower                                                         |
| pickle_dict                | 19.9 us                                                         | 20.2 us: 1.02x slower                                                          |
| regex_dna                  | 127 ms                                                          | 129 ms: 1.02x slower                                                           |
| async_generators           | 313 ms                                                          | 322 ms: 1.03x slower                                                           |
| tornado_http               | 105 ms                                                          | 110 ms: 1.04x slower                                                           |
| regex_v8                   | 15.0 ms                                                         | 15.9 ms: 1.05x slower                                                          |
| bench_mp_pool              | 75.4 ms                                                         | 80.2 ms: 1.06x slower                                                          |
| telco                      | 5.51 ms                                                         | 5.93 ms: 1.08x slower                                                          |
| unpickle                   | 9.71 us                                                         | 10.6 us: 1.09x slower                                                          |
| python_startup_no_site     | 19.1 ms                                                         | 20.9 ms: 1.10x slower                                                          |
| python_startup             | 22.4 ms                                                         | 25.0 ms: 1.12x slower                                                          |
| coverage                   | 48.4 ms                                                         | 54.7 ms: 1.13x slower                                                          |
| typing_runtime_protocols   | 126 us                                                          | 145 us: 1.15x slower                                                           |
| create_gc_cycles           | 652 us                                                          | 752 us: 1.15x slower                                                           |
| Geometric mean             | (ref)                                                           | 1.22x faster                                                                   |

Benchmark hidden because not significant (6): regex_effbot, pidigits, gc_traversal, sqlglot_normalize, pickle_list, asyncio_tcp
Ignored benchmarks (6) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20240907-3.14.0a0-11fa119-JIT/bm-20240907-pythonperf1_win32-x86-python-11fa11987990eb7ed75b-3.14.0a0-11fa119.json: genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.18x
- 95% likely to have a speedup of 1.17x
- 99% likely to have a speedup of 1.15x

# Memory
- memory change: unknown