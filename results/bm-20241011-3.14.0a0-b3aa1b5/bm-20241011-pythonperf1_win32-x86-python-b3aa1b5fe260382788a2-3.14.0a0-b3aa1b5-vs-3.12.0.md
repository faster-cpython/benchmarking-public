# Results vs. 3.12.0

- fork: python
- ref: b3aa1b5fe260382788a2
- machine: windows-x86
- commit hash: b3aa1b5
- commit date: 2024-10-11
- overall geometric mean: 1.13x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.11x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241011-pythonperf1_win32-x86-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 248 ms: 1.13x faster                                                           |
| docutils       | 1.98 sec                                                        | 1.88 sec: 1.06x faster                                                         |
| tornado_http   | 105 ms                                                          | 104 ms: 1.01x faster                                                           |
| Geometric mean | (ref)                                                           | 1.07x faster                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241011-pythonperf1_win32-x86-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5 |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_none_tg         | 278 ms                                                          | 196 ms: 1.41x faster                                                           |
| async_tree_memoization_tg  | 350 ms                                                          | 249 ms: 1.41x faster                                                           |
| async_tree_none            | 298 ms                                                          | 213 ms: 1.40x faster                                                           |
| async_tree_memoization     | 364 ms                                                          | 270 ms: 1.35x faster                                                           |
| async_tree_io_tg           | 677 ms                                                          | 519 ms: 1.31x faster                                                           |
| async_tree_io              | 693 ms                                                          | 532 ms: 1.30x faster                                                           |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 471 ms: 1.20x faster                                                           |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 459 ms: 1.19x faster                                                           |
| Geometric mean             | (ref)                                                           | 1.32x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241011-pythonperf1_win32-x86-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 86.7 ms: 1.47x faster                                                          |
| float          | 76.7 ms                                                         | 60.9 ms: 1.26x faster                                                          |
| Geometric mean | (ref)                                                           | 1.23x faster                                                                   |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241011-pythonperf1_win32-x86-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 107 ms: 1.21x faster                                                           |
| regex_effbot   | 2.04 ms                                                         | 1.84 ms: 1.11x faster                                                          |
| regex_dna      | 127 ms                                                          | 117 ms: 1.08x faster                                                           |
| regex_v8       | 15.0 ms                                                         | 15.7 ms: 1.04x slower                                                          |
| Geometric mean | (ref)                                                           | 1.09x faster                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241011-pythonperf1_win32-x86-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5 |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| unpickle_pure_python | 210 us                                                          | 177 us: 1.19x faster                                                           |
| tomli_loads          | 2.20 sec                                                        | 1.87 sec: 1.18x faster                                                         |
| xml_etree_iterparse  | 77.6 ms                                                         | 68.7 ms: 1.13x faster                                                          |
| xml_etree_process    | 53.2 ms                                                         | 48.3 ms: 1.10x faster                                                          |
| pickle_pure_python   | 286 us                                                          | 265 us: 1.08x faster                                                           |
| xml_etree_generate   | 72.1 ms                                                         | 67.7 ms: 1.07x faster                                                          |
| unpickle_list        | 2.95 us                                                         | 2.89 us: 1.02x faster                                                          |
| pickle_list          | 3.37 us                                                         | 3.42 us: 1.01x slower                                                          |
| json_loads           | 20.4 us                                                         | 21.0 us: 1.03x slower                                                          |
| unpickle             | 9.71 us                                                         | 10.1 us: 1.04x slower                                                          |
| pickle_dict          | 19.9 us                                                         | 21.7 us: 1.09x slower                                                          |
| pickle               | 7.79 us                                                         | 8.55 us: 1.10x slower                                                          |
| json_dumps           | 7.40 ms                                                         | 9.01 ms: 1.22x slower                                                          |
| Geometric mean       | (ref)                                                           | 1.02x faster                                                                   |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241011-pythonperf1_win32-x86-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5 |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 20.7 ms: 1.09x slower                                                          |
| python_startup         | 22.4 ms                                                         | 24.9 ms: 1.11x slower                                                          |
| Geometric mean         | (ref)                                                           | 1.10x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241011-pythonperf1_win32-x86-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5 |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 7.76 ms: 1.28x faster                                                          |
| django_template | 36.9 ms                                                         | 34.8 ms: 1.06x faster                                                          |
| Geometric mean  | (ref)                                                           | 1.17x faster                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241011-pythonperf1_win32-x86-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5 |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| deepcopy_memo              | 38.4 us                                                         | 21.3 us: 1.80x faster                                                          |
| generators                 | 38.5 ms                                                         | 23.5 ms: 1.64x faster                                                          |
| logging_silent             | 101 ns                                                          | 67.4 ns: 1.50x faster                                                          |
| deepcopy                   | 360 us                                                          | 245 us: 1.47x faster                                                           |
| nbody                      | 127 ms                                                          | 86.7 ms: 1.47x faster                                                          |
| comprehensions             | 19.2 us                                                         | 13.1 us: 1.46x faster                                                          |
| unpack_sequence            | 62.5 ns                                                         | 43.4 ns: 1.44x faster                                                          |
| async_tree_none_tg         | 278 ms                                                          | 196 ms: 1.41x faster                                                           |
| async_tree_memoization_tg  | 350 ms                                                          | 249 ms: 1.41x faster                                                           |
| spectral_norm              | 104 ms                                                          | 74.0 ms: 1.40x faster                                                          |
| async_tree_none            | 298 ms                                                          | 213 ms: 1.40x faster                                                           |
| go                         | 137 ms                                                          | 99.3 ms: 1.38x faster                                                          |
| hexiom                     | 6.82 ms                                                         | 4.96 ms: 1.38x faster                                                          |
| scimark_lu                 | 93.2 ms                                                         | 68.5 ms: 1.36x faster                                                          |
| async_tree_memoization     | 364 ms                                                          | 270 ms: 1.35x faster                                                           |
| deltablue                  | 3.58 ms                                                         | 2.70 ms: 1.33x faster                                                          |
| scimark_sor                | 130 ms                                                          | 99.4 ms: 1.31x faster                                                          |
| async_tree_io_tg           | 677 ms                                                          | 519 ms: 1.31x faster                                                           |
| async_tree_io              | 693 ms                                                          | 532 ms: 1.30x faster                                                           |
| deepcopy_reduce            | 3.23 us                                                         | 2.49 us: 1.29x faster                                                          |
| mako                       | 9.96 ms                                                         | 7.76 ms: 1.28x faster                                                          |
| raytrace                   | 308 ms                                                          | 243 ms: 1.27x faster                                                           |
| chaos                      | 69.4 ms                                                         | 55.0 ms: 1.26x faster                                                          |
| float                      | 76.7 ms                                                         | 60.9 ms: 1.26x faster                                                          |
| nqueens                    | 93.7 ms                                                         | 74.7 ms: 1.25x faster                                                          |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 3.09 ms: 1.25x faster                                                          |
| logging_simple             | 9.75 us                                                         | 7.84 us: 1.24x faster                                                          |
| logging_format             | 10.4 us                                                         | 8.57 us: 1.21x faster                                                          |
| regex_compile              | 129 ms                                                          | 107 ms: 1.21x faster                                                           |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 471 ms: 1.20x faster                                                           |
| coroutines                 | 20.9 ms                                                         | 17.5 ms: 1.19x faster                                                          |
| pyflate                    | 424 ms                                                          | 356 ms: 1.19x faster                                                           |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 459 ms: 1.19x faster                                                           |
| scimark_monte_carlo        | 66.4 ms                                                         | 55.9 ms: 1.19x faster                                                          |
| unpickle_pure_python       | 210 us                                                          | 177 us: 1.19x faster                                                           |
| scimark_fft                | 271 ms                                                          | 229 ms: 1.18x faster                                                           |
| sqlglot_parse              | 1.25 ms                                                         | 1.06 ms: 1.18x faster                                                          |
| tomli_loads                | 2.20 sec                                                        | 1.87 sec: 1.18x faster                                                         |
| sqlglot_transpile          | 1.53 ms                                                         | 1.30 ms: 1.18x faster                                                          |
| pycparser                  | 978 ms                                                          | 836 ms: 1.17x faster                                                           |
| fannkuch                   | 354 ms                                                          | 308 ms: 1.15x faster                                                           |
| pprint_pformat             | 1.50 sec                                                        | 1.32 sec: 1.14x faster                                                         |
| sympy_sum                  | 123 ms                                                          | 108 ms: 1.13x faster                                                           |
| crypto_pyaes               | 69.2 ms                                                         | 61.1 ms: 1.13x faster                                                          |
| dulwich_log                | 58.5 ms                                                         | 51.7 ms: 1.13x faster                                                          |
| xml_etree_iterparse        | 77.6 ms                                                         | 68.7 ms: 1.13x faster                                                          |
| 2to3                       | 280 ms                                                          | 248 ms: 1.13x faster                                                           |
| sympy_integrate            | 17.5 ms                                                         | 15.6 ms: 1.12x faster                                                          |
| mdp                        | 1.91 sec                                                        | 1.71 sec: 1.12x faster                                                         |
| pprint_safe_repr           | 721 ms                                                          | 645 ms: 1.12x faster                                                           |
| regex_effbot               | 2.04 ms                                                         | 1.84 ms: 1.11x faster                                                          |
| xml_etree_process          | 53.2 ms                                                         | 48.3 ms: 1.10x faster                                                          |
| sqlglot_optimize           | 48.5 ms                                                         | 44.0 ms: 1.10x faster                                                          |
| sympy_str                  | 240 ms                                                          | 219 ms: 1.10x faster                                                           |
| bench_thread_pool          | 1.10 ms                                                         | 1.01 ms: 1.09x faster                                                          |
| meteor_contest             | 86.9 ms                                                         | 80.0 ms: 1.09x faster                                                          |
| regex_dna                  | 127 ms                                                          | 117 ms: 1.08x faster                                                           |
| pickle_pure_python         | 286 us                                                          | 265 us: 1.08x faster                                                           |
| xml_etree_generate         | 72.1 ms                                                         | 67.7 ms: 1.07x faster                                                          |
| django_template            | 36.9 ms                                                         | 34.8 ms: 1.06x faster                                                          |
| docutils                   | 1.98 sec                                                        | 1.88 sec: 1.06x faster                                                         |
| sqlite_synth               | 2.07 us                                                         | 1.97 us: 1.05x faster                                                          |
| async_generators           | 313 ms                                                          | 301 ms: 1.04x faster                                                           |
| pathlib                    | 91.4 ms                                                         | 88.1 ms: 1.04x faster                                                          |
| sympy_expand               | 398 ms                                                          | 386 ms: 1.03x faster                                                           |
| richards_super             | 46.5 ms                                                         | 45.3 ms: 1.02x faster                                                          |
| unpickle_list              | 2.95 us                                                         | 2.89 us: 1.02x faster                                                          |
| richards                   | 41.3 ms                                                         | 40.5 ms: 1.02x faster                                                          |
| bench_mp_pool              | 75.4 ms                                                         | 74.0 ms: 1.02x faster                                                          |
| asyncio_tcp_ssl            | 17.7 sec                                                        | 17.4 sec: 1.02x faster                                                         |
| tornado_http               | 105 ms                                                          | 104 ms: 1.01x faster                                                           |
| pickle_list                | 3.37 us                                                         | 3.42 us: 1.01x slower                                                          |
| json                       | 4.15 ms                                                         | 4.27 ms: 1.03x slower                                                          |
| json_loads                 | 20.4 us                                                         | 21.0 us: 1.03x slower                                                          |
| regex_v8                   | 15.0 ms                                                         | 15.7 ms: 1.04x slower                                                          |
| unpickle                   | 9.71 us                                                         | 10.1 us: 1.04x slower                                                          |
| pickle_dict                | 19.9 us                                                         | 21.7 us: 1.09x slower                                                          |
| python_startup_no_site     | 19.1 ms                                                         | 20.7 ms: 1.09x slower                                                          |
| coverage                   | 48.4 ms                                                         | 52.7 ms: 1.09x slower                                                          |
| typing_runtime_protocols   | 126 us                                                          | 139 us: 1.10x slower                                                           |
| pickle                     | 7.79 us                                                         | 8.55 us: 1.10x slower                                                          |
| python_startup             | 22.4 ms                                                         | 24.9 ms: 1.11x slower                                                          |
| asyncio_tcp                | 662 ms                                                          | 738 ms: 1.12x slower                                                           |
| create_gc_cycles           | 652 us                                                          | 783 us: 1.20x slower                                                           |
| json_dumps                 | 7.40 ms                                                         | 9.01 ms: 1.22x slower                                                          |
| telco                      | 5.51 ms                                                         | 6.98 ms: 1.27x slower                                                          |
| sqlglot_normalize          | 100 ms                                                          | 229 ms: 2.29x slower                                                           |
| Geometric mean             | (ref)                                                           | 1.13x faster                                                                   |

Benchmark hidden because not significant (3): xml_etree_parse, pidigits, gc_traversal
Ignored benchmarks (6) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20241011-3.14.0a0-b3aa1b5/bm-20241011-pythonperf1_win32-x86-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5.json: genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.13x
- 95% likely to have a speedup of 1.12x
- 99% likely to have a speedup of 1.11x

# Memory
- memory change: unknown