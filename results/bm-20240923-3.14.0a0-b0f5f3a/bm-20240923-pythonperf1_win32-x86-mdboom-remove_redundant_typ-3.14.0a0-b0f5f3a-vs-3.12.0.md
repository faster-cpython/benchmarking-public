# Results vs. 3.12.0

- fork: mdboom
- ref: remove_redundant_typ
- machine: windows-x86
- commit hash: b0f5f3a
- commit date: 2024-09-23
- overall geometric mean: 1.13x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.09x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240923-pythonperf1_win32-x86-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 251 ms: 1.12x faster                                                           |
| docutils       | 1.98 sec                                                        | 1.86 sec: 1.07x faster                                                         |
| tornado_http   | 105 ms                                                          | 95.6 ms: 1.10x faster                                                          |
| Geometric mean | (ref)                                                           | 1.09x faster                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240923-pythonperf1_win32-x86-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 350 ms                                                          | 250 ms: 1.40x faster                                                           |
| async_tree_none_tg         | 278 ms                                                          | 201 ms: 1.38x faster                                                           |
| async_tree_none            | 298 ms                                                          | 218 ms: 1.36x faster                                                           |
| async_tree_memoization     | 364 ms                                                          | 270 ms: 1.35x faster                                                           |
| async_tree_io_tg           | 677 ms                                                          | 520 ms: 1.30x faster                                                           |
| async_tree_io              | 693 ms                                                          | 538 ms: 1.29x faster                                                           |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 487 ms: 1.16x faster                                                           |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 476 ms: 1.15x faster                                                           |
| Geometric mean             | (ref)                                                           | 1.30x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240923-pythonperf1_win32-x86-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 93.0 ms: 1.37x faster                                                          |
| float          | 76.7 ms                                                         | 62.7 ms: 1.22x faster                                                          |
| pidigits       | 199 ms                                                          | 197 ms: 1.01x faster                                                           |
| Geometric mean | (ref)                                                           | 1.19x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240923-pythonperf1_win32-x86-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 108 ms: 1.20x faster                                                           |
| regex_dna      | 127 ms                                                          | 117 ms: 1.08x faster                                                           |
| regex_effbot   | 2.04 ms                                                         | 1.89 ms: 1.08x faster                                                          |
| regex_v8       | 15.0 ms                                                         | 16.0 ms: 1.07x slower                                                          |
| Geometric mean | (ref)                                                           | 1.07x faster                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240923-pythonperf1_win32-x86-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| tomli_loads          | 2.20 sec                                                        | 1.85 sec: 1.19x faster                                                         |
| unpickle_pure_python | 210 us                                                          | 177 us: 1.19x faster                                                           |
| xml_etree_iterparse  | 77.6 ms                                                         | 67.6 ms: 1.15x faster                                                          |
| pickle_pure_python   | 286 us                                                          | 260 us: 1.10x faster                                                           |
| xml_etree_process    | 53.2 ms                                                         | 49.9 ms: 1.07x faster                                                          |
| xml_etree_parse      | 113 ms                                                          | 107 ms: 1.05x faster                                                           |
| xml_etree_generate   | 72.1 ms                                                         | 69.1 ms: 1.04x faster                                                          |
| pickle_list          | 3.37 us                                                         | 3.40 us: 1.01x slower                                                          |
| pickle               | 7.79 us                                                         | 7.91 us: 1.02x slower                                                          |
| unpickle_list        | 2.95 us                                                         | 3.01 us: 1.02x slower                                                          |
| json_loads           | 20.4 us                                                         | 20.9 us: 1.03x slower                                                          |
| json_dumps           | 7.40 ms                                                         | 7.70 ms: 1.04x slower                                                          |
| pickle_dict          | 19.9 us                                                         | 20.8 us: 1.04x slower                                                          |
| unpickle             | 9.71 us                                                         | 10.4 us: 1.07x slower                                                          |
| Geometric mean       | (ref)                                                           | 1.04x faster                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240923-pythonperf1_win32-x86-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 19.7 ms: 1.03x slower                                                          |
| python_startup         | 22.4 ms                                                         | 23.7 ms: 1.06x slower                                                          |
| Geometric mean         | (ref)                                                           | 1.05x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240923-pythonperf1_win32-x86-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 8.09 ms: 1.23x faster                                                          |
| django_template | 36.9 ms                                                         | 33.2 ms: 1.11x faster                                                          |
| Geometric mean  | (ref)                                                           | 1.17x faster                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240923-pythonperf1_win32-x86-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| deepcopy_memo              | 38.4 us                                                         | 22.5 us: 1.71x faster                                                          |
| generators                 | 38.5 ms                                                         | 25.8 ms: 1.49x faster                                                          |
| deepcopy                   | 360 us                                                          | 245 us: 1.47x faster                                                           |
| async_tree_memoization_tg  | 350 ms                                                          | 250 ms: 1.40x faster                                                           |
| comprehensions             | 19.2 us                                                         | 13.7 us: 1.40x faster                                                          |
| async_tree_none_tg         | 278 ms                                                          | 201 ms: 1.38x faster                                                           |
| unpack_sequence            | 62.5 ns                                                         | 45.3 ns: 1.38x faster                                                          |
| spectral_norm              | 104 ms                                                          | 75.5 ms: 1.37x faster                                                          |
| logging_silent             | 101 ns                                                          | 73.5 ns: 1.37x faster                                                          |
| nbody                      | 127 ms                                                          | 93.0 ms: 1.37x faster                                                          |
| async_tree_none            | 298 ms                                                          | 218 ms: 1.36x faster                                                           |
| async_tree_memoization     | 364 ms                                                          | 270 ms: 1.35x faster                                                           |
| scimark_lu                 | 93.2 ms                                                         | 69.6 ms: 1.34x faster                                                          |
| hexiom                     | 6.82 ms                                                         | 5.13 ms: 1.33x faster                                                          |
| async_tree_io_tg           | 677 ms                                                          | 520 ms: 1.30x faster                                                           |
| raytrace                   | 308 ms                                                          | 237 ms: 1.30x faster                                                           |
| deltablue                  | 3.58 ms                                                         | 2.76 ms: 1.30x faster                                                          |
| go                         | 137 ms                                                          | 106 ms: 1.30x faster                                                           |
| async_tree_io              | 693 ms                                                          | 538 ms: 1.29x faster                                                           |
| scimark_sor                | 130 ms                                                          | 101 ms: 1.28x faster                                                           |
| chaos                      | 69.4 ms                                                         | 54.7 ms: 1.27x faster                                                          |
| nqueens                    | 93.7 ms                                                         | 74.6 ms: 1.26x faster                                                          |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 3.09 ms: 1.25x faster                                                          |
| deepcopy_reduce            | 3.23 us                                                         | 2.60 us: 1.24x faster                                                          |
| logging_simple             | 9.75 us                                                         | 7.91 us: 1.23x faster                                                          |
| mako                       | 9.96 ms                                                         | 8.09 ms: 1.23x faster                                                          |
| float                      | 76.7 ms                                                         | 62.7 ms: 1.22x faster                                                          |
| crypto_pyaes               | 69.2 ms                                                         | 57.1 ms: 1.21x faster                                                          |
| logging_format             | 10.4 us                                                         | 8.62 us: 1.21x faster                                                          |
| regex_compile              | 129 ms                                                          | 108 ms: 1.20x faster                                                           |
| tomli_loads                | 2.20 sec                                                        | 1.85 sec: 1.19x faster                                                         |
| unpickle_pure_python       | 210 us                                                          | 177 us: 1.19x faster                                                           |
| pyflate                    | 424 ms                                                          | 358 ms: 1.18x faster                                                           |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 487 ms: 1.16x faster                                                           |
| dulwich_log                | 58.5 ms                                                         | 50.6 ms: 1.16x faster                                                          |
| scimark_monte_carlo        | 66.4 ms                                                         | 57.7 ms: 1.15x faster                                                          |
| xml_etree_iterparse        | 77.6 ms                                                         | 67.6 ms: 1.15x faster                                                          |
| sqlglot_parse              | 1.25 ms                                                         | 1.09 ms: 1.15x faster                                                          |
| scimark_fft                | 271 ms                                                          | 236 ms: 1.15x faster                                                           |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 476 ms: 1.15x faster                                                           |
| coroutines                 | 20.9 ms                                                         | 18.3 ms: 1.14x faster                                                          |
| sqlglot_transpile          | 1.53 ms                                                         | 1.34 ms: 1.14x faster                                                          |
| sympy_sum                  | 123 ms                                                          | 108 ms: 1.14x faster                                                           |
| pycparser                  | 978 ms                                                          | 862 ms: 1.13x faster                                                           |
| sympy_integrate            | 17.5 ms                                                         | 15.5 ms: 1.13x faster                                                          |
| 2to3                       | 280 ms                                                          | 251 ms: 1.12x faster                                                           |
| django_template            | 36.9 ms                                                         | 33.2 ms: 1.11x faster                                                          |
| mdp                        | 1.91 sec                                                        | 1.73 sec: 1.11x faster                                                         |
| pickle_pure_python         | 286 us                                                          | 260 us: 1.10x faster                                                           |
| tornado_http               | 105 ms                                                          | 95.6 ms: 1.10x faster                                                          |
| pprint_pformat             | 1.50 sec                                                        | 1.37 sec: 1.09x faster                                                         |
| sympy_str                  | 240 ms                                                          | 219 ms: 1.09x faster                                                           |
| sqlglot_optimize           | 48.5 ms                                                         | 44.4 ms: 1.09x faster                                                          |
| pathlib                    | 91.4 ms                                                         | 83.9 ms: 1.09x faster                                                          |
| fannkuch                   | 354 ms                                                          | 326 ms: 1.08x faster                                                           |
| regex_dna                  | 127 ms                                                          | 117 ms: 1.08x faster                                                           |
| regex_effbot               | 2.04 ms                                                         | 1.89 ms: 1.08x faster                                                          |
| meteor_contest             | 86.9 ms                                                         | 80.6 ms: 1.08x faster                                                          |
| bench_thread_pool          | 1.10 ms                                                         | 1.03 ms: 1.07x faster                                                          |
| pprint_safe_repr           | 721 ms                                                          | 676 ms: 1.07x faster                                                           |
| xml_etree_process          | 53.2 ms                                                         | 49.9 ms: 1.07x faster                                                          |
| docutils                   | 1.98 sec                                                        | 1.86 sec: 1.07x faster                                                         |
| bench_mp_pool              | 75.4 ms                                                         | 71.4 ms: 1.06x faster                                                          |
| xml_etree_parse            | 113 ms                                                          | 107 ms: 1.05x faster                                                           |
| sqlite_synth               | 2.07 us                                                         | 1.98 us: 1.05x faster                                                          |
| xml_etree_generate         | 72.1 ms                                                         | 69.1 ms: 1.04x faster                                                          |
| asyncio_tcp_ssl            | 17.7 sec                                                        | 17.0 sec: 1.04x faster                                                         |
| richards_super             | 46.5 ms                                                         | 44.8 ms: 1.04x faster                                                          |
| async_generators           | 313 ms                                                          | 303 ms: 1.03x faster                                                           |
| sympy_expand               | 398 ms                                                          | 387 ms: 1.03x faster                                                           |
| gc_traversal               | 1.44 ms                                                         | 1.41 ms: 1.02x faster                                                          |
| richards                   | 41.3 ms                                                         | 40.5 ms: 1.02x faster                                                          |
| pidigits                   | 199 ms                                                          | 197 ms: 1.01x faster                                                           |
| pickle_list                | 3.37 us                                                         | 3.40 us: 1.01x slower                                                          |
| pickle                     | 7.79 us                                                         | 7.91 us: 1.02x slower                                                          |
| json                       | 4.15 ms                                                         | 4.24 ms: 1.02x slower                                                          |
| unpickle_list              | 2.95 us                                                         | 3.01 us: 1.02x slower                                                          |
| json_loads                 | 20.4 us                                                         | 20.9 us: 1.03x slower                                                          |
| python_startup_no_site     | 19.1 ms                                                         | 19.7 ms: 1.03x slower                                                          |
| json_dumps                 | 7.40 ms                                                         | 7.70 ms: 1.04x slower                                                          |
| pickle_dict                | 19.9 us                                                         | 20.8 us: 1.04x slower                                                          |
| python_startup             | 22.4 ms                                                         | 23.7 ms: 1.06x slower                                                          |
| regex_v8                   | 15.0 ms                                                         | 16.0 ms: 1.07x slower                                                          |
| unpickle                   | 9.71 us                                                         | 10.4 us: 1.07x slower                                                          |
| coverage                   | 48.4 ms                                                         | 52.7 ms: 1.09x slower                                                          |
| create_gc_cycles           | 652 us                                                          | 728 us: 1.12x slower                                                           |
| typing_runtime_protocols   | 126 us                                                          | 144 us: 1.14x slower                                                           |
| telco                      | 5.51 ms                                                         | 6.79 ms: 1.23x slower                                                          |
| sqlglot_normalize          | 100 ms                                                          | 231 ms: 2.31x slower                                                           |
| Geometric mean             | (ref)                                                           | 1.13x faster                                                                   |

Benchmark hidden because not significant (1): asyncio_tcp
Ignored benchmarks (6) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20240923-3.14.0a0-b0f5f3a/bm-20240923-pythonperf1_win32-x86-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a.json: genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.11x
- 95% likely to have a speedup of 1.10x
- 99% likely to have a speedup of 1.09x

# Memory
- memory change: unknown