# Results vs. 3.12.0

- fork: brandtbucher
- ref: no_cold_exits
- machine: windows-x86
- commit hash: f837cc6
- commit date: 2024-06-10
- overall geometric mean: 1.24x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.16x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240610-pythonperf1_win32-x86-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|----------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 244 ms: 1.15x faster                                                          |
| docutils       | 1.98 sec                                                        | 1.87 sec: 1.06x faster                                                        |
| tornado_http   | 105 ms                                                          | 97.0 ms: 1.08x faster                                                         |
| Geometric mean | (ref)                                                           | 1.10x faster                                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240610-pythonperf1_win32-x86-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|----------------------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_none_tg         | 278 ms                                                          | 206 ms: 1.35x faster                                                          |
| async_tree_memoization_tg  | 350 ms                                                          | 261 ms: 1.34x faster                                                          |
| async_tree_io              | 693 ms                                                          | 527 ms: 1.31x faster                                                          |
| async_tree_memoization     | 364 ms                                                          | 278 ms: 1.31x faster                                                          |
| async_tree_none            | 298 ms                                                          | 228 ms: 1.30x faster                                                          |
| async_tree_io_tg           | 677 ms                                                          | 533 ms: 1.27x faster                                                          |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 464 ms: 1.18x faster                                                          |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 479 ms: 1.18x faster                                                          |
| Geometric mean             | (ref)                                                           | 1.28x faster                                                                  |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240610-pythonperf1_win32-x86-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|----------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 52.6 ms: 2.41x faster                                                         |
| float          | 76.7 ms                                                         | 41.6 ms: 1.84x faster                                                         |
| pidigits       | 199 ms                                                          | 195 ms: 1.02x faster                                                          |
| Geometric mean | (ref)                                                           | 1.66x faster                                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240610-pythonperf1_win32-x86-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|----------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 96.3 ms: 1.34x faster                                                         |
| regex_effbot   | 2.04 ms                                                         | 1.99 ms: 1.02x faster                                                         |
| regex_dna      | 127 ms                                                          | 124 ms: 1.02x faster                                                          |
| regex_v8       | 15.0 ms                                                         | 15.9 ms: 1.06x slower                                                         |
| Geometric mean | (ref)                                                           | 1.07x faster                                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240610-pythonperf1_win32-x86-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|----------------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| tomli_loads          | 2.20 sec                                                        | 1.39 sec: 1.58x faster                                                        |
| unpickle_pure_python | 210 us                                                          | 135 us: 1.56x faster                                                          |
| pickle_pure_python   | 286 us                                                          | 201 us: 1.42x faster                                                          |
| xml_etree_generate   | 72.1 ms                                                         | 54.5 ms: 1.32x faster                                                         |
| xml_etree_process    | 53.2 ms                                                         | 40.2 ms: 1.32x faster                                                         |
| xml_etree_iterparse  | 77.6 ms                                                         | 61.1 ms: 1.27x faster                                                         |
| xml_etree_parse      | 113 ms                                                          | 99.5 ms: 1.14x faster                                                         |
| json_dumps           | 7.40 ms                                                         | 6.66 ms: 1.11x faster                                                         |
| unpickle_list        | 2.95 us                                                         | 2.76 us: 1.07x faster                                                         |
| json_loads           | 20.4 us                                                         | 20.7 us: 1.02x slower                                                         |
| pickle_dict          | 19.9 us                                                         | 20.9 us: 1.05x slower                                                         |
| pickle               | 7.79 us                                                         | 8.24 us: 1.06x slower                                                         |
| unpickle             | 9.71 us                                                         | 10.3 us: 1.06x slower                                                         |
| pickle_list          | 3.37 us                                                         | 3.58 us: 1.06x slower                                                         |
| Geometric mean       | (ref)                                                           | 1.16x faster                                                                  |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240610-pythonperf1_win32-x86-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|------------------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 18.5 ms: 1.03x faster                                                         |
| python_startup         | 22.4 ms                                                         | 22.9 ms: 1.02x slower                                                         |
| Geometric mean         | (ref)                                                           | 1.00x faster                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240610-pythonperf1_win32-x86-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|-----------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 5.33 ms: 1.87x faster                                                         |
| django_template | 36.9 ms                                                         | 31.7 ms: 1.16x faster                                                         |
| Geometric mean  | (ref)                                                           | 1.47x faster                                                                  |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240610-pythonperf1_win32-x86-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|----------------------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| nbody                      | 127 ms                                                          | 52.6 ms: 2.41x faster                                                         |
| spectral_norm              | 104 ms                                                          | 47.9 ms: 2.17x faster                                                         |
| deepcopy_memo              | 38.4 us                                                         | 20.0 us: 1.92x faster                                                         |
| mako                       | 9.96 ms                                                         | 5.33 ms: 1.87x faster                                                         |
| logging_silent             | 101 ns                                                          | 54.8 ns: 1.85x faster                                                         |
| float                      | 76.7 ms                                                         | 41.6 ms: 1.84x faster                                                         |
| comprehensions             | 19.2 us                                                         | 11.3 us: 1.69x faster                                                         |
| fannkuch                   | 354 ms                                                          | 211 ms: 1.67x faster                                                          |
| scimark_monte_carlo        | 66.4 ms                                                         | 39.9 ms: 1.66x faster                                                         |
| scimark_fft                | 271 ms                                                          | 163 ms: 1.66x faster                                                          |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 2.34 ms: 1.65x faster                                                         |
| generators                 | 38.5 ms                                                         | 23.5 ms: 1.64x faster                                                         |
| tomli_loads                | 2.20 sec                                                        | 1.39 sec: 1.58x faster                                                        |
| pyflate                    | 424 ms                                                          | 270 ms: 1.57x faster                                                          |
| unpickle_pure_python       | 210 us                                                          | 135 us: 1.56x faster                                                          |
| hexiom                     | 6.82 ms                                                         | 4.45 ms: 1.53x faster                                                         |
| scimark_sor                | 130 ms                                                          | 87.6 ms: 1.48x faster                                                         |
| raytrace                   | 308 ms                                                          | 213 ms: 1.45x faster                                                          |
| crypto_pyaes               | 69.2 ms                                                         | 48.5 ms: 1.43x faster                                                         |
| deltablue                  | 3.58 ms                                                         | 2.51 ms: 1.43x faster                                                         |
| pickle_pure_python         | 286 us                                                          | 201 us: 1.42x faster                                                          |
| richards                   | 41.3 ms                                                         | 29.2 ms: 1.41x faster                                                         |
| richards_super             | 46.5 ms                                                         | 33.3 ms: 1.40x faster                                                         |
| nqueens                    | 93.7 ms                                                         | 67.4 ms: 1.39x faster                                                         |
| sqlglot_parse              | 1.25 ms                                                         | 899 us: 1.39x faster                                                          |
| logging_simple             | 9.75 us                                                         | 7.21 us: 1.35x faster                                                         |
| chaos                      | 69.4 ms                                                         | 51.3 ms: 1.35x faster                                                         |
| async_tree_none_tg         | 278 ms                                                          | 206 ms: 1.35x faster                                                          |
| async_tree_memoization_tg  | 350 ms                                                          | 261 ms: 1.34x faster                                                          |
| coroutines                 | 20.9 ms                                                         | 15.6 ms: 1.34x faster                                                         |
| regex_compile              | 129 ms                                                          | 96.3 ms: 1.34x faster                                                         |
| logging_format             | 10.4 us                                                         | 7.82 us: 1.33x faster                                                         |
| xml_etree_generate         | 72.1 ms                                                         | 54.5 ms: 1.32x faster                                                         |
| pprint_pformat             | 1.50 sec                                                        | 1.13 sec: 1.32x faster                                                        |
| xml_etree_process          | 53.2 ms                                                         | 40.2 ms: 1.32x faster                                                         |
| sqlglot_transpile          | 1.53 ms                                                         | 1.16 ms: 1.32x faster                                                         |
| async_tree_io              | 693 ms                                                          | 527 ms: 1.31x faster                                                          |
| scimark_lu                 | 93.2 ms                                                         | 71.1 ms: 1.31x faster                                                         |
| pprint_safe_repr           | 721 ms                                                          | 550 ms: 1.31x faster                                                          |
| async_tree_memoization     | 364 ms                                                          | 278 ms: 1.31x faster                                                          |
| async_tree_none            | 298 ms                                                          | 228 ms: 1.30x faster                                                          |
| async_tree_io_tg           | 677 ms                                                          | 533 ms: 1.27x faster                                                          |
| xml_etree_iterparse        | 77.6 ms                                                         | 61.1 ms: 1.27x faster                                                         |
| go                         | 137 ms                                                          | 111 ms: 1.24x faster                                                          |
| pycparser                  | 978 ms                                                          | 795 ms: 1.23x faster                                                          |
| mdp                        | 1.91 sec                                                        | 1.59 sec: 1.20x faster                                                        |
| deepcopy                   | 360 us                                                          | 300 us: 1.20x faster                                                          |
| meteor_contest             | 86.9 ms                                                         | 72.3 ms: 1.20x faster                                                         |
| deepcopy_reduce            | 3.23 us                                                         | 2.74 us: 1.18x faster                                                         |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 464 ms: 1.18x faster                                                          |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 479 ms: 1.18x faster                                                          |
| sqlglot_optimize           | 48.5 ms                                                         | 41.7 ms: 1.16x faster                                                         |
| django_template            | 36.9 ms                                                         | 31.7 ms: 1.16x faster                                                         |
| 2to3                       | 280 ms                                                          | 244 ms: 1.15x faster                                                          |
| sympy_sum                  | 123 ms                                                          | 108 ms: 1.14x faster                                                          |
| xml_etree_parse            | 113 ms                                                          | 99.5 ms: 1.14x faster                                                         |
| sympy_str                  | 240 ms                                                          | 211 ms: 1.13x faster                                                          |
| sympy_integrate            | 17.5 ms                                                         | 15.5 ms: 1.13x faster                                                         |
| bench_thread_pool          | 1.10 ms                                                         | 976 us: 1.13x faster                                                          |
| json_dumps                 | 7.40 ms                                                         | 6.66 ms: 1.11x faster                                                         |
| pathlib                    | 91.4 ms                                                         | 82.7 ms: 1.11x faster                                                         |
| tornado_http               | 105 ms                                                          | 97.0 ms: 1.08x faster                                                         |
| sqlite_synth               | 2.07 us                                                         | 1.92 us: 1.08x faster                                                         |
| unpickle_list              | 2.95 us                                                         | 2.76 us: 1.07x faster                                                         |
| sympy_expand               | 398 ms                                                          | 374 ms: 1.06x faster                                                          |
| docutils                   | 1.98 sec                                                        | 1.87 sec: 1.06x faster                                                        |
| asyncio_tcp                | 662 ms                                                          | 626 ms: 1.06x faster                                                          |
| telco                      | 5.51 ms                                                         | 5.23 ms: 1.05x faster                                                         |
| asyncio_tcp_ssl            | 17.7 sec                                                        | 16.8 sec: 1.05x faster                                                        |
| async_generators           | 313 ms                                                          | 301 ms: 1.04x faster                                                          |
| bench_mp_pool              | 75.4 ms                                                         | 73.0 ms: 1.03x faster                                                         |
| python_startup_no_site     | 19.1 ms                                                         | 18.5 ms: 1.03x faster                                                         |
| pidigits                   | 199 ms                                                          | 195 ms: 1.02x faster                                                          |
| regex_effbot               | 2.04 ms                                                         | 1.99 ms: 1.02x faster                                                         |
| regex_dna                  | 127 ms                                                          | 124 ms: 1.02x faster                                                          |
| gc_traversal               | 1.44 ms                                                         | 1.46 ms: 1.01x slower                                                         |
| json_loads                 | 20.4 us                                                         | 20.7 us: 1.02x slower                                                         |
| python_startup             | 22.4 ms                                                         | 22.9 ms: 1.02x slower                                                         |
| json                       | 4.15 ms                                                         | 4.30 ms: 1.04x slower                                                         |
| pickle_dict                | 19.9 us                                                         | 20.9 us: 1.05x slower                                                         |
| regex_v8                   | 15.0 ms                                                         | 15.9 ms: 1.06x slower                                                         |
| pickle                     | 7.79 us                                                         | 8.24 us: 1.06x slower                                                         |
| unpickle                   | 9.71 us                                                         | 10.3 us: 1.06x slower                                                         |
| pickle_list                | 3.37 us                                                         | 3.58 us: 1.06x slower                                                         |
| typing_runtime_protocols   | 126 us                                                          | 146 us: 1.15x slower                                                          |
| create_gc_cycles           | 652 us                                                          | 755 us: 1.16x slower                                                          |
| sqlglot_normalize          | 100 ms                                                          | 219 ms: 2.18x slower                                                          |
| Geometric mean             | (ref)                                                           | 1.24x faster                                                                  |

Benchmark hidden because not significant (1): coverage
Ignored benchmarks (8) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, dulwich_log, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (5) of results/bm-20240610-3.14.0a0-f837cc6-JIT/bm-20240610-pythonperf1_win32-x86-brandtbucher-no_cold_exits-3.14.0a0-f837cc6.json: genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.20x
- 95% likely to have a speedup of 1.20x
- 99% likely to have a speedup of 1.16x

# Memory
- memory change: unknown