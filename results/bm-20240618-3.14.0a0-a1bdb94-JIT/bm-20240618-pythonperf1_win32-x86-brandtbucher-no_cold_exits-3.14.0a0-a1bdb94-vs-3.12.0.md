# Results vs. 3.12.0

- fork: brandtbucher
- ref: no_cold_exits
- machine: windows-x86
- commit hash: a1bdb94
- commit date: 2024-06-18
- overall geometric mean: 1.22x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.14x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240618-pythonperf1_win32-x86-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94 |
|----------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 249 ms: 1.13x faster                                                          |
| docutils       | 1.98 sec                                                        | 1.92 sec: 1.03x faster                                                        |
| tornado_http   | 105 ms                                                          | 97.8 ms: 1.07x faster                                                         |
| Geometric mean | (ref)                                                           | 1.08x faster                                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240618-pythonperf1_win32-x86-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94 |
|----------------------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 350 ms                                                          | 263 ms: 1.33x faster                                                          |
| async_tree_none_tg         | 278 ms                                                          | 213 ms: 1.31x faster                                                          |
| async_tree_memoization     | 364 ms                                                          | 289 ms: 1.26x faster                                                          |
| async_tree_none            | 298 ms                                                          | 238 ms: 1.25x faster                                                          |
| async_tree_io              | 693 ms                                                          | 555 ms: 1.25x faster                                                          |
| async_tree_io_tg           | 677 ms                                                          | 549 ms: 1.23x faster                                                          |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 460 ms: 1.19x faster                                                          |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 488 ms: 1.16x faster                                                          |
| Geometric mean             | (ref)                                                           | 1.25x faster                                                                  |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240618-pythonperf1_win32-x86-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94 |
|----------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 52.5 ms: 2.42x faster                                                         |
| float          | 76.7 ms                                                         | 43.0 ms: 1.78x faster                                                         |
| pidigits       | 199 ms                                                          | 197 ms: 1.01x faster                                                          |
| Geometric mean | (ref)                                                           | 1.64x faster                                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240618-pythonperf1_win32-x86-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94 |
|----------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 94.7 ms: 1.36x faster                                                         |
| regex_dna      | 127 ms                                                          | 132 ms: 1.04x slower                                                          |
| regex_v8       | 15.0 ms                                                         | 16.0 ms: 1.06x slower                                                         |
| Geometric mean | (ref)                                                           | 1.05x faster                                                                  |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240618-pythonperf1_win32-x86-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94 |
|----------------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| tomli_loads          | 2.20 sec                                                        | 1.48 sec: 1.48x faster                                                        |
| unpickle_pure_python | 210 us                                                          | 143 us: 1.47x faster                                                          |
| pickle_pure_python   | 286 us                                                          | 210 us: 1.36x faster                                                          |
| xml_etree_iterparse  | 77.6 ms                                                         | 61.3 ms: 1.27x faster                                                         |
| xml_etree_generate   | 72.1 ms                                                         | 58.3 ms: 1.24x faster                                                         |
| xml_etree_process    | 53.2 ms                                                         | 43.2 ms: 1.23x faster                                                         |
| xml_etree_parse      | 113 ms                                                          | 102 ms: 1.11x faster                                                          |
| json_dumps           | 7.40 ms                                                         | 7.01 ms: 1.06x faster                                                         |
| unpickle_list        | 2.95 us                                                         | 2.89 us: 1.02x faster                                                         |
| json_loads           | 20.4 us                                                         | 20.5 us: 1.01x slower                                                         |
| pickle_dict          | 19.9 us                                                         | 20.6 us: 1.03x slower                                                         |
| unpickle             | 9.71 us                                                         | 10.1 us: 1.04x slower                                                         |
| pickle_list          | 3.37 us                                                         | 3.60 us: 1.07x slower                                                         |
| pickle               | 7.79 us                                                         | 8.35 us: 1.07x slower                                                         |
| Geometric mean       | (ref)                                                           | 1.13x faster                                                                  |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240618-pythonperf1_win32-x86-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94 |
|------------------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 18.6 ms: 1.03x faster                                                         |
| python_startup         | 22.4 ms                                                         | 22.8 ms: 1.02x slower                                                         |
| Geometric mean         | (ref)                                                           | 1.00x faster                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240618-pythonperf1_win32-x86-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94 |
|-----------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 5.50 ms: 1.81x faster                                                         |
| django_template | 36.9 ms                                                         | 32.9 ms: 1.12x faster                                                         |
| Geometric mean  | (ref)                                                           | 1.43x faster                                                                  |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240618-pythonperf1_win32-x86-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94 |
|----------------------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| deepcopy_memo              | 38.4 us                                                         | 15.4 us: 2.48x faster                                                         |
| nbody                      | 127 ms                                                          | 52.5 ms: 2.42x faster                                                         |
| spectral_norm              | 104 ms                                                          | 49.3 ms: 2.11x faster                                                         |
| mako                       | 9.96 ms                                                         | 5.50 ms: 1.81x faster                                                         |
| float                      | 76.7 ms                                                         | 43.0 ms: 1.78x faster                                                         |
| logging_silent             | 101 ns                                                          | 57.4 ns: 1.76x faster                                                         |
| comprehensions             | 19.2 us                                                         | 11.2 us: 1.72x faster                                                         |
| scimark_monte_carlo        | 66.4 ms                                                         | 39.7 ms: 1.67x faster                                                         |
| fannkuch                   | 354 ms                                                          | 215 ms: 1.64x faster                                                          |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 2.40 ms: 1.61x faster                                                         |
| scimark_fft                | 271 ms                                                          | 169 ms: 1.60x faster                                                          |
| deepcopy                   | 360 us                                                          | 234 us: 1.54x faster                                                          |
| pyflate                    | 424 ms                                                          | 283 ms: 1.50x faster                                                          |
| hexiom                     | 6.82 ms                                                         | 4.55 ms: 1.50x faster                                                         |
| tomli_loads                | 2.20 sec                                                        | 1.48 sec: 1.48x faster                                                        |
| unpickle_pure_python       | 210 us                                                          | 143 us: 1.47x faster                                                          |
| crypto_pyaes               | 69.2 ms                                                         | 48.1 ms: 1.44x faster                                                         |
| generators                 | 38.5 ms                                                         | 27.9 ms: 1.38x faster                                                         |
| pickle_pure_python         | 286 us                                                          | 210 us: 1.36x faster                                                          |
| regex_compile              | 129 ms                                                          | 94.7 ms: 1.36x faster                                                         |
| raytrace                   | 308 ms                                                          | 227 ms: 1.36x faster                                                          |
| deepcopy_reduce            | 3.23 us                                                         | 2.39 us: 1.35x faster                                                         |
| scimark_sor                | 130 ms                                                          | 96.2 ms: 1.35x faster                                                         |
| async_tree_memoization_tg  | 350 ms                                                          | 263 ms: 1.33x faster                                                          |
| sqlglot_parse              | 1.25 ms                                                         | 939 us: 1.33x faster                                                          |
| pprint_pformat             | 1.50 sec                                                        | 1.14 sec: 1.31x faster                                                        |
| chaos                      | 69.4 ms                                                         | 53.1 ms: 1.31x faster                                                         |
| deltablue                  | 3.58 ms                                                         | 2.74 ms: 1.31x faster                                                         |
| async_tree_none_tg         | 278 ms                                                          | 213 ms: 1.31x faster                                                          |
| pprint_safe_repr           | 721 ms                                                          | 553 ms: 1.30x faster                                                          |
| nqueens                    | 93.7 ms                                                         | 71.9 ms: 1.30x faster                                                         |
| logging_simple             | 9.75 us                                                         | 7.56 us: 1.29x faster                                                         |
| sqlglot_transpile          | 1.53 ms                                                         | 1.20 ms: 1.27x faster                                                         |
| logging_format             | 10.4 us                                                         | 8.21 us: 1.27x faster                                                         |
| richards                   | 41.3 ms                                                         | 32.6 ms: 1.27x faster                                                         |
| xml_etree_iterparse        | 77.6 ms                                                         | 61.3 ms: 1.27x faster                                                         |
| async_tree_memoization     | 364 ms                                                          | 289 ms: 1.26x faster                                                          |
| async_tree_none            | 298 ms                                                          | 238 ms: 1.25x faster                                                          |
| async_tree_io              | 693 ms                                                          | 555 ms: 1.25x faster                                                          |
| scimark_lu                 | 93.2 ms                                                         | 74.8 ms: 1.25x faster                                                         |
| go                         | 137 ms                                                          | 111 ms: 1.24x faster                                                          |
| xml_etree_generate         | 72.1 ms                                                         | 58.3 ms: 1.24x faster                                                         |
| async_tree_io_tg           | 677 ms                                                          | 549 ms: 1.23x faster                                                          |
| xml_etree_process          | 53.2 ms                                                         | 43.2 ms: 1.23x faster                                                         |
| richards_super             | 46.5 ms                                                         | 37.8 ms: 1.23x faster                                                         |
| meteor_contest             | 86.9 ms                                                         | 72.6 ms: 1.20x faster                                                         |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 460 ms: 1.19x faster                                                          |
| pycparser                  | 978 ms                                                          | 827 ms: 1.18x faster                                                          |
| coroutines                 | 20.9 ms                                                         | 17.7 ms: 1.18x faster                                                         |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 488 ms: 1.16x faster                                                          |
| sympy_sum                  | 123 ms                                                          | 108 ms: 1.14x faster                                                          |
| mdp                        | 1.91 sec                                                        | 1.67 sec: 1.14x faster                                                        |
| bench_thread_pool          | 1.10 ms                                                         | 976 us: 1.13x faster                                                          |
| 2to3                       | 280 ms                                                          | 249 ms: 1.13x faster                                                          |
| django_template            | 36.9 ms                                                         | 32.9 ms: 1.12x faster                                                         |
| sqlglot_optimize           | 48.5 ms                                                         | 43.2 ms: 1.12x faster                                                         |
| sympy_str                  | 240 ms                                                          | 214 ms: 1.12x faster                                                          |
| sympy_integrate            | 17.5 ms                                                         | 15.8 ms: 1.11x faster                                                         |
| xml_etree_parse            | 113 ms                                                          | 102 ms: 1.11x faster                                                          |
| pathlib                    | 91.4 ms                                                         | 82.8 ms: 1.10x faster                                                         |
| sqlite_synth               | 2.07 us                                                         | 1.90 us: 1.09x faster                                                         |
| asyncio_tcp                | 662 ms                                                          | 617 ms: 1.07x faster                                                          |
| tornado_http               | 105 ms                                                          | 97.8 ms: 1.07x faster                                                         |
| json_dumps                 | 7.40 ms                                                         | 7.01 ms: 1.06x faster                                                         |
| asyncio_tcp_ssl            | 17.7 sec                                                        | 16.9 sec: 1.05x faster                                                        |
| sympy_expand               | 398 ms                                                          | 381 ms: 1.05x faster                                                          |
| async_generators           | 313 ms                                                          | 302 ms: 1.04x faster                                                          |
| docutils                   | 1.98 sec                                                        | 1.92 sec: 1.03x faster                                                        |
| python_startup_no_site     | 19.1 ms                                                         | 18.6 ms: 1.03x faster                                                         |
| bench_mp_pool              | 75.4 ms                                                         | 73.5 ms: 1.03x faster                                                         |
| unpickle_list              | 2.95 us                                                         | 2.89 us: 1.02x faster                                                         |
| pidigits                   | 199 ms                                                          | 197 ms: 1.01x faster                                                          |
| json_loads                 | 20.4 us                                                         | 20.5 us: 1.01x slower                                                         |
| python_startup             | 22.4 ms                                                         | 22.8 ms: 1.02x slower                                                         |
| telco                      | 5.51 ms                                                         | 5.64 ms: 1.02x slower                                                         |
| pickle_dict                | 19.9 us                                                         | 20.6 us: 1.03x slower                                                         |
| regex_dna                  | 127 ms                                                          | 132 ms: 1.04x slower                                                          |
| unpickle                   | 9.71 us                                                         | 10.1 us: 1.04x slower                                                         |
| coverage                   | 48.4 ms                                                         | 50.9 ms: 1.05x slower                                                         |
| regex_v8                   | 15.0 ms                                                         | 16.0 ms: 1.06x slower                                                         |
| pickle_list                | 3.37 us                                                         | 3.60 us: 1.07x slower                                                         |
| pickle                     | 7.79 us                                                         | 8.35 us: 1.07x slower                                                         |
| typing_runtime_protocols   | 126 us                                                          | 142 us: 1.13x slower                                                          |
| create_gc_cycles           | 652 us                                                          | 759 us: 1.16x slower                                                          |
| sqlglot_normalize          | 100 ms                                                          | 236 ms: 2.35x slower                                                          |
| Geometric mean             | (ref)                                                           | 1.22x faster                                                                  |

Benchmark hidden because not significant (3): json, gc_traversal, regex_effbot
Ignored benchmarks (8) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, dulwich_log, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (5) of results/bm-20240618-3.14.0a0-a1bdb94-JIT/bm-20240618-pythonperf1_win32-x86-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94.json: genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.17x
- 95% likely to have a speedup of 1.16x
- 99% likely to have a speedup of 1.14x

# Memory
- memory change: unknown