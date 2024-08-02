# Results vs. 3.12.0

- fork: python
- ref: 5b941e57c71d7d0ab983
- machine: windows-x86
- commit hash: 5b941e5
- commit date: 2024-05-11
- overall geometric mean: 1.14x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.11x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240511-pythonperf1_win32-x86-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 255 ms: 1.10x faster                                                           |
| chameleon      | 7.75 ms                                                         | 6.18 ms: 1.25x faster                                                          |
| docutils       | 1.98 sec                                                        | 2.01 sec: 1.01x slower                                                         |
| tornado_http   | 105 ms                                                          | 99.3 ms: 1.06x faster                                                          |
| Geometric mean | (ref)                                                           | 1.10x faster                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240511-pythonperf1_win32-x86-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 350 ms                                                          | 263 ms: 1.33x faster                                                           |
| async_tree_none_tg         | 278 ms                                                          | 210 ms: 1.32x faster                                                           |
| async_tree_memoization     | 364 ms                                                          | 283 ms: 1.28x faster                                                           |
| async_tree_io              | 693 ms                                                          | 542 ms: 1.28x faster                                                           |
| async_tree_none            | 298 ms                                                          | 234 ms: 1.27x faster                                                           |
| async_tree_io_tg           | 677 ms                                                          | 540 ms: 1.25x faster                                                           |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 444 ms: 1.23x faster                                                           |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 472 ms: 1.19x faster                                                           |
| Geometric mean             | (ref)                                                           | 1.27x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240511-pythonperf1_win32-x86-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 75.9 ms: 1.67x faster                                                          |
| float          | 76.7 ms                                                         | 51.9 ms: 1.48x faster                                                          |
| pidigits       | 199 ms                                                          | 198 ms: 1.00x faster                                                           |
| Geometric mean | (ref)                                                           | 1.35x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240511-pythonperf1_win32-x86-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_effbot   | 2.04 ms                                                         | 1.91 ms: 1.07x faster                                                          |
| regex_dna      | 127 ms                                                          | 120 ms: 1.06x faster                                                           |
| regex_compile  | 129 ms                                                          | 123 ms: 1.05x faster                                                           |
| regex_v8       | 15.0 ms                                                         | 16.1 ms: 1.07x slower                                                          |
| Geometric mean | (ref)                                                           | 1.03x faster                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240511-pythonperf1_win32-x86-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| tomli_loads          | 2.20 sec                                                        | 1.61 sec: 1.37x faster                                                         |
| unpickle_pure_python | 210 us                                                          | 168 us: 1.25x faster                                                           |
| xml_etree_process    | 53.2 ms                                                         | 43.2 ms: 1.23x faster                                                          |
| xml_etree_iterparse  | 77.6 ms                                                         | 64.7 ms: 1.20x faster                                                          |
| xml_etree_generate   | 72.1 ms                                                         | 60.3 ms: 1.20x faster                                                          |
| pickle_pure_python   | 286 us                                                          | 243 us: 1.18x faster                                                           |
| xml_etree_parse      | 113 ms                                                          | 104 ms: 1.09x faster                                                           |
| json_dumps           | 7.40 ms                                                         | 6.92 ms: 1.07x faster                                                          |
| json_loads           | 20.4 us                                                         | 20.7 us: 1.02x slower                                                          |
| unpickle_list        | 2.95 us                                                         | 3.02 us: 1.03x slower                                                          |
| pickle_dict          | 19.9 us                                                         | 20.7 us: 1.04x slower                                                          |
| pickle               | 7.79 us                                                         | 8.17 us: 1.05x slower                                                          |
| unpickle             | 9.71 us                                                         | 10.3 us: 1.06x slower                                                          |
| pickle_list          | 3.37 us                                                         | 3.58 us: 1.06x slower                                                          |
| Geometric mean       | (ref)                                                           | 1.09x faster                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240511-pythonperf1_win32-x86-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup | 22.4 ms                                                         | 23.0 ms: 1.03x slower                                                          |
| Geometric mean | (ref)                                                           | 1.02x slower                                                                   |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240511-pythonperf1_win32-x86-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 7.08 ms: 1.41x faster                                                          |
| django_template | 36.9 ms                                                         | 32.2 ms: 1.15x faster                                                          |
| Geometric mean  | (ref)                                                           | 1.27x faster                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240511-pythonperf1_win32-x86-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| nbody                      | 127 ms                                                          | 75.9 ms: 1.67x faster                                                          |
| generators                 | 38.5 ms                                                         | 23.2 ms: 1.66x faster                                                          |
| float                      | 76.7 ms                                                         | 51.9 ms: 1.48x faster                                                          |
| raytrace                   | 308 ms                                                          | 209 ms: 1.48x faster                                                           |
| comprehensions             | 19.2 us                                                         | 13.3 us: 1.44x faster                                                          |
| spectral_norm              | 104 ms                                                          | 72.3 ms: 1.44x faster                                                          |
| mako                       | 9.96 ms                                                         | 7.08 ms: 1.41x faster                                                          |
| deepcopy_memo              | 38.4 us                                                         | 27.6 us: 1.39x faster                                                          |
| scimark_sor                | 130 ms                                                          | 93.5 ms: 1.39x faster                                                          |
| tomli_loads                | 2.20 sec                                                        | 1.61 sec: 1.37x faster                                                         |
| logging_silent             | 101 ns                                                          | 74.1 ns: 1.36x faster                                                          |
| scimark_fft                | 271 ms                                                          | 202 ms: 1.34x faster                                                           |
| async_tree_memoization_tg  | 350 ms                                                          | 263 ms: 1.33x faster                                                           |
| richards                   | 41.3 ms                                                         | 31.0 ms: 1.33x faster                                                          |
| async_tree_none_tg         | 278 ms                                                          | 210 ms: 1.32x faster                                                           |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 2.94 ms: 1.31x faster                                                          |
| scimark_monte_carlo        | 66.4 ms                                                         | 50.8 ms: 1.31x faster                                                          |
| richards_super             | 46.5 ms                                                         | 35.5 ms: 1.31x faster                                                          |
| chaos                      | 69.4 ms                                                         | 53.4 ms: 1.30x faster                                                          |
| async_tree_memoization     | 364 ms                                                          | 283 ms: 1.28x faster                                                           |
| async_tree_io              | 693 ms                                                          | 542 ms: 1.28x faster                                                           |
| fannkuch                   | 354 ms                                                          | 276 ms: 1.28x faster                                                           |
| coroutines                 | 20.9 ms                                                         | 16.4 ms: 1.28x faster                                                          |
| async_tree_none            | 298 ms                                                          | 234 ms: 1.27x faster                                                           |
| logging_simple             | 9.75 us                                                         | 7.70 us: 1.27x faster                                                          |
| deltablue                  | 3.58 ms                                                         | 2.84 ms: 1.26x faster                                                          |
| async_tree_io_tg           | 677 ms                                                          | 540 ms: 1.25x faster                                                           |
| chameleon                  | 7.75 ms                                                         | 6.18 ms: 1.25x faster                                                          |
| sqlglot_parse              | 1.25 ms                                                         | 997 us: 1.25x faster                                                           |
| logging_format             | 10.4 us                                                         | 8.32 us: 1.25x faster                                                          |
| unpickle_pure_python       | 210 us                                                          | 168 us: 1.25x faster                                                           |
| xml_etree_process          | 53.2 ms                                                         | 43.2 ms: 1.23x faster                                                          |
| sqlglot_transpile          | 1.53 ms                                                         | 1.24 ms: 1.23x faster                                                          |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 444 ms: 1.23x faster                                                           |
| go                         | 137 ms                                                          | 113 ms: 1.21x faster                                                           |
| scimark_lu                 | 93.2 ms                                                         | 77.3 ms: 1.21x faster                                                          |
| xml_etree_iterparse        | 77.6 ms                                                         | 64.7 ms: 1.20x faster                                                          |
| deepcopy                   | 360 us                                                          | 301 us: 1.20x faster                                                           |
| xml_etree_generate         | 72.1 ms                                                         | 60.3 ms: 1.20x faster                                                          |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 472 ms: 1.19x faster                                                           |
| hexiom                     | 6.82 ms                                                         | 5.72 ms: 1.19x faster                                                          |
| nqueens                    | 93.7 ms                                                         | 79.0 ms: 1.18x faster                                                          |
| crypto_pyaes               | 69.2 ms                                                         | 58.5 ms: 1.18x faster                                                          |
| deepcopy_reduce            | 3.23 us                                                         | 2.73 us: 1.18x faster                                                          |
| mdp                        | 1.91 sec                                                        | 1.62 sec: 1.18x faster                                                         |
| pickle_pure_python         | 286 us                                                          | 243 us: 1.18x faster                                                           |
| pyflate                    | 424 ms                                                          | 360 ms: 1.18x faster                                                           |
| pprint_pformat             | 1.50 sec                                                        | 1.29 sec: 1.16x faster                                                         |
| django_template            | 36.9 ms                                                         | 32.2 ms: 1.15x faster                                                          |
| pprint_safe_repr           | 721 ms                                                          | 630 ms: 1.14x faster                                                           |
| pycparser                  | 978 ms                                                          | 854 ms: 1.14x faster                                                           |
| meteor_contest             | 86.9 ms                                                         | 77.7 ms: 1.12x faster                                                          |
| sqlglot_optimize           | 48.5 ms                                                         | 43.6 ms: 1.11x faster                                                          |
| 2to3                       | 280 ms                                                          | 255 ms: 1.10x faster                                                           |
| xml_etree_parse            | 113 ms                                                          | 104 ms: 1.09x faster                                                           |
| sqlite_synth               | 2.07 us                                                         | 1.92 us: 1.08x faster                                                          |
| json_dumps                 | 7.40 ms                                                         | 6.92 ms: 1.07x faster                                                          |
| regex_effbot               | 2.04 ms                                                         | 1.91 ms: 1.07x faster                                                          |
| sympy_integrate            | 17.5 ms                                                         | 16.5 ms: 1.06x faster                                                          |
| async_generators           | 313 ms                                                          | 295 ms: 1.06x faster                                                           |
| regex_dna                  | 127 ms                                                          | 120 ms: 1.06x faster                                                           |
| tornado_http               | 105 ms                                                          | 99.3 ms: 1.06x faster                                                          |
| bench_thread_pool          | 1.10 ms                                                         | 1.05 ms: 1.05x faster                                                          |
| pathlib                    | 91.4 ms                                                         | 87.3 ms: 1.05x faster                                                          |
| regex_compile              | 129 ms                                                          | 123 ms: 1.05x faster                                                           |
| sympy_sum                  | 123 ms                                                          | 118 ms: 1.04x faster                                                           |
| asyncio_tcp_ssl            | 17.7 sec                                                        | 17.0 sec: 1.04x faster                                                         |
| bench_mp_pool              | 75.4 ms                                                         | 72.7 ms: 1.04x faster                                                          |
| pidigits                   | 199 ms                                                          | 198 ms: 1.00x faster                                                           |
| sympy_str                  | 240 ms                                                          | 238 ms: 1.00x faster                                                           |
| docutils                   | 1.98 sec                                                        | 2.01 sec: 1.01x slower                                                         |
| json_loads                 | 20.4 us                                                         | 20.7 us: 1.02x slower                                                          |
| json                       | 4.15 ms                                                         | 4.23 ms: 1.02x slower                                                          |
| coverage                   | 48.4 ms                                                         | 49.7 ms: 1.03x slower                                                          |
| unpickle_list              | 2.95 us                                                         | 3.02 us: 1.03x slower                                                          |
| python_startup             | 22.4 ms                                                         | 23.0 ms: 1.03x slower                                                          |
| pickle_dict                | 19.9 us                                                         | 20.7 us: 1.04x slower                                                          |
| pickle                     | 7.79 us                                                         | 8.17 us: 1.05x slower                                                          |
| unpickle                   | 9.71 us                                                         | 10.3 us: 1.06x slower                                                          |
| pickle_list                | 3.37 us                                                         | 3.58 us: 1.06x slower                                                          |
| sympy_expand               | 398 ms                                                          | 423 ms: 1.06x slower                                                           |
| regex_v8                   | 15.0 ms                                                         | 16.1 ms: 1.07x slower                                                          |
| asyncio_tcp                | 662 ms                                                          | 711 ms: 1.07x slower                                                           |
| telco                      | 5.51 ms                                                         | 6.08 ms: 1.10x slower                                                          |
| create_gc_cycles           | 652 us                                                          | 758 us: 1.16x slower                                                           |
| typing_runtime_protocols   | 126 us                                                          | 149 us: 1.18x slower                                                           |
| sqlglot_normalize          | 100 ms                                                          | 226 ms: 2.25x slower                                                           |
| Geometric mean             | (ref)                                                           | 1.14x faster                                                                   |

Benchmark hidden because not significant (2): gc_traversal, python_startup_no_site
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, dask, dulwich_log, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (6) of results/bm-20240511-3.14.0a0-5b941e5-PYTHON_UOPS/bm-20240511-pythonperf1_win32-x86-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5.json: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.14x
- 95% likely to have a speedup of 1.13x
- 99% likely to have a speedup of 1.11x

# Memory
- memory change: unknown