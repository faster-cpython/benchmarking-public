# Results vs. 3.12.0

- fork: brandtbucher
- ref: justin_compact
- machine: windows-x86
- commit hash: 34e6994
- commit date: 2024-06-20
- overall geometric mean: 1.20x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.12x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240620-pythonperf1_win32-x86-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 257 ms: 1.09x faster                                                           |
| docutils       | 1.98 sec                                                        | 1.93 sec: 1.03x faster                                                         |
| tornado_http   | 105 ms                                                          | 97.8 ms: 1.07x faster                                                          |
| Geometric mean | (ref)                                                           | 1.06x faster                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240620-pythonperf1_win32-x86-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 350 ms                                                          | 269 ms: 1.30x faster                                                           |
| async_tree_none_tg         | 278 ms                                                          | 217 ms: 1.28x faster                                                           |
| async_tree_io_tg           | 677 ms                                                          | 541 ms: 1.25x faster                                                           |
| async_tree_io              | 693 ms                                                          | 559 ms: 1.24x faster                                                           |
| async_tree_memoization     | 364 ms                                                          | 295 ms: 1.23x faster                                                           |
| async_tree_none            | 298 ms                                                          | 242 ms: 1.23x faster                                                           |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 481 ms: 1.14x faster                                                           |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 498 ms: 1.13x faster                                                           |
| Geometric mean             | (ref)                                                           | 1.22x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240620-pythonperf1_win32-x86-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 54.4 ms: 2.33x faster                                                          |
| float          | 76.7 ms                                                         | 43.1 ms: 1.78x faster                                                          |
| pidigits       | 199 ms                                                          | 195 ms: 1.02x faster                                                           |
| Geometric mean | (ref)                                                           | 1.62x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240620-pythonperf1_win32-x86-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 93.6 ms: 1.38x faster                                                          |
| regex_dna      | 127 ms                                                          | 129 ms: 1.01x slower                                                           |
| regex_v8       | 15.0 ms                                                         | 16.0 ms: 1.06x slower                                                          |
| Geometric mean | (ref)                                                           | 1.06x faster                                                                   |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240620-pythonperf1_win32-x86-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| tomli_loads          | 2.20 sec                                                        | 1.50 sec: 1.46x faster                                                         |
| unpickle_pure_python | 210 us                                                          | 146 us: 1.44x faster                                                           |
| pickle_pure_python   | 286 us                                                          | 211 us: 1.36x faster                                                           |
| xml_etree_iterparse  | 77.6 ms                                                         | 61.9 ms: 1.25x faster                                                          |
| xml_etree_generate   | 72.1 ms                                                         | 57.8 ms: 1.25x faster                                                          |
| xml_etree_process    | 53.2 ms                                                         | 42.8 ms: 1.24x faster                                                          |
| xml_etree_parse      | 113 ms                                                          | 104 ms: 1.08x faster                                                           |
| json_dumps           | 7.40 ms                                                         | 6.87 ms: 1.08x faster                                                          |
| unpickle_list        | 2.95 us                                                         | 2.78 us: 1.06x faster                                                          |
| json_loads           | 20.4 us                                                         | 20.7 us: 1.02x slower                                                          |
| pickle_dict          | 19.9 us                                                         | 20.8 us: 1.04x slower                                                          |
| pickle               | 7.79 us                                                         | 8.28 us: 1.06x slower                                                          |
| unpickle             | 9.71 us                                                         | 10.3 us: 1.06x slower                                                          |
| pickle_list          | 3.37 us                                                         | 4.10 us: 1.22x slower                                                          |
| Geometric mean       | (ref)                                                           | 1.12x faster                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240620-pythonperf1_win32-x86-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 21.0 ms: 1.10x slower                                                          |
| python_startup         | 22.4 ms                                                         | 25.1 ms: 1.12x slower                                                          |
| Geometric mean         | (ref)                                                           | 1.11x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240620-pythonperf1_win32-x86-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 5.34 ms: 1.86x faster                                                          |
| django_template | 36.9 ms                                                         | 34.1 ms: 1.08x faster                                                          |
| Geometric mean  | (ref)                                                           | 1.42x faster                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240620-pythonperf1_win32-x86-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| deepcopy_memo              | 38.4 us                                                         | 15.8 us: 2.43x faster                                                          |
| nbody                      | 127 ms                                                          | 54.4 ms: 2.33x faster                                                          |
| spectral_norm              | 104 ms                                                          | 49.0 ms: 2.12x faster                                                          |
| mako                       | 9.96 ms                                                         | 5.34 ms: 1.86x faster                                                          |
| float                      | 76.7 ms                                                         | 43.1 ms: 1.78x faster                                                          |
| logging_silent             | 101 ns                                                          | 58.3 ns: 1.73x faster                                                          |
| comprehensions             | 19.2 us                                                         | 11.4 us: 1.68x faster                                                          |
| fannkuch                   | 354 ms                                                          | 213 ms: 1.66x faster                                                           |
| scimark_monte_carlo        | 66.4 ms                                                         | 41.2 ms: 1.61x faster                                                          |
| scimark_fft                | 271 ms                                                          | 170 ms: 1.59x faster                                                           |
| hexiom                     | 6.82 ms                                                         | 4.32 ms: 1.58x faster                                                          |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 2.48 ms: 1.56x faster                                                          |
| pyflate                    | 424 ms                                                          | 277 ms: 1.53x faster                                                           |
| deepcopy                   | 360 us                                                          | 238 us: 1.51x faster                                                           |
| tomli_loads                | 2.20 sec                                                        | 1.50 sec: 1.46x faster                                                         |
| unpickle_pure_python       | 210 us                                                          | 146 us: 1.44x faster                                                           |
| crypto_pyaes               | 69.2 ms                                                         | 48.5 ms: 1.43x faster                                                          |
| generators                 | 38.5 ms                                                         | 27.7 ms: 1.39x faster                                                          |
| regex_compile              | 129 ms                                                          | 93.6 ms: 1.38x faster                                                          |
| deepcopy_reduce            | 3.23 us                                                         | 2.35 us: 1.37x faster                                                          |
| pickle_pure_python         | 286 us                                                          | 211 us: 1.36x faster                                                           |
| sqlglot_parse              | 1.25 ms                                                         | 922 us: 1.35x faster                                                           |
| nqueens                    | 93.7 ms                                                         | 71.2 ms: 1.31x faster                                                          |
| scimark_sor                | 130 ms                                                          | 99.5 ms: 1.31x faster                                                          |
| async_tree_memoization_tg  | 350 ms                                                          | 269 ms: 1.30x faster                                                           |
| deltablue                  | 3.58 ms                                                         | 2.78 ms: 1.29x faster                                                          |
| sqlglot_transpile          | 1.53 ms                                                         | 1.19 ms: 1.29x faster                                                          |
| async_tree_none_tg         | 278 ms                                                          | 217 ms: 1.28x faster                                                           |
| raytrace                   | 308 ms                                                          | 241 ms: 1.28x faster                                                           |
| logging_simple             | 9.75 us                                                         | 7.65 us: 1.27x faster                                                          |
| xml_etree_iterparse        | 77.6 ms                                                         | 61.9 ms: 1.25x faster                                                          |
| logging_format             | 10.4 us                                                         | 8.31 us: 1.25x faster                                                          |
| async_tree_io_tg           | 677 ms                                                          | 541 ms: 1.25x faster                                                           |
| pprint_pformat             | 1.50 sec                                                        | 1.20 sec: 1.25x faster                                                         |
| xml_etree_generate         | 72.1 ms                                                         | 57.8 ms: 1.25x faster                                                          |
| xml_etree_process          | 53.2 ms                                                         | 42.8 ms: 1.24x faster                                                          |
| async_tree_io              | 693 ms                                                          | 559 ms: 1.24x faster                                                           |
| chaos                      | 69.4 ms                                                         | 56.1 ms: 1.24x faster                                                          |
| pprint_safe_repr           | 721 ms                                                          | 584 ms: 1.23x faster                                                           |
| async_tree_memoization     | 364 ms                                                          | 295 ms: 1.23x faster                                                           |
| async_tree_none            | 298 ms                                                          | 242 ms: 1.23x faster                                                           |
| scimark_lu                 | 93.2 ms                                                         | 75.9 ms: 1.23x faster                                                          |
| go                         | 137 ms                                                          | 114 ms: 1.21x faster                                                           |
| coroutines                 | 20.9 ms                                                         | 17.5 ms: 1.19x faster                                                          |
| meteor_contest             | 86.9 ms                                                         | 73.4 ms: 1.18x faster                                                          |
| richards_super             | 46.5 ms                                                         | 39.3 ms: 1.18x faster                                                          |
| pycparser                  | 978 ms                                                          | 831 ms: 1.18x faster                                                           |
| richards                   | 41.3 ms                                                         | 35.2 ms: 1.18x faster                                                          |
| mdp                        | 1.91 sec                                                        | 1.64 sec: 1.17x faster                                                         |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 481 ms: 1.14x faster                                                           |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 498 ms: 1.13x faster                                                           |
| bench_thread_pool          | 1.10 ms                                                         | 976 us: 1.13x faster                                                           |
| sympy_sum                  | 123 ms                                                          | 109 ms: 1.12x faster                                                           |
| sqlglot_optimize           | 48.5 ms                                                         | 43.2 ms: 1.12x faster                                                          |
| sympy_str                  | 240 ms                                                          | 217 ms: 1.10x faster                                                           |
| sympy_integrate            | 17.5 ms                                                         | 16.0 ms: 1.10x faster                                                          |
| pathlib                    | 91.4 ms                                                         | 83.3 ms: 1.10x faster                                                          |
| 2to3                       | 280 ms                                                          | 257 ms: 1.09x faster                                                           |
| xml_etree_parse            | 113 ms                                                          | 104 ms: 1.08x faster                                                           |
| sqlite_synth               | 2.07 us                                                         | 1.92 us: 1.08x faster                                                          |
| django_template            | 36.9 ms                                                         | 34.1 ms: 1.08x faster                                                          |
| json_dumps                 | 7.40 ms                                                         | 6.87 ms: 1.08x faster                                                          |
| tornado_http               | 105 ms                                                          | 97.8 ms: 1.07x faster                                                          |
| unpickle_list              | 2.95 us                                                         | 2.78 us: 1.06x faster                                                          |
| asyncio_tcp                | 662 ms                                                          | 629 ms: 1.05x faster                                                           |
| asyncio_tcp_ssl            | 17.7 sec                                                        | 16.9 sec: 1.05x faster                                                         |
| docutils                   | 1.98 sec                                                        | 1.93 sec: 1.03x faster                                                         |
| async_generators           | 313 ms                                                          | 305 ms: 1.03x faster                                                           |
| sympy_expand               | 398 ms                                                          | 389 ms: 1.02x faster                                                           |
| pidigits                   | 199 ms                                                          | 195 ms: 1.02x faster                                                           |
| bench_mp_pool              | 75.4 ms                                                         | 76.1 ms: 1.01x slower                                                          |
| regex_dna                  | 127 ms                                                          | 129 ms: 1.01x slower                                                           |
| gc_traversal               | 1.44 ms                                                         | 1.46 ms: 1.01x slower                                                          |
| json_loads                 | 20.4 us                                                         | 20.7 us: 1.02x slower                                                          |
| coverage                   | 48.4 ms                                                         | 49.6 ms: 1.02x slower                                                          |
| pickle_dict                | 19.9 us                                                         | 20.8 us: 1.04x slower                                                          |
| regex_v8                   | 15.0 ms                                                         | 16.0 ms: 1.06x slower                                                          |
| pickle                     | 7.79 us                                                         | 8.28 us: 1.06x slower                                                          |
| unpickle                   | 9.71 us                                                         | 10.3 us: 1.06x slower                                                          |
| json                       | 4.15 ms                                                         | 4.52 ms: 1.09x slower                                                          |
| telco                      | 5.51 ms                                                         | 6.04 ms: 1.10x slower                                                          |
| python_startup_no_site     | 19.1 ms                                                         | 21.0 ms: 1.10x slower                                                          |
| python_startup             | 22.4 ms                                                         | 25.1 ms: 1.12x slower                                                          |
| create_gc_cycles           | 652 us                                                          | 751 us: 1.15x slower                                                           |
| typing_runtime_protocols   | 126 us                                                          | 148 us: 1.17x slower                                                           |
| pickle_list                | 3.37 us                                                         | 4.10 us: 1.22x slower                                                          |
| sqlglot_normalize          | 100 ms                                                          | 233 ms: 2.32x slower                                                           |
| Geometric mean             | (ref)                                                           | 1.20x faster                                                                   |

Benchmark hidden because not significant (1): regex_effbot
Ignored benchmarks (8) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, dulwich_log, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (5) of results/bm-20240620-3.14.0a0-34e6994-JIT/bm-20240620-pythonperf1_win32-x86-brandtbucher-justin_compact-3.14.0a0-34e6994.json: genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.16x
- 95% likely to have a speedup of 1.14x
- 99% likely to have a speedup of 1.12x

# Memory
- memory change: unknown