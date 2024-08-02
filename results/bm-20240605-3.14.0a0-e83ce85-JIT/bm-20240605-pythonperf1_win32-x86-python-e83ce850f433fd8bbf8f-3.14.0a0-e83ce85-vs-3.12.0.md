# Results vs. 3.12.0

- fork: python
- ref: e83ce850f433fd8bbf8f
- machine: windows-x86
- commit hash: e83ce85
- commit date: 2024-06-05
- overall geometric mean: 1.24x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.16x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240605-pythonperf1_win32-x86-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 242 ms: 1.16x faster                                                           |
| docutils       | 1.98 sec                                                        | 1.85 sec: 1.07x faster                                                         |
| tornado_http   | 105 ms                                                          | 96.4 ms: 1.09x faster                                                          |
| Geometric mean | (ref)                                                           | 1.11x faster                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240605-pythonperf1_win32-x86-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 350 ms                                                          | 261 ms: 1.34x faster                                                           |
| async_tree_none_tg         | 278 ms                                                          | 207 ms: 1.34x faster                                                           |
| async_tree_memoization     | 364 ms                                                          | 280 ms: 1.30x faster                                                           |
| async_tree_io              | 693 ms                                                          | 534 ms: 1.30x faster                                                           |
| async_tree_none            | 298 ms                                                          | 230 ms: 1.30x faster                                                           |
| async_tree_io_tg           | 677 ms                                                          | 537 ms: 1.26x faster                                                           |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 484 ms: 1.13x faster                                                           |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 504 ms: 1.12x faster                                                           |
| Geometric mean             | (ref)                                                           | 1.26x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240605-pythonperf1_win32-x86-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 52.9 ms: 2.40x faster                                                          |
| float          | 76.7 ms                                                         | 41.4 ms: 1.85x faster                                                          |
| pidigits       | 199 ms                                                          | 198 ms: 1.01x faster                                                           |
| Geometric mean | (ref)                                                           | 1.65x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240605-pythonperf1_win32-x86-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 96.7 ms: 1.33x faster                                                          |
| regex_dna      | 127 ms                                                          | 123 ms: 1.03x faster                                                           |
| regex_effbot   | 2.04 ms                                                         | 1.98 ms: 1.03x faster                                                          |
| regex_v8       | 15.0 ms                                                         | 15.9 ms: 1.05x slower                                                          |
| Geometric mean | (ref)                                                           | 1.08x faster                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240605-pythonperf1_win32-x86-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| unpickle_pure_python | 210 us                                                          | 135 us: 1.55x faster                                                           |
| tomli_loads          | 2.20 sec                                                        | 1.43 sec: 1.54x faster                                                         |
| pickle_pure_python   | 286 us                                                          | 199 us: 1.44x faster                                                           |
| xml_etree_process    | 53.2 ms                                                         | 40.4 ms: 1.32x faster                                                          |
| xml_etree_generate   | 72.1 ms                                                         | 55.2 ms: 1.31x faster                                                          |
| xml_etree_iterparse  | 77.6 ms                                                         | 61.2 ms: 1.27x faster                                                          |
| json_dumps           | 7.40 ms                                                         | 6.51 ms: 1.14x faster                                                          |
| xml_etree_parse      | 113 ms                                                          | 102 ms: 1.10x faster                                                           |
| unpickle_list        | 2.95 us                                                         | 2.90 us: 1.02x faster                                                          |
| json_loads           | 20.4 us                                                         | 20.7 us: 1.02x slower                                                          |
| pickle_dict          | 19.9 us                                                         | 20.7 us: 1.04x slower                                                          |
| pickle               | 7.79 us                                                         | 8.23 us: 1.06x slower                                                          |
| unpickle             | 9.71 us                                                         | 10.5 us: 1.08x slower                                                          |
| pickle_list          | 3.37 us                                                         | 3.72 us: 1.11x slower                                                          |
| Geometric mean       | (ref)                                                           | 1.15x faster                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240605-pythonperf1_win32-x86-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 20.2 ms: 1.06x slower                                                          |
| python_startup         | 22.4 ms                                                         | 24.2 ms: 1.08x slower                                                          |
| Geometric mean         | (ref)                                                           | 1.07x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240605-pythonperf1_win32-x86-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 5.34 ms: 1.86x faster                                                          |
| django_template | 36.9 ms                                                         | 31.7 ms: 1.16x faster                                                          |
| Geometric mean  | (ref)                                                           | 1.47x faster                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240605-pythonperf1_win32-x86-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| nbody                      | 127 ms                                                          | 52.9 ms: 2.40x faster                                                          |
| spectral_norm              | 104 ms                                                          | 47.6 ms: 2.18x faster                                                          |
| logging_silent             | 101 ns                                                          | 53.9 ns: 1.87x faster                                                          |
| mako                       | 9.96 ms                                                         | 5.34 ms: 1.86x faster                                                          |
| deepcopy_memo              | 38.4 us                                                         | 20.7 us: 1.86x faster                                                          |
| float                      | 76.7 ms                                                         | 41.4 ms: 1.85x faster                                                          |
| comprehensions             | 19.2 us                                                         | 11.0 us: 1.74x faster                                                          |
| generators                 | 38.5 ms                                                         | 23.0 ms: 1.67x faster                                                          |
| scimark_monte_carlo        | 66.4 ms                                                         | 39.8 ms: 1.67x faster                                                          |
| scimark_fft                | 271 ms                                                          | 164 ms: 1.65x faster                                                           |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 2.34 ms: 1.65x faster                                                          |
| fannkuch                   | 354 ms                                                          | 219 ms: 1.61x faster                                                           |
| pyflate                    | 424 ms                                                          | 271 ms: 1.57x faster                                                           |
| unpickle_pure_python       | 210 us                                                          | 135 us: 1.55x faster                                                           |
| tomli_loads                | 2.20 sec                                                        | 1.43 sec: 1.54x faster                                                         |
| hexiom                     | 6.82 ms                                                         | 4.53 ms: 1.50x faster                                                          |
| raytrace                   | 308 ms                                                          | 205 ms: 1.50x faster                                                           |
| crypto_pyaes               | 69.2 ms                                                         | 47.9 ms: 1.45x faster                                                          |
| pickle_pure_python         | 286 us                                                          | 199 us: 1.44x faster                                                           |
| scimark_sor                | 130 ms                                                          | 90.4 ms: 1.44x faster                                                          |
| deltablue                  | 3.58 ms                                                         | 2.54 ms: 1.41x faster                                                          |
| sqlglot_parse              | 1.25 ms                                                         | 900 us: 1.39x faster                                                           |
| chaos                      | 69.4 ms                                                         | 50.1 ms: 1.38x faster                                                          |
| async_tree_memoization_tg  | 350 ms                                                          | 261 ms: 1.34x faster                                                           |
| async_tree_none_tg         | 278 ms                                                          | 207 ms: 1.34x faster                                                           |
| logging_simple             | 9.75 us                                                         | 7.27 us: 1.34x faster                                                          |
| regex_compile              | 129 ms                                                          | 96.7 ms: 1.33x faster                                                          |
| nqueens                    | 93.7 ms                                                         | 70.2 ms: 1.33x faster                                                          |
| coroutines                 | 20.9 ms                                                         | 15.7 ms: 1.33x faster                                                          |
| richards_super             | 46.5 ms                                                         | 35.1 ms: 1.32x faster                                                          |
| sqlglot_transpile          | 1.53 ms                                                         | 1.16 ms: 1.32x faster                                                          |
| pprint_pformat             | 1.50 sec                                                        | 1.13 sec: 1.32x faster                                                         |
| richards                   | 41.3 ms                                                         | 31.3 ms: 1.32x faster                                                          |
| pprint_safe_repr           | 721 ms                                                          | 546 ms: 1.32x faster                                                           |
| xml_etree_process          | 53.2 ms                                                         | 40.4 ms: 1.32x faster                                                          |
| logging_format             | 10.4 us                                                         | 7.92 us: 1.31x faster                                                          |
| scimark_lu                 | 93.2 ms                                                         | 71.1 ms: 1.31x faster                                                          |
| xml_etree_generate         | 72.1 ms                                                         | 55.2 ms: 1.31x faster                                                          |
| async_tree_memoization     | 364 ms                                                          | 280 ms: 1.30x faster                                                           |
| async_tree_io              | 693 ms                                                          | 534 ms: 1.30x faster                                                           |
| async_tree_none            | 298 ms                                                          | 230 ms: 1.30x faster                                                           |
| xml_etree_iterparse        | 77.6 ms                                                         | 61.2 ms: 1.27x faster                                                          |
| async_tree_io_tg           | 677 ms                                                          | 537 ms: 1.26x faster                                                           |
| go                         | 137 ms                                                          | 109 ms: 1.25x faster                                                           |
| pycparser                  | 978 ms                                                          | 798 ms: 1.22x faster                                                           |
| deepcopy                   | 360 us                                                          | 300 us: 1.20x faster                                                           |
| meteor_contest             | 86.9 ms                                                         | 72.3 ms: 1.20x faster                                                          |
| deepcopy_reduce            | 3.23 us                                                         | 2.74 us: 1.18x faster                                                          |
| mdp                        | 1.91 sec                                                        | 1.63 sec: 1.18x faster                                                         |
| sqlglot_optimize           | 48.5 ms                                                         | 41.3 ms: 1.17x faster                                                          |
| django_template            | 36.9 ms                                                         | 31.7 ms: 1.16x faster                                                          |
| 2to3                       | 280 ms                                                          | 242 ms: 1.16x faster                                                           |
| sympy_sum                  | 123 ms                                                          | 106 ms: 1.16x faster                                                           |
| sympy_str                  | 240 ms                                                          | 208 ms: 1.15x faster                                                           |
| json_dumps                 | 7.40 ms                                                         | 6.51 ms: 1.14x faster                                                          |
| sympy_integrate            | 17.5 ms                                                         | 15.5 ms: 1.13x faster                                                          |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 484 ms: 1.13x faster                                                           |
| bench_thread_pool          | 1.10 ms                                                         | 984 us: 1.12x faster                                                           |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 504 ms: 1.12x faster                                                           |
| pathlib                    | 91.4 ms                                                         | 82.4 ms: 1.11x faster                                                          |
| asyncio_tcp                | 662 ms                                                          | 600 ms: 1.10x faster                                                           |
| xml_etree_parse            | 113 ms                                                          | 102 ms: 1.10x faster                                                           |
| sqlite_synth               | 2.07 us                                                         | 1.90 us: 1.09x faster                                                          |
| tornado_http               | 105 ms                                                          | 96.4 ms: 1.09x faster                                                          |
| sympy_expand               | 398 ms                                                          | 370 ms: 1.07x faster                                                           |
| docutils                   | 1.98 sec                                                        | 1.85 sec: 1.07x faster                                                         |
| asyncio_tcp_ssl            | 17.7 sec                                                        | 16.8 sec: 1.05x faster                                                         |
| regex_dna                  | 127 ms                                                          | 123 ms: 1.03x faster                                                           |
| regex_effbot               | 2.04 ms                                                         | 1.98 ms: 1.03x faster                                                          |
| async_generators           | 313 ms                                                          | 305 ms: 1.03x faster                                                           |
| bench_mp_pool              | 75.4 ms                                                         | 74.1 ms: 1.02x faster                                                          |
| unpickle_list              | 2.95 us                                                         | 2.90 us: 1.02x faster                                                          |
| pidigits                   | 199 ms                                                          | 198 ms: 1.01x faster                                                           |
| json_loads                 | 20.4 us                                                         | 20.7 us: 1.02x slower                                                          |
| telco                      | 5.51 ms                                                         | 5.64 ms: 1.02x slower                                                          |
| pickle_dict                | 19.9 us                                                         | 20.7 us: 1.04x slower                                                          |
| coverage                   | 48.4 ms                                                         | 50.6 ms: 1.05x slower                                                          |
| regex_v8                   | 15.0 ms                                                         | 15.9 ms: 1.05x slower                                                          |
| pickle                     | 7.79 us                                                         | 8.23 us: 1.06x slower                                                          |
| python_startup_no_site     | 19.1 ms                                                         | 20.2 ms: 1.06x slower                                                          |
| typing_runtime_protocols   | 126 us                                                          | 135 us: 1.07x slower                                                           |
| python_startup             | 22.4 ms                                                         | 24.2 ms: 1.08x slower                                                          |
| unpickle                   | 9.71 us                                                         | 10.5 us: 1.08x slower                                                          |
| pickle_list                | 3.37 us                                                         | 3.72 us: 1.11x slower                                                          |
| create_gc_cycles           | 652 us                                                          | 757 us: 1.16x slower                                                           |
| sqlglot_normalize          | 100 ms                                                          | 218 ms: 2.18x slower                                                           |
| Geometric mean             | (ref)                                                           | 1.24x faster                                                                   |

Benchmark hidden because not significant (2): gc_traversal, json
Ignored benchmarks (8) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, dulwich_log, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (5) of results/bm-20240605-3.14.0a0-e83ce85-JIT/bm-20240605-pythonperf1_win32-x86-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85.json: genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.19x
- 95% likely to have a speedup of 1.17x
- 99% likely to have a speedup of 1.16x

# Memory
- memory change: unknown