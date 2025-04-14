# Results vs. 3.12.0

- fork: python
- ref: v3.14.0a1
- machine: windows-x86
- commit hash: 8cdaca8
- commit date: 2024-10-15
- overall geometric mean: 1.178x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.11x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241015-pythonperf1_win32-x86-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 264 ms: 1.06x faster                                                |
| docutils       | 1.98 sec                                                        | 2.07 sec: 1.04x slower                                              |
| tornado_http   | 105 ms                                                          | 109 ms: 1.04x slower                                                |
| Geometric mean | (ref)                                                           | 1.01x slower                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241015-pythonperf1_win32-x86-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_memoization_tg  | 350 ms                                                          | 255 ms: 1.38x faster                                                |
| async_tree_none_tg         | 278 ms                                                          | 204 ms: 1.36x faster                                                |
| async_tree_none            | 298 ms                                                          | 219 ms: 1.36x faster                                                |
| async_tree_io              | 693 ms                                                          | 523 ms: 1.33x faster                                                |
| async_tree_memoization     | 364 ms                                                          | 278 ms: 1.31x faster                                                |
| async_tree_io_tg           | 677 ms                                                          | 551 ms: 1.23x faster                                                |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 470 ms: 1.20x faster                                                |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 466 ms: 1.17x faster                                                |
| Geometric mean             | (ref)                                                           | 1.29x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241015-pythonperf1_win32-x86-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 63.2 ms: 2.01x faster                                               |
| float          | 76.7 ms                                                         | 47.0 ms: 1.63x faster                                               |
| pidigits       | 199 ms                                                          | 200 ms: 1.01x slower                                                |
| Geometric mean | (ref)                                                           | 1.48x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241015-pythonperf1_win32-x86-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 104 ms: 1.24x faster                                                |
| regex_effbot   | 2.04 ms                                                         | 1.82 ms: 1.12x faster                                               |
| regex_dna      | 127 ms                                                          | 118 ms: 1.08x faster                                                |
| regex_v8       | 15.0 ms                                                         | 15.4 ms: 1.02x slower                                               |
| Geometric mean | (ref)                                                           | 1.10x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241015-pythonperf1_win32-x86-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| tomli_loads          | 2.20 sec                                                        | 1.56 sec: 1.41x faster                                              |
| unpickle_pure_python | 210 us                                                          | 161 us: 1.30x faster                                                |
| xml_etree_generate   | 72.1 ms                                                         | 55.7 ms: 1.29x faster                                               |
| xml_etree_process    | 53.2 ms                                                         | 42.8 ms: 1.24x faster                                               |
| xml_etree_iterparse  | 77.6 ms                                                         | 64.3 ms: 1.21x faster                                               |
| pickle_pure_python   | 286 us                                                          | 246 us: 1.16x faster                                                |
| unpickle_list        | 2.95 us                                                         | 2.71 us: 1.09x faster                                               |
| xml_etree_parse      | 113 ms                                                          | 109 ms: 1.04x faster                                                |
| json_loads           | 20.4 us                                                         | 20.8 us: 1.02x slower                                               |
| pickle_list          | 3.37 us                                                         | 3.48 us: 1.03x slower                                               |
| unpickle             | 9.71 us                                                         | 10.4 us: 1.07x slower                                               |
| pickle_dict          | 19.9 us                                                         | 21.5 us: 1.08x slower                                               |
| json_dumps           | 7.40 ms                                                         | 8.11 ms: 1.10x slower                                               |
| pickle               | 7.79 us                                                         | 8.60 us: 1.10x slower                                               |
| Geometric mean       | (ref)                                                           | 1.09x faster                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241015-pythonperf1_win32-x86-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 20.3 ms: 1.06x slower                                               |
| python_startup         | 22.4 ms                                                         | 27.1 ms: 1.21x slower                                               |
| Geometric mean         | (ref)                                                           | 1.14x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241015-pythonperf1_win32-x86-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 5.70 ms: 1.75x faster                                               |
| django_template | 36.9 ms                                                         | 33.6 ms: 1.10x faster                                               |
| Geometric mean  | (ref)                                                           | 1.39x faster                                                        |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241015-pythonperf1_win32-x86-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| deepcopy_memo              | 38.4 us                                                         | 16.2 us: 2.37x faster                                               |
| nbody                      | 127 ms                                                          | 63.2 ms: 2.01x faster                                               |
| scimark_sor                | 130 ms                                                          | 70.1 ms: 1.85x faster                                               |
| spectral_norm              | 104 ms                                                          | 57.2 ms: 1.81x faster                                               |
| logging_silent             | 101 ns                                                          | 56.0 ns: 1.80x faster                                               |
| mako                       | 9.96 ms                                                         | 5.70 ms: 1.75x faster                                               |
| float                      | 76.7 ms                                                         | 47.0 ms: 1.63x faster                                               |
| scimark_monte_carlo        | 66.4 ms                                                         | 41.6 ms: 1.60x faster                                               |
| scimark_lu                 | 93.2 ms                                                         | 60.6 ms: 1.54x faster                                               |
| generators                 | 38.5 ms                                                         | 25.1 ms: 1.54x faster                                               |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 2.54 ms: 1.52x faster                                               |
| deepcopy                   | 360 us                                                          | 238 us: 1.51x faster                                                |
| unpack_sequence            | 62.5 ns                                                         | 41.7 ns: 1.50x faster                                               |
| comprehensions             | 19.2 us                                                         | 13.0 us: 1.47x faster                                               |
| scimark_fft                | 271 ms                                                          | 187 ms: 1.45x faster                                                |
| fannkuch                   | 354 ms                                                          | 249 ms: 1.42x faster                                                |
| go                         | 137 ms                                                          | 97.2 ms: 1.41x faster                                               |
| tomli_loads                | 2.20 sec                                                        | 1.56 sec: 1.41x faster                                              |
| async_tree_memoization_tg  | 350 ms                                                          | 255 ms: 1.38x faster                                                |
| async_tree_none_tg         | 278 ms                                                          | 204 ms: 1.36x faster                                                |
| pyflate                    | 424 ms                                                          | 312 ms: 1.36x faster                                                |
| deltablue                  | 3.58 ms                                                         | 2.64 ms: 1.36x faster                                               |
| async_tree_none            | 298 ms                                                          | 219 ms: 1.36x faster                                                |
| pprint_pformat             | 1.50 sec                                                        | 1.12 sec: 1.34x faster                                              |
| crypto_pyaes               | 69.2 ms                                                         | 51.9 ms: 1.33x faster                                               |
| async_tree_io              | 693 ms                                                          | 523 ms: 1.33x faster                                                |
| pprint_safe_repr           | 721 ms                                                          | 546 ms: 1.32x faster                                                |
| deepcopy_reduce            | 3.23 us                                                         | 2.44 us: 1.32x faster                                               |
| async_tree_memoization     | 364 ms                                                          | 278 ms: 1.31x faster                                                |
| unpickle_pure_python       | 210 us                                                          | 161 us: 1.30x faster                                                |
| xml_etree_generate         | 72.1 ms                                                         | 55.7 ms: 1.29x faster                                               |
| logging_simple             | 9.75 us                                                         | 7.54 us: 1.29x faster                                               |
| hexiom                     | 6.82 ms                                                         | 5.38 ms: 1.27x faster                                               |
| logging_format             | 10.4 us                                                         | 8.27 us: 1.26x faster                                               |
| xml_etree_process          | 53.2 ms                                                         | 42.8 ms: 1.24x faster                                               |
| chaos                      | 69.4 ms                                                         | 55.8 ms: 1.24x faster                                               |
| regex_compile              | 129 ms                                                          | 104 ms: 1.24x faster                                                |
| async_tree_io_tg           | 677 ms                                                          | 551 ms: 1.23x faster                                                |
| nqueens                    | 93.7 ms                                                         | 76.2 ms: 1.23x faster                                               |
| xml_etree_iterparse        | 77.6 ms                                                         | 64.3 ms: 1.21x faster                                               |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 470 ms: 1.20x faster                                                |
| sqlglot_parse              | 1.25 ms                                                         | 1.05 ms: 1.19x faster                                               |
| dulwich_log                | 58.5 ms                                                         | 49.3 ms: 1.19x faster                                               |
| meteor_contest             | 86.9 ms                                                         | 73.3 ms: 1.18x faster                                               |
| coroutines                 | 20.9 ms                                                         | 17.8 ms: 1.17x faster                                               |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 466 ms: 1.17x faster                                                |
| pycparser                  | 978 ms                                                          | 834 ms: 1.17x faster                                                |
| pickle_pure_python         | 286 us                                                          | 246 us: 1.16x faster                                                |
| raytrace                   | 308 ms                                                          | 269 ms: 1.14x faster                                                |
| regex_effbot               | 2.04 ms                                                         | 1.82 ms: 1.12x faster                                               |
| sqlglot_transpile          | 1.53 ms                                                         | 1.37 ms: 1.12x faster                                               |
| mdp                        | 1.91 sec                                                        | 1.73 sec: 1.11x faster                                              |
| django_template            | 36.9 ms                                                         | 33.6 ms: 1.10x faster                                               |
| bench_thread_pool          | 1.10 ms                                                         | 1.01 ms: 1.09x faster                                               |
| unpickle_list              | 2.95 us                                                         | 2.71 us: 1.09x faster                                               |
| sqlite_synth               | 2.07 us                                                         | 1.91 us: 1.08x faster                                               |
| regex_dna                  | 127 ms                                                          | 118 ms: 1.08x faster                                                |
| 2to3                       | 280 ms                                                          | 264 ms: 1.06x faster                                                |
| sympy_str                  | 240 ms                                                          | 227 ms: 1.05x faster                                                |
| sympy_sum                  | 123 ms                                                          | 117 ms: 1.05x faster                                                |
| xml_etree_parse            | 113 ms                                                          | 109 ms: 1.04x faster                                                |
| pathlib                    | 91.4 ms                                                         | 88.4 ms: 1.03x faster                                               |
| richards                   | 41.3 ms                                                         | 40.2 ms: 1.03x faster                                               |
| richards_super             | 46.5 ms                                                         | 45.6 ms: 1.02x faster                                               |
| asyncio_tcp_ssl            | 17.7 sec                                                        | 17.5 sec: 1.01x faster                                              |
| sympy_expand               | 398 ms                                                          | 394 ms: 1.01x faster                                                |
| pidigits                   | 199 ms                                                          | 200 ms: 1.01x slower                                                |
| regex_v8                   | 15.0 ms                                                         | 15.4 ms: 1.02x slower                                               |
| json_loads                 | 20.4 us                                                         | 20.8 us: 1.02x slower                                               |
| pickle_list                | 3.37 us                                                         | 3.48 us: 1.03x slower                                               |
| sqlglot_optimize           | 48.5 ms                                                         | 50.3 ms: 1.04x slower                                               |
| tornado_http               | 105 ms                                                          | 109 ms: 1.04x slower                                                |
| async_generators           | 313 ms                                                          | 325 ms: 1.04x slower                                                |
| docutils                   | 1.98 sec                                                        | 2.07 sec: 1.04x slower                                              |
| python_startup_no_site     | 19.1 ms                                                         | 20.3 ms: 1.06x slower                                               |
| unpickle                   | 9.71 us                                                         | 10.4 us: 1.07x slower                                               |
| pickle_dict                | 19.9 us                                                         | 21.5 us: 1.08x slower                                               |
| json_dumps                 | 7.40 ms                                                         | 8.11 ms: 1.10x slower                                               |
| pickle                     | 7.79 us                                                         | 8.60 us: 1.10x slower                                               |
| coverage                   | 48.4 ms                                                         | 53.8 ms: 1.11x slower                                               |
| telco                      | 5.51 ms                                                         | 6.36 ms: 1.15x slower                                               |
| typing_runtime_protocols   | 126 us                                                          | 148 us: 1.17x slower                                                |
| asyncio_tcp                | 662 ms                                                          | 789 ms: 1.19x slower                                                |
| json                       | 4.15 ms                                                         | 5.03 ms: 1.21x slower                                               |
| python_startup             | 22.4 ms                                                         | 27.1 ms: 1.21x slower                                               |
| bench_mp_pool              | 75.4 ms                                                         | 94.5 ms: 1.25x slower                                               |
| gc_traversal               | 1.44 ms                                                         | 1.81 ms: 1.26x slower                                               |
| create_gc_cycles           | 652 us                                                          | 1.20 ms: 1.84x slower                                               |
| sqlglot_normalize          | 100 ms                                                          | 244 ms: 2.44x slower                                                |
| Geometric mean             | (ref)                                                           | 1.16x faster                                                        |

Benchmark hidden because not significant (1): sympy_integrate
Ignored benchmarks (6) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (6) of results/bm-20241015-3.14.0a1-8cdaca8-JIT/bm-20241015-pythonperf1_win32-x86-python-v3.14.0a1-3.14.0a1-8cdaca8.json: genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift

- Geometric mean (including insignificant results): 1.178x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.16x
- 95% likely to have a speedup of 1.14x
- 99% likely to have a speedup of 1.11x

# Memory
- memory change: unknown