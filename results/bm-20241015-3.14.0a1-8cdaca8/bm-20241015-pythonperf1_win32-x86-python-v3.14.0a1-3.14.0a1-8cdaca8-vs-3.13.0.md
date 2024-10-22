# Results vs. 3.13.0

- fork: python
- ref: v3.14.0a1
- machine: windows-x86
- commit hash: 8cdaca8
- commit date: 2024-10-15
- overall geometric mean: 1.01x faster
- HPT reliability: 99.94%
- HPT 99th percentile: 1.01x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241015-pythonperf1_win32-x86-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 253 ms                                                          | 246 ms: 1.03x faster                                                |
| docutils       | 1.82 sec                                                        | 1.85 sec: 1.02x slower                                              |
| html5lib       | 48.3 ms                                                         | 44.9 ms: 1.08x faster                                               |
| Geometric mean | (ref)                                                           | 1.02x faster                                                        |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241015-pythonperf1_win32-x86-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|---------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_memoization_tg | 287 ms                                                          | 256 ms: 1.12x faster                                                |
| async_tree_none           | 246 ms                                                          | 223 ms: 1.10x faster                                                |
| async_tree_memoization    | 302 ms                                                          | 280 ms: 1.08x faster                                                |
| async_tree_none_tg        | 219 ms                                                          | 205 ms: 1.06x faster                                                |
| async_tree_cpu_io_mixed   | 494 ms                                                          | 467 ms: 1.06x faster                                                |
| asyncio_tcp               | 842 ms                                                          | 819 ms: 1.03x faster                                                |
| coroutines                | 15.7 ms                                                         | 17.1 ms: 1.09x slower                                               |
| async_tree_io_tg          | 509 ms                                                          | 558 ms: 1.10x slower                                                |
| async_generators          | 274 ms                                                          | 306 ms: 1.12x slower                                                |
| Geometric mean            | (ref)                                                           | 1.01x faster                                                        |

Benchmark hidden because not significant (3): async_tree_io, async_tree_cpu_io_mixed_tg, asyncio_tcp_ssl

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241015-pythonperf1_win32-x86-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| pidigits       | 202 ms                                                          | 199 ms: 1.02x faster                                                |
| nbody          | 81.9 ms                                                         | 87.2 ms: 1.07x slower                                               |
| float          | 57.8 ms                                                         | 61.9 ms: 1.07x slower                                               |
| Geometric mean | (ref)                                                           | 1.04x slower                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241015-pythonperf1_win32-x86-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_effbot   | 1.81 ms                                                         | 1.82 ms: 1.01x slower                                               |
| regex_dna      | 117 ms                                                          | 118 ms: 1.01x slower                                                |
| regex_v8       | 15.6 ms                                                         | 15.8 ms: 1.01x slower                                               |
| regex_compile  | 103 ms                                                          | 105 ms: 1.02x slower                                                |
| Geometric mean | (ref)                                                           | 1.01x slower                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241015-pythonperf1_win32-x86-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| unpickle_list        | 3.09 us                                                         | 2.98 us: 1.04x faster                                               |
| unpickle             | 10.5 us                                                         | 10.2 us: 1.03x faster                                               |
| json_loads           | 21.0 us                                                         | 20.5 us: 1.03x faster                                               |
| pickle_dict          | 21.7 us                                                         | 21.6 us: 1.00x faster                                               |
| pickle               | 8.42 us                                                         | 8.56 us: 1.02x slower                                               |
| pickle_list          | 3.40 us                                                         | 3.49 us: 1.03x slower                                               |
| xml_etree_parse      | 109 ms                                                          | 113 ms: 1.04x slower                                                |
| xml_etree_process    | 45.0 ms                                                         | 47.6 ms: 1.06x slower                                               |
| xml_etree_generate   | 62.6 ms                                                         | 66.5 ms: 1.06x slower                                               |
| xml_etree_iterparse  | 65.1 ms                                                         | 69.5 ms: 1.07x slower                                               |
| tomli_loads          | 1.73 sec                                                        | 1.87 sec: 1.08x slower                                              |
| unpickle_pure_python | 162 us                                                          | 178 us: 1.10x slower                                                |
| pickle_pure_python   | 238 us                                                          | 265 us: 1.12x slower                                                |
| json_dumps           | 7.40 ms                                                         | 9.09 ms: 1.23x slower                                               |
| Geometric mean       | (ref)                                                           | 1.05x slower                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241015-pythonperf1_win32-x86-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup_no_site | 19.9 ms                                                         | 20.1 ms: 1.01x slower                                               |
| python_startup         | 24.3 ms                                                         | 26.6 ms: 1.10x slower                                               |
| Geometric mean         | (ref)                                                           | 1.05x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241015-pythonperf1_win32-x86-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| genshi_text    | 22.4 ms                                                         | 20.6 ms: 1.09x faster                                               |
| genshi_xml     | 49.5 ms                                                         | 45.9 ms: 1.08x faster                                               |
| mako           | 7.31 ms                                                         | 7.83 ms: 1.07x slower                                               |
| Geometric mean | (ref)                                                           | 1.03x faster                                                        |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                 | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241015-pythonperf1_win32-x86-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|---------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| thrift                    | 10.1 ms                                                         | 762 us: 13.32x faster                                               |
| coverage                  | 333 ms                                                          | 51.9 ms: 6.42x faster                                               |
| deepcopy                  | 307 us                                                          | 242 us: 1.27x faster                                                |
| deepcopy_memo             | 26.2 us                                                         | 22.3 us: 1.17x faster                                               |
| async_tree_memoization_tg | 287 ms                                                          | 256 ms: 1.12x faster                                                |
| go                        | 111 ms                                                          | 99.5 ms: 1.12x faster                                               |
| deepcopy_reduce           | 2.85 us                                                         | 2.55 us: 1.12x faster                                               |
| async_tree_none           | 246 ms                                                          | 223 ms: 1.10x faster                                                |
| genshi_text               | 22.4 ms                                                         | 20.6 ms: 1.09x faster                                               |
| async_tree_memoization    | 302 ms                                                          | 280 ms: 1.08x faster                                                |
| genshi_xml                | 49.5 ms                                                         | 45.9 ms: 1.08x faster                                               |
| html5lib                  | 48.3 ms                                                         | 44.9 ms: 1.08x faster                                               |
| async_tree_none_tg        | 219 ms                                                          | 205 ms: 1.06x faster                                                |
| async_tree_cpu_io_mixed   | 494 ms                                                          | 467 ms: 1.06x faster                                                |
| pycparser                 | 869 ms                                                          | 825 ms: 1.05x faster                                                |
| unpickle_list             | 3.09 us                                                         | 2.98 us: 1.04x faster                                               |
| unpickle                  | 10.5 us                                                         | 10.2 us: 1.03x faster                                               |
| 2to3                      | 253 ms                                                          | 246 ms: 1.03x faster                                                |
| asyncio_tcp               | 842 ms                                                          | 819 ms: 1.03x faster                                                |
| json_loads                | 21.0 us                                                         | 20.5 us: 1.03x faster                                               |
| pidigits                  | 202 ms                                                          | 199 ms: 1.02x faster                                                |
| pathlib                   | 89.4 ms                                                         | 88.2 ms: 1.01x faster                                               |
| telco                     | 6.67 ms                                                         | 6.58 ms: 1.01x faster                                               |
| sympy_sum                 | 108 ms                                                          | 107 ms: 1.01x faster                                                |
| nqueens                   | 75.1 ms                                                         | 74.5 ms: 1.01x faster                                               |
| pickle_dict               | 21.7 us                                                         | 21.6 us: 1.00x faster                                               |
| regex_effbot              | 1.81 ms                                                         | 1.82 ms: 1.01x slower                                               |
| python_startup_no_site    | 19.9 ms                                                         | 20.1 ms: 1.01x slower                                               |
| regex_dna                 | 117 ms                                                          | 118 ms: 1.01x slower                                                |
| logging_simple            | 7.87 us                                                         | 7.95 us: 1.01x slower                                               |
| sqlglot_parse             | 1.05 ms                                                         | 1.06 ms: 1.01x slower                                               |
| sympy_str                 | 215 ms                                                          | 218 ms: 1.01x slower                                                |
| regex_v8                  | 15.6 ms                                                         | 15.8 ms: 1.01x slower                                               |
| sqlite_synth              | 1.97 us                                                         | 1.99 us: 1.01x slower                                               |
| logging_format            | 8.57 us                                                         | 8.70 us: 1.02x slower                                               |
| pickle                    | 8.42 us                                                         | 8.56 us: 1.02x slower                                               |
| docutils                  | 1.82 sec                                                        | 1.85 sec: 1.02x slower                                              |
| regex_compile             | 103 ms                                                          | 105 ms: 1.02x slower                                                |
| sqlglot_transpile         | 1.29 ms                                                         | 1.32 ms: 1.02x slower                                               |
| sqlglot_normalize         | 220 ms                                                          | 224 ms: 1.02x slower                                                |
| sympy_integrate           | 15.2 ms                                                         | 15.5 ms: 1.02x slower                                               |
| mdp                       | 1.67 sec                                                        | 1.72 sec: 1.03x slower                                              |
| sqlglot_optimize          | 42.5 ms                                                         | 43.6 ms: 1.03x slower                                               |
| pickle_list               | 3.40 us                                                         | 3.49 us: 1.03x slower                                               |
| pprint_safe_repr          | 644 ms                                                          | 662 ms: 1.03x slower                                                |
| crypto_pyaes              | 58.2 ms                                                         | 60.0 ms: 1.03x slower                                               |
| sympy_expand              | 375 ms                                                          | 387 ms: 1.03x slower                                                |
| xml_etree_parse           | 109 ms                                                          | 113 ms: 1.04x slower                                                |
| meteor_contest            | 77.0 ms                                                         | 80.3 ms: 1.04x slower                                               |
| comprehensions            | 12.7 us                                                         | 13.4 us: 1.05x slower                                               |
| typing_runtime_protocols  | 136 us                                                          | 143 us: 1.05x slower                                                |
| xml_etree_process         | 45.0 ms                                                         | 47.6 ms: 1.06x slower                                               |
| dulwich_log               | 49.7 ms                                                         | 52.5 ms: 1.06x slower                                               |
| pprint_pformat            | 1.30 sec                                                        | 1.37 sec: 1.06x slower                                              |
| xml_etree_generate        | 62.6 ms                                                         | 66.5 ms: 1.06x slower                                               |
| scimark_lu                | 63.5 ms                                                         | 67.6 ms: 1.06x slower                                               |
| nbody                     | 81.9 ms                                                         | 87.2 ms: 1.07x slower                                               |
| xml_etree_iterparse       | 65.1 ms                                                         | 69.5 ms: 1.07x slower                                               |
| mako                      | 7.31 ms                                                         | 7.83 ms: 1.07x slower                                               |
| float                     | 57.8 ms                                                         | 61.9 ms: 1.07x slower                                               |
| tomli_loads               | 1.73 sec                                                        | 1.87 sec: 1.08x slower                                              |
| chaos                     | 51.2 ms                                                         | 55.4 ms: 1.08x slower                                               |
| spectral_norm             | 71.3 ms                                                         | 77.3 ms: 1.08x slower                                               |
| coroutines                | 15.7 ms                                                         | 17.1 ms: 1.09x slower                                               |
| hexiom                    | 4.64 ms                                                         | 5.05 ms: 1.09x slower                                               |
| generators                | 22.1 ms                                                         | 24.1 ms: 1.09x slower                                               |
| scimark_sparse_mat_mult   | 2.90 ms                                                         | 3.17 ms: 1.09x slower                                               |
| async_tree_io_tg          | 509 ms                                                          | 558 ms: 1.10x slower                                                |
| python_startup            | 24.3 ms                                                         | 26.6 ms: 1.10x slower                                               |
| unpickle_pure_python      | 162 us                                                          | 178 us: 1.10x slower                                                |
| fannkuch                  | 293 ms                                                          | 325 ms: 1.11x slower                                                |
| scimark_fft               | 206 ms                                                          | 230 ms: 1.11x slower                                                |
| deltablue                 | 2.41 ms                                                         | 2.68 ms: 1.11x slower                                               |
| pickle_pure_python        | 238 us                                                          | 265 us: 1.12x slower                                                |
| async_generators          | 274 ms                                                          | 306 ms: 1.12x slower                                                |
| scimark_sor               | 91.8 ms                                                         | 103 ms: 1.12x slower                                                |
| logging_silent            | 61.6 ns                                                         | 69.5 ns: 1.13x slower                                               |
| pyflate                   | 326 ms                                                          | 368 ms: 1.13x slower                                                |
| raytrace                  | 205 ms                                                          | 236 ms: 1.15x slower                                                |
| scimark_monte_carlo       | 50.3 ms                                                         | 58.2 ms: 1.16x slower                                               |
| unpack_sequence           | 42.9 ns                                                         | 49.8 ns: 1.16x slower                                               |
| bench_mp_pool             | 74.3 ms                                                         | 89.0 ms: 1.20x slower                                               |
| json_dumps                | 7.40 ms                                                         | 9.09 ms: 1.23x slower                                               |
| richards                  | 33.8 ms                                                         | 41.5 ms: 1.23x slower                                               |
| richards_super            | 38.0 ms                                                         | 47.3 ms: 1.24x slower                                               |
| gc_traversal              | 1.45 ms                                                         | 1.81 ms: 1.25x slower                                               |
| json                      | 4.27 ms                                                         | 5.97 ms: 1.40x slower                                               |
| create_gc_cycles          | 713 us                                                          | 1.19 ms: 1.67x slower                                               |
| Geometric mean            | (ref)                                                           | 1.01x faster                                                        |

Benchmark hidden because not significant (7): bench_thread_pool, django_template, tornado_http, async_tree_io, async_tree_cpu_io_mixed_tg, asyncio_tcp_ssl, pylint
Ignored benchmarks (2) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: chameleon, flaskblogging
Ignored benchmarks (1) of results/bm-20241015-3.14.0a1-8cdaca8/bm-20241015-pythonperf1_win32-x86-python-v3.14.0a1-3.14.0a1-8cdaca8.json: sphinx

# HPT report

- Reliability score: 99.94% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: unknown